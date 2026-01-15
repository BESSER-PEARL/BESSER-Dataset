from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FolderType(Enum):
    relations = "relations"
    user = "user"
    strategy = "strategy"
    business = "business"
    application = "application"
    technology = "technology"
    other = "other"
    diagrams = "diagrams"
    motivation = "motivation"
    implementation_migration = "implementation_migration"


############################################
# Definition of Classes
############################################

class DiagramModelConnection:

    pass
class DiagramModelArchimateComponent:

    pass
class model_DiagramModelArchimateConnection(DiagramModelArchimateComponent, DiagramModelConnection):

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

class model_ArchimateDiagramModel(DiagramModel):

    def __init__(self, viewpoint: str):
        self.viewpoint = viewpoint
        
    @property
    def viewpoint(self) -> str:
        return self.__viewpoint

    @viewpoint.setter
    def viewpoint(self, viewpoint: str):
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

class model_DiagramModelImageProvider(ABC):

    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        
    @property
    def imagePath(self) -> str:
        return self.__imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str):
        self.__imagePath = imagePath

class model_BorderType(ABC):

    def __init__(self, borderType: int):
        self.borderType = borderType
        
    @property
    def borderType(self) -> int:
        return self.__borderType

    @borderType.setter
    def borderType(self, borderType: int):
        self.__borderType = borderType

class model_BorderObject(ABC):

    def __init__(self, borderColor: str):
        self.borderColor = borderColor
        
    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

class model_TextAlignment(ABC):

    def __init__(self, textAlignment: int):
        self.textAlignment = textAlignment
        
    @property
    def textAlignment(self) -> int:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: int):
        self.__textAlignment = textAlignment

class model_TextPosition(ABC):

    def __init__(self, textPosition: int):
        self.textPosition = textPosition
        
    @property
    def textPosition(self) -> int:
        return self.__textPosition

    @textPosition.setter
    def textPosition(self, textPosition: int):
        self.__textPosition = textPosition

class model_FontAttribute(ABC):

    def __init__(self, font: str, fontColor: str):
        self.font = font
        self.fontColor = fontColor
        
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

class model_LineObject(ABC):

    def __init__(self, lineWidth: int, lineColor: str):
        self.lineWidth = lineWidth
        self.lineColor = lineColor
        
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

class DiagramModelImageProvider:

    pass
class BorderObject:

    pass
class TextContent:

    pass
class BorderType:

    pass
class model_Bounds:

    def __init__(self, x: int, y: int, width: int, height: int, model_Bounds: "model_DiagramModelObject" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.model_Bounds = model_Bounds
        
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
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

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
            if hasattr(old_value, "model_DiagramModelObject20"):
                opp_val = getattr(old_value, "model_DiagramModelObject20", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelObject20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelObject20"):
                opp_val = getattr(value, "model_DiagramModelObject20", None)
                setattr(value, "model_DiagramModelObject20", self)

    def setSize(self, width: int, height: int):
        # TODO: Implement setSize method
        pass

    def setLocation(self, y: int, x: int):
        # TODO: Implement setLocation method
        pass

    def getCopy(self) -> str:
        # TODO: Implement getCopy method
        pass

class TextAlignment:

    pass
class LineObject:

    pass
class FontAttribute:

    pass
class Connectable:

    pass
class model_DiagramModelArchimateComponent(Connectable):

    def __init__(self):
        
    def addArchimateConceptToModel(self, parent: str):
        # TODO: Implement addArchimateConceptToModel method
        pass

    def setArchimateConcept(self, concept: ArchimateConcept):
        # TODO: Implement setArchimateConcept method
        pass

    def removeArchimateConceptFromModel(self):
        # TODO: Implement removeArchimateConceptFromModel method
        pass

    def getArchimateConcept(self) -> ArchimateConcept:
        # TODO: Implement getArchimateConcept method
        pass

class TextPosition:

    pass
class DiagramModelObject:

    pass
class model_DiagramModelReference(TextPosition, DiagramModelObject):

    pass
class DiagramModelContainer:

    pass
class model_DiagramModelArchimateObject(TextPosition, DiagramModelArchimateComponent, DiagramModelContainer, DiagramModelObject):

    def __init__(self, type: int, model_DiagramModelArchimateObject: "model_ArchimateElement" = None):
        self.type = type
        self.model_DiagramModelArchimateObject = model_DiagramModelArchimateObject
        
    @property
    def type(self) -> int:
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
            if hasattr(old_value, "model_ArchimateElement"):
                opp_val = getattr(old_value, "model_ArchimateElement", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateElement"):
                opp_val = getattr(value, "model_ArchimateElement", None)
                setattr(value, "model_ArchimateElement", self)

class model_DiagramModelObject(LineObject, FontAttribute, TextAlignment, Connectable):

    def __init__(self, fillColor: str, alpha: int, model_DiagramModelObject: "model_DiagramModelContainer" = None, model_DiagramModelObject20: "model_Bounds" = None):
        self.fillColor = fillColor
        self.alpha = alpha
        self.model_DiagramModelObject = model_DiagramModelObject
        self.model_DiagramModelObject20 = model_DiagramModelObject20
        
    @property
    def fillColor(self) -> str:
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor

    @property
    def alpha(self) -> int:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha

    @property
    def model_DiagramModelObject20(self):
        return self.__model_DiagramModelObject20

    @model_DiagramModelObject20.setter
    def model_DiagramModelObject20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelObject__model_DiagramModelObject20", None)
        self.__model_DiagramModelObject20 = value
        
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

    def setBounds(self, height: int, x: int, y: int, width: int):
        # TODO: Implement setBounds method
        pass

class DiagramModelComponent:

    pass
class model_DiagramModelContainer(DiagramModelComponent):

    pass
class model_Connectable(DiagramModelComponent):

    def __init__(self, model_Connectable: set["model_DiagramModelConnection"] = None, model_Connectable15: set["model_DiagramModelConnection"] = None, model_Connectable23: "model_DiagramModelConnection" = None, model_Connectable26: "model_DiagramModelConnection" = None):
        self.model_Connectable = model_Connectable if model_Connectable is not None else set()
        self.model_Connectable15 = model_Connectable15 if model_Connectable15 is not None else set()
        self.model_Connectable23 = model_Connectable23
        self.model_Connectable26 = model_Connectable26
        
    @property
    def model_Connectable26(self):
        return self.__model_Connectable26

    @model_Connectable26.setter
    def model_Connectable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Connectable__model_Connectable26", None)
        self.__model_Connectable26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection25"):
                opp_val = getattr(old_value, "model_DiagramModelConnection25", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection25"):
                opp_val = getattr(value, "model_DiagramModelConnection25", None)
                setattr(value, "model_DiagramModelConnection25", self)

    @property
    def model_Connectable(self):
        return self.__model_Connectable

    @model_Connectable.setter
    def model_Connectable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Connectable__model_Connectable", None)
        self.__model_Connectable = value if value is not None else set()
        
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
    def model_Connectable23(self):
        return self.__model_Connectable23

    @model_Connectable23.setter
    def model_Connectable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Connectable__model_Connectable23", None)
        self.__model_Connectable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelConnection22"):
                opp_val = getattr(old_value, "model_DiagramModelConnection22", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelConnection22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection22"):
                opp_val = getattr(value, "model_DiagramModelConnection22", None)
                setattr(value, "model_DiagramModelConnection22", self)

    @property
    def model_Connectable15(self):
        return self.__model_Connectable15

    @model_Connectable15.setter
    def model_Connectable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Connectable__model_Connectable15", None)
        self.__model_Connectable15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_DiagramModelConnection16"):
                    opp_val = getattr(item, "model_DiagramModelConnection16", None)
                    
                    if opp_val == self:
                        setattr(item, "model_DiagramModelConnection16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_DiagramModelConnection16"):
                    opp_val = getattr(item, "model_DiagramModelConnection16", None)
                    
                    setattr(item, "model_DiagramModelConnection16", self)
                    

    def addConnection(self, connection: str):
        # TODO: Implement addConnection method
        pass

    def removeConnection(self, connection: str):
        # TODO: Implement removeConnection method
        pass

class OtherRelationship:

    pass
class model_SpecializationRelationship(OtherRelationship):

    pass
class DynamicRelationship:

    pass
class model_TriggeringRelationship(DynamicRelationship):

    pass
class model_FlowRelationship(DynamicRelationship):

    pass
class StructuralRelationship:

    pass
class model_RealizationRelationship(StructuralRelationship):

    pass
class model_CompositionRelationship(StructuralRelationship):

    pass
class model_AssignmentRelationship(StructuralRelationship):

    pass
class model_AggregationRelationship(StructuralRelationship):

    pass
class DependendencyRelationship:

    pass
class model_InfluenceRelationship(DependendencyRelationship):

    def __init__(self, strength: str):
        self.strength = strength
        
    @property
    def strength(self) -> str:
        return self.__strength

    @strength.setter
    def strength(self, strength: str):
        self.__strength = strength

class model_ServingRelationship(DependendencyRelationship):

    pass
class model_AssociationRelationship(DependendencyRelationship):

    def __init__(self, directed: bool):
        self.directed = directed
        
    @property
    def directed(self) -> bool:
        return self.__directed

    @directed.setter
    def directed(self, directed: bool):
        self.__directed = directed

class model_AccessRelationship(DependendencyRelationship):

    def __init__(self, accessType: int):
        self.accessType = accessType
        
    @property
    def accessType(self) -> int:
        return self.__accessType

    @accessType.setter
    def accessType(self, accessType: int):
        self.__accessType = accessType

class CompositeElement:

    pass
class model_Location(CompositeElement):

    pass
class model_Grouping(CompositeElement):

    pass
class PhysicalElement:

    pass
class ImplementationMigrationElement:

    pass
class model_Plateau(CompositeElement, ImplementationMigrationElement):

    pass
class model_ImplementationEvent(ImplementationMigrationElement):

    pass
class BusinessObject:

    pass
class model_Contract(BusinessObject):

    pass
class StrategyBehaviorElement:

    pass
class model_ValueStream(StrategyBehaviorElement):

    pass
class model_Capability(StrategyBehaviorElement):

    pass
class BusinessElement:

    pass
class model_Product(CompositeElement, BusinessElement):

    pass
class MotivationElement:

    pass
class model_Outcome(MotivationElement):

    pass
class model_Meaning(MotivationElement):

    pass
class model_Requirement(MotivationElement):

    pass
class model_Value(MotivationElement):

    pass
class model_Driver(MotivationElement):

    pass
class model_Principle(MotivationElement):

    pass
class model_Constraint(MotivationElement):

    pass
class model_Assessment(MotivationElement):

    pass
class TechnologyObject:

    pass
class model_Material(PhysicalElement, TechnologyObject):

    pass
class model_Artifact(TechnologyObject):

    pass
class model_Goal(MotivationElement):

    pass
class ActiveStructureElement:

    pass
class model_Stakeholder(ActiveStructureElement, MotivationElement):

    pass
class model_Equipment(ActiveStructureElement, PhysicalElement):

    pass
class model_BusinessInterface(ActiveStructureElement, BusinessElement):

    pass
class model_BusinessRole(ActiveStructureElement, BusinessElement):

    pass
class model_DistributionNetwork(ActiveStructureElement, PhysicalElement):

    pass
class model_Facility(ActiveStructureElement, PhysicalElement):

    pass
class model_BusinessCollaboration(ActiveStructureElement, BusinessElement):

    pass
class model_BusinessActor(ActiveStructureElement, BusinessElement):

    pass
class ApplicationElement:

    pass
class model_ApplicationComponent(ActiveStructureElement, ApplicationElement):

    pass
class model_ApplicationInterface(ActiveStructureElement, ApplicationElement):

    pass
class model_ApplicationCollaboration(ActiveStructureElement, ApplicationElement):

    pass
class ArchimateRelationship:

    pass
class model_DynamicRelationship(ArchimateRelationship):

    pass
class model_OtherRelationship(ArchimateRelationship):

    pass
class model_DependendencyRelationship(ArchimateRelationship):

    pass
class model_StructuralRelationship(ArchimateRelationship):

    pass
class StructureElement:

    pass
class model_PassiveStructureElement(StructureElement):

    pass
class model_ActiveStructureElement(StructureElement):

    pass
class StrategyElement:

    pass
class model_Resource(StrategyElement, StructureElement):

    pass
class BehaviorElement:

    pass
class model_ApplicationService(BehaviorElement, ApplicationElement):

    pass
class model_BusinessEvent(BehaviorElement, BusinessElement):

    pass
class model_CourseOfAction(BehaviorElement, StrategyElement):

    pass
class model_BusinessFunction(BehaviorElement, BusinessElement):

    pass
class model_ApplicationProcess(BehaviorElement, ApplicationElement):

    pass
class model_BusinessInteraction(BehaviorElement, BusinessElement):

    pass
class model_BusinessProcess(BehaviorElement, BusinessElement):

    pass
class model_BusinessService(BehaviorElement, BusinessElement):

    pass
class model_WorkPackage(BehaviorElement, ImplementationMigrationElement):

    pass
class model_ApplicationEvent(BehaviorElement, ApplicationElement):

    pass
class model_StrategyBehaviorElement(BehaviorElement, StrategyElement):

    pass
class model_ApplicationInteraction(BehaviorElement, ApplicationElement):

    pass
class model_ApplicationFunction(BehaviorElement, ApplicationElement):

    pass
class PassiveStructureElement:

    pass
class model_BusinessObject(PassiveStructureElement, BusinessElement):

    pass
class model_Gap(PassiveStructureElement, ImplementationMigrationElement):

    pass
class model_Representation(PassiveStructureElement, BusinessElement):

    pass
class model_DataObject(PassiveStructureElement, ApplicationElement):

    pass
class model_Deliverable(PassiveStructureElement, ImplementationMigrationElement):

    pass
class TechnologyElement:

    pass
class model_CommunicationNetwork(ActiveStructureElement, TechnologyElement):

    pass
class model_TechnologyEvent(BehaviorElement, TechnologyElement):

    pass
class model_Path(ActiveStructureElement, TechnologyElement):

    pass
class model_SystemSoftware(ActiveStructureElement, TechnologyElement):

    pass
class model_TechnologyFunction(BehaviorElement, TechnologyElement):

    pass
class model_TechnologyCollaboration(ActiveStructureElement, TechnologyElement):

    pass
class model_Device(ActiveStructureElement, TechnologyElement):

    pass
class model_TechnologyInterface(ActiveStructureElement, TechnologyElement):

    pass
class model_TechnologyProcess(BehaviorElement, TechnologyElement):

    pass
class model_Node(ActiveStructureElement, TechnologyElement):

    pass
class model_TechnologyInteraction(BehaviorElement, TechnologyElement):

    pass
class model_TechnologyService(BehaviorElement, TechnologyElement):

    pass
class model_TechnologyObject(PassiveStructureElement, TechnologyElement):

    pass
class ArchimateElement:

    pass
class model_ImplementationMigrationElement(ArchimateElement):

    pass
class model_MotivationElement(ArchimateElement):

    pass
class model_StructureElement(ArchimateElement):

    pass
class model_Junction(ArchimateElement):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class model_ApplicationElement(ArchimateElement):

    pass
class model_TechnologyElement(ArchimateElement):

    pass
class model_BehaviorElement(ArchimateElement):

    pass
class model_BusinessElement(ArchimateElement):

    pass
class model_CompositeElement(ArchimateElement):

    pass
class model_StrategyElement(ArchimateElement):

    pass
class ArchimateConcept:

    pass
class model_ArchimateRelationship(ArchimateConcept):

    def __init__(self, model_ArchimateRelationship: "model_ArchimateConcept" = None, model_ArchimateRelationship9: "model_ArchimateConcept" = None, model_ArchimateRelationship31: "model_DiagramModelArchimateConnection" = None):
        self.model_ArchimateRelationship = model_ArchimateRelationship
        self.model_ArchimateRelationship9 = model_ArchimateRelationship9
        self.model_ArchimateRelationship31 = model_ArchimateRelationship31
        
    @property
    def model_ArchimateRelationship9(self):
        return self.__model_ArchimateRelationship9

    @model_ArchimateRelationship9.setter
    def model_ArchimateRelationship9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ArchimateRelationship__model_ArchimateRelationship9", None)
        self.__model_ArchimateRelationship9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ArchimateConcept10"):
                opp_val = getattr(old_value, "model_ArchimateConcept10", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateConcept10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateConcept10"):
                opp_val = getattr(value, "model_ArchimateConcept10", None)
                setattr(value, "model_ArchimateConcept10", self)

    @property
    def model_ArchimateRelationship(self):
        return self.__model_ArchimateRelationship

    @model_ArchimateRelationship.setter
    def model_ArchimateRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ArchimateRelationship__model_ArchimateRelationship", None)
        self.__model_ArchimateRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ArchimateConcept"):
                opp_val = getattr(old_value, "model_ArchimateConcept", None)
                if opp_val == self:
                    setattr(old_value, "model_ArchimateConcept", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ArchimateConcept"):
                opp_val = getattr(value, "model_ArchimateConcept", None)
                setattr(value, "model_ArchimateConcept", self)

    @property
    def model_ArchimateRelationship31(self):
        return self.__model_ArchimateRelationship31

    @model_ArchimateRelationship31.setter
    def model_ArchimateRelationship31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ArchimateRelationship__model_ArchimateRelationship31", None)
        self.__model_ArchimateRelationship31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_DiagramModelArchimateConnection"):
                opp_val = getattr(old_value, "model_DiagramModelArchimateConnection", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelArchimateConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelArchimateConnection"):
                opp_val = getattr(value, "model_DiagramModelArchimateConnection", None)
                setattr(value, "model_DiagramModelArchimateConnection", self)

    def connect(self, target: ArchimateConcept, source: ArchimateConcept):
        # TODO: Implement connect method
        pass

    def reconnect(self):
        # TODO: Implement reconnect method
        pass

    def disconnect(self):
        # TODO: Implement disconnect method
        pass

class model_ArchimateElement(ArchimateConcept):

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
    def endX(self) -> int:
        return self.__endX

    @endX.setter
    def endX(self, endX: int):
        self.__endX = endX

    @property
    def endY(self) -> int:
        return self.__endY

    @endY.setter
    def endY(self, endY: int):
        self.__endY = endY

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
            if hasattr(old_value, "model_DiagramModelConnection28"):
                opp_val = getattr(old_value, "model_DiagramModelConnection28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelConnection28"):
                opp_val = getattr(value, "model_DiagramModelConnection28", None)
                if opp_val is None:
                    setattr(value, "model_DiagramModelConnection28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Features:

    pass
class Identifier:

    pass
class Nameable:

    pass
class Adapter:

    pass
class model_ArchimateModelObject(Identifier, Nameable, Adapter, Features):

    def __init__(self):
        
    def getArchimateModel(self) -> str:
        # TODO: Implement getArchimateModel method
        pass

class model_EObject:

    pass
class Properties:

    pass
class model_DiagramModelNote(Properties, DiagramModelObject, TextContent, BorderType, TextPosition):

    pass
class model_SketchModelSticky(Properties, DiagramModelObject, TextContent, DiagramModelContainer, TextPosition):

    pass
class Documentable:

    pass
class model_SketchModelActor(DiagramModelObject, Documentable, Properties):

    pass
class model_DiagramModelGroup(Documentable, Properties, DiagramModelObject, DiagramModelContainer, BorderType, TextPosition):

    pass
class model_DiagramModelConnection(FontAttribute, Documentable, Properties, Connectable, LineObject):

    def __init__(self, text: str, textPosition: int, type: int, model_DiagramModelConnection: "model_Connectable" = None, model_DiagramModelConnection16: "model_Connectable" = None, model_DiagramModelConnection22: "model_Connectable" = None, model_DiagramModelConnection25: "model_Connectable" = None, model_DiagramModelConnection28: set["model_DiagramModelBendpoint"] = None):
        self.text = text
        self.textPosition = textPosition
        self.type = type
        self.model_DiagramModelConnection = model_DiagramModelConnection
        self.model_DiagramModelConnection16 = model_DiagramModelConnection16
        self.model_DiagramModelConnection22 = model_DiagramModelConnection22
        self.model_DiagramModelConnection25 = model_DiagramModelConnection25
        self.model_DiagramModelConnection28 = model_DiagramModelConnection28 if model_DiagramModelConnection28 is not None else set()
        
    @property
    def textPosition(self) -> int:
        return self.__textPosition

    @textPosition.setter
    def textPosition(self, textPosition: int):
        self.__textPosition = textPosition

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def model_DiagramModelConnection22(self):
        return self.__model_DiagramModelConnection22

    @model_DiagramModelConnection22.setter
    def model_DiagramModelConnection22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection22", None)
        self.__model_DiagramModelConnection22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Connectable23"):
                opp_val = getattr(old_value, "model_Connectable23", None)
                if opp_val == self:
                    setattr(old_value, "model_Connectable23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connectable23"):
                opp_val = getattr(value, "model_Connectable23", None)
                setattr(value, "model_Connectable23", self)

    @property
    def model_DiagramModelConnection25(self):
        return self.__model_DiagramModelConnection25

    @model_DiagramModelConnection25.setter
    def model_DiagramModelConnection25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection25", None)
        self.__model_DiagramModelConnection25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Connectable26"):
                opp_val = getattr(old_value, "model_Connectable26", None)
                if opp_val == self:
                    setattr(old_value, "model_Connectable26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connectable26"):
                opp_val = getattr(value, "model_Connectable26", None)
                setattr(value, "model_Connectable26", self)

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
            if hasattr(old_value, "model_Connectable"):
                opp_val = getattr(old_value, "model_Connectable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connectable"):
                opp_val = getattr(value, "model_Connectable", None)
                if opp_val is None:
                    setattr(value, "model_Connectable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelConnection16(self):
        return self.__model_DiagramModelConnection16

    @model_DiagramModelConnection16.setter
    def model_DiagramModelConnection16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection16", None)
        self.__model_DiagramModelConnection16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Connectable15"):
                opp_val = getattr(old_value, "model_Connectable15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connectable15"):
                opp_val = getattr(value, "model_Connectable15", None)
                if opp_val is None:
                    setattr(value, "model_Connectable15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_DiagramModelConnection28(self):
        return self.__model_DiagramModelConnection28

    @model_DiagramModelConnection28.setter
    def model_DiagramModelConnection28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_DiagramModelConnection__model_DiagramModelConnection28", None)
        self.__model_DiagramModelConnection28 = value if value is not None else set()
        
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

    def connect(self, target: Connectable, source: Connectable):
        # TODO: Implement connect method
        pass

class model_DiagramModelImage(BorderObject, Documentable, DiagramModelObject, Properties, DiagramModelImageProvider):

    pass
class FolderContainer:

    pass
class ArchimateModelObject:

    pass
class model_DiagramModel(DiagramModelContainer, ArchimateModelObject, Documentable, Properties):

    def __init__(self, connectionRouterType: int, model_DiagramModel: "model_DiagramModelReference" = None):
        self.connectionRouterType = connectionRouterType
        self.model_DiagramModel = model_DiagramModel
        
    @property
    def connectionRouterType(self) -> int:
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
            if hasattr(old_value, "model_DiagramModelReference"):
                opp_val = getattr(old_value, "model_DiagramModelReference", None)
                if opp_val == self:
                    setattr(old_value, "model_DiagramModelReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_DiagramModelReference"):
                opp_val = getattr(value, "model_DiagramModelReference", None)
                setattr(value, "model_DiagramModelReference", self)

class model_ArchimateModel(ArchimateModelObject, FolderContainer, Properties):

    def __init__(self, purpose: str, file: str, version: str, model_ArchimateModel: "model_Metadata" = None):
        self.purpose = purpose
        self.file = file
        self.version = version
        self.model_ArchimateModel = model_ArchimateModel
        
    @property
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

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
            if hasattr(old_value, "model_Metadata12"):
                opp_val = getattr(old_value, "model_Metadata12", None)
                if opp_val == self:
                    setattr(old_value, "model_Metadata12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Metadata12"):
                opp_val = getattr(value, "model_Metadata12", None)
                setattr(value, "model_Metadata12", self)

    def getDefaultFolderForObject(self, object: str) -> str:
        # TODO: Implement getDefaultFolderForObject method
        pass

    def getDefaultDiagramModel(self) -> str:
        # TODO: Implement getDefaultDiagramModel method
        pass

    def getFolder(self, type: str) -> str:
        # TODO: Implement getFolder method
        pass

    def setDefaults(self):
        # TODO: Implement setDefaults method
        pass

    def getDiagramModels(self) -> str:
        # TODO: Implement getDiagramModels method
        pass

class model_ArchimateConcept(ArchimateModelObject, Cloneable, Documentable, Properties):

    pass
class model_DiagramModelComponent(Cloneable, Nameable, Identifier, Adapter, ArchimateModelObject):

    def __init__(self):
        
    def getDiagramModel(self) -> str:
        # TODO: Implement getDiagramModel method
        pass

class model_Folder(ArchimateModelObject, FolderContainer, Documentable, Properties):

    def __init__(self, type: str, model_Folder: "model_FolderContainer" = None, model_Folder6: set["model_EObject"] = None):
        self.type = type
        self.model_Folder = model_Folder
        self.model_Folder6 = model_Folder6 if model_Folder6 is not None else set()
        
    @property
    def type(self) -> str:
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
    def model_Folder6(self):
        return self.__model_Folder6

    @model_Folder6.setter
    def model_Folder6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Folder__model_Folder6", None)
        self.__model_Folder6 = value if value is not None else set()
        
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
class model_PhysicalElement(ArchimateElement):

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

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_Metadata:

    pass
class model_Features(ABC):

    pass
class model_Feature:

    def __init__(self, name: str, value: str, model_Feature: "model_Features" = None):
        self.name = name
        self.value = value
        self.model_Feature = model_Feature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_Feature(self):
        return self.__model_Feature

    @model_Feature.setter
    def model_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Feature__model_Feature", None)
        self.__model_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Features"):
                opp_val = getattr(old_value, "model_Features", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Features"):
                opp_val = getattr(value, "model_Features", None)
                if opp_val is None:
                    setattr(value, "model_Features", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Properties(ABC):

    pass
class model_Property:

    def __init__(self, key: str, value: str, model_Property: "model_Properties" = None, model_Property3: "model_Metadata" = None):
        self.key = key
        self.value = value
        self.model_Property = model_Property
        self.model_Property3 = model_Property3
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

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

    @property
    def model_Property3(self):
        return self.__model_Property3

    @model_Property3.setter
    def model_Property3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Property__model_Property3", None)
        self.__model_Property3 = value
        
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

class model_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class model_Adapter(ABC):

    def __init__(self):
        
    def setAdapter(self, object: str, adapter: str):
        # TODO: Implement setAdapter method
        pass

    def getAdapter(self, adapter: str) -> str:
        # TODO: Implement getAdapter method
        pass
