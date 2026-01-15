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
StandardsClass: Enumeration = Enumeration(
    name="StandardsClass",
    literals={
            EnumerationLiteral(name="NonStandard"),
			EnumerationLiteral(name="Proposed"),
			EnumerationLiteral(name="Provisional"),
			EnumerationLiteral(name="Standard"),
			EnumerationLiteral(name="PhasingOut"),
			EnumerationLiteral(name="Retired")
    }
)

PrincipleCategory: Enumeration = Enumeration(
    name="PrincipleCategory",
    literals={
            EnumerationLiteral(name="GuidingPrinciple"),
			EnumerationLiteral(name="BusinessPrinciple"),
			EnumerationLiteral(name="DataPrinciple"),
			EnumerationLiteral(name="ApplicationPrinciple"),
			EnumerationLiteral(name="IntegrationPrinciple"),
			EnumerationLiteral(name="TechnologyPrinciple")
    }
)

LifeCycleStatus: Enumeration = Enumeration(
    name="LifeCycleStatus",
    literals={
            EnumerationLiteral(name="Proposed"),
			EnumerationLiteral(name="InDevelopment"),
			EnumerationLiteral(name="Live"),
			EnumerationLiteral(name="PhasingOut"),
			EnumerationLiteral(name="Retired")
    }
)

DataEntityCategory: Enumeration = Enumeration(
    name="DataEntityCategory",
    literals={
            EnumerationLiteral(name="Message"),
			EnumerationLiteral(name="InternallyStoredEntity")
    }
)

WorkPackageCategory: Enumeration = Enumeration(
    name="WorkPackageCategory",
    literals={
            EnumerationLiteral(name="WorkPackage"),
			EnumerationLiteral(name="WorkStream"),
			EnumerationLiteral(name="Project"),
			EnumerationLiteral(name="Program"),
			EnumerationLiteral(name="Portofolio")
    }
)

# Classes
contentfwk_Architecture = Class(name="contentfwk::Architecture", is_abstract=True)
contentfwk_BusinessArchitecture = Class(name="contentfwk::BusinessArchitecture")
Architecture = Class(name="Architecture")
contentfwk_Driver = Class(name="contentfwk::Driver")
contentfwk_Goal = Class(name="contentfwk::Goal")
contentfwk_Objective = Class(name="contentfwk::Objective")
contentfwk_OrganizationUnit = Class(name="contentfwk::OrganizationUnit")
contentfwk_Actor = Class(name="contentfwk::Actor")
contentfwk_Role = Class(name="contentfwk::Role")
contentfwk_Function = Class(name="contentfwk::Function")
contentfwk_BusinessService = Class(name="contentfwk::BusinessService")
contentfwk_Process = Class(name="contentfwk::Process")
contentfwk_EnterpriseArchitecture = Class(name="contentfwk::EnterpriseArchitecture")
contentfwk_Measure = Class(name="contentfwk::Measure")
contentfwk_ServiceQuality = Class(name="contentfwk::ServiceQuality")
contentfwk_DataArchitecture = Class(name="contentfwk::DataArchitecture")
contentfwk_DataEntity = Class(name="contentfwk::DataEntity")
contentfwk_LogicalDataComponent = Class(name="contentfwk::LogicalDataComponent")
contentfwk_PhysicalDataComponent = Class(name="contentfwk::PhysicalDataComponent")
contentfwk_TechnologyArchitecture = Class(name="contentfwk::TechnologyArchitecture")
contentfwk_PlatformService = Class(name="contentfwk::PlatformService")
contentfwk_PhysicalTechnologyComponent = Class(name="contentfwk::PhysicalTechnologyComponent")
contentfwk_LogicalTechnologyComponent = Class(name="contentfwk::LogicalTechnologyComponent")
Element = Class(name="Element")
contentfwk_Control = Class(name="contentfwk::Control")
contentfwk_Event = Class(name="contentfwk::Event")
contentfwk_Location = Class(name="contentfwk::Location")
contentfwk_Product = Class(name="contentfwk::Product")
contentfwk_Contract = Class(name="contentfwk::Contract")
contentfwk_Service = Class(name="contentfwk::Service", is_abstract=True)
contentfwk_LogicalApplicationComponent = Class(name="contentfwk::LogicalApplicationComponent")
Standard = Class(name="Standard")
Service = Class(name="Service")
ApplicationComponent = Class(name="ApplicationComponent")
contentfwk_PhysicalApplicationComponent = Class(name="contentfwk::PhysicalApplicationComponent")
TechnologyComponent = Class(name="TechnologyComponent")
contentfwk_Capability = Class(name="contentfwk::Capability")
contentfwk_WorkPackage = Class(name="contentfwk::WorkPackage")
contentfwk_Element = Class(name="contentfwk::Element")
contentfwk_Constraint = Class(name="contentfwk::Constraint")
contentfwk_Assumption = Class(name="contentfwk::Assumption")
contentfwk_Requirement = Class(name="contentfwk::Requirement")
contentfwk_Gap = Class(name="contentfwk::Gap")
DataComponent = Class(name="DataComponent")
contentfwk_StrategicElement = Class(name="contentfwk::StrategicElement", is_abstract=True)
contentfwk_Principle = Class(name="contentfwk::Principle")
StrategicElement = Class(name="StrategicElement")
contentfwk_ApplicationArchitecture = Class(name="contentfwk::ApplicationArchitecture")
contentfwk_InformationSystemService = Class(name="contentfwk::InformationSystemService")
contentfwk_Standard = Class(name="contentfwk::Standard", is_abstract=True)
contentfwk_StrategicArchitecture = Class(name="contentfwk::StrategicArchitecture")
contentfwk_ApplicationComponent = Class(name="contentfwk::ApplicationComponent", is_abstract=True)
contentfwk_DataComponent = Class(name="contentfwk::DataComponent", is_abstract=True)
contentfwk_TechnologyComponent = Class(name="contentfwk::TechnologyComponent", is_abstract=True)

# contentfwk_Architecture class attributes and methods
contentfwk_Architecture_ID: Property = Property(name="ID", type=StringType)
contentfwk_Architecture_m_forceID: Method = Method(name="forceID", parameters={Parameter(name='newID')})
contentfwk_Architecture.attributes={contentfwk_Architecture_ID}
contentfwk_Architecture.methods={contentfwk_Architecture_m_forceID}

# contentfwk_BusinessArchitecture class attributes and methods

# Architecture class attributes and methods

# contentfwk_Driver class attributes and methods

# contentfwk_Goal class attributes and methods

# contentfwk_Objective class attributes and methods

# contentfwk_OrganizationUnit class attributes and methods
contentfwk_OrganizationUnit_headcount: Property = Property(name="headcount", type=StringType)
contentfwk_OrganizationUnit.attributes={contentfwk_OrganizationUnit_headcount}

# contentfwk_Actor class attributes and methods
contentfwk_Actor_FTEs: Property = Property(name="FTEs", type=StringType)
contentfwk_Actor_actorGoal: Property = Property(name="actorGoal", type=StringType)
contentfwk_Actor_actorTasks: Property = Property(name="actorTasks", type=StringType)
contentfwk_Actor.attributes={contentfwk_Actor_actorTasks, contentfwk_Actor_actorGoal, contentfwk_Actor_FTEs}

# contentfwk_Role class attributes and methods
contentfwk_Role_estimatedFTEs: Property = Property(name="estimatedFTEs", type=StringType)
contentfwk_Role.attributes={contentfwk_Role_estimatedFTEs}

# contentfwk_Function class attributes and methods

# contentfwk_BusinessService class attributes and methods

# contentfwk_Process class attributes and methods
contentfwk_Process_processCritiality: Property = Property(name="processCritiality", type=StringType)
contentfwk_Process_isAutomated: Property = Property(name="isAutomated", type=BooleanType)
contentfwk_Process_processVolumetrics: Property = Property(name="processVolumetrics", type=StringType)
contentfwk_Process.attributes={contentfwk_Process_processCritiality, contentfwk_Process_processVolumetrics, contentfwk_Process_isAutomated}

# contentfwk_EnterpriseArchitecture class attributes and methods
contentfwk_EnterpriseArchitecture_ID: Property = Property(name="ID", type=StringType)
contentfwk_EnterpriseArchitecture_m_forceID: Method = Method(name="forceID", parameters={Parameter(name='newID')})
contentfwk_EnterpriseArchitecture.attributes={contentfwk_EnterpriseArchitecture_ID}
contentfwk_EnterpriseArchitecture.methods={contentfwk_EnterpriseArchitecture_m_forceID}

# contentfwk_Measure class attributes and methods

# contentfwk_ServiceQuality class attributes and methods

# contentfwk_DataArchitecture class attributes and methods

# contentfwk_DataEntity class attributes and methods
contentfwk_DataEntity_dataEntityCategory: Property = Property(name="dataEntityCategory", type=StringType)
contentfwk_DataEntity_privacyClassification: Property = Property(name="privacyClassification", type=StringType)
contentfwk_DataEntity_retentionClassification: Property = Property(name="retentionClassification", type=StringType)
contentfwk_DataEntity.attributes={contentfwk_DataEntity_retentionClassification, contentfwk_DataEntity_privacyClassification, contentfwk_DataEntity_dataEntityCategory}

# contentfwk_LogicalDataComponent class attributes and methods

# contentfwk_PhysicalDataComponent class attributes and methods

# contentfwk_TechnologyArchitecture class attributes and methods

# contentfwk_PlatformService class attributes and methods
contentfwk_PlatformService_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_PlatformService_standardClass: Property = Property(name="standardClass", type=StringType)
contentfwk_PlatformService.attributes={contentfwk_PlatformService_standardClass, contentfwk_PlatformService_categoryTRM}

# contentfwk_PhysicalTechnologyComponent class attributes and methods
contentfwk_PhysicalTechnologyComponent_productName: Property = Property(name="productName", type=StringType)
contentfwk_PhysicalTechnologyComponent_moduleName: Property = Property(name="moduleName", type=StringType)
contentfwk_PhysicalTechnologyComponent_vendor: Property = Property(name="vendor", type=StringType)
contentfwk_PhysicalTechnologyComponent_version: Property = Property(name="version", type=StringType)
contentfwk_PhysicalTechnologyComponent_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_PhysicalTechnologyComponent.attributes={contentfwk_PhysicalTechnologyComponent_categoryTRM, contentfwk_PhysicalTechnologyComponent_version, contentfwk_PhysicalTechnologyComponent_moduleName, contentfwk_PhysicalTechnologyComponent_vendor, contentfwk_PhysicalTechnologyComponent_productName}

# contentfwk_LogicalTechnologyComponent class attributes and methods
contentfwk_LogicalTechnologyComponent_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_LogicalTechnologyComponent.attributes={contentfwk_LogicalTechnologyComponent_categoryTRM}

# Element class attributes and methods

# contentfwk_Control class attributes and methods

# contentfwk_Event class attributes and methods

# contentfwk_Location class attributes and methods

# contentfwk_Product class attributes and methods

# contentfwk_Contract class attributes and methods
contentfwk_Contract_servicesTimes: Property = Property(name="servicesTimes", type=StringType)
contentfwk_Contract_manageabilityCharacteristics: Property = Property(name="manageabilityCharacteristics", type=StringType)
contentfwk_Contract_serviceabilityCharacteristics: Property = Property(name="serviceabilityCharacteristics", type=StringType)
contentfwk_Contract_performanceCharacteristics: Property = Property(name="performanceCharacteristics", type=StringType)
contentfwk_Contract_responseCharacteristics: Property = Property(name="responseCharacteristics", type=StringType)
contentfwk_Contract_reliabilityCharacteristics: Property = Property(name="reliabilityCharacteristics", type=StringType)
contentfwk_Contract_qualityOfInformationRequired: Property = Property(name="qualityOfInformationRequired", type=StringType)
contentfwk_Contract_contractControlRequirements: Property = Property(name="contractControlRequirements", type=StringType)
contentfwk_Contract_resultControlRequirements: Property = Property(name="resultControlRequirements", type=StringType)
contentfwk_Contract_recoverabilityCharacteristics: Property = Property(name="recoverabilityCharacteristics", type=StringType)
contentfwk_Contract_locatabilityCharacteristics: Property = Property(name="locatabilityCharacteristics", type=StringType)
contentfwk_Contract_securityCharacteristics: Property = Property(name="securityCharacteristics", type=StringType)
contentfwk_Contract_privacyCharacteristics: Property = Property(name="privacyCharacteristics", type=StringType)
contentfwk_Contract_integrityCharacteristics: Property = Property(name="integrityCharacteristics", type=StringType)
contentfwk_Contract_credibilityCharacteristics: Property = Property(name="credibilityCharacteristics", type=StringType)
contentfwk_Contract_localizationCharacteristics: Property = Property(name="localizationCharacteristics", type=StringType)
contentfwk_Contract_internationalizationCharacteristics: Property = Property(name="internationalizationCharacteristics", type=StringType)
contentfwk_Contract_interoperabilityCharacteristics: Property = Property(name="interoperabilityCharacteristics", type=StringType)
contentfwk_Contract_scalabilityCharacteristics: Property = Property(name="scalabilityCharacteristics", type=StringType)
contentfwk_Contract_portabilityCharacteristics: Property = Property(name="portabilityCharacteristics", type=StringType)
contentfwk_Contract_extensibilityCharacteristics: Property = Property(name="extensibilityCharacteristics", type=StringType)
contentfwk_Contract_capacityCharacteristics: Property = Property(name="capacityCharacteristics", type=StringType)
contentfwk_Contract_throughput: Property = Property(name="throughput", type=StringType)
contentfwk_Contract_throughputPeriod: Property = Property(name="throughputPeriod", type=StringType)
contentfwk_Contract_growth: Property = Property(name="growth", type=StringType)
contentfwk_Contract_growthPeriod: Property = Property(name="growthPeriod", type=StringType)
contentfwk_Contract_peakProfileShortTerm: Property = Property(name="peakProfileShortTerm", type=StringType)
contentfwk_Contract_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
contentfwk_Contract_behaviorCharacteristics: Property = Property(name="behaviorCharacteristics", type=StringType)
contentfwk_Contract_serviceNameCaller: Property = Property(name="serviceNameCaller", type=StringType)
contentfwk_Contract_serviceNameCalled: Property = Property(name="serviceNameCalled", type=StringType)
contentfwk_Contract_serviceQualityCharacteristics: Property = Property(name="serviceQualityCharacteristics", type=StringType)
contentfwk_Contract_availabilityQualityCharacteristics: Property = Property(name="availabilityQualityCharacteristics", type=StringType)
contentfwk_Contract.attributes={contentfwk_Contract_throughputPeriod, contentfwk_Contract_interoperabilityCharacteristics, contentfwk_Contract_capacityCharacteristics, contentfwk_Contract_availabilityQualityCharacteristics, contentfwk_Contract_manageabilityCharacteristics, contentfwk_Contract_serviceQualityCharacteristics, contentfwk_Contract_portabilityCharacteristics, contentfwk_Contract_localizationCharacteristics, contentfwk_Contract_peakProfileShortTerm, contentfwk_Contract_recoverabilityCharacteristics, contentfwk_Contract_locatabilityCharacteristics, contentfwk_Contract_behaviorCharacteristics, contentfwk_Contract_qualityOfInformationRequired, contentfwk_Contract_growth, contentfwk_Contract_servicesTimes, contentfwk_Contract_performanceCharacteristics, contentfwk_Contract_privacyCharacteristics, contentfwk_Contract_peakProfileLongTerm, contentfwk_Contract_scalabilityCharacteristics, contentfwk_Contract_extensibilityCharacteristics, contentfwk_Contract_contractControlRequirements, contentfwk_Contract_credibilityCharacteristics, contentfwk_Contract_growthPeriod, contentfwk_Contract_serviceNameCaller, contentfwk_Contract_throughput, contentfwk_Contract_serviceabilityCharacteristics, contentfwk_Contract_responseCharacteristics, contentfwk_Contract_serviceNameCalled, contentfwk_Contract_integrityCharacteristics, contentfwk_Contract_securityCharacteristics, contentfwk_Contract_internationalizationCharacteristics, contentfwk_Contract_reliabilityCharacteristics, contentfwk_Contract_resultControlRequirements}

# contentfwk_Service class attributes and methods

# contentfwk_LogicalApplicationComponent class attributes and methods

# Standard class attributes and methods

# Service class attributes and methods

# ApplicationComponent class attributes and methods

# contentfwk_PhysicalApplicationComponent class attributes and methods
contentfwk_PhysicalApplicationComponent_lifeCycleStatus: Property = Property(name="lifeCycleStatus", type=StringType)
contentfwk_PhysicalApplicationComponent_initialLiveDate: Property = Property(name="initialLiveDate", type=DateType)
contentfwk_PhysicalApplicationComponent_dateOfLastRelease: Property = Property(name="dateOfLastRelease", type=DateType)
contentfwk_PhysicalApplicationComponent_dateOfNextRelease: Property = Property(name="dateOfNextRelease", type=DateType)
contentfwk_PhysicalApplicationComponent_retirementDate: Property = Property(name="retirementDate", type=DateType)
contentfwk_PhysicalApplicationComponent_availabilityCharacteristics: Property = Property(name="availabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_servicesTimes: Property = Property(name="servicesTimes", type=StringType)
contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics: Property = Property(name="manageabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics: Property = Property(name="serviceabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_performanceCharacteristics: Property = Property(name="performanceCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics: Property = Property(name="reliabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics: Property = Property(name="recoverabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics: Property = Property(name="locatabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_securityCharacteristics: Property = Property(name="securityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_privacyCharacteristics: Property = Property(name="privacyCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_integrityCharacteristics: Property = Property(name="integrityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_credibilityCharacteristics: Property = Property(name="credibilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_localizationCharacteristics: Property = Property(name="localizationCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics: Property = Property(name="internationalizationCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics: Property = Property(name="interoperabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics: Property = Property(name="scalabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_portabilityCharacteristics: Property = Property(name="portabilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics: Property = Property(name="extensibilityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_capacityCharacteristics: Property = Property(name="capacityCharacteristics", type=StringType)
contentfwk_PhysicalApplicationComponent_throughput: Property = Property(name="throughput", type=StringType)
contentfwk_PhysicalApplicationComponent_throughputPeriod: Property = Property(name="throughputPeriod", type=StringType)
contentfwk_PhysicalApplicationComponent_growth: Property = Property(name="growth", type=StringType)
contentfwk_PhysicalApplicationComponent_growthPeriod: Property = Property(name="growthPeriod", type=StringType)
contentfwk_PhysicalApplicationComponent_peakProfileShortTerm: Property = Property(name="peakProfileShortTerm", type=StringType)
contentfwk_PhysicalApplicationComponent_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
contentfwk_PhysicalApplicationComponent.attributes={contentfwk_PhysicalApplicationComponent_growthPeriod, contentfwk_PhysicalApplicationComponent_throughput, contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics, contentfwk_PhysicalApplicationComponent_privacyCharacteristics, contentfwk_PhysicalApplicationComponent_integrityCharacteristics, contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics, contentfwk_PhysicalApplicationComponent_growth, contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics, contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics, contentfwk_PhysicalApplicationComponent_dateOfLastRelease, contentfwk_PhysicalApplicationComponent_localizationCharacteristics, contentfwk_PhysicalApplicationComponent_retirementDate, contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics, contentfwk_PhysicalApplicationComponent_throughputPeriod, contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics, contentfwk_PhysicalApplicationComponent_portabilityCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileLongTerm, contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics, contentfwk_PhysicalApplicationComponent_lifeCycleStatus, contentfwk_PhysicalApplicationComponent_credibilityCharacteristics, contentfwk_PhysicalApplicationComponent_initialLiveDate, contentfwk_PhysicalApplicationComponent_servicesTimes, contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileShortTerm, contentfwk_PhysicalApplicationComponent_securityCharacteristics, contentfwk_PhysicalApplicationComponent_availabilityCharacteristics, contentfwk_PhysicalApplicationComponent_performanceCharacteristics, contentfwk_PhysicalApplicationComponent_capacityCharacteristics, contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics, contentfwk_PhysicalApplicationComponent_dateOfNextRelease}

# TechnologyComponent class attributes and methods

# contentfwk_Capability class attributes and methods
contentfwk_Capability_businessValue: Property = Property(name="businessValue", type=StringType)
contentfwk_Capability_increments: Property = Property(name="increments", type=StringType)
contentfwk_Capability.attributes={contentfwk_Capability_increments, contentfwk_Capability_businessValue}

# contentfwk_WorkPackage class attributes and methods
contentfwk_WorkPackage_workPackageCategory: Property = Property(name="workPackageCategory", type=StringType)
contentfwk_WorkPackage_capabilityDelivered: Property = Property(name="capabilityDelivered", type=StringType)
contentfwk_WorkPackage.attributes={contentfwk_WorkPackage_capabilityDelivered, contentfwk_WorkPackage_workPackageCategory}

# contentfwk_Element class attributes and methods
contentfwk_Element_name: Property = Property(name="name", type=StringType)
contentfwk_Element_description: Property = Property(name="description", type=StringType)
contentfwk_Element_sourceDescr: Property = Property(name="sourceDescr", type=StringType)
contentfwk_Element_ownerDescr: Property = Property(name="ownerDescr", type=StringType)
contentfwk_Element_ID: Property = Property(name="ID", type=StringType)
contentfwk_Element_category: Property = Property(name="category", type=StringType)
contentfwk_Element_m_forceID: Method = Method(name="forceID", parameters={Parameter(name='newID')})
contentfwk_Element.attributes={contentfwk_Element_name, contentfwk_Element_category, contentfwk_Element_ownerDescr, contentfwk_Element_ID, contentfwk_Element_sourceDescr, contentfwk_Element_description}
contentfwk_Element.methods={contentfwk_Element_m_forceID}

# contentfwk_Constraint class attributes and methods

# contentfwk_Assumption class attributes and methods

# contentfwk_Requirement class attributes and methods
contentfwk_Requirement_statementOfRequirement: Property = Property(name="statementOfRequirement", type=StringType)
contentfwk_Requirement_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Requirement_acceptanceCriteria: Property = Property(name="acceptanceCriteria", type=StringType)
contentfwk_Requirement.attributes={contentfwk_Requirement_statementOfRequirement, contentfwk_Requirement_acceptanceCriteria, contentfwk_Requirement_rationale}

# contentfwk_Gap class attributes and methods

# DataComponent class attributes and methods

# contentfwk_StrategicElement class attributes and methods

# contentfwk_Principle class attributes and methods
contentfwk_Principle_statementOfPrinciple: Property = Property(name="statementOfPrinciple", type=StringType)
contentfwk_Principle_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Principle_implication: Property = Property(name="implication", type=StringType)
contentfwk_Principle_metric: Property = Property(name="metric", type=StringType)
contentfwk_Principle_principleCategory: Property = Property(name="principleCategory", type=StringType)
contentfwk_Principle_priority: Property = Property(name="priority", type=StringType)
contentfwk_Principle.attributes={contentfwk_Principle_implication, contentfwk_Principle_metric, contentfwk_Principle_priority, contentfwk_Principle_principleCategory, contentfwk_Principle_rationale, contentfwk_Principle_statementOfPrinciple}

# StrategicElement class attributes and methods

# contentfwk_ApplicationArchitecture class attributes and methods

# contentfwk_InformationSystemService class attributes and methods

# contentfwk_Standard class attributes and methods
contentfwk_Standard_standardClass: Property = Property(name="standardClass", type=StringType)
contentfwk_Standard_standardCreationDate: Property = Property(name="standardCreationDate", type=DateType)
contentfwk_Standard_lastStandardReviewDate: Property = Property(name="lastStandardReviewDate", type=DateType)
contentfwk_Standard_nextStandardReviewDate: Property = Property(name="nextStandardReviewDate", type=DateType)
contentfwk_Standard_retireDate: Property = Property(name="retireDate", type=DateType)
contentfwk_Standard.attributes={contentfwk_Standard_lastStandardReviewDate, contentfwk_Standard_standardCreationDate, contentfwk_Standard_retireDate, contentfwk_Standard_nextStandardReviewDate, contentfwk_Standard_standardClass}

# contentfwk_StrategicArchitecture class attributes and methods

# contentfwk_ApplicationComponent class attributes and methods

# contentfwk_DataComponent class attributes and methods

# contentfwk_TechnologyComponent class attributes and methods

# Relationships
architectures0: BinaryAssociation = BinaryAssociation(
    name="architectures0",
    ends={
        Property(name="contentfwk_Architecture", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_EnterpriseArchitecture", type=contentfwk_Architecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drivers1: BinaryAssociation = BinaryAssociation(
    name="drivers1",
    ends={
        Property(name="contentfwk_Driver", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals2: BinaryAssociation = BinaryAssociation(
    name="goals2",
    ends={
        Property(name="contentfwk_Goal", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture3", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectives4: BinaryAssociation = BinaryAssociation(
    name="objectives4",
    ends={
        Property(name="contentfwk_Objective", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture5", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units6: BinaryAssociation = BinaryAssociation(
    name="units6",
    ends={
        Property(name="contentfwk_OrganizationUnit", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture7", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors8: BinaryAssociation = BinaryAssociation(
    name="actors8",
    ends={
        Property(name="contentfwk_Actor", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture9", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles10: BinaryAssociation = BinaryAssociation(
    name="roles10",
    ends={
        Property(name="contentfwk_Role", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture11", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions12: BinaryAssociation = BinaryAssociation(
    name="functions12",
    ends={
        Property(name="contentfwk_Function", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture13", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services14: BinaryAssociation = BinaryAssociation(
    name="services14",
    ends={
        Property(name="contentfwk_BusinessService", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture15", type=contentfwk_BusinessService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes16: BinaryAssociation = BinaryAssociation(
    name="processes16",
    ends={
        Property(name="contentfwk_Process", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture17", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures28: BinaryAssociation = BinaryAssociation(
    name="measures28",
    ends={
        Property(name="contentfwk_Measure", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture29", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicesQuality30: BinaryAssociation = BinaryAssociation(
    name="servicesQuality30",
    ends={
        Property(name="contentfwk_ServiceQuality", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture31", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities32: BinaryAssociation = BinaryAssociation(
    name="entities32",
    ends={
        Property(name="contentfwk_DataEntity", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents33: BinaryAssociation = BinaryAssociation(
    name="logicalComponents33",
    ends={
        Property(name="contentfwk_LogicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture34", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents35: BinaryAssociation = BinaryAssociation(
    name="physicalComponents35",
    ends={
        Property(name="contentfwk_PhysicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture36", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platformServices37: BinaryAssociation = BinaryAssociation(
    name="platformServices37",
    ends={
        Property(name="contentfwk_PlatformService", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents38: BinaryAssociation = BinaryAssociation(
    name="physicalComponents38",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture39", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents40: BinaryAssociation = BinaryAssociation(
    name="logicalComponents40",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture41", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createsGoals42: BinaryAssociation = BinaryAssociation(
    name="createsGoals42",
    ends={
        Property(name="Goal", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="addressesDrivers", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
motivatesOrganizationUnits43: BinaryAssociation = BinaryAssociation(
    name="motivatesOrganizationUnits43",
    ends={
        Property(name="OrganizationUnit", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="isMotivatedByDrivers", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesDriver45: BinaryAssociation = BinaryAssociation(
    name="decomposesDriver45",
    ends={
        Property(name="Driver", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByDrivers", type=contentfwk_Driver, multiplicity=Multiplicity(0, 1))
    }
)
controls18: BinaryAssociation = BinaryAssociation(
    name="controls18",
    ends={
        Property(name="contentfwk_Control", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture19", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events20: BinaryAssociation = BinaryAssociation(
    name="events20",
    ends={
        Property(name="contentfwk_Event", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture21", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations22: BinaryAssociation = BinaryAssociation(
    name="locations22",
    ends={
        Property(name="contentfwk_Location", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture23", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products24: BinaryAssociation = BinaryAssociation(
    name="products24",
    ends={
        Property(name="contentfwk_Product", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture25", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contracts26: BinaryAssociation = BinaryAssociation(
    name="contracts26",
    ends={
        Property(name="contentfwk_Contract", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture27", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isDecomposedByGoals56: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByGoals56",
    ends={
        Property(name="Goal57", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesGoal", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
realizesGoals58: BinaryAssociation = BinaryAssociation(
    name="realizesGoals58",
    ends={
        Property(name="Goal59", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughObjectives", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures60: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures60",
    ends={
        Property(name="Measure", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForObjectives", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesObjective62: BinaryAssociation = BinaryAssociation(
    name="decomposesObjective62",
    ends={
        Property(name="Objective63", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByObjectives", type=contentfwk_Objective, multiplicity=Multiplicity(0, 1))
    }
)
isSupportedByBusinessService64: BinaryAssociation = BinaryAssociation(
    name="isSupportedByBusinessService64",
    ends={
        Property(name="BusinessService", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsObjective", type=contentfwk_BusinessService, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByObjectives66: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByObjectives66",
    ends={
        Property(name="Objective67", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesObjective", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
ownsAndGovernsServices68: BinaryAssociation = BinaryAssociation(
    name="ownsAndGovernsServices68",
    ends={
        Property(name="Service", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedAndGovernedByOrganizationUnits", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors69: BinaryAssociation = BinaryAssociation(
    name="containsActors69",
    ends={
        Property(name="Actor", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsToOrganizationUnit", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
ownsFunctions70: BinaryAssociation = BinaryAssociation(
    name="ownsFunctions70",
    ends={
        Property(name="Function", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedByOrganizationUnit", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses71: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses71",
    ends={
        Property(name="Process", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesOrganizationUnits", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isMotivatedByDrivers72: BinaryAssociation = BinaryAssociation(
    name="isMotivatedByDrivers72",
    ends={
        Property(name="Driver73", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="motivatesOrganizationUnits", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts74: BinaryAssociation = BinaryAssociation(
    name="producesProducts74",
    ends={
        Property(name="Product", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByOrganizationUnits", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation75: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation75",
    ends={
        Property(name="Location", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="containsOrganizationUnits", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
decomposesOrganizationUnit77: BinaryAssociation = BinaryAssociation(
    name="decomposesOrganizationUnit77",
    ends={
        Property(name="OrganizationUnit78", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByOrganizationUnits", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByOrganizationUnits80: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByOrganizationUnits80",
    ends={
        Property(name="OrganizationUnit81", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesOrganizationUnit", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByDrivers47: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByDrivers47",
    ends={
        Property(name="Driver48", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesDriver", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
addressesDrivers49: BinaryAssociation = BinaryAssociation(
    name="addressesDrivers49",
    ends={
        Property(name="Driver50", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="createsGoals", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughObjectives51: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughObjectives51",
    ends={
        Property(name="Objective", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesGoals", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesGoal53: BinaryAssociation = BinaryAssociation(
    name="decomposesGoal53",
    ends={
        Property(name="Goal54", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByGoals", type=contentfwk_Goal, multiplicity=Multiplicity(0, 1))
    }
)
interactsWithFunctions87: BinaryAssociation = BinaryAssociation(
    name="interactsWithFunctions87",
    ends={
        Property(name="Function88", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
performsTaskInRoles89: BinaryAssociation = BinaryAssociation(
    name="performsTaskInRoles89",
    ends={
        Property(name="Role", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isAssumedByActors", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses90: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses90",
    ends={
        Property(name="Process91", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesActors", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices92: BinaryAssociation = BinaryAssociation(
    name="consumesServices92",
    ends={
        Property(name="Service93", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isProvidedToActors", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents94: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents94",
    ends={
        Property(name="Event", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents95: BinaryAssociation = BinaryAssociation(
    name="generatesEvents95",
    ends={
        Property(name="Event96", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation97: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation97",
    ends={
        Property(name="Location99", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors98", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
performsFunctions100: BinaryAssociation = BinaryAssociation(
    name="performsFunctions100",
    ends={
        Property(name="Function101", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isPerformedByActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesActor103: BinaryAssociation = BinaryAssociation(
    name="decomposesActor103",
    ends={
        Property(name="Actor104", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByActors", type=contentfwk_Actor, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByActors106: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByActors106",
    ends={
        Property(name="Actor107", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesActor", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAssumedByActors108: BinaryAssociation = BinaryAssociation(
    name="isAssumedByActors108",
    ends={
        Property(name="Actor109", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="performsTaskInRoles", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
suppliesDataEntities82: BinaryAssociation = BinaryAssociation(
    name="suppliesDataEntities82",
    ends={
        Property(name="DataEntity", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesDataEntities83: BinaryAssociation = BinaryAssociation(
    name="consumesDataEntities83",
    ends={
        Property(name="DataEntity84", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isConsumedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
belongsToOrganizationUnit85: BinaryAssociation = BinaryAssociation(
    name="belongsToOrganizationUnit85",
    ends={
        Property(name="OrganizationUnit86", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
accessesFunctions110: BinaryAssociation = BinaryAssociation(
    name="accessesFunctions110",
    ends={
        Property(name="Function111", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="canBeAccessedByRoles", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesRole113: BinaryAssociation = BinaryAssociation(
    name="decomposesRole113",
    ends={
        Property(name="Role114", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByRoles", type=contentfwk_Role, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByRoles116: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByRoles116",
    ends={
        Property(name="Role117", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesRole", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
isSuppliedByActors118: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByActors118",
    ends={
        Property(name="Actor119", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesDataEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isConsumedByActors120: BinaryAssociation = BinaryAssociation(
    name="isConsumedByActors120",
    ends={
        Property(name="Actor121", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesDataEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAccessedByServices122: BinaryAssociation = BinaryAssociation(
    name="isAccessedByServices122",
    ends={
        Property(name="Service124", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesDataEntities123", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isUpdatedThroughServices125: BinaryAssociation = BinaryAssociation(
    name="isUpdatedThroughServices125",
    ends={
        Property(name="Service126", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providesDataEntities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
residesWithinLogicalDataComponent127: BinaryAssociation = BinaryAssociation(
    name="residesWithinLogicalDataComponent127",
    ends={
        Property(name="LogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatesDataEntities", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
isProcessesByLogicalApplicationComponents128: BinaryAssociation = BinaryAssociation(
    name="isProcessesByLogicalApplicationComponents128",
    ends={
        Property(name="LogicalApplicationComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesOnDataEntities", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesDataEntity130: BinaryAssociation = BinaryAssociation(
    name="decomposesDataEntity130",
    ends={
        Property(name="contentfwk_DataEntity131", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity129", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 1))
    }
)
relatesToDataEntities133: BinaryAssociation = BinaryAssociation(
    name="relatesToDataEntities133",
    ends={
        Property(name="contentfwk_DataEntity134", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity132", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByDataEntities136: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByDataEntities136",
    ends={
        Property(name="contentfwk_DataEntity137", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity135", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith144: BinaryAssociation = BinaryAssociation(
    name="communicatesWith144",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent143", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999)),
        Property(name="contentfwk_LogicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1))
    }
)
decomposesLogicalApplicationComponent146: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalApplicationComponent146",
    ends={
        Property(name="LogicalApplicationComponent147", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByLogicalApplicationComponents", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByLogicalApplicationComponents149: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByLogicalApplicationComponents149",
    ends={
        Property(name="LogicalApplicationComponent150", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesLogicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isPerformedByActors151: BinaryAssociation = BinaryAssociation(
    name="isPerformedByActors151",
    ends={
        Property(name="Actor152", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="performsFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedByOrganizationUnit153: BinaryAssociation = BinaryAssociation(
    name="isOwnedByOrganizationUnit153",
    ends={
        Property(name="OrganizationUnit154", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsFunctions", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
isBoundedByServices155: BinaryAssociation = BinaryAssociation(
    name="isBoundedByServices155",
    ends={
        Property(name="Service156", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="providesGovernedInterfaceToAccessFunctions", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses157: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses157",
    ends={
        Property(name="Process158", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses159: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses159",
    ends={
        Property(name="Process160", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
canBeAccessedByRoles161: BinaryAssociation = BinaryAssociation(
    name="canBeAccessedByRoles161",
    ends={
        Property(name="Role162", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesFunctions", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
supportsActors163: BinaryAssociation = BinaryAssociation(
    name="supportsActors163",
    ends={
        Property(name="Actor164", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="interactsWithFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunction166: BinaryAssociation = BinaryAssociation(
    name="decomposesFunction166",
    ends={
        Property(name="Function167", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByFunctions", type=contentfwk_Function, multiplicity=Multiplicity(0, 1))
    }
)
communicatesWithFunctions169: BinaryAssociation = BinaryAssociation(
    name="communicatesWithFunctions169",
    ends={
        Property(name="contentfwk_Function170", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function168", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByFunctions172: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByFunctions172",
    ends={
        Property(name="Function173", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesFunction", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
supportsObjective174: BinaryAssociation = BinaryAssociation(
    name="supportsObjective174",
    ends={
        Property(name="Objective175", type=contentfwk_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="isSupportedByBusinessService", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
implementsServices138: BinaryAssociation = BinaryAssociation(
    name="implementsServices138",
    ends={
        Property(name="Service139", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughLogicalApplicationComponent", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
operatesOnDataEntities140: BinaryAssociation = BinaryAssociation(
    name="operatesOnDataEntities140",
    ends={
        Property(name="DataEntity141", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isProcessesByLogicalApplicationComponents", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalApplicationComponents142: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalApplicationComponents142",
    ends={
        Property(name="PhysicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalApplicationComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
involvesOrganizationUnits180: BinaryAssociation = BinaryAssociation(
    name="involvesOrganizationUnits180",
    ends={
        Property(name="OrganizationUnit181", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesServices182: BinaryAssociation = BinaryAssociation(
    name="orchestratesServices182",
    ends={
        Property(name="Service184", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses183", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices185: BinaryAssociation = BinaryAssociation(
    name="decomposesServices185",
    ends={
        Property(name="Service187", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses186", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
involvesActors188: BinaryAssociation = BinaryAssociation(
    name="involvesActors188",
    ends={
        Property(name="Actor190", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses189", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGuidedByControls191: BinaryAssociation = BinaryAssociation(
    name="isGuidedByControls191",
    ends={
        Property(name="Control", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ensuresCorrectOperationOfProcesses", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents192: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents192",
    ends={
        Property(name="Event193", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents194: BinaryAssociation = BinaryAssociation(
    name="generatesEvents194",
    ends={
        Property(name="Event195", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts196: BinaryAssociation = BinaryAssociation(
    name="producesProducts196",
    ends={
        Property(name="Product197", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByProcesses", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesProcess199: BinaryAssociation = BinaryAssociation(
    name="decomposesProcess199",
    ends={
        Property(name="Process200", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 1))
    }
)
precedesProcesses202: BinaryAssociation = BinaryAssociation(
    name="precedesProcesses202",
    ends={
        Property(name="Process203", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="followsProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
followsProcesses205: BinaryAssociation = BinaryAssociation(
    name="followsProcesses205",
    ends={
        Property(name="Process206", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="precedesProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByProcesses208: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByProcesses208",
    ends={
        Property(name="Process209", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesProcess", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isSuppliedByLogicalTechnologyComponents210: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByLogicalTechnologyComponents210",
    ends={
        Property(name="LogicalTechnologyComponent", type=contentfwk_PlatformService, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesPlatformServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesFunctions176: BinaryAssociation = BinaryAssociation(
    name="orchestratesFunctions176",
    ends={
        Property(name="Function177", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunctions178: BinaryAssociation = BinaryAssociation(
    name="decomposesFunctions178",
    ends={
        Property(name="Function179", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalTechnologyComponent219: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalTechnologyComponent219",
    ends={
        Property(name="PhysicalTechnologyComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByPhysicalTechnologyComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnPhysicalTechnologyComponents221: BinaryAssociation = BinaryAssociation(
    name="isDependentOnPhysicalTechnologyComponents221",
    ends={
        Property(name="PhysicalTechnologyComponent222", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRequiredByPhysicalTechnologyComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRequiredByPhysicalTechnologyComponent224: BinaryAssociation = BinaryAssociation(
    name="isRequiredByPhysicalTechnologyComponent224",
    ends={
        Property(name="PhysicalTechnologyComponent225", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDependentOnPhysicalTechnologyComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByPhysicalTechnologyComponents227: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByPhysicalTechnologyComponents227",
    ends={
        Property(name="PhysicalTechnologyComponent228", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesPhysicalTechnologyComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByOrganizationUnits229: BinaryAssociation = BinaryAssociation(
    name="isProducedByOrganizationUnits229",
    ends={
        Property(name="OrganizationUnit230", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByProcesses231: BinaryAssociation = BinaryAssociation(
    name="isProducedByProcesses231",
    ends={
        Property(name="Process233", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts232", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForObjectives234: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForObjectives234",
    ends={
        Property(name="Objective235", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForServices236: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForServices236",
    ends={
        Property(name="Service238", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures237", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesMeasure240: BinaryAssociation = BinaryAssociation(
    name="decomposesMeasure240",
    ends={
        Property(name="Measure241", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByMeasures", type=contentfwk_Measure, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByMeasures243: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByMeasures243",
    ends={
        Property(name="Measure244", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesMeasure", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToServices245: BinaryAssociation = BinaryAssociation(
    name="appliesToServices245",
    ends={
        Property(name="Service246", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsServiceQualities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToContracts247: BinaryAssociation = BinaryAssociation(
    name="appliesToContracts247",
    ends={
        Property(name="Contract", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
realizesPhysicalApplicationComponents211: BinaryAssociation = BinaryAssociation(
    name="realizesPhysicalApplicationComponents211",
    ends={
        Property(name="PhysicalApplicationComponent212", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByPhysicalTechnologyComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalTechnologyComponents213: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalTechnologyComponents213",
    ends={
        Property(name="LogicalTechnologyComponent215", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByPhysicalTechnologyComponents214", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation216: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation216",
    ends={
        Property(name="Location217", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalTechnologyComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByServices251: BinaryAssociation = BinaryAssociation(
    name="isResolvedByServices251",
    ends={
        Property(name="Service252", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByProcesses253: BinaryAssociation = BinaryAssociation(
    name="isResolvedByProcesses253",
    ends={
        Property(name="Process255", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents254", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByProcesses256: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByProcesses256",
    ends={
        Property(name="Process257", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByActors258: BinaryAssociation = BinaryAssociation(
    name="isResolvedByActors258",
    ends={
        Property(name="Actor260", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents259", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByActors261: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByActors261",
    ends={
        Property(name="Actor263", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents262", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
governsAndMeasuresBusinessServices248: BinaryAssociation = BinaryAssociation(
    name="governsAndMeasuresBusinessServices248",
    ends={
        Property(name="Service249", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="isGovernedAndMeasuredByContracts", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
meetsServiceQuality250: BinaryAssociation = BinaryAssociation(
    name="meetsServiceQuality250",
    ends={
        Property(name="ServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToContracts", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors271: BinaryAssociation = BinaryAssociation(
    name="containsActors271",
    ends={
        Property(name="Actor272", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
containsOrganizationUnits273: BinaryAssociation = BinaryAssociation(
    name="containsOrganizationUnits273",
    ends={
        Property(name="OrganizationUnit275", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation274", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalDataComponents276: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalDataComponents276",
    ends={
        Property(name="PhysicalDataComponent", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHotedInLocation", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalApplicationComponents277: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalApplicationComponents277",
    ends={
        Property(name="PhysicalApplicationComponent278", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalTechnologyComponents279: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalTechnologyComponents279",
    ends={
        Property(name="PhysicalTechnologyComponent281", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation280", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLocation283: BinaryAssociation = BinaryAssociation(
    name="decomposesLocation283",
    ends={
        Property(name="Location284", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByLocations", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByLocations286: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByLocations286",
    ends={
        Property(name="Location287", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesLocation", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
isDeliveredBy288: BinaryAssociation = BinaryAssociation(
    name="isDeliveredBy288",
    ends={
        Property(name="WorkPackage", type=contentfwk_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="deliversCapabilities", type=contentfwk_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
ensuresCorrectOperationOfProcesses264: BinaryAssociation = BinaryAssociation(
    name="ensuresCorrectOperationOfProcesses264",
    ends={
        Property(name="Process265", type=contentfwk_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="isGuidedByControls", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
delegates267: BinaryAssociation = BinaryAssociation(
    name="delegates267",
    ends={
        Property(name="Element", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="isDelegatedBy", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isDelegatedBy269: BinaryAssociation = BinaryAssociation(
    name="isDelegatedBy269",
    ends={
        Property(name="Element270", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
deliversCapabilities289: BinaryAssociation = BinaryAssociation(
    name="deliversCapabilities289",
    ends={
        Property(name="Capability", type=contentfwk_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="isDeliveredBy", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesDataEntities290: BinaryAssociation = BinaryAssociation(
    name="encapsulatesDataEntities290",
    ends={
        Property(name="DataEntity291", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="residesWithinLogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalDataComponents292: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalDataComponents292",
    ends={
        Property(name="PhysicalDataComponent293", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalDataComponents", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
logicalApplicationComponents306: BinaryAssociation = BinaryAssociation(
    name="logicalApplicationComponents306",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent307", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalApplicationComponents308: BinaryAssociation = BinaryAssociation(
    name="physicalApplicationComponents308",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture309", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informationSystemServices310: BinaryAssociation = BinaryAssociation(
    name="informationSystemServices310",
    ends={
        Property(name="contentfwk_InformationSystemService", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture311", type=contentfwk_InformationSystemService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsLogicalApplicationComponents312: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalApplicationComponents312",
    ends={
        Property(name="LogicalApplicationComponent313", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalApplicationComponents", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation314: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation314",
    ends={
        Property(name="Location315", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalApplicationComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith317: BinaryAssociation = BinaryAssociation(
    name="communicatesWith317",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent318", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent316", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalDataComponents294: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalDataComponents294",
    ends={
        Property(name="LogicalDataComponent295", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalDataComponents", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHotedInLocation296: BinaryAssociation = BinaryAssociation(
    name="isHotedInLocation296",
    ends={
        Property(name="Location297", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalDataComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
decomposesPhysicalDataComponent299: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalDataComponent299",
    ends={
        Property(name="PhysicalDataComponent300", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByPhysicalDataComponents", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatesPhysicalApplicationComponents301: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalApplicationComponents301",
    ends={
        Property(name="PhysicalApplicationComponent302", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatesPhysicalDataComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByPhysicalDataComponents304: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByPhysicalDataComponents304",
    ends={
        Property(name="PhysicalDataComponent305", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesPhysicalDataComponent", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents321: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents321",
    ends={
        Property(name="PhysicalTechnologyComponent322", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesPhysicalApplicationComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalApplicationComponent324: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalApplicationComponent324",
    ends={
        Property(name="PhysicalApplicationComponent325", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByPhysicalApplicationComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDecomposedByPhysicalApplicationComponents327: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByPhysicalApplicationComponents327",
    ends={
        Property(name="PhysicalApplicationComponent328", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesPhysicalApplicationComponent", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
providesPlatformForServices329: BinaryAssociation = BinaryAssociation(
    name="providesPlatformForServices329",
    ends={
        Property(name="Service330", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isImplementedOnLogicalTechnologyComponents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
suppliesPlatformServices331: BinaryAssociation = BinaryAssociation(
    name="suppliesPlatformServices331",
    ends={
        Property(name="PlatformService", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByLogicalTechnologyComponents", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents332: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents332",
    ends={
        Property(name="PhysicalTechnologyComponent333", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalTechnologyComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalTechnologyComponent335: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalTechnologyComponent335",
    ends={
        Property(name="LogicalTechnologyComponent336", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByLogicalTechnologyComponents", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnLogicalTechnologyComponents338: BinaryAssociation = BinaryAssociation(
    name="isDependentOnLogicalTechnologyComponents338",
    ends={
        Property(name="LogicalTechnologyComponent339", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRequiredByLogicalTechnologyComponents", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalTechnologyComponent340: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalTechnologyComponent340",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent342", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent341", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRequiredByLogicalTechnologyComponents344: BinaryAssociation = BinaryAssociation(
    name="isRequiredByLogicalTechnologyComponents344",
    ends={
        Property(name="LogicalTechnologyComponent345", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isDependentOnLogicalTechnologyComponents", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesPhysicalDataComponents319: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalDataComponents319",
    ends={
        Property(name="PhysicalDataComponent320", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatesPhysicalApplicationComponents", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isProvidedToActors352: BinaryAssociation = BinaryAssociation(
    name="isProvidedToActors352",
    ends={
        Property(name="Actor353", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesServices", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
providesGovernedInterfaceToAccessFunctions354: BinaryAssociation = BinaryAssociation(
    name="providesGovernedInterfaceToAccessFunctions354",
    ends={
        Property(name="Function355", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isBoundedByServices", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
providesDataEntities356: BinaryAssociation = BinaryAssociation(
    name="providesDataEntities356",
    ends={
        Property(name="DataEntity357", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isUpdatedThroughServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesDataEntities358: BinaryAssociation = BinaryAssociation(
    name="consumesDataEntities358",
    ends={
        Property(name="DataEntity359", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isAccessedByServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isGovernedAndMeasuredByContracts360: BinaryAssociation = BinaryAssociation(
    name="isGovernedAndMeasuredByContracts360",
    ends={
        Property(name="Contract361", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="governsAndMeasuresBusinessServices", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents362: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents362",
    ends={
        Property(name="Event363", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByServices", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByLogicalTechnologyComponents347: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByLogicalTechnologyComponents347",
    ends={
        Property(name="LogicalTechnologyComponent348", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesLogicalTechnologyComponent", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
capabilities349: BinaryAssociation = BinaryAssociation(
    name="capabilities349",
    ends={
        Property(name="contentfwk_Capability", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strategicElements350: BinaryAssociation = BinaryAssociation(
    name="strategicElements350",
    ends={
        Property(name="contentfwk_StrategicElement", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture351", type=contentfwk_StrategicElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isTrackedAgainstMeasures370: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures370",
    ends={
        Property(name="Measure371", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForServices", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses372: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses372",
    ends={
        Property(name="Process373", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses374: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses374",
    ends={
        Property(name="Process375", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
meetsServiceQualities376: BinaryAssociation = BinaryAssociation(
    name="meetsServiceQualities376",
    ends={
        Property(name="ServiceQuality377", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToServices", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices379: BinaryAssociation = BinaryAssociation(
    name="consumesServices379",
    ends={
        Property(name="contentfwk_Service", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service378", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices381: BinaryAssociation = BinaryAssociation(
    name="decomposesServices381",
    ends={
        Property(name="Service382", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isDecomposedByServices", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isDecomposedByServices384: BinaryAssociation = BinaryAssociation(
    name="isDecomposedByServices384",
    ends={
        Property(name="Service386", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesServices385", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isImplementedOnLogicalTechnologyComponents364: BinaryAssociation = BinaryAssociation(
    name="isImplementedOnLogicalTechnologyComponents364",
    ends={
        Property(name="LogicalTechnologyComponent365", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="providesPlatformForServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughLogicalApplicationComponent366: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughLogicalApplicationComponent366",
    ends={
        Property(name="LogicalApplicationComponent367", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="implementsServices", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedAndGovernedByOrganizationUnits368: BinaryAssociation = BinaryAssociation(
    name="isOwnedAndGovernedByOrganizationUnits368",
    ends={
        Property(name="OrganizationUnit369", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsAndGovernsServices", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_contentfwk_BusinessArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_BusinessArchitecture)
gen_contentfwk_DataArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_DataArchitecture)
gen_contentfwk_TechnologyArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_TechnologyArchitecture)
gen_contentfwk_Driver_Element = Generalization(general=Element, specific=contentfwk_Driver)
gen_contentfwk_Objective_Element = Generalization(general=Element, specific=contentfwk_Objective)
gen_contentfwk_OrganizationUnit_Element = Generalization(general=Element, specific=contentfwk_OrganizationUnit)
gen_contentfwk_Goal_Element = Generalization(general=Element, specific=contentfwk_Goal)
gen_contentfwk_Role_Element = Generalization(general=Element, specific=contentfwk_Role)
gen_contentfwk_Actor_Element = Generalization(general=Element, specific=contentfwk_Actor)
gen_contentfwk_DataEntity_Element = Generalization(general=Element, specific=contentfwk_DataEntity)
gen_contentfwk_Function_Element = Generalization(general=Element, specific=contentfwk_Function)
gen_contentfwk_Function_Standard = Generalization(general=Standard, specific=contentfwk_Function)
gen_contentfwk_BusinessService_Element = Generalization(general=Element, specific=contentfwk_BusinessService)
gen_contentfwk_BusinessService_Service = Generalization(general=Service, specific=contentfwk_BusinessService)
gen_contentfwk_LogicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_LogicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_PlatformService_Element = Generalization(general=Element, specific=contentfwk_PlatformService)
gen_contentfwk_Process_Element = Generalization(general=Element, specific=contentfwk_Process)
gen_contentfwk_Process_Standard = Generalization(general=Standard, specific=contentfwk_Process)
gen_contentfwk_Product_Element = Generalization(general=Element, specific=contentfwk_Product)
gen_contentfwk_Measure_Element = Generalization(general=Element, specific=contentfwk_Measure)
gen_contentfwk_ServiceQuality_Element = Generalization(general=Element, specific=contentfwk_ServiceQuality)
gen_contentfwk_Contract_Element = Generalization(general=Element, specific=contentfwk_Contract)
gen_contentfwk_PhysicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_Event_Element = Generalization(general=Element, specific=contentfwk_Event)
gen_contentfwk_Control_Element = Generalization(general=Element, specific=contentfwk_Control)
gen_contentfwk_Location_Element = Generalization(general=Element, specific=contentfwk_Location)
gen_contentfwk_Capability_Element = Generalization(general=Element, specific=contentfwk_Capability)
gen_contentfwk_Constraint_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Constraint)
gen_contentfwk_Assumption_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Assumption)
gen_contentfwk_Requirement_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Requirement)
gen_contentfwk_Gap_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Gap)
gen_contentfwk_WorkPackage_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_WorkPackage)
gen_contentfwk_LogicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_LogicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_PhysicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_PhysicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_StrategicElement_Element = Generalization(general=Element, specific=contentfwk_StrategicElement)
gen_contentfwk_Principle_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Principle)
gen_contentfwk_ApplicationArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_ApplicationArchitecture)
gen_contentfwk_PhysicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_LogicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_Service_Standard = Generalization(general=Standard, specific=contentfwk_Service)
gen_contentfwk_StrategicArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_StrategicArchitecture)
gen_contentfwk_ApplicationComponent_Standard = Generalization(general=Standard, specific=contentfwk_ApplicationComponent)
gen_contentfwk_InformationSystemService_Service = Generalization(general=Service, specific=contentfwk_InformationSystemService)
gen_contentfwk_InformationSystemService_Element = Generalization(general=Element, specific=contentfwk_InformationSystemService)
gen_contentfwk_DataComponent_Standard = Generalization(general=Standard, specific=contentfwk_DataComponent)
gen_contentfwk_TechnologyComponent_Standard = Generalization(general=Standard, specific=contentfwk_TechnologyComponent)

# Domain Model
domain_model = DomainModel(
    name="contentfwk",
    types={contentfwk_Architecture, contentfwk_BusinessArchitecture, Architecture, contentfwk_Driver, contentfwk_Goal, contentfwk_Objective, contentfwk_OrganizationUnit, contentfwk_Actor, contentfwk_Role, contentfwk_Function, contentfwk_BusinessService, contentfwk_Process, contentfwk_EnterpriseArchitecture, contentfwk_Measure, contentfwk_ServiceQuality, contentfwk_DataArchitecture, contentfwk_DataEntity, contentfwk_LogicalDataComponent, contentfwk_PhysicalDataComponent, contentfwk_TechnologyArchitecture, contentfwk_PlatformService, contentfwk_PhysicalTechnologyComponent, contentfwk_LogicalTechnologyComponent, Element, contentfwk_Control, contentfwk_Event, contentfwk_Location, contentfwk_Product, contentfwk_Contract, contentfwk_Service, contentfwk_LogicalApplicationComponent, Standard, Service, ApplicationComponent, contentfwk_PhysicalApplicationComponent, TechnologyComponent, contentfwk_Capability, contentfwk_WorkPackage, contentfwk_Element, contentfwk_Constraint, contentfwk_Assumption, contentfwk_Requirement, contentfwk_Gap, DataComponent, contentfwk_StrategicElement, contentfwk_Principle, StrategicElement, contentfwk_ApplicationArchitecture, contentfwk_InformationSystemService, contentfwk_Standard, contentfwk_StrategicArchitecture, contentfwk_ApplicationComponent, contentfwk_DataComponent, contentfwk_TechnologyComponent, StandardsClass, PrincipleCategory, LifeCycleStatus, DataEntityCategory, WorkPackageCategory},
    associations={architectures0, drivers1, goals2, objectives4, units6, actors8, roles10, functions12, services14, processes16, measures28, servicesQuality30, entities32, logicalComponents33, physicalComponents35, platformServices37, physicalComponents38, logicalComponents40, createsGoals42, motivatesOrganizationUnits43, decomposesDriver45, controls18, events20, locations22, products24, contracts26, isDecomposedByGoals56, realizesGoals58, isTrackedAgainstMeasures60, decomposesObjective62, isSupportedByBusinessService64, isDecomposedByObjectives66, ownsAndGovernsServices68, containsActors69, ownsFunctions70, participatesInProcesses71, isMotivatedByDrivers72, producesProducts74, operatesInLocation75, decomposesOrganizationUnit77, isDecomposedByOrganizationUnits80, isDecomposedByDrivers47, addressesDrivers49, isRealizedThroughObjectives51, decomposesGoal53, interactsWithFunctions87, performsTaskInRoles89, participatesInProcesses90, consumesServices92, resolvesEvents94, generatesEvents95, operatesInLocation97, performsFunctions100, decomposesActor103, isDecomposedByActors106, isAssumedByActors108, suppliesDataEntities82, consumesDataEntities83, belongsToOrganizationUnit85, accessesFunctions110, decomposesRole113, isDecomposedByRoles116, isSuppliedByActors118, isConsumedByActors120, isAccessedByServices122, isUpdatedThroughServices125, residesWithinLogicalDataComponent127, isProcessesByLogicalApplicationComponents128, decomposesDataEntity130, relatesToDataEntities133, isDecomposedByDataEntities136, communicatesWith144, decomposesLogicalApplicationComponent146, isDecomposedByLogicalApplicationComponents149, isPerformedByActors151, isOwnedByOrganizationUnit153, isBoundedByServices155, supportsProcesses157, isRealizedByProcesses159, canBeAccessedByRoles161, supportsActors163, decomposesFunction166, communicatesWithFunctions169, isDecomposedByFunctions172, supportsObjective174, implementsServices138, operatesOnDataEntities140, isExtendedByPhysicalApplicationComponents142, involvesOrganizationUnits180, orchestratesServices182, decomposesServices185, involvesActors188, isGuidedByControls191, resolvesEvents192, generatesEvents194, producesProducts196, decomposesProcess199, precedesProcesses202, followsProcesses205, isDecomposedByProcesses208, isSuppliedByLogicalTechnologyComponents210, orchestratesFunctions176, decomposesFunctions178, decomposesPhysicalTechnologyComponent219, isDependentOnPhysicalTechnologyComponents221, isRequiredByPhysicalTechnologyComponent224, isDecomposedByPhysicalTechnologyComponents227, isProducedByOrganizationUnits229, isProducedByProcesses231, setsPerformanceCriteriaForObjectives234, setsPerformanceCriteriaForServices236, decomposesMeasure240, isDecomposedByMeasures243, appliesToServices245, appliesToContracts247, realizesPhysicalApplicationComponents211, extendsLogicalTechnologyComponents213, isHostedInLocation216, isResolvedByServices251, isResolvedByProcesses253, isGeneratedByProcesses256, isResolvedByActors258, isGeneratedByActors261, governsAndMeasuresBusinessServices248, meetsServiceQuality250, containsActors271, containsOrganizationUnits273, containsPhysicalDataComponents276, containsPhysicalApplicationComponents277, containsPhysicalTechnologyComponents279, decomposesLocation283, isDecomposedByLocations286, isDeliveredBy288, ensuresCorrectOperationOfProcesses264, delegates267, isDelegatedBy269, deliversCapabilities289, encapsulatesDataEntities290, isExtendedByPhysicalDataComponents292, logicalApplicationComponents306, physicalApplicationComponents308, informationSystemServices310, extendsLogicalApplicationComponents312, isHostedInLocation314, communicatesWith317, extendsLogicalDataComponents294, isHotedInLocation296, decomposesPhysicalDataComponent299, encapsulatesPhysicalApplicationComponents301, isDecomposedByPhysicalDataComponents304, isRealizedByPhysicalTechnologyComponents321, decomposesPhysicalApplicationComponent324, isDecomposedByPhysicalApplicationComponents327, providesPlatformForServices329, suppliesPlatformServices331, isRealizedByPhysicalTechnologyComponents332, decomposesLogicalTechnologyComponent335, isDependentOnLogicalTechnologyComponents338, isExtendedByPhysicalTechnologyComponent340, isRequiredByLogicalTechnologyComponents344, encapsulatesPhysicalDataComponents319, isProvidedToActors352, providesGovernedInterfaceToAccessFunctions354, providesDataEntities356, consumesDataEntities358, isGovernedAndMeasuredByContracts360, resolvesEvents362, isDecomposedByLogicalTechnologyComponents347, capabilities349, strategicElements350, isTrackedAgainstMeasures370, supportsProcesses372, isRealizedByProcesses374, meetsServiceQualities376, consumesServices379, decomposesServices381, isDecomposedByServices384, isImplementedOnLogicalTechnologyComponents364, isRealizedThroughLogicalApplicationComponent366, isOwnedAndGovernedByOrganizationUnits368},
    generalizations={gen_contentfwk_BusinessArchitecture_Architecture, gen_contentfwk_DataArchitecture_Architecture, gen_contentfwk_TechnologyArchitecture_Architecture, gen_contentfwk_Driver_Element, gen_contentfwk_Objective_Element, gen_contentfwk_OrganizationUnit_Element, gen_contentfwk_Goal_Element, gen_contentfwk_Role_Element, gen_contentfwk_Actor_Element, gen_contentfwk_DataEntity_Element, gen_contentfwk_Function_Element, gen_contentfwk_Function_Standard, gen_contentfwk_BusinessService_Element, gen_contentfwk_BusinessService_Service, gen_contentfwk_LogicalApplicationComponent_Element, gen_contentfwk_LogicalApplicationComponent_ApplicationComponent, gen_contentfwk_PlatformService_Element, gen_contentfwk_Process_Element, gen_contentfwk_Process_Standard, gen_contentfwk_Product_Element, gen_contentfwk_Measure_Element, gen_contentfwk_ServiceQuality_Element, gen_contentfwk_Contract_Element, gen_contentfwk_PhysicalTechnologyComponent_Element, gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent, gen_contentfwk_Event_Element, gen_contentfwk_Control_Element, gen_contentfwk_Location_Element, gen_contentfwk_Capability_Element, gen_contentfwk_Constraint_StrategicElement, gen_contentfwk_Assumption_StrategicElement, gen_contentfwk_Requirement_StrategicElement, gen_contentfwk_Gap_StrategicElement, gen_contentfwk_WorkPackage_StrategicElement, gen_contentfwk_LogicalDataComponent_Element, gen_contentfwk_LogicalDataComponent_DataComponent, gen_contentfwk_PhysicalDataComponent_Element, gen_contentfwk_PhysicalDataComponent_DataComponent, gen_contentfwk_StrategicElement_Element, gen_contentfwk_Principle_StrategicElement, gen_contentfwk_ApplicationArchitecture_Architecture, gen_contentfwk_PhysicalApplicationComponent_Element, gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent, gen_contentfwk_LogicalTechnologyComponent_Element, gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent, gen_contentfwk_Service_Standard, gen_contentfwk_StrategicArchitecture_Architecture, gen_contentfwk_ApplicationComponent_Standard, gen_contentfwk_InformationSystemService_Service, gen_contentfwk_InformationSystemService_Element, gen_contentfwk_DataComponent_Standard, gen_contentfwk_TechnologyComponent_Standard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)