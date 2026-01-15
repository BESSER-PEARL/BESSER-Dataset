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
contentfwk_EnterpriseArchitecture = Class(name="contentfwk::EnterpriseArchitecture")
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
contentfwk_Control = Class(name="contentfwk::Control")
contentfwk_Event = Class(name="contentfwk::Event")
contentfwk_Location = Class(name="contentfwk::Location")
contentfwk_Product = Class(name="contentfwk::Product")
contentfwk_Contract = Class(name="contentfwk::Contract")
contentfwk_Measure = Class(name="contentfwk::Measure")
contentfwk_ServiceQuality = Class(name="contentfwk::ServiceQuality")
contentfwk_Container = Class(name="contentfwk::Container")
contentfwk_PlatformService = Class(name="contentfwk::PlatformService")
contentfwk_PhysicalTechnologyComponent = Class(name="contentfwk::PhysicalTechnologyComponent")
contentfwk_LogicalTechnologyComponent = Class(name="contentfwk::LogicalTechnologyComponent")
Element = Class(name="Element")
contentfwk_DataArchitecture = Class(name="contentfwk::DataArchitecture")
contentfwk_DataEntity = Class(name="contentfwk::DataEntity")
contentfwk_LogicalDataComponent = Class(name="contentfwk::LogicalDataComponent")
contentfwk_PhysicalDataComponent = Class(name="contentfwk::PhysicalDataComponent")
contentfwk_TechnologyArchitecture = Class(name="contentfwk::TechnologyArchitecture")
contentfwk_Service = Class(name="contentfwk::Service", is_abstract=True)
contentfwk_LogicalApplicationComponent = Class(name="contentfwk::LogicalApplicationComponent")
contentfwk_PhysicalApplicationComponent = Class(name="contentfwk::PhysicalApplicationComponent")
Standard = Class(name="Standard")
ApplicationComponent = Class(name="ApplicationComponent")
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
DataComponent = Class(name="DataComponent")
contentfwk_ApplicationArchitecture = Class(name="contentfwk::ApplicationArchitecture")
contentfwk_InformationSystemService = Class(name="contentfwk::InformationSystemService")
contentfwk_Gap = Class(name="contentfwk::Gap")
contentfwk_StrategicArchitecture = Class(name="contentfwk::StrategicArchitecture")
contentfwk_Standard = Class(name="contentfwk::Standard", is_abstract=True)
contentfwk_ApplicationComponent = Class(name="contentfwk::ApplicationComponent", is_abstract=True)
contentfwk_DataComponent = Class(name="contentfwk::DataComponent", is_abstract=True)
contentfwk_TechnologyComponent = Class(name="contentfwk::TechnologyComponent", is_abstract=True)

# contentfwk_EnterpriseArchitecture class attributes and methods

# contentfwk_Architecture class attributes and methods

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
contentfwk_Actor.attributes={contentfwk_Actor_FTEs, contentfwk_Actor_actorTasks, contentfwk_Actor_actorGoal}

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

# contentfwk_Control class attributes and methods

# contentfwk_Event class attributes and methods

# contentfwk_Location class attributes and methods

# contentfwk_Product class attributes and methods

# contentfwk_Contract class attributes and methods
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
contentfwk_Contract_securityCharacteristics: Property = Property(name="securityCharacteristics", type=StringType)
contentfwk_Contract_privacyCharacteristics: Property = Property(name="privacyCharacteristics", type=StringType)
contentfwk_Contract_integrityCharacteristics: Property = Property(name="integrityCharacteristics", type=StringType)
contentfwk_Contract_credibilityCharacteristics: Property = Property(name="credibilityCharacteristics", type=StringType)
contentfwk_Contract_localizationCharacteristics: Property = Property(name="localizationCharacteristics", type=StringType)
contentfwk_Contract_internationalizationCharacteristics: Property = Property(name="internationalizationCharacteristics", type=StringType)
contentfwk_Contract_interoperabilityCharacteristics: Property = Property(name="interoperabilityCharacteristics", type=StringType)
contentfwk_Contract_scalabilityCharacteristics: Property = Property(name="scalabilityCharacteristics", type=StringType)
contentfwk_Contract_portabilityCharacteristics: Property = Property(name="portabilityCharacteristics", type=StringType)
contentfwk_Contract_behaviorCharacteristics: Property = Property(name="behaviorCharacteristics", type=StringType)
contentfwk_Contract_ServiceNameCaller: Property = Property(name="ServiceNameCaller", type=StringType)
contentfwk_Contract_growthPeriod: Property = Property(name="growthPeriod", type=StringType)
contentfwk_Contract_peakProfileShortTerm: Property = Property(name="peakProfileShortTerm", type=StringType)
contentfwk_Contract_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
contentfwk_Contract_extensibilityCharacteristics: Property = Property(name="extensibilityCharacteristics", type=StringType)
contentfwk_Contract_capacityCharacteristics: Property = Property(name="capacityCharacteristics", type=StringType)
contentfwk_Contract_throughput: Property = Property(name="throughput", type=StringType)
contentfwk_Contract_throughputPeriod: Property = Property(name="throughputPeriod", type=StringType)
contentfwk_Contract_growth: Property = Property(name="growth", type=StringType)
contentfwk_Contract.attributes={contentfwk_Contract_reliabilityCharacteristics, contentfwk_Contract_locatabilityCharacteristics, contentfwk_Contract_credibilityCharacteristics, contentfwk_Contract_growth, contentfwk_Contract_growthPeriod, contentfwk_Contract_peakProfileShortTerm, contentfwk_Contract_servicesTimes, contentfwk_Contract_contractControlRequirements, contentfwk_Contract_internationalizationCharacteristics, contentfwk_Contract_qualityOfInformationRequired, contentfwk_Contract_portabilityCharacteristics, contentfwk_Contract_resultControlRequirements, contentfwk_Contract_ServiceNameCalled, contentfwk_Contract_serviceabilityCharacteristics, contentfwk_Contract_ServiceNameCaller, contentfwk_Contract_performanceCharacteristics, contentfwk_Contract_extensibilityCharacteristics, contentfwk_Contract_localizationCharacteristics, contentfwk_Contract_interoperabilityCharacteristics, contentfwk_Contract_peakProfileLongTerm, contentfwk_Contract_behaviorCharacteristics, contentfwk_Contract_recoverabilityCharacteristics, contentfwk_Contract_manageabilityCharacteristics, contentfwk_Contract_throughput, contentfwk_Contract_scalabilityCharacteristics, contentfwk_Contract_integrityCharacteristics, contentfwk_Contract_privacyCharacteristics, contentfwk_Contract_serviceQualityCharacteristics, contentfwk_Contract_availabilityQualityCharacteristics, contentfwk_Contract_capacityCharacteristics, contentfwk_Contract_throughputPeriod, contentfwk_Contract_responseCharacteristics, contentfwk_Contract_securityCharacteristics}

# contentfwk_Measure class attributes and methods

# contentfwk_ServiceQuality class attributes and methods

# contentfwk_Container class attributes and methods
contentfwk_Container_name: Property = Property(name="name", type=StringType)
contentfwk_Container.attributes={contentfwk_Container_name}

# contentfwk_PlatformService class attributes and methods

# contentfwk_PhysicalTechnologyComponent class attributes and methods
contentfwk_PhysicalTechnologyComponent_productName: Property = Property(name="productName", type=StringType)
contentfwk_PhysicalTechnologyComponent_moduleName: Property = Property(name="moduleName", type=StringType)
contentfwk_PhysicalTechnologyComponent_vendor: Property = Property(name="vendor", type=StringType)
contentfwk_PhysicalTechnologyComponent_version: Property = Property(name="version", type=StringType)
contentfwk_PhysicalTechnologyComponent.attributes={contentfwk_PhysicalTechnologyComponent_version, contentfwk_PhysicalTechnologyComponent_moduleName, contentfwk_PhysicalTechnologyComponent_vendor, contentfwk_PhysicalTechnologyComponent_productName}

# contentfwk_LogicalTechnologyComponent class attributes and methods

# Element class attributes and methods

# contentfwk_DataArchitecture class attributes and methods

# contentfwk_DataEntity class attributes and methods
contentfwk_DataEntity_dataEntityCategory: Property = Property(name="dataEntityCategory", type=StringType)
contentfwk_DataEntity_privacyClassification: Property = Property(name="privacyClassification", type=StringType)
contentfwk_DataEntity_retentionClassification: Property = Property(name="retentionClassification", type=StringType)
contentfwk_DataEntity.attributes={contentfwk_DataEntity_retentionClassification, contentfwk_DataEntity_dataEntityCategory, contentfwk_DataEntity_privacyClassification}

# contentfwk_LogicalDataComponent class attributes and methods

# contentfwk_PhysicalDataComponent class attributes and methods

# contentfwk_TechnologyArchitecture class attributes and methods

# contentfwk_Service class attributes and methods

# contentfwk_LogicalApplicationComponent class attributes and methods

# contentfwk_PhysicalApplicationComponent class attributes and methods
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
contentfwk_PhysicalApplicationComponent_lifeCycleStatus: Property = Property(name="lifeCycleStatus", type=StringType)
contentfwk_PhysicalApplicationComponent_initialLiveDate: Property = Property(name="initialLiveDate", type=DateType)
contentfwk_PhysicalApplicationComponent_dateOfLastRelease: Property = Property(name="dateOfLastRelease", type=DateType)
contentfwk_PhysicalApplicationComponent.attributes={contentfwk_PhysicalApplicationComponent_localizationCharacteristics, contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics, contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics, contentfwk_PhysicalApplicationComponent_initialLiveDate, contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics, contentfwk_PhysicalApplicationComponent_throughput, contentfwk_PhysicalApplicationComponent_dateOfNextRelease, contentfwk_PhysicalApplicationComponent_servicesTimes, contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics, contentfwk_PhysicalApplicationComponent_portabilityCharacteristics, contentfwk_PhysicalApplicationComponent_integrityCharacteristics, contentfwk_PhysicalApplicationComponent_lifeCycleStatus, contentfwk_PhysicalApplicationComponent_growthPeriod, contentfwk_PhysicalApplicationComponent_performanceCharacteristics, contentfwk_PhysicalApplicationComponent_growth, contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileLongTerm, contentfwk_PhysicalApplicationComponent_dateOfLastRelease, contentfwk_PhysicalApplicationComponent_capacityCharacteristics, contentfwk_PhysicalApplicationComponent_throughputPeriod, contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics, contentfwk_PhysicalApplicationComponent_securityCharacteristics, contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileShortTerm, contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics, contentfwk_PhysicalApplicationComponent_credibilityCharacteristics, contentfwk_PhysicalApplicationComponent_retirementDate, contentfwk_PhysicalApplicationComponent_privacyCharacteristics, contentfwk_PhysicalApplicationComponent_availabilityQualityCharacteristics, contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics}

# Standard class attributes and methods

# ApplicationComponent class attributes and methods

# Service class attributes and methods

# TechnologyComponent class attributes and methods

# contentfwk_Element class attributes and methods
contentfwk_Element_name: Property = Property(name="name", type=StringType)
contentfwk_Element_description: Property = Property(name="description", type=StringType)
contentfwk_Element_category: Property = Property(name="category", type=StringType)
contentfwk_Element_sourceDescr: Property = Property(name="sourceDescr", type=StringType)
contentfwk_Element_ownerDescr: Property = Property(name="ownerDescr", type=StringType)
contentfwk_Element_ID: Property = Property(name="ID", type=StringType)
contentfwk_Element.attributes={contentfwk_Element_category, contentfwk_Element_description, contentfwk_Element_ownerDescr, contentfwk_Element_sourceDescr, contentfwk_Element_ID, contentfwk_Element_name}

# contentfwk_Capability class attributes and methods
contentfwk_Capability_businessValue: Property = Property(name="businessValue", type=StringType)
contentfwk_Capability_increments: Property = Property(name="increments", type=StringType)
contentfwk_Capability.attributes={contentfwk_Capability_businessValue, contentfwk_Capability_increments}

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
contentfwk_Principle.attributes={contentfwk_Principle_principleCategory, contentfwk_Principle_implication, contentfwk_Principle_metric, contentfwk_Principle_rationale, contentfwk_Principle_statementOfPrinciple, contentfwk_Principle_priority}

# StrategicElement class attributes and methods

# contentfwk_Constraint class attributes and methods

# contentfwk_Assumption class attributes and methods

# contentfwk_Requirement class attributes and methods
contentfwk_Requirement_statementOfRequirement: Property = Property(name="statementOfRequirement", type=StringType)
contentfwk_Requirement_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Requirement_acceptanceCriteria: Property = Property(name="acceptanceCriteria", type=StringType)
contentfwk_Requirement.attributes={contentfwk_Requirement_acceptanceCriteria, contentfwk_Requirement_statementOfRequirement, contentfwk_Requirement_rationale}

# DataComponent class attributes and methods

# contentfwk_ApplicationArchitecture class attributes and methods

# contentfwk_InformationSystemService class attributes and methods

# contentfwk_Gap class attributes and methods

# contentfwk_StrategicArchitecture class attributes and methods

# contentfwk_Standard class attributes and methods
contentfwk_Standard_standardClass: Property = Property(name="standardClass", type=StringType)
contentfwk_Standard_standardCreationDate: Property = Property(name="standardCreationDate", type=DateType)
contentfwk_Standard_lastStandardCreationDate: Property = Property(name="lastStandardCreationDate", type=DateType)
contentfwk_Standard_nextStandardCreationDate: Property = Property(name="nextStandardCreationDate", type=DateType)
contentfwk_Standard_retireDate: Property = Property(name="retireDate", type=StringType)
contentfwk_Standard.attributes={contentfwk_Standard_nextStandardCreationDate, contentfwk_Standard_lastStandardCreationDate, contentfwk_Standard_standardClass, contentfwk_Standard_retireDate, contentfwk_Standard_standardCreationDate}

# contentfwk_ApplicationComponent class attributes and methods

# contentfwk_DataComponent class attributes and methods

# contentfwk_TechnologyComponent class attributes and methods

# Relationships
drivers3: BinaryAssociation = BinaryAssociation(
    name="drivers3",
    ends={
        Property(name="contentfwk_Driver", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goals4: BinaryAssociation = BinaryAssociation(
    name="goals4",
    ends={
        Property(name="contentfwk_Goal", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture5", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectives6: BinaryAssociation = BinaryAssociation(
    name="objectives6",
    ends={
        Property(name="contentfwk_Objective", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture7", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units8: BinaryAssociation = BinaryAssociation(
    name="units8",
    ends={
        Property(name="contentfwk_OrganizationUnit", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture9", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors10: BinaryAssociation = BinaryAssociation(
    name="actors10",
    ends={
        Property(name="contentfwk_Actor", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture11", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roles12: BinaryAssociation = BinaryAssociation(
    name="roles12",
    ends={
        Property(name="contentfwk_Role", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture13", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions14: BinaryAssociation = BinaryAssociation(
    name="functions14",
    ends={
        Property(name="contentfwk_Function", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture15", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services16: BinaryAssociation = BinaryAssociation(
    name="services16",
    ends={
        Property(name="contentfwk_BusinessService", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture17", type=contentfwk_BusinessService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processes18: BinaryAssociation = BinaryAssociation(
    name="processes18",
    ends={
        Property(name="contentfwk_Process", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture19", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controls20: BinaryAssociation = BinaryAssociation(
    name="controls20",
    ends={
        Property(name="contentfwk_Control", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture21", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events22: BinaryAssociation = BinaryAssociation(
    name="events22",
    ends={
        Property(name="contentfwk_Event", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture23", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locations24: BinaryAssociation = BinaryAssociation(
    name="locations24",
    ends={
        Property(name="contentfwk_Location", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture25", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
products26: BinaryAssociation = BinaryAssociation(
    name="products26",
    ends={
        Property(name="contentfwk_Product", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture27", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contracts28: BinaryAssociation = BinaryAssociation(
    name="contracts28",
    ends={
        Property(name="contentfwk_Contract", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture29", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measures30: BinaryAssociation = BinaryAssociation(
    name="measures30",
    ends={
        Property(name="contentfwk_Measure", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture31", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servicesQuality32: BinaryAssociation = BinaryAssociation(
    name="servicesQuality32",
    ends={
        Property(name="contentfwk_ServiceQuality", type=contentfwk_BusinessArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessArchitecture33", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
architectures0: BinaryAssociation = BinaryAssociation(
    name="architectures0",
    ends={
        Property(name="contentfwk_Architecture", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_EnterpriseArchitecture", type=contentfwk_Architecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containers1: BinaryAssociation = BinaryAssociation(
    name="containers1",
    ends={
        Property(name="contentfwk_Container", type=contentfwk_EnterpriseArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_EnterpriseArchitecture2", type=contentfwk_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
platformServices39: BinaryAssociation = BinaryAssociation(
    name="platformServices39",
    ends={
        Property(name="contentfwk_PlatformService", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents40: BinaryAssociation = BinaryAssociation(
    name="physicalComponents40",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture41", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents42: BinaryAssociation = BinaryAssociation(
    name="logicalComponents42",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent", type=contentfwk_TechnologyArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_TechnologyArchitecture43", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createsGoals44: BinaryAssociation = BinaryAssociation(
    name="createsGoals44",
    ends={
        Property(name="45", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
motivatesOrganizationUnits46: BinaryAssociation = BinaryAssociation(
    name="motivatesOrganizationUnits46",
    ends={
        Property(name="48", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="47", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesDriver50: BinaryAssociation = BinaryAssociation(
    name="decomposesDriver50",
    ends={
        Property(name="contentfwk_Driver51", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Driver49", type=contentfwk_Driver, multiplicity=Multiplicity(0, 1))
    }
)
addressesDrivers52: BinaryAssociation = BinaryAssociation(
    name="addressesDrivers52",
    ends={
        Property(name="54", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="53", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughObjectives55: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughObjectives55",
    ends={
        Property(name="57", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="56", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesGoal59: BinaryAssociation = BinaryAssociation(
    name="decomposesGoal59",
    ends={
        Property(name="contentfwk_Goal60", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Goal58", type=contentfwk_Goal, multiplicity=Multiplicity(0, 1))
    }
)
realizesGoals61: BinaryAssociation = BinaryAssociation(
    name="realizesGoals61",
    ends={
        Property(name="63", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="62", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures64: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures64",
    ends={
        Property(name="66", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="65", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesObjective68: BinaryAssociation = BinaryAssociation(
    name="decomposesObjective68",
    ends={
        Property(name="contentfwk_Objective69", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Objective67", type=contentfwk_Objective, multiplicity=Multiplicity(0, 1))
    }
)
entities34: BinaryAssociation = BinaryAssociation(
    name="entities34",
    ends={
        Property(name="contentfwk_DataEntity", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalComponents35: BinaryAssociation = BinaryAssociation(
    name="logicalComponents35",
    ends={
        Property(name="contentfwk_LogicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture36", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalComponents37: BinaryAssociation = BinaryAssociation(
    name="physicalComponents37",
    ends={
        Property(name="contentfwk_PhysicalDataComponent", type=contentfwk_DataArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataArchitecture38", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isMotivatedByDrivers82: BinaryAssociation = BinaryAssociation(
    name="isMotivatedByDrivers82",
    ends={
        Property(name="84", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="83", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts85: BinaryAssociation = BinaryAssociation(
    name="producesProducts85",
    ends={
        Property(name="87", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="86", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation88: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation88",
    ends={
        Property(name="90", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="89", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
suppliesEntities91: BinaryAssociation = BinaryAssociation(
    name="suppliesEntities91",
    ends={
        Property(name="93", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="92", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities94: BinaryAssociation = BinaryAssociation(
    name="consumesEntities94",
    ends={
        Property(name="96", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="95", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo97: BinaryAssociation = BinaryAssociation(
    name="belongsTo97",
    ends={
        Property(name="99", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="98", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
interactsWithFunctions100: BinaryAssociation = BinaryAssociation(
    name="interactsWithFunctions100",
    ends={
        Property(name="102", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="101", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
performsTaskInRoles103: BinaryAssociation = BinaryAssociation(
    name="performsTaskInRoles103",
    ends={
        Property(name="105", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="104", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses106: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses106",
    ends={
        Property(name="108", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="107", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices109: BinaryAssociation = BinaryAssociation(
    name="consumesServices109",
    ends={
        Property(name="contentfwk_Service", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor110", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents111: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents111",
    ends={
        Property(name="113", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="112", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents114: BinaryAssociation = BinaryAssociation(
    name="generatesEvents114",
    ends={
        Property(name="116", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="115", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation117: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation117",
    ends={
        Property(name="119", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="118", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
ownsAndGovernsServices70: BinaryAssociation = BinaryAssociation(
    name="ownsAndGovernsServices70",
    ends={
        Property(name="72", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="71", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors73: BinaryAssociation = BinaryAssociation(
    name="containsActors73",
    ends={
        Property(name="75", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="74", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
ownsFunctions76: BinaryAssociation = BinaryAssociation(
    name="ownsFunctions76",
    ends={
        Property(name="78", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="77", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses79: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses79",
    ends={
        Property(name="81", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="80", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
performsFunctions120: BinaryAssociation = BinaryAssociation(
    name="performsFunctions120",
    ends={
        Property(name="122", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="121", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesActors124: BinaryAssociation = BinaryAssociation(
    name="decomposesActors124",
    ends={
        Property(name="contentfwk_Actor125", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor123", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAssumedByActors126: BinaryAssociation = BinaryAssociation(
    name="isAssumedByActors126",
    ends={
        Property(name="128", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="127", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
accessesFunctions129: BinaryAssociation = BinaryAssociation(
    name="accessesFunctions129",
    ends={
        Property(name="131", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="130", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesRole133: BinaryAssociation = BinaryAssociation(
    name="decomposesRole133",
    ends={
        Property(name="contentfwk_Role134", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Role132", type=contentfwk_Role, multiplicity=Multiplicity(0, 1))
    }
)
isSuppliedByActors135: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByActors135",
    ends={
        Property(name="137", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="136", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isConsumedByActors138: BinaryAssociation = BinaryAssociation(
    name="isConsumedByActors138",
    ends={
        Property(name="140", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="139", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAccessedByServices141: BinaryAssociation = BinaryAssociation(
    name="isAccessedByServices141",
    ends={
        Property(name="143", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="142", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isUpdatedThroughServices144: BinaryAssociation = BinaryAssociation(
    name="isUpdatedThroughServices144",
    ends={
        Property(name="146", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="145", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
residesWithinLogicalDataComponent147: BinaryAssociation = BinaryAssociation(
    name="residesWithinLogicalDataComponent147",
    ends={
        Property(name="149", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="148", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
isProcessesByLogicalApplicationComponents150: BinaryAssociation = BinaryAssociation(
    name="isProcessesByLogicalApplicationComponents150",
    ends={
        Property(name="152", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="151", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
implementsServices159: BinaryAssociation = BinaryAssociation(
    name="implementsServices159",
    ends={
        Property(name="161", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="160", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
operatesOnDataEntities162: BinaryAssociation = BinaryAssociation(
    name="operatesOnDataEntities162",
    ends={
        Property(name="164", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="163", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalApplicationComponents165: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalApplicationComponents165",
    ends={
        Property(name="167", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="166", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith169: BinaryAssociation = BinaryAssociation(
    name="communicatesWith169",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent168", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalApplicationComponent171: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalApplicationComponent171",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent172", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent170", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
isPerformedByActors173: BinaryAssociation = BinaryAssociation(
    name="isPerformedByActors173",
    ends={
        Property(name="175", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="174", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedByUnit176: BinaryAssociation = BinaryAssociation(
    name="isOwnedByUnit176",
    ends={
        Property(name="178", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="177", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
isBoundedByServices179: BinaryAssociation = BinaryAssociation(
    name="isBoundedByServices179",
    ends={
        Property(name="181", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="180", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses182: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses182",
    ends={
        Property(name="184", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="183", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses185: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses185",
    ends={
        Property(name="187", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="186", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
canBeAccessedByRoles188: BinaryAssociation = BinaryAssociation(
    name="canBeAccessedByRoles188",
    ends={
        Property(name="190", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="189", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
supportsActors191: BinaryAssociation = BinaryAssociation(
    name="supportsActors191",
    ends={
        Property(name="193", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="192", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunction195: BinaryAssociation = BinaryAssociation(
    name="decomposesFunction195",
    ends={
        Property(name="contentfwk_Function196", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function194", type=contentfwk_Function, multiplicity=Multiplicity(0, 1))
    }
)
communicatedWithFunctions198: BinaryAssociation = BinaryAssociation(
    name="communicatedWithFunctions198",
    ends={
        Property(name="contentfwk_Function199", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function197", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposeEntity154: BinaryAssociation = BinaryAssociation(
    name="decomposeEntity154",
    ends={
        Property(name="contentfwk_DataEntity155", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity153", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 1))
    }
)
relatesTo157: BinaryAssociation = BinaryAssociation(
    name="relatesTo157",
    ends={
        Property(name="contentfwk_DataEntity158", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity156", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesFunctions203: BinaryAssociation = BinaryAssociation(
    name="orchestratesFunctions203",
    ends={
        Property(name="205", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="204", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunctions206: BinaryAssociation = BinaryAssociation(
    name="decomposesFunctions206",
    ends={
        Property(name="208", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="207", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
involvesOrganizationUnits209: BinaryAssociation = BinaryAssociation(
    name="involvesOrganizationUnits209",
    ends={
        Property(name="211", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="210", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesServices212: BinaryAssociation = BinaryAssociation(
    name="orchestratesServices212",
    ends={
        Property(name="214", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="213", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices215: BinaryAssociation = BinaryAssociation(
    name="decomposesServices215",
    ends={
        Property(name="217", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="216", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
involvesActors218: BinaryAssociation = BinaryAssociation(
    name="involvesActors218",
    ends={
        Property(name="220", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="219", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGuidedByControls221: BinaryAssociation = BinaryAssociation(
    name="isGuidedByControls221",
    ends={
        Property(name="223", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="222", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents224: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents224",
    ends={
        Property(name="226", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="225", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents227: BinaryAssociation = BinaryAssociation(
    name="generatesEvents227",
    ends={
        Property(name="229", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="228", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts230: BinaryAssociation = BinaryAssociation(
    name="producesProducts230",
    ends={
        Property(name="232", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="231", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesProcess234: BinaryAssociation = BinaryAssociation(
    name="decomposesProcess234",
    ends={
        Property(name="contentfwk_Process235", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Process233", type=contentfwk_Process, multiplicity=Multiplicity(0, 1))
    }
)
precedesProcesses237: BinaryAssociation = BinaryAssociation(
    name="precedesProcesses237",
    ends={
        Property(name="239", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="238", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
followsProcesses241: BinaryAssociation = BinaryAssociation(
    name="followsProcesses241",
    ends={
        Property(name="243", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="242", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
supportsObjective200: BinaryAssociation = BinaryAssociation(
    name="supportsObjective200",
    ends={
        Property(name="contentfwk_Objective202", type=contentfwk_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessService201", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
realizesApplicationComponents247: BinaryAssociation = BinaryAssociation(
    name="realizesApplicationComponents247",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent248", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalTechnologyComponents249: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalTechnologyComponents249",
    ends={
        Property(name="251", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="250", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation252: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation252",
    ends={
        Property(name="254", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="253", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalTechnologyComponent256: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalTechnologyComponent256",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent257", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent255", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnPhysicalTechnologyComponents259: BinaryAssociation = BinaryAssociation(
    name="isDependentOnPhysicalTechnologyComponents259",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent260", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent258", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByOrganizationUnits261: BinaryAssociation = BinaryAssociation(
    name="isProducedByOrganizationUnits261",
    ends={
        Property(name="263", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="262", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByProcesses264: BinaryAssociation = BinaryAssociation(
    name="isProducedByProcesses264",
    ends={
        Property(name="266", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="265", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForObjectives267: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForObjectives267",
    ends={
        Property(name="269", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="268", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForServices270: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForServices270",
    ends={
        Property(name="272", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="271", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesMeasure274: BinaryAssociation = BinaryAssociation(
    name="decomposesMeasure274",
    ends={
        Property(name="contentfwk_Measure275", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Measure273", type=contentfwk_Measure, multiplicity=Multiplicity(0, 1))
    }
)
appliesToServices276: BinaryAssociation = BinaryAssociation(
    name="appliesToServices276",
    ends={
        Property(name="278", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="277", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToContracts279: BinaryAssociation = BinaryAssociation(
    name="appliesToContracts279",
    ends={
        Property(name="281", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="280", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
governsAndMeasuresBusinessServices282: BinaryAssociation = BinaryAssociation(
    name="governsAndMeasuresBusinessServices282",
    ends={
        Property(name="284", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="283", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isSuppliedByLogicalTechnologyComponents244: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByLogicalTechnologyComponents244",
    ends={
        Property(name="246", type=contentfwk_PlatformService, multiplicity=Multiplicity(1, 1)),
        Property(name="245", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
meetsServiceQuality285: BinaryAssociation = BinaryAssociation(
    name="meetsServiceQuality285",
    ends={
        Property(name="287", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="286", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByBusinessServices288: BinaryAssociation = BinaryAssociation(
    name="isResolvedByBusinessServices288",
    ends={
        Property(name="290", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="289", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByProcesses291: BinaryAssociation = BinaryAssociation(
    name="isResolvedByProcesses291",
    ends={
        Property(name="293", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="292", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByProcesses294: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByProcesses294",
    ends={
        Property(name="296", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="295", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByActors297: BinaryAssociation = BinaryAssociation(
    name="isResolvedByActors297",
    ends={
        Property(name="299", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="298", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByActors300: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByActors300",
    ends={
        Property(name="302", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="301", type=contentfwk_Actor, multiplicity=Multiplicity(0, 1))
    }
)
ensuresCorrectOperationOfProcesses303: BinaryAssociation = BinaryAssociation(
    name="ensuresCorrectOperationOfProcesses303",
    ends={
        Property(name="305", type=contentfwk_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="304", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
delegates307: BinaryAssociation = BinaryAssociation(
    name="delegates307",
    ends={
        Property(name="309", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="308", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isDelegatedBy311: BinaryAssociation = BinaryAssociation(
    name="isDelegatedBy311",
    ends={
        Property(name="313", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="312", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
containsOrganizationUnits319: BinaryAssociation = BinaryAssociation(
    name="containsOrganizationUnits319",
    ends={
        Property(name="321", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="320", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalDataComponents322: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalDataComponents322",
    ends={
        Property(name="324", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="323", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalApplicationComponents325: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalApplicationComponents325",
    ends={
        Property(name="327", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="326", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalTechnologyComponents328: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalTechnologyComponents328",
    ends={
        Property(name="330", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="329", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLocation332: BinaryAssociation = BinaryAssociation(
    name="decomposesLocation332",
    ends={
        Property(name="contentfwk_Location333", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Location331", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
isDeliveredBy334: BinaryAssociation = BinaryAssociation(
    name="isDeliveredBy334",
    ends={
        Property(name="336", type=contentfwk_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="335", type=contentfwk_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
ownsElements314: BinaryAssociation = BinaryAssociation(
    name="ownsElements314",
    ends={
        Property(name="contentfwk_Element", type=contentfwk_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Container315", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors316: BinaryAssociation = BinaryAssociation(
    name="containsActors316",
    ends={
        Property(name="318", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="317", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
deliversCapabilities337: BinaryAssociation = BinaryAssociation(
    name="deliversCapabilities337",
    ends={
        Property(name="339", type=contentfwk_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="338", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesDataEntities340: BinaryAssociation = BinaryAssociation(
    name="encapsulatesDataEntities340",
    ends={
        Property(name="342", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="341", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalDataComponents343: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalDataComponents343",
    ends={
        Property(name="345", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="344", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalDataComponents346: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalDataComponents346",
    ends={
        Property(name="348", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="347", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHotedInLocation349: BinaryAssociation = BinaryAssociation(
    name="isHotedInLocation349",
    ends={
        Property(name="351", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="350", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
decomposesPhysicalDataComponent353: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalDataComponent353",
    ends={
        Property(name="contentfwk_PhysicalDataComponent354", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent352", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatesPhysicalApplicationComponents355: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalApplicationComponents355",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent357", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent356", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
logicalApplicationComponents358: BinaryAssociation = BinaryAssociation(
    name="logicalApplicationComponents358",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent359", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalApplicationComponents360: BinaryAssociation = BinaryAssociation(
    name="physicalApplicationComponents360",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent362", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture361", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informationSystemServices363: BinaryAssociation = BinaryAssociation(
    name="informationSystemServices363",
    ends={
        Property(name="contentfwk_InformationSystemService", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture364", type=contentfwk_InformationSystemService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsLogicalApplicationComponents365: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalApplicationComponents365",
    ends={
        Property(name="367", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="366", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation368: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation368",
    ends={
        Property(name="370", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="369", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesPhysicalDataComponents374: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalDataComponents374",
    ends={
        Property(name="contentfwk_PhysicalDataComponent376", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent375", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents377: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents377",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent379", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent378", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
communicatesWith372: BinaryAssociation = BinaryAssociation(
    name="communicatesWith372",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent373", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent371", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents389: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents389",
    ends={
        Property(name="391", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="390", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalTechnologyComponent393: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalTechnologyComponent393",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent394", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent392", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnLogicalTechnologyComponents396: BinaryAssociation = BinaryAssociation(
    name="isDependentOnLogicalTechnologyComponents396",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent397", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent395", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
capabilities398: BinaryAssociation = BinaryAssociation(
    name="capabilities398",
    ends={
        Property(name="contentfwk_Capability", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strategicElements399: BinaryAssociation = BinaryAssociation(
    name="strategicElements399",
    ends={
        Property(name="contentfwk_StrategicElement", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture400", type=contentfwk_StrategicElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isProvidedToActors401: BinaryAssociation = BinaryAssociation(
    name="isProvidedToActors401",
    ends={
        Property(name="contentfwk_Actor403", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service402", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
providesGovernedInterfaceToAccessFunctions404: BinaryAssociation = BinaryAssociation(
    name="providesGovernedInterfaceToAccessFunctions404",
    ends={
        Property(name="406", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="405", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalApplicationComponent381: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalApplicationComponent381",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent382", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent380", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
providesPlatformForServices383: BinaryAssociation = BinaryAssociation(
    name="providesPlatformForServices383",
    ends={
        Property(name="385", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="384", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
suppliesPlatformServices386: BinaryAssociation = BinaryAssociation(
    name="suppliesPlatformServices386",
    ends={
        Property(name="388", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="387", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999))
    }
)
isImplementedOnLogicalTechnologyComponents419: BinaryAssociation = BinaryAssociation(
    name="isImplementedOnLogicalTechnologyComponents419",
    ends={
        Property(name="421", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="420", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughLogicalApplicationComponent422: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughLogicalApplicationComponent422",
    ends={
        Property(name="424", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="423", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedAndGovernedByOrganizationUnits425: BinaryAssociation = BinaryAssociation(
    name="isOwnedAndGovernedByOrganizationUnits425",
    ends={
        Property(name="427", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="426", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures428: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures428",
    ends={
        Property(name="430", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="429", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses431: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses431",
    ends={
        Property(name="433", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="432", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses434: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses434",
    ends={
        Property(name="436", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="435", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
meetsQualities437: BinaryAssociation = BinaryAssociation(
    name="meetsQualities437",
    ends={
        Property(name="439", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="438", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices441: BinaryAssociation = BinaryAssociation(
    name="consumesServices441",
    ends={
        Property(name="contentfwk_Service442", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service440", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices444: BinaryAssociation = BinaryAssociation(
    name="decomposesServices444",
    ends={
        Property(name="contentfwk_Service445", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service443", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
providesEntities407: BinaryAssociation = BinaryAssociation(
    name="providesEntities407",
    ends={
        Property(name="409", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="408", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities410: BinaryAssociation = BinaryAssociation(
    name="consumesEntities410",
    ends={
        Property(name="412", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="411", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isGovernedAndMeasuredByContracts413: BinaryAssociation = BinaryAssociation(
    name="isGovernedAndMeasuredByContracts413",
    ends={
        Property(name="415", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="414", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents416: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents416",
    ends={
        Property(name="418", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="417", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_contentfwk_BusinessArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_BusinessArchitecture)
gen_contentfwk_Driver_Element = Generalization(general=Element, specific=contentfwk_Driver)
gen_contentfwk_Goal_Element = Generalization(general=Element, specific=contentfwk_Goal)
gen_contentfwk_Objective_Element = Generalization(general=Element, specific=contentfwk_Objective)
gen_contentfwk_OrganizationUnit_Element = Generalization(general=Element, specific=contentfwk_OrganizationUnit)
gen_contentfwk_DataArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_DataArchitecture)
gen_contentfwk_TechnologyArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_TechnologyArchitecture)
gen_contentfwk_Actor_Element = Generalization(general=Element, specific=contentfwk_Actor)
gen_contentfwk_Role_Element = Generalization(general=Element, specific=contentfwk_Role)
gen_contentfwk_DataEntity_Element = Generalization(general=Element, specific=contentfwk_DataEntity)
gen_contentfwk_Function_Element = Generalization(general=Element, specific=contentfwk_Function)
gen_contentfwk_Function_Standard = Generalization(general=Standard, specific=contentfwk_Function)
gen_contentfwk_LogicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_LogicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_Process_Element = Generalization(general=Element, specific=contentfwk_Process)
gen_contentfwk_Process_Standard = Generalization(general=Standard, specific=contentfwk_Process)
gen_contentfwk_BusinessService_Element = Generalization(general=Element, specific=contentfwk_BusinessService)
gen_contentfwk_BusinessService_Service = Generalization(general=Service, specific=contentfwk_BusinessService)
gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_Product_Element = Generalization(general=Element, specific=contentfwk_Product)
gen_contentfwk_Measure_Element = Generalization(general=Element, specific=contentfwk_Measure)
gen_contentfwk_ServiceQuality_Element = Generalization(general=Element, specific=contentfwk_ServiceQuality)
gen_contentfwk_Contract_Element = Generalization(general=Element, specific=contentfwk_Contract)
gen_contentfwk_PlatformService_Element = Generalization(general=Element, specific=contentfwk_PlatformService)
gen_contentfwk_PlatformService_Service = Generalization(general=Service, specific=contentfwk_PlatformService)
gen_contentfwk_PhysicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_Event_Element = Generalization(general=Element, specific=contentfwk_Event)
gen_contentfwk_Control_Element = Generalization(general=Element, specific=contentfwk_Control)
gen_contentfwk_Capability_Element = Generalization(general=Element, specific=contentfwk_Capability)
gen_contentfwk_StrategicElement_Element = Generalization(general=Element, specific=contentfwk_StrategicElement)
gen_contentfwk_Principle_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Principle)
gen_contentfwk_Constraint_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Constraint)
gen_contentfwk_Assumption_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Assumption)
gen_contentfwk_Requirement_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Requirement)
gen_contentfwk_Location_Element = Generalization(general=Element, specific=contentfwk_Location)
gen_contentfwk_WorkPackage_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_WorkPackage)
gen_contentfwk_LogicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_LogicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_PhysicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_PhysicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_ApplicationArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_ApplicationArchitecture)
gen_contentfwk_PhysicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_Gap_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Gap)
gen_contentfwk_StrategicArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_StrategicArchitecture)
gen_contentfwk_Service_Standard = Generalization(general=Standard, specific=contentfwk_Service)
gen_contentfwk_LogicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_ApplicationComponent_Standard = Generalization(general=Standard, specific=contentfwk_ApplicationComponent)
gen_contentfwk_InformationSystemService_Service = Generalization(general=Service, specific=contentfwk_InformationSystemService)
gen_contentfwk_InformationSystemService_Element = Generalization(general=Element, specific=contentfwk_InformationSystemService)
gen_contentfwk_DataComponent_Standard = Generalization(general=Standard, specific=contentfwk_DataComponent)
gen_contentfwk_TechnologyComponent_Standard = Generalization(general=Standard, specific=contentfwk_TechnologyComponent)

# Domain Model
domain_model = DomainModel(
    name="contentfwk",
    types={contentfwk_EnterpriseArchitecture, contentfwk_Architecture, contentfwk_BusinessArchitecture, Architecture, contentfwk_Driver, contentfwk_Goal, contentfwk_Objective, contentfwk_OrganizationUnit, contentfwk_Actor, contentfwk_Role, contentfwk_Function, contentfwk_BusinessService, contentfwk_Process, contentfwk_Control, contentfwk_Event, contentfwk_Location, contentfwk_Product, contentfwk_Contract, contentfwk_Measure, contentfwk_ServiceQuality, contentfwk_Container, contentfwk_PlatformService, contentfwk_PhysicalTechnologyComponent, contentfwk_LogicalTechnologyComponent, Element, contentfwk_DataArchitecture, contentfwk_DataEntity, contentfwk_LogicalDataComponent, contentfwk_PhysicalDataComponent, contentfwk_TechnologyArchitecture, contentfwk_Service, contentfwk_LogicalApplicationComponent, contentfwk_PhysicalApplicationComponent, Standard, ApplicationComponent, Service, TechnologyComponent, contentfwk_Element, contentfwk_Capability, contentfwk_WorkPackage, contentfwk_StrategicElement, contentfwk_Principle, StrategicElement, contentfwk_Constraint, contentfwk_Assumption, contentfwk_Requirement, DataComponent, contentfwk_ApplicationArchitecture, contentfwk_InformationSystemService, contentfwk_Gap, contentfwk_StrategicArchitecture, contentfwk_Standard, contentfwk_ApplicationComponent, contentfwk_DataComponent, contentfwk_TechnologyComponent, PrincipleCategory, StandardsClass, LifeCycleStatus, DataEntityCategory, WorkPackageCategory},
    associations={drivers3, goals4, objectives6, units8, actors10, roles12, functions14, services16, processes18, controls20, events22, locations24, products26, contracts28, measures30, servicesQuality32, architectures0, containers1, platformServices39, physicalComponents40, logicalComponents42, createsGoals44, motivatesOrganizationUnits46, decomposesDriver50, addressesDrivers52, isRealizedThroughObjectives55, decomposesGoal59, realizesGoals61, isTrackedAgainstMeasures64, decomposesObjective68, entities34, logicalComponents35, physicalComponents37, isMotivatedByDrivers82, producesProducts85, operatesInLocation88, suppliesEntities91, consumesEntities94, belongsTo97, interactsWithFunctions100, performsTaskInRoles103, participatesInProcesses106, consumesServices109, resolvesEvents111, generatesEvents114, operatesInLocation117, ownsAndGovernsServices70, containsActors73, ownsFunctions76, participatesInProcesses79, performsFunctions120, decomposesActors124, isAssumedByActors126, accessesFunctions129, decomposesRole133, isSuppliedByActors135, isConsumedByActors138, isAccessedByServices141, isUpdatedThroughServices144, residesWithinLogicalDataComponent147, isProcessesByLogicalApplicationComponents150, implementsServices159, operatesOnDataEntities162, isExtendedByPhysicalApplicationComponents165, communicatesWith169, decomposesLogicalApplicationComponent171, isPerformedByActors173, isOwnedByUnit176, isBoundedByServices179, supportsProcesses182, isRealizedByProcesses185, canBeAccessedByRoles188, supportsActors191, decomposesFunction195, communicatedWithFunctions198, decomposeEntity154, relatesTo157, orchestratesFunctions203, decomposesFunctions206, involvesOrganizationUnits209, orchestratesServices212, decomposesServices215, involvesActors218, isGuidedByControls221, resolvesEvents224, generatesEvents227, producesProducts230, decomposesProcess234, precedesProcesses237, followsProcesses241, supportsObjective200, realizesApplicationComponents247, extendsLogicalTechnologyComponents249, isHostedInLocation252, decomposesPhysicalTechnologyComponent256, isDependentOnPhysicalTechnologyComponents259, isProducedByOrganizationUnits261, isProducedByProcesses264, setsPerformanceCriteriaForObjectives267, setsPerformanceCriteriaForServices270, decomposesMeasure274, appliesToServices276, appliesToContracts279, governsAndMeasuresBusinessServices282, isSuppliedByLogicalTechnologyComponents244, meetsServiceQuality285, isResolvedByBusinessServices288, isResolvedByProcesses291, isGeneratedByProcesses294, isResolvedByActors297, isGeneratedByActors300, ensuresCorrectOperationOfProcesses303, delegates307, isDelegatedBy311, containsOrganizationUnits319, containsPhysicalDataComponents322, containsPhysicalApplicationComponents325, containsPhysicalTechnologyComponents328, decomposesLocation332, isDeliveredBy334, ownsElements314, containsActors316, deliversCapabilities337, encapsulatesDataEntities340, isExtendedByPhysicalDataComponents343, extendsLogicalDataComponents346, isHotedInLocation349, decomposesPhysicalDataComponent353, encapsulatesPhysicalApplicationComponents355, logicalApplicationComponents358, physicalApplicationComponents360, informationSystemServices363, extendsLogicalApplicationComponents365, isHostedInLocation368, encapsulatesPhysicalDataComponents374, isRealizedByPhysicalTechnologyComponents377, communicatesWith372, isRealizedByPhysicalTechnologyComponents389, decomposesLogicalTechnologyComponent393, isDependentOnLogicalTechnologyComponents396, capabilities398, strategicElements399, isProvidedToActors401, providesGovernedInterfaceToAccessFunctions404, decomposesPhysicalApplicationComponent381, providesPlatformForServices383, suppliesPlatformServices386, isImplementedOnLogicalTechnologyComponents419, isRealizedThroughLogicalApplicationComponent422, isOwnedAndGovernedByOrganizationUnits425, isTrackedAgainstMeasures428, supportsProcesses431, isRealizedByProcesses434, meetsQualities437, consumesServices441, decomposesServices444, providesEntities407, consumesEntities410, isGovernedAndMeasuredByContracts413, resolvesEvents416},
    generalizations={gen_contentfwk_BusinessArchitecture_Architecture, gen_contentfwk_Driver_Element, gen_contentfwk_Goal_Element, gen_contentfwk_Objective_Element, gen_contentfwk_OrganizationUnit_Element, gen_contentfwk_DataArchitecture_Architecture, gen_contentfwk_TechnologyArchitecture_Architecture, gen_contentfwk_Actor_Element, gen_contentfwk_Role_Element, gen_contentfwk_DataEntity_Element, gen_contentfwk_Function_Element, gen_contentfwk_Function_Standard, gen_contentfwk_LogicalApplicationComponent_Element, gen_contentfwk_LogicalApplicationComponent_ApplicationComponent, gen_contentfwk_Process_Element, gen_contentfwk_Process_Standard, gen_contentfwk_BusinessService_Element, gen_contentfwk_BusinessService_Service, gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent, gen_contentfwk_Product_Element, gen_contentfwk_Measure_Element, gen_contentfwk_ServiceQuality_Element, gen_contentfwk_Contract_Element, gen_contentfwk_PlatformService_Element, gen_contentfwk_PlatformService_Service, gen_contentfwk_PhysicalTechnologyComponent_Element, gen_contentfwk_Event_Element, gen_contentfwk_Control_Element, gen_contentfwk_Capability_Element, gen_contentfwk_StrategicElement_Element, gen_contentfwk_Principle_StrategicElement, gen_contentfwk_Constraint_StrategicElement, gen_contentfwk_Assumption_StrategicElement, gen_contentfwk_Requirement_StrategicElement, gen_contentfwk_Location_Element, gen_contentfwk_WorkPackage_StrategicElement, gen_contentfwk_LogicalDataComponent_Element, gen_contentfwk_LogicalDataComponent_DataComponent, gen_contentfwk_PhysicalDataComponent_Element, gen_contentfwk_PhysicalDataComponent_DataComponent, gen_contentfwk_ApplicationArchitecture_Architecture, gen_contentfwk_PhysicalApplicationComponent_Element, gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent, gen_contentfwk_Gap_StrategicElement, gen_contentfwk_StrategicArchitecture_Architecture, gen_contentfwk_Service_Standard, gen_contentfwk_LogicalTechnologyComponent_Element, gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent, gen_contentfwk_ApplicationComponent_Standard, gen_contentfwk_InformationSystemService_Service, gen_contentfwk_InformationSystemService_Element, gen_contentfwk_DataComponent_Standard, gen_contentfwk_TechnologyComponent_Standard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)