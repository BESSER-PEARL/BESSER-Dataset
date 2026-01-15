####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
archimateC2_ArchimateModel = Class(name="archimateC2::ArchimateModel")
archimateC2_ArchimateElement = Class(name="archimateC2::ArchimateElement", is_abstract=True)
archimateC2_PassiveStructure = Class(name="archimateC2::PassiveStructure", is_abstract=True)
ArchimateElement = Class(name="ArchimateElement")
archimateC2_BehaviorElement = Class(name="archimateC2::BehaviorElement", is_abstract=True)
archimateC2_ActiveStructure = Class(name="archimateC2::ActiveStructure", is_abstract=True)
archimateC2_Value = Class(name="archimateC2::Value")
PassiveStructure = Class(name="PassiveStructure")
archimateC2_Product = Class(name="archimateC2::Product")
archimateC2_Contract = Class(name="archimateC2::Contract")
archimateC2_BusinessService = Class(name="archimateC2::BusinessService")
archimateC2_InfrastructureService = Class(name="archimateC2::InfrastructureService")
BusinessObject = Class(name="BusinessObject")
archimateC2_BusinessObject = Class(name="archimateC2::BusinessObject")
archimateC2_Meaning = Class(name="archimateC2::Meaning")
archimateC2_Representation = Class(name="archimateC2::Representation")
archimateC2_Location = Class(name="archimateC2::Location")
archimateC2_BusinessEvent = Class(name="archimateC2::BusinessEvent")
archimateC2_BusinessBehaviorElement = Class(name="archimateC2::BusinessBehaviorElement", is_abstract=True)
archimateC2_ApplicationService = Class(name="archimateC2::ApplicationService")
BehaviorElement = Class(name="BehaviorElement")
archimateC2_BusinessActor = Class(name="archimateC2::BusinessActor")
archimateC2_DataObject = Class(name="archimateC2::DataObject")
archimateC2_BusinessInterface = Class(name="archimateC2::BusinessInterface")
archimateC2_BusinessRole = Class(name="archimateC2::BusinessRole")
archimateC2_ApplicationInterface = Class(name="archimateC2::ApplicationInterface")
archimateC2_ApplicationComponent = Class(name="archimateC2::ApplicationComponent")
archimateC2_BusinessProcess = Class(name="archimateC2::BusinessProcess")
BusinessBehaviorElement = Class(name="BusinessBehaviorElement")
archimateC2_BusinessFunction = Class(name="archimateC2::BusinessFunction")
archimateC2_BusinessInteraction = Class(name="archimateC2::BusinessInteraction")
ActiveStructure = Class(name="ActiveStructure")
archimateC2_Node = Class(name="archimateC2::Node")
archimateC2_Network = Class(name="archimateC2::Network")
archimateC2_CommunicationPath = Class(name="archimateC2::CommunicationPath")
archimateC2_BusinessCollaboration = Class(name="archimateC2::BusinessCollaboration")
archimateC2_Artifact = Class(name="archimateC2::Artifact")
BusinessRole = Class(name="BusinessRole")
archimateC2_ApplicationFunction = Class(name="archimateC2::ApplicationFunction")
archimateC2_ApplicationInteraction = Class(name="archimateC2::ApplicationInteraction")
ApplicationFunction = Class(name="ApplicationFunction")
archimateC2_ApplicationCollaboration = Class(name="archimateC2::ApplicationCollaboration")
archimateC2_InfrastructureInterface = Class(name="archimateC2::InfrastructureInterface")
ApplicationComponent = Class(name="ApplicationComponent")
archimateC2_SystemSoftware = Class(name="archimateC2::SystemSoftware")
Node = Class(name="Node")
archimateC2_Device = Class(name="archimateC2::Device")

# archimateC2_ArchimateModel class attributes and methods

# archimateC2_ArchimateElement class attributes and methods
archimateC2_ArchimateElement_elementName: Property = Property(name="elementName", type=StringType)
archimateC2_ArchimateElement_description: Property = Property(name="description", type=StringType)
archimateC2_ArchimateElement.attributes={archimateC2_ArchimateElement_elementName, archimateC2_ArchimateElement_description}

# archimateC2_PassiveStructure class attributes and methods

# ArchimateElement class attributes and methods

# archimateC2_BehaviorElement class attributes and methods

# archimateC2_ActiveStructure class attributes and methods

# archimateC2_Value class attributes and methods

# PassiveStructure class attributes and methods

# archimateC2_Product class attributes and methods
archimateC2_Product_contract: Property = Property(name="contract", type=StringType)
archimateC2_Product.attributes={archimateC2_Product_contract}

# archimateC2_Contract class attributes and methods

# archimateC2_BusinessService class attributes and methods

# archimateC2_InfrastructureService class attributes and methods

# BusinessObject class attributes and methods

# archimateC2_BusinessObject class attributes and methods

# archimateC2_Meaning class attributes and methods

# archimateC2_Representation class attributes and methods

# archimateC2_Location class attributes and methods
archimateC2_Location_address: Property = Property(name="address", type=StringType)
archimateC2_Location.attributes={archimateC2_Location_address}

# archimateC2_BusinessEvent class attributes and methods

# archimateC2_BusinessBehaviorElement class attributes and methods

# archimateC2_ApplicationService class attributes and methods

# BehaviorElement class attributes and methods

# archimateC2_BusinessActor class attributes and methods

# archimateC2_DataObject class attributes and methods

# archimateC2_BusinessInterface class attributes and methods

# archimateC2_BusinessRole class attributes and methods
archimateC2_BusinessRole_rank: Property = Property(name="rank", type=IntegerType)
archimateC2_BusinessRole.attributes={archimateC2_BusinessRole_rank}

# archimateC2_ApplicationInterface class attributes and methods

# archimateC2_ApplicationComponent class attributes and methods

# archimateC2_BusinessProcess class attributes and methods
archimateC2_BusinessProcess_processID: Property = Property(name="processID", type=StringType)
archimateC2_BusinessProcess_processFullName: Property = Property(name="processFullName", type=StringType)
archimateC2_BusinessProcess_processType: Property = Property(name="processType", type=StringType)
archimateC2_BusinessProcess_importance: Property = Property(name="importance", type=IntegerType)
archimateC2_BusinessProcess_processDesign: Property = Property(name="processDesign", type=StringType)
archimateC2_BusinessProcess_missionary: Property = Property(name="missionary", type=BooleanType)
archimateC2_BusinessProcess.attributes={archimateC2_BusinessProcess_processFullName, archimateC2_BusinessProcess_processDesign, archimateC2_BusinessProcess_importance, archimateC2_BusinessProcess_processType, archimateC2_BusinessProcess_processID, archimateC2_BusinessProcess_missionary}

# BusinessBehaviorElement class attributes and methods

# archimateC2_BusinessFunction class attributes and methods

# archimateC2_BusinessInteraction class attributes and methods

# ActiveStructure class attributes and methods

# archimateC2_Node class attributes and methods

# archimateC2_Network class attributes and methods

# archimateC2_CommunicationPath class attributes and methods

# archimateC2_BusinessCollaboration class attributes and methods
archimateC2_BusinessCollaboration_collaboration: Property = Property(name="collaboration", type=StringType)
archimateC2_BusinessCollaboration.attributes={archimateC2_BusinessCollaboration_collaboration}

# archimateC2_Artifact class attributes and methods

# BusinessRole class attributes and methods

# archimateC2_ApplicationFunction class attributes and methods

# archimateC2_ApplicationInteraction class attributes and methods

# ApplicationFunction class attributes and methods

# archimateC2_ApplicationCollaboration class attributes and methods

# archimateC2_InfrastructureInterface class attributes and methods

# ApplicationComponent class attributes and methods

# archimateC2_SystemSoftware class attributes and methods

# Node class attributes and methods

# archimateC2_Device class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="archimateC2_ArchimateElement", type=archimateC2_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC2_ArchimateModel", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composesElementElement4: BinaryAssociation = BinaryAssociation(
    name="composesElementElement4",
    ends={
        Property(name="ArchimateElement5", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composedOfElementElement", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
aggregatesElementElement7: BinaryAssociation = BinaryAssociation(
    name="aggregatesElementElement7",
    ends={
        Property(name="ArchimateElement8", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByElementElement", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByElementElement10: BinaryAssociation = BinaryAssociation(
    name="aggregatedByElementElement10",
    ends={
        Property(name="ArchimateElement11", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesElementElement", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
associatedWithProductValue12: BinaryAssociation = BinaryAssociation(
    name="associatedWithProductValue12",
    ends={
        Property(name="Product", type=archimateC2_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithValueProduct", type=archimateC2_Product, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithValueProduct13: BinaryAssociation = BinaryAssociation(
    name="associatedWithValueProduct13",
    ends={
        Property(name="Value", type=archimateC2_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithProductValue", type=archimateC2_Value, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesContractProduct14: BinaryAssociation = BinaryAssociation(
    name="aggregatesContractProduct14",
    ends={
        Property(name="Contract", type=archimateC2_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByProductContract", type=archimateC2_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesBusinessServiceProduct15: BinaryAssociation = BinaryAssociation(
    name="aggregatesBusinessServiceProduct15",
    ends={
        Property(name="BusinessService", type=archimateC2_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByProductBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
composedOfElementElement2: BinaryAssociation = BinaryAssociation(
    name="composedOfElementElement2",
    ends={
        Property(name="ArchimateElement", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composesElementElement", type=archimateC2_ArchimateElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregatedByProductInfrastructureService17: BinaryAssociation = BinaryAssociation(
    name="aggregatedByProductInfrastructureService17",
    ends={
        Property(name="InfrastructureService", type=archimateC2_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesProductInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByProductContract18: BinaryAssociation = BinaryAssociation(
    name="aggregatedByProductContract18",
    ends={
        Property(name="Product19", type=archimateC2_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesContractProduct", type=archimateC2_Product, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithMeaningBusinessObject20: BinaryAssociation = BinaryAssociation(
    name="associatedWithMeaningBusinessObject20",
    ends={
        Property(name="Meaning", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithBusinessObjectMeaning", type=archimateC2_Meaning, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByRepresentationBusinessObject21: BinaryAssociation = BinaryAssociation(
    name="realizedByRepresentationBusinessObject21",
    ends={
        Property(name="Representation", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesBusinessObjectRepresentation", type=archimateC2_Representation, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationBusinessObject22: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationBusinessObject22",
    ends={
        Property(name="Location", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromBusinessObjectLocation", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
accessesBusinessEventBusinessObject23: BinaryAssociation = BinaryAssociation(
    name="accessesBusinessEventBusinessObject23",
    ends={
        Property(name="BusinessEvent", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByBusinessObjectBusinessEvent", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByBusinessServiceBusinessObject24: BinaryAssociation = BinaryAssociation(
    name="accessedByBusinessServiceBusinessObject24",
    ends={
        Property(name="BusinessService25", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesBusinessObjectBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByBusinessBehaviorElementBusinessObject26: BinaryAssociation = BinaryAssociation(
    name="accessedByBusinessBehaviorElementBusinessObject26",
    ends={
        Property(name="BusinessBehaviorElement", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesBusinessObjectBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByProductApplicationService16: BinaryAssociation = BinaryAssociation(
    name="aggregatedByProductApplicationService16",
    ends={
        Property(name="ApplicationService", type=archimateC2_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesProductApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithBusinessObjectMeaning28: BinaryAssociation = BinaryAssociation(
    name="associatedWithBusinessObjectMeaning28",
    ends={
        Property(name="BusinessObject", type=archimateC2_Meaning, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithMeaningBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
realizesBusinessObjectRepresentation29: BinaryAssociation = BinaryAssociation(
    name="realizesBusinessObjectRepresentation29",
    ends={
        Property(name="BusinessObject30", type=archimateC2_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByRepresentationBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationRepresentation31: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationRepresentation31",
    ends={
        Property(name="Location32", type=archimateC2_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromRepresentationLocation", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByProductBusinessService33: BinaryAssociation = BinaryAssociation(
    name="aggregatedByProductBusinessService33",
    ends={
        Property(name="Product34", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesBusinessServiceProduct", type=archimateC2_Product, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessActorBusinessService35: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessActorBusinessService35",
    ends={
        Property(name="BusinessActor", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesElementBusinessServiceBusinessActor", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByBusinessBehaviorElementBusinessService36: BinaryAssociation = BinaryAssociation(
    name="realizedByBusinessBehaviorElementBusinessService36",
    ends={
        Property(name="BusinessBehaviorElement37", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="realisesBusinessServiceBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
realizesBusinessObjectDataObject27: BinaryAssociation = BinaryAssociation(
    name="realizesBusinessObjectDataObject27",
    ends={
        Property(name="DataObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByBusinessObjectDataObject", type=archimateC2_DataObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessInterfaceBusinessService40: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessInterfaceBusinessService40",
    ends={
        Property(name="BusinessInterface", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessServiceBusinessInterface", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(0, 9999))
    }
)
accessesBusinessObjectBusinessService41: BinaryAssociation = BinaryAssociation(
    name="accessesBusinessObjectBusinessService41",
    ends={
        Property(name="BusinessObject42", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByBusinessServiceBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
usedByElementBusinessRoleBusinessService43: BinaryAssociation = BinaryAssociation(
    name="usedByElementBusinessRoleBusinessService43",
    ends={
        Property(name="BusinessRole", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesElementBusinessServiceBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessBehaviorElementBusinessService38: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessBehaviorElementBusinessService38",
    ends={
        Property(name="BusinessBehaviorElement39", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessServiceBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
triggersToBusinessBehaviorElementBusinessBehaviorElement46: BinaryAssociation = BinaryAssociation(
    name="triggersToBusinessBehaviorElementBusinessBehaviorElement46",
    ends={
        Property(name="BusinessBehaviorElement47", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredByBusinessBehaviorElementBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
triggeredByBusinessBehaviorElementBusinessBehaviorElement49: BinaryAssociation = BinaryAssociation(
    name="triggeredByBusinessBehaviorElementBusinessBehaviorElement49",
    ends={
        Property(name="BusinessBehaviorElement50", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersToBusinessBehaviorElementBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
flowsFromBusinessBehaviorElementBusinessBehaviorElement52: BinaryAssociation = BinaryAssociation(
    name="flowsFromBusinessBehaviorElementBusinessBehaviorElement52",
    ends={
        Property(name="BusinessBehaviorElement53", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="flowsToBusinessBehaviorElementBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
flowsToBusinessBehaviorElementBusinessBehaviorElement55: BinaryAssociation = BinaryAssociation(
    name="flowsToBusinessBehaviorElementBusinessBehaviorElement55",
    ends={
        Property(name="BusinessBehaviorElement56", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="flowsFromBusinessBehaviorElementBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
triggersBusinessEventBusinessBehaviorElement57: BinaryAssociation = BinaryAssociation(
    name="triggersBusinessEventBusinessBehaviorElement57",
    ends={
        Property(name="BusinessEvent58", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersByBusinessBehaviorElementBusinessEvent", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(0, 9999))
    }
)
triggersByBusinessEventBusinessBehaviorElement59: BinaryAssociation = BinaryAssociation(
    name="triggersByBusinessEventBusinessBehaviorElement59",
    ends={
        Property(name="BusinessEvent60", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersBusinessBehaviorElementBusinessEvent", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(0, 9999))
    }
)
realisesBusinessServiceBusinessBehaviorElement61: BinaryAssociation = BinaryAssociation(
    name="realisesBusinessServiceBusinessBehaviorElement61",
    ends={
        Property(name="BusinessService62", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByBusinessBehaviorElementBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 1))
    }
)
usesBusinessServiceBusinessBehaviorElement63: BinaryAssociation = BinaryAssociation(
    name="usesBusinessServiceBusinessBehaviorElement63",
    ends={
        Property(name="BusinessService64", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessBehaviorElementBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
accessesBusinessObjectBusinessBehaviorElement65: BinaryAssociation = BinaryAssociation(
    name="accessesBusinessObjectBusinessBehaviorElement65",
    ends={
        Property(name="BusinessObject66", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByBusinessBehaviorElementBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
assigedToBusinessServiceApplicationInterface44: BinaryAssociation = BinaryAssociation(
    name="assigedToBusinessServiceApplicationInterface44",
    ends={
        Property(name="ApplicationInterface", type=archimateC2_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromBusinessServiceApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessBehaviorElementApplicationservice69: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessBehaviorElementApplicationservice69",
    ends={
        Property(name="ApplicationService70", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessBehaviorElementApplicationservice", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToApplicationComponentBusinessBehaviorElement71: BinaryAssociation = BinaryAssociation(
    name="assignedToApplicationComponentBusinessBehaviorElement71",
    ends={
        Property(name="ApplicationComponent", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromApplicationComponentBusinessBehaviorElement", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessRoleBusinessBehaviorElement67: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessRoleBusinessBehaviorElement67",
    ends={
        Property(name="BusinessRole68", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessBehaviorElementBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByBusinessObjectBusinessEvent76: BinaryAssociation = BinaryAssociation(
    name="accessedByBusinessObjectBusinessEvent76",
    ends={
        Property(name="BusinessObject77", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesBusinessEventBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromBusinessActorLocation78: BinaryAssociation = BinaryAssociation(
    name="assignedFromBusinessActorLocation78",
    ends={
        Property(name="BusinessActor79", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationBusinessActor", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromBusinessObjectLocation80: BinaryAssociation = BinaryAssociation(
    name="assignedFromBusinessObjectLocation80",
    ends={
        Property(name="BusinessObject81", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationBusinessObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromRepresentationLocation82: BinaryAssociation = BinaryAssociation(
    name="assignedFromRepresentationLocation82",
    ends={
        Property(name="Representation83", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationRepresentation", type=archimateC2_Representation, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationDataObject84: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationDataObject84",
    ends={
        Property(name="DataObject85", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedfromLocationDataObject", type=archimateC2_DataObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromLocationApplicationComponent86: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationApplicationComponent86",
    ends={
        Property(name="ApplicationComponent87", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationApplicationComponent", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromLocationNode88: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationNode88",
    ends={
        Property(name="Node", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromLocationNetwork89: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationNetwork89",
    ends={
        Property(name="archimateC2_Network", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC2_Location", type=archimateC2_Network, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromLocationCommunicationPath90: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationCommunicationPath90",
    ends={
        Property(name="archimateC2_CommunicationPath", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC2_Location91", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(0, 9999))
    }
)
triggersByBusinessBehaviorElementBusinessEvent72: BinaryAssociation = BinaryAssociation(
    name="triggersByBusinessBehaviorElementBusinessEvent72",
    ends={
        Property(name="BusinessBehaviorElement73", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersBusinessEventBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
triggersBusinessBehaviorElementBusinessEvent74: BinaryAssociation = BinaryAssociation(
    name="triggersBusinessBehaviorElementBusinessEvent74",
    ends={
        Property(name="BusinessBehaviorElement75", type=archimateC2_BusinessEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersByBusinessEventBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
composesBusinessRoleBusinessInterface93: BinaryAssociation = BinaryAssociation(
    name="composesBusinessRoleBusinessInterface93",
    ends={
        Property(name="BusinessRole94", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="composedOfBusinessInterfaceBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 1))
    }
)
usedByBusinessActorBusinessInterface95: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessActorBusinessInterface95",
    ends={
        Property(name="BusinessActor96", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessInterfaceBusinessActor", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessRoleBusinessInterface97: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessRoleBusinessInterface97",
    ends={
        Property(name="BusinessRole98", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessInterfaceBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessServiceBusinessInterface99: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessServiceBusinessInterface99",
    ends={
        Property(name="BusinessService100", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessInterfaceBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
composedOfBusinessInterfaceBusinessRole101: BinaryAssociation = BinaryAssociation(
    name="composedOfBusinessInterfaceBusinessRole101",
    ends={
        Property(name="BusinessInterface102", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="composesBusinessRoleBusinessInterface", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesBusinessInterfaceBusinessRole103: BinaryAssociation = BinaryAssociation(
    name="usesBusinessInterfaceBusinessRole103",
    ends={
        Property(name="BusinessInterface104", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessRoleBusinessInterface", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessActorBusinessRole105: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessActorBusinessRole105",
    ends={
        Property(name="BusinessActor106", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessRoleBusinessActor", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByBusinessCollaborationBusinessRole107: BinaryAssociation = BinaryAssociation(
    name="aggregatedByBusinessCollaborationBusinessRole107",
    ends={
        Property(name="BusinessCollaboration", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesBusinessRoleBusinessCollaboration", type=archimateC2_BusinessCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
assignedFromLocationArtifact92: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationArtifact92",
    ends={
        Property(name="Artifact", type=archimateC2_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationArtifact", type=archimateC2_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
usesElementBusinessServiceBusinessRole110: BinaryAssociation = BinaryAssociation(
    name="usesElementBusinessServiceBusinessRole110",
    ends={
        Property(name="usedByElementBusinessRoleBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999)),
        Property(name="BusinessService111", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1))
    }
)
usesBusinessRoleApplicationService112: BinaryAssociation = BinaryAssociation(
    name="usesBusinessRoleApplicationService112",
    ends={
        Property(name="ApplicationService113", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessRoleApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessRoleApplicationInterface114: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessRoleApplicationInterface114",
    ends={
        Property(name="ApplicationInterface115", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessRoleApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesBusinessActorBusinessCollaboration116: BinaryAssociation = BinaryAssociation(
    name="aggregatesBusinessActorBusinessCollaboration116",
    ends={
        Property(name="BusinessActor117", type=archimateC2_BusinessCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesByBusinessCollaborationBusinessActor", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesBusinessRoleBusinessCollaboration118: BinaryAssociation = BinaryAssociation(
    name="aggregatesBusinessRoleBusinessCollaboration118",
    ends={
        Property(name="BusinessRole119", type=archimateC2_BusinessCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByBusinessCollaborationBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesByBusinessCollaborationBusinessActor120: BinaryAssociation = BinaryAssociation(
    name="aggregatesByBusinessCollaborationBusinessActor120",
    ends={
        Property(name="BusinessCollaboration121", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesBusinessActorBusinessCollaboration", type=archimateC2_BusinessCollaboration, multiplicity=Multiplicity(0, 9999))
    }
)
usesBusinessInterfaceBusinessActor122: BinaryAssociation = BinaryAssociation(
    name="usesBusinessInterfaceBusinessActor122",
    ends={
        Property(name="BusinessInterface123", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessActorBusinessInterface", type=archimateC2_BusinessInterface, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessBehaviorElementBusinessRole108: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessBehaviorElementBusinessRole108",
    ends={
        Property(name="BusinessBehaviorElement109", type=archimateC2_BusinessRole, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessRoleBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
usesElementBusinessServiceBusinessActor126: BinaryAssociation = BinaryAssociation(
    name="usesElementBusinessServiceBusinessActor126",
    ends={
        Property(name="BusinessService127", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessActorBusinessService", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationBusinessActor128: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationBusinessActor128",
    ends={
        Property(name="Location129", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromBusinessActorLocation", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
usesBusinessActorApplicationService130: BinaryAssociation = BinaryAssociation(
    name="usesBusinessActorApplicationService130",
    ends={
        Property(name="ApplicationService131", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessActorApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessActorApplicationInterface132: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessActorApplicationInterface132",
    ends={
        Property(name="ApplicationInterface133", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessActorApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByApplicationFunctionDataObject134: BinaryAssociation = BinaryAssociation(
    name="accessedByApplicationFunctionDataObject134",
    ends={
        Property(name="ApplicationFunction", type=archimateC2_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesDataObjectApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByApplicationServiceDataObject135: BinaryAssociation = BinaryAssociation(
    name="accessedByApplicationServiceDataObject135",
    ends={
        Property(name="ApplicationService136", type=archimateC2_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesDataObjectApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByBusinessObjectDataObject137: BinaryAssociation = BinaryAssociation(
    name="realizedByBusinessObjectDataObject137",
    ends={
        Property(name="BusinessObject138", type=archimateC2_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesBusinessObjectDataObject", type=archimateC2_BusinessObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedfromLocationDataObject139: BinaryAssociation = BinaryAssociation(
    name="assignedfromLocationDataObject139",
    ends={
        Property(name="Location140", type=archimateC2_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToLocationDataObject", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByDataObjectArtifact141: BinaryAssociation = BinaryAssociation(
    name="realizedByDataObjectArtifact141",
    ends={
        Property(name="Artifact142", type=archimateC2_DataObject, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesDataObjectArtifact", type=archimateC2_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToBusinessRoleBusinessActor124: BinaryAssociation = BinaryAssociation(
    name="assignedToBusinessRoleBusinessActor124",
    ends={
        Property(name="BusinessRole125", type=archimateC2_BusinessActor, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToBusinessActorBusinessRole", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByApplicationFunctionApplicationService143: BinaryAssociation = BinaryAssociation(
    name="realizedByApplicationFunctionApplicationService143",
    ends={
        Property(name="ApplicationFunction144", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesApplicationServiceApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
usedByApplicationFunctionApplicationService145: BinaryAssociation = BinaryAssociation(
    name="usedByApplicationFunctionApplicationService145",
    ends={
        Property(name="ApplicationFunction146", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesApplicationServiceApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToApplicationInterfaceApplicationService147: BinaryAssociation = BinaryAssociation(
    name="assignedToApplicationInterfaceApplicationService147",
    ends={
        Property(name="ApplicationInterface148", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToApplicationServiceApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999))
    }
)
accessesDataObjectApplicationService149: BinaryAssociation = BinaryAssociation(
    name="accessesDataObjectApplicationService149",
    ends={
        Property(name="DataObject150", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByApplicationServiceDataObject", type=archimateC2_DataObject, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesProductApplicationService151: BinaryAssociation = BinaryAssociation(
    name="aggregatesProductApplicationService151",
    ends={
        Property(name="Product152", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByProductApplicationService", type=archimateC2_Product, multiplicity=Multiplicity(0, 9999))
    }
)
usesBusinessBehaviorElementApplicationservice153: BinaryAssociation = BinaryAssociation(
    name="usesBusinessBehaviorElementApplicationservice153",
    ends={
        Property(name="BusinessBehaviorElement154", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessBehaviorElementApplicationservice", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessRoleApplicationService155: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessRoleApplicationService155",
    ends={
        Property(name="BusinessRole156", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessRoleApplicationService", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
usedByBusinessActorApplicationService157: BinaryAssociation = BinaryAssociation(
    name="usedByBusinessActorApplicationService157",
    ends={
        Property(name="BusinessActor158", type=archimateC2_ApplicationService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesBusinessActorApplicationService", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
triggeredByApplicationFunctionApplicationFunction160: BinaryAssociation = BinaryAssociation(
    name="triggeredByApplicationFunctionApplicationFunction160",
    ends={
        Property(name="ApplicationFunction161", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersToApplicationFunctionApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
flowsToApplicationFunctionApplicationFunction166: BinaryAssociation = BinaryAssociation(
    name="flowsToApplicationFunctionApplicationFunction166",
    ends={
        Property(name="ApplicationFunction167", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="flowsFromApplicationFunctionApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
flowsFromApplicationFunctionApplicationFunction169: BinaryAssociation = BinaryAssociation(
    name="flowsFromApplicationFunctionApplicationFunction169",
    ends={
        Property(name="ApplicationFunction170", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="flowsToApplicationFunctionApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
realizesApplicationServiceApplicationFunction171: BinaryAssociation = BinaryAssociation(
    name="realizesApplicationServiceApplicationFunction171",
    ends={
        Property(name="ApplicationService172", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByApplicationFunctionApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 1))
    }
)
assignedToApplicationComponentApplicationFunction173: BinaryAssociation = BinaryAssociation(
    name="assignedToApplicationComponentApplicationFunction173",
    ends={
        Property(name="ApplicationComponent174", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToApplicationFunctionApplicationComponent", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
usesApplicationServiceApplicationFunction175: BinaryAssociation = BinaryAssociation(
    name="usesApplicationServiceApplicationFunction175",
    ends={
        Property(name="ApplicationService176", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByApplicationFunctionApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
accessesDataObjectApplicationFunction177: BinaryAssociation = BinaryAssociation(
    name="accessesDataObjectApplicationFunction177",
    ends={
        Property(name="DataObject178", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByApplicationFunctionDataObject", type=archimateC2_DataObject, multiplicity=Multiplicity(0, 9999))
    }
)
usesApplicationFunctionInfrastructureService179: BinaryAssociation = BinaryAssociation(
    name="usesApplicationFunctionInfrastructureService179",
    ends={
        Property(name="InfrastructureService180", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByApplicationFunctionInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
triggersToApplicationFunctionApplicationFunction163: BinaryAssociation = BinaryAssociation(
    name="triggersToApplicationFunctionApplicationFunction163",
    ends={
        Property(name="ApplicationFunction164", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="triggeredByApplicationFunctionApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToApplicationServiceApplicationInterface185: BinaryAssociation = BinaryAssociation(
    name="assignedToApplicationServiceApplicationInterface185",
    ends={
        Property(name="ApplicationService186", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToApplicationInterfaceApplicationService", type=archimateC2_ApplicationService, multiplicity=Multiplicity(0, 9999))
    }
)
usesBusinessActorApplicationInterface187: BinaryAssociation = BinaryAssociation(
    name="usesBusinessActorApplicationInterface187",
    ends={
        Property(name="BusinessActor188", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessActorApplicationInterface", type=archimateC2_BusinessActor, multiplicity=Multiplicity(0, 9999))
    }
)
usesBusinessRoleApplicationInterface189: BinaryAssociation = BinaryAssociation(
    name="usesBusinessRoleApplicationInterface189",
    ends={
        Property(name="BusinessRole190", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByBusinessRoleApplicationInterface", type=archimateC2_BusinessRole, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromBusinessServiceApplicationInterface191: BinaryAssociation = BinaryAssociation(
    name="assignedFromBusinessServiceApplicationInterface191",
    ends={
        Property(name="BusinessService192", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="assigedToBusinessServiceApplicationInterface", type=archimateC2_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedByApplicationCollaborationApplicationComponent193: BinaryAssociation = BinaryAssociation(
    name="aggregatedByApplicationCollaborationApplicationComponent193",
    ends={
        Property(name="ApplicationCollaboration", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatesApplicationComponentApplicationCollaboration", type=archimateC2_ApplicationCollaboration, multiplicity=Multiplicity(0, 1))
    }
)
assignedToApplicationFunctionApplicationComponent194: BinaryAssociation = BinaryAssociation(
    name="assignedToApplicationFunctionApplicationComponent194",
    ends={
        Property(name="ApplicationFunction195", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToApplicationComponentApplicationFunction", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
composedOfApplicationInterfaceApplicationComponent196: BinaryAssociation = BinaryAssociation(
    name="composedOfApplicationInterfaceApplicationComponent196",
    ends={
        Property(name="ApplicationInterface197", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="composesApplicationComponentApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesApplicationInterfaceApplicationComponent198: BinaryAssociation = BinaryAssociation(
    name="usesApplicationInterfaceApplicationComponent198",
    ends={
        Property(name="ApplicationInterface199", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByApplicationComponentApplicationInterface", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationApplicationComponent200: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationApplicationComponent200",
    ends={
        Property(name="Location201", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromLocationApplicationComponent", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
composesApplicationComponentApplicationInterface181: BinaryAssociation = BinaryAssociation(
    name="composesApplicationComponentApplicationInterface181",
    ends={
        Property(name="ApplicationComponent182", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="composedOfApplicationInterfaceApplicationComponent", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
usedByApplicationComponentApplicationInterface183: BinaryAssociation = BinaryAssociation(
    name="usedByApplicationComponentApplicationInterface183",
    ends={
        Property(name="ApplicationComponent184", type=archimateC2_ApplicationInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usesApplicationInterfaceApplicationComponent", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByApplicationComponentArtifact204: BinaryAssociation = BinaryAssociation(
    name="realizedByApplicationComponentArtifact204",
    ends={
        Property(name="Artifact205", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesApplicationComponentArtifact", type=archimateC2_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
usesApplicationComponentInfrastructureInterface206: BinaryAssociation = BinaryAssociation(
    name="usesApplicationComponentInfrastructureInterface206",
    ends={
        Property(name="InfrastructureInterface", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByApplicationComponentInfrastructureInterface", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(0, 9999))
    }
)
usesApplicationComponentInfrastructureService207: BinaryAssociation = BinaryAssociation(
    name="usesApplicationComponentInfrastructureService207",
    ends={
        Property(name="InfrastructureService208", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByApplicationComponentInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesApplicationComponentApplicationCollaboration209: BinaryAssociation = BinaryAssociation(
    name="aggregatesApplicationComponentApplicationCollaboration209",
    ends={
        Property(name="ApplicationComponent210", type=archimateC2_ApplicationCollaboration, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByApplicationCollaborationApplicationComponent", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
accessedByInfrastructureServiceArtifact211: BinaryAssociation = BinaryAssociation(
    name="accessedByInfrastructureServiceArtifact211",
    ends={
        Property(name="InfrastructureService212", type=archimateC2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesArtifactInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToNodeArtifact213: BinaryAssociation = BinaryAssociation(
    name="assignedToNodeArtifact213",
    ends={
        Property(name="Node214", type=archimateC2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToArtifactNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationArtifact215: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationArtifact215",
    ends={
        Property(name="Location216", type=archimateC2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromLocationArtifact", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
realizesDataObjectArtifact217: BinaryAssociation = BinaryAssociation(
    name="realizesDataObjectArtifact217",
    ends={
        Property(name="DataObject218", type=archimateC2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByDataObjectArtifact", type=archimateC2_DataObject, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromApplicationComponentBusinessBehaviorElement202: BinaryAssociation = BinaryAssociation(
    name="assignedFromApplicationComponentBusinessBehaviorElement202",
    ends={
        Property(name="BusinessBehaviorElement203", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToApplicationComponentBusinessBehaviorElement", type=archimateC2_BusinessBehaviorElement, multiplicity=Multiplicity(0, 9999))
    }
)
accessesArtifactInfrastructureService221: BinaryAssociation = BinaryAssociation(
    name="accessesArtifactInfrastructureService221",
    ends={
        Property(name="Artifact222", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedByInfrastructureServiceArtifact", type=archimateC2_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToInfrastructureInterfaceInfrastructureService223: BinaryAssociation = BinaryAssociation(
    name="assignedToInfrastructureInterfaceInfrastructureService223",
    ends={
        Property(name="InfrastructureInterface224", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToInfrastructureServiceInfrastructureInterface", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(0, 9999))
    }
)
realizedByNodeInfrastructureService225: BinaryAssociation = BinaryAssociation(
    name="realizedByNodeInfrastructureService225",
    ends={
        Property(name="Node226", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesInfrastructureServiceNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatesProductInfrastructureService227: BinaryAssociation = BinaryAssociation(
    name="aggregatesProductInfrastructureService227",
    ends={
        Property(name="Product228", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregatedByProductInfrastructureService", type=archimateC2_Product, multiplicity=Multiplicity(0, 9999))
    }
)
usedByApplicationComponentInfrastructureService229: BinaryAssociation = BinaryAssociation(
    name="usedByApplicationComponentInfrastructureService229",
    ends={
        Property(name="ApplicationComponent230", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesApplicationComponentInfrastructureService", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
usedByApplicationFunctionInfrastructureService231: BinaryAssociation = BinaryAssociation(
    name="usedByApplicationFunctionInfrastructureService231",
    ends={
        Property(name="ApplicationFunction232", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(1, 1)),
        Property(name="usesApplicationFunctionInfrastructureService", type=archimateC2_ApplicationFunction, multiplicity=Multiplicity(0, 9999))
    }
)
composesNodeInfrastructureInterface233: BinaryAssociation = BinaryAssociation(
    name="composesNodeInfrastructureInterface233",
    ends={
        Property(name="Node234", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="composedOfInfrastructureInterfaceNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 1))
    }
)
assignedToInfrastructureServiceInfrastructureInterface235: BinaryAssociation = BinaryAssociation(
    name="assignedToInfrastructureServiceInfrastructureInterface235",
    ends={
        Property(name="InfrastructureService236", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToInfrastructureInterfaceInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
realizesApplicationComponentArtifact219: BinaryAssociation = BinaryAssociation(
    name="realizesApplicationComponentArtifact219",
    ends={
        Property(name="ApplicationComponent220", type=archimateC2_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByApplicationComponentArtifact", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
usedByApplicationComponentInfrastructureInterface239: BinaryAssociation = BinaryAssociation(
    name="usedByApplicationComponentInfrastructureInterface239",
    ends={
        Property(name="ApplicationComponent240", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usesApplicationComponentInfrastructureInterface", type=archimateC2_ApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithCommunicationPathNode241: BinaryAssociation = BinaryAssociation(
    name="associatedWithCommunicationPathNode241",
    ends={
        Property(name="CommunicationPath", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithNodeCommunicationPath", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(0, 1))
    }
)
assignedToArtifactNode242: BinaryAssociation = BinaryAssociation(
    name="assignedToArtifactNode242",
    ends={
        Property(name="Artifact243", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToNodeArtifact", type=archimateC2_Artifact, multiplicity=Multiplicity(0, 9999))
    }
)
composedOfInfrastructureInterfaceNode244: BinaryAssociation = BinaryAssociation(
    name="composedOfInfrastructureInterfaceNode244",
    ends={
        Property(name="InfrastructureInterface245", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="composesNodeInfrastructureInterface", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesInfrastructureInterfaceNode246: BinaryAssociation = BinaryAssociation(
    name="usesInfrastructureInterfaceNode246",
    ends={
        Property(name="InfrastructureInterface247", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="usedByNodeInfrastructureInterface", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(0, 9999))
    }
)
usesInfrastructureServiceNode248: BinaryAssociation = BinaryAssociation(
    name="usesInfrastructureServiceNode248",
    ends={
        Property(name="InfrastructureService249", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByNodeInfrastructureService", type=archimateC2_InfrastructureService, multiplicity=Multiplicity(0, 9999))
    }
)
assignedToLocationNode250: BinaryAssociation = BinaryAssociation(
    name="assignedToLocationNode250",
    ends={
        Property(name="Location251", type=archimateC2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedFromLocationNode", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
usedByNodeInfrastructureInterface237: BinaryAssociation = BinaryAssociation(
    name="usedByNodeInfrastructureInterface237",
    ends={
        Property(name="Node238", type=archimateC2_InfrastructureInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="usesInfrastructureInterfaceNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithNetworkDevice253: BinaryAssociation = BinaryAssociation(
    name="associatedWithNetworkDevice253",
    ends={
        Property(name="Network", type=archimateC2_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithDeviceNetwork", type=archimateC2_Network, multiplicity=Multiplicity(0, 1))
    }
)
assignedToSystemSoftwareDevice254: BinaryAssociation = BinaryAssociation(
    name="assignedToSystemSoftwareDevice254",
    ends={
        Property(name="SystemSoftware", type=archimateC2_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToDeviceSystemSoftware", type=archimateC2_SystemSoftware, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithNodeCommunicationPath255: BinaryAssociation = BinaryAssociation(
    name="associatedWithNodeCommunicationPath255",
    ends={
        Property(name="Node256", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithCommunicationPathNode", type=archimateC2_Node, multiplicity=Multiplicity(0, 1))
    }
)
realizedByNetworkCommunicationPath257: BinaryAssociation = BinaryAssociation(
    name="realizedByNetworkCommunicationPath257",
    ends={
        Property(name="Network258", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesCommunicationPathNetwork", type=archimateC2_Network, multiplicity=Multiplicity(0, 9999))
    }
)
assignedFromLocationCommunicationPath259: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationCommunicationPath259",
    ends={
        Property(name="archimateC2_Location261", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC2_CommunicationPath260", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)
realizesCommunicationPathNetwork262: BinaryAssociation = BinaryAssociation(
    name="realizesCommunicationPathNetwork262",
    ends={
        Property(name="CommunicationPath263", type=archimateC2_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="realizedByNetworkCommunicationPath", type=archimateC2_CommunicationPath, multiplicity=Multiplicity(0, 1))
    }
)
assignedToDeviceSystemSoftware252: BinaryAssociation = BinaryAssociation(
    name="assignedToDeviceSystemSoftware252",
    ends={
        Property(name="Device", type=archimateC2_SystemSoftware, multiplicity=Multiplicity(1, 1)),
        Property(name="assignedToSystemSoftwareDevice", type=archimateC2_Device, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWithDeviceNetwork264: BinaryAssociation = BinaryAssociation(
    name="associatedWithDeviceNetwork264",
    ends={
        Property(name="Device265", type=archimateC2_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedWithNetworkDevice", type=archimateC2_Device, multiplicity=Multiplicity(0, 1))
    }
)
assignedFromLocationNetwork266: BinaryAssociation = BinaryAssociation(
    name="assignedFromLocationNetwork266",
    ends={
        Property(name="archimateC2_Location268", type=archimateC2_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC2_Network267", type=archimateC2_Location, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_archimateC2_PassiveStructure_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_PassiveStructure)
gen_archimateC2_BehaviorElement_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_BehaviorElement)
gen_archimateC2_ActiveStructure_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_ActiveStructure)
gen_archimateC2_Value_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC2_Value)
gen_archimateC2_Product_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC2_Product)
gen_archimateC2_Contract_BusinessObject = Generalization(general=BusinessObject, specific=archimateC2_Contract)
gen_archimateC2_BusinessObject_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC2_BusinessObject)
gen_archimateC2_Meaning_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC2_Meaning)
gen_archimateC2_Representation_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC2_Representation)
gen_archimateC2_BusinessService_BehaviorElement = Generalization(general=BehaviorElement, specific=archimateC2_BusinessService)
gen_archimateC2_BusinessBehaviorElement_BehaviorElement = Generalization(general=BehaviorElement, specific=archimateC2_BusinessBehaviorElement)
gen_archimateC2_BusinessProcess_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC2_BusinessProcess)
gen_archimateC2_BusinessFunction_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC2_BusinessFunction)
gen_archimateC2_BusinessInteraction_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC2_BusinessInteraction)
gen_archimateC2_BusinessEvent_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_BusinessEvent)
gen_archimateC2_Location_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC2_Location)
gen_archimateC2_BusinessRole_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC2_BusinessRole)
gen_archimateC2_BusinessInterface_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC2_BusinessInterface)
gen_archimateC2_BusinessCollaboration_BusinessRole = Generalization(general=BusinessRole, specific=archimateC2_BusinessCollaboration)
gen_archimateC2_BusinessActor_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC2_BusinessActor)
gen_archimateC2_DataObject_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_DataObject)
gen_archimateC2_ApplicationFunction_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_ApplicationFunction)
gen_archimateC2_ApplicationService_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_ApplicationService)
gen_archimateC2_ApplicationInteraction_ApplicationFunction = Generalization(general=ApplicationFunction, specific=archimateC2_ApplicationInteraction)
gen_archimateC2_ApplicationInterface_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_ApplicationInterface)
gen_archimateC2_ApplicationComponent_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_ApplicationComponent)
gen_archimateC2_ApplicationCollaboration_ApplicationComponent = Generalization(general=ApplicationComponent, specific=archimateC2_ApplicationCollaboration)
gen_archimateC2_Artifact_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_Artifact)
gen_archimateC2_InfrastructureService_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_InfrastructureService)
gen_archimateC2_InfrastructureInterface_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_InfrastructureInterface)
gen_archimateC2_Node_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_Node)
gen_archimateC2_SystemSoftware_Node = Generalization(general=Node, specific=archimateC2_SystemSoftware)
gen_archimateC2_Device_Node = Generalization(general=Node, specific=archimateC2_Device)
gen_archimateC2_CommunicationPath_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_CommunicationPath)
gen_archimateC2_Network_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC2_Network)

# Domain Model
domain_model = DomainModel(
    name="archimateC2",
    types={archimateC2_ArchimateModel, archimateC2_ArchimateElement, archimateC2_PassiveStructure, ArchimateElement, archimateC2_BehaviorElement, archimateC2_ActiveStructure, archimateC2_Value, PassiveStructure, archimateC2_Product, archimateC2_Contract, archimateC2_BusinessService, archimateC2_InfrastructureService, BusinessObject, archimateC2_BusinessObject, archimateC2_Meaning, archimateC2_Representation, archimateC2_Location, archimateC2_BusinessEvent, archimateC2_BusinessBehaviorElement, archimateC2_ApplicationService, BehaviorElement, archimateC2_BusinessActor, archimateC2_DataObject, archimateC2_BusinessInterface, archimateC2_BusinessRole, archimateC2_ApplicationInterface, archimateC2_ApplicationComponent, archimateC2_BusinessProcess, BusinessBehaviorElement, archimateC2_BusinessFunction, archimateC2_BusinessInteraction, ActiveStructure, archimateC2_Node, archimateC2_Network, archimateC2_CommunicationPath, archimateC2_BusinessCollaboration, archimateC2_Artifact, BusinessRole, archimateC2_ApplicationFunction, archimateC2_ApplicationInteraction, ApplicationFunction, archimateC2_ApplicationCollaboration, archimateC2_InfrastructureInterface, ApplicationComponent, archimateC2_SystemSoftware, Node, archimateC2_Device},
    associations={elements0, composesElementElement4, aggregatesElementElement7, aggregatedByElementElement10, associatedWithProductValue12, associatedWithValueProduct13, aggregatesContractProduct14, aggregatesBusinessServiceProduct15, composedOfElementElement2, aggregatedByProductInfrastructureService17, aggregatedByProductContract18, associatedWithMeaningBusinessObject20, realizedByRepresentationBusinessObject21, assignedToLocationBusinessObject22, accessesBusinessEventBusinessObject23, accessedByBusinessServiceBusinessObject24, accessedByBusinessBehaviorElementBusinessObject26, aggregatedByProductApplicationService16, associatedWithBusinessObjectMeaning28, realizesBusinessObjectRepresentation29, assignedToLocationRepresentation31, aggregatedByProductBusinessService33, usedByBusinessActorBusinessService35, realizedByBusinessBehaviorElementBusinessService36, realizesBusinessObjectDataObject27, assignedToBusinessInterfaceBusinessService40, accessesBusinessObjectBusinessService41, usedByElementBusinessRoleBusinessService43, usedByBusinessBehaviorElementBusinessService38, triggersToBusinessBehaviorElementBusinessBehaviorElement46, triggeredByBusinessBehaviorElementBusinessBehaviorElement49, flowsFromBusinessBehaviorElementBusinessBehaviorElement52, flowsToBusinessBehaviorElementBusinessBehaviorElement55, triggersBusinessEventBusinessBehaviorElement57, triggersByBusinessEventBusinessBehaviorElement59, realisesBusinessServiceBusinessBehaviorElement61, usesBusinessServiceBusinessBehaviorElement63, accessesBusinessObjectBusinessBehaviorElement65, assigedToBusinessServiceApplicationInterface44, usedByBusinessBehaviorElementApplicationservice69, assignedToApplicationComponentBusinessBehaviorElement71, assignedToBusinessRoleBusinessBehaviorElement67, accessedByBusinessObjectBusinessEvent76, assignedFromBusinessActorLocation78, assignedFromBusinessObjectLocation80, assignedFromRepresentationLocation82, assignedToLocationDataObject84, assignedFromLocationApplicationComponent86, assignedFromLocationNode88, assignedFromLocationNetwork89, assignedFromLocationCommunicationPath90, triggersByBusinessBehaviorElementBusinessEvent72, triggersBusinessBehaviorElementBusinessEvent74, composesBusinessRoleBusinessInterface93, usedByBusinessActorBusinessInterface95, usedByBusinessRoleBusinessInterface97, assignedToBusinessServiceBusinessInterface99, composedOfBusinessInterfaceBusinessRole101, usesBusinessInterfaceBusinessRole103, assignedToBusinessActorBusinessRole105, aggregatedByBusinessCollaborationBusinessRole107, assignedFromLocationArtifact92, usesElementBusinessServiceBusinessRole110, usesBusinessRoleApplicationService112, usedByBusinessRoleApplicationInterface114, aggregatesBusinessActorBusinessCollaboration116, aggregatesBusinessRoleBusinessCollaboration118, aggregatesByBusinessCollaborationBusinessActor120, usesBusinessInterfaceBusinessActor122, assignedToBusinessBehaviorElementBusinessRole108, usesElementBusinessServiceBusinessActor126, assignedToLocationBusinessActor128, usesBusinessActorApplicationService130, usedByBusinessActorApplicationInterface132, accessedByApplicationFunctionDataObject134, accessedByApplicationServiceDataObject135, realizedByBusinessObjectDataObject137, assignedfromLocationDataObject139, realizedByDataObjectArtifact141, assignedToBusinessRoleBusinessActor124, realizedByApplicationFunctionApplicationService143, usedByApplicationFunctionApplicationService145, assignedToApplicationInterfaceApplicationService147, accessesDataObjectApplicationService149, aggregatesProductApplicationService151, usesBusinessBehaviorElementApplicationservice153, usedByBusinessRoleApplicationService155, usedByBusinessActorApplicationService157, triggeredByApplicationFunctionApplicationFunction160, flowsToApplicationFunctionApplicationFunction166, flowsFromApplicationFunctionApplicationFunction169, realizesApplicationServiceApplicationFunction171, assignedToApplicationComponentApplicationFunction173, usesApplicationServiceApplicationFunction175, accessesDataObjectApplicationFunction177, usesApplicationFunctionInfrastructureService179, triggersToApplicationFunctionApplicationFunction163, assignedToApplicationServiceApplicationInterface185, usesBusinessActorApplicationInterface187, usesBusinessRoleApplicationInterface189, assignedFromBusinessServiceApplicationInterface191, aggregatedByApplicationCollaborationApplicationComponent193, assignedToApplicationFunctionApplicationComponent194, composedOfApplicationInterfaceApplicationComponent196, usesApplicationInterfaceApplicationComponent198, assignedToLocationApplicationComponent200, composesApplicationComponentApplicationInterface181, usedByApplicationComponentApplicationInterface183, realizedByApplicationComponentArtifact204, usesApplicationComponentInfrastructureInterface206, usesApplicationComponentInfrastructureService207, aggregatesApplicationComponentApplicationCollaboration209, accessedByInfrastructureServiceArtifact211, assignedToNodeArtifact213, assignedToLocationArtifact215, realizesDataObjectArtifact217, assignedFromApplicationComponentBusinessBehaviorElement202, accessesArtifactInfrastructureService221, assignedToInfrastructureInterfaceInfrastructureService223, realizedByNodeInfrastructureService225, aggregatesProductInfrastructureService227, usedByApplicationComponentInfrastructureService229, usedByApplicationFunctionInfrastructureService231, composesNodeInfrastructureInterface233, assignedToInfrastructureServiceInfrastructureInterface235, realizesApplicationComponentArtifact219, usedByApplicationComponentInfrastructureInterface239, associatedWithCommunicationPathNode241, assignedToArtifactNode242, composedOfInfrastructureInterfaceNode244, usesInfrastructureInterfaceNode246, usesInfrastructureServiceNode248, assignedToLocationNode250, usedByNodeInfrastructureInterface237, associatedWithNetworkDevice253, assignedToSystemSoftwareDevice254, associatedWithNodeCommunicationPath255, realizedByNetworkCommunicationPath257, assignedFromLocationCommunicationPath259, realizesCommunicationPathNetwork262, assignedToDeviceSystemSoftware252, associatedWithDeviceNetwork264, assignedFromLocationNetwork266},
    generalizations={gen_archimateC2_PassiveStructure_ArchimateElement, gen_archimateC2_BehaviorElement_ArchimateElement, gen_archimateC2_ActiveStructure_ArchimateElement, gen_archimateC2_Value_PassiveStructure, gen_archimateC2_Product_PassiveStructure, gen_archimateC2_Contract_BusinessObject, gen_archimateC2_BusinessObject_PassiveStructure, gen_archimateC2_Meaning_PassiveStructure, gen_archimateC2_Representation_PassiveStructure, gen_archimateC2_BusinessService_BehaviorElement, gen_archimateC2_BusinessBehaviorElement_BehaviorElement, gen_archimateC2_BusinessProcess_BusinessBehaviorElement, gen_archimateC2_BusinessFunction_BusinessBehaviorElement, gen_archimateC2_BusinessInteraction_BusinessBehaviorElement, gen_archimateC2_BusinessEvent_ArchimateElement, gen_archimateC2_Location_ActiveStructure, gen_archimateC2_BusinessRole_ActiveStructure, gen_archimateC2_BusinessInterface_ActiveStructure, gen_archimateC2_BusinessCollaboration_BusinessRole, gen_archimateC2_BusinessActor_ActiveStructure, gen_archimateC2_DataObject_ArchimateElement, gen_archimateC2_ApplicationFunction_ArchimateElement, gen_archimateC2_ApplicationService_ArchimateElement, gen_archimateC2_ApplicationInteraction_ApplicationFunction, gen_archimateC2_ApplicationInterface_ArchimateElement, gen_archimateC2_ApplicationComponent_ArchimateElement, gen_archimateC2_ApplicationCollaboration_ApplicationComponent, gen_archimateC2_Artifact_ArchimateElement, gen_archimateC2_InfrastructureService_ArchimateElement, gen_archimateC2_InfrastructureInterface_ArchimateElement, gen_archimateC2_Node_ArchimateElement, gen_archimateC2_SystemSoftware_Node, gen_archimateC2_Device_Node, gen_archimateC2_CommunicationPath_ArchimateElement, gen_archimateC2_Network_ArchimateElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)