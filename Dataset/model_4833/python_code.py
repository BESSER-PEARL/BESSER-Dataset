from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class archimateC2_Device(Node):

    pass
class archimateC2_SystemSoftware(Node):

    pass
class ApplicationComponent:

    pass
class archimateC2_ApplicationCollaboration(ApplicationComponent):

    pass
class ApplicationFunction:

    pass
class archimateC2_ApplicationInteraction(ApplicationFunction):

    pass
class BusinessRole:

    pass
class archimateC2_BusinessCollaboration(BusinessRole):

    def __init__(self, collaboration: str, BusinessCollaboration: "archimateC2_BusinessRole" = None, aggregatesByBusinessCollaborationBusinessActor: set["archimateC2_BusinessActor"] = None, aggregatedByBusinessCollaborationBusinessRole: set["archimateC2_BusinessRole"] = None, BusinessCollaboration121: "archimateC2_BusinessActor" = None):
        self.collaboration = collaboration
        self.BusinessCollaboration = BusinessCollaboration
        self.aggregatesByBusinessCollaborationBusinessActor = aggregatesByBusinessCollaborationBusinessActor if aggregatesByBusinessCollaborationBusinessActor is not None else set()
        self.aggregatedByBusinessCollaborationBusinessRole = aggregatedByBusinessCollaborationBusinessRole if aggregatedByBusinessCollaborationBusinessRole is not None else set()
        self.BusinessCollaboration121 = BusinessCollaboration121
        
    @property
    def collaboration(self) -> str:
        return self.__collaboration

    @collaboration.setter
    def collaboration(self, collaboration: str):
        self.__collaboration = collaboration

    @property
    def BusinessCollaboration(self):
        return self.__BusinessCollaboration

    @BusinessCollaboration.setter
    def BusinessCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessCollaboration__BusinessCollaboration", None)
        self.__BusinessCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatesBusinessRoleBusinessCollaboration"):
                opp_val = getattr(old_value, "aggregatesBusinessRoleBusinessCollaboration", None)
                if opp_val == self:
                    setattr(old_value, "aggregatesBusinessRoleBusinessCollaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatesBusinessRoleBusinessCollaboration"):
                opp_val = getattr(value, "aggregatesBusinessRoleBusinessCollaboration", None)
                setattr(value, "aggregatesBusinessRoleBusinessCollaboration", self)

    @property
    def aggregatesByBusinessCollaborationBusinessActor(self):
        return self.__aggregatesByBusinessCollaborationBusinessActor

    @aggregatesByBusinessCollaborationBusinessActor.setter
    def aggregatesByBusinessCollaborationBusinessActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessCollaboration__aggregatesByBusinessCollaborationBusinessActor", None)
        self.__aggregatesByBusinessCollaborationBusinessActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessActor117"):
                    opp_val = getattr(item, "BusinessActor117", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessActor117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessActor117"):
                    opp_val = getattr(item, "BusinessActor117", None)
                    
                    setattr(item, "BusinessActor117", self)
                    

    @property
    def BusinessCollaboration121(self):
        return self.__BusinessCollaboration121

    @BusinessCollaboration121.setter
    def BusinessCollaboration121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessCollaboration__BusinessCollaboration121", None)
        self.__BusinessCollaboration121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatesBusinessActorBusinessCollaboration"):
                opp_val = getattr(old_value, "aggregatesBusinessActorBusinessCollaboration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatesBusinessActorBusinessCollaboration"):
                opp_val = getattr(value, "aggregatesBusinessActorBusinessCollaboration", None)
                if opp_val is None:
                    setattr(value, "aggregatesBusinessActorBusinessCollaboration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregatedByBusinessCollaborationBusinessRole(self):
        return self.__aggregatedByBusinessCollaborationBusinessRole

    @aggregatedByBusinessCollaborationBusinessRole.setter
    def aggregatedByBusinessCollaborationBusinessRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessCollaboration__aggregatedByBusinessCollaborationBusinessRole", None)
        self.__aggregatedByBusinessCollaborationBusinessRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessRole119"):
                    opp_val = getattr(item, "BusinessRole119", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessRole119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessRole119"):
                    opp_val = getattr(item, "BusinessRole119", None)
                    
                    setattr(item, "BusinessRole119", self)
                    

class ActiveStructure:

    pass
class BusinessBehaviorElement:

    pass
class archimateC2_BusinessFunction(BusinessBehaviorElement):

    pass
class archimateC2_BusinessInteraction(BusinessBehaviorElement):

    pass
class archimateC2_BusinessProcess(BusinessBehaviorElement):

    def __init__(self, processID: str, processFullName: str, processType: str, importance: int, processDesign: str, missionary: bool):
        self.processID = processID
        self.processFullName = processFullName
        self.processType = processType
        self.importance = importance
        self.processDesign = processDesign
        self.missionary = missionary
        
    @property
    def processFullName(self) -> str:
        return self.__processFullName

    @processFullName.setter
    def processFullName(self, processFullName: str):
        self.__processFullName = processFullName

    @property
    def processDesign(self) -> str:
        return self.__processDesign

    @processDesign.setter
    def processDesign(self, processDesign: str):
        self.__processDesign = processDesign

    @property
    def importance(self) -> int:
        return self.__importance

    @importance.setter
    def importance(self, importance: int):
        self.__importance = importance

    @property
    def processType(self) -> str:
        return self.__processType

    @processType.setter
    def processType(self, processType: str):
        self.__processType = processType

    @property
    def processID(self) -> str:
        return self.__processID

    @processID.setter
    def processID(self, processID: str):
        self.__processID = processID

    @property
    def missionary(self) -> bool:
        return self.__missionary

    @missionary.setter
    def missionary(self, missionary: bool):
        self.__missionary = missionary

class archimateC2_BusinessRole(ActiveStructure):

    def __init__(self, rank: int, BusinessRole: "archimateC2_BusinessService" = None, BusinessRole68: "archimateC2_BusinessBehaviorElement" = None, BusinessRole94: "archimateC2_BusinessInterface" = None, BusinessRole98: "archimateC2_BusinessInterface" = None, composesBusinessRoleBusinessInterface: set["archimateC2_BusinessInterface"] = None, usedByBusinessRoleBusinessInterface: set["archimateC2_BusinessInterface"] = None, assignedToBusinessRoleBusinessActor: set["archimateC2_BusinessActor"] = None, aggregatesBusinessRoleBusinessCollaboration: "archimateC2_BusinessCollaboration" = None, usedByElementBusinessRoleBusinessService: set["archimateC2_BusinessService"] = None, usedByBusinessRoleApplicationService: set["archimateC2_ApplicationService"] = None, usesBusinessRoleApplicationInterface: set["archimateC2_ApplicationInterface"] = None, BusinessRole119: "archimateC2_BusinessCollaboration" = None, assignedToBusinessRoleBusinessBehaviorElement: set["archimateC2_BusinessBehaviorElement"] = None, BusinessRole125: "archimateC2_BusinessActor" = None, BusinessRole156: "archimateC2_ApplicationService" = None, BusinessRole190: "archimateC2_ApplicationInterface" = None):
        self.rank = rank
        self.BusinessRole = BusinessRole
        self.BusinessRole68 = BusinessRole68
        self.BusinessRole94 = BusinessRole94
        self.BusinessRole98 = BusinessRole98
        self.composesBusinessRoleBusinessInterface = composesBusinessRoleBusinessInterface if composesBusinessRoleBusinessInterface is not None else set()
        self.usedByBusinessRoleBusinessInterface = usedByBusinessRoleBusinessInterface if usedByBusinessRoleBusinessInterface is not None else set()
        self.assignedToBusinessRoleBusinessActor = assignedToBusinessRoleBusinessActor if assignedToBusinessRoleBusinessActor is not None else set()
        self.aggregatesBusinessRoleBusinessCollaboration = aggregatesBusinessRoleBusinessCollaboration
        self.usedByElementBusinessRoleBusinessService = usedByElementBusinessRoleBusinessService if usedByElementBusinessRoleBusinessService is not None else set()
        self.usedByBusinessRoleApplicationService = usedByBusinessRoleApplicationService if usedByBusinessRoleApplicationService is not None else set()
        self.usesBusinessRoleApplicationInterface = usesBusinessRoleApplicationInterface if usesBusinessRoleApplicationInterface is not None else set()
        self.BusinessRole119 = BusinessRole119
        self.assignedToBusinessRoleBusinessBehaviorElement = assignedToBusinessRoleBusinessBehaviorElement if assignedToBusinessRoleBusinessBehaviorElement is not None else set()
        self.BusinessRole125 = BusinessRole125
        self.BusinessRole156 = BusinessRole156
        self.BusinessRole190 = BusinessRole190
        
    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def BusinessRole98(self):
        return self.__BusinessRole98

    @BusinessRole98.setter
    def BusinessRole98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole98", None)
        self.__BusinessRole98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usesBusinessInterfaceBusinessRole"):
                opp_val = getattr(old_value, "usesBusinessInterfaceBusinessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usesBusinessInterfaceBusinessRole"):
                opp_val = getattr(value, "usesBusinessInterfaceBusinessRole", None)
                if opp_val is None:
                    setattr(value, "usesBusinessInterfaceBusinessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def usedByElementBusinessRoleBusinessService(self):
        return self.__usedByElementBusinessRoleBusinessService

    @usedByElementBusinessRoleBusinessService.setter
    def usedByElementBusinessRoleBusinessService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__usedByElementBusinessRoleBusinessService", None)
        self.__usedByElementBusinessRoleBusinessService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessService111"):
                    opp_val = getattr(item, "BusinessService111", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessService111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessService111"):
                    opp_val = getattr(item, "BusinessService111", None)
                    
                    setattr(item, "BusinessService111", self)
                    

    @property
    def usedByBusinessRoleBusinessInterface(self):
        return self.__usedByBusinessRoleBusinessInterface

    @usedByBusinessRoleBusinessInterface.setter
    def usedByBusinessRoleBusinessInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__usedByBusinessRoleBusinessInterface", None)
        self.__usedByBusinessRoleBusinessInterface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessInterface104"):
                    opp_val = getattr(item, "BusinessInterface104", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessInterface104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessInterface104"):
                    opp_val = getattr(item, "BusinessInterface104", None)
                    
                    setattr(item, "BusinessInterface104", self)
                    

    @property
    def aggregatesBusinessRoleBusinessCollaboration(self):
        return self.__aggregatesBusinessRoleBusinessCollaboration

    @aggregatesBusinessRoleBusinessCollaboration.setter
    def aggregatesBusinessRoleBusinessCollaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__aggregatesBusinessRoleBusinessCollaboration", None)
        self.__aggregatesBusinessRoleBusinessCollaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BusinessCollaboration"):
                opp_val = getattr(old_value, "BusinessCollaboration", None)
                if opp_val == self:
                    setattr(old_value, "BusinessCollaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BusinessCollaboration"):
                opp_val = getattr(value, "BusinessCollaboration", None)
                setattr(value, "BusinessCollaboration", self)

    @property
    def assignedToBusinessRoleBusinessBehaviorElement(self):
        return self.__assignedToBusinessRoleBusinessBehaviorElement

    @assignedToBusinessRoleBusinessBehaviorElement.setter
    def assignedToBusinessRoleBusinessBehaviorElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__assignedToBusinessRoleBusinessBehaviorElement", None)
        self.__assignedToBusinessRoleBusinessBehaviorElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessBehaviorElement109"):
                    opp_val = getattr(item, "BusinessBehaviorElement109", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessBehaviorElement109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessBehaviorElement109"):
                    opp_val = getattr(item, "BusinessBehaviorElement109", None)
                    
                    setattr(item, "BusinessBehaviorElement109", self)
                    

    @property
    def assignedToBusinessRoleBusinessActor(self):
        return self.__assignedToBusinessRoleBusinessActor

    @assignedToBusinessRoleBusinessActor.setter
    def assignedToBusinessRoleBusinessActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__assignedToBusinessRoleBusinessActor", None)
        self.__assignedToBusinessRoleBusinessActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessActor106"):
                    opp_val = getattr(item, "BusinessActor106", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessActor106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessActor106"):
                    opp_val = getattr(item, "BusinessActor106", None)
                    
                    setattr(item, "BusinessActor106", self)
                    

    @property
    def usesBusinessRoleApplicationInterface(self):
        return self.__usesBusinessRoleApplicationInterface

    @usesBusinessRoleApplicationInterface.setter
    def usesBusinessRoleApplicationInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__usesBusinessRoleApplicationInterface", None)
        self.__usesBusinessRoleApplicationInterface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationInterface115"):
                    opp_val = getattr(item, "ApplicationInterface115", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationInterface115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationInterface115"):
                    opp_val = getattr(item, "ApplicationInterface115", None)
                    
                    setattr(item, "ApplicationInterface115", self)
                    

    @property
    def BusinessRole(self):
        return self.__BusinessRole

    @BusinessRole.setter
    def BusinessRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole", None)
        self.__BusinessRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usesElementBusinessServiceBusinessRole"):
                opp_val = getattr(old_value, "usesElementBusinessServiceBusinessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usesElementBusinessServiceBusinessRole"):
                opp_val = getattr(value, "usesElementBusinessServiceBusinessRole", None)
                if opp_val is None:
                    setattr(value, "usesElementBusinessServiceBusinessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessRole119(self):
        return self.__BusinessRole119

    @BusinessRole119.setter
    def BusinessRole119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole119", None)
        self.__BusinessRole119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatedByBusinessCollaborationBusinessRole"):
                opp_val = getattr(old_value, "aggregatedByBusinessCollaborationBusinessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatedByBusinessCollaborationBusinessRole"):
                opp_val = getattr(value, "aggregatedByBusinessCollaborationBusinessRole", None)
                if opp_val is None:
                    setattr(value, "aggregatedByBusinessCollaborationBusinessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def usedByBusinessRoleApplicationService(self):
        return self.__usedByBusinessRoleApplicationService

    @usedByBusinessRoleApplicationService.setter
    def usedByBusinessRoleApplicationService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__usedByBusinessRoleApplicationService", None)
        self.__usedByBusinessRoleApplicationService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationService113"):
                    opp_val = getattr(item, "ApplicationService113", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationService113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationService113"):
                    opp_val = getattr(item, "ApplicationService113", None)
                    
                    setattr(item, "ApplicationService113", self)
                    

    @property
    def BusinessRole125(self):
        return self.__BusinessRole125

    @BusinessRole125.setter
    def BusinessRole125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole125", None)
        self.__BusinessRole125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedToBusinessActorBusinessRole"):
                opp_val = getattr(old_value, "assignedToBusinessActorBusinessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedToBusinessActorBusinessRole"):
                opp_val = getattr(value, "assignedToBusinessActorBusinessRole", None)
                if opp_val is None:
                    setattr(value, "assignedToBusinessActorBusinessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessRole68(self):
        return self.__BusinessRole68

    @BusinessRole68.setter
    def BusinessRole68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole68", None)
        self.__BusinessRole68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedToBusinessBehaviorElementBusinessRole"):
                opp_val = getattr(old_value, "assignedToBusinessBehaviorElementBusinessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedToBusinessBehaviorElementBusinessRole"):
                opp_val = getattr(value, "assignedToBusinessBehaviorElementBusinessRole", None)
                if opp_val is None:
                    setattr(value, "assignedToBusinessBehaviorElementBusinessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def composesBusinessRoleBusinessInterface(self):
        return self.__composesBusinessRoleBusinessInterface

    @composesBusinessRoleBusinessInterface.setter
    def composesBusinessRoleBusinessInterface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__composesBusinessRoleBusinessInterface", None)
        self.__composesBusinessRoleBusinessInterface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessInterface102"):
                    opp_val = getattr(item, "BusinessInterface102", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessInterface102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessInterface102"):
                    opp_val = getattr(item, "BusinessInterface102", None)
                    
                    setattr(item, "BusinessInterface102", self)
                    

    @property
    def BusinessRole156(self):
        return self.__BusinessRole156

    @BusinessRole156.setter
    def BusinessRole156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole156", None)
        self.__BusinessRole156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usesBusinessRoleApplicationService"):
                opp_val = getattr(old_value, "usesBusinessRoleApplicationService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usesBusinessRoleApplicationService"):
                opp_val = getattr(value, "usesBusinessRoleApplicationService", None)
                if opp_val is None:
                    setattr(value, "usesBusinessRoleApplicationService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessRole190(self):
        return self.__BusinessRole190

    @BusinessRole190.setter
    def BusinessRole190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole190", None)
        self.__BusinessRole190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "usedByBusinessRoleApplicationInterface"):
                opp_val = getattr(old_value, "usedByBusinessRoleApplicationInterface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "usedByBusinessRoleApplicationInterface"):
                opp_val = getattr(value, "usedByBusinessRoleApplicationInterface", None)
                if opp_val is None:
                    setattr(value, "usedByBusinessRoleApplicationInterface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BusinessRole94(self):
        return self.__BusinessRole94

    @BusinessRole94.setter
    def BusinessRole94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_BusinessRole__BusinessRole94", None)
        self.__BusinessRole94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composedOfBusinessInterfaceBusinessRole"):
                opp_val = getattr(old_value, "composedOfBusinessInterfaceBusinessRole", None)
                if opp_val == self:
                    setattr(old_value, "composedOfBusinessInterfaceBusinessRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composedOfBusinessInterfaceBusinessRole"):
                opp_val = getattr(value, "composedOfBusinessInterfaceBusinessRole", None)
                setattr(value, "composedOfBusinessInterfaceBusinessRole", self)

class archimateC2_BusinessInterface(ActiveStructure):

    pass
class archimateC2_BusinessActor(ActiveStructure):

    pass
class BehaviorElement:

    pass
class archimateC2_BusinessBehaviorElement(BehaviorElement):

    pass
class archimateC2_Location(ActiveStructure):

    def __init__(self, address: str, Location: "archimateC2_BusinessObject" = None, Location32: "archimateC2_Representation" = None, assignedToLocationBusinessActor: set["archimateC2_BusinessActor"] = None, assignedToLocationBusinessObject: set["archimateC2_BusinessObject"] = None, assignedToLocationRepresentation: set["archimateC2_Representation"] = None, assignedfromLocationDataObject: set["archimateC2_DataObject"] = None, assignedToLocationApplicationComponent: set["archimateC2_ApplicationComponent"] = None, assignedToLocationNode: set["archimateC2_Node"] = None, archimateC2_Location: set["archimateC2_Network"] = None, archimateC2_Location91: set["archimateC2_CommunicationPath"] = None, assignedToLocationArtifact: set["archimateC2_Artifact"] = None, Location129: "archimateC2_BusinessActor" = None, Location140: "archimateC2_DataObject" = None, Location201: "archimateC2_ApplicationComponent" = None, Location216: "archimateC2_Artifact" = None, Location251: "archimateC2_Node" = None, archimateC2_Location261: "archimateC2_CommunicationPath" = None, archimateC2_Location268: "archimateC2_Network" = None):
        self.address = address
        self.Location = Location
        self.Location32 = Location32
        self.assignedToLocationBusinessActor = assignedToLocationBusinessActor if assignedToLocationBusinessActor is not None else set()
        self.assignedToLocationBusinessObject = assignedToLocationBusinessObject if assignedToLocationBusinessObject is not None else set()
        self.assignedToLocationRepresentation = assignedToLocationRepresentation if assignedToLocationRepresentation is not None else set()
        self.assignedfromLocationDataObject = assignedfromLocationDataObject if assignedfromLocationDataObject is not None else set()
        self.assignedToLocationApplicationComponent = assignedToLocationApplicationComponent if assignedToLocationApplicationComponent is not None else set()
        self.assignedToLocationNode = assignedToLocationNode if assignedToLocationNode is not None else set()
        self.archimateC2_Location = archimateC2_Location if archimateC2_Location is not None else set()
        self.archimateC2_Location91 = archimateC2_Location91 if archimateC2_Location91 is not None else set()
        self.assignedToLocationArtifact = assignedToLocationArtifact if assignedToLocationArtifact is not None else set()
        self.Location129 = Location129
        self.Location140 = Location140
        self.Location201 = Location201
        self.Location216 = Location216
        self.Location251 = Location251
        self.archimateC2_Location261 = archimateC2_Location261
        self.archimateC2_Location268 = archimateC2_Location268
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def assignedfromLocationDataObject(self):
        return self.__assignedfromLocationDataObject

    @assignedfromLocationDataObject.setter
    def assignedfromLocationDataObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedfromLocationDataObject", None)
        self.__assignedfromLocationDataObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataObject85"):
                    opp_val = getattr(item, "DataObject85", None)
                    
                    if opp_val == self:
                        setattr(item, "DataObject85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataObject85"):
                    opp_val = getattr(item, "DataObject85", None)
                    
                    setattr(item, "DataObject85", self)
                    

    @property
    def assignedToLocationBusinessObject(self):
        return self.__assignedToLocationBusinessObject

    @assignedToLocationBusinessObject.setter
    def assignedToLocationBusinessObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationBusinessObject", None)
        self.__assignedToLocationBusinessObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessObject81"):
                    opp_val = getattr(item, "BusinessObject81", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessObject81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessObject81"):
                    opp_val = getattr(item, "BusinessObject81", None)
                    
                    setattr(item, "BusinessObject81", self)
                    

    @property
    def Location140(self):
        return self.__Location140

    @Location140.setter
    def Location140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location140", None)
        self.__Location140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedToLocationDataObject"):
                opp_val = getattr(old_value, "assignedToLocationDataObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedToLocationDataObject"):
                opp_val = getattr(value, "assignedToLocationDataObject", None)
                if opp_val is None:
                    setattr(value, "assignedToLocationDataObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimateC2_Location(self):
        return self.__archimateC2_Location

    @archimateC2_Location.setter
    def archimateC2_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__archimateC2_Location", None)
        self.__archimateC2_Location = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimateC2_Network"):
                    opp_val = getattr(item, "archimateC2_Network", None)
                    
                    if opp_val == self:
                        setattr(item, "archimateC2_Network", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimateC2_Network"):
                    opp_val = getattr(item, "archimateC2_Network", None)
                    
                    setattr(item, "archimateC2_Network", self)
                    

    @property
    def archimateC2_Location91(self):
        return self.__archimateC2_Location91

    @archimateC2_Location91.setter
    def archimateC2_Location91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__archimateC2_Location91", None)
        self.__archimateC2_Location91 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimateC2_CommunicationPath"):
                    opp_val = getattr(item, "archimateC2_CommunicationPath", None)
                    
                    if opp_val == self:
                        setattr(item, "archimateC2_CommunicationPath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimateC2_CommunicationPath"):
                    opp_val = getattr(item, "archimateC2_CommunicationPath", None)
                    
                    setattr(item, "archimateC2_CommunicationPath", self)
                    

    @property
    def assignedToLocationBusinessActor(self):
        return self.__assignedToLocationBusinessActor

    @assignedToLocationBusinessActor.setter
    def assignedToLocationBusinessActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationBusinessActor", None)
        self.__assignedToLocationBusinessActor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessActor79"):
                    opp_val = getattr(item, "BusinessActor79", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessActor79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessActor79"):
                    opp_val = getattr(item, "BusinessActor79", None)
                    
                    setattr(item, "BusinessActor79", self)
                    

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location", None)
        self.__Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromBusinessObjectLocation"):
                opp_val = getattr(old_value, "assignedFromBusinessObjectLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromBusinessObjectLocation"):
                opp_val = getattr(value, "assignedFromBusinessObjectLocation", None)
                if opp_val is None:
                    setattr(value, "assignedFromBusinessObjectLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Location216(self):
        return self.__Location216

    @Location216.setter
    def Location216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location216", None)
        self.__Location216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromLocationArtifact"):
                opp_val = getattr(old_value, "assignedFromLocationArtifact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromLocationArtifact"):
                opp_val = getattr(value, "assignedFromLocationArtifact", None)
                if opp_val is None:
                    setattr(value, "assignedFromLocationArtifact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimateC2_Location268(self):
        return self.__archimateC2_Location268

    @archimateC2_Location268.setter
    def archimateC2_Location268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__archimateC2_Location268", None)
        self.__archimateC2_Location268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC2_Network267"):
                opp_val = getattr(old_value, "archimateC2_Network267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC2_Network267"):
                opp_val = getattr(value, "archimateC2_Network267", None)
                if opp_val is None:
                    setattr(value, "archimateC2_Network267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignedToLocationRepresentation(self):
        return self.__assignedToLocationRepresentation

    @assignedToLocationRepresentation.setter
    def assignedToLocationRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationRepresentation", None)
        self.__assignedToLocationRepresentation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Representation83"):
                    opp_val = getattr(item, "Representation83", None)
                    
                    if opp_val == self:
                        setattr(item, "Representation83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Representation83"):
                    opp_val = getattr(item, "Representation83", None)
                    
                    setattr(item, "Representation83", self)
                    

    @property
    def Location32(self):
        return self.__Location32

    @Location32.setter
    def Location32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location32", None)
        self.__Location32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromRepresentationLocation"):
                opp_val = getattr(old_value, "assignedFromRepresentationLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromRepresentationLocation"):
                opp_val = getattr(value, "assignedFromRepresentationLocation", None)
                if opp_val is None:
                    setattr(value, "assignedFromRepresentationLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Location201(self):
        return self.__Location201

    @Location201.setter
    def Location201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location201", None)
        self.__Location201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromLocationApplicationComponent"):
                opp_val = getattr(old_value, "assignedFromLocationApplicationComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromLocationApplicationComponent"):
                opp_val = getattr(value, "assignedFromLocationApplicationComponent", None)
                if opp_val is None:
                    setattr(value, "assignedFromLocationApplicationComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignedToLocationArtifact(self):
        return self.__assignedToLocationArtifact

    @assignedToLocationArtifact.setter
    def assignedToLocationArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationArtifact", None)
        self.__assignedToLocationArtifact = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Artifact"):
                    opp_val = getattr(item, "Artifact", None)
                    
                    if opp_val == self:
                        setattr(item, "Artifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Artifact"):
                    opp_val = getattr(item, "Artifact", None)
                    
                    setattr(item, "Artifact", self)
                    

    @property
    def assignedToLocationApplicationComponent(self):
        return self.__assignedToLocationApplicationComponent

    @assignedToLocationApplicationComponent.setter
    def assignedToLocationApplicationComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationApplicationComponent", None)
        self.__assignedToLocationApplicationComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationComponent87"):
                    opp_val = getattr(item, "ApplicationComponent87", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationComponent87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationComponent87"):
                    opp_val = getattr(item, "ApplicationComponent87", None)
                    
                    setattr(item, "ApplicationComponent87", self)
                    

    @property
    def Location251(self):
        return self.__Location251

    @Location251.setter
    def Location251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location251", None)
        self.__Location251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromLocationNode"):
                opp_val = getattr(old_value, "assignedFromLocationNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromLocationNode"):
                opp_val = getattr(value, "assignedFromLocationNode", None)
                if opp_val is None:
                    setattr(value, "assignedFromLocationNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Location129(self):
        return self.__Location129

    @Location129.setter
    def Location129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__Location129", None)
        self.__Location129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignedFromBusinessActorLocation"):
                opp_val = getattr(old_value, "assignedFromBusinessActorLocation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignedFromBusinessActorLocation"):
                opp_val = getattr(value, "assignedFromBusinessActorLocation", None)
                if opp_val is None:
                    setattr(value, "assignedFromBusinessActorLocation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignedToLocationNode(self):
        return self.__assignedToLocationNode

    @assignedToLocationNode.setter
    def assignedToLocationNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__assignedToLocationNode", None)
        self.__assignedToLocationNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def archimateC2_Location261(self):
        return self.__archimateC2_Location261

    @archimateC2_Location261.setter
    def archimateC2_Location261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Location__archimateC2_Location261", None)
        self.__archimateC2_Location261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC2_CommunicationPath260"):
                opp_val = getattr(old_value, "archimateC2_CommunicationPath260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC2_CommunicationPath260"):
                opp_val = getattr(value, "archimateC2_CommunicationPath260", None)
                if opp_val is None:
                    setattr(value, "archimateC2_CommunicationPath260", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BusinessObject:

    pass
class archimateC2_BusinessService(BehaviorElement):

    pass
class archimateC2_Contract(BusinessObject):

    pass
class PassiveStructure:

    pass
class archimateC2_Meaning(PassiveStructure):

    pass
class archimateC2_Product(PassiveStructure):

    def __init__(self, contract: str, Product: "archimateC2_Value" = None, associatedWithProductValue: set["archimateC2_Value"] = None, aggregatedByProductContract: set["archimateC2_Contract"] = None, aggregatedByProductBusinessService: set["archimateC2_BusinessService"] = None, aggregatesProductInfrastructureService: set["archimateC2_InfrastructureService"] = None, Product19: "archimateC2_Contract" = None, aggregatesProductApplicationService: set["archimateC2_ApplicationService"] = None, Product34: "archimateC2_BusinessService" = None, Product152: "archimateC2_ApplicationService" = None, Product228: "archimateC2_InfrastructureService" = None):
        self.contract = contract
        self.Product = Product
        self.associatedWithProductValue = associatedWithProductValue if associatedWithProductValue is not None else set()
        self.aggregatedByProductContract = aggregatedByProductContract if aggregatedByProductContract is not None else set()
        self.aggregatedByProductBusinessService = aggregatedByProductBusinessService if aggregatedByProductBusinessService is not None else set()
        self.aggregatesProductInfrastructureService = aggregatesProductInfrastructureService if aggregatesProductInfrastructureService is not None else set()
        self.Product19 = Product19
        self.aggregatesProductApplicationService = aggregatesProductApplicationService if aggregatesProductApplicationService is not None else set()
        self.Product34 = Product34
        self.Product152 = Product152
        self.Product228 = Product228
        
    @property
    def contract(self) -> str:
        return self.__contract

    @contract.setter
    def contract(self, contract: str):
        self.__contract = contract

    @property
    def aggregatedByProductContract(self):
        return self.__aggregatedByProductContract

    @aggregatedByProductContract.setter
    def aggregatedByProductContract(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__aggregatedByProductContract", None)
        self.__aggregatedByProductContract = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Contract"):
                    opp_val = getattr(item, "Contract", None)
                    
                    if opp_val == self:
                        setattr(item, "Contract", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Contract"):
                    opp_val = getattr(item, "Contract", None)
                    
                    setattr(item, "Contract", self)
                    

    @property
    def aggregatesProductInfrastructureService(self):
        return self.__aggregatesProductInfrastructureService

    @aggregatesProductInfrastructureService.setter
    def aggregatesProductInfrastructureService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__aggregatesProductInfrastructureService", None)
        self.__aggregatesProductInfrastructureService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InfrastructureService"):
                    opp_val = getattr(item, "InfrastructureService", None)
                    
                    if opp_val == self:
                        setattr(item, "InfrastructureService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InfrastructureService"):
                    opp_val = getattr(item, "InfrastructureService", None)
                    
                    setattr(item, "InfrastructureService", self)
                    

    @property
    def Product19(self):
        return self.__Product19

    @Product19.setter
    def Product19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__Product19", None)
        self.__Product19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatesContractProduct"):
                opp_val = getattr(old_value, "aggregatesContractProduct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatesContractProduct"):
                opp_val = getattr(value, "aggregatesContractProduct", None)
                if opp_val is None:
                    setattr(value, "aggregatesContractProduct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregatesProductApplicationService(self):
        return self.__aggregatesProductApplicationService

    @aggregatesProductApplicationService.setter
    def aggregatesProductApplicationService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__aggregatesProductApplicationService", None)
        self.__aggregatesProductApplicationService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ApplicationService"):
                    opp_val = getattr(item, "ApplicationService", None)
                    
                    if opp_val == self:
                        setattr(item, "ApplicationService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ApplicationService"):
                    opp_val = getattr(item, "ApplicationService", None)
                    
                    setattr(item, "ApplicationService", self)
                    

    @property
    def aggregatedByProductBusinessService(self):
        return self.__aggregatedByProductBusinessService

    @aggregatedByProductBusinessService.setter
    def aggregatedByProductBusinessService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__aggregatedByProductBusinessService", None)
        self.__aggregatedByProductBusinessService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BusinessService"):
                    opp_val = getattr(item, "BusinessService", None)
                    
                    if opp_val == self:
                        setattr(item, "BusinessService", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BusinessService"):
                    opp_val = getattr(item, "BusinessService", None)
                    
                    setattr(item, "BusinessService", self)
                    

    @property
    def associatedWithProductValue(self):
        return self.__associatedWithProductValue

    @associatedWithProductValue.setter
    def associatedWithProductValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__associatedWithProductValue", None)
        self.__associatedWithProductValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Value"):
                    opp_val = getattr(item, "Value", None)
                    
                    if opp_val == self:
                        setattr(item, "Value", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Value"):
                    opp_val = getattr(item, "Value", None)
                    
                    setattr(item, "Value", self)
                    

    @property
    def Product34(self):
        return self.__Product34

    @Product34.setter
    def Product34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__Product34", None)
        self.__Product34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatesBusinessServiceProduct"):
                opp_val = getattr(old_value, "aggregatesBusinessServiceProduct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatesBusinessServiceProduct"):
                opp_val = getattr(value, "aggregatesBusinessServiceProduct", None)
                if opp_val is None:
                    setattr(value, "aggregatesBusinessServiceProduct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Product152(self):
        return self.__Product152

    @Product152.setter
    def Product152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__Product152", None)
        self.__Product152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatedByProductApplicationService"):
                opp_val = getattr(old_value, "aggregatedByProductApplicationService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatedByProductApplicationService"):
                opp_val = getattr(value, "aggregatedByProductApplicationService", None)
                if opp_val is None:
                    setattr(value, "aggregatedByProductApplicationService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Product228(self):
        return self.__Product228

    @Product228.setter
    def Product228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__Product228", None)
        self.__Product228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatedByProductInfrastructureService"):
                opp_val = getattr(old_value, "aggregatedByProductInfrastructureService", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatedByProductInfrastructureService"):
                opp_val = getattr(value, "aggregatedByProductInfrastructureService", None)
                if opp_val is None:
                    setattr(value, "aggregatedByProductInfrastructureService", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Product(self):
        return self.__Product

    @Product.setter
    def Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_Product__Product", None)
        self.__Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associatedWithValueProduct"):
                opp_val = getattr(old_value, "associatedWithValueProduct", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associatedWithValueProduct"):
                opp_val = getattr(value, "associatedWithValueProduct", None)
                if opp_val is None:
                    setattr(value, "associatedWithValueProduct", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimateC2_BusinessObject(PassiveStructure):

    pass
class archimateC2_Representation(PassiveStructure):

    pass
class archimateC2_Value(PassiveStructure):

    pass
class ArchimateElement:

    pass
class archimateC2_Artifact(ArchimateElement):

    pass
class archimateC2_BehaviorElement(ArchimateElement):

    pass
class archimateC2_ApplicationComponent(ArchimateElement):

    pass
class archimateC2_ApplicationService(ArchimateElement):

    pass
class archimateC2_BusinessEvent(ArchimateElement):

    pass
class archimateC2_InfrastructureInterface(ArchimateElement):

    pass
class archimateC2_CommunicationPath(ArchimateElement):

    pass
class archimateC2_ActiveStructure(ArchimateElement):

    pass
class archimateC2_ApplicationFunction(ArchimateElement):

    pass
class archimateC2_Network(ArchimateElement):

    pass
class archimateC2_Node(ArchimateElement):

    pass
class archimateC2_ApplicationInterface(ArchimateElement):

    pass
class archimateC2_DataObject(ArchimateElement):

    pass
class archimateC2_InfrastructureService(ArchimateElement):

    pass
class archimateC2_PassiveStructure(ArchimateElement):

    pass
class archimateC2_ArchimateElement(ABC):

    def __init__(self, elementName: str, description: str, archimateC2_ArchimateElement: "archimateC2_ArchimateModel" = None, ArchimateElement5: "archimateC2_ArchimateElement" = None, composedOfElementElement: "archimateC2_ArchimateElement" = None, ArchimateElement8: "archimateC2_ArchimateElement" = None, aggregatedByElementElement: set["archimateC2_ArchimateElement"] = None, ArchimateElement11: "archimateC2_ArchimateElement" = None, aggregatesElementElement: "archimateC2_ArchimateElement" = None, ArchimateElement: "archimateC2_ArchimateElement" = None, composesElementElement: set["archimateC2_ArchimateElement"] = None):
        self.elementName = elementName
        self.description = description
        self.archimateC2_ArchimateElement = archimateC2_ArchimateElement
        self.ArchimateElement5 = ArchimateElement5
        self.composedOfElementElement = composedOfElementElement
        self.ArchimateElement8 = ArchimateElement8
        self.aggregatedByElementElement = aggregatedByElementElement if aggregatedByElementElement is not None else set()
        self.ArchimateElement11 = ArchimateElement11
        self.aggregatesElementElement = aggregatesElementElement
        self.ArchimateElement = ArchimateElement
        self.composesElementElement = composesElementElement if composesElementElement is not None else set()
        
    @property
    def elementName(self) -> str:
        return self.__elementName

    @elementName.setter
    def elementName(self, elementName: str):
        self.__elementName = elementName

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def archimateC2_ArchimateElement(self):
        return self.__archimateC2_ArchimateElement

    @archimateC2_ArchimateElement.setter
    def archimateC2_ArchimateElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__archimateC2_ArchimateElement", None)
        self.__archimateC2_ArchimateElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimateC2_ArchimateModel"):
                opp_val = getattr(old_value, "archimateC2_ArchimateModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimateC2_ArchimateModel"):
                opp_val = getattr(value, "archimateC2_ArchimateModel", None)
                if opp_val is None:
                    setattr(value, "archimateC2_ArchimateModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ArchimateElement5(self):
        return self.__ArchimateElement5

    @ArchimateElement5.setter
    def ArchimateElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__ArchimateElement5", None)
        self.__ArchimateElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composedOfElementElement"):
                opp_val = getattr(old_value, "composedOfElementElement", None)
                if opp_val == self:
                    setattr(old_value, "composedOfElementElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composedOfElementElement"):
                opp_val = getattr(value, "composedOfElementElement", None)
                setattr(value, "composedOfElementElement", self)

    @property
    def ArchimateElement11(self):
        return self.__ArchimateElement11

    @ArchimateElement11.setter
    def ArchimateElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__ArchimateElement11", None)
        self.__ArchimateElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatesElementElement"):
                opp_val = getattr(old_value, "aggregatesElementElement", None)
                if opp_val == self:
                    setattr(old_value, "aggregatesElementElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatesElementElement"):
                opp_val = getattr(value, "aggregatesElementElement", None)
                setattr(value, "aggregatesElementElement", self)

    @property
    def aggregatedByElementElement(self):
        return self.__aggregatedByElementElement

    @aggregatedByElementElement.setter
    def aggregatedByElementElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__aggregatedByElementElement", None)
        self.__aggregatedByElementElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArchimateElement8"):
                    opp_val = getattr(item, "ArchimateElement8", None)
                    
                    if opp_val == self:
                        setattr(item, "ArchimateElement8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArchimateElement8"):
                    opp_val = getattr(item, "ArchimateElement8", None)
                    
                    setattr(item, "ArchimateElement8", self)
                    

    @property
    def composedOfElementElement(self):
        return self.__composedOfElementElement

    @composedOfElementElement.setter
    def composedOfElementElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__composedOfElementElement", None)
        self.__composedOfElementElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArchimateElement5"):
                opp_val = getattr(old_value, "ArchimateElement5", None)
                if opp_val == self:
                    setattr(old_value, "ArchimateElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArchimateElement5"):
                opp_val = getattr(value, "ArchimateElement5", None)
                setattr(value, "ArchimateElement5", self)

    @property
    def ArchimateElement8(self):
        return self.__ArchimateElement8

    @ArchimateElement8.setter
    def ArchimateElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__ArchimateElement8", None)
        self.__ArchimateElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aggregatedByElementElement"):
                opp_val = getattr(old_value, "aggregatedByElementElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aggregatedByElementElement"):
                opp_val = getattr(value, "aggregatedByElementElement", None)
                if opp_val is None:
                    setattr(value, "aggregatedByElementElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def aggregatesElementElement(self):
        return self.__aggregatesElementElement

    @aggregatesElementElement.setter
    def aggregatesElementElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__aggregatesElementElement", None)
        self.__aggregatesElementElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArchimateElement11"):
                opp_val = getattr(old_value, "ArchimateElement11", None)
                if opp_val == self:
                    setattr(old_value, "ArchimateElement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArchimateElement11"):
                opp_val = getattr(value, "ArchimateElement11", None)
                setattr(value, "ArchimateElement11", self)

    @property
    def ArchimateElement(self):
        return self.__ArchimateElement

    @ArchimateElement.setter
    def ArchimateElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__ArchimateElement", None)
        self.__ArchimateElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composesElementElement"):
                opp_val = getattr(old_value, "composesElementElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composesElementElement"):
                opp_val = getattr(value, "composesElementElement", None)
                if opp_val is None:
                    setattr(value, "composesElementElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def composesElementElement(self):
        return self.__composesElementElement

    @composesElementElement.setter
    def composesElementElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimateC2_ArchimateElement__composesElementElement", None)
        self.__composesElementElement = value if value is not None else set()
        
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
                    

class archimateC2_ArchimateModel:

    pass