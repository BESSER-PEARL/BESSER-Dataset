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

# Classes
contentfwk_Container = Class(name="contentfwk_Container")
contentfwk_BusinessArchitecture = Class(name="contentfwk_BusinessArchitecture")
Architecture = Class(name="Architecture")
contentfwk_Driver = Class(name="contentfwk_Driver")
contentfwk_Goal = Class(name="contentfwk_Goal")
contentfwk_Objective = Class(name="contentfwk_Objective")
contentfwk_OrganizationUnit = Class(name="contentfwk_OrganizationUnit")
contentfwk_Actor = Class(name="contentfwk_Actor")
contentfwk_EnterpriseArchitecture = Class(name="contentfwk_EnterpriseArchitecture")
contentfwk_Architecture = Class(name="contentfwk_Architecture", is_abstract=True)
contentfwk_Product = Class(name="contentfwk_Product")
contentfwk_Contract = Class(name="contentfwk_Contract")
contentfwk_Measure = Class(name="contentfwk_Measure")
contentfwk_ServiceQuality = Class(name="contentfwk_ServiceQuality")
contentfwk_DataArchitecture = Class(name="contentfwk_DataArchitecture")
contentfwk_DataEntity = Class(name="contentfwk_DataEntity")
contentfwk_LogicalDataComponent = Class(name="contentfwk_LogicalDataComponent")
contentfwk_PhysicalDataComponent = Class(name="contentfwk_PhysicalDataComponent")
contentfwk_TechnologyArchitecture = Class(name="contentfwk_TechnologyArchitecture")
contentfwk_PlatformService = Class(name="contentfwk_PlatformService")
contentfwk_PhysicalTechnologyComponent = Class(name="contentfwk_PhysicalTechnologyComponent")
contentfwk_Role = Class(name="contentfwk_Role")
contentfwk_Function = Class(name="contentfwk_Function")
contentfwk_BusinessService = Class(name="contentfwk_BusinessService")
contentfwk_Process = Class(name="contentfwk_Process")
contentfwk_Control = Class(name="contentfwk_Control")
contentfwk_Event = Class(name="contentfwk_Event")
contentfwk_Location = Class(name="contentfwk_Location")
contentfwk_Service = Class(name="contentfwk_Service", is_abstract=True)
contentfwk_LogicalTechnologyComponent = Class(name="contentfwk_LogicalTechnologyComponent")
Element = Class(name="Element")
contentfwk_LogicalApplicationComponent = Class(name="contentfwk_LogicalApplicationComponent")
Standard = Class(name="Standard")
ApplicationComponent = Class(name="ApplicationComponent")
contentfwk_PhysicalApplicationComponent = Class(name="contentfwk_PhysicalApplicationComponent")
Service = Class(name="Service")
TechnologyComponent = Class(name="TechnologyComponent")
contentfwk_Element = Class(name="contentfwk_Element")
contentfwk_Constraint = Class(name="contentfwk_Constraint")
contentfwk_Assumption = Class(name="contentfwk_Assumption")
contentfwk_Requirement = Class(name="contentfwk_Requirement")
contentfwk_Gap = Class(name="contentfwk_Gap")
contentfwk_Capability = Class(name="contentfwk_Capability")
contentfwk_WorkPackage = Class(name="contentfwk_WorkPackage")
contentfwk_StrategicElement = Class(name="contentfwk_StrategicElement", is_abstract=True)
contentfwk_Principle = Class(name="contentfwk_Principle")
StrategicElement = Class(name="StrategicElement")
contentfwk_ApplicationArchitecture = Class(name="contentfwk_ApplicationArchitecture")
contentfwk_InformationSystemService = Class(name="contentfwk_InformationSystemService")
DataComponent = Class(name="DataComponent")
contentfwk_StrategicArchitecture = Class(name="contentfwk_StrategicArchitecture")
contentfwk_Standard = Class(name="contentfwk_Standard", is_abstract=True)
contentfwk_TechnologyComponent = Class(name="contentfwk_TechnologyComponent", is_abstract=True)
contentfwk_ApplicationComponent = Class(name="contentfwk_ApplicationComponent", is_abstract=True)
contentfwk_DataComponent = Class(name="contentfwk_DataComponent", is_abstract=True)

# contentfwk_Container class attributes and methods
contentfwk_Container_name: Property = Property(name="name", type=StringType)
contentfwk_Container.attributes={contentfwk_Container_name}

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
contentfwk_Actor.attributes={contentfwk_Actor_FTEs, contentfwk_Actor_actorGoal, contentfwk_Actor_actorTasks}

# contentfwk_EnterpriseArchitecture class attributes and methods

# contentfwk_Architecture class attributes and methods

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
contentfwk_Contract_behaviorCharacteristics: Property = Property(name="behaviorCharacteristics", type=StringType)
contentfwk_Contract_ServiceNameCaller: Property = Property(name="ServiceNameCaller", type=StringType)
contentfwk_Contract_peakProfileShortTerm: Property = Property(name="peakProfileShortTerm", type=StringType)
contentfwk_Contract_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
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
contentfwk_Contract.attributes={contentfwk_Contract_resultControlRequirements, contentfwk_Contract_recoverabilityCharacteristics, contentfwk_Contract_extensibilityCharacteristics, contentfwk_Contract_integrityCharacteristics, contentfwk_Contract_interoperabilityCharacteristics, contentfwk_Contract_serviceabilityCharacteristics, contentfwk_Contract_securityCharacteristics, contentfwk_Contract_availabilityQualityCharacteristics, contentfwk_Contract_locatabilityCharacteristics, contentfwk_Contract_servicesTimes, contentfwk_Contract_reliabilityCharacteristics, contentfwk_Contract_privacyCharacteristics, contentfwk_Contract_localizationCharacteristics, contentfwk_Contract_ServiceNameCaller, contentfwk_Contract_portabilityCharacteristics, contentfwk_Contract_internationalizationCharacteristics, contentfwk_Contract_ServiceNameCalled, contentfwk_Contract_throughput, contentfwk_Contract_credibilityCharacteristics, contentfwk_Contract_responseCharacteristics, contentfwk_Contract_performanceCharacteristics, contentfwk_Contract_growth, contentfwk_Contract_qualityOfInformationRequired, contentfwk_Contract_capacityCharacteristics, contentfwk_Contract_behaviorCharacteristics, contentfwk_Contract_serviceQualityCharacteristics, contentfwk_Contract_peakProfileLongTerm, contentfwk_Contract_manageabilityCharacteristics, contentfwk_Contract_growthPeriod, contentfwk_Contract_peakProfileShortTerm, contentfwk_Contract_scalabilityCharacteristics, contentfwk_Contract_contractControlRequirements, contentfwk_Contract_throughputPeriod}

# contentfwk_Measure class attributes and methods

# contentfwk_ServiceQuality class attributes and methods

# contentfwk_DataArchitecture class attributes and methods

# contentfwk_DataEntity class attributes and methods
contentfwk_DataEntity_dataEntityCategory: Property = Property(name="dataEntityCategory", type=StringType)
contentfwk_DataEntity_privacyClassification: Property = Property(name="privacyClassification", type=StringType)
contentfwk_DataEntity_retentionClassification: Property = Property(name="retentionClassification", type=StringType)
contentfwk_DataEntity.attributes={contentfwk_DataEntity_privacyClassification, contentfwk_DataEntity_dataEntityCategory, contentfwk_DataEntity_retentionClassification}

# contentfwk_LogicalDataComponent class attributes and methods

# contentfwk_PhysicalDataComponent class attributes and methods

# contentfwk_TechnologyArchitecture class attributes and methods

# contentfwk_PlatformService class attributes and methods

# contentfwk_PhysicalTechnologyComponent class attributes and methods
contentfwk_PhysicalTechnologyComponent_productName: Property = Property(name="productName", type=StringType)
contentfwk_PhysicalTechnologyComponent_moduleName: Property = Property(name="moduleName", type=StringType)
contentfwk_PhysicalTechnologyComponent_vendor: Property = Property(name="vendor", type=StringType)
contentfwk_PhysicalTechnologyComponent_version: Property = Property(name="version", type=StringType)
contentfwk_PhysicalTechnologyComponent.attributes={contentfwk_PhysicalTechnologyComponent_productName, contentfwk_PhysicalTechnologyComponent_version, contentfwk_PhysicalTechnologyComponent_moduleName, contentfwk_PhysicalTechnologyComponent_vendor}

# contentfwk_Role class attributes and methods
contentfwk_Role_estimatedFTEs: Property = Property(name="estimatedFTEs", type=StringType)
contentfwk_Role.attributes={contentfwk_Role_estimatedFTEs}

# contentfwk_Function class attributes and methods

# contentfwk_BusinessService class attributes and methods

# contentfwk_Process class attributes and methods
contentfwk_Process_processCritiality: Property = Property(name="processCritiality", type=StringType)
contentfwk_Process_isAutomated: Property = Property(name="isAutomated", type=BooleanType)
contentfwk_Process_processVolumetrics: Property = Property(name="processVolumetrics", type=StringType)
contentfwk_Process.attributes={contentfwk_Process_isAutomated, contentfwk_Process_processVolumetrics, contentfwk_Process_processCritiality}

# contentfwk_Control class attributes and methods

# contentfwk_Event class attributes and methods

# contentfwk_Location class attributes and methods

# contentfwk_Service class attributes and methods

# contentfwk_LogicalTechnologyComponent class attributes and methods

# Element class attributes and methods

# contentfwk_LogicalApplicationComponent class attributes and methods

# Standard class attributes and methods

# ApplicationComponent class attributes and methods

# contentfwk_PhysicalApplicationComponent class attributes and methods
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
contentfwk_PhysicalApplicationComponent_peakProfileLongTerm: Property = Property(name="peakProfileLongTerm", type=StringType)
contentfwk_PhysicalApplicationComponent.attributes={contentfwk_PhysicalApplicationComponent_interoperabilityCharacteristics, contentfwk_PhysicalApplicationComponent_dateOfLastRelease, contentfwk_PhysicalApplicationComponent_initialLiveDate, contentfwk_PhysicalApplicationComponent_reliabilityCharacteristics, contentfwk_PhysicalApplicationComponent_throughput, contentfwk_PhysicalApplicationComponent_dateOfNextRelease, contentfwk_PhysicalApplicationComponent_integrityCharacteristics, contentfwk_PhysicalApplicationComponent_retirementDate, contentfwk_PhysicalApplicationComponent_lifeCycleStatus, contentfwk_PhysicalApplicationComponent_growthPeriod, contentfwk_PhysicalApplicationComponent_growth, contentfwk_PhysicalApplicationComponent_extensibilityCharacteristics, contentfwk_PhysicalApplicationComponent_performanceCharacteristics, contentfwk_PhysicalApplicationComponent_credibilityCharacteristics, contentfwk_PhysicalApplicationComponent_manageabilityCharacteristics, contentfwk_PhysicalApplicationComponent_availabilityQualityCharacteristics, contentfwk_PhysicalApplicationComponent_servicesTimes, contentfwk_PhysicalApplicationComponent_serviceabilityCharacteristics, contentfwk_PhysicalApplicationComponent_recoverabilityCharacteristics, contentfwk_PhysicalApplicationComponent_capacityCharacteristics, contentfwk_PhysicalApplicationComponent_peakProfileShortTerm, contentfwk_PhysicalApplicationComponent_portabilityCharacteristics, contentfwk_PhysicalApplicationComponent_internationalizationCharacteristics, contentfwk_PhysicalApplicationComponent_localizationCharacteristics, contentfwk_PhysicalApplicationComponent_throughputPeriod, contentfwk_PhysicalApplicationComponent_peakProfileLongTerm, contentfwk_PhysicalApplicationComponent_privacyCharacteristics, contentfwk_PhysicalApplicationComponent_locatabilityCharacteristics, contentfwk_PhysicalApplicationComponent_scalabilityCharacteristics, contentfwk_PhysicalApplicationComponent_securityCharacteristics}

# Service class attributes and methods

# TechnologyComponent class attributes and methods

# contentfwk_Element class attributes and methods
contentfwk_Element_name: Property = Property(name="name", type=StringType)
contentfwk_Element_description: Property = Property(name="description", type=StringType)
contentfwk_Element_category: Property = Property(name="category", type=StringType)
contentfwk_Element_sourceDescr: Property = Property(name="sourceDescr", type=StringType)
contentfwk_Element_ownerDescr: Property = Property(name="ownerDescr", type=StringType)
contentfwk_Element_ID: Property = Property(name="ID", type=StringType)
contentfwk_Element.attributes={contentfwk_Element_name, contentfwk_Element_sourceDescr, contentfwk_Element_category, contentfwk_Element_ownerDescr, contentfwk_Element_description, contentfwk_Element_ID}

# contentfwk_Constraint class attributes and methods

# contentfwk_Assumption class attributes and methods

# contentfwk_Requirement class attributes and methods
contentfwk_Requirement_statementOfRequirement: Property = Property(name="statementOfRequirement", type=StringType)
contentfwk_Requirement_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Requirement_acceptanceCriteria: Property = Property(name="acceptanceCriteria", type=StringType)
contentfwk_Requirement.attributes={contentfwk_Requirement_statementOfRequirement, contentfwk_Requirement_rationale, contentfwk_Requirement_acceptanceCriteria}

# contentfwk_Gap class attributes and methods

# contentfwk_Capability class attributes and methods
contentfwk_Capability_businessValue: Property = Property(name="businessValue", type=StringType)
contentfwk_Capability_increments: Property = Property(name="increments", type=StringType)
contentfwk_Capability.attributes={contentfwk_Capability_businessValue, contentfwk_Capability_increments}

# contentfwk_WorkPackage class attributes and methods
contentfwk_WorkPackage_workPackageCategory: Property = Property(name="workPackageCategory", type=StringType)
contentfwk_WorkPackage.attributes={contentfwk_WorkPackage_workPackageCategory}

# contentfwk_StrategicElement class attributes and methods

# contentfwk_Principle class attributes and methods
contentfwk_Principle_rationale: Property = Property(name="rationale", type=StringType)
contentfwk_Principle_implication: Property = Property(name="implication", type=StringType)
contentfwk_Principle_metric: Property = Property(name="metric", type=StringType)
contentfwk_Principle_principleCategory: Property = Property(name="principleCategory", type=StringType)
contentfwk_Principle_priority: Property = Property(name="priority", type=StringType)
contentfwk_Principle_statementOfPrinciple: Property = Property(name="statementOfPrinciple", type=StringType)
contentfwk_Principle.attributes={contentfwk_Principle_priority, contentfwk_Principle_implication, contentfwk_Principle_metric, contentfwk_Principle_rationale, contentfwk_Principle_principleCategory, contentfwk_Principle_statementOfPrinciple}

# StrategicElement class attributes and methods

# contentfwk_ApplicationArchitecture class attributes and methods

# contentfwk_InformationSystemService class attributes and methods

# DataComponent class attributes and methods

# contentfwk_StrategicArchitecture class attributes and methods

# contentfwk_Standard class attributes and methods
contentfwk_Standard_standardClass: Property = Property(name="standardClass", type=StringType)
contentfwk_Standard_standardCreationDate: Property = Property(name="standardCreationDate", type=DateType)
contentfwk_Standard_lastStandardCreationDate: Property = Property(name="lastStandardCreationDate", type=DateType)
contentfwk_Standard_nextStandardCreationDate: Property = Property(name="nextStandardCreationDate", type=DateType)
contentfwk_Standard_retireDate: Property = Property(name="retireDate", type=StringType)
contentfwk_Standard.attributes={contentfwk_Standard_standardClass, contentfwk_Standard_retireDate, contentfwk_Standard_standardCreationDate, contentfwk_Standard_lastStandardCreationDate, contentfwk_Standard_nextStandardCreationDate}

# contentfwk_TechnologyComponent class attributes and methods

# contentfwk_ApplicationComponent class attributes and methods

# contentfwk_DataComponent class attributes and methods

# Relationships
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
realizesGoals54: BinaryAssociation = BinaryAssociation(
    name="realizesGoals54",
    ends={
        Property(name="Goal55", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughObjectives", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures56: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures56",
    ends={
        Property(name="Measure", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForObjectives", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesObjective58: BinaryAssociation = BinaryAssociation(
    name="decomposesObjective58",
    ends={
        Property(name="contentfwk_Objective59", type=contentfwk_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Objective57", type=contentfwk_Objective, multiplicity=Multiplicity(0, 1))
    }
)
ownsAndGovernsServices60: BinaryAssociation = BinaryAssociation(
    name="ownsAndGovernsServices60",
    ends={
        Property(name="Service", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedAndGovernedByOrganizationUnits", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors61: BinaryAssociation = BinaryAssociation(
    name="containsActors61",
    ends={
        Property(name="Actor", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="belongsTo", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
ownsFunctions62: BinaryAssociation = BinaryAssociation(
    name="ownsFunctions62",
    ends={
        Property(name="Function", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isOwnedByUnit", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses63: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses63",
    ends={
        Property(name="Process", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesOrganizationUnits", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isMotivatedByDrivers64: BinaryAssociation = BinaryAssociation(
    name="isMotivatedByDrivers64",
    ends={
        Property(name="Driver65", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="motivatesOrganizationUnits", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
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
        Property(name="Goal", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="addressesDrivers", type=contentfwk_Goal, multiplicity=Multiplicity(0, 9999))
    }
)
motivatesOrganizationUnits45: BinaryAssociation = BinaryAssociation(
    name="motivatesOrganizationUnits45",
    ends={
        Property(name="OrganizationUnit", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="isMotivatedByDrivers", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesDriver47: BinaryAssociation = BinaryAssociation(
    name="decomposesDriver47",
    ends={
        Property(name="contentfwk_Driver48", type=contentfwk_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Driver46", type=contentfwk_Driver, multiplicity=Multiplicity(0, 1))
    }
)
addressesDrivers49: BinaryAssociation = BinaryAssociation(
    name="addressesDrivers49",
    ends={
        Property(name="Driver", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="createsGoals", type=contentfwk_Driver, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughObjectives50: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughObjectives50",
    ends={
        Property(name="Objective", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="realizesGoals", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesGoal52: BinaryAssociation = BinaryAssociation(
    name="decomposesGoal52",
    ends={
        Property(name="contentfwk_Goal53", type=contentfwk_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Goal51", type=contentfwk_Goal, multiplicity=Multiplicity(0, 1))
    }
)
interactsWithFunctions73: BinaryAssociation = BinaryAssociation(
    name="interactsWithFunctions73",
    ends={
        Property(name="supportsActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999)),
        Property(name="Function74", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1))
    }
)
performsTaskInRoles75: BinaryAssociation = BinaryAssociation(
    name="performsTaskInRoles75",
    ends={
        Property(name="Role", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isAssumedByActors", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
participatesInProcesses76: BinaryAssociation = BinaryAssociation(
    name="participatesInProcesses76",
    ends={
        Property(name="Process77", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="involvesActors", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices78: BinaryAssociation = BinaryAssociation(
    name="consumesServices78",
    ends={
        Property(name="contentfwk_Service", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor79", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents80: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents80",
    ends={
        Property(name="Event", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents81: BinaryAssociation = BinaryAssociation(
    name="generatesEvents81",
    ends={
        Property(name="Event82", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByActors", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation83: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation83",
    ends={
        Property(name="Location85", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors84", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
performsFunctions86: BinaryAssociation = BinaryAssociation(
    name="performsFunctions86",
    ends={
        Property(name="Function87", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isPerformedByActors", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts66: BinaryAssociation = BinaryAssociation(
    name="producesProducts66",
    ends={
        Property(name="Product", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByOrganizationUnits", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
operatesInLocation67: BinaryAssociation = BinaryAssociation(
    name="operatesInLocation67",
    ends={
        Property(name="Location", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="containsOrganizationUnits", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
suppliesEntities68: BinaryAssociation = BinaryAssociation(
    name="suppliesEntities68",
    ends={
        Property(name="DataEntity", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities69: BinaryAssociation = BinaryAssociation(
    name="consumesEntities69",
    ends={
        Property(name="DataEntity70", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="isConsumedByActors", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
belongsTo71: BinaryAssociation = BinaryAssociation(
    name="belongsTo71",
    ends={
        Property(name="OrganizationUnit72", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="containsActors", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
isSuppliedByActors98: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByActors98",
    ends={
        Property(name="Actor99", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isConsumedByActors100: BinaryAssociation = BinaryAssociation(
    name="isConsumedByActors100",
    ends={
        Property(name="Actor101", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesEntities", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAccessedByServices102: BinaryAssociation = BinaryAssociation(
    name="isAccessedByServices102",
    ends={
        Property(name="Service104", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="consumesEntities103", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isUpdatedThroughServices105: BinaryAssociation = BinaryAssociation(
    name="isUpdatedThroughServices105",
    ends={
        Property(name="Service106", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="providesEntities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
residesWithinLogicalDataComponent107: BinaryAssociation = BinaryAssociation(
    name="residesWithinLogicalDataComponent107",
    ends={
        Property(name="LogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatesDataEntities", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
isProcessesByLogicalApplicationComponents108: BinaryAssociation = BinaryAssociation(
    name="isProcessesByLogicalApplicationComponents108",
    ends={
        Property(name="LogicalApplicationComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesOnDataEntities", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposeEntity110: BinaryAssociation = BinaryAssociation(
    name="decomposeEntity110",
    ends={
        Property(name="contentfwk_DataEntity111", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity109", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 1))
    }
)
relatesTo113: BinaryAssociation = BinaryAssociation(
    name="relatesTo113",
    ends={
        Property(name="contentfwk_DataEntity114", type=contentfwk_DataEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_DataEntity112", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesActors89: BinaryAssociation = BinaryAssociation(
    name="decomposesActors89",
    ends={
        Property(name="contentfwk_Actor90", type=contentfwk_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Actor88", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isAssumedByActors91: BinaryAssociation = BinaryAssociation(
    name="isAssumedByActors91",
    ends={
        Property(name="Actor92", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="performsTaskInRoles", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
accessesFunctions93: BinaryAssociation = BinaryAssociation(
    name="accessesFunctions93",
    ends={
        Property(name="Function94", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="canBeAccessedByRoles", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesRole96: BinaryAssociation = BinaryAssociation(
    name="decomposesRole96",
    ends={
        Property(name="contentfwk_Role97", type=contentfwk_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Role95", type=contentfwk_Role, multiplicity=Multiplicity(0, 1))
    }
)
communicatesWith121: BinaryAssociation = BinaryAssociation(
    name="communicatesWith121",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent120", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalApplicationComponent123: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalApplicationComponent123",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent124", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalApplicationComponent122", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
isPerformedByActors125: BinaryAssociation = BinaryAssociation(
    name="isPerformedByActors125",
    ends={
        Property(name="Actor126", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="performsFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedByUnit127: BinaryAssociation = BinaryAssociation(
    name="isOwnedByUnit127",
    ends={
        Property(name="OrganizationUnit128", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsFunctions", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 1))
    }
)
implementsServices115: BinaryAssociation = BinaryAssociation(
    name="implementsServices115",
    ends={
        Property(name="Service116", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedThroughLogicalApplicationComponent", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
operatesOnDataEntities117: BinaryAssociation = BinaryAssociation(
    name="operatesOnDataEntities117",
    ends={
        Property(name="DataEntity118", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isProcessesByLogicalApplicationComponents", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalApplicationComponents119: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalApplicationComponents119",
    ends={
        Property(name="PhysicalApplicationComponent", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalApplicationComponents", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
supportsObjective145: BinaryAssociation = BinaryAssociation(
    name="supportsObjective145",
    ends={
        Property(name="contentfwk_Objective147", type=contentfwk_BusinessService, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_BusinessService146", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesFunctions148: BinaryAssociation = BinaryAssociation(
    name="orchestratesFunctions148",
    ends={
        Property(name="Function149", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
isBoundedByServices129: BinaryAssociation = BinaryAssociation(
    name="isBoundedByServices129",
    ends={
        Property(name="Service130", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="providesGovernedInterfaceToAccessFunctions", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses131: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses131",
    ends={
        Property(name="Process132", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses133: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses133",
    ends={
        Property(name="Process134", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesFunctions", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
canBeAccessedByRoles135: BinaryAssociation = BinaryAssociation(
    name="canBeAccessedByRoles135",
    ends={
        Property(name="Role136", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="accessesFunctions", type=contentfwk_Role, multiplicity=Multiplicity(0, 9999))
    }
)
supportsActors137: BinaryAssociation = BinaryAssociation(
    name="supportsActors137",
    ends={
        Property(name="Actor138", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="interactsWithFunctions", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunction140: BinaryAssociation = BinaryAssociation(
    name="decomposesFunction140",
    ends={
        Property(name="contentfwk_Function141", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function139", type=contentfwk_Function, multiplicity=Multiplicity(0, 1))
    }
)
communicatedWithFunctions143: BinaryAssociation = BinaryAssociation(
    name="communicatedWithFunctions143",
    ends={
        Property(name="contentfwk_Function144", type=contentfwk_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Function142", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
isGuidedByControls163: BinaryAssociation = BinaryAssociation(
    name="isGuidedByControls163",
    ends={
        Property(name="Control", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="ensuresCorrectOperationOfProcesses", type=contentfwk_Control, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents164: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents164",
    ends={
        Property(name="Event165", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
generatesEvents166: BinaryAssociation = BinaryAssociation(
    name="generatesEvents166",
    ends={
        Property(name="Event167", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isGeneratedByProcesses", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
producesProducts168: BinaryAssociation = BinaryAssociation(
    name="producesProducts168",
    ends={
        Property(name="Product169", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isProducedByProcesses", type=contentfwk_Product, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesProcess171: BinaryAssociation = BinaryAssociation(
    name="decomposesProcess171",
    ends={
        Property(name="contentfwk_Process172", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Process170", type=contentfwk_Process, multiplicity=Multiplicity(0, 1))
    }
)
precedesProcesses174: BinaryAssociation = BinaryAssociation(
    name="precedesProcesses174",
    ends={
        Property(name="Process175", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="followsProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesFunctions150: BinaryAssociation = BinaryAssociation(
    name="decomposesFunctions150",
    ends={
        Property(name="Function151", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
involvesOrganizationUnits152: BinaryAssociation = BinaryAssociation(
    name="involvesOrganizationUnits152",
    ends={
        Property(name="OrganizationUnit153", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
orchestratesServices154: BinaryAssociation = BinaryAssociation(
    name="orchestratesServices154",
    ends={
        Property(name="Service156", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByProcesses155", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices157: BinaryAssociation = BinaryAssociation(
    name="decomposesServices157",
    ends={
        Property(name="Service159", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="supportsProcesses158", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
involvesActors160: BinaryAssociation = BinaryAssociation(
    name="involvesActors160",
    ends={
        Property(name="Actor162", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="participatesInProcesses161", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalTechnologyComponent187: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalTechnologyComponent187",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent188", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent186", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 1))
    }
)
isDependentOnPhysicalTechnologyComponents190: BinaryAssociation = BinaryAssociation(
    name="isDependentOnPhysicalTechnologyComponents190",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent191", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent189", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByOrganizationUnits192: BinaryAssociation = BinaryAssociation(
    name="isProducedByOrganizationUnits192",
    ends={
        Property(name="OrganizationUnit193", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isProducedByProcesses194: BinaryAssociation = BinaryAssociation(
    name="isProducedByProcesses194",
    ends={
        Property(name="Process196", type=contentfwk_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="producesProducts195", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForObjectives197: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForObjectives197",
    ends={
        Property(name="Objective198", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures", type=contentfwk_Objective, multiplicity=Multiplicity(0, 9999))
    }
)
followsProcesses177: BinaryAssociation = BinaryAssociation(
    name="followsProcesses177",
    ends={
        Property(name="Process178", type=contentfwk_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="precedesProcesses", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isSuppliedByLogicalTechnologyComponents179: BinaryAssociation = BinaryAssociation(
    name="isSuppliedByLogicalTechnologyComponents179",
    ends={
        Property(name="LogicalTechnologyComponent", type=contentfwk_PlatformService, multiplicity=Multiplicity(1, 1)),
        Property(name="suppliesPlatformServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
realizesApplicationComponents180: BinaryAssociation = BinaryAssociation(
    name="realizesApplicationComponents180",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalTechnologyComponent181", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalTechnologyComponents182: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalTechnologyComponents182",
    ends={
        Property(name="LogicalTechnologyComponent183", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isRealizedByPhysicalTechnologyComponents", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation184: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation184",
    ends={
        Property(name="Location185", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalTechnologyComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
setsPerformanceCriteriaForServices199: BinaryAssociation = BinaryAssociation(
    name="setsPerformanceCriteriaForServices199",
    ends={
        Property(name="Service201", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="isTrackedAgainstMeasures200", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesMeasure203: BinaryAssociation = BinaryAssociation(
    name="decomposesMeasure203",
    ends={
        Property(name="contentfwk_Measure204", type=contentfwk_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Measure202", type=contentfwk_Measure, multiplicity=Multiplicity(0, 1))
    }
)
appliesToServices205: BinaryAssociation = BinaryAssociation(
    name="appliesToServices205",
    ends={
        Property(name="Service206", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsQualities", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
appliesToContracts207: BinaryAssociation = BinaryAssociation(
    name="appliesToContracts207",
    ends={
        Property(name="Contract", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(1, 1)),
        Property(name="meetsServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
governsAndMeasuresBusinessServices208: BinaryAssociation = BinaryAssociation(
    name="governsAndMeasuresBusinessServices208",
    ends={
        Property(name="Service209", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="isGovernedAndMeasuredByContracts", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
meetsServiceQuality210: BinaryAssociation = BinaryAssociation(
    name="meetsServiceQuality210",
    ends={
        Property(name="ServiceQuality", type=contentfwk_Contract, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToContracts", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByBusinessServices211: BinaryAssociation = BinaryAssociation(
    name="isResolvedByBusinessServices211",
    ends={
        Property(name="Service212", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByProcesses213: BinaryAssociation = BinaryAssociation(
    name="isResolvedByProcesses213",
    ends={
        Property(name="Process215", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents214", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByProcesses216: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByProcesses216",
    ends={
        Property(name="Process217", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isResolvedByActors218: BinaryAssociation = BinaryAssociation(
    name="isResolvedByActors218",
    ends={
        Property(name="Actor220", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="resolvesEvents219", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
isGeneratedByActors221: BinaryAssociation = BinaryAssociation(
    name="isGeneratedByActors221",
    ends={
        Property(name="Actor223", type=contentfwk_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="generatesEvents222", type=contentfwk_Actor, multiplicity=Multiplicity(0, 1))
    }
)
ensuresCorrectOperationOfProcesses224: BinaryAssociation = BinaryAssociation(
    name="ensuresCorrectOperationOfProcesses224",
    ends={
        Property(name="Process225", type=contentfwk_Control, multiplicity=Multiplicity(1, 1)),
        Property(name="isGuidedByControls", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
ownsElements231: BinaryAssociation = BinaryAssociation(
    name="ownsElements231",
    ends={
        Property(name="contentfwk_Element", type=contentfwk_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Container232", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
containsActors233: BinaryAssociation = BinaryAssociation(
    name="containsActors233",
    ends={
        Property(name="Actor234", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
containsOrganizationUnits235: BinaryAssociation = BinaryAssociation(
    name="containsOrganizationUnits235",
    ends={
        Property(name="OrganizationUnit237", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="operatesInLocation236", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalDataComponents238: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalDataComponents238",
    ends={
        Property(name="PhysicalDataComponent", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHotedInLocation", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalApplicationComponents239: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalApplicationComponents239",
    ends={
        Property(name="PhysicalApplicationComponent240", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
containsPhysicalTechnologyComponents241: BinaryAssociation = BinaryAssociation(
    name="containsPhysicalTechnologyComponents241",
    ends={
        Property(name="PhysicalTechnologyComponent", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="isHostedInLocation242", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLocation244: BinaryAssociation = BinaryAssociation(
    name="decomposesLocation244",
    ends={
        Property(name="contentfwk_Location245", type=contentfwk_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Location243", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
delegates227: BinaryAssociation = BinaryAssociation(
    name="delegates227",
    ends={
        Property(name="Element", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="isDelegatedBy", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isDelegatedBy229: BinaryAssociation = BinaryAssociation(
    name="isDelegatedBy229",
    ends={
        Property(name="Element230", type=contentfwk_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="delegates", type=contentfwk_Element, multiplicity=Multiplicity(0, 9999))
    }
)
isDeliveredBy246: BinaryAssociation = BinaryAssociation(
    name="isDeliveredBy246",
    ends={
        Property(name="WorkPackage", type=contentfwk_Capability, multiplicity=Multiplicity(1, 1)),
        Property(name="deliversCapabilities", type=contentfwk_WorkPackage, multiplicity=Multiplicity(0, 1))
    }
)
encapsulatesPhysicalApplicationComponents259: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalApplicationComponents259",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent261", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent260", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
logicalApplicationComponents262: BinaryAssociation = BinaryAssociation(
    name="logicalApplicationComponents262",
    ends={
        Property(name="contentfwk_LogicalApplicationComponent263", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalApplicationComponents264: BinaryAssociation = BinaryAssociation(
    name="physicalApplicationComponents264",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent266", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture265", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
informationSystemServices267: BinaryAssociation = BinaryAssociation(
    name="informationSystemServices267",
    ends={
        Property(name="contentfwk_InformationSystemService", type=contentfwk_ApplicationArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_ApplicationArchitecture268", type=contentfwk_InformationSystemService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsLogicalApplicationComponents269: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalApplicationComponents269",
    ends={
        Property(name="LogicalApplicationComponent270", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalApplicationComponents", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHostedInLocation271: BinaryAssociation = BinaryAssociation(
    name="isHostedInLocation271",
    ends={
        Property(name="Location272", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalApplicationComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 9999))
    }
)
deliversCapabilities247: BinaryAssociation = BinaryAssociation(
    name="deliversCapabilities247",
    ends={
        Property(name="Capability", type=contentfwk_WorkPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="isDeliveredBy", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999))
    }
)
encapsulatesDataEntities248: BinaryAssociation = BinaryAssociation(
    name="encapsulatesDataEntities248",
    ends={
        Property(name="DataEntity249", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="residesWithinLogicalDataComponent", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isExtendedByPhysicalDataComponents250: BinaryAssociation = BinaryAssociation(
    name="isExtendedByPhysicalDataComponents250",
    ends={
        Property(name="PhysicalDataComponent251", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalDataComponents", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
extendsLogicalDataComponents252: BinaryAssociation = BinaryAssociation(
    name="extendsLogicalDataComponents252",
    ends={
        Property(name="LogicalDataComponent253", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isExtendedByPhysicalDataComponents", type=contentfwk_LogicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isHotedInLocation254: BinaryAssociation = BinaryAssociation(
    name="isHotedInLocation254",
    ends={
        Property(name="Location255", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="containsPhysicalDataComponents", type=contentfwk_Location, multiplicity=Multiplicity(0, 1))
    }
)
decomposesPhysicalDataComponent257: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalDataComponent257",
    ends={
        Property(name="contentfwk_PhysicalDataComponent258", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalDataComponent256", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 1))
    }
)
communicatesWith274: BinaryAssociation = BinaryAssociation(
    name="communicatesWith274",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent275", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent273", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesLogicalTechnologyComponent291: BinaryAssociation = BinaryAssociation(
    name="decomposesLogicalTechnologyComponent291",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent290", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent292", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1))
    }
)
isDependentOnLogicalTechnologyComponents294: BinaryAssociation = BinaryAssociation(
    name="isDependentOnLogicalTechnologyComponents294",
    ends={
        Property(name="contentfwk_LogicalTechnologyComponent295", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_LogicalTechnologyComponent293", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
capabilities296: BinaryAssociation = BinaryAssociation(
    name="capabilities296",
    ends={
        Property(name="contentfwk_Capability", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture", type=contentfwk_Capability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strategicElements297: BinaryAssociation = BinaryAssociation(
    name="strategicElements297",
    ends={
        Property(name="contentfwk_StrategicElement", type=contentfwk_StrategicArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_StrategicArchitecture298", type=contentfwk_StrategicElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
encapsulatesPhysicalDataComponents276: BinaryAssociation = BinaryAssociation(
    name="encapsulatesPhysicalDataComponents276",
    ends={
        Property(name="contentfwk_PhysicalDataComponent278", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent277", type=contentfwk_PhysicalDataComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents279: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents279",
    ends={
        Property(name="contentfwk_PhysicalTechnologyComponent281", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent280", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesPhysicalApplicationComponent283: BinaryAssociation = BinaryAssociation(
    name="decomposesPhysicalApplicationComponent283",
    ends={
        Property(name="contentfwk_PhysicalApplicationComponent284", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_PhysicalApplicationComponent282", type=contentfwk_PhysicalApplicationComponent, multiplicity=Multiplicity(0, 1))
    }
)
providesPlatformForServices285: BinaryAssociation = BinaryAssociation(
    name="providesPlatformForServices285",
    ends={
        Property(name="Service286", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isImplementedOnLogicalTechnologyComponents", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
suppliesPlatformServices287: BinaryAssociation = BinaryAssociation(
    name="suppliesPlatformServices287",
    ends={
        Property(name="PlatformService", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="isSuppliedByLogicalTechnologyComponents", type=contentfwk_PlatformService, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByPhysicalTechnologyComponents288: BinaryAssociation = BinaryAssociation(
    name="isRealizedByPhysicalTechnologyComponents288",
    ends={
        Property(name="PhysicalTechnologyComponent289", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsLogicalTechnologyComponents", type=contentfwk_PhysicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
resolvesEvents310: BinaryAssociation = BinaryAssociation(
    name="resolvesEvents310",
    ends={
        Property(name="Event311", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isResolvedByBusinessServices", type=contentfwk_Event, multiplicity=Multiplicity(0, 9999))
    }
)
isImplementedOnLogicalTechnologyComponents312: BinaryAssociation = BinaryAssociation(
    name="isImplementedOnLogicalTechnologyComponents312",
    ends={
        Property(name="LogicalTechnologyComponent313", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="providesPlatformForServices", type=contentfwk_LogicalTechnologyComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedThroughLogicalApplicationComponent314: BinaryAssociation = BinaryAssociation(
    name="isRealizedThroughLogicalApplicationComponent314",
    ends={
        Property(name="LogicalApplicationComponent315", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="implementsServices", type=contentfwk_LogicalApplicationComponent, multiplicity=Multiplicity(0, 9999))
    }
)
isOwnedAndGovernedByOrganizationUnits316: BinaryAssociation = BinaryAssociation(
    name="isOwnedAndGovernedByOrganizationUnits316",
    ends={
        Property(name="OrganizationUnit317", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsAndGovernsServices", type=contentfwk_OrganizationUnit, multiplicity=Multiplicity(0, 9999))
    }
)
isTrackedAgainstMeasures318: BinaryAssociation = BinaryAssociation(
    name="isTrackedAgainstMeasures318",
    ends={
        Property(name="Measure319", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="setsPerformanceCriteriaForServices", type=contentfwk_Measure, multiplicity=Multiplicity(0, 9999))
    }
)
supportsProcesses320: BinaryAssociation = BinaryAssociation(
    name="supportsProcesses320",
    ends={
        Property(name="Process321", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="decomposesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
isRealizedByProcesses322: BinaryAssociation = BinaryAssociation(
    name="isRealizedByProcesses322",
    ends={
        Property(name="Process323", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="orchestratesServices", type=contentfwk_Process, multiplicity=Multiplicity(0, 9999))
    }
)
meetsQualities324: BinaryAssociation = BinaryAssociation(
    name="meetsQualities324",
    ends={
        Property(name="ServiceQuality325", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="appliesToServices", type=contentfwk_ServiceQuality, multiplicity=Multiplicity(0, 9999))
    }
)
isProvidedToActors299: BinaryAssociation = BinaryAssociation(
    name="isProvidedToActors299",
    ends={
        Property(name="contentfwk_Actor301", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service300", type=contentfwk_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
providesGovernedInterfaceToAccessFunctions302: BinaryAssociation = BinaryAssociation(
    name="providesGovernedInterfaceToAccessFunctions302",
    ends={
        Property(name="Function303", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isBoundedByServices", type=contentfwk_Function, multiplicity=Multiplicity(0, 9999))
    }
)
providesEntities304: BinaryAssociation = BinaryAssociation(
    name="providesEntities304",
    ends={
        Property(name="DataEntity305", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isUpdatedThroughServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
consumesEntities306: BinaryAssociation = BinaryAssociation(
    name="consumesEntities306",
    ends={
        Property(name="DataEntity307", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="isAccessedByServices", type=contentfwk_DataEntity, multiplicity=Multiplicity(0, 9999))
    }
)
isGovernedAndMeasuredByContracts308: BinaryAssociation = BinaryAssociation(
    name="isGovernedAndMeasuredByContracts308",
    ends={
        Property(name="Contract309", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="governsAndMeasuresBusinessServices", type=contentfwk_Contract, multiplicity=Multiplicity(0, 9999))
    }
)
consumesServices327: BinaryAssociation = BinaryAssociation(
    name="consumesServices327",
    ends={
        Property(name="contentfwk_Service328", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service326", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)
decomposesServices330: BinaryAssociation = BinaryAssociation(
    name="decomposesServices330",
    ends={
        Property(name="contentfwk_Service331", type=contentfwk_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="contentfwk_Service329", type=contentfwk_Service, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_contentfwk_BusinessArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_BusinessArchitecture)
gen_contentfwk_DataArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_DataArchitecture)
gen_contentfwk_TechnologyArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_TechnologyArchitecture)
gen_contentfwk_Objective_Element = Generalization(general=Element, specific=contentfwk_Objective)
gen_contentfwk_OrganizationUnit_Element = Generalization(general=Element, specific=contentfwk_OrganizationUnit)
gen_contentfwk_Driver_Element = Generalization(general=Element, specific=contentfwk_Driver)
gen_contentfwk_Goal_Element = Generalization(general=Element, specific=contentfwk_Goal)
gen_contentfwk_Actor_Element = Generalization(general=Element, specific=contentfwk_Actor)
gen_contentfwk_Role_Element = Generalization(general=Element, specific=contentfwk_Role)
gen_contentfwk_DataEntity_Element = Generalization(general=Element, specific=contentfwk_DataEntity)
gen_contentfwk_Function_Element = Generalization(general=Element, specific=contentfwk_Function)
gen_contentfwk_Function_Standard = Generalization(general=Standard, specific=contentfwk_Function)
gen_contentfwk_LogicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_LogicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_LogicalApplicationComponent)
gen_contentfwk_BusinessService_Element = Generalization(general=Element, specific=contentfwk_BusinessService)
gen_contentfwk_BusinessService_Service = Generalization(general=Service, specific=contentfwk_BusinessService)
gen_contentfwk_Process_Element = Generalization(general=Element, specific=contentfwk_Process)
gen_contentfwk_Process_Standard = Generalization(general=Standard, specific=contentfwk_Process)
gen_contentfwk_Product_Element = Generalization(general=Element, specific=contentfwk_Product)
gen_contentfwk_Measure_Element = Generalization(general=Element, specific=contentfwk_Measure)
gen_contentfwk_PlatformService_Element = Generalization(general=Element, specific=contentfwk_PlatformService)
gen_contentfwk_PlatformService_Service = Generalization(general=Service, specific=contentfwk_PlatformService)
gen_contentfwk_PhysicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_PhysicalTechnologyComponent)
gen_contentfwk_ServiceQuality_Element = Generalization(general=Element, specific=contentfwk_ServiceQuality)
gen_contentfwk_Contract_Element = Generalization(general=Element, specific=contentfwk_Contract)
gen_contentfwk_Event_Element = Generalization(general=Element, specific=contentfwk_Event)
gen_contentfwk_Control_Element = Generalization(general=Element, specific=contentfwk_Control)
gen_contentfwk_Location_Element = Generalization(general=Element, specific=contentfwk_Location)
gen_contentfwk_Constraint_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Constraint)
gen_contentfwk_Assumption_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Assumption)
gen_contentfwk_Requirement_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Requirement)
gen_contentfwk_Gap_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Gap)
gen_contentfwk_WorkPackage_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_WorkPackage)
gen_contentfwk_Capability_Element = Generalization(general=Element, specific=contentfwk_Capability)
gen_contentfwk_StrategicElement_Element = Generalization(general=Element, specific=contentfwk_StrategicElement)
gen_contentfwk_Principle_StrategicElement = Generalization(general=StrategicElement, specific=contentfwk_Principle)
gen_contentfwk_ApplicationArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_ApplicationArchitecture)
gen_contentfwk_PhysicalApplicationComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent = Generalization(general=ApplicationComponent, specific=contentfwk_PhysicalApplicationComponent)
gen_contentfwk_LogicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_LogicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_LogicalDataComponent)
gen_contentfwk_PhysicalDataComponent_Element = Generalization(general=Element, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_PhysicalDataComponent_DataComponent = Generalization(general=DataComponent, specific=contentfwk_PhysicalDataComponent)
gen_contentfwk_StrategicArchitecture_Architecture = Generalization(general=Architecture, specific=contentfwk_StrategicArchitecture)
gen_contentfwk_LogicalTechnologyComponent_Element = Generalization(general=Element, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent = Generalization(general=TechnologyComponent, specific=contentfwk_LogicalTechnologyComponent)
gen_contentfwk_Service_Standard = Generalization(general=Standard, specific=contentfwk_Service)
gen_contentfwk_TechnologyComponent_Standard = Generalization(general=Standard, specific=contentfwk_TechnologyComponent)
gen_contentfwk_ApplicationComponent_Standard = Generalization(general=Standard, specific=contentfwk_ApplicationComponent)
gen_contentfwk_InformationSystemService_Service = Generalization(general=Service, specific=contentfwk_InformationSystemService)
gen_contentfwk_InformationSystemService_Element = Generalization(general=Element, specific=contentfwk_InformationSystemService)
gen_contentfwk_DataComponent_Standard = Generalization(general=Standard, specific=contentfwk_DataComponent)

# Domain Model
domain_model = DomainModel(
    name="contentfwk",
    types={contentfwk_Container, contentfwk_BusinessArchitecture, Architecture, contentfwk_Driver, contentfwk_Goal, contentfwk_Objective, contentfwk_OrganizationUnit, contentfwk_Actor, contentfwk_EnterpriseArchitecture, contentfwk_Architecture, contentfwk_Product, contentfwk_Contract, contentfwk_Measure, contentfwk_ServiceQuality, contentfwk_DataArchitecture, contentfwk_DataEntity, contentfwk_LogicalDataComponent, contentfwk_PhysicalDataComponent, contentfwk_TechnologyArchitecture, contentfwk_PlatformService, contentfwk_PhysicalTechnologyComponent, contentfwk_Role, contentfwk_Function, contentfwk_BusinessService, contentfwk_Process, contentfwk_Control, contentfwk_Event, contentfwk_Location, contentfwk_Service, contentfwk_LogicalTechnologyComponent, Element, contentfwk_LogicalApplicationComponent, Standard, ApplicationComponent, contentfwk_PhysicalApplicationComponent, Service, TechnologyComponent, contentfwk_Element, contentfwk_Constraint, contentfwk_Assumption, contentfwk_Requirement, contentfwk_Gap, contentfwk_Capability, contentfwk_WorkPackage, contentfwk_StrategicElement, contentfwk_Principle, StrategicElement, contentfwk_ApplicationArchitecture, contentfwk_InformationSystemService, DataComponent, contentfwk_StrategicArchitecture, contentfwk_Standard, contentfwk_TechnologyComponent, contentfwk_ApplicationComponent, contentfwk_DataComponent, PrincipleCategory, StandardsClass, WorkPackageCategory, LifeCycleStatus, DataEntityCategory},
    associations={architectures0, containers1, drivers3, goals4, objectives6, units8, actors10, products26, contracts28, measures30, servicesQuality32, entities34, logicalComponents35, physicalComponents37, platformServices39, physicalComponents40, roles12, functions14, services16, processes18, controls20, events22, locations24, realizesGoals54, isTrackedAgainstMeasures56, decomposesObjective58, ownsAndGovernsServices60, containsActors61, ownsFunctions62, participatesInProcesses63, isMotivatedByDrivers64, logicalComponents42, createsGoals44, motivatesOrganizationUnits45, decomposesDriver47, addressesDrivers49, isRealizedThroughObjectives50, decomposesGoal52, interactsWithFunctions73, performsTaskInRoles75, participatesInProcesses76, consumesServices78, resolvesEvents80, generatesEvents81, operatesInLocation83, performsFunctions86, producesProducts66, operatesInLocation67, suppliesEntities68, consumesEntities69, belongsTo71, isSuppliedByActors98, isConsumedByActors100, isAccessedByServices102, isUpdatedThroughServices105, residesWithinLogicalDataComponent107, isProcessesByLogicalApplicationComponents108, decomposeEntity110, relatesTo113, decomposesActors89, isAssumedByActors91, accessesFunctions93, decomposesRole96, communicatesWith121, decomposesLogicalApplicationComponent123, isPerformedByActors125, isOwnedByUnit127, implementsServices115, operatesOnDataEntities117, isExtendedByPhysicalApplicationComponents119, supportsObjective145, orchestratesFunctions148, isBoundedByServices129, supportsProcesses131, isRealizedByProcesses133, canBeAccessedByRoles135, supportsActors137, decomposesFunction140, communicatedWithFunctions143, isGuidedByControls163, resolvesEvents164, generatesEvents166, producesProducts168, decomposesProcess171, precedesProcesses174, decomposesFunctions150, involvesOrganizationUnits152, orchestratesServices154, decomposesServices157, involvesActors160, decomposesPhysicalTechnologyComponent187, isDependentOnPhysicalTechnologyComponents190, isProducedByOrganizationUnits192, isProducedByProcesses194, setsPerformanceCriteriaForObjectives197, followsProcesses177, isSuppliedByLogicalTechnologyComponents179, realizesApplicationComponents180, extendsLogicalTechnologyComponents182, isHostedInLocation184, setsPerformanceCriteriaForServices199, decomposesMeasure203, appliesToServices205, appliesToContracts207, governsAndMeasuresBusinessServices208, meetsServiceQuality210, isResolvedByBusinessServices211, isResolvedByProcesses213, isGeneratedByProcesses216, isResolvedByActors218, isGeneratedByActors221, ensuresCorrectOperationOfProcesses224, ownsElements231, containsActors233, containsOrganizationUnits235, containsPhysicalDataComponents238, containsPhysicalApplicationComponents239, containsPhysicalTechnologyComponents241, decomposesLocation244, delegates227, isDelegatedBy229, isDeliveredBy246, encapsulatesPhysicalApplicationComponents259, logicalApplicationComponents262, physicalApplicationComponents264, informationSystemServices267, extendsLogicalApplicationComponents269, isHostedInLocation271, deliversCapabilities247, encapsulatesDataEntities248, isExtendedByPhysicalDataComponents250, extendsLogicalDataComponents252, isHotedInLocation254, decomposesPhysicalDataComponent257, communicatesWith274, decomposesLogicalTechnologyComponent291, isDependentOnLogicalTechnologyComponents294, capabilities296, strategicElements297, encapsulatesPhysicalDataComponents276, isRealizedByPhysicalTechnologyComponents279, decomposesPhysicalApplicationComponent283, providesPlatformForServices285, suppliesPlatformServices287, isRealizedByPhysicalTechnologyComponents288, resolvesEvents310, isImplementedOnLogicalTechnologyComponents312, isRealizedThroughLogicalApplicationComponent314, isOwnedAndGovernedByOrganizationUnits316, isTrackedAgainstMeasures318, supportsProcesses320, isRealizedByProcesses322, meetsQualities324, isProvidedToActors299, providesGovernedInterfaceToAccessFunctions302, providesEntities304, consumesEntities306, isGovernedAndMeasuredByContracts308, consumesServices327, decomposesServices330},
    generalizations={gen_contentfwk_BusinessArchitecture_Architecture, gen_contentfwk_DataArchitecture_Architecture, gen_contentfwk_TechnologyArchitecture_Architecture, gen_contentfwk_Objective_Element, gen_contentfwk_OrganizationUnit_Element, gen_contentfwk_Driver_Element, gen_contentfwk_Goal_Element, gen_contentfwk_Actor_Element, gen_contentfwk_Role_Element, gen_contentfwk_DataEntity_Element, gen_contentfwk_Function_Element, gen_contentfwk_Function_Standard, gen_contentfwk_LogicalApplicationComponent_Element, gen_contentfwk_LogicalApplicationComponent_ApplicationComponent, gen_contentfwk_BusinessService_Element, gen_contentfwk_BusinessService_Service, gen_contentfwk_Process_Element, gen_contentfwk_Process_Standard, gen_contentfwk_Product_Element, gen_contentfwk_Measure_Element, gen_contentfwk_PlatformService_Element, gen_contentfwk_PlatformService_Service, gen_contentfwk_PhysicalTechnologyComponent_Element, gen_contentfwk_PhysicalTechnologyComponent_TechnologyComponent, gen_contentfwk_ServiceQuality_Element, gen_contentfwk_Contract_Element, gen_contentfwk_Event_Element, gen_contentfwk_Control_Element, gen_contentfwk_Location_Element, gen_contentfwk_Constraint_StrategicElement, gen_contentfwk_Assumption_StrategicElement, gen_contentfwk_Requirement_StrategicElement, gen_contentfwk_Gap_StrategicElement, gen_contentfwk_WorkPackage_StrategicElement, gen_contentfwk_Capability_Element, gen_contentfwk_StrategicElement_Element, gen_contentfwk_Principle_StrategicElement, gen_contentfwk_ApplicationArchitecture_Architecture, gen_contentfwk_PhysicalApplicationComponent_Element, gen_contentfwk_PhysicalApplicationComponent_ApplicationComponent, gen_contentfwk_LogicalDataComponent_Element, gen_contentfwk_LogicalDataComponent_DataComponent, gen_contentfwk_PhysicalDataComponent_Element, gen_contentfwk_PhysicalDataComponent_DataComponent, gen_contentfwk_StrategicArchitecture_Architecture, gen_contentfwk_LogicalTechnologyComponent_Element, gen_contentfwk_LogicalTechnologyComponent_TechnologyComponent, gen_contentfwk_Service_Standard, gen_contentfwk_TechnologyComponent_Standard, gen_contentfwk_ApplicationComponent_Standard, gen_contentfwk_InformationSystemService_Service, gen_contentfwk_InformationSystemService_Element, gen_contentfwk_DataComponent_Standard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)