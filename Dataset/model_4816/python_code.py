from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FolderType(Enum):
    user = "user"
    business = "business"
    application = "application"
    technology = "technology"
    connectors = "connectors"
    relations = "relations"
    diagrams = "diagrams"
    derived = "derived"
    motivation = "motivation"
    implementation_migration = "implementation_migration"


############################################
# Definition of Classes
############################################

class DiagramModelConnection:

    pass
class model_DiagramModelArchimateConnection(DiagramModelConnection):

    def __init__(self, model_DiagramModelArchimateConnection: "model_Relationship" = None):
        self.model_DiagramModelArchimateConnection = model_DiagramModelArchimateConnection
        
        pass
    @property
    def model_DiagramModelArchimateConnection(self):
        return self.__model_DiagramModelArchimateConnection

    @model_DiagramModelArchimateConnection.setter
    def model_DiagramModelArchimateConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelArchimateConnection__model_DiagramModelArchimateConnection", None)
        self.__model_DiagramModelArchimateConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Relationship31"):
                opp_val = getattr(old_value, "model_Relationship31", None)
                if opp_val == self:
                    setattr(old_value, "model_Relationship31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Relationship31"):
                opp_val = getattr(value, "model_Relationship31", None)
                setattr(value, "model_Relationship31", self)

    def addRelationshipToModel(self, model_parent):
        # TODO: Implement addRelationshipToModel method
        pass

    def removeRelationshipFromModel(self):
        # TODO: Implement removeRelationshipFromModel method
        pass

class DiagramModel:

    pass
class model_SketchModel(DiagramModel):

    def __init__(self, background: int):
        self.background = background
        
        pass
    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: int):
        self.__background = background


class model_ArchimateDiagramModel(DiagramModel):

    def __init__(self, viewpoint: int):
        self.viewpoint = viewpoint
        
        pass
    @property
    def viewpoint(self):
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: int):
        self.__viewpoint = viewpoint


class model_Lockable(ABC):

    def __init__(self, locked: bool):
        self.locked = locked
        
        pass
    @property
    def locked(self):
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked


class model_DiagramModelImageProvider(ABC):

    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        
        pass
    @property
    def imagePath(self):
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath


class model_BorderObject(ABC):

    def __init__(self, borderColor: str):
        self.borderColor = borderColor
        
        pass
    @property
    def borderColor(self):
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
        
        pass
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font


    @property
    def textPosition(self):
        return self.__textPosition

    @textPosition.setter
    def textPosition(self, textPosition: int):
        self.__textPosition = textPosition


    @property
    def textAlignment(self):
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: int):
        self.__textAlignment = textAlignment


    @property
    def fontColor(self):
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor


    def getDefaultTextAlignment(self) :
        # TODO: Implement getDefaultTextAlignment method
        pass

class DiagramModelImageProvider:

    pass
class BorderObject:

    pass
class TextContent:

    pass
class model_Bounds:

    def __init__(self, x: int, y: int, width: int, height: int, model_Bounds: "model_DiagramModelObject" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.model_Bounds = model_Bounds
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


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
            if hasattr(old_value, "model_DiagramModelObject14"):
                opp_val = getattr(old_value, "model_DiagramModelObject14", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject14"):
                opp_val = getattr(value, "model_DiagramModelObject14", None)
                setattr(value, "model_DiagramModelObject14", self)

    def getCopy(self) :
        # TODO: Implement getCopy method
        pass

class FontAttribute:

    pass
class DiagramModelObject:

    pass
class model_DiagramModelNote(DiagramModelObject, TextContent):

    pass
class model_DiagramModelImage(BorderObject, DiagramModelObject, DiagramModelImageProvider):

    pass
class model_DiagramModelReference(DiagramModelObject):

    pass
class DiagramModelComponent:

    pass
class model_DiagramModelObject(FontAttribute, DiagramModelComponent):

    def __init__(self, fillColor: str, model_DiagramModelObject: "model_DiagramModelContainer" = None, model_DiagramModelObject14: "model_Bounds" = None, model_DiagramModelObject16: set["model_DiagramModelConnection"] = None, model_DiagramModelObject18: set["model_DiagramModelConnection"] = None, model_DiagramModelObject22: "model_DiagramModelConnection" = None, model_DiagramModelObject25: "model_DiagramModelConnection" = None):
        self.fillColor = fillColor
        self.model_DiagramModelObject = model_DiagramModelObject
        self.model_DiagramModelObject14 = model_DiagramModelObject14
        self.model_DiagramModelObject16 = model_DiagramModelObject16 if model_DiagramModelObject16 is not None else set()
        self.model_DiagramModelObject18 = model_DiagramModelObject18 if model_DiagramModelObject18 is not None else set()
        self.model_DiagramModelObject22 = model_DiagramModelObject22
        self.model_DiagramModelObject25 = model_DiagramModelObject25
        
        pass
    @property
    def fillColor(self):
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor


    @property
    def model_DiagramModelObject18(self):
        return self.__model_DiagramModelObject18

    @model_DiagramModelObject18.setter
    def model_DiagramModelObject18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject18", None)
        self.__model_DiagramModelObject18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelConnection19"):
                    opp_val = getattr(item, "model_DiagramModelConnection19", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelConnection19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelConnection19"):
                    opp_val = getattr(item, "model_DiagramModelConnection19", None)
                    
                    setattr(item, "model_DiagramModelConnection19", self)
                    

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
    def model_DiagramModelObject25(self):
        return self.__model_DiagramModelObject25

    @model_DiagramModelObject25.setter
    def model_DiagramModelObject25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject25", None)
        self.__model_DiagramModelObject25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection24"):
                opp_val = getattr(old_value, "model_DiagramModelConnection24", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection24"):
                opp_val = getattr(value, "model_DiagramModelConnection24", None)
                setattr(value, "model_DiagramModelConnection24", self)

    @property
    def model_DiagramModelObject16(self):
        return self.__model_DiagramModelObject16

    @model_DiagramModelObject16.setter
    def model_DiagramModelObject16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject16", None)
        self.__model_DiagramModelObject16 = value if value is not None else set()
        
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
    def model_DiagramModelObject14(self):
        return self.__model_DiagramModelObject14

    @model_DiagramModelObject14.setter
    def model_DiagramModelObject14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject14", None)
        self.__model_DiagramModelObject14 = value
        
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
    def model_DiagramModelObject22(self):
        return self.__model_DiagramModelObject22

    @model_DiagramModelObject22.setter
    def model_DiagramModelObject22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject22", None)
        self.__model_DiagramModelObject22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection21"):
                opp_val = getattr(old_value, "model_DiagramModelConnection21", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection21"):
                opp_val = getattr(value, "model_DiagramModelConnection21", None)
                setattr(value, "model_DiagramModelConnection21", self)

    def setBounds(self, model_y, model_height, model_x, model_width):
        # TODO: Implement setBounds method
        pass

    def addConnection(self, model_connection):
        # TODO: Implement addConnection method
        pass

    def removeConnection(self, model_connection):
        # TODO: Implement removeConnection method
        pass

class model_DiagramModelContainer(DiagramModelComponent):

    pass
class ImplementationMigrationElement:

    pass
class model_Gap(ImplementationMigrationElement):

    pass
class model_Deliverable(ImplementationMigrationElement):

    pass
class model_Plateau(ImplementationMigrationElement):

    pass
class model_WorkPackage(ImplementationMigrationElement):

    pass
class DiagramModelContainer:

    pass
class model_DiagramModelArchimateObject(DiagramModelContainer, DiagramModelObject):

    def __init__(self, type: int, model_DiagramModelArchimateObject: "model_ArchimateElement" = None):
        self.type = type
        self.model_DiagramModelArchimateObject = model_DiagramModelArchimateObject
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type


    @property
    def model_DiagramModelArchimateObject(self):
        return self.__model_DiagramModelArchimateObject

    @model_DiagramModelArchimateObject.setter
    def model_DiagramModelArchimateObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelArchimateObject__model_DiagramModelArchimateObject", None)
        self.__model_DiagramModelArchimateObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ArchimateElement29"):
                opp_val = getattr(old_value, "model_ArchimateElement29", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateElement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateElement29"):
                opp_val = getattr(value, "model_ArchimateElement29", None)
                setattr(value, "model_ArchimateElement29", self)

    def addArchimateElementToModel(self, model_parent):
        # TODO: Implement addArchimateElementToModel method
        pass

    def removeArchimateElementFromModel(self):
        # TODO: Implement removeArchimateElementFromModel method
        pass

class TechnologyLayerElement:

    pass
class model_InfrastructureService(TechnologyLayerElement):

    pass
class model_Network(TechnologyLayerElement):

    pass
class model_SystemSoftware(TechnologyLayerElement):

    pass
class model_Node(TechnologyLayerElement):

    pass
class model_InfrastructureFunction(TechnologyLayerElement):

    pass
class model_CommunicationPath(TechnologyLayerElement):

    pass
class model_Device(TechnologyLayerElement):

    pass
class model_Artifact(TechnologyLayerElement):

    pass
class MotivationElement:

    pass
class model_Goal(MotivationElement):

    pass
class model_Constraint(MotivationElement):

    pass
class model_Driver(MotivationElement):

    pass
class model_Principle(MotivationElement):

    pass
class model_Assessment(MotivationElement):

    pass
class model_Requirement(MotivationElement):

    pass
class model_Stakeholder(MotivationElement):

    pass
class ApplicationLayerElement:

    pass
class model_ApplicationComponent(ApplicationLayerElement):

    pass
class model_ApplicationFunction(ApplicationLayerElement):

    pass
class model_DataObject(ApplicationLayerElement):

    pass
class model_ApplicationService(ApplicationLayerElement):

    pass
class model_ApplicationCollaboration(ApplicationLayerElement):

    pass
class model_ApplicationInteraction(ApplicationLayerElement):

    pass
class InterfaceElement:

    pass
class model_InfrastructureInterface(TechnologyLayerElement, InterfaceElement):

    pass
class model_ApplicationInterface(ApplicationLayerElement, InterfaceElement):

    pass
class BusinessLayerElement:

    pass
class model_BusinessInteraction(BusinessLayerElement):

    pass
class model_BusinessRole(BusinessLayerElement):

    pass
class model_Location(BusinessLayerElement):

    pass
class model_BusinessFunction(BusinessLayerElement):

    pass
class model_Value(BusinessLayerElement):

    pass
class model_Contract(BusinessLayerElement):

    pass
class model_Product(BusinessLayerElement):

    pass
class model_BusinessCollaboration(BusinessLayerElement):

    pass
class model_BusinessInterface(BusinessLayerElement, InterfaceElement):

    pass
class model_BusinessEvent(BusinessLayerElement):

    pass
class model_BusinessActor(BusinessLayerElement):

    pass
class model_BusinessService(BusinessLayerElement):

    pass
class model_Representation(BusinessLayerElement):

    pass
class model_BusinessActivity(BusinessLayerElement):

    pass
class model_BusinessProcess(BusinessLayerElement):

    pass
class model_BusinessObject(BusinessLayerElement):

    pass
class model_Meaning(BusinessLayerElement):

    pass
class Relationship:

    pass
class model_RealisationRelationship(Relationship):

    pass
class model_CompositionRelationship(Relationship):

    pass
class model_InfluenceRelationship(Relationship):

    pass
class model_AssignmentRelationship(Relationship):

    pass
class model_FlowRelationship(Relationship):

    pass
class model_AggregationRelationship(Relationship):

    pass
class model_UsedByRelationship(Relationship):

    pass
class model_TriggeringRelationship(Relationship):

    pass
class model_SpecialisationRelationship(Relationship):

    pass
class model_AccessRelationship(Relationship):

    def __init__(self, accessType: int):
        self.accessType = accessType
        
        pass
    @property
    def accessType(self):
        return self.__accessType

    @accessType.setter
    def accessType(self, accessType: int):
        self.__accessType = accessType


class model_AssociationRelationship(Relationship):

    pass
class Documentable:

    pass
class JunctionElement:

    pass
class model_OrJunction(JunctionElement):

    pass
class model_AndJunction(JunctionElement):

    pass
class model_Junction(JunctionElement):

    pass
class ArchimateElement:

    pass
class model_ApplicationLayerElement(ArchimateElement):

    pass
class model_BusinessLayerElement(ArchimateElement):

    pass
class model_TechnologyLayerElement(ArchimateElement):

    pass
class model_ImplementationMigrationElement(ArchimateElement):

    pass
class model_MotivationElement(ArchimateElement):

    pass
class model_Relationship(ArchimateElement):

    pass
class model_InterfaceElement(ArchimateElement):

    def __init__(self, interfaceType: int):
        self.interfaceType = interfaceType
        
        pass
    @property
    def interfaceType(self):
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: int):
        self.__interfaceType = interfaceType


class model_JunctionElement(ArchimateElement):

    pass
class Cloneable:

    pass
class model_DiagramModelBendpoint(Cloneable):

    def __init__(self, endY: int, startX: int, startY: int, endX: int, model_DiagramModelBendpoint: "model_DiagramModelConnection" = None):
        self.endY = endY
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.model_DiagramModelBendpoint = model_DiagramModelBendpoint
        
        pass
    @property
    def endY(self):
        return self.__endY

    @endY.setter
    def endY(self, endY: int):
        self.__endY = endY


    @property
    def endX(self):
        return self.__endX

    @endX.setter
    def endX(self, endX: int):
        self.__endX = endX


    @property
    def startX(self):
        return self.__startX

    @startX.setter
    def startX(self, startX: int):
        self.__startX = startX


    @property
    def startY(self):
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
            if hasattr(old_value, "model_DiagramModelConnection27"):
                opp_val = getattr(old_value, "model_DiagramModelConnection27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection27"):
                opp_val = getattr(value, "model_DiagramModelConnection27", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelConnection27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_EObject:

    pass
class Adapter:

    pass
class model_ArchimateModelElement(Adapter):

    pass
class Properties:

    pass
class model_SketchModelSticky(DiagramModelContainer, DiagramModelObject, Properties, TextContent):

    pass
class model_DiagramModelGroup(DiagramModelContainer, DiagramModelObject, Properties, Documentable):

    pass
class model_DiagramModelConnection(FontAttribute, Properties, DiagramModelComponent, Documentable):

    def __init__(self, text: str, lineWidth: int, lineColor: str, type: int, model_DiagramModelConnection: "model_DiagramModelObject" = None, model_DiagramModelConnection19: "model_DiagramModelObject" = None, model_DiagramModelConnection21: "model_DiagramModelObject" = None, model_DiagramModelConnection24: "model_DiagramModelObject" = None, model_DiagramModelConnection27: set["model_DiagramModelBendpoint"] = None):
        self.text = text
        self.lineWidth = lineWidth
        self.lineColor = lineColor
        self.type = type
        self.model_DiagramModelConnection = model_DiagramModelConnection
        self.model_DiagramModelConnection19 = model_DiagramModelConnection19
        self.model_DiagramModelConnection21 = model_DiagramModelConnection21
        self.model_DiagramModelConnection24 = model_DiagramModelConnection24
        self.model_DiagramModelConnection27 = model_DiagramModelConnection27 if model_DiagramModelConnection27 is not None else set()
        
        pass
    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type


    @property
    def lineColor(self):
        return self.__lineColor

    @lineColor.setter
    def lineColor(self, lineColor: str):
        self.__lineColor = lineColor


    @property
    def model_DiagramModelConnection21(self):
        return self.__model_DiagramModelConnection21

    @model_DiagramModelConnection21.setter
    def model_DiagramModelConnection21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection21", None)
        self.__model_DiagramModelConnection21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject22"):
                opp_val = getattr(old_value, "model_DiagramModelObject22", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject22"):
                opp_val = getattr(value, "model_DiagramModelObject22", None)
                setattr(value, "model_DiagramModelObject22", self)

    @property
    def model_DiagramModelConnection27(self):
        return self.__model_DiagramModelConnection27

    @model_DiagramModelConnection27.setter
    def model_DiagramModelConnection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection27", None)
        self.__model_DiagramModelConnection27 = value if value is not None else set()
        
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
    def model_DiagramModelConnection(self):
        return self.__model_DiagramModelConnection

    @model_DiagramModelConnection.setter
    def model_DiagramModelConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection", None)
        self.__model_DiagramModelConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject16"):
                opp_val = getattr(old_value, "model_DiagramModelObject16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject16"):
                opp_val = getattr(value, "model_DiagramModelObject16", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelConnection24(self):
        return self.__model_DiagramModelConnection24

    @model_DiagramModelConnection24.setter
    def model_DiagramModelConnection24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection24", None)
        self.__model_DiagramModelConnection24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject25"):
                opp_val = getattr(old_value, "model_DiagramModelObject25", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject25"):
                opp_val = getattr(value, "model_DiagramModelObject25", None)
                setattr(value, "model_DiagramModelObject25", self)

    @property
    def model_DiagramModelConnection19(self):
        return self.__model_DiagramModelConnection19

    @model_DiagramModelConnection19.setter
    def model_DiagramModelConnection19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection19", None)
        self.__model_DiagramModelConnection19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject18"):
                opp_val = getattr(old_value, "model_DiagramModelObject18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject18"):
                opp_val = getattr(value, "model_DiagramModelObject18", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def connect(self, model_target, model_source):
        # TODO: Implement connect method
        pass

    def disconnect(self):
        # TODO: Implement disconnect method
        pass

    def reconnect(self):
        # TODO: Implement reconnect method
        pass

class model_SketchModelActor(DiagramModelObject, Properties, Documentable):

    pass
class ArchimateModelElement:

    pass
class model_DiagramModel(DiagramModelContainer, ArchimateModelElement, Properties, Documentable):

    def __init__(self, connectionRouterType: int, model_DiagramModel: "model_DiagramModelComponent" = None, model_DiagramModel12: "model_DiagramModelReference" = None):
        self.connectionRouterType = connectionRouterType
        self.model_DiagramModel = model_DiagramModel
        self.model_DiagramModel12 = model_DiagramModel12
        
        pass
    @property
    def connectionRouterType(self):
        return self.__connectionRouterType

    @connectionRouterType.setter
    def connectionRouterType(self, connectionRouterType: int):
        self.__connectionRouterType = connectionRouterType


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
    def model_DiagramModel12(self):
        return self.__model_DiagramModel12

    @model_DiagramModel12.setter
    def model_DiagramModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModel__model_DiagramModel12", None)
        self.__model_DiagramModel12 = value
        
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

class Identifier:

    pass
class Nameable:

    pass
class model_DiagramModelComponent(Nameable, Adapter, Cloneable, Identifier):

    pass
class model_ArchimateElement(Documentable, Nameable, Cloneable, Identifier, Properties, ArchimateModelElement):

    pass
class FolderContainer:

    pass
class model_ArchimateModel(Nameable, Properties, Identifier, ArchimateModelElement, FolderContainer):

    def __init__(self, purpose: str, version: str, file: str, model_ArchimateModel: "model_ArchimateModelElement" = None):
        self.purpose = purpose
        self.version = version
        self.file = file
        self.model_ArchimateModel = model_ArchimateModel
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def purpose(self):
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose


    @property
    def model_ArchimateModel(self):
        return self.__model_ArchimateModel

    @model_ArchimateModel.setter
    def model_ArchimateModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ArchimateModel__model_ArchimateModel", None)
        self.__model_ArchimateModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ArchimateModelElement"):
                opp_val = getattr(old_value, "model_ArchimateModelElement", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateModelElement"):
                opp_val = getattr(value, "model_ArchimateModelElement", None)
                setattr(value, "model_ArchimateModelElement", self)

    def setDefaults(self):
        # TODO: Implement setDefaults method
        pass

    def getDefaultDiagramModel(self) :
        # TODO: Implement getDefaultDiagramModel method
        pass

    def getFolder(self, model_type) :
        # TODO: Implement getFolder method
        pass

    def getDiagramModels(self) :
        # TODO: Implement getDiagramModels method
        pass

    def getDefaultFolderForElement(self, model_element) :
        # TODO: Implement getDefaultFolderForElement method
        pass

    def addDerivedRelationsFolder(self) :
        # TODO: Implement addDerivedRelationsFolder method
        pass

    def removeDerivedRelationsFolder(self):
        # TODO: Implement removeDerivedRelationsFolder method
        pass

class model_Documentable(ABC):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


class model_Folder(Documentable, Nameable, Properties, Identifier, ArchimateModelElement, FolderContainer):

    def __init__(self, type: str, model_Folder: "model_FolderContainer" = None, model_Folder4: set["model_EObject"] = None):
        self.type = type
        self.model_Folder = model_Folder
        self.model_Folder4 = model_Folder4 if model_Folder4 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_Folder(self):
        return self.__model_Folder

    @model_Folder.setter
    def model_Folder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Folder__model_Folder", None)
        self.__model_Folder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FolderContainer"):
                opp_val = getattr(old_value, "model_FolderContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FolderContainer"):
                opp_val = getattr(value, "model_FolderContainer", None)
                if opp_val is None:
                    setattr(value, "model_FolderContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Folder4(self):
        return self.__model_Folder4

    @model_Folder4.setter
    def model_Folder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Folder__model_Folder4", None)
        self.__model_Folder4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_EObject"):
                    opp_val = getattr(item, "model_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "model_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_EObject"):
                    opp_val = getattr(item, "model_EObject", None)
                    
                    setattr(item, "model_EObject", self)
                    

class model_FolderContainer(ABC):

    pass
class model_TextContent(ABC):

    def __init__(self, content: str):
        self.content = content
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class model_Cloneable(ABC):

    def __init__(self):
        
        pass
    def getCopy(self) :
        # TODO: Implement getCopy method
        pass

class model_Nameable(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class model_Property:

    def __init__(self, key: str, value: str, model_Property: "model_Properties" = None):
        self.key = key
        self.value = value
        self.model_Property = model_Property
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


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

class model_Properties(ABC):

    pass
class model_Adapter(ABC):

    def __init__(self):
        
        pass
    def setAdapter(self, model_adapter, model_object):
        # TODO: Implement setAdapter method
        pass

    def getAdapter(self, model_adapter) :
        # TODO: Implement getAdapter method
        pass

class model_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

