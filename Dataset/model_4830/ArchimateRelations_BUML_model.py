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
archimateC3_ArchimateModel = Class(name="archimateC3::ArchimateModel")
archimateC3_ArchimateElement = Class(name="archimateC3::ArchimateElement", is_abstract=True)
archimateC3_ArchimateRelation = Class(name="archimateC3::ArchimateRelation", is_abstract=True)
archimateC3_Group = Class(name="archimateC3::Group")
archimateC3_ActiveStructure = Class(name="archimateC3::ActiveStructure", is_abstract=True)
archimateC3_value = Class(name="archimateC3::value")
PassiveStructure = Class(name="PassiveStructure")
archimateC3_Product = Class(name="archimateC3::Product")
archimateC3_Contract = Class(name="archimateC3::Contract")
BusinessObject = Class(name="BusinessObject")
archimateC3_BusinessObject = Class(name="archimateC3::BusinessObject")
archimateC3_Meaning = Class(name="archimateC3::Meaning")
archimateC3_Representation = Class(name="archimateC3::Representation")
archimateC3_BusinessService = Class(name="archimateC3::BusinessService")
BehaviorElement = Class(name="BehaviorElement")
archimateC3_BusinessBehaviorElement = Class(name="archimateC3::BusinessBehaviorElement", is_abstract=True)
archimateC3_BusinessProcess = Class(name="archimateC3::BusinessProcess")
BusinessBehaviorElement = Class(name="BusinessBehaviorElement")
archimateC3_BusinessFunction = Class(name="archimateC3::BusinessFunction")
archimateC3_BusinessInteraction = Class(name="archimateC3::BusinessInteraction")
archimateC3_BusinessEvent = Class(name="archimateC3::BusinessEvent")
archimateC3_Location = Class(name="archimateC3::Location")
ActiveStructure = Class(name="ActiveStructure")
archimateC3_BusinessInterface = Class(name="archimateC3::BusinessInterface")
archimateC3_BusinessRole = Class(name="archimateC3::BusinessRole")
archimateC3_BusinessCollaboration = Class(name="archimateC3::BusinessCollaboration")
BusinessRole = Class(name="BusinessRole")
archimateC3_BusinessActor = Class(name="archimateC3::BusinessActor")
archimateC3_DataObject = Class(name="archimateC3::DataObject")
archimateC3_ApplicationService = Class(name="archimateC3::ApplicationService")
archimateC3_ApplicationFunction = Class(name="archimateC3::ApplicationFunction")
archimateC3_ApplicationInteraction = Class(name="archimateC3::ApplicationInteraction")
ApplicationFunction = Class(name="ApplicationFunction")
archimateC3_ApplicationInterface = Class(name="archimateC3::ApplicationInterface")
archimateC3_ApplicationComponent = Class(name="archimateC3::ApplicationComponent")
archimateC3_ApplicationCollaboration = Class(name="archimateC3::ApplicationCollaboration")
ApplicationComponent = Class(name="ApplicationComponent")
archimateC3_Artifact = Class(name="archimateC3::Artifact")
archimateC3_PassiveStructure = Class(name="archimateC3::PassiveStructure", is_abstract=True)
ArchimateElement = Class(name="ArchimateElement")
archimateC3_BehaviorElement = Class(name="archimateC3::BehaviorElement", is_abstract=True)
archimateC3_SystemSoftware = Class(name="archimateC3::SystemSoftware")
Node = Class(name="Node")
archimateC3_Device = Class(name="archimateC3::Device")
archimateC3_CommunicationPath = Class(name="archimateC3::CommunicationPath")
archimateC3_Network = Class(name="archimateC3::Network")
archimateC3_Composition = Class(name="archimateC3::Composition")
ArchimateRelation = Class(name="ArchimateRelation")
archimateC3_Aggregation = Class(name="archimateC3::Aggregation")
archimateC3_Access = Class(name="archimateC3::Access")
archimateC3_Association = Class(name="archimateC3::Association")
archimateC3_Triggering = Class(name="archimateC3::Triggering")
archimateC3_Flow = Class(name="archimateC3::Flow")
archimateC3_Specialization = Class(name="archimateC3::Specialization")
archimateC3_Realization = Class(name="archimateC3::Realization")
archimateC3_Assignment = Class(name="archimateC3::Assignment")
archimateC3_UsedBy = Class(name="archimateC3::UsedBy")
archimateC3_Stakeholder = Class(name="archimateC3::Stakeholder")
archimateC3_Driver = Class(name="archimateC3::Driver")
archimateC3_Assessment = Class(name="archimateC3::Assessment")
archimateC3_Goal = Class(name="archimateC3::Goal")
archimateC3_Requirement = Class(name="archimateC3::Requirement")
archimateC3_Constraint = Class(name="archimateC3::Constraint")
archimateC3_Principle = Class(name="archimateC3::Principle")
archimateC3_WorkPackage = Class(name="archimateC3::WorkPackage")
archimateC3_Deliverable = Class(name="archimateC3::Deliverable")
archimateC3_Plateau = Class(name="archimateC3::Plateau")
archimateC3_Gap = Class(name="archimateC3::Gap")
archimateC3_InfrastructureService = Class(name="archimateC3::InfrastructureService")
archimateC3_InfrastructureInterface = Class(name="archimateC3::InfrastructureInterface")
archimateC3_Node = Class(name="archimateC3::Node")

# archimateC3_ArchimateModel class attributes and methods

# archimateC3_ArchimateElement class attributes and methods
archimateC3_ArchimateElement_elementName: Property = Property(name="elementName", type=StringType)
archimateC3_ArchimateElement_description: Property = Property(name="description", type=StringType)
archimateC3_ArchimateElement.attributes={archimateC3_ArchimateElement_description, archimateC3_ArchimateElement_elementName}

# archimateC3_ArchimateRelation class attributes and methods
archimateC3_ArchimateRelation_connectorName: Property = Property(name="connectorName", type=StringType)
archimateC3_ArchimateRelation.attributes={archimateC3_ArchimateRelation_connectorName}

# archimateC3_Group class attributes and methods
archimateC3_Group_groupName: Property = Property(name="groupName", type=StringType)
archimateC3_Group.attributes={archimateC3_Group_groupName}

# archimateC3_ActiveStructure class attributes and methods

# archimateC3_value class attributes and methods

# PassiveStructure class attributes and methods

# archimateC3_Product class attributes and methods

# archimateC3_Contract class attributes and methods

# BusinessObject class attributes and methods

# archimateC3_BusinessObject class attributes and methods

# archimateC3_Meaning class attributes and methods

# archimateC3_Representation class attributes and methods

# archimateC3_BusinessService class attributes and methods

# BehaviorElement class attributes and methods

# archimateC3_BusinessBehaviorElement class attributes and methods

# archimateC3_BusinessProcess class attributes and methods
archimateC3_BusinessProcess_processID: Property = Property(name="processID", type=StringType)
archimateC3_BusinessProcess_processFullName: Property = Property(name="processFullName", type=StringType)
archimateC3_BusinessProcess_processType: Property = Property(name="processType", type=StringType)
archimateC3_BusinessProcess_importance: Property = Property(name="importance", type=IntegerType)
archimateC3_BusinessProcess_processDesign: Property = Property(name="processDesign", type=StringType)
archimateC3_BusinessProcess_missionary: Property = Property(name="missionary", type=BooleanType)
archimateC3_BusinessProcess.attributes={archimateC3_BusinessProcess_processDesign, archimateC3_BusinessProcess_processFullName, archimateC3_BusinessProcess_processID, archimateC3_BusinessProcess_importance, archimateC3_BusinessProcess_missionary, archimateC3_BusinessProcess_processType}

# BusinessBehaviorElement class attributes and methods

# archimateC3_BusinessFunction class attributes and methods

# archimateC3_BusinessInteraction class attributes and methods

# archimateC3_BusinessEvent class attributes and methods

# archimateC3_Location class attributes and methods
archimateC3_Location_address: Property = Property(name="address", type=StringType)
archimateC3_Location.attributes={archimateC3_Location_address}

# ActiveStructure class attributes and methods

# archimateC3_BusinessInterface class attributes and methods

# archimateC3_BusinessRole class attributes and methods

# archimateC3_BusinessCollaboration class attributes and methods

# BusinessRole class attributes and methods

# archimateC3_BusinessActor class attributes and methods

# archimateC3_DataObject class attributes and methods

# archimateC3_ApplicationService class attributes and methods

# archimateC3_ApplicationFunction class attributes and methods

# archimateC3_ApplicationInteraction class attributes and methods

# ApplicationFunction class attributes and methods

# archimateC3_ApplicationInterface class attributes and methods

# archimateC3_ApplicationComponent class attributes and methods

# archimateC3_ApplicationCollaboration class attributes and methods

# ApplicationComponent class attributes and methods

# archimateC3_Artifact class attributes and methods

# archimateC3_PassiveStructure class attributes and methods

# ArchimateElement class attributes and methods

# archimateC3_BehaviorElement class attributes and methods

# archimateC3_SystemSoftware class attributes and methods

# Node class attributes and methods

# archimateC3_Device class attributes and methods

# archimateC3_CommunicationPath class attributes and methods

# archimateC3_Network class attributes and methods

# archimateC3_Composition class attributes and methods

# ArchimateRelation class attributes and methods

# archimateC3_Aggregation class attributes and methods

# archimateC3_Access class attributes and methods

# archimateC3_Association class attributes and methods

# archimateC3_Triggering class attributes and methods

# archimateC3_Flow class attributes and methods

# archimateC3_Specialization class attributes and methods

# archimateC3_Realization class attributes and methods

# archimateC3_Assignment class attributes and methods

# archimateC3_UsedBy class attributes and methods

# archimateC3_Stakeholder class attributes and methods

# archimateC3_Driver class attributes and methods

# archimateC3_Assessment class attributes and methods

# archimateC3_Goal class attributes and methods

# archimateC3_Requirement class attributes and methods

# archimateC3_Constraint class attributes and methods

# archimateC3_Principle class attributes and methods

# archimateC3_WorkPackage class attributes and methods

# archimateC3_Deliverable class attributes and methods

# archimateC3_Plateau class attributes and methods

# archimateC3_Gap class attributes and methods

# archimateC3_InfrastructureService class attributes and methods

# archimateC3_InfrastructureInterface class attributes and methods

# archimateC3_Node class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="archimateC3_ArchimateElement", type=archimateC3_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_ArchimateModel", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="archimateC3_ArchimateRelation", type=archimateC3_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_ArchimateModel2", type=archimateC3_ArchimateRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups3: BinaryAssociation = BinaryAssociation(
    name="groups3",
    ends={
        Property(name="archimateC3_Group", type=archimateC3_ArchimateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_ArchimateModel4", type=archimateC3_Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composedOf6: BinaryAssociation = BinaryAssociation(
    name="composedOf6",
    ends={
        Property(name="ArchimateElement", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composes", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
composes8: BinaryAssociation = BinaryAssociation(
    name="composes8",
    ends={
        Property(name="ArchimateElement9", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(1, 1)),
        Property(name="composedOf", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
sourceC10: BinaryAssociation = BinaryAssociation(
    name="sourceC10",
    ends={
        Property(name="archimateC3_ArchimateElement12", type=archimateC3_ArchimateRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_ArchimateRelation11", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
targetC13: BinaryAssociation = BinaryAssociation(
    name="targetC13",
    ends={
        Property(name="archimateC3_ArchimateElement15", type=archimateC3_ArchimateRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_ArchimateRelation14", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 1))
    }
)
groupElements16: BinaryAssociation = BinaryAssociation(
    name="groupElements16",
    ends={
        Property(name="archimateC3_ArchimateElement18", type=archimateC3_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="archimateC3_Group17", type=archimateC3_ArchimateElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_archimateC3_ActiveStructure_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_ActiveStructure)
gen_archimateC3_value_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC3_value)
gen_archimateC3_Product_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC3_Product)
gen_archimateC3_Contract_BusinessObject = Generalization(general=BusinessObject, specific=archimateC3_Contract)
gen_archimateC3_BusinessObject_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC3_BusinessObject)
gen_archimateC3_Meaning_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC3_Meaning)
gen_archimateC3_Representation_PassiveStructure = Generalization(general=PassiveStructure, specific=archimateC3_Representation)
gen_archimateC3_BusinessService_BehaviorElement = Generalization(general=BehaviorElement, specific=archimateC3_BusinessService)
gen_archimateC3_BusinessBehaviorElement_BehaviorElement = Generalization(general=BehaviorElement, specific=archimateC3_BusinessBehaviorElement)
gen_archimateC3_BusinessProcess_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC3_BusinessProcess)
gen_archimateC3_BusinessFunction_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC3_BusinessFunction)
gen_archimateC3_BusinessInteraction_BusinessBehaviorElement = Generalization(general=BusinessBehaviorElement, specific=archimateC3_BusinessInteraction)
gen_archimateC3_BusinessEvent_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_BusinessEvent)
gen_archimateC3_Location_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC3_Location)
gen_archimateC3_BusinessInterface_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC3_BusinessInterface)
gen_archimateC3_BusinessRole_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC3_BusinessRole)
gen_archimateC3_BusinessCollaboration_BusinessRole = Generalization(general=BusinessRole, specific=archimateC3_BusinessCollaboration)
gen_archimateC3_BusinessActor_ActiveStructure = Generalization(general=ActiveStructure, specific=archimateC3_BusinessActor)
gen_archimateC3_DataObject_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_DataObject)
gen_archimateC3_ApplicationService_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_ApplicationService)
gen_archimateC3_ApplicationFunction_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_ApplicationFunction)
gen_archimateC3_ApplicationInteraction_ApplicationFunction = Generalization(general=ApplicationFunction, specific=archimateC3_ApplicationInteraction)
gen_archimateC3_ApplicationInterface_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_ApplicationInterface)
gen_archimateC3_ApplicationComponent_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_ApplicationComponent)
gen_archimateC3_ApplicationCollaboration_ApplicationComponent = Generalization(general=ApplicationComponent, specific=archimateC3_ApplicationCollaboration)
gen_archimateC3_Artifact_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Artifact)
gen_archimateC3_PassiveStructure_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_PassiveStructure)
gen_archimateC3_BehaviorElement_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_BehaviorElement)
gen_archimateC3_SystemSoftware_Node = Generalization(general=Node, specific=archimateC3_SystemSoftware)
gen_archimateC3_Device_Node = Generalization(general=Node, specific=archimateC3_Device)
gen_archimateC3_CommunicationPath_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_CommunicationPath)
gen_archimateC3_Network_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Network)
gen_archimateC3_Composition_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Composition)
gen_archimateC3_Aggregation_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Aggregation)
gen_archimateC3_Access_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Access)
gen_archimateC3_Association_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Association)
gen_archimateC3_Triggering_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Triggering)
gen_archimateC3_Flow_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Flow)
gen_archimateC3_Specialization_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Specialization)
gen_archimateC3_Realization_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Realization)
gen_archimateC3_Assignment_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_Assignment)
gen_archimateC3_UsedBy_ArchimateRelation = Generalization(general=ArchimateRelation, specific=archimateC3_UsedBy)
gen_archimateC3_Stakeholder_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Stakeholder)
gen_archimateC3_Driver_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Driver)
gen_archimateC3_Assessment_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Assessment)
gen_archimateC3_Goal_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Goal)
gen_archimateC3_Requirement_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Requirement)
gen_archimateC3_Constraint_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Constraint)
gen_archimateC3_Principle_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Principle)
gen_archimateC3_WorkPackage_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_WorkPackage)
gen_archimateC3_Deliverable_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Deliverable)
gen_archimateC3_Plateau_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Plateau)
gen_archimateC3_Gap_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Gap)
gen_archimateC3_InfrastructureService_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_InfrastructureService)
gen_archimateC3_InfrastructureInterface_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_InfrastructureInterface)
gen_archimateC3_Node_ArchimateElement = Generalization(general=ArchimateElement, specific=archimateC3_Node)

# Domain Model
domain_model = DomainModel(
    name="archimateC3",
    types={archimateC3_ArchimateModel, archimateC3_ArchimateElement, archimateC3_ArchimateRelation, archimateC3_Group, archimateC3_ActiveStructure, archimateC3_value, PassiveStructure, archimateC3_Product, archimateC3_Contract, BusinessObject, archimateC3_BusinessObject, archimateC3_Meaning, archimateC3_Representation, archimateC3_BusinessService, BehaviorElement, archimateC3_BusinessBehaviorElement, archimateC3_BusinessProcess, BusinessBehaviorElement, archimateC3_BusinessFunction, archimateC3_BusinessInteraction, archimateC3_BusinessEvent, archimateC3_Location, ActiveStructure, archimateC3_BusinessInterface, archimateC3_BusinessRole, archimateC3_BusinessCollaboration, BusinessRole, archimateC3_BusinessActor, archimateC3_DataObject, archimateC3_ApplicationService, archimateC3_ApplicationFunction, archimateC3_ApplicationInteraction, ApplicationFunction, archimateC3_ApplicationInterface, archimateC3_ApplicationComponent, archimateC3_ApplicationCollaboration, ApplicationComponent, archimateC3_Artifact, archimateC3_PassiveStructure, ArchimateElement, archimateC3_BehaviorElement, archimateC3_SystemSoftware, Node, archimateC3_Device, archimateC3_CommunicationPath, archimateC3_Network, archimateC3_Composition, ArchimateRelation, archimateC3_Aggregation, archimateC3_Access, archimateC3_Association, archimateC3_Triggering, archimateC3_Flow, archimateC3_Specialization, archimateC3_Realization, archimateC3_Assignment, archimateC3_UsedBy, archimateC3_Stakeholder, archimateC3_Driver, archimateC3_Assessment, archimateC3_Goal, archimateC3_Requirement, archimateC3_Constraint, archimateC3_Principle, archimateC3_WorkPackage, archimateC3_Deliverable, archimateC3_Plateau, archimateC3_Gap, archimateC3_InfrastructureService, archimateC3_InfrastructureInterface, archimateC3_Node},
    associations={elements0, relations1, groups3, composedOf6, composes8, sourceC10, targetC13, groupElements16},
    generalizations={gen_archimateC3_ActiveStructure_ArchimateElement, gen_archimateC3_value_PassiveStructure, gen_archimateC3_Product_PassiveStructure, gen_archimateC3_Contract_BusinessObject, gen_archimateC3_BusinessObject_PassiveStructure, gen_archimateC3_Meaning_PassiveStructure, gen_archimateC3_Representation_PassiveStructure, gen_archimateC3_BusinessService_BehaviorElement, gen_archimateC3_BusinessBehaviorElement_BehaviorElement, gen_archimateC3_BusinessProcess_BusinessBehaviorElement, gen_archimateC3_BusinessFunction_BusinessBehaviorElement, gen_archimateC3_BusinessInteraction_BusinessBehaviorElement, gen_archimateC3_BusinessEvent_ArchimateElement, gen_archimateC3_Location_ActiveStructure, gen_archimateC3_BusinessInterface_ActiveStructure, gen_archimateC3_BusinessRole_ActiveStructure, gen_archimateC3_BusinessCollaboration_BusinessRole, gen_archimateC3_BusinessActor_ActiveStructure, gen_archimateC3_DataObject_ArchimateElement, gen_archimateC3_ApplicationService_ArchimateElement, gen_archimateC3_ApplicationFunction_ArchimateElement, gen_archimateC3_ApplicationInteraction_ApplicationFunction, gen_archimateC3_ApplicationInterface_ArchimateElement, gen_archimateC3_ApplicationComponent_ArchimateElement, gen_archimateC3_ApplicationCollaboration_ApplicationComponent, gen_archimateC3_Artifact_ArchimateElement, gen_archimateC3_PassiveStructure_ArchimateElement, gen_archimateC3_BehaviorElement_ArchimateElement, gen_archimateC3_SystemSoftware_Node, gen_archimateC3_Device_Node, gen_archimateC3_CommunicationPath_ArchimateElement, gen_archimateC3_Network_ArchimateElement, gen_archimateC3_Composition_ArchimateRelation, gen_archimateC3_Aggregation_ArchimateRelation, gen_archimateC3_Access_ArchimateRelation, gen_archimateC3_Association_ArchimateRelation, gen_archimateC3_Triggering_ArchimateRelation, gen_archimateC3_Flow_ArchimateRelation, gen_archimateC3_Specialization_ArchimateRelation, gen_archimateC3_Realization_ArchimateRelation, gen_archimateC3_Assignment_ArchimateRelation, gen_archimateC3_UsedBy_ArchimateRelation, gen_archimateC3_Stakeholder_ArchimateElement, gen_archimateC3_Driver_ArchimateElement, gen_archimateC3_Assessment_ArchimateElement, gen_archimateC3_Goal_ArchimateElement, gen_archimateC3_Requirement_ArchimateElement, gen_archimateC3_Constraint_ArchimateElement, gen_archimateC3_Principle_ArchimateElement, gen_archimateC3_WorkPackage_ArchimateElement, gen_archimateC3_Deliverable_ArchimateElement, gen_archimateC3_Plateau_ArchimateElement, gen_archimateC3_Gap_ArchimateElement, gen_archimateC3_InfrastructureService_ArchimateElement, gen_archimateC3_InfrastructureInterface_ArchimateElement, gen_archimateC3_Node_ArchimateElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)