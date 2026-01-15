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
InterrestKindType: Enumeration = Enumeration(
    name="InterrestKindType",
    literals={
            EnumerationLiteral(name="Escallation"),
			EnumerationLiteral(name="Reporting"),
			EnumerationLiteral(name="SalesManagement"),
			EnumerationLiteral(name="ProductManagement"),
			EnumerationLiteral(name="FinancialManagement"),
			EnumerationLiteral(name="ServiceManagement")
    }
)

LifeCycleStateType: Enumeration = Enumeration(
    name="LifeCycleStateType",
    literals={
            EnumerationLiteral(name="Planned"),
			EnumerationLiteral(name="Active"),
			EnumerationLiteral(name="Removed")
    }
)

MaintenanceType: Enumeration = Enumeration(
    name="MaintenanceType",
    literals={
            EnumerationLiteral(name="_1stLineMaintenance"),
			EnumerationLiteral(name="_2ndLineMaintenance")
    }
)

SecurityRatingType: Enumeration = Enumeration(
    name="SecurityRatingType",
    literals={
            EnumerationLiteral(name="High"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Low")
    }
)

ServiceClassType: Enumeration = Enumeration(
    name="ServiceClassType",
    literals={
            EnumerationLiteral(name="Sold"),
			EnumerationLiteral(name="Silver"),
			EnumerationLiteral(name="Bronze")
    }
)

ServiceKindType: Enumeration = Enumeration(
    name="ServiceKindType",
    literals={
            EnumerationLiteral(name="RFS"),
			EnumerationLiteral(name="CFS")
    }
)

UsageStateType: Enumeration = Enumeration(
    name="UsageStateType",
    literals={
            EnumerationLiteral(name="Assigned"),
			EnumerationLiteral(name="Reserved"),
			EnumerationLiteral(name="Free"),
			EnumerationLiteral(name="Disabled")
    }
)

# Classes
services_CFSService = Class(name="services::CFSService")
Service = Class(name="Service")
services_EObject = Class(name="services::EObject")
services_CIID = Class(name="services::CIID")
services_RFSService = Class(name="services::RFSService")
services_ServiceProfile = Class(name="services::ServiceProfile")
services_Service = Class(name="services::Service")
services_ServiceName = Class(name="services::ServiceName")
services_ServiceDescription = Class(name="services::ServiceDescription")
services_ServiceIncidentMgt = Class(name="services::ServiceIncidentMgt")
services_ServiceInterrest = Class(name="services::ServiceInterrest")
services_ServiceContract = Class(name="services::ServiceContract")
services_ServiceSupport = Class(name="services::ServiceSupport")
services_ServiceAdditional = Class(name="services::ServiceAdditional")
services_ServiceSecurityMgt = Class(name="services::ServiceSecurityMgt")
services_Parameter = Class(name="services::Parameter")

# services_CFSService class attributes and methods
services_CFSService_provider: Property = Property(name="provider", type=StringType)
services_CFSService_scenario: Property = Property(name="scenario", type=StringType)
services_CFSService.attributes={services_CFSService_provider, services_CFSService_scenario}

# Service class attributes and methods

# services_EObject class attributes and methods

# services_CIID class attributes and methods
services_CIID_commonCIID: Property = Property(name="commonCIID", type=StringType)
services_CIID_localCIID: Property = Property(name="localCIID", type=StringType)
services_CIID.attributes={services_CIID_commonCIID, services_CIID_localCIID}

# services_RFSService class attributes and methods
services_RFSService_functionalCategory: Property = Property(name="functionalCategory", type=StringType)
services_RFSService_location: Property = Property(name="location", type=StringType)
services_RFSService.attributes={services_RFSService_location, services_RFSService_functionalCategory}

# services_ServiceProfile class attributes and methods
services_ServiceProfile_name: Property = Property(name="name", type=StringType)
services_ServiceProfile.attributes={services_ServiceProfile_name}

# services_Service class attributes and methods
services_Service_mostTopService: Property = Property(name="mostTopService", type=StringType)
services_Service_serviceCategory: Property = Property(name="serviceCategory", type=StringType)
services_Service_serviceCharacterCommon: Property = Property(name="serviceCharacterCommon", type=StringType)
services_Service_serviceClass: Property = Property(name="serviceClass", type=StringType)
services_Service_serviceKind: Property = Property(name="serviceKind", type=StringType)
services_Service_serviceSupport1: Property = Property(name="serviceSupport1", type=StringType)
services_Service_ssDomain: Property = Property(name="ssDomain", type=StringType)
services_Service.attributes={services_Service_serviceKind, services_Service_serviceSupport1, services_Service_serviceCategory, services_Service_serviceClass, services_Service_ssDomain, services_Service_serviceCharacterCommon, services_Service_mostTopService}

# services_ServiceName class attributes and methods
services_ServiceName_alias: Property = Property(name="alias", type=StringType)
services_ServiceName_identifier: Property = Property(name="identifier", type=StringType)
services_ServiceName_index: Property = Property(name="index", type=StringType)
services_ServiceName_name: Property = Property(name="name", type=StringType)
services_ServiceName.attributes={services_ServiceName_name, services_ServiceName_index, services_ServiceName_identifier, services_ServiceName_alias}

# services_ServiceDescription class attributes and methods
services_ServiceDescription_serviceDescriptionCommon: Property = Property(name="serviceDescriptionCommon", type=StringType)
services_ServiceDescription_serviceDescriptionNational: Property = Property(name="serviceDescriptionNational", type=StringType)
services_ServiceDescription.attributes={services_ServiceDescription_serviceDescriptionNational, services_ServiceDescription_serviceDescriptionCommon}

# services_ServiceIncidentMgt class attributes and methods
services_ServiceIncidentMgt_businessImpact: Property = Property(name="businessImpact", type=StringType)
services_ServiceIncidentMgt_maintenance: Property = Property(name="maintenance", type=StringType)
services_ServiceIncidentMgt_maintenanceWindow: Property = Property(name="maintenanceWindow", type=StringType)
services_ServiceIncidentMgt_monitoring: Property = Property(name="monitoring", type=StringType)
services_ServiceIncidentMgt.attributes={services_ServiceIncidentMgt_businessImpact, services_ServiceIncidentMgt_maintenance, services_ServiceIncidentMgt_monitoring, services_ServiceIncidentMgt_maintenanceWindow}

# services_ServiceInterrest class attributes and methods
services_ServiceInterrest_contactUnit: Property = Property(name="contactUnit", type=StringType)
services_ServiceInterrest_interrestKind: Property = Property(name="interrestKind", type=StringType)
services_ServiceInterrest.attributes={services_ServiceInterrest_interrestKind, services_ServiceInterrest_contactUnit}

# services_ServiceContract class attributes and methods
services_ServiceContract_oLA: Property = Property(name="oLA", type=StringType)
services_ServiceContract_sLA: Property = Property(name="sLA", type=StringType)
services_ServiceContract_uC: Property = Property(name="uC", type=StringType)
services_ServiceContract_wLA: Property = Property(name="wLA", type=StringType)
services_ServiceContract.attributes={services_ServiceContract_uC, services_ServiceContract_wLA, services_ServiceContract_sLA, services_ServiceContract_oLA}

# services_ServiceSupport class attributes and methods
services_ServiceSupport_supportDays: Property = Property(name="supportDays", type=StringType)
services_ServiceSupport_supportHours: Property = Property(name="supportHours", type=StringType)
services_ServiceSupport.attributes={services_ServiceSupport_supportHours, services_ServiceSupport_supportDays}

# services_ServiceAdditional class attributes and methods
services_ServiceAdditional_costCenter: Property = Property(name="costCenter", type=StringType)
services_ServiceAdditional_history: Property = Property(name="history", type=StringType)
services_ServiceAdditional_kpi: Property = Property(name="kpi", type=StringType)
services_ServiceAdditional_lifeCycleState: Property = Property(name="lifeCycleState", type=StringType)
services_ServiceAdditional_link: Property = Property(name="link", type=StringType)
services_ServiceAdditional_report: Property = Property(name="report", type=StringType)
services_ServiceAdditional_usageState: Property = Property(name="usageState", type=StringType)
services_ServiceAdditional.attributes={services_ServiceAdditional_costCenter, services_ServiceAdditional_history, services_ServiceAdditional_kpi, services_ServiceAdditional_usageState, services_ServiceAdditional_link, services_ServiceAdditional_report, services_ServiceAdditional_lifeCycleState}

# services_ServiceSecurityMgt class attributes and methods
services_ServiceSecurityMgt_drPlanContact: Property = Property(name="drPlanContact", type=StringType)
services_ServiceSecurityMgt_drPlanRepository: Property = Property(name="drPlanRepository", type=StringType)
services_ServiceSecurityMgt_drRecoveryPlan: Property = Property(name="drRecoveryPlan", type=StringType)
services_ServiceSecurityMgt_securityRating: Property = Property(name="securityRating", type=StringType)
services_ServiceSecurityMgt.attributes={services_ServiceSecurityMgt_drPlanContact, services_ServiceSecurityMgt_drPlanRepository, services_ServiceSecurityMgt_securityRating, services_ServiceSecurityMgt_drRecoveryPlan}

# services_Parameter class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="services_EObject", type=services_CFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_CFSService", type=services_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
serviceProfile3: BinaryAssociation = BinaryAssociation(
    name="serviceProfile3",
    ends={
        Property(name="services_ServiceProfile", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService4", type=services_ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceName5: BinaryAssociation = BinaryAssociation(
    name="serviceName5",
    ends={
        Property(name="services_ServiceName", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service", type=services_ServiceName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceDescription6: BinaryAssociation = BinaryAssociation(
    name="serviceDescription6",
    ends={
        Property(name="services_ServiceDescription", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service7", type=services_ServiceDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="services_EObject2", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService", type=services_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
serviceSecurityMgt8: BinaryAssociation = BinaryAssociation(
    name="serviceSecurityMgt8",
    ends={
        Property(name="services_ServiceSecurityMgt", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service9", type=services_ServiceSecurityMgt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceIncidentMgt10: BinaryAssociation = BinaryAssociation(
    name="serviceIncidentMgt10",
    ends={
        Property(name="services_ServiceIncidentMgt", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service11", type=services_ServiceIncidentMgt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ciID12: BinaryAssociation = BinaryAssociation(
    name="ciID12",
    ends={
        Property(name="services_CIID", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service13", type=services_CIID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceInterrest14: BinaryAssociation = BinaryAssociation(
    name="serviceInterrest14",
    ends={
        Property(name="services_ServiceInterrest", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service15", type=services_ServiceInterrest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceContracts16: BinaryAssociation = BinaryAssociation(
    name="serviceContracts16",
    ends={
        Property(name="services_ServiceContract", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service17", type=services_ServiceContract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceSupport18: BinaryAssociation = BinaryAssociation(
    name="serviceSupport18",
    ends={
        Property(name="services_ServiceSupport", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service19", type=services_ServiceSupport, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceMisc20: BinaryAssociation = BinaryAssociation(
    name="serviceMisc20",
    ends={
        Property(name="services_ServiceAdditional", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service21", type=services_ServiceAdditional, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services23: BinaryAssociation = BinaryAssociation(
    name="services23",
    ends={
        Property(name="services_Service24", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service22", type=services_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceParameters25: BinaryAssociation = BinaryAssociation(
    name="serviceParameters25",
    ends={
        Property(name="services_Parameter", type=services_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceProfile26", type=services_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_services_CFSService_Service = Generalization(general=Service, specific=services_CFSService)
gen_services_RFSService_Service = Generalization(general=Service, specific=services_RFSService)

# Domain Model
domain_model = DomainModel(
    name="services",
    types={services_CFSService, Service, services_EObject, services_CIID, services_RFSService, services_ServiceProfile, services_Service, services_ServiceName, services_ServiceDescription, services_ServiceIncidentMgt, services_ServiceInterrest, services_ServiceContract, services_ServiceSupport, services_ServiceAdditional, services_ServiceSecurityMgt, services_Parameter, InterrestKindType, LifeCycleStateType, MaintenanceType, SecurityRatingType, ServiceClassType, ServiceKindType, UsageStateType},
    associations={elements0, serviceProfile3, serviceName5, serviceDescription6, elements1, serviceSecurityMgt8, serviceIncidentMgt10, ciID12, serviceInterrest14, serviceContracts16, serviceSupport18, serviceMisc20, services23, serviceParameters25},
    generalizations={gen_services_CFSService_Service, gen_services_RFSService_Service},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)