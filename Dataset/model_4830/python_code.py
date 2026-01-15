from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArchimateRelation:

    pass
class archimateC3_Triggering(ArchimateRelation):

    pass
class archimateC3_Flow(ArchimateRelation):

    pass
class archimateC3_Aggregation(ArchimateRelation):

    pass
class archimateC3_Specialization(ArchimateRelation):

    pass
class archimateC3_UsedBy(ArchimateRelation):

    pass
class archimateC3_Realization(ArchimateRelation):

    pass
class archimateC3_Access(ArchimateRelation):

    pass
class archimateC3_Association(ArchimateRelation):

    pass
class archimateC3_Assignment(ArchimateRelation):

    pass
class archimateC3_Composition(ArchimateRelation):

    pass
class Node:

    pass
class archimateC3_Device(Node):

    pass
class archimateC3_SystemSoftware(Node):

    pass
class ArchimateElement:

    pass
class archimateC3_BehaviorElement(ArchimateElement):

    pass
class archimateC3_WorkPackage(ArchimateElement):

    pass
class archimateC3_Driver(ArchimateElement):

    pass
class archimateC3_InfrastructureInterface(ArchimateElement):

    pass
class archimateC3_InfrastructureService(ArchimateElement):

    pass
class archimateC3_Plateau(ArchimateElement):

    pass
class archimateC3_Requirement(ArchimateElement):

    pass
class archimateC3_Constraint(ArchimateElement):

    pass
class archimateC3_Deliverable(ArchimateElement):

    pass
class archimateC3_Stakeholder(ArchimateElement):

    pass
class archimateC3_Assessment(ArchimateElement):

    pass
class archimateC3_CommunicationPath(ArchimateElement):

    pass
class archimateC3_Gap(ArchimateElement):

    pass
class archimateC3_Node(ArchimateElement):

    pass
class archimateC3_Goal(ArchimateElement):

    pass
class archimateC3_Principle(ArchimateElement):

    pass
class archimateC3_Network(ArchimateElement):

    pass
class archimateC3_PassiveStructure(ArchimateElement):

    pass
class archimateC3_Artifact(ArchimateElement):

    pass
class ApplicationComponent:

    pass
class archimateC3_ApplicationCollaboration(ApplicationComponent):

    pass
class archimateC3_ApplicationComponent(ArchimateElement):

    pass
class archimateC3_ApplicationInterface(ArchimateElement):

    pass
class ApplicationFunction:

    pass
class archimateC3_ApplicationInteraction(ApplicationFunction):

    pass
class archimateC3_ApplicationFunction(ArchimateElement):

    pass
class archimateC3_ApplicationService(ArchimateElement):

    pass
class archimateC3_DataObject(ArchimateElement):

    pass
class BusinessRole:

    pass
class archimateC3_BusinessCollaboration(BusinessRole):

    pass
class ActiveStructure:

    pass
class archimateC3_BusinessRole(ActiveStructure):

    pass
class archimateC3_BusinessInterface(ActiveStructure):

    pass
class archimateC3_BusinessActor(ActiveStructure):

    pass
class archimateC3_Location(ActiveStructure):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class archimateC3_BusinessEvent(ArchimateElement):

    pass
class BusinessBehaviorElement:

    pass
class archimateC3_BusinessFunction(BusinessBehaviorElement):

    pass
class archimateC3_BusinessInteraction(BusinessBehaviorElement):

    pass
class archimateC3_BusinessProcess(BusinessBehaviorElement):

    def __init__(self, processID: str, processFullName: str, processType: str, importance: int, processDesign: str, missionary: bool):
        self.processID = processID
        self.processFullName = processFullName
        self.processType = processType
        self.importance = importance
        self.processDesign = processDesign
        self.missionary = missionary
        
    @property
    def processDesign(self) -> str:
        return self.__processDesign

    @processDesign.setter
    def processDesign(self, processDesign: str):
        self.__processDesign = processDesign

    @property
    def processFullName(self) -> str:
        return self.__processFullName

    @processFullName.setter
    def processFullName(self, processFullName: str):
        self.__processFullName = processFullName

    @property
    def processID(self) -> str:
        return self.__processID

    @processID.setter
    def processID(self, processID: str):
        self.__processID = processID

    @property
    def importance(self) -> int:
        return self.__importance

    @importance.setter
    def importance(self, importance: int):
        self.__importance = importance

    @property
    def missionary(self) -> bool:
        return self.__missionary

    @missionary.setter
    def missionary(self, missionary: bool):
        self.__missionary = missionary

    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

class BehaviorElement:

    pass
class archimateC3_BusinessBehaviorElement(BehaviorElement):

    pass
class archimateC3_BusinessService(BehaviorElement):

    pass
class BusinessObject:

    pass
class archimateC3_Contract(BusinessObject):

    pass
class PassiveStructure:

    pass
class archimateC3_Representation(PassiveStructure):

    pass
class archimateC3_Product(PassiveStructure):

    pass
class archimateC3_BusinessObject(PassiveStructure):

    pass
class archimateC3_Meaning(PassiveStructure):

    pass
class archimateC3_value(PassiveStructure):

    pass
class archimateC3_ActiveStructure(ArchimateElement):

    pass
class archimateC3_Group:

    def __init__(self, groupName: str, archimateC3_Group: "archimateC3_ArchimateModel" = None, archimateC3_Group17: set["archimateC3_ArchimateElement"] = None):
        self.groupName = groupName
        self.archimateC3_Group = archimateC3_Group
        self.archimateC3_Group17 = archimateC3_Group17 if archimateC3_Group17 is not None else set()
        
    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def archimateC3_Group17(self):
        return self.__archimateC3_Group17

    @archimateC3_Group17.setter
    def archimateC3_Group17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_Group__archimateC3_Group17", None)
        self.__archimateC3_Group17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimateC3_ArchimateElement18"):
                    opp_val = getattr(item, "archimateC3_ArchimateElement18", None)
                    
                    if opp_val == self:
                        setattr(item, "archimateC3_ArchimateElement18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimateC3_ArchimateElement18"):
                    opp_val = getattr(item, "archimateC3_ArchimateElement18", None)
                    
                    setattr(item, "archimateC3_ArchimateElement18", self)
                    

    @property
    def archimateC3_Group(self):
        return self.__archimateC3_Group

    @archimateC3_Group.setter
    def archimateC3_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_Group__archimateC3_Group", None)
        self.__archimateC3_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateModel4"):
                opp_val = getattr(old_value, "archimateC3_ArchimateModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateModel4"):
                opp_val = getattr(value, "archimateC3_ArchimateModel4", None)
                if opp_val is None:
                    setattr(value, "archimateC3_ArchimateModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimateC3_ArchimateRelation(ABC):

    def __init__(self, connectorName: str, archimateC3_ArchimateRelation: "archimateC3_ArchimateModel" = None, archimateC3_ArchimateRelation11: "archimateC3_ArchimateElement" = None, archimateC3_ArchimateRelation14: "archimateC3_ArchimateElement" = None):
        self.connectorName = connectorName
        self.archimateC3_ArchimateRelation = archimateC3_ArchimateRelation
        self.archimateC3_ArchimateRelation11 = archimateC3_ArchimateRelation11
        self.archimateC3_ArchimateRelation14 = archimateC3_ArchimateRelation14
        
    @property
    def connectorName(self) -> str:
        return self.__connectorName

    @connectorName.setter
    def connectorName(self, connectorName: str):
        self.__connectorName = connectorName

    @property
    def archimateC3_ArchimateRelation14(self):
        return self.__archimateC3_ArchimateRelation14

    @archimateC3_ArchimateRelation14.setter
    def archimateC3_ArchimateRelation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateRelation__archimateC3_ArchimateRelation14", None)
        self.__archimateC3_ArchimateRelation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateElement15"):
                opp_val = getattr(old_value, "archimateC3_ArchimateElement15", None)
                if opp_val == self:
                    setattr(old_value, "archimateC3_ArchimateElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateElement15"):
                opp_val = getattr(value, "archimateC3_ArchimateElement15", None)
                setattr(value, "archimateC3_ArchimateElement15", self)

    @property
    def archimateC3_ArchimateRelation11(self):
        return self.__archimateC3_ArchimateRelation11

    @archimateC3_ArchimateRelation11.setter
    def archimateC3_ArchimateRelation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateRelation__archimateC3_ArchimateRelation11", None)
        self.__archimateC3_ArchimateRelation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateElement12"):
                opp_val = getattr(old_value, "archimateC3_ArchimateElement12", None)
                if opp_val == self:
                    setattr(old_value, "archimateC3_ArchimateElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateElement12"):
                opp_val = getattr(value, "archimateC3_ArchimateElement12", None)
                setattr(value, "archimateC3_ArchimateElement12", self)

    @property
    def archimateC3_ArchimateRelation(self):
        return self.__archimateC3_ArchimateRelation

    @archimateC3_ArchimateRelation.setter
    def archimateC3_ArchimateRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateRelation__archimateC3_ArchimateRelation", None)
        self.__archimateC3_ArchimateRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateModel2"):
                opp_val = getattr(old_value, "archimateC3_ArchimateModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateModel2"):
                opp_val = getattr(value, "archimateC3_ArchimateModel2", None)
                if opp_val is None:
                    setattr(value, "archimateC3_ArchimateModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimateC3_ArchimateElement(ABC):

    def __init__(self, elementName: str, description: str, archimateC3_ArchimateElement: "archimateC3_ArchimateModel" = None, ArchimateElement: "archimateC3_ArchimateElement" = None, composes: set["archimateC3_ArchimateElement"] = None, ArchimateElement9: "archimateC3_ArchimateElement" = None, composedOf: "archimateC3_ArchimateElement" = None, archimateC3_ArchimateElement12: "archimateC3_ArchimateRelation" = None, archimateC3_ArchimateElement15: "archimateC3_ArchimateRelation" = None, archimateC3_ArchimateElement18: "archimateC3_Group" = None):
        self.elementName = elementName
        self.description = description
        self.archimateC3_ArchimateElement = archimateC3_ArchimateElement
        self.ArchimateElement = ArchimateElement
        self.composes = composes if composes is not None else set()
        self.ArchimateElement9 = ArchimateElement9
        self.composedOf = composedOf
        self.archimateC3_ArchimateElement12 = archimateC3_ArchimateElement12
        self.archimateC3_ArchimateElement15 = archimateC3_ArchimateElement15
        self.archimateC3_ArchimateElement18 = archimateC3_ArchimateElement18
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def archimateC3_ArchimateElement(self):
        return self.__archimateC3_ArchimateElement

    @archimateC3_ArchimateElement.setter
    def archimateC3_ArchimateElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__archimateC3_ArchimateElement", None)
        self.__archimateC3_ArchimateElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateModel"):
                opp_val = getattr(old_value, "archimateC3_ArchimateModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateModel"):
                opp_val = getattr(value, "archimateC3_ArchimateModel", None)
                if opp_val is None:
                    setattr(value, "archimateC3_ArchimateModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimateC3_ArchimateElement18(self):
        return self.__archimateC3_ArchimateElement18

    @archimateC3_ArchimateElement18.setter
    def archimateC3_ArchimateElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__archimateC3_ArchimateElement18", None)
        self.__archimateC3_ArchimateElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_Group17"):
                opp_val = getattr(old_value, "archimateC3_Group17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_Group17"):
                opp_val = getattr(value, "archimateC3_Group17", None)
                if opp_val is None:
                    setattr(value, "archimateC3_Group17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def composes(self):
        return self.__composes

    @composes.setter
    def composes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__composes", None)
        self.__composes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArchimateElement"):
                    opp_val = getattr(item, "ArchimateElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ArchimateElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArchimateElement"):
                    opp_val = getattr(item, "ArchimateElement", None)
                    
                    setattr(item, "ArchimateElement", self)
                    

    @property
    def ArchimateElement9(self):
        return self.__ArchimateElement9

    @ArchimateElement9.setter
    def ArchimateElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__ArchimateElement9", None)
        self.__ArchimateElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composedOf"):
                opp_val = getattr(old_value, "composedOf", None)
                if opp_val == self:
                    setattr(old_value, "composedOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composedOf"):
                opp_val = getattr(value, "composedOf", None)
                setattr(value, "composedOf", self)

    @property
    def archimateC3_ArchimateElement12(self):
        return self.__archimateC3_ArchimateElement12

    @archimateC3_ArchimateElement12.setter
    def archimateC3_ArchimateElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__archimateC3_ArchimateElement12", None)
        self.__archimateC3_ArchimateElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateRelation11"):
                opp_val = getattr(old_value, "archimateC3_ArchimateRelation11", None)
                if opp_val == self:
                    setattr(old_value, "archimateC3_ArchimateRelation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateRelation11"):
                opp_val = getattr(value, "archimateC3_ArchimateRelation11", None)
                setattr(value, "archimateC3_ArchimateRelation11", self)

    @property
    def archimateC3_ArchimateElement15(self):
        return self.__archimateC3_ArchimateElement15

    @archimateC3_ArchimateElement15.setter
    def archimateC3_ArchimateElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__archimateC3_ArchimateElement15", None)
        self.__archimateC3_ArchimateElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC3_ArchimateRelation14"):
                opp_val = getattr(old_value, "archimateC3_ArchimateRelation14", None)
                if opp_val == self:
                    setattr(old_value, "archimateC3_ArchimateRelation14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC3_ArchimateRelation14"):
                opp_val = getattr(value, "archimateC3_ArchimateRelation14", None)
                setattr(value, "archimateC3_ArchimateRelation14", self)

    @property
    def composedOf(self):
        return self.__composedOf

    @composedOf.setter
    def composedOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__composedOf", None)
        self.__composedOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArchimateElement9"):
                opp_val = getattr(old_value, "ArchimateElement9", None)
                if opp_val == self:
                    setattr(old_value, "ArchimateElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArchimateElement9"):
                opp_val = getattr(value, "ArchimateElement9", None)
                setattr(value, "ArchimateElement9", self)

    @property
    def ArchimateElement(self):
        return self.__ArchimateElement

    @ArchimateElement.setter
    def ArchimateElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC3_ArchimateElement__ArchimateElement", None)
        self.__ArchimateElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composes"):
                opp_val = getattr(old_value, "composes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composes"):
                opp_val = getattr(value, "composes", None)
                if opp_val is None:
                    setattr(value, "composes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimateC3_ArchimateModel:

    pass