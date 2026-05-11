from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ImplementationAndMigrationConcept:

    pass
class archimate_Plateau(ImplementationAndMigrationConcept):

    pass
class archimate_Deliverable(ImplementationAndMigrationConcept):

    pass
class archimate_Gap(ImplementationAndMigrationConcept):

    pass
class archimate_WorkPackage(ImplementationAndMigrationConcept):

    pass
class Requirement:

    pass
class archimate_Constraint(Requirement):

    pass
class MotivationConcept:

    pass
class archimate_Driver(MotivationConcept):

    pass
class archimate_Requirement(MotivationConcept):

    pass
class archimate_Assessment(MotivationConcept):

    pass
class archimate_Principle(MotivationConcept):

    pass
class archimate_Goal(MotivationConcept):

    pass
class archimate_Stakeholder(MotivationConcept):

    pass
class Node:

    pass
class archimate_SystemSoftware(Node):

    pass
class archimate_Device(Node):

    pass
class TechnologyConcept:

    pass
class ApplicationConcept:

    pass
class archimate_ApplicationCollaboration(ApplicationConcept):

    pass
class BusinessObject:

    pass
class archimate_Contract(BusinessObject):

    pass
class Behavior:

    pass
class archimate_ApplicationService(Behavior, ApplicationConcept):

    pass
class archimate_InfrastructureService(Behavior, TechnologyConcept):

    pass
class archimate_ApplicationInteraction(Behavior, ApplicationConcept):

    pass
class archimate_InfrastructureFunction(Behavior, TechnologyConcept):

    pass
class archimate_ApplicationFunction(Behavior, ApplicationConcept):

    pass
class Passive:

    pass
class archimate_Artifact(Passive, ApplicationConcept):

    pass
class archimate_DataObject(Passive, ApplicationConcept):

    pass
class Active:

    pass
class archimate_CommunicationPath(TechnologyConcept, Active):

    pass
class archimate_ApplicationInterface(ApplicationConcept, Active):

    pass
class archimate_Node(TechnologyConcept, Active):

    pass
class archimate_Network(TechnologyConcept, Active):

    pass
class archimate_ApplicationComponent(ApplicationConcept, Active):

    pass
class archimate_InfrastructureInterface(TechnologyConcept, Active):

    pass
class BusinessConcept:

    pass
class archimate_BusinessService(BusinessConcept, Behavior):

    pass
class archimate_BusinessFunction(BusinessConcept, Behavior):

    pass
class archimate_Location(BusinessConcept, Active):

    pass
class archimate_BusinessInterface(BusinessConcept, Active):

    pass
class archimate_Representation(BusinessConcept, Passive):

    pass
class archimate_Meaning(BusinessConcept, Passive):

    pass
class archimate_BusinessEvent(BusinessConcept, Behavior):

    pass
class archimate_Product(BusinessConcept, Passive):

    pass
class archimate_BusinessProcess(BusinessConcept, Behavior):

    pass
class archimate_BusinessObject(BusinessConcept, Passive):

    pass
class archimate_BusinessCollaboration(BusinessConcept):

    pass
class archimate_BusinessInteraction(BusinessConcept, Behavior):

    pass
class archimate_Value(BusinessConcept, Passive):

    pass
class archimate_BusinessRole(BusinessConcept, Active):

    pass
class archimate_BusinessActor(BusinessConcept, Active):

    pass
class archimate_Active(ABC):

    pass
class archimate_Behavior(ABC):

    pass
class archimate_Passive(ABC):

    pass
class Concept:

    pass
class archimate_MotivationConcept(Concept):

    pass
class archimate_ImplementationAndMigrationConcept(Concept):

    pass
class archimate_ApplicationConcept(Concept):

    pass
class archimate_TechnologyConcept(Concept):

    pass
class archimate_BusinessConcept(Concept):

    pass
class archimate_Concept(ABC):

    def __init__(self, name: str, description: str, archimate_Concept: "archimate_Concept" = None, archimate_Concept0: set["archimate_Concept"] = None):
        self.name = name
        self.description = description
        self.archimate_Concept = archimate_Concept
        self.archimate_Concept0 = archimate_Concept0 if archimate_Concept0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def archimate_Concept(self):
        return self.__archimate_Concept

    @archimate_Concept.setter
    def archimate_Concept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_Concept__archimate_Concept", None)
        self.__archimate_Concept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_Concept0"):
                opp_val = getattr(old_value, "archimate_Concept0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_Concept0"):
                opp_val = getattr(value, "archimate_Concept0", None)
                if opp_val is None:
                    setattr(value, "archimate_Concept0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_Concept0(self):
        return self.__archimate_Concept0

    @archimate_Concept0.setter
    def archimate_Concept0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_Concept__archimate_Concept0", None)
        self.__archimate_Concept0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_Concept"):
                    opp_val = getattr(item, "archimate_Concept", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_Concept", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_Concept"):
                    opp_val = getattr(item, "archimate_Concept", None)
                    
                    setattr(item, "archimate_Concept", self)
                    
