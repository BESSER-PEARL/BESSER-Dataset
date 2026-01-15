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

# Enumerations
RequirementNature: Enumeration = Enumeration(
    name="RequirementNature",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Functional"),
			EnumerationLiteral(name="Non_functional"),
			EnumerationLiteral(name="Constraint"),
			EnumerationLiteral(name="Verification_and_Validation")
    }
)

RequirementOrigin: Enumeration = Enumeration(
    name="RequirementOrigin",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Stackeholder_requirement"),
			EnumerationLiteral(name="System_requirement"),
			EnumerationLiteral(name="Expectation")
    }
)

RoleType: Enumeration = Enumeration(
    name="RoleType",
    literals={
            EnumerationLiteral(name="Composite"),
			EnumerationLiteral(name="Decision"),
			EnumerationLiteral(name="Transformation"),
			EnumerationLiteral(name="Controle")
    }
)

ProductState: Enumeration = Enumeration(
    name="ProductState",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Ready_for_customer"),
			EnumerationLiteral(name="Intermediary")
    }
)

ServiceState: Enumeration = Enumeration(
    name="ServiceState",
    literals={
            EnumerationLiteral(name="For_external_customer"),
			EnumerationLiteral(name="For_internal_usage")
    }
)

ProductNature: Enumeration = Enumeration(
    name="ProductNature",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Physical"),
			EnumerationLiteral(name="Information")
    }
)

CapabilityType: Enumeration = Enumeration(
    name="CapabilityType",
    literals={
            EnumerationLiteral(name="Functional"),
			EnumerationLiteral(name="ObjectRelated"),
			EnumerationLiteral(name="Performance"),
			EnumerationLiteral(name="Operational")
    }
)

StakeholderType: Enumeration = Enumeration(
    name="StakeholderType",
    literals={
            EnumerationLiteral(name="EEnumLiteral0")
    }
)

EnterpriseObjectiveType: Enumeration = Enumeration(
    name="EnterpriseObjectiveType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Strategic"),
			EnumerationLiteral(name="Tactic"),
			EnumerationLiteral(name="Operational")
    }
)

ObjectiveNature: Enumeration = Enumeration(
    name="ObjectiveNature",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Performance"),
			EnumerationLiteral(name="Quality"),
			EnumerationLiteral(name="Delay"),
			EnumerationLiteral(name="Cost"),
			EnumerationLiteral(name="Environmental"),
			EnumerationLiteral(name="Legacy"),
			EnumerationLiteral(name="Human"),
			EnumerationLiteral(name="Economical"),
			EnumerationLiteral(name="Other")
    }
)

Origin: Enumeration = Enumeration(
    name="Origin",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Internal_provider"),
			EnumerationLiteral(name="External_provider")
    }
)

# Classes
sipme_Activity = Class(name="sipme::Activity")
EnterpriseProcessor = Class(name="EnterpriseProcessor")
sipme_Task = Class(name="sipme::Task")
sipme_BusinessProcess = Class(name="sipme::BusinessProcess")
sipme_Application = Class(name="sipme::Application")
EnterpriseResource = Class(name="EnterpriseResource")
sipme_Domain = Class(name="sipme::Domain")
sipme_OrganisationCell = Class(name="sipme::OrganisationCell")
sipme_ObjectsFileView = Class(name="sipme::ObjectsFileView")
sipme_Device_Machine = Class(name="sipme::Device::Machine")
SIPME_object = Class(name="SIPME::object")
OrganisationCell = Class(name="OrganisationCell")
sipme_BusinessRules = Class(name="sipme::BusinessRules")
EnterpriseObject = Class(name="EnterpriseObject")
sipme_EnterpriseObject = Class(name="sipme::EnterpriseObject", is_abstract=True)
sipme_Capability = Class(name="sipme::Capability")
sipme_Capacity = Class(name="sipme::Capacity")
sipme_CompanyMember = Class(name="sipme::CompanyMember")
Stakeholder = Class(name="Stakeholder")
sipme_Workstation = Class(name="sipme::Workstation")
sipme_ObjectView = Class(name="sipme::ObjectView")
sipme_EnterpriseProcessor = Class(name="sipme::EnterpriseProcessor", is_abstract=True)
sipme_Event = Class(name="sipme::Event")
sipme_Enterprise = Class(name="sipme::Enterprise")
sipme_Objective = Class(name="sipme::Objective")
sipme_EnterpriseService = Class(name="sipme::EnterpriseService")
sipme_EnterpriseProduct = Class(name="sipme::EnterpriseProduct")
sipme_Role_Function = Class(name="sipme::Role::Function")
sipme_EnterpriseResource = Class(name="sipme::EnterpriseResource", is_abstract=True)
ObjectView = Class(name="ObjectView")
sipme_Stakeholder = Class(name="sipme::Stakeholder", is_abstract=True)
sipme_Requirement = Class(name="sipme::Requirement")
sipme_SIPME_object = Class(name="sipme::SIPME::object", is_abstract=True)

# sipme_Activity class attributes and methods
sipme_Activity_ActivityDuration: Property = Property(name="ActivityDuration", type=IntegerType)
sipme_Activity_endingStatus: Property = Property(name="endingStatus", type=StringType)
sipme_Activity.attributes={sipme_Activity_ActivityDuration, sipme_Activity_endingStatus}

# EnterpriseProcessor class attributes and methods

# sipme_Task class attributes and methods
sipme_Task_taskDuration: Property = Property(name="taskDuration", type=IntegerType)
sipme_Task.attributes={sipme_Task_taskDuration}

# sipme_BusinessProcess class attributes and methods
sipme_BusinessProcess_ProcessPriority: Property = Property(name="ProcessPriority", type=IntegerType)
sipme_BusinessProcess.attributes={sipme_BusinessProcess_ProcessPriority}

# sipme_Application class attributes and methods
sipme_Application_applicationEditor: Property = Property(name="applicationEditor", type=StringType)
sipme_Application_applicationMaintainer: Property = Property(name="applicationMaintainer", type=StringType)
sipme_Application.attributes={sipme_Application_applicationEditor, sipme_Application_applicationMaintainer}

# EnterpriseResource class attributes and methods

# sipme_Domain class attributes and methods
sipme_Domain_domainCharacterization: Property = Property(name="domainCharacterization", type=StringType)
sipme_Domain_performanceIndicators: Property = Property(name="performanceIndicators", type=FloatType)
sipme_Domain.attributes={sipme_Domain_domainCharacterization, sipme_Domain_performanceIndicators}

# sipme_OrganisationCell class attributes and methods
sipme_OrganisationCell_organisationLevel: Property = Property(name="organisationLevel", type=IntegerType)
sipme_OrganisationCell.attributes={sipme_OrganisationCell_organisationLevel}

# sipme_ObjectsFileView class attributes and methods
sipme_ObjectsFileView_filePriority: Property = Property(name="filePriority", type=IntegerType)
sipme_ObjectsFileView_fileState: Property = Property(name="fileState", type=StringType)
sipme_ObjectsFileView.attributes={sipme_ObjectsFileView_filePriority, sipme_ObjectsFileView_fileState}

# sipme_Device_Machine class attributes and methods
sipme_Device_Machine_manufacturer: Property = Property(name="manufacturer", type=StringType)
sipme_Device_Machine_machineMaintainer: Property = Property(name="machineMaintainer", type=StringType)
sipme_Device_Machine.attributes={sipme_Device_Machine_machineMaintainer, sipme_Device_Machine_manufacturer}

# SIPME_object class attributes and methods

# OrganisationCell class attributes and methods

# sipme_BusinessRules class attributes and methods

# EnterpriseObject class attributes and methods

# sipme_EnterpriseObject class attributes and methods
sipme_EnterpriseObject_reference: Property = Property(name="reference", type=StringType)
sipme_EnterpriseObject_properties: Property = Property(name="properties", type=StringType)
sipme_EnterpriseObject.attributes={sipme_EnterpriseObject_reference, sipme_EnterpriseObject_properties}

# sipme_Capability class attributes and methods
sipme_Capability_capabilityType: Property = Property(name="capabilityType", type=StringType)
sipme_Capability.attributes={sipme_Capability_capabilityType}

# sipme_Capacity class attributes and methods
sipme_Capacity_value: Property = Property(name="value", type=FloatType)
sipme_Capacity_unit: Property = Property(name="unit", type=StringType)
sipme_Capacity.attributes={sipme_Capacity_value, sipme_Capacity_unit}

# sipme_CompanyMember class attributes and methods
sipme_CompanyMember_fullName: Property = Property(name="fullName", type=StringType)
sipme_CompanyMember_socialSecurityNumber: Property = Property(name="socialSecurityNumber", type=IntegerType)
sipme_CompanyMember_address: Property = Property(name="address", type=StringType)
sipme_CompanyMember.attributes={sipme_CompanyMember_socialSecurityNumber, sipme_CompanyMember_fullName, sipme_CompanyMember_address}

# Stakeholder class attributes and methods

# sipme_Workstation class attributes and methods
sipme_Workstation_ProfileDeescription: Property = Property(name="ProfileDeescription", type=StringType)
sipme_Workstation.attributes={sipme_Workstation_ProfileDeescription}

# sipme_ObjectView class attributes and methods
sipme_ObjectView_viewPoint: Property = Property(name="viewPoint", type=StringType)
sipme_ObjectView.attributes={sipme_ObjectView_viewPoint}

# sipme_EnterpriseProcessor class attributes and methods
sipme_EnterpriseProcessor_processorOrigin: Property = Property(name="processorOrigin", type=StringType)
sipme_EnterpriseProcessor.attributes={sipme_EnterpriseProcessor_processorOrigin}

# sipme_Event class attributes and methods
sipme_Event_occurenceProbability: Property = Property(name="occurenceProbability", type=StringType)
sipme_Event_frequency: Property = Property(name="frequency", type=StringType)
sipme_Event_timeStamp: Property = Property(name="timeStamp", type=DateType)
sipme_Event_source: Property = Property(name="source", type=StringType)
sipme_Event.attributes={sipme_Event_source, sipme_Event_frequency, sipme_Event_occurenceProbability, sipme_Event_timeStamp}

# sipme_Enterprise class attributes and methods
sipme_Enterprise_acronym: Property = Property(name="acronym", type=StringType)
sipme_Enterprise_status: Property = Property(name="status", type=StringType)
sipme_Enterprise.attributes={sipme_Enterprise_status, sipme_Enterprise_acronym}

# sipme_Objective class attributes and methods
sipme_Objective_objectiveType: Property = Property(name="objectiveType", type=StringType)
sipme_Objective_objectiveNature: Property = Property(name="objectiveNature", type=StringType)
sipme_Objective.attributes={sipme_Objective_objectiveType, sipme_Objective_objectiveNature}

# sipme_EnterpriseService class attributes and methods
sipme_EnterpriseService_serviceState: Property = Property(name="serviceState", type=StringType)
sipme_EnterpriseService.attributes={sipme_EnterpriseService_serviceState}

# sipme_EnterpriseProduct class attributes and methods
sipme_EnterpriseProduct_productState: Property = Property(name="productState", type=StringType)
sipme_EnterpriseProduct_productNarure: Property = Property(name="productNarure", type=StringType)
sipme_EnterpriseProduct.attributes={sipme_EnterpriseProduct_productNarure, sipme_EnterpriseProduct_productState}

# sipme_Role_Function class attributes and methods
sipme_Role_Function_roleType: Property = Property(name="roleType", type=StringType)
sipme_Role_Function.attributes={sipme_Role_Function_roleType}

# sipme_EnterpriseResource class attributes and methods
sipme_EnterpriseResource_resourceOrigin: Property = Property(name="resourceOrigin", type=StringType)
sipme_EnterpriseResource.attributes={sipme_EnterpriseResource_resourceOrigin}

# ObjectView class attributes and methods

# sipme_Stakeholder class attributes and methods
sipme_Stakeholder_stakeholderType: Property = Property(name="stakeholderType", type=StringType)
sipme_Stakeholder_stakeholderOrganism: Property = Property(name="stakeholderOrganism", type=StringType)
sipme_Stakeholder.attributes={sipme_Stakeholder_stakeholderType, sipme_Stakeholder_stakeholderOrganism}

# sipme_Requirement class attributes and methods
sipme_Requirement_requirementOrigin: Property = Property(name="requirementOrigin", type=StringType)
sipme_Requirement_requirementNature: Property = Property(name="requirementNature", type=StringType)
sipme_Requirement_requirementVersion: Property = Property(name="requirementVersion", type=StringType)
sipme_Requirement_requirementDate: Property = Property(name="requirementDate", type=DateType)
sipme_Requirement_requirementStatement: Property = Property(name="requirementStatement", type=StringType)
sipme_Requirement_requirementPriority: Property = Property(name="requirementPriority", type=IntegerType)
sipme_Requirement_requirementMaturity: Property = Property(name="requirementMaturity", type=IntegerType)
sipme_Requirement_requirementStatus: Property = Property(name="requirementStatus", type=StringType)
sipme_Requirement.attributes={sipme_Requirement_requirementVersion, sipme_Requirement_requirementOrigin, sipme_Requirement_requirementMaturity, sipme_Requirement_requirementStatus, sipme_Requirement_requirementStatement, sipme_Requirement_requirementPriority, sipme_Requirement_requirementDate, sipme_Requirement_requirementNature}

# sipme_SIPME_object class attributes and methods
sipme_SIPME_object_name: Property = Property(name="name", type=StringType)
sipme_SIPME_object_description: Property = Property(name="description", type=StringType)
sipme_SIPME_object_UUID: Property = Property(name="UUID", type=StringType)
sipme_SIPME_object.attributes={sipme_SIPME_object_description, sipme_SIPME_object_name, sipme_SIPME_object_UUID}

# Relationships
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="Task", type=sipme_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="taskOf", type=sipme_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activityOf1: BinaryAssociation = BinaryAssociation(
    name="activityOf1",
    ends={
        Property(name="BusinessProcess", type=sipme_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activities", type=sipme_BusinessProcess, multiplicity=Multiplicity(1, 1))
    }
)
activities2: BinaryAssociation = BinaryAssociation(
    name="activities2",
    ends={
        Property(name="Activity", type=sipme_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="activityOf", type=sipme_Activity, multiplicity=Multiplicity(2, 6), is_composite=True)
    }
)
businessProcessOf3: BinaryAssociation = BinaryAssociation(
    name="businessProcessOf3",
    ends={
        Property(name="sipme_Domain", type=sipme_BusinessProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_BusinessProcess", type=sipme_Domain, multiplicity=Multiplicity(0, 1))
    }
)
responsibleOfCell12: BinaryAssociation = BinaryAssociation(
    name="responsibleOfCell12",
    ends={
        Property(name="OrganisationCell", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="cellResponsible", type=sipme_OrganisationCell, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleOfFile13: BinaryAssociation = BinaryAssociation(
    name="responsibleOfFile13",
    ends={
        Property(name="ObjectsFileView", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="fileResponsible", type=sipme_ObjectsFileView, multiplicity=Multiplicity(0, 9999))
    }
)
businessProcesses14: BinaryAssociation = BinaryAssociation(
    name="businessProcesses14",
    ends={
        Property(name="sipme_BusinessProcess16", type=sipme_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Domain15", type=sipme_BusinessProcess, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
coveredBy17: BinaryAssociation = BinaryAssociation(
    name="coveredBy17",
    ends={
        Property(name="OrganisationCell18", type=sipme_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="covers", type=sipme_OrganisationCell, multiplicity=Multiplicity(1, 9999))
    }
)
induces19: BinaryAssociation = BinaryAssociation(
    name="induces19",
    ends={
        Property(name="sipme_BusinessRules21", type=sipme_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Domain20", type=sipme_BusinessRules, multiplicity=Multiplicity(0, 9999))
    }
)
considers4: BinaryAssociation = BinaryAssociation(
    name="considers4",
    ends={
        Property(name="sipme_EnterpriseObject", type=sipme_BusinessRules, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_BusinessRules", type=sipme_EnterpriseObject, multiplicity=Multiplicity(0, 9999))
    }
)
impacts5: BinaryAssociation = BinaryAssociation(
    name="impacts5",
    ends={
        Property(name="sipme_EnterpriseObject7", type=sipme_BusinessRules, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_BusinessRules6", type=sipme_EnterpriseObject, multiplicity=Multiplicity(0, 9999))
    }
)
defines8: BinaryAssociation = BinaryAssociation(
    name="defines8",
    ends={
        Property(name="sipme_Capacity", type=sipme_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Capability", type=sipme_Capacity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inChargeOf9: BinaryAssociation = BinaryAssociation(
    name="inChargeOf9",
    ends={
        Property(name="Workstation", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="owners", type=sipme_Workstation, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleOf10: BinaryAssociation = BinaryAssociation(
    name="responsibleOf10",
    ends={
        Property(name="Workstation11", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="responsible", type=sipme_Workstation, multiplicity=Multiplicity(0, 9999))
    }
)
partOf38: BinaryAssociation = BinaryAssociation(
    name="partOf38",
    ends={
        Property(name="EnterpriseObject", type=sipme_EnterpriseObject, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposedIn", type=sipme_EnterpriseObject, multiplicity=Multiplicity(0, 1))
    }
)
representedBy39: BinaryAssociation = BinaryAssociation(
    name="representedBy39",
    ends={
        Property(name="ObjectView", type=sipme_EnterpriseObject, multiplicity=Multiplicity(1, 1)),
        Property(name="represents", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999))
    }
)
decomposedIn41: BinaryAssociation = BinaryAssociation(
    name="decomposedIn41",
    ends={
        Property(name="EnterpriseObject42", type=sipme_EnterpriseObject, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf", type=sipme_EnterpriseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generates43: BinaryAssociation = BinaryAssociation(
    name="generates43",
    ends={
        Property(name="Event", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedBy", type=sipme_Event, multiplicity=Multiplicity(0, 9999))
    }
)
providesOutputs44: BinaryAssociation = BinaryAssociation(
    name="providesOutputs44",
    ends={
        Property(name="sipme_ObjectView", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseProcessor", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999))
    }
)
hasInputs45: BinaryAssociation = BinaryAssociation(
    name="hasInputs45",
    ends={
        Property(name="sipme_ObjectView47", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseProcessor46", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999))
    }
)
initiatedBy48: BinaryAssociation = BinaryAssociation(
    name="initiatedBy48",
    ends={
        Property(name="Event49", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="initiates", type=sipme_Event, multiplicity=Multiplicity(0, 9999))
    }
)
strategicObjectives22: BinaryAssociation = BinaryAssociation(
    name="strategicObjectives22",
    ends={
        Property(name="sipme_Objective", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise", type=sipme_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
concerns23: BinaryAssociation = BinaryAssociation(
    name="concerns23",
    ends={
        Property(name="sipme_Domain25", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise24", type=sipme_Domain, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refers26: BinaryAssociation = BinaryAssociation(
    name="refers26",
    ends={
        Property(name="sipme_EnterpriseObject28", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise27", type=sipme_EnterpriseObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
proposesServices29: BinaryAssociation = BinaryAssociation(
    name="proposesServices29",
    ends={
        Property(name="sipme_EnterpriseService", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise30", type=sipme_EnterpriseService, multiplicity=Multiplicity(0, 9999))
    }
)
proposesProducts31: BinaryAssociation = BinaryAssociation(
    name="proposesProducts31",
    ends={
        Property(name="sipme_EnterpriseProduct", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise32", type=sipme_EnterpriseProduct, multiplicity=Multiplicity(0, 9999))
    }
)
companyMembers33: BinaryAssociation = BinaryAssociation(
    name="companyMembers33",
    ends={
        Property(name="sipme_CompanyMember", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise34", type=sipme_CompanyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
organizationCells35: BinaryAssociation = BinaryAssociation(
    name="organizationCells35",
    ends={
        Property(name="sipme_OrganisationCell", type=sipme_Enterprise, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Enterprise36", type=sipme_OrganisationCell, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatedBy68: BinaryAssociation = BinaryAssociation(
    name="generatedBy68",
    ends={
        Property(name="EnterpriseProcessor", type=sipme_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generates", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
initiates69: BinaryAssociation = BinaryAssociation(
    name="initiates69",
    ends={
        Property(name="EnterpriseProcessor70", type=sipme_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="initiatedBy", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
priorTo72: BinaryAssociation = BinaryAssociation(
    name="priorTo72",
    ends={
        Property(name="sipme_Event", type=sipme_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Event71", type=sipme_Event, multiplicity=Multiplicity(0, 9999))
    }
)
hasAssociatedEvents73: BinaryAssociation = BinaryAssociation(
    name="hasAssociatedEvents73",
    ends={
        Property(name="ObjectView74", type=sipme_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999))
    }
)
subObjectives76: BinaryAssociation = BinaryAssociation(
    name="subObjectives76",
    ends={
        Property(name="Objective", type=sipme_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="refines", type=sipme_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasControlInputs50: BinaryAssociation = BinaryAssociation(
    name="hasControlInputs50",
    ends={
        Property(name="sipme_ObjectView52", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseProcessor51", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999))
    }
)
implements53: BinaryAssociation = BinaryAssociation(
    name="implements53",
    ends={
        Property(name="Role_Function", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="implementedBy", type=sipme_Role_Function, multiplicity=Multiplicity(1, 9999))
    }
)
hasCapacity54: BinaryAssociation = BinaryAssociation(
    name="hasCapacity54",
    ends={
        Property(name="sipme_Capacity56", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseProcessor55", type=sipme_Capacity, multiplicity=Multiplicity(0, 9999))
    }
)
requiresCapabilities57: BinaryAssociation = BinaryAssociation(
    name="requiresCapabilities57",
    ends={
        Property(name="sipme_Capability59", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseProcessor58", type=sipme_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
executes60: BinaryAssociation = BinaryAssociation(
    name="executes60",
    ends={
        Property(name="sipme_Task", type=sipme_EnterpriseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseResource", type=sipme_Task, multiplicity=Multiplicity(0, 1))
    }
)
plays61: BinaryAssociation = BinaryAssociation(
    name="plays61",
    ends={
        Property(name="Role_Function62", type=sipme_EnterpriseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="playedBy", type=sipme_Role_Function, multiplicity=Multiplicity(0, 9999))
    }
)
isAbleToPlay63: BinaryAssociation = BinaryAssociation(
    name="isAbleToPlay63",
    ends={
        Property(name="Role_Function64", type=sipme_EnterpriseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="canBePlayedBy", type=sipme_Role_Function, multiplicity=Multiplicity(0, 9999))
    }
)
providesCapability65: BinaryAssociation = BinaryAssociation(
    name="providesCapability65",
    ends={
        Property(name="sipme_Capability67", type=sipme_EnterpriseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_EnterpriseResource66", type=sipme_Capability, multiplicity=Multiplicity(1, 9999))
    }
)
objectViews92: BinaryAssociation = BinaryAssociation(
    name="objectViews92",
    ends={
        Property(name="sipme_ObjectView93", type=sipme_ObjectsFileView, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_ObjectsFileView", type=sipme_ObjectView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFiles95: BinaryAssociation = BinaryAssociation(
    name="subFiles95",
    ends={
        Property(name="sipme_ObjectsFileView96", type=sipme_ObjectsFileView, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_ObjectsFileView94", type=sipme_ObjectsFileView, multiplicity=Multiplicity(0, 9999))
    }
)
fileResponsible97: BinaryAssociation = BinaryAssociation(
    name="fileResponsible97",
    ends={
        Property(name="CompanyMember98", type=sipme_ObjectsFileView, multiplicity=Multiplicity(1, 1)),
        Property(name="responsibleOfFile", type=sipme_CompanyMember, multiplicity=Multiplicity(0, 1))
    }
)
associatedObjective99: BinaryAssociation = BinaryAssociation(
    name="associatedObjective99",
    ends={
        Property(name="Objective100", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="takenIntoAccountBy", type=sipme_Objective, multiplicity=Multiplicity(0, 1))
    }
)
expresseCommonlydBy101: BinaryAssociation = BinaryAssociation(
    name="expresseCommonlydBy101",
    ends={
        Property(name="sipme_Stakeholder", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Requirement", type=sipme_Stakeholder, multiplicity=Multiplicity(0, 9999))
    }
)
refinesRequirement103: BinaryAssociation = BinaryAssociation(
    name="refinesRequirement103",
    ends={
        Property(name="sipme_Requirement104", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Requirement102", type=sipme_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
concernsResources105: BinaryAssociation = BinaryAssociation(
    name="concernsResources105",
    ends={
        Property(name="sipme_EnterpriseResource107", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Requirement106", type=sipme_EnterpriseResource, multiplicity=Multiplicity(0, 9999))
    }
)
refines78: BinaryAssociation = BinaryAssociation(
    name="refines78",
    ends={
        Property(name="Objective79", type=sipme_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="subObjectives", type=sipme_Objective, multiplicity=Multiplicity(1, 1))
    }
)
takenIntoAccountBy80: BinaryAssociation = BinaryAssociation(
    name="takenIntoAccountBy80",
    ends={
        Property(name="Requirement", type=sipme_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="associatedObjective", type=sipme_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
represents81: BinaryAssociation = BinaryAssociation(
    name="represents81",
    ends={
        Property(name="EnterpriseObject82", type=sipme_ObjectView, multiplicity=Multiplicity(1, 1)),
        Property(name="representedBy", type=sipme_EnterpriseObject, multiplicity=Multiplicity(1, 1))
    }
)
events83: BinaryAssociation = BinaryAssociation(
    name="events83",
    ends={
        Property(name="Event84", type=sipme_ObjectView, multiplicity=Multiplicity(1, 1)),
        Property(name="hasAssociatedEvents", type=sipme_Event, multiplicity=Multiplicity(0, 9999))
    }
)
workstations85: BinaryAssociation = BinaryAssociation(
    name="workstations85",
    ends={
        Property(name="Workstation86", type=sipme_OrganisationCell, multiplicity=Multiplicity(1, 1)),
        Property(name="organisationCell", type=sipme_Workstation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
covers87: BinaryAssociation = BinaryAssociation(
    name="covers87",
    ends={
        Property(name="Domain", type=sipme_OrganisationCell, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=sipme_Domain, multiplicity=Multiplicity(1, 9999))
    }
)
cellResponsible88: BinaryAssociation = BinaryAssociation(
    name="cellResponsible88",
    ends={
        Property(name="CompanyMember", type=sipme_OrganisationCell, multiplicity=Multiplicity(1, 1)),
        Property(name="responsibleOfCell", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1))
    }
)
assignedTo90: BinaryAssociation = BinaryAssociation(
    name="assignedTo90",
    ends={
        Property(name="sipme_OrganisationCell91", type=sipme_OrganisationCell, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_OrganisationCell89", type=sipme_OrganisationCell, multiplicity=Multiplicity(0, 9999))
    }
)
respectsRoleRules120: BinaryAssociation = BinaryAssociation(
    name="respectsRoleRules120",
    ends={
        Property(name="sipme_BusinessRules122", type=sipme_Role_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Role_Function121", type=sipme_BusinessRules, multiplicity=Multiplicity(0, 9999))
    }
)
expresses123: BinaryAssociation = BinaryAssociation(
    name="expresses123",
    ends={
        Property(name="sipme_Requirement125", type=sipme_Stakeholder, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Stakeholder124", type=sipme_Requirement, multiplicity=Multiplicity(0, 9999))
    }
)
respectsTaskRules126: BinaryAssociation = BinaryAssociation(
    name="respectsTaskRules126",
    ends={
        Property(name="sipme_BusinessRules128", type=sipme_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Task127", type=sipme_BusinessRules, multiplicity=Multiplicity(0, 1))
    }
)
taskOf129: BinaryAssociation = BinaryAssociation(
    name="taskOf129",
    ends={
        Property(name="Activity130", type=sipme_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="tasks", type=sipme_Activity, multiplicity=Multiplicity(1, 1))
    }
)
operations132: BinaryAssociation = BinaryAssociation(
    name="operations132",
    ends={
        Property(name="sipme_Task133", type=sipme_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Task131", type=sipme_Task, multiplicity=Multiplicity(0, 9999))
    }
)
concernsProcessors108: BinaryAssociation = BinaryAssociation(
    name="concernsProcessors108",
    ends={
        Property(name="sipme_EnterpriseProcessor110", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Requirement109", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(0, 1))
    }
)
concernsActivity111: BinaryAssociation = BinaryAssociation(
    name="concernsActivity111",
    ends={
        Property(name="sipme_Activity", type=sipme_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Requirement112", type=sipme_Activity, multiplicity=Multiplicity(0, 1))
    }
)
requiresTasks113: BinaryAssociation = BinaryAssociation(
    name="requiresTasks113",
    ends={
        Property(name="sipme_Task114", type=sipme_Role_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="sipme_Role_Function", type=sipme_Task, multiplicity=Multiplicity(1, 9999))
    }
)
playedBy115: BinaryAssociation = BinaryAssociation(
    name="playedBy115",
    ends={
        Property(name="EnterpriseResource", type=sipme_Role_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="plays", type=sipme_EnterpriseResource, multiplicity=Multiplicity(1, 9999))
    }
)
canBePlayedBy116: BinaryAssociation = BinaryAssociation(
    name="canBePlayedBy116",
    ends={
        Property(name="EnterpriseResource117", type=sipme_Role_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="isAbleToPlay", type=sipme_EnterpriseResource, multiplicity=Multiplicity(0, 9999))
    }
)
implementedBy118: BinaryAssociation = BinaryAssociation(
    name="implementedBy118",
    ends={
        Property(name="EnterpriseProcessor119", type=sipme_Role_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="implements", type=sipme_EnterpriseProcessor, multiplicity=Multiplicity(0, 9999))
    }
)
organisationCell134: BinaryAssociation = BinaryAssociation(
    name="organisationCell134",
    ends={
        Property(name="OrganisationCell135", type=sipme_Workstation, multiplicity=Multiplicity(1, 1)),
        Property(name="workstations", type=sipme_OrganisationCell, multiplicity=Multiplicity(0, 1))
    }
)
responsible136: BinaryAssociation = BinaryAssociation(
    name="responsible136",
    ends={
        Property(name="CompanyMember137", type=sipme_Workstation, multiplicity=Multiplicity(1, 1)),
        Property(name="responsibleOf", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 1))
    }
)
owners138: BinaryAssociation = BinaryAssociation(
    name="owners138",
    ends={
        Property(name="CompanyMember139", type=sipme_Workstation, multiplicity=Multiplicity(1, 1)),
        Property(name="inChargeOf", type=sipme_CompanyMember, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_sipme_Activity_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Activity)
gen_sipme_Application_EnterpriseResource = Generalization(general=EnterpriseResource, specific=sipme_Application)
gen_sipme_BusinessProcess_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_BusinessProcess)
gen_sipme_Device_Machine_EnterpriseResource = Generalization(general=EnterpriseResource, specific=sipme_Device_Machine)
gen_sipme_Domain_SIPME_object = Generalization(general=SIPME_object, specific=sipme_Domain)
gen_sipme_Domain_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Domain)
gen_sipme_Domain_OrganisationCell = Generalization(general=OrganisationCell, specific=sipme_Domain)
gen_sipme_BusinessRules_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_BusinessRules)
gen_sipme_Capability_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_Capability)
gen_sipme_Capacity_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_Capacity)
gen_sipme_CompanyMember_EnterpriseResource = Generalization(general=EnterpriseResource, specific=sipme_CompanyMember)
gen_sipme_CompanyMember_Stakeholder = Generalization(general=Stakeholder, specific=sipme_CompanyMember)
gen_sipme_EnterpriseProcessor_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_EnterpriseProcessor)
gen_sipme_Enterprise_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Enterprise)
gen_sipme_EnterpriseObject_SIPME_object = Generalization(general=SIPME_object, specific=sipme_EnterpriseObject)
gen_sipme_EnterpriseService_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_EnterpriseService)
gen_sipme_Event_SIPME_object = Generalization(general=SIPME_object, specific=sipme_Event)
gen_sipme_Objective_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_Objective)
gen_sipme_EnterpriseProduct_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_EnterpriseProduct)
gen_sipme_EnterpriseResource_EnterpriseObject = Generalization(general=EnterpriseObject, specific=sipme_EnterpriseResource)
gen_sipme_ObjectsFileView_ObjectView = Generalization(general=ObjectView, specific=sipme_ObjectsFileView)
gen_sipme_Requirement_SIPME_object = Generalization(general=SIPME_object, specific=sipme_Requirement)
gen_sipme_ObjectView_SIPME_object = Generalization(general=SIPME_object, specific=sipme_ObjectView)
gen_sipme_OrganisationCell_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_OrganisationCell)
gen_sipme_Stakeholder_SIPME_object = Generalization(general=SIPME_object, specific=sipme_Stakeholder)
gen_sipme_Task_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Task)
gen_sipme_Role_Function_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Role_Function)
gen_sipme_Workstation_EnterpriseProcessor = Generalization(general=EnterpriseProcessor, specific=sipme_Workstation)

# Domain Model
domain_model = DomainModel(
    name="sipme",
    types={sipme_Activity, EnterpriseProcessor, sipme_Task, sipme_BusinessProcess, sipme_Application, EnterpriseResource, sipme_Domain, sipme_OrganisationCell, sipme_ObjectsFileView, sipme_Device_Machine, SIPME_object, OrganisationCell, sipme_BusinessRules, EnterpriseObject, sipme_EnterpriseObject, sipme_Capability, sipme_Capacity, sipme_CompanyMember, Stakeholder, sipme_Workstation, sipme_ObjectView, sipme_EnterpriseProcessor, sipme_Event, sipme_Enterprise, sipme_Objective, sipme_EnterpriseService, sipme_EnterpriseProduct, sipme_Role_Function, sipme_EnterpriseResource, ObjectView, sipme_Stakeholder, sipme_Requirement, sipme_SIPME_object, RequirementNature, RequirementOrigin, RoleType, ProductState, ServiceState, ProductNature, CapabilityType, StakeholderType, EnterpriseObjectiveType, ObjectiveNature, Origin},
    associations={tasks0, activityOf1, activities2, businessProcessOf3, responsibleOfCell12, responsibleOfFile13, businessProcesses14, coveredBy17, induces19, considers4, impacts5, defines8, inChargeOf9, responsibleOf10, partOf38, representedBy39, decomposedIn41, generates43, providesOutputs44, hasInputs45, initiatedBy48, strategicObjectives22, concerns23, refers26, proposesServices29, proposesProducts31, companyMembers33, organizationCells35, generatedBy68, initiates69, priorTo72, hasAssociatedEvents73, subObjectives76, hasControlInputs50, implements53, hasCapacity54, requiresCapabilities57, executes60, plays61, isAbleToPlay63, providesCapability65, objectViews92, subFiles95, fileResponsible97, associatedObjective99, expresseCommonlydBy101, refinesRequirement103, concernsResources105, refines78, takenIntoAccountBy80, represents81, events83, workstations85, covers87, cellResponsible88, assignedTo90, respectsRoleRules120, expresses123, respectsTaskRules126, taskOf129, operations132, concernsProcessors108, concernsActivity111, requiresTasks113, playedBy115, canBePlayedBy116, implementedBy118, organisationCell134, responsible136, owners138},
    generalizations={gen_sipme_Activity_EnterpriseProcessor, gen_sipme_Application_EnterpriseResource, gen_sipme_BusinessProcess_EnterpriseProcessor, gen_sipme_Device_Machine_EnterpriseResource, gen_sipme_Domain_SIPME_object, gen_sipme_Domain_EnterpriseProcessor, gen_sipme_Domain_OrganisationCell, gen_sipme_BusinessRules_EnterpriseObject, gen_sipme_Capability_EnterpriseObject, gen_sipme_Capacity_EnterpriseObject, gen_sipme_CompanyMember_EnterpriseResource, gen_sipme_CompanyMember_Stakeholder, gen_sipme_EnterpriseProcessor_EnterpriseObject, gen_sipme_Enterprise_EnterpriseProcessor, gen_sipme_EnterpriseObject_SIPME_object, gen_sipme_EnterpriseService_EnterpriseObject, gen_sipme_Event_SIPME_object, gen_sipme_Objective_EnterpriseObject, gen_sipme_EnterpriseProduct_EnterpriseObject, gen_sipme_EnterpriseResource_EnterpriseObject, gen_sipme_ObjectsFileView_ObjectView, gen_sipme_Requirement_SIPME_object, gen_sipme_ObjectView_SIPME_object, gen_sipme_OrganisationCell_EnterpriseProcessor, gen_sipme_Stakeholder_SIPME_object, gen_sipme_Task_EnterpriseProcessor, gen_sipme_Role_Function_EnterpriseProcessor, gen_sipme_Workstation_EnterpriseProcessor},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)