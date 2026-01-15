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
archimate_Concept = Class(name="archimate::Concept", is_abstract=True)
archimate_BusinessConcept = Class(name="archimate::BusinessConcept", is_abstract=True)
Concept = Class(name="Concept")
archimate_ApplicationConcept = Class(name="archimate::ApplicationConcept", is_abstract=True)
archimate_TechnologyConcept = Class(name="archimate::TechnologyConcept", is_abstract=True)
archimate_MotivationConcept = Class(name="archimate::MotivationConcept", is_abstract=True)
archimate_ImplementationAndMigrationConcept = Class(name="archimate::ImplementationAndMigrationConcept", is_abstract=True)
archimate_Passive = Class(name="archimate::Passive", is_abstract=True)
archimate_Behavior = Class(name="archimate::Behavior", is_abstract=True)
archimate_Active = Class(name="archimate::Active", is_abstract=True)
archimate_BusinessEvent = Class(name="archimate::BusinessEvent")
archimate_BusinessService = Class(name="archimate::BusinessService")
archimate_Representation = Class(name="archimate::Representation")
archimate_Meaning = Class(name="archimate::Meaning")
archimate_Value = Class(name="archimate::Value")
archimate_Product = Class(name="archimate::Product")
archimate_Contract = Class(name="archimate::Contract")
BusinessObject = Class(name="BusinessObject")
archimate_ApplicationComponent = Class(name="archimate::ApplicationComponent")
ApplicationConcept = Class(name="ApplicationConcept")
archimate_ApplicationCollaboration = Class(name="archimate::ApplicationCollaboration")
archimate_ApplicationInterface = Class(name="archimate::ApplicationInterface")
archimate_BusinessActor = Class(name="archimate::BusinessActor")
BusinessConcept = Class(name="BusinessConcept")
Active = Class(name="Active")
archimate_BusinessRole = Class(name="archimate::BusinessRole")
archimate_BusinessCollaboration = Class(name="archimate::BusinessCollaboration")
archimate_BusinessInterface = Class(name="archimate::BusinessInterface")
archimate_Location = Class(name="archimate::Location")
archimate_BusinessObject = Class(name="archimate::BusinessObject")
Passive = Class(name="Passive")
archimate_BusinessProcess = Class(name="archimate::BusinessProcess")
Behavior = Class(name="Behavior")
archimate_BusinessFunction = Class(name="archimate::BusinessFunction")
archimate_BusinessInteraction = Class(name="archimate::BusinessInteraction")
archimate_DataObject = Class(name="archimate::DataObject")
archimate_ApplicationFunction = Class(name="archimate::ApplicationFunction")
archimate_ApplicationInteraction = Class(name="archimate::ApplicationInteraction")
archimate_ApplicationService = Class(name="archimate::ApplicationService")
archimate_Node = Class(name="archimate::Node")
TechnologyConcept = Class(name="TechnologyConcept")
archimate_Device = Class(name="archimate::Device")
Node = Class(name="Node")
archimate_SystemSoftware = Class(name="archimate::SystemSoftware")
archimate_InfrastructureInterface = Class(name="archimate::InfrastructureInterface")
archimate_Network = Class(name="archimate::Network")
archimate_CommunicationPath = Class(name="archimate::CommunicationPath")
archimate_InfrastructureFunction = Class(name="archimate::InfrastructureFunction")
archimate_InfrastructureService = Class(name="archimate::InfrastructureService")
archimate_Artifact = Class(name="archimate::Artifact")
archimate_Stakeholder = Class(name="archimate::Stakeholder")
MotivationConcept = Class(name="MotivationConcept")
archimate_Driver = Class(name="archimate::Driver")
archimate_Assessment = Class(name="archimate::Assessment")
archimate_Goal = Class(name="archimate::Goal")
archimate_Requirement = Class(name="archimate::Requirement")
archimate_Constraint = Class(name="archimate::Constraint")
Requirement = Class(name="Requirement")
archimate_Principle = Class(name="archimate::Principle")
archimate_WorkPackage = Class(name="archimate::WorkPackage")
ImplementationAndMigrationConcept = Class(name="ImplementationAndMigrationConcept")
archimate_Deliverable = Class(name="archimate::Deliverable")
archimate_Plateau = Class(name="archimate::Plateau")
archimate_Gap = Class(name="archimate::Gap")

# archimate_Concept class attributes and methods
archimate_Concept_name: Property = Property(name="name", type=StringType)
archimate_Concept_description: Property = Property(name="description", type=StringType)
archimate_Concept.attributes={archimate_Concept_description, archimate_Concept_name}

# archimate_BusinessConcept class attributes and methods

# Concept class attributes and methods

# archimate_ApplicationConcept class attributes and methods

# archimate_TechnologyConcept class attributes and methods

# archimate_MotivationConcept class attributes and methods

# archimate_ImplementationAndMigrationConcept class attributes and methods

# archimate_Passive class attributes and methods

# archimate_Behavior class attributes and methods

# archimate_Active class attributes and methods

# archimate_BusinessEvent class attributes and methods

# archimate_BusinessService class attributes and methods

# archimate_Representation class attributes and methods

# archimate_Meaning class attributes and methods

# archimate_Value class attributes and methods

# archimate_Product class attributes and methods

# archimate_Contract class attributes and methods

# BusinessObject class attributes and methods

# archimate_ApplicationComponent class attributes and methods

# ApplicationConcept class attributes and methods

# archimate_ApplicationCollaboration class attributes and methods

# archimate_ApplicationInterface class attributes and methods

# archimate_BusinessActor class attributes and methods

# BusinessConcept class attributes and methods

# Active class attributes and methods

# archimate_BusinessRole class attributes and methods

# archimate_BusinessCollaboration class attributes and methods

# archimate_BusinessInterface class attributes and methods

# archimate_Location class attributes and methods

# archimate_BusinessObject class attributes and methods

# Passive class attributes and methods

# archimate_BusinessProcess class attributes and methods

# Behavior class attributes and methods

# archimate_BusinessFunction class attributes and methods

# archimate_BusinessInteraction class attributes and methods

# archimate_DataObject class attributes and methods

# archimate_ApplicationFunction class attributes and methods

# archimate_ApplicationInteraction class attributes and methods

# archimate_ApplicationService class attributes and methods

# archimate_Node class attributes and methods

# TechnologyConcept class attributes and methods

# archimate_Device class attributes and methods

# Node class attributes and methods

# archimate_SystemSoftware class attributes and methods

# archimate_InfrastructureInterface class attributes and methods

# archimate_Network class attributes and methods

# archimate_CommunicationPath class attributes and methods

# archimate_InfrastructureFunction class attributes and methods

# archimate_InfrastructureService class attributes and methods

# archimate_Artifact class attributes and methods

# archimate_Stakeholder class attributes and methods

# MotivationConcept class attributes and methods

# archimate_Driver class attributes and methods

# archimate_Assessment class attributes and methods

# archimate_Goal class attributes and methods

# archimate_Requirement class attributes and methods

# archimate_Constraint class attributes and methods

# Requirement class attributes and methods

# archimate_Principle class attributes and methods

# archimate_WorkPackage class attributes and methods

# ImplementationAndMigrationConcept class attributes and methods

# archimate_Deliverable class attributes and methods

# archimate_Plateau class attributes and methods

# archimate_Gap class attributes and methods

# Relationships
specializes1: BinaryAssociation = BinaryAssociation(
    name="specializes1",
    ends={
        Property(name="archimate_Concept", type=archimate_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Concept0", type=archimate_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
flowsTo_Behavior34: BinaryAssociation = BinaryAssociation(
    name="flowsTo_Behavior34",
    ends={
        Property(name="archimate_Behavior35", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior33", type=archimate_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
triggers_Behavior37: BinaryAssociation = BinaryAssociation(
    name="triggers_Behavior37",
    ends={
        Property(name="archimate_Behavior38", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior36", type=archimate_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
realizes_Behavior40: BinaryAssociation = BinaryAssociation(
    name="realizes_Behavior40",
    ends={
        Property(name="archimate_Behavior41", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior39", type=archimate_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
uses_Behavior43: BinaryAssociation = BinaryAssociation(
    name="uses_Behavior43",
    ends={
        Property(name="archimate_Behavior44", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior42", type=archimate_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
assignedTo_Active45: BinaryAssociation = BinaryAssociation(
    name="assignedTo_Active45",
    ends={
        Property(name="archimate_Active47", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior46", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
usesActive48: BinaryAssociation = BinaryAssociation(
    name="usesActive48",
    ends={
        Property(name="archimate_Active50", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior49", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
aggregates_Pasive51: BinaryAssociation = BinaryAssociation(
    name="aggregates_Pasive51",
    ends={
        Property(name="archimate_Passive53", type=archimate_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Behavior52", type=archimate_Passive, multiplicity=Multiplicity(0, 9999))
    }
)
composes_Active55: BinaryAssociation = BinaryAssociation(
    name="composes_Active55",
    ends={
        Property(name="archimate_Active56", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active54", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
realizes3: BinaryAssociation = BinaryAssociation(
    name="realizes3",
    ends={
        Property(name="archimate_MotivationConcept", type=archimate_MotivationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationConcept2", type=archimate_MotivationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWith5: BinaryAssociation = BinaryAssociation(
    name="associatedWith5",
    ends={
        Property(name="archimate_MotivationConcept6", type=archimate_MotivationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationConcept4", type=archimate_MotivationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
influences8: BinaryAssociation = BinaryAssociation(
    name="influences8",
    ends={
        Property(name="archimate_MotivationConcept9", type=archimate_MotivationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_MotivationConcept7", type=archimate_MotivationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
triggers11: BinaryAssociation = BinaryAssociation(
    name="triggers11",
    ends={
        Property(name="archimate_ImplementationAndMigrationConcept", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ImplementationAndMigrationConcept10", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWith13: BinaryAssociation = BinaryAssociation(
    name="associatedWith13",
    ends={
        Property(name="archimate_ImplementationAndMigrationConcept14", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ImplementationAndMigrationConcept12", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
realizes16: BinaryAssociation = BinaryAssociation(
    name="realizes16",
    ends={
        Property(name="archimate_ImplementationAndMigrationConcept17", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ImplementationAndMigrationConcept15", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
flowTo19: BinaryAssociation = BinaryAssociation(
    name="flowTo19",
    ends={
        Property(name="archimate_ImplementationAndMigrationConcept20", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_ImplementationAndMigrationConcept18", type=archimate_ImplementationAndMigrationConcept, multiplicity=Multiplicity(0, 9999))
    }
)
aggregates_Passive22: BinaryAssociation = BinaryAssociation(
    name="aggregates_Passive22",
    ends={
        Property(name="archimate_Passive", type=archimate_Passive, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Passive21", type=archimate_Passive, multiplicity=Multiplicity(0, 9999))
    }
)
realizes_Passive24: BinaryAssociation = BinaryAssociation(
    name="realizes_Passive24",
    ends={
        Property(name="archimate_Passive25", type=archimate_Passive, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Passive23", type=archimate_Passive, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWith_Passive27: BinaryAssociation = BinaryAssociation(
    name="associatedWith_Passive27",
    ends={
        Property(name="archimate_Passive28", type=archimate_Passive, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Passive26", type=archimate_Passive, multiplicity=Multiplicity(0, 9999))
    }
)
accesses_Behavior29: BinaryAssociation = BinaryAssociation(
    name="accesses_Behavior29",
    ends={
        Property(name="archimate_Behavior", type=archimate_Passive, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Passive30", type=archimate_Behavior, multiplicity=Multiplicity(0, 9999))
    }
)
assignedTo_Active31: BinaryAssociation = BinaryAssociation(
    name="assignedTo_Active31",
    ends={
        Property(name="archimate_Active", type=archimate_Passive, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Passive32", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
uses_Active58: BinaryAssociation = BinaryAssociation(
    name="uses_Active58",
    ends={
        Property(name="archimate_Active59", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active57", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
aggregates_Active61: BinaryAssociation = BinaryAssociation(
    name="aggregates_Active61",
    ends={
        Property(name="archimate_Active62", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active60", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
associatedWith_Active64: BinaryAssociation = BinaryAssociation(
    name="associatedWith_Active64",
    ends={
        Property(name="archimate_Active65", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active63", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
realizes_Active67: BinaryAssociation = BinaryAssociation(
    name="realizes_Active67",
    ends={
        Property(name="archimate_Active68", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active66", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
assignedTo_Active70: BinaryAssociation = BinaryAssociation(
    name="assignedTo_Active70",
    ends={
        Property(name="archimate_Active71", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active69", type=archimate_Active, multiplicity=Multiplicity(0, 9999))
    }
)
realizes_Passive72: BinaryAssociation = BinaryAssociation(
    name="realizes_Passive72",
    ends={
        Property(name="archimate_Passive74", type=archimate_Active, multiplicity=Multiplicity(1, 1)),
        Property(name="archimate_Active73", type=archimate_Passive, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_archimate_BusinessConcept_Concept = Generalization(general=Concept, specific=archimate_BusinessConcept)
gen_archimate_ApplicationConcept_Concept = Generalization(general=Concept, specific=archimate_ApplicationConcept)
gen_archimate_TechnologyConcept_Concept = Generalization(general=Concept, specific=archimate_TechnologyConcept)
gen_archimate_MotivationConcept_Concept = Generalization(general=Concept, specific=archimate_MotivationConcept)
gen_archimate_ImplementationAndMigrationConcept_Concept = Generalization(general=Concept, specific=archimate_ImplementationAndMigrationConcept)
gen_archimate_BusinessInteraction_Behavior = Generalization(general=Behavior, specific=archimate_BusinessInteraction)
gen_archimate_BusinessEvent_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessEvent)
gen_archimate_BusinessEvent_Behavior = Generalization(general=Behavior, specific=archimate_BusinessEvent)
gen_archimate_BusinessService_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessService)
gen_archimate_BusinessService_Behavior = Generalization(general=Behavior, specific=archimate_BusinessService)
gen_archimate_Representation_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_Representation)
gen_archimate_Representation_Passive = Generalization(general=Passive, specific=archimate_Representation)
gen_archimate_Meaning_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_Meaning)
gen_archimate_Meaning_Passive = Generalization(general=Passive, specific=archimate_Meaning)
gen_archimate_Value_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_Value)
gen_archimate_Value_Passive = Generalization(general=Passive, specific=archimate_Value)
gen_archimate_Product_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_Product)
gen_archimate_Product_Passive = Generalization(general=Passive, specific=archimate_Product)
gen_archimate_Contract_BusinessObject = Generalization(general=BusinessObject, specific=archimate_Contract)
gen_archimate_ApplicationComponent_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationComponent)
gen_archimate_ApplicationComponent_Active = Generalization(general=Active, specific=archimate_ApplicationComponent)
gen_archimate_ApplicationCollaboration_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationCollaboration)
gen_archimate_ApplicationInterface_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationInterface)
gen_archimate_ApplicationInterface_Active = Generalization(general=Active, specific=archimate_ApplicationInterface)
gen_archimate_BusinessActor_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessActor)
gen_archimate_BusinessActor_Active = Generalization(general=Active, specific=archimate_BusinessActor)
gen_archimate_BusinessRole_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessRole)
gen_archimate_BusinessRole_Active = Generalization(general=Active, specific=archimate_BusinessRole)
gen_archimate_BusinessCollaboration_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessCollaboration)
gen_archimate_BusinessInterface_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessInterface)
gen_archimate_BusinessInterface_Active = Generalization(general=Active, specific=archimate_BusinessInterface)
gen_archimate_Location_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_Location)
gen_archimate_Location_Active = Generalization(general=Active, specific=archimate_Location)
gen_archimate_BusinessObject_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessObject)
gen_archimate_BusinessObject_Passive = Generalization(general=Passive, specific=archimate_BusinessObject)
gen_archimate_BusinessProcess_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessProcess)
gen_archimate_BusinessProcess_Behavior = Generalization(general=Behavior, specific=archimate_BusinessProcess)
gen_archimate_BusinessFunction_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessFunction)
gen_archimate_BusinessFunction_Behavior = Generalization(general=Behavior, specific=archimate_BusinessFunction)
gen_archimate_BusinessInteraction_BusinessConcept = Generalization(general=BusinessConcept, specific=archimate_BusinessInteraction)
gen_archimate_DataObject_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_DataObject)
gen_archimate_DataObject_Passive = Generalization(general=Passive, specific=archimate_DataObject)
gen_archimate_ApplicationFunction_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationFunction)
gen_archimate_ApplicationFunction_Behavior = Generalization(general=Behavior, specific=archimate_ApplicationFunction)
gen_archimate_ApplicationInteraction_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationInteraction)
gen_archimate_ApplicationInteraction_Behavior = Generalization(general=Behavior, specific=archimate_ApplicationInteraction)
gen_archimate_ApplicationService_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_ApplicationService)
gen_archimate_ApplicationService_Behavior = Generalization(general=Behavior, specific=archimate_ApplicationService)
gen_archimate_Node_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_Node)
gen_archimate_Node_Active = Generalization(general=Active, specific=archimate_Node)
gen_archimate_Device_Node = Generalization(general=Node, specific=archimate_Device)
gen_archimate_SystemSoftware_Node = Generalization(general=Node, specific=archimate_SystemSoftware)
gen_archimate_InfrastructureInterface_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_InfrastructureInterface)
gen_archimate_InfrastructureInterface_Active = Generalization(general=Active, specific=archimate_InfrastructureInterface)
gen_archimate_Network_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_Network)
gen_archimate_Network_Active = Generalization(general=Active, specific=archimate_Network)
gen_archimate_CommunicationPath_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_CommunicationPath)
gen_archimate_CommunicationPath_Active = Generalization(general=Active, specific=archimate_CommunicationPath)
gen_archimate_InfrastructureFunction_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_InfrastructureFunction)
gen_archimate_InfrastructureFunction_Behavior = Generalization(general=Behavior, specific=archimate_InfrastructureFunction)
gen_archimate_InfrastructureService_TechnologyConcept = Generalization(general=TechnologyConcept, specific=archimate_InfrastructureService)
gen_archimate_InfrastructureService_Behavior = Generalization(general=Behavior, specific=archimate_InfrastructureService)
gen_archimate_Artifact_ApplicationConcept = Generalization(general=ApplicationConcept, specific=archimate_Artifact)
gen_archimate_Artifact_Passive = Generalization(general=Passive, specific=archimate_Artifact)
gen_archimate_Stakeholder_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Stakeholder)
gen_archimate_Driver_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Driver)
gen_archimate_Assessment_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Assessment)
gen_archimate_Goal_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Goal)
gen_archimate_Requirement_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Requirement)
gen_archimate_Constraint_Requirement = Generalization(general=Requirement, specific=archimate_Constraint)
gen_archimate_Principle_MotivationConcept = Generalization(general=MotivationConcept, specific=archimate_Principle)
gen_archimate_WorkPackage_ImplementationAndMigrationConcept = Generalization(general=ImplementationAndMigrationConcept, specific=archimate_WorkPackage)
gen_archimate_Deliverable_ImplementationAndMigrationConcept = Generalization(general=ImplementationAndMigrationConcept, specific=archimate_Deliverable)
gen_archimate_Plateau_ImplementationAndMigrationConcept = Generalization(general=ImplementationAndMigrationConcept, specific=archimate_Plateau)
gen_archimate_Gap_ImplementationAndMigrationConcept = Generalization(general=ImplementationAndMigrationConcept, specific=archimate_Gap)

# Domain Model
domain_model = DomainModel(
    name="archimate",
    types={archimate_Concept, archimate_BusinessConcept, Concept, archimate_ApplicationConcept, archimate_TechnologyConcept, archimate_MotivationConcept, archimate_ImplementationAndMigrationConcept, archimate_Passive, archimate_Behavior, archimate_Active, archimate_BusinessEvent, archimate_BusinessService, archimate_Representation, archimate_Meaning, archimate_Value, archimate_Product, archimate_Contract, BusinessObject, archimate_ApplicationComponent, ApplicationConcept, archimate_ApplicationCollaboration, archimate_ApplicationInterface, archimate_BusinessActor, BusinessConcept, Active, archimate_BusinessRole, archimate_BusinessCollaboration, archimate_BusinessInterface, archimate_Location, archimate_BusinessObject, Passive, archimate_BusinessProcess, Behavior, archimate_BusinessFunction, archimate_BusinessInteraction, archimate_DataObject, archimate_ApplicationFunction, archimate_ApplicationInteraction, archimate_ApplicationService, archimate_Node, TechnologyConcept, archimate_Device, Node, archimate_SystemSoftware, archimate_InfrastructureInterface, archimate_Network, archimate_CommunicationPath, archimate_InfrastructureFunction, archimate_InfrastructureService, archimate_Artifact, archimate_Stakeholder, MotivationConcept, archimate_Driver, archimate_Assessment, archimate_Goal, archimate_Requirement, archimate_Constraint, Requirement, archimate_Principle, archimate_WorkPackage, ImplementationAndMigrationConcept, archimate_Deliverable, archimate_Plateau, archimate_Gap},
    associations={specializes1, flowsTo_Behavior34, triggers_Behavior37, realizes_Behavior40, uses_Behavior43, assignedTo_Active45, usesActive48, aggregates_Pasive51, composes_Active55, realizes3, associatedWith5, influences8, triggers11, associatedWith13, realizes16, flowTo19, aggregates_Passive22, realizes_Passive24, associatedWith_Passive27, accesses_Behavior29, assignedTo_Active31, uses_Active58, aggregates_Active61, associatedWith_Active64, realizes_Active67, assignedTo_Active70, realizes_Passive72},
    generalizations={gen_archimate_BusinessConcept_Concept, gen_archimate_ApplicationConcept_Concept, gen_archimate_TechnologyConcept_Concept, gen_archimate_MotivationConcept_Concept, gen_archimate_ImplementationAndMigrationConcept_Concept, gen_archimate_BusinessInteraction_Behavior, gen_archimate_BusinessEvent_BusinessConcept, gen_archimate_BusinessEvent_Behavior, gen_archimate_BusinessService_BusinessConcept, gen_archimate_BusinessService_Behavior, gen_archimate_Representation_BusinessConcept, gen_archimate_Representation_Passive, gen_archimate_Meaning_BusinessConcept, gen_archimate_Meaning_Passive, gen_archimate_Value_BusinessConcept, gen_archimate_Value_Passive, gen_archimate_Product_BusinessConcept, gen_archimate_Product_Passive, gen_archimate_Contract_BusinessObject, gen_archimate_ApplicationComponent_ApplicationConcept, gen_archimate_ApplicationComponent_Active, gen_archimate_ApplicationCollaboration_ApplicationConcept, gen_archimate_ApplicationInterface_ApplicationConcept, gen_archimate_ApplicationInterface_Active, gen_archimate_BusinessActor_BusinessConcept, gen_archimate_BusinessActor_Active, gen_archimate_BusinessRole_BusinessConcept, gen_archimate_BusinessRole_Active, gen_archimate_BusinessCollaboration_BusinessConcept, gen_archimate_BusinessInterface_BusinessConcept, gen_archimate_BusinessInterface_Active, gen_archimate_Location_BusinessConcept, gen_archimate_Location_Active, gen_archimate_BusinessObject_BusinessConcept, gen_archimate_BusinessObject_Passive, gen_archimate_BusinessProcess_BusinessConcept, gen_archimate_BusinessProcess_Behavior, gen_archimate_BusinessFunction_BusinessConcept, gen_archimate_BusinessFunction_Behavior, gen_archimate_BusinessInteraction_BusinessConcept, gen_archimate_DataObject_ApplicationConcept, gen_archimate_DataObject_Passive, gen_archimate_ApplicationFunction_ApplicationConcept, gen_archimate_ApplicationFunction_Behavior, gen_archimate_ApplicationInteraction_ApplicationConcept, gen_archimate_ApplicationInteraction_Behavior, gen_archimate_ApplicationService_ApplicationConcept, gen_archimate_ApplicationService_Behavior, gen_archimate_Node_TechnologyConcept, gen_archimate_Node_Active, gen_archimate_Device_Node, gen_archimate_SystemSoftware_Node, gen_archimate_InfrastructureInterface_TechnologyConcept, gen_archimate_InfrastructureInterface_Active, gen_archimate_Network_TechnologyConcept, gen_archimate_Network_Active, gen_archimate_CommunicationPath_TechnologyConcept, gen_archimate_CommunicationPath_Active, gen_archimate_InfrastructureFunction_TechnologyConcept, gen_archimate_InfrastructureFunction_Behavior, gen_archimate_InfrastructureService_TechnologyConcept, gen_archimate_InfrastructureService_Behavior, gen_archimate_Artifact_ApplicationConcept, gen_archimate_Artifact_Passive, gen_archimate_Stakeholder_MotivationConcept, gen_archimate_Driver_MotivationConcept, gen_archimate_Assessment_MotivationConcept, gen_archimate_Goal_MotivationConcept, gen_archimate_Requirement_MotivationConcept, gen_archimate_Constraint_Requirement, gen_archimate_Principle_MotivationConcept, gen_archimate_WorkPackage_ImplementationAndMigrationConcept, gen_archimate_Deliverable_ImplementationAndMigrationConcept, gen_archimate_Plateau_ImplementationAndMigrationConcept, gen_archimate_Gap_ImplementationAndMigrationConcept},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)