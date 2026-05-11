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
            if hasattr(old_value, "model_Relationship36"):
                opp_val = getattr(old_value, "model_Relationship36", None)
                if opp_val == self:
                    setattr(old_value, "model_Relationship36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Relationship36"):
                opp_val = getattr(value, "model_Relationship36", None)
                setattr(value, "model_Relationship36", self)

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


class model_FontAttribute(ABC):

    def __init__(self, font: str, fontColor: str, textAlignment: int, textPosition: int):
        self.font = font
        self.fontColor = fontColor
        self.textAlignment = textAlignment
        self.textPosition = textPosition
        
        pass
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
    def font(self):
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font


    @property
    def fontColor(self):
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor


    def getDefaultTextAlignment(self) :
        # TODO: Implement getDefaultTextAlignment method
        pass

class model_LineObject(ABC):

    def __init__(self, lineWidth: int, lineColor: str):
        self.lineWidth = lineWidth
        self.lineColor = lineColor
        
        pass
    @property
    def lineColor(self):
        return self.__lineColor

    @lineColor.setter
    def lineColor(self, lineColor: str):
        self.__lineColor = lineColor


    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth


class TextContent:

    pass
class DiagramModelImageProvider:

    pass
class BorderObject:

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
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


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
            if hasattr(old_value, "model_DiagramModelObject19"):
                opp_val = getattr(old_value, "model_DiagramModelObject19", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject19"):
                opp_val = getattr(value, "model_DiagramModelObject19", None)
                setattr(value, "model_DiagramModelObject19", self)

    def getCopy(self) :
        # TODO: Implement getCopy method
        pass

class DiagramModelObject:

    pass
class model_DiagramModelNote(TextContent, DiagramModelObject):

    pass
class model_DiagramModelImage(BorderObject, DiagramModelImageProvider, DiagramModelObject):

    pass
class model_DiagramModelReference(DiagramModelObject):

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
            if hasattr(old_value, "model_ArchimateElement34"):
                opp_val = getattr(old_value, "model_ArchimateElement34", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateElement34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateElement34"):
                opp_val = getattr(value, "model_ArchimateElement34", None)
                setattr(value, "model_ArchimateElement34", self)

    def removeArchimateElementFromModel(self):
        # TODO: Implement removeArchimateElementFromModel method
        pass

    def addArchimateElementToModel(self, model_parent):
        # TODO: Implement addArchimateElementToModel method
        pass

class LineObject:

    pass
class FontAttribute:

    pass
class DiagramModelComponent:

    pass
class model_DiagramModelObject(LineObject, DiagramModelComponent, FontAttribute):

    def __init__(self, fillColor: str, model_DiagramModelObject: "model_DiagramModelContainer" = None, model_DiagramModelObject19: "model_Bounds" = None, model_DiagramModelObject21: set["model_DiagramModelConnection"] = None, model_DiagramModelObject23: set["model_DiagramModelConnection"] = None, model_DiagramModelObject27: "model_DiagramModelConnection" = None, model_DiagramModelObject30: "model_DiagramModelConnection" = None):
        self.fillColor = fillColor
        self.model_DiagramModelObject = model_DiagramModelObject
        self.model_DiagramModelObject19 = model_DiagramModelObject19
        self.model_DiagramModelObject21 = model_DiagramModelObject21 if model_DiagramModelObject21 is not None else set()
        self.model_DiagramModelObject23 = model_DiagramModelObject23 if model_DiagramModelObject23 is not None else set()
        self.model_DiagramModelObject27 = model_DiagramModelObject27
        self.model_DiagramModelObject30 = model_DiagramModelObject30
        
        pass
    @property
    def fillColor(self):
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor


    @property
    def model_DiagramModelObject21(self):
        return self.__model_DiagramModelObject21

    @model_DiagramModelObject21.setter
    def model_DiagramModelObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject21", None)
        self.__model_DiagramModelObject21 = value if value is not None else set()
        
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
    def model_DiagramModelObject19(self):
        return self.__model_DiagramModelObject19

    @model_DiagramModelObject19.setter
    def model_DiagramModelObject19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject19", None)
        self.__model_DiagramModelObject19 = value
        
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
    def model_DiagramModelObject27(self):
        return self.__model_DiagramModelObject27

    @model_DiagramModelObject27.setter
    def model_DiagramModelObject27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject27", None)
        self.__model_DiagramModelObject27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection26"):
                opp_val = getattr(old_value, "model_DiagramModelConnection26", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection26"):
                opp_val = getattr(value, "model_DiagramModelConnection26", None)
                setattr(value, "model_DiagramModelConnection26", self)

    @property
    def model_DiagramModelObject23(self):
        return self.__model_DiagramModelObject23

    @model_DiagramModelObject23.setter
    def model_DiagramModelObject23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject23", None)
        self.__model_DiagramModelObject23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelConnection24"):
                    opp_val = getattr(item, "model_DiagramModelConnection24", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelConnection24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelConnection24"):
                    opp_val = getattr(item, "model_DiagramModelConnection24", None)
                    
                    setattr(item, "model_DiagramModelConnection24", self)
                    

    @property
    def model_DiagramModelObject30(self):
        return self.__model_DiagramModelObject30

    @model_DiagramModelObject30.setter
    def model_DiagramModelObject30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject30", None)
        self.__model_DiagramModelObject30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection29"):
                opp_val = getattr(old_value, "model_DiagramModelConnection29", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection29"):
                opp_val = getattr(value, "model_DiagramModelConnection29", None)
                setattr(value, "model_DiagramModelConnection29", self)

    def addConnection(self, model_connection):
        # TODO: Implement addConnection method
        pass

    def setBounds(self, model_height, model_x, model_width, model_y):
        # TODO: Implement setBounds method
        pass

    def removeConnection(self, model_connection):
        # TODO: Implement removeConnection method
        pass

class model_DiagramModelContainer(DiagramModelComponent):

    pass
class ImplementationMigrationElement:

    pass
class model_Deliverable(ImplementationMigrationElement):

    pass
class model_WorkPackage(ImplementationMigrationElement):

    pass
class model_Gap(ImplementationMigrationElement):

    pass
class model_Plateau(ImplementationMigrationElement):

    pass
class MotivationElement:

    pass
class model_Driver(MotivationElement):

    pass
class model_Assessment(MotivationElement):

    pass
class model_Stakeholder(MotivationElement):

    pass
class model_Principle(MotivationElement):

    pass
class model_Constraint(MotivationElement):

    pass
class model_Requirement(MotivationElement):

    pass
class model_Goal(MotivationElement):

    pass
class ApplicationLayerElement:

    pass
class model_DataObject(ApplicationLayerElement):

    pass
class model_ApplicationFunction(ApplicationLayerElement):

    pass
class model_ApplicationInteraction(ApplicationLayerElement):

    pass
class model_ApplicationComponent(ApplicationLayerElement):

    pass
class model_ApplicationCollaboration(ApplicationLayerElement):

    pass
class TechnologyLayerElement:

    pass
class model_Node(TechnologyLayerElement):

    pass
class model_CommunicationPath(TechnologyLayerElement):

    pass
class model_Network(TechnologyLayerElement):

    pass
class model_Device(TechnologyLayerElement):

    pass
class model_SystemSoftware(TechnologyLayerElement):

    pass
class model_InfrastructureFunction(TechnologyLayerElement):

    pass
class model_Artifact(TechnologyLayerElement):

    pass
class InterfaceElement:

    pass
class model_ApplicationInterface(ApplicationLayerElement, InterfaceElement):

    pass
class model_InfrastructureInterface(InterfaceElement, TechnologyLayerElement):

    pass
class ServiceElement:

    pass
class model_ApplicationService(ApplicationLayerElement, ServiceElement):

    pass
class model_InfrastructureService(ServiceElement, TechnologyLayerElement):

    pass
class BusinessLayerElement:

    pass
class model_Location(BusinessLayerElement):

    pass
class model_BusinessCollaboration(BusinessLayerElement):

    pass
class model_BusinessRole(BusinessLayerElement):

    pass
class model_BusinessEvent(BusinessLayerElement):

    pass
class model_BusinessService(BusinessLayerElement, ServiceElement):

    pass
class model_BusinessInterface(InterfaceElement, BusinessLayerElement):

    pass
class model_BusinessInteraction(BusinessLayerElement):

    pass
class model_Product(BusinessLayerElement):

    pass
class model_Value(BusinessLayerElement):

    pass
class model_Representation(BusinessLayerElement):

    pass
class model_Meaning(BusinessLayerElement):

    pass
class model_BusinessFunction(BusinessLayerElement):

    pass
class model_BusinessActor(BusinessLayerElement):

    pass
class model_Contract(BusinessLayerElement):

    pass
class model_BusinessProcess(BusinessLayerElement):

    pass
class model_BusinessObject(BusinessLayerElement):

    pass
class model_BusinessActivity(BusinessLayerElement):

    pass
class JunctionElement:

    pass
class model_Junction(JunctionElement):

    pass
class ArchimateElement:

    pass
class model_BusinessLayerElement(ArchimateElement):

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


class model_ServiceElement(ArchimateElement):

    pass
class model_ApplicationLayerElement(ArchimateElement):

    pass
class model_ImplementationMigrationElement(ArchimateElement):

    pass
class model_MotivationElement(ArchimateElement):

    pass
class model_TechnologyLayerElement(ArchimateElement):

    pass
class model_JunctionElement(ArchimateElement):

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
        
        pass
    @property
    def startY(self):
        return self.__startY

    @startY.setter
    def startY(self, startY: int):
        self.__startY = startY


    @property
    def startX(self):
        return self.__startX

    @startX.setter
    def startX(self, startX: int):
        self.__startX = startX


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
    def model_DiagramModelBendpoint(self):
        return self.__model_DiagramModelBendpoint

    @model_DiagramModelBendpoint.setter
    def model_DiagramModelBendpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelBendpoint__model_DiagramModelBendpoint", None)
        self.__model_DiagramModelBendpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection32"):
                opp_val = getattr(old_value, "model_DiagramModelConnection32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection32"):
                opp_val = getattr(value, "model_DiagramModelConnection32", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelConnection32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Relationship:

    pass
class model_AggregationRelationship(Relationship):

    pass
class model_SpecialisationRelationship(Relationship):

    pass
class model_AssignmentRelationship(Relationship):

    pass
class model_UsedByRelationship(Relationship):

    pass
class model_CompositionRelationship(Relationship):

    pass
class model_InfluenceRelationship(Relationship):

    pass
class model_TriggeringRelationship(Relationship):

    pass
class model_RealisationRelationship(Relationship):

    pass
class model_AssociationRelationship(Relationship):

    pass
class model_FlowRelationship(Relationship):

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


class model_Relationship(ArchimateElement):

    pass
class model_OrJunction(JunctionElement):

    pass
class model_AndJunction(JunctionElement):

    pass
class model_EObject:

    pass
class Documentable:

    pass
class Adapter:

    pass
class model_ArchimateModelElement(Adapter):

    pass
class model_Cloneable(ABC):

    def __init__(self):
        
        pass
    def getCopy(self) :
        # TODO: Implement getCopy method
        pass

class Properties:

    pass
class model_DiagramModelGroup(Documentable, Properties, DiagramModelContainer, DiagramModelObject):

    pass
class model_DiagramModelConnection(FontAttribute, Documentable, DiagramModelComponent, LineObject, Properties):

    def __init__(self, type: int, text: str, model_DiagramModelConnection: "model_DiagramModelObject" = None, model_DiagramModelConnection24: "model_DiagramModelObject" = None, model_DiagramModelConnection32: set["model_DiagramModelBendpoint"] = None, model_DiagramModelConnection26: "model_DiagramModelObject" = None, model_DiagramModelConnection29: "model_DiagramModelObject" = None):
        self.type = type
        self.text = text
        self.model_DiagramModelConnection = model_DiagramModelConnection
        self.model_DiagramModelConnection24 = model_DiagramModelConnection24
        self.model_DiagramModelConnection32 = model_DiagramModelConnection32 if model_DiagramModelConnection32 is not None else set()
        self.model_DiagramModelConnection26 = model_DiagramModelConnection26
        self.model_DiagramModelConnection29 = model_DiagramModelConnection29
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def model_DiagramModelConnection26(self):
        return self.__model_DiagramModelConnection26

    @model_DiagramModelConnection26.setter
    def model_DiagramModelConnection26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection26", None)
        self.__model_DiagramModelConnection26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject27"):
                opp_val = getattr(old_value, "model_DiagramModelObject27", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject27"):
                opp_val = getattr(value, "model_DiagramModelObject27", None)
                setattr(value, "model_DiagramModelObject27", self)

    @property
    def model_DiagramModelConnection29(self):
        return self.__model_DiagramModelConnection29

    @model_DiagramModelConnection29.setter
    def model_DiagramModelConnection29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection29", None)
        self.__model_DiagramModelConnection29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelObject30"):
                opp_val = getattr(old_value, "model_DiagramModelObject30", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject30"):
                opp_val = getattr(value, "model_DiagramModelObject30", None)
                setattr(value, "model_DiagramModelObject30", self)

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
            if hasattr(old_value, "model_DiagramModelObject21"):
                opp_val = getattr(old_value, "model_DiagramModelObject21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject21"):
                opp_val = getattr(value, "model_DiagramModelObject21", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject21", set([self]))
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
            if hasattr(old_value, "model_DiagramModelObject23"):
                opp_val = getattr(old_value, "model_DiagramModelObject23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject23"):
                opp_val = getattr(value, "model_DiagramModelObject23", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelObject23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelConnection32(self):
        return self.__model_DiagramModelConnection32

    @model_DiagramModelConnection32.setter
    def model_DiagramModelConnection32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection32", None)
        self.__model_DiagramModelConnection32 = value if value is not None else set()
        
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
                    

    def reconnect(self):
        # TODO: Implement reconnect method
        pass

    def disconnect(self):
        # TODO: Implement disconnect method
        pass

    def connect(self, model_source, model_target):
        # TODO: Implement connect method
        pass

class model_SketchModelSticky(TextContent, Properties, DiagramModelContainer, DiagramModelObject):

    pass
class model_SketchModelActor(Documentable, Properties, DiagramModelObject):

    pass
class ArchimateModelElement:

    pass
class model_DiagramModel(Documentable, Properties, DiagramModelContainer, ArchimateModelElement):

    def __init__(self, connectionRouterType: int, model_DiagramModel: "model_DiagramModelComponent" = None, model_DiagramModel17: "model_DiagramModelReference" = None):
        self.connectionRouterType = connectionRouterType
        self.model_DiagramModel = model_DiagramModel
        self.model_DiagramModel17 = model_DiagramModel17
        
        pass
    @property
    def connectionRouterType(self):
        return self.__connectionRouterType

    @connectionRouterType.setter
    def connectionRouterType(self, connectionRouterType: int):
        self.__connectionRouterType = connectionRouterType


    @property
    def model_DiagramModel17(self):
        return self.__model_DiagramModel17

    @model_DiagramModel17.setter
    def model_DiagramModel17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModel__model_DiagramModel17", None)
        self.__model_DiagramModel17 = value
        
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

class Identifier:

    pass
class Nameable:

    pass
class model_ArchimateElement(Cloneable, ArchimateModelElement, Identifier, Nameable, Documentable, Properties):

    pass
class model_DiagramModelComponent(Nameable, Adapter, Cloneable, Identifier):

    pass
class FolderContainer:

    pass
class model_ArchimateModel(ArchimateModelElement, FolderContainer, Identifier, Nameable, Properties):

    def __init__(self, purpose: str, file: str, version: str, model_ArchimateModel: "model_Metadata" = None, model_ArchimateModel7: "model_ArchimateModelElement" = None):
        self.purpose = purpose
        self.file = file
        self.version = version
        self.model_ArchimateModel = model_ArchimateModel
        self.model_ArchimateModel7 = model_ArchimateModel7
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


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
            if hasattr(old_value, "model_Metadata5"):
                opp_val = getattr(old_value, "model_Metadata5", None)
                if opp_val == self:
                    setattr(old_value, "model_Metadata5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Metadata5"):
                opp_val = getattr(value, "model_Metadata5", None)
                setattr(value, "model_Metadata5", self)

    @property
    def model_ArchimateModel7(self):
        return self.__model_ArchimateModel7

    @model_ArchimateModel7.setter
    def model_ArchimateModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ArchimateModel__model_ArchimateModel7", None)
        self.__model_ArchimateModel7 = value
        
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

    def removeDerivedRelationsFolder(self):
        # TODO: Implement removeDerivedRelationsFolder method
        pass

    def getFolder(self, model_type) :
        # TODO: Implement getFolder method
        pass

    def addDerivedRelationsFolder(self) :
        # TODO: Implement addDerivedRelationsFolder method
        pass

    def getDiagramModels(self) :
        # TODO: Implement getDiagramModels method
        pass

    def getDefaultDiagramModel(self) :
        # TODO: Implement getDefaultDiagramModel method
        pass

    def getDefaultFolderForElement(self, model_element) :
        # TODO: Implement getDefaultFolderForElement method
        pass

    def setDefaults(self):
        # TODO: Implement setDefaults method
        pass

class model_Folder(ArchimateModelElement, FolderContainer, Identifier, Nameable, Documentable, Properties):

    def __init__(self, type: str, model_Folder: "model_FolderContainer" = None, model_Folder9: set["model_EObject"] = None):
        self.type = type
        self.model_Folder = model_Folder
        self.model_Folder9 = model_Folder9 if model_Folder9 is not None else set()
        
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
    def model_Folder9(self):
        return self.__model_Folder9

    @model_Folder9.setter
    def model_Folder9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Folder__model_Folder9", None)
        self.__model_Folder9 = value if value is not None else set()
        
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
class model_Properties(ABC):

    pass
class model_Property:

    def __init__(self, key: str, value: str, model_Property2: "model_Metadata" = None, model_Property: "model_Properties" = None):
        self.key = key
        self.value = value
        self.model_Property2 = model_Property2
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
    def model_Property2(self):
        return self.__model_Property2

    @model_Property2.setter
    def model_Property2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Property__model_Property2", None)
        self.__model_Property2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Metadata"):
                opp_val = getattr(old_value, "model_Metadata", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Metadata"):
                opp_val = getattr(value, "model_Metadata", None)
                if opp_val is None:
                    setattr(value, "model_Metadata", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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


class model_Metadata:

    pass
class model_Adapter(ABC):

    def __init__(self):
        
        pass
    def getAdapter(self, model_adapter) :
        # TODO: Implement getAdapter method
        pass

    def setAdapter(self, model_adapter, model_object):
        # TODO: Implement setAdapter method
        pass
