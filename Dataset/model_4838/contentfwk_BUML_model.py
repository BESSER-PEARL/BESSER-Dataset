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
contentfwk_Container = Class(name="contentfwk::Container")
contentfwk_Label = Class(name="contentfwk::Label")
contentfwk_BusinessArchitecture = Class(name="contentfwk::BusinessArchitecture")
Architecture = Class(name="Architecture")
contentfwk_Driver = Class(name="contentfwk::Driver")
contentfwk_Goal = Class(name="contentfwk::Goal")
contentfwk_EnterpriseArchitecture = Class(name="contentfwk::EnterpriseArchitecture")
contentfwk_Architecture = Class(name="contentfwk::Architecture", is_abstract=True)
contentfwk_Control = Class(name="contentfwk::Control")
contentfwk_Event = Class(name="contentfwk::Event")
contentfwk_Location = Class(name="contentfwk::Location")
contentfwk_Product = Class(name="contentfwk::Product")
contentfwk_Contract = Class(name="contentfwk::Contract")
contentfwk_Measure = Class(name="contentfwk::Measure")
contentfwk_Objective = Class(name="contentfwk::Objective")
contentfwk_OrganizationUnit = Class(name="contentfwk::OrganizationUnit")
contentfwk_Actor = Class(name="contentfwk::Actor")
contentfwk_Role = Class(name="contentfwk::Role")
contentfwk_Function = Class(name="contentfwk::Function")
contentfwk_BusinessService = Class(name="contentfwk::BusinessService")
contentfwk_Process = Class(name="contentfwk::Process")
contentfwk_PhysicalTechnologyComponent = Class(name="contentfwk::PhysicalTechnologyComponent")
contentfwk_LogicalTechnologyComponent = Class(name="contentfwk::LogicalTechnologyComponent")
Element = Class(name="Element")
contentfwk_ServiceQuality = Class(name="contentfwk::ServiceQuality")
contentfwk_DataArchitecture = Class(name="contentfwk::DataArchitecture")
contentfwk_DataEntity = Class(name="contentfwk::DataEntity")
contentfwk_LogicalDataComponent = Class(name="contentfwk::LogicalDataComponent")
contentfwk_PhysicalDataComponent = Class(name="contentfwk::PhysicalDataComponent")
contentfwk_TechnologyArchitecture = Class(name="contentfwk::TechnologyArchitecture")
contentfwk_PlatformService = Class(name="contentfwk::PlatformService")
contentfwk_Service = Class(name="contentfwk::Service", is_abstract=True)
contentfwk_LogicalApplicationComponent = Class(name="contentfwk::LogicalApplicationComponent")
contentfwk_PhysicalApplicationComponent = Class(name="contentfwk::PhysicalApplicationComponent")
ApplicationComponent = Class(name="ApplicationComponent")
Standard = Class(name="Standard")
Service = Class(name="Service")
TechnologyComponent = Class(name="TechnologyComponent")
contentfwk_Element = Class(name="contentfwk::Element")
contentfwk_Capability = Class(name="contentfwk::Capability")
contentfwk_WorkPackage = Class(name="contentfwk::WorkPackage")
contentfwk_StrategicElement = Class(name="contentfwk::StrategicElement", is_abstract=True)
contentfwk_Principle = Class(name="contentfwk::Principle")
StrategicElement = Class(name="StrategicElement")
contentfwk_Constraint = Class(name="contentfwk::Constraint")
contentfwk_Assumption = Class(name="contentfwk::Assumption")
contentfwk_Requirement = Class(name="contentfwk::Requirement")
contentfwk_Gap = Class(name="contentfwk::Gap")
DataComponent = Class(name="DataComponent")
contentfwk_ApplicationArchitecture = Class(name="contentfwk::ApplicationArchitecture")
contentfwk_InformationSystemService = Class(name="contentfwk::InformationSystemService")
contentfwk_StrategicArchitecture = Class(name="contentfwk::StrategicArchitecture")
contentfwk_Standard = Class(name="contentfwk::Standard", is_abstract=True)
contentfwk_ApplicationComponent = Class(name="contentfwk::ApplicationComponent", is_abstract=True)
contentfwk_DataComponent = Class(name="contentfwk::DataComponent", is_abstract=True)
contentfwk_TechnologyComponent = Class(name="contentfwk::TechnologyComponent", is_abstract=True)

# contentfwk_Container class attributes and methods
contentfwk_Container_id: Property = Property(name="id", type=StringType)
contentfwk_Container_description: Property = Property(name="description", type=StringType)
contentfwk_Container_name: Property = Property(name="name", type=StringType)
contentfwk_Container.attributes={contentfwk_Container_name, contentfwk_Container_id, contentfwk_Container_description}

# contentfwk_Label class attributes and methods
contentfwk_Label_name: Property = Property(name="name", type=StringType)
contentfwk_Label_id: Property = Property(name="id", type=StringType)
contentfwk_Label_description: Property = Property(name="description", type=StringType)
contentfwk_Label.attributes={contentfwk_Label_name, contentfwk_Label_description, contentfwk_Label_id}

# contentfwk_BusinessArchitecture class attributes and methods

# Architecture class attributes and methods

# contentfwk_Driver class attributes and methods

# contentfwk_Goal class attributes and methods

# contentfwk_EnterpriseArchitecture class attributes and methods

# contentfwk_Architecture class attributes and methods

# contentfwk_Control class attributes and methods

# contentfwk_Event class attributes and methods

# contentfwk_Location class attributes and methods

# contentfwk_Product class attributes and methods

# contentfwk_Contract class attributes and methods
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
contentfwk_Contract_behaviorCharacteristics: Property = Property(name="behaviorCharacteristics", type=StringType)
contentfwk_Contract_ServiceNameCaller: Property = Property(name="ServiceNameCaller", type=StringType)
contentfwk_Contract_ServiceNameCalled: Property = Property(name="ServiceNameCalled", type=StringType)
contentfwk_Contract_serviceQualityCharacteristics: Property = Property(name="serviceQualityCharacteristics", type=StringType)
contentfwk_Contract_availabilityQualityCharacteristics: Property = Property(name="availabilityQualityCharacteristics", type=StringType)
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
contentfwk_Contract_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
contentfwk_Contract.attributes={contentfwk_Contract_peakProfileLongTerm, contentfwk_Contract_contractControlRequirements, contentfwk_Contract_serviceabilityCharacteristics, contentfwk_Contract_credibilityCharacteristics, contentfwk_Contract_securityCharacteristics, contentfwk_Contract_growthPeriod, contentfwk_Contract_locatabilityCharacteristics, contentfwk_Contract_internationalizationCharacteristics, contentfwk_Contract_portabilityCharacteristics, contentfwk_Contract_integrityCharacteristics, contentfwk_Contract_scalabilityCharacteristics, contentfwk_Contract_extensibilityCharacteristics, contentfwk_Contract_interoperabilityCharacteristics, contentfwk_Contract_resultControlRequirements, contentfwk_Contract_growth, contentfwk_Contract_peakProfileShortTerm, contentfwk_Contract_capacityCharacteristics, contentfwk_Contract_serviceQualityCharacteristics, contentfwk_Contract_manageabilityCharacteristics, contentfwk_Contract_throughput, contentfwk_Contract_privacyCharacteristics, contentfwk_Contract_reliabilityCharacteristics, contentfwk_Contract_qualityOfInformationRequired, contentfwk_Contract_throughputPeriod, contentfwk_Contract_localizationCharacteristics, contentfwk_Contract_behaviorCharacteristics, contentfwk_Contract_availabilityQualityCharacteristics, contentfwk_Contract_ServiceNameCalled, contentfwk_Contract_servicesTimes, contentfwk_Contract_performanceCharacteristics, contentfwk_Contract_recoverabilityCharacteristics, contentfwk_Contract_ServiceNameCaller, contentfwk_Contract_responseCharacteristics}

# contentfwk_Measure class attributes and methods

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
contentfwk_Process_isAutomated: Property = Property(name="isAutomated", type=BooleanType)
contentfwk_Process_processVolumetrics: Property = Property(name="processVolumetrics", type=StringType)
contentfwk_Process_processCritiality: Property = Property(name="processCritiality", type=StringType)
contentfwk_Process.attributes={contentfwk_Process_isAutomated, contentfwk_Process_processCritiality, contentfwk_Process_processVolumetrics}

# contentfwk_PhysicalTechnologyComponent class attributes and methods
contentfwk_PhysicalTechnologyComponent_productName: Property = Property(name="productName", type=StringType)
contentfwk_PhysicalTechnologyComponent_moduleName: Property = Property(name="moduleName", type=StringType)
contentfwk_PhysicalTechnologyComponent_vendor: Property = Property(name="vendor", type=StringType)
contentfwk_PhysicalTechnologyComponent_version: Property = Property(name="version", type=StringType)
contentfwk_PhysicalTechnologyComponent_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_PhysicalTechnologyComponent.attributes={contentfwk_PhysicalTechnologyComponent_productName, contentfwk_PhysicalTechnologyComponent_version, contentfwk_PhysicalTechnologyComponent_vendor, contentfwk_PhysicalTechnologyComponent_moduleName, contentfwk_PhysicalTechnologyComponent_categoryTRM}

# contentfwk_LogicalTechnologyComponent class attributes and methods
contentfwk_LogicalTechnologyComponent_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_LogicalTechnologyComponent.attributes={contentfwk_LogicalTechnologyComponent_categoryTRM}

# Element class attributes and methods

# contentfwk_ServiceQuality class attributes and methods

# contentfwk_DataArchitecture class attributes and methods

# contentfwk_DataEntity class attributes and methods
contentfwk_DataEntity_dataEntityCategory: Property = Property(name="dataEntityCategory", type=StringType)
contentfwk_DataEntity_privacyClassification: Property = Property(name="privacyClassification", type=StringType)
contentfwk_DataEntity_retentionClassification: Property = Property(name="retentionClassification", type=StringType)
contentfwk_DataEntity.attributes={contentfwk_DataEntity_privacyClassification, contentfwk_DataEntity_retentionClassification, contentfwk_DataEntity_dataEntityCategory}

# contentfwk_LogicalDataComponent class attributes and methods

# contentfwk_PhysicalDataComponent class attributes and methods

# contentfwk_TechnologyArchitecture class attributes and methods

# contentfwk_PlatformService class attributes and methods
contentfwk_PlatformService_categoryTRM: Property = Property(name="categoryTRM", type=StringType)
contentfwk_PlatformService.attributes={contentfwk_PlatformService_categoryTRM}

# contentfwk_Service class attributes and methods

# contentfwk_LogicalApplicationComponent class attributes and methods

# contentfwk_PhysicalApplicationComponent class attributes and methods
contentfwk_PhysicalApplicationComponent_lifeCycleStatus: Property = Property(name="lifeCycleStatus", type=StringType)
contentfwk_PhysicalApplicationComponent_initialLiveDate: Property = Property(name="initialLiveDate", type=DateType)
contentfwk_PhysicalApplicationComponent_dateOfLastRelease: Property = Property(name="dateOfLastRelease", type=DateType)
contentfwk_PhysicalApplicationComponent_dateOfNextRelease: Property = Property(name="dateOfNextRelease", type=DateType)
contentfwk_PhysicalApplicationComponent_retirementDate: Property = Property(name="retirementDate", type=DateType)
contentfwk_PhysicalApplicationComponent_availabilityQualityCharacteristics: Property = Property(name="availabilityQualityCharacteristics", type=StringType)
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
contentfwk_PhysicalApplicationComponent.attributes={contentfwk_PhysicalApplicationComponent_growthPeriod, contentfwk_PhysicalApplicationComponent_privacyCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileShortTerm, contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics, contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics, contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics, contentfwk_PhysicalApplicationComponent_portabilityCharacteristics, contentfwk_PhysicalApplicationComponent_lifeCycleStatus, contentfwk_PhysicalApplicationComponent_growth, contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics, contentfwk_PhysicalApplicationComponent_throughputPeriod, contentfwk_PhysicalApplicationComponent_retirementDate, contentfwk_PhysicalApplicationComponent_securityCharacteristics, contentfwk_PhysicalApplicationComponent_localizationCharacteristics, contentfwk_PhysicalApplicationComponent_availabilityQualityCharacteristics, contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics, contentfwk_PhysicalApplicationComponent_dateOfLastRelease, contentfwk_PhysicalApplicationComponent_dateOfNextRelease, contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileLongTerm, contentfwk_PhysicalApplicationComponent_initialLiveDate, contentfwk_PhysicalApplicationComponent_integrityCharacteristics, contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics, contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics, contentfwk_PhysicalApplicationComponent_performanceCharacteristics, contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics, contentfwk_PhysicalApplicationComponent_credibilityCharacteristics, contentfwk_PhysicalApplicationComponent_servicesTimes, contentfwk_PhysicalApplicationComponent_throughput, contentfwk_PhysicalApplicationComponent_capacityCharacteristics}

# ApplicationComponent class attributes and methods

# Standard class attributes and methods

# Service class attributes and methods

# TechnologyComponent class attributes and methods

# contentfwk_Element class attributes and methods
contentfwk_Element_name: Property = Property(name="name", type=StringType)
contentfwk_Element_description: Property = Property(name="description", type=StringType)
contentfwk_Element_sourceDescr: Property = Property(name="sourceDescr", type=StringType)
contentfwk_Element_ownerDescr: Property = Property(name="ownerDescr", type=StringType)
contentfwk_Element_ID: Property = Property(name="ID", type=StringType)
contentfwk_Element.attributes={contentfwk_Element_ID, contentfwk_Element_description, contentfwk_Element_sourceDescr, contentfwk_Element_ownerDescr, contentfwk_Element_name}

# contentfwk_Capability class attributes and methods
contentfwk_Capability_businessValue: Property = Property(name="businessValue", type=StringType)
contentfwk_Capability_increments: Property = Property(name="increments", type=StringType)
contentfwk_Capability.attributes={contentfwk_Capability_increments, contentfwk_Capability_businessValue}

# contentfwk_WorkPackage class attributes and methods
contentfwk_WorkPackage_workPackageCategory: Property = Property(name="workPackageCategory", type=StringType)
contentfwk_WorkPackage.attributes={contentfwk_WorkPackage_workPackageCategory}

# contentfwk_StrategicElement class attributes and methods

# contentfwk_Principle class attributes and methods
contentfwk_Principle_principleCategory: Property = Property(name="principleCategory", type=StringType)
contentfwk_Principle_priority: Property = Property(name="priority", type=StringType)
contentfwk_Principle_statementOfPrinciple: Property = Property(name="statementOfPrinciple", type=StringType)
contentfwk_Principle_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Principle_implication: Property = Property(name="implication", type=StringType)
contentfwk_Principle_metric: Property = Property(name="metric", type=StringType)
contentfwk_Principle.attributes={contentfwk_Principle_statementOfPrinciple, contentfwk_Principle_priority, contentfwk_Principle_rationale, contentfwk_Principle_implication, contentfwk_Principle_metric, contentfwk_Principle_principleCategory}

# StrategicElement class attributes and methods

# contentfwk_Constraint class attributes and methods

# contentfwk_Assumption class attributes and methods

# contentfwk_Requirement class attributes and methods
contentfwk_Requirement_statementOfRequirement: Property = Property(name="statementOfRequirement", type=StringType)
contentfwk_Requirement_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Requirement_acceptanceCriteria: Property = Property(name="acceptanceCriteria", type=StringType)
contentfwk_Requirement.attributes={contentfwk_Requirement_acceptanceCriteria, contentfwk_Requirement_statementOfRequirement, contentfwk_Requirement_rationale}

# contentfwk_Gap class attributes and methods

# DataComponent class attributes and methods

# contentfwk_ApplicationArchitecture class attributes and methods

# contentfwk_InformationSystemService class attributes and methods

# contentfwk_StrategicArchitecture class attributes and methods

# contentfwk_Standard class attributes and methods
contentfwk_Standard_standardClass: Property = Property(name="standardClass", type=StringType)
contentfwk_Standard_standardCreationDate: Property = Property(name="standardCreationDate", type=DateType)
contentfwk_Standard_lastStandardCreationDate: Property = Property(name="lastStandardCreationDate", type=DateType)
contentfwk_Standard_nextStandardCreationDate: Property = Property(name="nextStandardCreationDate", type=DateType)
contentfwk_Standard_retireDate: Property = Property(name="retireDate", type=DateType)
contentfwk_Standard.attributes={contentfwk_Standard_standardClass, contentfwk_Standard_lastStandardCreationDate, contentfwk_Standard_retireDate, contentfwk_Standard_nextStandardCreationDate, contentfwk_Standard_standardCreationDate}

# contentfwk_ApplicationComponent class attributes and methods

# contentfwk_DataComponent class attributes and methods

# contentfwk_TechnologyComponent class attributes and methods

# Relationships
architectures0: BinaryAssociation = BinaryAssociation(
    name="architectures0",
    ends={
        Property(name="contentfwk_EnterpriseArchitecture", type=contentfwk_Architecture, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="contentfwk_Architecture", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1))
    }
)
containers1: BinaryAssociation = BinaryAssociation(
    name="containers1",
    ends={
        Property(name="contentfwk_Container", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_EnterpriseArchitecture2", type=contentfwk_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels3: BinaryAssociation = BinaryAssociation(
    name="labels3",
    ends={
        Property(name="contentfwk_Label", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_EnterpriseArchitecture4", type=contentfwk_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drivers5: BinaryAssociation = BinaryAssociation(
    name="drivers5",
    ends={
        Property(name="contentfwk_Driver", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls22: BinaryAssociation = BinaryAssociation(
    name="controls22",
    ends={
        Property(name="contentfwk_Control", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture23", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events24: BinaryAssociation = BinaryAssociation(
    name="events24",
    ends={
        Property(name="contentfwk_Event", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture25", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations26: BinaryAssociation = BinaryAssociation(
    name="locations26",
    ends={
        Property(name="contentfwk_Location", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture27", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products28: BinaryAssociation = BinaryAssociation(
    name="products28",
    ends={
        Property(name="contentfwk_Product", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture29", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contracts30: BinaryAssociation = BinaryAssociation(
    name="contracts30",
    ends={
        Property(name="contentfwk_Contract", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture31", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures32: BinaryAssociation = BinaryAssociation(
    name="measures32",
    ends={
        Property(name="contentfwk_Measure", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture33", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals6: BinaryAssociation = BinaryAssociation(
    name="goals6",
    ends={
        Property(name="contentfwk_Goal", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture7", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectives8: BinaryAssociation = BinaryAssociation(
    name="objectives8",
    ends={
        Property(name="contentfwk_Objective", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture9", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units10: BinaryAssociation = BinaryAssociation(
    name="units10",
    ends={
        Property(name="contentfwk_OrganizationUnit", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture11", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors12: BinaryAssociation = BinaryAssociation(
    name="actors12",
    ends={
        Property(name="contentfwk_Actor", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture13", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles14: BinaryAssociation = BinaryAssociation(
    name="roles14",
    ends={
        Property(name="contentfwk_Role", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture15", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions16: BinaryAssociation = BinaryAssociation(
    name="functions16",
    ends={
        Property(name="contentfwk_Function", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture17", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services18: BinaryAssociation = BinaryAssociation(
    name="services18",
    ends={
        Property(name="contentfwk_BusinessService", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture19", type=contentfwk_BusinessService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes20: BinaryAssociation = BinaryAssociation(
    name="processes20",
    ends={
        Property(name="contentfwk_Process", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture21", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents42: BinaryAssociation = BinaryAssociation(
    name="physicalComponents42",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture43", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents44: BinaryAssociation = BinaryAssociation(
    name="logicalComponents44",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture45", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createsGoals46: BinaryAssociation = BinaryAssociation(
    name="createsGoals46",
    ends={
        Property(name="Goal", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="addressesDrivers", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
motivatesOrganizationUnits47: BinaryAssociation = BinaryAssociation(
    name="motivatesOrganizationUnits47",
    ends={
        Property(name="OrganizationUnit", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="isMotivatedByDrivers", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesDriver49: BinaryAssociation = BinaryAssociation(
    name="decomposesDriver49",
    ends={
        Property(name="contentfwk_Driver50", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Driver48", type=contentfwk_Driver, multiplicity=Multiplicity(0, 1))
    }
)
servicesQuality34: BinaryAssociation = BinaryAssociation(
    name="servicesQuality34",
    ends={
        Property(name="contentfwk_ServiceQuality", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture35", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities36: BinaryAssociation = BinaryAssociation(
    name="entities36",
    ends={
        Property(name="contentfwk_DataEntity", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents37: BinaryAssociation = BinaryAssociation(
    name="logicalComponents37",
    ends={
        Property(name="contentfwk_LogicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture38", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents39: BinaryAssociation = BinaryAssociation(
    name="physicalComponents39",
    ends={
        Property(name="contentfwk_PhysicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture40", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platformServices41: BinaryAssociation = BinaryAssociation(
    name="platformServices41",
    ends={
        Property(name="contentfwk_PlatformService", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decomposesObjective60: BinaryAssociation = BinaryAssociation(
    name="decomposesObjective60",
    ends={
        Property(name="contentfwk_Objective59", type=contentfwk_Objective, multiplicity=Multiplicity(0, 1)),
        Property(name="contentfwk_Objective61", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1))
    }
)
ownsAndGovernsServices62: BinaryAssociation = BinaryAssociation(
    name="ownsAndGovernsServices62",
    ends={
        Property(name="Service", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedAndGovernedByOrganizationUnits", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors63: BinaryAssociation = BinaryAssociation(
    name="containsActors63",
    ends={
        Property(name="Actor", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsTo", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
ownsFunctions64: BinaryAssociation = BinaryAssociation(
    name="ownsFunctions64",
    ends={
        Property(name="Function", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedByUnit", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses65: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses65",
    ends={
        Property(name="Process", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesOrganizationUnits", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isMotivatedByDrivers66: BinaryAssociation = BinaryAssociation(
    name="isMotivatedByDrivers66",
    ends={
        Property(name="Driver67", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="motivatesOrganizationUnits", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
addressesDrivers51: BinaryAssociation = BinaryAssociation(
    name="addressesDrivers51",
    ends={
        Property(name="Driver", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="createsGoals", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughObjectives52: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughObjectives52",
    ends={
        Property(name="Objective", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesGoals", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesGoal54: BinaryAssociation = BinaryAssociation(
    name="decomposesGoal54",
    ends={
        Property(name="contentfwk_Goal55", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Goal53", type=contentfwk_Goal, multiplicity=Multiplicity(0, 1))
    }
)
realizesGoals56: BinaryAssociation = BinaryAssociation(
    name="realizesGoals56",
    ends={
        Property(name="Goal57", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughObjectives", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures58: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures58",
    ends={
        Property(name="Measure", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForObjectives", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
interactsWithFunctions75: BinaryAssociation = BinaryAssociation(
    name="interactsWithFunctions75",
    ends={
        Property(name="supportsActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999)),
        Property(name="Function76", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1))
    }
)
performsTaskInRoles77: BinaryAssociation = BinaryAssociation(
    name="performsTaskInRoles77",
    ends={
        Property(name="Role", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isAssumedByActors", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses78: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses78",
    ends={
        Property(name="Process79", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesActors", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices80: BinaryAssociation = BinaryAssociation(
    name="consumesServices80",
    ends={
        Property(name="contentfwk_Service", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor81", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents82: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents82",
    ends={
        Property(name="Event", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents83: BinaryAssociation = BinaryAssociation(
    name="generatesEvents83",
    ends={
        Property(name="Event84", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation85: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation85",
    ends={
        Property(name="Location87", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors86", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
producesProducts68: BinaryAssociation = BinaryAssociation(
    name="producesProducts68",
    ends={
        Property(name="Product", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByOrganizationUnits", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation69: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation69",
    ends={
        Property(name="Location", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="containsOrganizationUnits", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
suppliesEntities70: BinaryAssociation = BinaryAssociation(
    name="suppliesEntities70",
    ends={
        Property(name="DataEntity", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities71: BinaryAssociation = BinaryAssociation(
    name="consumesEntities71",
    ends={
        Property(name="DataEntity72", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isConsumedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo73: BinaryAssociation = BinaryAssociation(
    name="belongsTo73",
    ends={
        Property(name="OrganizationUnit74", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
performsFunctions88: BinaryAssociation = BinaryAssociation(
    name="performsFunctions88",
    ends={
        Property(name="Function89", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isPerformedByActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesActors91: BinaryAssociation = BinaryAssociation(
    name="decomposesActors91",
    ends={
        Property(name="contentfwk_Actor92", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor90", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAssumedByActors93: BinaryAssociation = BinaryAssociation(
    name="isAssumedByActors93",
    ends={
        Property(name="Actor94", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="performsTaskInRoles", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isConsumedByActors102: BinaryAssociation = BinaryAssociation(
    name="isConsumedByActors102",
    ends={
        Property(name="Actor103", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAccessedByServices104: BinaryAssociation = BinaryAssociation(
    name="isAccessedByServices104",
    ends={
        Property(name="Service106", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesEntities105", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isUpdatedThroughServices107: BinaryAssociation = BinaryAssociation(
    name="isUpdatedThroughServices107",
    ends={
        Property(name="Service108", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providesEntities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
residesWithinLogicalDataComponent109: BinaryAssociation = BinaryAssociation(
    name="residesWithinLogicalDataComponent109",
    ends={
        Property(name="LogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatesDataEntities", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
accessesFunctions95: BinaryAssociation = BinaryAssociation(
    name="accessesFunctions95",
    ends={
        Property(name="Function96", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="canBeAccessedByRoles", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesRole98: BinaryAssociation = BinaryAssociation(
    name="decomposesRole98",
    ends={
        Property(name="contentfwk_Role99", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Role97", type=contentfwk_Role, multiplicity=Multiplicity(0, 1))
    }
)
isSuppliedByActors100: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByActors100",
    ends={
        Property(name="Actor101", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
implementsServices117: BinaryAssociation = BinaryAssociation(
    name="implementsServices117",
    ends={
        Property(name="Service118", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughLogicalApplicationComponent", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
operatesOnDataEntities119: BinaryAssociation = BinaryAssociation(
    name="operatesOnDataEntities119",
    ends={
        Property(name="DataEntity120", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isProcessesByLogicalApplicationComponents", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalApplicationComponents121: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalApplicationComponents121",
    ends={
        Property(name="PhysicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalApplicationComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith123: BinaryAssociation = BinaryAssociation(
    name="communicatesWith123",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent122", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalApplicationComponent125: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalApplicationComponent125",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent126", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent124", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
isProcessesByLogicalApplicationComponents110: BinaryAssociation = BinaryAssociation(
    name="isProcessesByLogicalApplicationComponents110",
    ends={
        Property(name="LogicalApplicationComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesOnDataEntities", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposeEntity112: BinaryAssociation = BinaryAssociation(
    name="decomposeEntity112",
    ends={
        Property(name="contentfwk_DataEntity113", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity111", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 1))
    }
)
relatesTo115: BinaryAssociation = BinaryAssociation(
    name="relatesTo115",
    ends={
        Property(name="contentfwk_DataEntity116", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity114", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isBoundedByServices131: BinaryAssociation = BinaryAssociation(
    name="isBoundedByServices131",
    ends={
        Property(name="providesGovernedInterfaceToAccessFunctions", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999)),
        Property(name="Service132", type=contentfwk_Function, multiplicity=Multiplicity(1, 1))
    }
)
supportsProcesses133: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses133",
    ends={
        Property(name="Process134", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses135: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses135",
    ends={
        Property(name="Process136", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
canBeAccessedByRoles137: BinaryAssociation = BinaryAssociation(
    name="canBeAccessedByRoles137",
    ends={
        Property(name="Role138", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesFunctions", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
supportsActors139: BinaryAssociation = BinaryAssociation(
    name="supportsActors139",
    ends={
        Property(name="Actor140", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="interactsWithFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunction142: BinaryAssociation = BinaryAssociation(
    name="decomposesFunction142",
    ends={
        Property(name="contentfwk_Function143", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function141", type=contentfwk_Function, multiplicity=Multiplicity(0, 1))
    }
)
isPerformedByActors127: BinaryAssociation = BinaryAssociation(
    name="isPerformedByActors127",
    ends={
        Property(name="Actor128", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="performsFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedByUnit129: BinaryAssociation = BinaryAssociation(
    name="isOwnedByUnit129",
    ends={
        Property(name="OrganizationUnit130", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsFunctions", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
orchestratesFunctions150: BinaryAssociation = BinaryAssociation(
    name="orchestratesFunctions150",
    ends={
        Property(name="Function151", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunctions152: BinaryAssociation = BinaryAssociation(
    name="decomposesFunctions152",
    ends={
        Property(name="Function153", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
involvesOrganizationUnits154: BinaryAssociation = BinaryAssociation(
    name="involvesOrganizationUnits154",
    ends={
        Property(name="OrganizationUnit155", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesServices156: BinaryAssociation = BinaryAssociation(
    name="orchestratesServices156",
    ends={
        Property(name="Service158", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses157", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices159: BinaryAssociation = BinaryAssociation(
    name="decomposesServices159",
    ends={
        Property(name="Service161", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses160", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
communicatedWithFunctions145: BinaryAssociation = BinaryAssociation(
    name="communicatedWithFunctions145",
    ends={
        Property(name="contentfwk_Function146", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function144", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
supportsObjective147: BinaryAssociation = BinaryAssociation(
    name="supportsObjective147",
    ends={
        Property(name="contentfwk_Objective149", type=contentfwk_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessService148", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesProcess173: BinaryAssociation = BinaryAssociation(
    name="decomposesProcess173",
    ends={
        Property(name="contentfwk_Process174", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Process172", type=contentfwk_Process, multiplicity=Multiplicity(0, 1))
    }
)
precedesProcesses176: BinaryAssociation = BinaryAssociation(
    name="precedesProcesses176",
    ends={
        Property(name="Process177", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="followsProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
followsProcesses179: BinaryAssociation = BinaryAssociation(
    name="followsProcesses179",
    ends={
        Property(name="Process180", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="precedesProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
involvesActors162: BinaryAssociation = BinaryAssociation(
    name="involvesActors162",
    ends={
        Property(name="Actor164", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses163", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGuidedByControls165: BinaryAssociation = BinaryAssociation(
    name="isGuidedByControls165",
    ends={
        Property(name="Control", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ensuresCorrectOperationOfProcesses", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents166: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents166",
    ends={
        Property(name="Event167", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents168: BinaryAssociation = BinaryAssociation(
    name="generatesEvents168",
    ends={
        Property(name="Event169", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts170: BinaryAssociation = BinaryAssociation(
    name="producesProducts170",
    ends={
        Property(name="Product171", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByProcesses", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation186: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation186",
    ends={
        Property(name="Location187", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalTechnologyComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalTechnologyComponent189: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalTechnologyComponent189",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent190", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent188", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnPhysicalTechnologyComponents192: BinaryAssociation = BinaryAssociation(
    name="isDependentOnPhysicalTechnologyComponents192",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent193", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent191", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isSuppliedByLogicalTechnologyComponents181: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByLogicalTechnologyComponents181",
    ends={
        Property(name="LogicalTechnologyComponent", type=contentfwk_PlatformService, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesPlatformServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
realizesApplicationComponents182: BinaryAssociation = BinaryAssociation(
    name="realizesApplicationComponents182",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent183", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalTechnologyComponents184: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalTechnologyComponents184",
    ends={
        Property(name="LogicalTechnologyComponent185", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByPhysicalTechnologyComponents", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesMeasure205: BinaryAssociation = BinaryAssociation(
    name="decomposesMeasure205",
    ends={
        Property(name="contentfwk_Measure206", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Measure204", type=contentfwk_Measure, multiplicity=Multiplicity(0, 1))
    }
)
appliesToServices207: BinaryAssociation = BinaryAssociation(
    name="appliesToServices207",
    ends={
        Property(name="Service208", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsQualities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToContracts209: BinaryAssociation = BinaryAssociation(
    name="appliesToContracts209",
    ends={
        Property(name="Contract", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
governsAndMeasuresBusinessServices210: BinaryAssociation = BinaryAssociation(
    name="governsAndMeasuresBusinessServices210",
    ends={
        Property(name="Service211", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="isGovernedAndMeasuredByContracts", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByOrganizationUnits194: BinaryAssociation = BinaryAssociation(
    name="isProducedByOrganizationUnits194",
    ends={
        Property(name="OrganizationUnit195", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByProcesses196: BinaryAssociation = BinaryAssociation(
    name="isProducedByProcesses196",
    ends={
        Property(name="Process198", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts197", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForObjectives199: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForObjectives199",
    ends={
        Property(name="Objective200", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForServices201: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForServices201",
    ends={
        Property(name="Service203", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures202", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
meetsServiceQuality212: BinaryAssociation = BinaryAssociation(
    name="meetsServiceQuality212",
    ends={
        Property(name="ServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToContracts", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByActors223: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByActors223",
    ends={
        Property(name="Actor225", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents224", type=contentfwk_Actor, multiplicity=Multiplicity(0, 1))
    }
)
ensuresCorrectOperationOfProcesses226: BinaryAssociation = BinaryAssociation(
    name="ensuresCorrectOperationOfProcesses226",
    ends={
        Property(name="Process227", type=contentfwk_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="isGuidedByControls", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
delegates229: BinaryAssociation = BinaryAssociation(
    name="delegates229",
    ends={
        Property(name="Element", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="isDelegatedBy", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isDelegatedBy231: BinaryAssociation = BinaryAssociation(
    name="isDelegatedBy231",
    ends={
        Property(name="Element232", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByBusinessServices213: BinaryAssociation = BinaryAssociation(
    name="isResolvedByBusinessServices213",
    ends={
        Property(name="Service214", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByProcesses215: BinaryAssociation = BinaryAssociation(
    name="isResolvedByProcesses215",
    ends={
        Property(name="Process217", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents216", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByProcesses218: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByProcesses218",
    ends={
        Property(name="Process219", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByActors220: BinaryAssociation = BinaryAssociation(
    name="isResolvedByActors220",
    ends={
        Property(name="Actor222", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents221", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
labels237: BinaryAssociation = BinaryAssociation(
    name="labels237",
    ends={
        Property(name="Label238", type=contentfwk_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="containers", type=contentfwk_Label, multiplicity=Multiplicity(0, 9999))
    }
)
subLabels240: BinaryAssociation = BinaryAssociation(
    name="subLabels240",
    ends={
        Property(name="contentfwk_Label241", type=contentfwk_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Label239", type=contentfwk_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements242: BinaryAssociation = BinaryAssociation(
    name="ownedElements242",
    ends={
        Property(name="Element243", type=contentfwk_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
containers244: BinaryAssociation = BinaryAssociation(
    name="containers244",
    ends={
        Property(name="Container", type=contentfwk_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=contentfwk_Container, multiplicity=Multiplicity(0, 9999))
    }
)
category233: BinaryAssociation = BinaryAssociation(
    name="category233",
    ends={
        Property(name="Label", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElements", type=contentfwk_Label, multiplicity=Multiplicity(0, 9999))
    }
)
subContainers235: BinaryAssociation = BinaryAssociation(
    name="subContainers235",
    ends={
        Property(name="contentfwk_Container236", type=contentfwk_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Container234", type=contentfwk_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsPhysicalTechnologyComponents253: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalTechnologyComponents253",
    ends={
        Property(name="PhysicalTechnologyComponent", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation254", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors245: BinaryAssociation = BinaryAssociation(
    name="containsActors245",
    ends={
        Property(name="Actor246", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLocation256: BinaryAssociation = BinaryAssociation(
    name="decomposesLocation256",
    ends={
        Property(name="contentfwk_Location257", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Location255", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
containsOrganizationUnits247: BinaryAssociation = BinaryAssociation(
    name="containsOrganizationUnits247",
    ends={
        Property(name="OrganizationUnit249", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation248", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalDataComponents250: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalDataComponents250",
    ends={
        Property(name="PhysicalDataComponent", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHotedInLocation", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isDeliveredBy258: BinaryAssociation = BinaryAssociation(
    name="isDeliveredBy258",
    ends={
        Property(name="WorkPackage", type=contentfwk_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="deliversCapabilities", type=contentfwk_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
containsPhysicalApplicationComponents251: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalApplicationComponents251",
    ends={
        Property(name="PhysicalApplicationComponent252", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
deliversCapabilities259: BinaryAssociation = BinaryAssociation(
    name="deliversCapabilities259",
    ends={
        Property(name="Capability", type=contentfwk_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="isDeliveredBy", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesDataEntities260: BinaryAssociation = BinaryAssociation(
    name="encapsulatesDataEntities260",
    ends={
        Property(name="DataEntity261", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="residesWithinLogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalDataComponents262: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalDataComponents262",
    ends={
        Property(name="PhysicalDataComponent263", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalDataComponents", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalDataComponents264: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalDataComponents264",
    ends={
        Property(name="LogicalDataComponent265", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalDataComponents", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHotedInLocation266: BinaryAssociation = BinaryAssociation(
    name="isHotedInLocation266",
    ends={
        Property(name="Location267", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalDataComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
decomposesPhysicalDataComponent269: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalDataComponent269",
    ends={
        Property(name="contentfwk_PhysicalDataComponent270", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent268", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatesPhysicalApplicationComponents271: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalApplicationComponents271",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent273", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent272", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
logicalApplicationComponents274: BinaryAssociation = BinaryAssociation(
    name="logicalApplicationComponents274",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent275", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalApplicationComponents276: BinaryAssociation = BinaryAssociation(
    name="physicalApplicationComponents276",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent278", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture277", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informationSystemServices279: BinaryAssociation = BinaryAssociation(
    name="informationSystemServices279",
    ends={
        Property(name="contentfwk_InformationSystemService", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture280", type=contentfwk_InformationSystemService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsLogicalApplicationComponents281: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalApplicationComponents281",
    ends={
        Property(name="LogicalApplicationComponent282", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalApplicationComponents", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation283: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation283",
    ends={
        Property(name="Location284", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalApplicationComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith286: BinaryAssociation = BinaryAssociation(
    name="communicatesWith286",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent287", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent285", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesPhysicalDataComponents288: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalDataComponents288",
    ends={
        Property(name="contentfwk_PhysicalDataComponent290", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent289", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents291: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents291",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent293", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent292", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalApplicationComponent295: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalApplicationComponent295",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent296", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent294", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
providesPlatformForServices297: BinaryAssociation = BinaryAssociation(
    name="providesPlatformForServices297",
    ends={
        Property(name="Service298", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isImplementedOnLogicalTechnologyComponents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
suppliesPlatformServices299: BinaryAssociation = BinaryAssociation(
    name="suppliesPlatformServices299",
    ends={
        Property(name="PlatformService", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByLogicalTechnologyComponents", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents300: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents300",
    ends={
        Property(name="PhysicalTechnologyComponent301", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalTechnologyComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalTechnologyComponent303: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalTechnologyComponent303",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent304", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent302", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnLogicalTechnologyComponents306: BinaryAssociation = BinaryAssociation(
    name="isDependentOnLogicalTechnologyComponents306",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent307", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent305", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
capabilities308: BinaryAssociation = BinaryAssociation(
    name="capabilities308",
    ends={
        Property(name="contentfwk_Capability", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strategicElements309: BinaryAssociation = BinaryAssociation(
    name="strategicElements309",
    ends={
        Property(name="contentfwk_StrategicElement", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture310", type=contentfwk_StrategicElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isProvidedToActors311: BinaryAssociation = BinaryAssociation(
    name="isProvidedToActors311",
    ends={
        Property(name="contentfwk_Actor313", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service312", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
providesGovernedInterfaceToAccessFunctions314: BinaryAssociation = BinaryAssociation(
    name="providesGovernedInterfaceToAccessFunctions314",
    ends={
        Property(name="Function315", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isBoundedByServices", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
providesEntities316: BinaryAssociation = BinaryAssociation(
    name="providesEntities316",
    ends={
        Property(name="DataEntity317", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isUpdatedThroughServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities318: BinaryAssociation = BinaryAssociation(
    name="consumesEntities318",
    ends={
        Property(name="DataEntity319", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isAccessedByServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isGovernedAndMeasuredByContracts320: BinaryAssociation = BinaryAssociation(
    name="isGovernedAndMeasuredByContracts320",
    ends={
        Property(name="Contract321", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="governsAndMeasuresBusinessServices", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents322: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents322",
    ends={
        Property(name="Event323", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByBusinessServices", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
isImplementedOnLogicalTechnologyComponents324: BinaryAssociation = BinaryAssociation(
    name="isImplementedOnLogicalTechnologyComponents324",
    ends={
        Property(name="LogicalTechnologyComponent325", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="providesPlatformForServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughLogicalApplicationComponent326: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughLogicalApplicationComponent326",
    ends={
        Property(name="LogicalApplicationComponent327", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="implementsServices", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedAndGovernedByOrganizationUnits328: BinaryAssociation = BinaryAssociation(
    name="isOwnedAndGovernedByOrganizationUnits328",
    ends={
        Property(name="OrganizationUnit329", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsAndGovernsServices", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures330: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures330",
    ends={
        Property(name="Measure331", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForServices", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses332: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses332",
    ends={
        Property(name="Process333", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses334: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses334",
    ends={
        Property(name="Process335", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
meetsQualities336: BinaryAssociation = BinaryAssociation(
    name="meetsQualities336",
    ends={
        Property(name="ServiceQuality337", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToServices", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices339: BinaryAssociation = BinaryAssociation(
    name="consumesServices339",
    ends={
        Property(name="contentfwk_Service340", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service338", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices342: BinaryAssociation = BinaryAssociation(
    name="decomposesServices342",
    ends={
        Property(name="contentfwk_Service343", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service341", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_contentfwk_BusinessArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_BusinessArchitecture)
gen_contentfwk_Driver_Element = Generalization(general=Element, specific=contentfwk_Driver)
gen_contentfwk_Goal_Element = Generalization(general=Element, specific=contentfwk_Goal)
gen_contentfwk_DataArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_DataArchitecture)
gen_contentfwk_TechnologyArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_TechnologyArchitecture)
gen_contentfwk_OrganizationUnit_Element = Generalization(general=Element, specific=contentfwk_OrganizationUnit)
gen_contentfwk_Objective_Element = Generalization(general=Element, specific=contentfwk_Objective)
gen_contentfwk_Actor_Element = Generalization(general=Element, specific=contentfwk_Actor)
gen_contentfwk_Role_Element = Generalization(general=Element, specific=contentfwk_Role)
gen_contentfwk_DataEntity_Element = Generalization(general=Element, specific=contentfwk_DataEntity)
gen_contentfwk_LogicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_LogicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_Function_Element = Generalization(general=Element, specific=contentfwk_Function)
gen_contentfwk_Function_Standard = Generalization(general=Standard, specific=contentfwk_Function)
gen_contentfwk_BusinessService_Element = Generalization(general=Element, specific=contentfwk_BusinessService)
gen_contentfwk_BusinessService_Service = Generalization(general=Service, specific=contentfwk_BusinessService)
gen_contentfwk_Process_Element = Generalization(general=Element, specific=contentfwk_Process)
gen_contentfwk_Process_Standard = Generalization(general=Standard, specific=contentfwk_Process)
gen_contentfwk_PlatformService_Element = Generalization(general=Element, specific=contentfwk_PlatformService)
gen_contentfwk_PlatformService_Service = Generalization(general=Service, specific=contentfwk_PlatformService)
gen_contentfwk_PhysicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_ServiceQuality_Element = Generalization(general=Element, specific=contentfwk_ServiceQuality)
gen_contentfwk_Contract_Element = Generalization(general=Element, specific=contentfwk_Contract)
gen_contentfwk_Product_Element = Generalization(general=Element, specific=contentfwk_Product)
gen_contentfwk_Measure_Element = Generalization(general=Element, specific=contentfwk_Measure)
gen_contentfwk_Control_Element = Generalization(general=Element, specific=contentfwk_Control)
gen_contentfwk_Event_Element = Generalization(general=Element, specific=contentfwk_Event)
gen_contentfwk_Location_Element = Generalization(general=Element, specific=contentfwk_Location)
gen_contentfwk_Capability_Element = Generalization(general=Element, specific=contentfwk_Capability)
gen_contentfwk_StrategicElement_Element = Generalization(general=Element, specific=contentfwk_StrategicElement)
gen_contentfwk_Principle_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Principle)
gen_contentfwk_Constraint_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Constraint)
gen_contentfwk_Assumption_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Assumption)
gen_contentfwk_Requirement_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Requirement)
gen_contentfwk_Gap_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Gap)
gen_contentfwk_WorkPackage_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_WorkPackage)
gen_contentfwk_LogicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_LogicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_PhysicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_PhysicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_ApplicationArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_ApplicationArchitecture)
gen_contentfwk_PhysicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_LogicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_StrategicArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_StrategicArchitecture)
gen_contentfwk_Service_Standard = Generalization(general=Standard, specific=contentfwk_Service)
gen_contentfwk_ApplicationComponent_Standard = Generalization(general=Standard, specific=contentfwk_ApplicationComponent)
gen_contentfwk_InformationSystemService_Service = Generalization(general=Service, specific=contentfwk_InformationSystemService)
gen_contentfwk_InformationSystemService_Element = Generalization(general=Element, specific=contentfwk_InformationSystemService)
gen_contentfwk_DataComponent_Standard = Generalization(general=Standard, specific=contentfwk_DataComponent)
gen_contentfwk_TechnologyComponent_Standard = Generalization(general=Standard, specific=contentfwk_TechnologyComponent)

# Domain Model
domain_model = DomainModel(
    name="contentfwk",
    types={contentfwk_Container, contentfwk_Label, contentfwk_BusinessArchitecture, Architecture, contentfwk_Driver, contentfwk_Goal, contentfwk_EnterpriseArchitecture, contentfwk_Architecture, contentfwk_Control, contentfwk_Event, contentfwk_Location, contentfwk_Product, contentfwk_Contract, contentfwk_Measure, contentfwk_Objective, contentfwk_OrganizationUnit, contentfwk_Actor, contentfwk_Role, contentfwk_Function, contentfwk_BusinessService, contentfwk_Process, contentfwk_PhysicalTechnologyComponent, contentfwk_LogicalTechnologyComponent, Element, contentfwk_ServiceQuality, contentfwk_DataArchitecture, contentfwk_DataEntity, contentfwk_LogicalDataComponent, contentfwk_PhysicalDataComponent, contentfwk_TechnologyArchitecture, contentfwk_PlatformService, contentfwk_Service, contentfwk_LogicalApplicationComponent, contentfwk_PhysicalApplicationComponent, ApplicationComponent, Standard, Service, TechnologyComponent, contentfwk_Element, contentfwk_Capability, contentfwk_WorkPackage, contentfwk_StrategicElement, contentfwk_Principle, StrategicElement, contentfwk_Constraint, contentfwk_Assumption, contentfwk_Requirement, contentfwk_Gap, DataComponent, contentfwk_ApplicationArchitecture, contentfwk_InformationSystemService, contentfwk_StrategicArchitecture, contentfwk_Standard, contentfwk_ApplicationComponent, contentfwk_DataComponent, contentfwk_TechnologyComponent, PrincipleCategory, StandardsClass, LifeCycleStatus, DataEntityCategory, WorkPackageCategory},
    associations={architectures0, containers1, labels3, drivers5, controls22, events24, locations26, products28, contracts30, measures32, goals6, objectives8, units10, actors12, roles14, functions16, services18, processes20, physicalComponents42, logicalComponents44, createsGoals46, motivatesOrganizationUnits47, decomposesDriver49, servicesQuality34, entities36, logicalComponents37, physicalComponents39, platformServices41, decomposesObjective60, ownsAndGovernsServices62, containsActors63, ownsFunctions64, participatesInProcesses65, isMotivatedByDrivers66, addressesDrivers51, isRealizedThroughObjectives52, decomposesGoal54, realizesGoals56, isTrackedAgainstMeasures58, interactsWithFunctions75, performsTaskInRoles77, participatesInProcesses78, consumesServices80, resolvesEvents82, generatesEvents83, operatesInLocation85, producesProducts68, operatesInLocation69, suppliesEntities70, consumesEntities71, belongsTo73, performsFunctions88, decomposesActors91, isAssumedByActors93, isConsumedByActors102, isAccessedByServices104, isUpdatedThroughServices107, residesWithinLogicalDataComponent109, accessesFunctions95, decomposesRole98, isSuppliedByActors100, implementsServices117, operatesOnDataEntities119, isExtendedByPhysicalApplicationComponents121, communicatesWith123, decomposesLogicalApplicationComponent125, isProcessesByLogicalApplicationComponents110, decomposeEntity112, relatesTo115, isBoundedByServices131, supportsProcesses133, isRealizedByProcesses135, canBeAccessedByRoles137, supportsActors139, decomposesFunction142, isPerformedByActors127, isOwnedByUnit129, orchestratesFunctions150, decomposesFunctions152, involvesOrganizationUnits154, orchestratesServices156, decomposesServices159, communicatedWithFunctions145, supportsObjective147, decomposesProcess173, precedesProcesses176, followsProcesses179, involvesActors162, isGuidedByControls165, resolvesEvents166, generatesEvents168, producesProducts170, isHostedInLocation186, decomposesPhysicalTechnologyComponent189, isDependentOnPhysicalTechnologyComponents192, isSuppliedByLogicalTechnologyComponents181, realizesApplicationComponents182, extendsLogicalTechnologyComponents184, decomposesMeasure205, appliesToServices207, appliesToContracts209, governsAndMeasuresBusinessServices210, isProducedByOrganizationUnits194, isProducedByProcesses196, setsPerformanceCriteriaForObjectives199, setsPerformanceCriteriaForServices201, meetsServiceQuality212, isGeneratedByActors223, ensuresCorrectOperationOfProcesses226, delegates229, isDelegatedBy231, isResolvedByBusinessServices213, isResolvedByProcesses215, isGeneratedByProcesses218, isResolvedByActors220, labels237, subLabels240, ownedElements242, containers244, category233, subContainers235, containsPhysicalTechnologyComponents253, containsActors245, decomposesLocation256, containsOrganizationUnits247, containsPhysicalDataComponents250, isDeliveredBy258, containsPhysicalApplicationComponents251, deliversCapabilities259, encapsulatesDataEntities260, isExtendedByPhysicalDataComponents262, extendsLogicalDataComponents264, isHotedInLocation266, decomposesPhysicalDataComponent269, encapsulatesPhysicalApplicationComponents271, logicalApplicationComponents274, physicalApplicationComponents276, informationSystemServices279, extendsLogicalApplicationComponents281, isHostedInLocation283, communicatesWith286, encapsulatesPhysicalDataComponents288, isRealizedByPhysicalTechnologyComponents291, decomposesPhysicalApplicationComponent295, providesPlatformForServices297, suppliesPlatformServices299, isRealizedByPhysicalTechnologyComponents300, decomposesLogicalTechnologyComponent303, isDependentOnLogicalTechnologyComponents306, capabilities308, strategicElements309, isProvidedToActors311, providesGovernedInterfaceToAccessFunctions314, providesEntities316, consumesEntities318, isGovernedAndMeasuredByContracts320, resolvesEvents322, isImplementedOnLogicalTechnologyComponents324, isRealizedThroughLogicalApplicationComponent326, isOwnedAndGovernedByOrganizationUnits328, isTrackedAgainstMeasures330, supportsProcesses332, isRealizedByProcesses334, meetsQualities336, consumesServices339, decomposesServices342},
    generalizations={gen_contentfwk_BusinessArchitecture_Architecture, gen_contentfwk_Driver_Element, gen_contentfwk_Goal_Element, gen_contentfwk_DataArchitecture_Architecture, gen_contentfwk_TechnologyArchitecture_Architecture, gen_contentfwk_OrganizationUnit_Element, gen_contentfwk_Objective_Element, gen_contentfwk_Actor_Element, gen_contentfwk_Role_Element, gen_contentfwk_DataEntity_Element, gen_contentfwk_LogicalApplicationComponent_Element, gen_contentfwk_LogicalApplicationComponent_ApplicationComponent, gen_contentfwk_Function_Element, gen_contentfwk_Function_Standard, gen_contentfwk_BusinessService_Element, gen_contentfwk_BusinessService_Service, gen_contentfwk_Process_Element, gen_contentfwk_Process_Standard, gen_contentfwk_PlatformService_Element, gen_contentfwk_PlatformService_Service, gen_contentfwk_PhysicalTechnologyComponent_Element, gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent, gen_contentfwk_ServiceQuality_Element, gen_contentfwk_Contract_Element, gen_contentfwk_Product_Element, gen_contentfwk_Measure_Element, gen_contentfwk_Control_Element, gen_contentfwk_Event_Element, gen_contentfwk_Location_Element, gen_contentfwk_Capability_Element, gen_contentfwk_StrategicElement_Element, gen_contentfwk_Principle_StrategicElement, gen_contentfwk_Constraint_StrategicElement, gen_contentfwk_Assumption_StrategicElement, gen_contentfwk_Requirement_StrategicElement, gen_contentfwk_Gap_StrategicElement, gen_contentfwk_WorkPackage_StrategicElement, gen_contentfwk_LogicalDataComponent_Element, gen_contentfwk_LogicalDataComponent_DataComponent, gen_contentfwk_PhysicalDataComponent_Element, gen_contentfwk_PhysicalDataComponent_DataComponent, gen_contentfwk_ApplicationArchitecture_Architecture, gen_contentfwk_PhysicalApplicationComponent_Element, gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent, gen_contentfwk_LogicalTechnologyComponent_Element, gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent, gen_contentfwk_StrategicArchitecture_Architecture, gen_contentfwk_Service_Standard, gen_contentfwk_ApplicationComponent_Standard, gen_contentfwk_InformationSystemService_Service, gen_contentfwk_InformationSystemService_Element, gen_contentfwk_DataComponent_Standard, gen_contentfwk_TechnologyComponent_Standard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)