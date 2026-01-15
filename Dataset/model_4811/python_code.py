from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class model_Attribute:

    def __init__(self, minOccurs: int, maxOccurs: int, model_Attribute47: "model_BasicRelationship" = None, model_Attribute50: "model_BasicObject" = None, model_Attribute: "model_BasicObject" = None):
        self.minOccurs = minOccurs
        self.maxOccurs = maxOccurs
        self.model_Attribute47 = model_Attribute47
        self.model_Attribute50 = model_Attribute50
        self.model_Attribute = model_Attribute
        
    @property
    def minOccurs(self) -> int:
        return self.__minOccurs

    @minOccurs.setter
    def minOccurs(self, minOccurs: int):
        self.__minOccurs = minOccurs

    @property
    def maxOccurs(self) -> int:
        return self.__maxOccurs

    @maxOccurs.setter
    def maxOccurs(self, maxOccurs: int):
        self.__maxOccurs = maxOccurs

    @property
    def model_Attribute(self):
        return self.__model_Attribute

    @model_Attribute.setter
    def model_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Attribute__model_Attribute", None)
        self.__model_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicObject"):
                opp_val = getattr(old_value, "model_BasicObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicObject"):
                opp_val = getattr(value, "model_BasicObject", None)
                if opp_val is None:
                    setattr(value, "model_BasicObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Attribute47(self):
        return self.__model_Attribute47

    @model_Attribute47.setter
    def model_Attribute47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Attribute__model_Attribute47", None)
        self.__model_Attribute47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicRelationship48"):
                opp_val = getattr(old_value, "model_BasicRelationship48", None)
                if opp_val == self:
                    setattr(old_value, "model_BasicRelationship48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicRelationship48"):
                opp_val = getattr(value, "model_BasicRelationship48", None)
                setattr(value, "model_BasicRelationship48", self)

    @property
    def model_Attribute50(self):
        return self.__model_Attribute50

    @model_Attribute50.setter
    def model_Attribute50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Attribute__model_Attribute50", None)
        self.__model_Attribute50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BasicObject51"):
                opp_val = getattr(old_value, "model_BasicObject51", None)
                if opp_val == self:
                    setattr(old_value, "model_BasicObject51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BasicObject51"):
                opp_val = getattr(value, "model_BasicObject51", None)
                setattr(value, "model_BasicObject51", self)

class BasicObject:

    pass
class model_BasicRelationship(BasicObject):

    pass
class DiagramModelConnection:

    pass
class model_DiagramModelZentaConnection(DiagramModelConnection):

    def __init__(self, diagConnections: "model_BasicRelationship" = None, DiagramModelZentaConnection: "model_BasicRelationship" = None):
        self.diagConnections = diagConnections
        self.DiagramModelZentaConnection = DiagramModelZentaConnection
        
    @property
    def DiagramModelZentaConnection(self):
        return self.__DiagramModelZentaConnection

    @DiagramModelZentaConnection.setter
    def DiagramModelZentaConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelZentaConnection__DiagramModelZentaConnection", None)
        self.__DiagramModelZentaConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationship"):
                opp_val = getattr(old_value, "relationship", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationship"):
                opp_val = getattr(value, "relationship", None)
                if opp_val is None:
                    setattr(value, "relationship", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagConnections(self):
        return self.__diagConnections

    @diagConnections.setter
    def diagConnections(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelZentaConnection__diagConnections", None)
        self.__diagConnections = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicRelationship"):
                opp_val = getattr(old_value, "BasicRelationship", None)
                if opp_val == self:
                    setattr(old_value, "BasicRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicRelationship"):
                opp_val = getattr(value, "BasicRelationship", None)
                setattr(value, "BasicRelationship", self)

    def removeRelationshipFromModel(self):
        # TODO: Implement removeRelationshipFromModel method
        pass

    def addRelationshipToModel(self, parent: str):
        # TODO: Implement addRelationshipToModel method
        pass

class DiagramModel:

    pass
class model_SketchModel(DiagramModel):

    def __init__(self, background: int):
        self.background = background
        
    @property
    def background(self) -> int:
        return self.__background

    @background.setter
    def background(self, background: int):
        self.__background = background

class model_ZentaDiagramModel(DiagramModel):

    def __init__(self, viewpoint: int):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> int:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: int):
        self.__viewpoint = viewpoint

class model_Lockable(ABC):

    def __init__(self, locked: bool):
        self.locked = locked
        
    @property
    def locked(self) -> bool:
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked

class model_Template:

    def __init__(self, path: str, Template: "model_Metamodel" = None, template: set["model_BasicObject"] = None, Template40: "model_BasicObject" = None, templates: "model_Metamodel" = None, model_Template: "model_DiagramModel" = None):
        self.path = path
        self.Template = Template
        self.template = template if template is not None else set()
        self.Template40 = Template40
        self.templates = templates
        self.model_Template = model_Template
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def Template(self):
        return self.__Template

    @Template.setter
    def Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Template__Template", None)
        self.__Template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel"):
                opp_val = getattr(old_value, "metamodel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel"):
                opp_val = getattr(value, "metamodel", None)
                if opp_val is None:
                    setattr(value, "metamodel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Template(self):
        return self.__model_Template

    @model_Template.setter
    def model_Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Template__model_Template", None)
        self.__model_Template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModel30"):
                opp_val = getattr(old_value, "model_DiagramModel30", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModel30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModel30"):
                opp_val = getattr(value, "model_DiagramModel30", None)
                setattr(value, "model_DiagramModel30", self)

    @property
    def Template40(self):
        return self.__Template40

    @Template40.setter
    def Template40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Template__Template40", None)
        self.__Template40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classes"):
                opp_val = getattr(old_value, "classes", None)
                if opp_val == self:
                    setattr(old_value, "classes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classes"):
                opp_val = getattr(value, "classes", None)
                setattr(value, "classes", self)

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Template__template", None)
        self.__template = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BasicObject"):
                    opp_val = getattr(item, "BasicObject", None)
                    
                    if opp_val == self:
                        setattr(item, "BasicObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BasicObject"):
                    opp_val = getattr(item, "BasicObject", None)
                    
                    setattr(item, "BasicObject", self)
                    

    @property
    def templates(self):
        return self.__templates

    @templates.setter
    def templates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Template__templates", None)
        self.__templates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Metamodel"):
                opp_val = getattr(old_value, "Metamodel", None)
                if opp_val == self:
                    setattr(old_value, "Metamodel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Metamodel"):
                opp_val = getattr(value, "Metamodel", None)
                setattr(value, "Metamodel", self)

class model_Metamodel:

    pass
class Folder:

    pass
class DiagramModelImageProvider:

    pass
class BorderObject:

    pass
class TextContent:

    pass
class DiagramModelContainer:

    pass
class model_DiagramModelImageProvider(ABC):

    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        
    @property
    def imagePath(self) -> str:
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath

class model_BorderObject(ABC):

    def __init__(self, borderColor: str):
        self.borderColor = borderColor
        
    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

class model_FontAttribute(ABC):

    def __init__(self, font: str, fontColor: str, textAlignment: int, textPosition: int):
        self.font = font
        self.fontColor = fontColor
        self.textAlignment = textAlignment
        self.textPosition = textPosition
        
    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def fontColor(self) -> str:
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor

    @property
    def textPosition(self) -> int:
        return self.__textPosition

    @textPosition.setter
    def textPosition(self, textPosition: int):
        self.__textPosition = textPosition

    @property
    def textAlignment(self) -> int:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: int):
        self.__textAlignment = textAlignment

    def getDefaultTextAlignment(self) -> int:
        # TODO: Implement getDefaultTextAlignment method
        pass

class Cloneable:

    pass
class model_DiagramModelBendpoint(Cloneable):

    def __init__(self, startX: int, startY: int, endX: int, endY: int, model_DiagramModelBendpoint: "model_DiagramModelConnection" = None):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.model_DiagramModelBendpoint = model_DiagramModelBendpoint
        
    @property
    def endY(self) -> int:
        return self.__endY

    @endY.setter
    def endY(self, endY: int):
        self.__endY = endY

    @property
    def endX(self) -> int:
        return self.__endX

    @endX.setter
    def endX(self, endX: int):
        self.__endX = endX

    @property
    def startX(self) -> int:
        return self.__startX

    @startX.setter
    def startX(self, startX: int):
        self.__startX = startX

    @property
    def startY(self) -> int:
        return self.__startY

    @startY.setter
    def startY(self, startY: int):
        self.__startY = startY

    @property
    def model_DiagramModelBendpoint(self):
        return self.__model_DiagramModelBendpoint

    @model_DiagramModelBendpoint.setter
    def model_DiagramModelBendpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelBendpoint__model_DiagramModelBendpoint", None)
        self.__model_DiagramModelBendpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection23"):
                opp_val = getattr(old_value, "model_DiagramModelConnection23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection23"):
                opp_val = getattr(value, "model_DiagramModelConnection23", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelConnection23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JunctionElement:

    pass
class model_OrJunction(JunctionElement):

    pass
class model_AndJunction(JunctionElement):

    pass
class model_Junction(JunctionElement):

    pass
class ZentaElement:

    pass
class model_BasicObject(ZentaElement):

    pass
class model_InterfaceElement(ZentaElement):

    def __init__(self, interfaceType: int):
        self.interfaceType = interfaceType
        
    @property
    def interfaceType(self) -> int:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: int):
        self.__interfaceType = interfaceType

class model_JunctionElement(ZentaElement):

    pass
class model_Bounds:

    def __init__(self, x: int, y: int, width: int, height: int, model_Bounds: "model_DiagramModelObject" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.model_Bounds = model_Bounds
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def model_Bounds(self):
        return self.__model_Bounds

    @model_Bounds.setter
    def model_Bounds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Bounds__model_Bounds", None)
        self.__model_Bounds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject10"):
                opp_val = getattr(old_value, "model_DiagramModelObject10", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject10"):
                opp_val = getattr(value, "model_DiagramModelObject10", None)
                setattr(value, "model_DiagramModelObject10", self)

    def getCopy(self) -> str:
        # TODO: Implement getCopy method
        pass

class FontAttribute:

    pass
class DiagramModelObject:

    pass
class model_DiagramModelImage(DiagramModelImageProvider, DiagramModelObject, BorderObject):

    pass
class model_DiagramModelNote(TextContent, DiagramModelObject):

    pass
class model_DiagramModelZentaObject(DiagramModelContainer, DiagramModelObject):

    def __init__(self, type: int, diagObjects: "model_ZentaElement" = None, DiagramModelZentaObject: "model_ZentaElement" = None):
        self.type = type
        self.diagObjects = diagObjects
        self.DiagramModelZentaObject = DiagramModelZentaObject
        
    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def DiagramModelZentaObject(self):
        return self.__DiagramModelZentaObject

    @DiagramModelZentaObject.setter
    def DiagramModelZentaObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelZentaObject__DiagramModelZentaObject", None)
        self.__DiagramModelZentaObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "zentaElement"):
                opp_val = getattr(old_value, "zentaElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "zentaElement"):
                opp_val = getattr(value, "zentaElement", None)
                if opp_val is None:
                    setattr(value, "zentaElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagObjects(self):
        return self.__diagObjects

    @diagObjects.setter
    def diagObjects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelZentaObject__diagObjects", None)
        self.__diagObjects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ZentaElement"):
                opp_val = getattr(old_value, "ZentaElement", None)
                if opp_val == self:
                    setattr(old_value, "ZentaElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ZentaElement"):
                opp_val = getattr(value, "ZentaElement", None)
                setattr(value, "ZentaElement", self)

    def removeZentaElementFromModel(self):
        # TODO: Implement removeZentaElementFromModel method
        pass

    def addZentaElementToModel(self, parent: str):
        # TODO: Implement addZentaElementToModel method
        pass

class model_DiagramModelReference(DiagramModelObject):

    pass
class DiagramModelComponent:

    pass
class model_DiagramModelObject(FontAttribute, DiagramModelComponent):

    def __init__(self, fillColor: str, elementShape: str, model_DiagramModelObject: "model_DiagramModelContainer" = None, model_DiagramModelObject10: "model_Bounds" = None, model_DiagramModelObject12: set["model_DiagramModelConnection"] = None, model_DiagramModelObject21: "model_DiagramModelConnection" = None, model_DiagramModelObject14: set["model_DiagramModelConnection"] = None, model_DiagramModelObject18: "model_DiagramModelConnection" = None):
        self.fillColor = fillColor
        self.elementShape = elementShape
        self.model_DiagramModelObject = model_DiagramModelObject
        self.model_DiagramModelObject10 = model_DiagramModelObject10
        self.model_DiagramModelObject12 = model_DiagramModelObject12 if model_DiagramModelObject12 is not None else set()
        self.model_DiagramModelObject21 = model_DiagramModelObject21
        self.model_DiagramModelObject14 = model_DiagramModelObject14 if model_DiagramModelObject14 is not None else set()
        self.model_DiagramModelObject18 = model_DiagramModelObject18
        
    @property
    def elementShape(self) -> str:
        return self.__elementShape

    @elementShape.setter
    def elementShape(self, elementShape: str):
        self.__elementShape = elementShape

    @property
    def fillColor(self) -> str:
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor

    @property
    def model_DiagramModelObject14(self):
        return self.__model_DiagramModelObject14

    @model_DiagramModelObject14.setter
    def model_DiagramModelObject14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject14", None)
        self.__model_DiagramModelObject14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelConnection15"):
                    opp_val = getattr(item, "model_DiagramModelConnection15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelConnection15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelConnection15"):
                    opp_val = getattr(item, "model_DiagramModelConnection15", None)
                    
                    setattr(item, "model_DiagramModelConnection15", self)
                    

    @property
    def model_DiagramModelObject10(self):
        return self.__model_DiagramModelObject10

    @model_DiagramModelObject10.setter
    def model_DiagramModelObject10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject10", None)
        self.__model_DiagramModelObject10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Bounds"):
                opp_val = getattr(old_value, "model_Bounds", None)
                if opp_val == self:
                    setattr(old_value, "model_Bounds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Bounds"):
                opp_val = getattr(value, "model_Bounds", None)
                setattr(value, "model_Bounds", self)

    @property
    def model_DiagramModelObject12(self):
        return self.__model_DiagramModelObject12

    @model_DiagramModelObject12.setter
    def model_DiagramModelObject12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject12", None)
        self.__model_DiagramModelObject12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelConnection"):
                    opp_val = getattr(item, "model_DiagramModelConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelConnection"):
                    opp_val = getattr(item, "model_DiagramModelConnection", None)
                    
                    setattr(item, "model_DiagramModelConnection", self)
                    

    @property
    def model_DiagramModelObject21(self):
        return self.__model_DiagramModelObject21

    @model_DiagramModelObject21.setter
    def model_DiagramModelObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject21", None)
        self.__model_DiagramModelObject21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection20"):
                opp_val = getattr(old_value, "model_DiagramModelConnection20", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection20"):
                opp_val = getattr(value, "model_DiagramModelConnection20", None)
                setattr(value, "model_DiagramModelConnection20", self)

    @property
    def model_DiagramModelObject(self):
        return self.__model_DiagramModelObject

    @model_DiagramModelObject.setter
    def model_DiagramModelObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject", None)
        self.__model_DiagramModelObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelContainer"):
                opp_val = getattr(old_value, "model_DiagramModelContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelContainer"):
                opp_val = getattr(value, "model_DiagramModelContainer", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelObject18(self):
        return self.__model_DiagramModelObject18

    @model_DiagramModelObject18.setter
    def model_DiagramModelObject18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject18", None)
        self.__model_DiagramModelObject18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection17"):
                opp_val = getattr(old_value, "model_DiagramModelConnection17", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection17"):
                opp_val = getattr(value, "model_DiagramModelConnection17", None)
                setattr(value, "model_DiagramModelConnection17", self)

    def setBounds(self, width: int, height: int, y: int, x: int):
        # TODO: Implement setBounds method
        pass

    def addConnection(self, connection: str):
        # TODO: Implement addConnection method
        pass

    def removeConnection(self, connection: str):
        # TODO: Implement removeConnection method
        pass

class model_DiagramModelContainer(DiagramModelComponent):

    pass
class model_TextContent(ABC):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class model_Nameable(ABC):

    def __init__(self, name: str, model_Nameable: "model_Folder" = None):
        self.name = name
        self.model_Nameable = model_Nameable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Nameable(self):
        return self.__model_Nameable

    @model_Nameable.setter
    def model_Nameable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Nameable__model_Nameable", None)
        self.__model_Nameable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Folder4"):
                opp_val = getattr(old_value, "model_Folder4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Folder4"):
                opp_val = getattr(value, "model_Folder4", None)
                if opp_val is None:
                    setattr(value, "model_Folder4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Properties(ABC):

    pass
class model_Property:

    def __init__(self, key: str, value: str, generated: bool, model_Property: "model_Properties" = None):
        self.key = key
        self.value = value
        self.generated = generated
        self.model_Property = model_Property
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def generated(self) -> bool:
        return self.__generated

    @generated.setter
    def generated(self, generated: bool):
        self.__generated = generated

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_Property(self):
        return self.__model_Property

    @model_Property.setter
    def model_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Property__model_Property", None)
        self.__model_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Properties"):
                opp_val = getattr(old_value, "model_Properties", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Properties"):
                opp_val = getattr(value, "model_Properties", None)
                if opp_val is None:
                    setattr(value, "model_Properties", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Nameable:

    pass
class model_Identifier(Nameable):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Properties:

    pass
class model_SketchModelSticky(DiagramModelContainer, Properties, TextContent, DiagramModelObject):

    pass
class Documentable:

    pass
class model_DiagramModelGroup(DiagramModelContainer, Documentable, Properties, DiagramModelObject):

    pass
class model_SketchModelActor(Properties, Documentable, DiagramModelObject):

    pass
class model_DiagramModelConnection(Properties, Documentable, FontAttribute, DiagramModelComponent):

    def __init__(self, lineDecoration: str, type: int, text: str, model_DiagramModelConnection: "model_DiagramModelObject" = None, model_DiagramModelConnection20: "model_DiagramModelObject" = None, model_DiagramModelConnection23: set["model_DiagramModelBendpoint"] = None, model_DiagramModelConnection15: "model_DiagramModelObject" = None, model_DiagramModelConnection17: "model_DiagramModelObject" = None):
        self.lineDecoration = lineDecoration
        self.type = type
        self.text = text
        self.model_DiagramModelConnection = model_DiagramModelConnection
        self.model_DiagramModelConnection20 = model_DiagramModelConnection20
        self.model_DiagramModelConnection23 = model_DiagramModelConnection23 if model_DiagramModelConnection23 is not None else set()
        self.model_DiagramModelConnection15 = model_DiagramModelConnection15
        self.model_DiagramModelConnection17 = model_DiagramModelConnection17
        
    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def lineDecoration(self) -> str:
        return self.__lineDecoration

    @lineDecoration.setter
    def lineDecoration(self, lineDecoration: str):
        self.__lineDecoration = lineDecoration

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def model_DiagramModelConnection17(self):
        return self.__model_DiagramModelConnection17

    @model_DiagramModelConnection17.setter
    def model_DiagramModelConnection17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection17", None)
        self.__model_DiagramModelConnection17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject18"):
                opp_val = getattr(old_value, "model_DiagramModelObject18", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject18"):
                opp_val = getattr(value, "model_DiagramModelObject18", None)
                setattr(value, "model_DiagramModelObject18", self)

    @property
    def model_DiagramModelConnection15(self):
        return self.__model_DiagramModelConnection15

    @model_DiagramModelConnection15.setter
    def model_DiagramModelConnection15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection15", None)
        self.__model_DiagramModelConnection15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject14"):
                opp_val = getattr(old_value, "model_DiagramModelObject14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject14"):
                opp_val = getattr(value, "model_DiagramModelObject14", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelConnection23(self):
        return self.__model_DiagramModelConnection23

    @model_DiagramModelConnection23.setter
    def model_DiagramModelConnection23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection23", None)
        self.__model_DiagramModelConnection23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelBendpoint"):
                    opp_val = getattr(item, "model_DiagramModelBendpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelBendpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelBendpoint"):
                    opp_val = getattr(item, "model_DiagramModelBendpoint", None)
                    
                    setattr(item, "model_DiagramModelBendpoint", self)
                    

    @property
    def model_DiagramModelConnection20(self):
        return self.__model_DiagramModelConnection20

    @model_DiagramModelConnection20.setter
    def model_DiagramModelConnection20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection20", None)
        self.__model_DiagramModelConnection20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject21"):
                opp_val = getattr(old_value, "model_DiagramModelObject21", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject21"):
                opp_val = getattr(value, "model_DiagramModelObject21", None)
                setattr(value, "model_DiagramModelObject21", self)

    @property
    def model_DiagramModelConnection(self):
        return self.__model_DiagramModelConnection

    @model_DiagramModelConnection.setter
    def model_DiagramModelConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection", None)
        self.__model_DiagramModelConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject12"):
                opp_val = getattr(old_value, "model_DiagramModelObject12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject12"):
                opp_val = getattr(value, "model_DiagramModelObject12", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def disconnect(self):
        # TODO: Implement disconnect method
        pass

    def connect(self, source: DiagramModelObject, target: DiagramModelObject):
        # TODO: Implement connect method
        pass

    def reconnect(self):
        # TODO: Implement reconnect method
        pass

class Identifier:

    pass
class FolderContainer:

    pass
class ZentaModelElement:

    pass
class model_ZentaElement(Identifier, ZentaModelElement, Documentable, Cloneable, Nameable, Properties):

    pass
class model_DiagramModel(DiagramModelContainer, Properties, ZentaModelElement, Documentable):

    def __init__(self, connectionRouterType: int, model_DiagramModel8: "model_DiagramModelReference" = None, model_DiagramModel: "model_DiagramModelComponent" = None, model_DiagramModel30: "model_Template" = None):
        self.connectionRouterType = connectionRouterType
        self.model_DiagramModel8 = model_DiagramModel8
        self.model_DiagramModel = model_DiagramModel
        self.model_DiagramModel30 = model_DiagramModel30
        
    @property
    def connectionRouterType(self) -> int:
        return self.__connectionRouterType

    @connectionRouterType.setter
    def connectionRouterType(self, connectionRouterType: int):
        self.__connectionRouterType = connectionRouterType

    @property
    def model_DiagramModel30(self):
        return self.__model_DiagramModel30

    @model_DiagramModel30.setter
    def model_DiagramModel30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModel__model_DiagramModel30", None)
        self.__model_DiagramModel30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Template"):
                opp_val = getattr(old_value, "model_Template", None)
                if opp_val == self:
                    setattr(old_value, "model_Template", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Template"):
                opp_val = getattr(value, "model_Template", None)
                setattr(value, "model_Template", self)

    @property
    def model_DiagramModel(self):
        return self.__model_DiagramModel

    @model_DiagramModel.setter
    def model_DiagramModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModel__model_DiagramModel", None)
        self.__model_DiagramModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelComponent"):
                opp_val = getattr(old_value, "model_DiagramModelComponent", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelComponent"):
                opp_val = getattr(value, "model_DiagramModelComponent", None)
                setattr(value, "model_DiagramModelComponent", self)

    @property
    def model_DiagramModel8(self):
        return self.__model_DiagramModel8

    @model_DiagramModel8.setter
    def model_DiagramModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModel__model_DiagramModel8", None)
        self.__model_DiagramModel8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelReference"):
                opp_val = getattr(old_value, "model_DiagramModelReference", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelReference"):
                opp_val = getattr(value, "model_DiagramModelReference", None)
                setattr(value, "model_DiagramModelReference", self)

class model_ZentaModel(Identifier, Documentable, ZentaModelElement, FolderContainer, Nameable, Folder, Properties):

    def __init__(self, file: str, version: str, model_ZentaModel: "model_ZentaModelElement" = None):
        self.file = file
        self.version = version
        self.model_ZentaModel = model_ZentaModel
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def model_ZentaModel(self):
        return self.__model_ZentaModel

    @model_ZentaModel.setter
    def model_ZentaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ZentaModel__model_ZentaModel", None)
        self.__model_ZentaModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ZentaModelElement"):
                opp_val = getattr(old_value, "model_ZentaModelElement", None)
                if opp_val == self:
                    setattr(old_value, "model_ZentaModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ZentaModelElement"):
                opp_val = getattr(value, "model_ZentaModelElement", None)
                setattr(value, "model_ZentaModelElement", self)

    def getDiagramModels(self) -> DiagramModel:
        # TODO: Implement getDiagramModels method
        pass

    def getDefaultFolderForElement(self, element: str) -> Folder:
        # TODO: Implement getDefaultFolderForElement method
        pass

    def getDefaultDiagramModel(self) -> DiagramModel:
        # TODO: Implement getDefaultDiagramModel method
        pass

class Adapter:

    pass
class model_DiagramModelComponent(Nameable, Adapter, Identifier, Cloneable):

    def __init__(self, lineWidth: int, lineColor: str, model_DiagramModelComponent: "model_DiagramModel" = None):
        self.lineWidth = lineWidth
        self.lineColor = lineColor
        self.model_DiagramModelComponent = model_DiagramModelComponent
        
    @property
    def lineColor(self) -> str:
        return self.__lineColor

    @lineColor.setter
    def lineColor(self, lineColor: str):
        self.__lineColor = lineColor

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def model_DiagramModelComponent(self):
        return self.__model_DiagramModelComponent

    @model_DiagramModelComponent.setter
    def model_DiagramModelComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelComponent__model_DiagramModelComponent", None)
        self.__model_DiagramModelComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModel"):
                opp_val = getattr(old_value, "model_DiagramModel", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModel"):
                opp_val = getattr(value, "model_DiagramModel", None)
                setattr(value, "model_DiagramModel", self)

class model_ZentaModelElement(Adapter):

    pass
class model_Folder(Identifier, Documentable, ZentaModelElement, FolderContainer, Nameable, Properties):

    pass
class model_FolderContainer(ABC):

    pass
class model_Cloneable(ABC):

    def __init__(self):
        
    def getCopy(self) -> str:
        # TODO: Implement getCopy method
        pass

class model_Documentable(ABC):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

class model_Adapter(ABC):

    def __init__(self):
        
    def getAdapter(self, adapter: str) -> str:
        # TODO: Implement getAdapter method
        pass

    def setAdapter(self, object: str, adapter: str):
        # TODO: Implement setAdapter method
        pass
