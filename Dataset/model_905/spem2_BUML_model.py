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
WorkSequenceKind: Enumeration = Enumeration(
    name="WorkSequenceKind",
    literals={
            EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

ActivityUseKind: Enumeration = Enumeration(
    name="ActivityUseKind",
    literals={
            EnumerationLiteral(name="na"),
			EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="localContribution"),
			EnumerationLiteral(name="localReplacement")
    }
)

OptionalityKind: Enumeration = Enumeration(
    name="OptionalityKind",
    literals={
            EnumerationLiteral(name="mandatory"),
			EnumerationLiteral(name="optional")
    }
)

VariabilityType: Enumeration = Enumeration(
    name="VariabilityType",
    literals={
            EnumerationLiteral(name="na"),
			EnumerationLiteral(name="contributes"),
			EnumerationLiteral(name="extends"),
			EnumerationLiteral(name="replaces"),
			EnumerationLiteral(name="extends_replaces")
    }
)

WorkProductRelationshipKind: Enumeration = Enumeration(
    name="WorkProductRelationshipKind",
    literals={
            EnumerationLiteral(name="impactedBy"),
			EnumerationLiteral(name="composition"),
			EnumerationLiteral(name="aggregation")
    }
)

RiskLevel: Enumeration = Enumeration(
    name="RiskLevel",
    literals={
            EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="MID"),
			EnumerationLiteral(name="HIGH")
    }
)

EstimatingTechnique: Enumeration = Enumeration(
    name="EstimatingTechnique",
    literals={
            EnumerationLiteral(name="COST"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="SKILLS"),
			EnumerationLiteral(name="DEFECTS"),
			EnumerationLiteral(name="OTHER")
    }
)

ContractKind: Enumeration = Enumeration(
    name="ContractKind",
    literals={
            EnumerationLiteral(name="EXPRESS"),
			EnumerationLiteral(name="IMPLIED"),
			EnumerationLiteral(name="OTHER")
    }
)

ExpertiseLevel: Enumeration = Enumeration(
    name="ExpertiseLevel",
    literals={
            EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="MID"),
			EnumerationLiteral(name="LEVEL")
    }
)

# Classes
spem_ExtensibleElement = Class(name="spem::ExtensibleElement", is_abstract=True)
spem_Kind = Class(name="spem::Kind")
ExtensibleElement = Class(name="ExtensibleElement")
spem_WorkDefinitionPerformer = Class(name="spem::WorkDefinitionPerformer", is_abstract=True)
spem_WorkDefinition = Class(name="spem::WorkDefinition", is_abstract=True)
spem_WorkDefinitionParameter = Class(name="spem::WorkDefinitionParameter")
spem_WorkSequence = Class(name="spem::WorkSequence")
spem_Activity = Class(name="spem::Activity")
WorkDefinition = Class(name="WorkDefinition")
WorkBreakdownElement = Class(name="WorkBreakdownElement")
VariabilityElement = Class(name="VariabilityElement")
spem_BreakdownElement = Class(name="spem::BreakdownElement", is_abstract=True)
ProcessElement = Class(name="ProcessElement")
spem_PlanningData = Class(name="spem::PlanningData")
spem_WorkBreakdownElement = Class(name="spem::WorkBreakdownElement", is_abstract=True)
BreakdownElement = Class(name="BreakdownElement")
spem_RoleUse = Class(name="spem::RoleUse")
spem_TaskUse = Class(name="spem::TaskUse")
MethodContentUse = Class(name="MethodContentUse")
spem_RoleDefinition = Class(name="spem::RoleDefinition")
spem_Qualification = Class(name="spem::Qualification")
spem_ProcessResponsibilityAssignment = Class(name="spem::ProcessResponsibilityAssignment")
spem_WorkProductUse = Class(name="spem::WorkProductUse")
spem_WorkProductDefinition = Class(name="spem::WorkProductDefinition")
spem_WorkProductUseRelationship = Class(name="spem::WorkProductUseRelationship")
spem_ProcessParameter = Class(name="spem::ProcessParameter")
spem_MethodConfiguration = Class(name="spem::MethodConfiguration")
spem_ProcessPerformer = Class(name="spem::ProcessPerformer")
WorkDefinitionPerformer = Class(name="WorkDefinitionPerformer")
spem_Guidance = Class(name="spem::Guidance")
spem_Metric = Class(name="spem::Metric")
spem_Category = Class(name="spem::Category")
MethodContentElement = Class(name="MethodContentElement")
spem_MethodContentElement = Class(name="spem::MethodContentElement", is_abstract=True)
MethodContentPackageableElement = Class(name="MethodContentPackageableElement")
spem_MethodContentKind = Class(name="spem::MethodContentKind", is_abstract=True)
WorkDefinitionParameter = Class(name="WorkDefinitionParameter")
spem_Milestone = Class(name="spem::Milestone")
spem_ProcessElement = Class(name="spem::ProcessElement", is_abstract=True)
DescribableElement = Class(name="DescribableElement")
ProcessPackageableElement = Class(name="ProcessPackageableElement")
spem_ProcessKind = Class(name="spem::ProcessKind", is_abstract=True)
spem_DescribableElement = Class(name="spem::DescribableElement", is_abstract=True)
spem_WorkProductDefinitionRelationship = Class(name="spem::WorkProductDefinitionRelationship")
spem_Default_TaskDefinitionPerformer = Class(name="spem::Default::TaskDefinitionPerformer")
spem_Default_ResponsibilityAssignment = Class(name="spem::Default::ResponsibilityAssignment")
spem_ToolDefinition = Class(name="spem::ToolDefinition")
spem_TaskDefinition = Class(name="spem::TaskDefinition")
spem_Default_TaskDefinitionParameter = Class(name="spem::Default::TaskDefinitionParameter")
spem_Step = Class(name="spem::Step")
spem_MethodContentPackage = Class(name="spem::MethodContentPackage")
MethodPluginPackageableElement = Class(name="MethodPluginPackageableElement")
spem_ProcessPackage = Class(name="spem::ProcessPackage")
Kind = Class(name="Kind")
spem_MethodContentUse = Class(name="spem::MethodContentUse", is_abstract=True)
spem_MethodContentPackageableElement = Class(name="spem::MethodContentPackageableElement", is_abstract=True)
spem_ProcessPackageableElement = Class(name="spem::ProcessPackageableElement", is_abstract=True)
spem_VariabilityElement = Class(name="spem::VariabilityElement", is_abstract=True)
spem_ProcessComponent = Class(name="spem::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
spem_WorkProductPort = Class(name="spem::WorkProductPort")
spem_ProcessComponentUse = Class(name="spem::ProcessComponentUse")
spem_MethodLibraryPackageableElement = Class(name="spem::MethodLibraryPackageableElement", is_abstract=True)
spem_MethodPluginPackageableElement = Class(name="spem::MethodPluginPackageableElement", is_abstract=True)
MethodLibraryPackageableElement = Class(name="MethodLibraryPackageableElement")
spem_MethodPlugin = Class(name="spem::MethodPlugin")
spem_CompositeRole = Class(name="spem::CompositeRole")
RoleUse = Class(name="RoleUse")
spem_TeamProfile = Class(name="spem::TeamProfile")
spem_MethodLibrary = Class(name="spem::MethodLibrary")
spem_WorkProductPortConnector = Class(name="spem::WorkProductPortConnector")
spem_uma_Process = Class(name="spem::uma::Process")
Activity = Class(name="Activity")
CapabilityPattern = Class(name="CapabilityPattern")
uma_spem_WorkProductPortConnector = Class(name="uma::spem::WorkProductPortConnector")
spem_uma_DeliveryProcess = Class(name="spem::uma::DeliveryProcess")
SupportingMaterial = Class(name="SupportingMaterial")
spem_uma_Artifact = Class(name="spem::uma::Artifact")
WorkProductUse = Class(name="WorkProductUse")
Artifact = Class(name="Artifact")
spem_uma_CapabilityPattern = Class(name="spem::uma::CapabilityPattern")
Process = Class(name="Process")
spem_uma_Checklist = Class(name="spem::uma::Checklist")
Guidance = Class(name="Guidance")
spem_uma_Concept = Class(name="spem::uma::Concept")
spem_uma_CategoryPackage = Class(name="spem::uma::CategoryPackage")
MethodContentPackage = Class(name="MethodContentPackage")
spem_uma_CustomCategory = Class(name="spem::uma::CustomCategory")
Category = Class(name="Category")
spem_uma_Deliverable = Class(name="spem::uma::Deliverable")
uma_spem_WorkProductUse = Class(name="uma::spem::WorkProductUse")
spem_uma_Discipline = Class(name="spem::uma::Discipline")
uma_spem_TaskDefinition = Class(name="uma::spem::TaskDefinition")
spem_uma_DisciplineGrouping = Class(name="spem::uma::DisciplineGrouping")
spem_uma_Root = Class(name="spem::uma::Root")
uma_spem_MethodConfiguration = Class(name="uma::spem::MethodConfiguration")
uma_spem_MethodLibrary = Class(name="uma::spem::MethodLibrary")
uma_spem_MethodPlugin = Class(name="uma::spem::MethodPlugin")
spem_uma_Domain = Class(name="spem::uma::Domain")
uma_spem_WorkProductDefinition = Class(name="uma::spem::WorkProductDefinition")
spem_uma_EstimatingConsideration = Class(name="spem::uma::EstimatingConsideration")
spem_uma_ProcessPlanningTemplate = Class(name="spem::uma::ProcessPlanningTemplate")
spem_uma_Report = Class(name="spem::uma::Report")
spem_uma_ReusableAsset = Class(name="spem::uma::ReusableAsset")
spem_uma_Roadmap = Class(name="spem::uma::Roadmap")
spem_uma_Template = Class(name="spem::uma::Template")
spem_uma_TermDefinition = Class(name="spem::uma::TermDefinition")
spem_uma_ToolMentor = Class(name="spem::uma::ToolMentor")
spem_uma_Whitepaper = Class(name="spem::uma::Whitepaper")
Concept = Class(name="Concept")
spem_uma_Guideline = Class(name="spem::uma::Guideline")
spem_uma_SupportingMaterial = Class(name="spem::uma::SupportingMaterial")
spem_uma_RoleDefinitionPackage = Class(name="spem::uma::RoleDefinitionPackage")
spem_uma_TaskDefinitionPackage = Class(name="spem::uma::TaskDefinitionPackage")
spem_uma_WorkProductDefinitionPackage = Class(name="spem::uma::WorkProductDefinitionPackage")
spem_uma_GuidancePackage = Class(name="spem::uma::GuidancePackage")
spem_uma_DisciplinePackage = Class(name="spem::uma::DisciplinePackage")
spem_uma_DomainPackage = Class(name="spem::uma::DomainPackage")
spem_uma_WorkProductKindPackage = Class(name="spem::uma::WorkProductKindPackage")
spem_uma_RoleSetPackage = Class(name="spem::uma::RoleSetPackage")
spem_uma_ToolDefinitionPackage = Class(name="spem::uma::ToolDefinitionPackage")
spem_uma_Example = Class(name="spem::uma::Example")
spem_uma_Iteration = Class(name="spem::uma::Iteration")
spem_uma_Outcome = Class(name="spem::uma::Outcome")
spem_uma_Phase = Class(name="spem::uma::Phase")
spem_uma_Practice = Class(name="spem::uma::Practice")
Practice = Class(name="Practice")
uma_spem_Activity = Class(name="uma::spem::Activity")
uma_spem_MethodContentElement = Class(name="uma::spem::MethodContentElement")
spem_uma_WorkProductKind = Class(name="spem::uma::WorkProductKind")
spem_uma_ConfigurationPackage = Class(name="spem::uma::ConfigurationPackage")
spem_uma_CapabilityPatternPackage = Class(name="spem::uma::CapabilityPatternPackage")
spem_uma_DeliveryProcessPackage = Class(name="spem::uma::DeliveryProcessPackage")
spem_uma_RoleSet = Class(name="spem::uma::RoleSet")
uma_spem_RoleDefinition = Class(name="uma::spem::RoleDefinition")
spem_uma_QualificationPackage = Class(name="spem::uma::QualificationPackage")
spem_uma_ProcessComponentPackage = Class(name="spem::uma::ProcessComponentPackage")

# spem_ExtensibleElement class attributes and methods

# spem_Kind class attributes and methods

# ExtensibleElement class attributes and methods

# spem_WorkDefinitionPerformer class attributes and methods

# spem_WorkDefinition class attributes and methods
spem_WorkDefinition_preCondition: Property = Property(name="preCondition", type=StringType)
spem_WorkDefinition_postCondition: Property = Property(name="postCondition", type=StringType)
spem_WorkDefinition.attributes={spem_WorkDefinition_postCondition, spem_WorkDefinition_preCondition}

# spem_WorkDefinitionParameter class attributes and methods
spem_WorkDefinitionParameter_direction: Property = Property(name="direction", type=StringType)
spem_WorkDefinitionParameter.attributes={spem_WorkDefinitionParameter_direction}

# spem_WorkSequence class attributes and methods
spem_WorkSequence_linkKind: Property = Property(name="linkKind", type=StringType)
spem_WorkSequence.attributes={spem_WorkSequence_linkKind}

# spem_Activity class attributes and methods
spem_Activity_useKind: Property = Property(name="useKind", type=StringType)
spem_Activity_isEnactable: Property = Property(name="isEnactable", type=BooleanType)
spem_Activity.attributes={spem_Activity_useKind, spem_Activity_isEnactable}

# WorkDefinition class attributes and methods

# WorkBreakdownElement class attributes and methods

# VariabilityElement class attributes and methods

# spem_BreakdownElement class attributes and methods
spem_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=BooleanType)
spem_BreakdownElement_isOptional: Property = Property(name="isOptional", type=BooleanType)
spem_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=BooleanType)
spem_BreakdownElement.attributes={spem_BreakdownElement_hasMultipleOccurrences, spem_BreakdownElement_isOptional, spem_BreakdownElement_isPlanned}

# ProcessElement class attributes and methods

# spem_PlanningData class attributes and methods
spem_PlanningData_startDate: Property = Property(name="startDate", type=DateType)
spem_PlanningData_finishDate: Property = Property(name="finishDate", type=DateType)
spem_PlanningData_rank: Property = Property(name="rank", type=IntegerType)
spem_PlanningData_duration: Property = Property(name="duration", type=StringType)
spem_PlanningData.attributes={spem_PlanningData_startDate, spem_PlanningData_duration, spem_PlanningData_rank, spem_PlanningData_finishDate}

# spem_WorkBreakdownElement class attributes and methods
spem_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=BooleanType)
spem_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=BooleanType)
spem_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=BooleanType)
spem_WorkBreakdownElement.attributes={spem_WorkBreakdownElement_isRepeatable, spem_WorkBreakdownElement_isEventDriven, spem_WorkBreakdownElement_isOngoing}

# BreakdownElement class attributes and methods

# spem_RoleUse class attributes and methods

# spem_TaskUse class attributes and methods
spem_TaskUse_preCondition: Property = Property(name="preCondition", type=StringType)
spem_TaskUse_postCondition: Property = Property(name="postCondition", type=StringType)
spem_TaskUse.attributes={spem_TaskUse_preCondition, spem_TaskUse_postCondition}

# MethodContentUse class attributes and methods

# spem_RoleDefinition class attributes and methods
spem_RoleDefinition_synonym: Property = Property(name="synonym", type=StringType)
spem_RoleDefinition.attributes={spem_RoleDefinition_synonym}

# spem_Qualification class attributes and methods

# spem_ProcessResponsibilityAssignment class attributes and methods

# spem_WorkProductUse class attributes and methods

# spem_WorkProductDefinition class attributes and methods

# spem_WorkProductUseRelationship class attributes and methods
spem_WorkProductUseRelationship_relationshipKind: Property = Property(name="relationshipKind", type=StringType)
spem_WorkProductUseRelationship.attributes={spem_WorkProductUseRelationship_relationshipKind}

# spem_ProcessParameter class attributes and methods
spem_ProcessParameter_optionality: Property = Property(name="optionality", type=StringType)
spem_ProcessParameter.attributes={spem_ProcessParameter_optionality}

# spem_MethodConfiguration class attributes and methods

# spem_ProcessPerformer class attributes and methods

# WorkDefinitionPerformer class attributes and methods

# spem_Guidance class attributes and methods

# spem_Metric class attributes and methods
spem_Metric_expression: Property = Property(name="expression", type=StringType)
spem_Metric.attributes={spem_Metric_expression}

# spem_Category class attributes and methods

# MethodContentElement class attributes and methods

# spem_MethodContentElement class attributes and methods

# MethodContentPackageableElement class attributes and methods

# spem_MethodContentKind class attributes and methods

# WorkDefinitionParameter class attributes and methods

# spem_Milestone class attributes and methods

# spem_ProcessElement class attributes and methods

# DescribableElement class attributes and methods

# ProcessPackageableElement class attributes and methods

# spem_ProcessKind class attributes and methods

# spem_DescribableElement class attributes and methods
spem_DescribableElement_presentationName: Property = Property(name="presentationName", type=StringType)
spem_DescribableElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
spem_DescribableElement_mainDescription: Property = Property(name="mainDescription", type=StringType)
spem_DescribableElement_purpose: Property = Property(name="purpose", type=StringType)
spem_DescribableElement_copyright: Property = Property(name="copyright", type=StringType)
spem_DescribableElement_author: Property = Property(name="author", type=StringType)
spem_DescribableElement_changeDate: Property = Property(name="changeDate", type=DateType)
spem_DescribableElement_changeDescription: Property = Property(name="changeDescription", type=StringType)
spem_DescribableElement_version: Property = Property(name="version", type=StringType)
spem_DescribableElement.attributes={spem_DescribableElement_presentationName, spem_DescribableElement_purpose, spem_DescribableElement_mainDescription, spem_DescribableElement_copyright, spem_DescribableElement_author, spem_DescribableElement_changeDescription, spem_DescribableElement_changeDate, spem_DescribableElement_briefDescription, spem_DescribableElement_version}

# spem_WorkProductDefinitionRelationship class attributes and methods

# spem_Default_TaskDefinitionPerformer class attributes and methods

# spem_Default_ResponsibilityAssignment class attributes and methods

# spem_ToolDefinition class attributes and methods

# spem_TaskDefinition class attributes and methods

# spem_Default_TaskDefinitionParameter class attributes and methods
spem_Default_TaskDefinitionParameter_name: Property = Property(name="name", type=StringType)
spem_Default_TaskDefinitionParameter_optionality: Property = Property(name="optionality", type=StringType)
spem_Default_TaskDefinitionParameter.attributes={spem_Default_TaskDefinitionParameter_optionality, spem_Default_TaskDefinitionParameter_name}

# spem_Step class attributes and methods
spem_Step_name: Property = Property(name="name", type=StringType)
spem_Step.attributes={spem_Step_name}

# spem_MethodContentPackage class attributes and methods

# MethodPluginPackageableElement class attributes and methods

# spem_ProcessPackage class attributes and methods

# Kind class attributes and methods

# spem_MethodContentUse class attributes and methods
spem_MethodContentUse_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=BooleanType)
spem_MethodContentUse.attributes={spem_MethodContentUse_isSynchronizedWithSource}

# spem_MethodContentPackageableElement class attributes and methods
spem_MethodContentPackageableElement_name: Property = Property(name="name", type=StringType)
spem_MethodContentPackageableElement.attributes={spem_MethodContentPackageableElement_name}

# spem_ProcessPackageableElement class attributes and methods
spem_ProcessPackageableElement_name: Property = Property(name="name", type=StringType)
spem_ProcessPackageableElement.attributes={spem_ProcessPackageableElement_name}

# spem_VariabilityElement class attributes and methods
spem_VariabilityElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
spem_VariabilityElement.attributes={spem_VariabilityElement_variabilityType}

# spem_ProcessComponent class attributes and methods

# ProcessPackage class attributes and methods

# spem_WorkProductPort class attributes and methods
spem_WorkProductPort_isOptional: Property = Property(name="isOptional", type=BooleanType)
spem_WorkProductPort_portKind: Property = Property(name="portKind", type=StringType)
spem_WorkProductPort.attributes={spem_WorkProductPort_portKind, spem_WorkProductPort_isOptional}

# spem_ProcessComponentUse class attributes and methods

# spem_MethodLibraryPackageableElement class attributes and methods
spem_MethodLibraryPackageableElement_name: Property = Property(name="name", type=StringType)
spem_MethodLibraryPackageableElement.attributes={spem_MethodLibraryPackageableElement_name}

# spem_MethodPluginPackageableElement class attributes and methods

# MethodLibraryPackageableElement class attributes and methods

# spem_MethodPlugin class attributes and methods

# spem_CompositeRole class attributes and methods

# RoleUse class attributes and methods

# spem_TeamProfile class attributes and methods

# spem_MethodLibrary class attributes and methods
spem_MethodLibrary_name: Property = Property(name="name", type=StringType)
spem_MethodLibrary.attributes={spem_MethodLibrary_name}

# spem_WorkProductPortConnector class attributes and methods

# spem_uma_Process class attributes and methods
spem_uma_Process_scope: Property = Property(name="scope", type=StringType)
spem_uma_Process_usageNote: Property = Property(name="usageNote", type=StringType)
spem_uma_Process.attributes={spem_uma_Process_scope, spem_uma_Process_usageNote}

# Activity class attributes and methods

# CapabilityPattern class attributes and methods

# uma_spem_WorkProductPortConnector class attributes and methods

# spem_uma_DeliveryProcess class attributes and methods
spem_uma_DeliveryProcess_scale: Property = Property(name="scale", type=StringType)
spem_uma_DeliveryProcess_projectCharacteristics: Property = Property(name="projectCharacteristics", type=StringType)
spem_uma_DeliveryProcess_riskLevel: Property = Property(name="riskLevel", type=StringType)
spem_uma_DeliveryProcess_estimatingTechnique: Property = Property(name="estimatingTechnique", type=StringType)
spem_uma_DeliveryProcess_projectMemberExpertise: Property = Property(name="projectMemberExpertise", type=StringType)
spem_uma_DeliveryProcess_typeOfContract: Property = Property(name="typeOfContract", type=StringType)
spem_uma_DeliveryProcess.attributes={spem_uma_DeliveryProcess_projectMemberExpertise, spem_uma_DeliveryProcess_estimatingTechnique, spem_uma_DeliveryProcess_typeOfContract, spem_uma_DeliveryProcess_riskLevel, spem_uma_DeliveryProcess_scale, spem_uma_DeliveryProcess_projectCharacteristics}

# SupportingMaterial class attributes and methods

# spem_uma_Artifact class attributes and methods

# WorkProductUse class attributes and methods

# Artifact class attributes and methods

# spem_uma_CapabilityPattern class attributes and methods

# Process class attributes and methods

# spem_uma_Checklist class attributes and methods

# Guidance class attributes and methods

# spem_uma_Concept class attributes and methods

# spem_uma_CategoryPackage class attributes and methods

# MethodContentPackage class attributes and methods

# spem_uma_CustomCategory class attributes and methods

# Category class attributes and methods

# spem_uma_Deliverable class attributes and methods
spem_uma_Deliverable_externalDescription: Property = Property(name="externalDescription", type=StringType)
spem_uma_Deliverable_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
spem_uma_Deliverable.attributes={spem_uma_Deliverable_packagingGuidance, spem_uma_Deliverable_externalDescription}

# uma_spem_WorkProductUse class attributes and methods

# spem_uma_Discipline class attributes and methods

# uma_spem_TaskDefinition class attributes and methods

# spem_uma_DisciplineGrouping class attributes and methods

# spem_uma_Root class attributes and methods

# uma_spem_MethodConfiguration class attributes and methods

# uma_spem_MethodLibrary class attributes and methods

# uma_spem_MethodPlugin class attributes and methods

# spem_uma_Domain class attributes and methods

# uma_spem_WorkProductDefinition class attributes and methods

# spem_uma_EstimatingConsideration class attributes and methods

# spem_uma_ProcessPlanningTemplate class attributes and methods

# spem_uma_Report class attributes and methods

# spem_uma_ReusableAsset class attributes and methods

# spem_uma_Roadmap class attributes and methods

# spem_uma_Template class attributes and methods

# spem_uma_TermDefinition class attributes and methods

# spem_uma_ToolMentor class attributes and methods

# spem_uma_Whitepaper class attributes and methods

# Concept class attributes and methods

# spem_uma_Guideline class attributes and methods

# spem_uma_SupportingMaterial class attributes and methods

# spem_uma_RoleDefinitionPackage class attributes and methods

# spem_uma_TaskDefinitionPackage class attributes and methods

# spem_uma_WorkProductDefinitionPackage class attributes and methods

# spem_uma_GuidancePackage class attributes and methods

# spem_uma_DisciplinePackage class attributes and methods

# spem_uma_DomainPackage class attributes and methods

# spem_uma_WorkProductKindPackage class attributes and methods

# spem_uma_RoleSetPackage class attributes and methods

# spem_uma_ToolDefinitionPackage class attributes and methods

# spem_uma_Example class attributes and methods

# spem_uma_Iteration class attributes and methods

# spem_uma_Outcome class attributes and methods

# spem_uma_Phase class attributes and methods

# spem_uma_Practice class attributes and methods
spem_uma_Practice_background: Property = Property(name="background", type=StringType)
spem_uma_Practice_goal: Property = Property(name="goal", type=StringType)
spem_uma_Practice_levelOfAdoption: Property = Property(name="levelOfAdoption", type=StringType)
spem_uma_Practice_problem: Property = Property(name="problem", type=StringType)
spem_uma_Practice_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
spem_uma_Practice_application: Property = Property(name="application", type=StringType)
spem_uma_Practice.attributes={spem_uma_Practice_problem, spem_uma_Practice_application, spem_uma_Practice_goal, spem_uma_Practice_levelOfAdoption, spem_uma_Practice_additionalInfo, spem_uma_Practice_background}

# Practice class attributes and methods

# uma_spem_Activity class attributes and methods

# uma_spem_MethodContentElement class attributes and methods

# spem_uma_WorkProductKind class attributes and methods

# spem_uma_ConfigurationPackage class attributes and methods

# spem_uma_CapabilityPatternPackage class attributes and methods

# spem_uma_DeliveryProcessPackage class attributes and methods

# spem_uma_RoleSet class attributes and methods

# uma_spem_RoleDefinition class attributes and methods

# spem_uma_QualificationPackage class attributes and methods

# spem_uma_ProcessComponentPackage class attributes and methods

# Relationships
kind0: BinaryAssociation = BinaryAssociation(
    name="kind0",
    ends={
        Property(name="spem_Kind", type=spem_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ExtensibleElement", type=spem_Kind, multiplicity=Multiplicity(0, 1))
    }
)
linkedWorkDefinition1: BinaryAssociation = BinaryAssociation(
    name="linkedWorkDefinition1",
    ends={
        Property(name="spem_WorkDefinition", type=spem_WorkDefinitionPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkDefinitionPerformer", type=spem_WorkDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter2: BinaryAssociation = BinaryAssociation(
    name="ownedParameter2",
    ends={
        Property(name="spem_WorkDefinitionParameter", type=spem_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkDefinition3", type=spem_WorkDefinitionParameter, multiplicity=Multiplicity(0, 9999))
    }
)
linkToPredecessor5: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor5",
    ends={
        Property(name="WorkSequence", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linkToSuccessor6: BinaryAssociation = BinaryAssociation(
    name="linkToSuccessor6",
    ends={
        Property(name="WorkSequence7", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor8: BinaryAssociation = BinaryAssociation(
    name="predecessor8",
    ends={
        Property(name="WorkBreakdownElement", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToSuccessor", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
successor9: BinaryAssociation = BinaryAssociation(
    name="successor9",
    ends={
        Property(name="WorkBreakdownElement10", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToPredecessor", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
usedActivity12: BinaryAssociation = BinaryAssociation(
    name="usedActivity12",
    ends={
        Property(name="spem_Activity", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity11", type=spem_Activity, multiplicity=Multiplicity(0, 1))
    }
)
nestedBreakdownElement13: BinaryAssociation = BinaryAssociation(
    name="nestedBreakdownElement13",
    ends={
        Property(name="spem_BreakdownElement15", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity14", type=spem_BreakdownElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
planningData4: BinaryAssociation = BinaryAssociation(
    name="planningData4",
    ends={
        Property(name="spem_PlanningData", type=spem_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_BreakdownElement", type=spem_PlanningData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkedRoleUse26: BinaryAssociation = BinaryAssociation(
    name="linkedRoleUse26",
    ends={
        Property(name="spem_RoleUse", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer", type=spem_RoleUse, multiplicity=Multiplicity(1, 9999))
    }
)
linkedActivity27: BinaryAssociation = BinaryAssociation(
    name="linkedActivity27",
    ends={
        Property(name="spem_Activity29", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer28", type=spem_Activity, multiplicity=Multiplicity(0, 1))
    }
)
linkedTaskUse30: BinaryAssociation = BinaryAssociation(
    name="linkedTaskUse30",
    ends={
        Property(name="spem_TaskUse", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer31", type=spem_TaskUse, multiplicity=Multiplicity(0, 1))
    }
)
role32: BinaryAssociation = BinaryAssociation(
    name="role32",
    ends={
        Property(name="spem_RoleDefinition", type=spem_RoleUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_RoleUse33", type=spem_RoleDefinition, multiplicity=Multiplicity(0, 1))
    }
)
appliedQualification34: BinaryAssociation = BinaryAssociation(
    name="appliedQualification34",
    ends={
        Property(name="spem_Qualification", type=spem_RoleUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_RoleUse35", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
linkedRoleUse36: BinaryAssociation = BinaryAssociation(
    name="linkedRoleUse36",
    ends={
        Property(name="spem_RoleUse37", type=spem_ProcessResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessResponsibilityAssignment", type=spem_RoleUse, multiplicity=Multiplicity(1, 9999))
    }
)
linkedWorkProductUse38: BinaryAssociation = BinaryAssociation(
    name="linkedWorkProductUse38",
    ends={
        Property(name="spem_WorkProductUse", type=spem_ProcessResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessResponsibilityAssignment39", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1))
    }
)
workProduct40: BinaryAssociation = BinaryAssociation(
    name="workProduct40",
    ends={
        Property(name="spem_WorkProductDefinition", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUse41", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1))
    }
)
source42: BinaryAssociation = BinaryAssociation(
    name="source42",
    ends={
        Property(name="spem_WorkProductUse43", type=spem_WorkProductUseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUseRelationship", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1))
    }
)
target44: BinaryAssociation = BinaryAssociation(
    name="target44",
    ends={
        Property(name="spem_WorkProductUse46", type=spem_WorkProductUseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUseRelationship45", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 9999))
    }
)
suppressedBreakdownElement16: BinaryAssociation = BinaryAssociation(
    name="suppressedBreakdownElement16",
    ends={
        Property(name="spem_BreakdownElement18", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity17", type=spem_BreakdownElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedProcessParameter19: BinaryAssociation = BinaryAssociation(
    name="ownedProcessParameter19",
    ends={
        Property(name="spem_ProcessParameter", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity20", type=spem_ProcessParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultContext21: BinaryAssociation = BinaryAssociation(
    name="defaultContext21",
    ends={
        Property(name="spem_MethodConfiguration", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity22", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
validContext23: BinaryAssociation = BinaryAssociation(
    name="validContext23",
    ends={
        Property(name="spem_MethodConfiguration25", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity24", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
guidance53: BinaryAssociation = BinaryAssociation(
    name="guidance53",
    ends={
        Property(name="spem_Guidance", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement", type=spem_Guidance, multiplicity=Multiplicity(0, 9999))
    }
)
metric54: BinaryAssociation = BinaryAssociation(
    name="metric54",
    ends={
        Property(name="spem_Metric", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement55", type=spem_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
category56: BinaryAssociation = BinaryAssociation(
    name="category56",
    ends={
        Property(name="Category", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="categorizedElement", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
subCategory58: BinaryAssociation = BinaryAssociation(
    name="subCategory58",
    ends={
        Property(name="spem_Category", type=spem_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Category57", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
categorizedElement59: BinaryAssociation = BinaryAssociation(
    name="categorizedElement59",
    ends={
        Property(name="DescribableElement", type=spem_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=spem_DescribableElement, multiplicity=Multiplicity(0, 9999))
    }
)
parameterType47: BinaryAssociation = BinaryAssociation(
    name="parameterType47",
    ends={
        Property(name="spem_WorkProductUse49", type=spem_ProcessParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessParameter48", type=spem_WorkProductUse, multiplicity=Multiplicity(0, 1))
    }
)
requiredResult50: BinaryAssociation = BinaryAssociation(
    name="requiredResult50",
    ends={
        Property(name="spem_WorkProductUse51", type=spem_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Milestone", type=spem_WorkProductUse, multiplicity=Multiplicity(0, 9999))
    }
)
processKind52: BinaryAssociation = BinaryAssociation(
    name="processKind52",
    ends={
        Property(name="spem_ProcessKind", type=spem_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessElement", type=spem_ProcessKind, multiplicity=Multiplicity(0, 1))
    }
)
predecessor73: BinaryAssociation = BinaryAssociation(
    name="predecessor73",
    ends={
        Property(name="Step", type=spem_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="successor74", type=spem_Step, multiplicity=Multiplicity(0, 1))
    }
)
successor76: BinaryAssociation = BinaryAssociation(
    name="successor76",
    ends={
        Property(name="Step78", type=spem_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor77", type=spem_Step, multiplicity=Multiplicity(0, 1))
    }
)
providedQualification79: BinaryAssociation = BinaryAssociation(
    name="providedQualification79",
    ends={
        Property(name="spem_Qualification81", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_RoleDefinition80", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
source82: BinaryAssociation = BinaryAssociation(
    name="source82",
    ends={
        Property(name="spem_WorkProductDefinition83", type=spem_WorkProductDefinitionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinitionRelationship", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1))
    }
)
target84: BinaryAssociation = BinaryAssociation(
    name="target84",
    ends={
        Property(name="spem_WorkProductDefinition86", type=spem_WorkProductDefinitionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinitionRelationship85", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
linkedTaskDefinition87: BinaryAssociation = BinaryAssociation(
    name="linkedTaskDefinition87",
    ends={
        Property(name="spem_TaskDefinition88", type=spem_Default_TaskDefinitionPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_TaskDefinitionPerformer", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1))
    }
)
linkedRoleDefinition89: BinaryAssociation = BinaryAssociation(
    name="linkedRoleDefinition89",
    ends={
        Property(name="spem_RoleDefinition91", type=spem_Default_TaskDefinitionPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_TaskDefinitionPerformer90", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
linkedRoleDefinition92: BinaryAssociation = BinaryAssociation(
    name="linkedRoleDefinition92",
    ends={
        Property(name="spem_RoleDefinition93", type=spem_Default_ResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_ResponsibilityAssignment", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
methodContentKind60: BinaryAssociation = BinaryAssociation(
    name="methodContentKind60",
    ends={
        Property(name="spem_MethodContentKind", type=spem_MethodContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentElement", type=spem_MethodContentKind, multiplicity=Multiplicity(0, 1))
    }
)
managedWorkProduct61: BinaryAssociation = BinaryAssociation(
    name="managedWorkProduct61",
    ends={
        Property(name="spem_WorkProductDefinition62", type=spem_ToolDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ToolDefinition", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTaskDefinitionParameter63: BinaryAssociation = BinaryAssociation(
    name="ownedTaskDefinitionParameter63",
    ends={
        Property(name="spem_Default_TaskDefinitionParameter", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition", type=spem_Default_TaskDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedTool64: BinaryAssociation = BinaryAssociation(
    name="usedTool64",
    ends={
        Property(name="spem_ToolDefinition66", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition65", type=spem_ToolDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
step67: BinaryAssociation = BinaryAssociation(
    name="step67",
    ends={
        Property(name="spem_Step", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition68", type=spem_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredQualification69: BinaryAssociation = BinaryAssociation(
    name="requiredQualification69",
    ends={
        Property(name="spem_Qualification71", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition70", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodContentMember100: BinaryAssociation = BinaryAssociation(
    name="ownedMethodContentMember100",
    ends={
        Property(name="spem_MethodContentPackageableElement", type=spem_MethodContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentPackage", type=spem_MethodContentPackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedPackage102: BinaryAssociation = BinaryAssociation(
    name="reusedPackage102",
    ends={
        Property(name="spem_MethodContentPackage103", type=spem_MethodContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentPackage101", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedProcessMember104: BinaryAssociation = BinaryAssociation(
    name="ownedProcessMember104",
    ends={
        Property(name="spem_ProcessPackageableElement", type=spem_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPackage", type=spem_ProcessPackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task105: BinaryAssociation = BinaryAssociation(
    name="task105",
    ends={
        Property(name="spem_TaskDefinition107", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse106", type=spem_TaskDefinition, multiplicity=Multiplicity(0, 1))
    }
)
usedQualification108: BinaryAssociation = BinaryAssociation(
    name="usedQualification108",
    ends={
        Property(name="spem_Qualification110", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse109", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
selectedStep111: BinaryAssociation = BinaryAssociation(
    name="selectedStep111",
    ends={
        Property(name="spem_Step113", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse112", type=spem_Step, multiplicity=Multiplicity(0, 9999))
    }
)
linkedWorkProductDefinition94: BinaryAssociation = BinaryAssociation(
    name="linkedWorkProductDefinition94",
    ends={
        Property(name="spem_WorkProductDefinition96", type=spem_Default_ResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_ResponsibilityAssignment95", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parameterType97: BinaryAssociation = BinaryAssociation(
    name="parameterType97",
    ends={
        Property(name="spem_WorkProductDefinition99", type=spem_Default_TaskDefinitionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_TaskDefinitionParameter98", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1))
    }
)
teamRole124: BinaryAssociation = BinaryAssociation(
    name="teamRole124",
    ends={
        Property(name="spem_RoleUse125", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TeamProfile", type=spem_RoleUse, multiplicity=Multiplicity(0, 9999))
    }
)
variabilityBasedOnElement127: BinaryAssociation = BinaryAssociation(
    name="variabilityBasedOnElement127",
    ends={
        Property(name="spem_VariabilityElement", type=spem_VariabilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_VariabilityElement126", type=spem_VariabilityElement, multiplicity=Multiplicity(0, 1))
    }
)
process128: BinaryAssociation = BinaryAssociation(
    name="process128",
    ends={
        Property(name="spem_Activity129", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponent", type=spem_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPort130: BinaryAssociation = BinaryAssociation(
    name="ownedPort130",
    ends={
        Property(name="spem_WorkProductPort", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponent131", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processComponent132: BinaryAssociation = BinaryAssociation(
    name="processComponent132",
    ends={
        Property(name="spem_ProcessComponent133", type=spem_ProcessComponentUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponentUse", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
usedPort134: BinaryAssociation = BinaryAssociation(
    name="usedPort134",
    ends={
        Property(name="spem_WorkProductPort136", type=spem_ProcessComponentUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponentUse135", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseConfiguration138: BinaryAssociation = BinaryAssociation(
    name="baseConfiguration138",
    ends={
        Property(name="spem_MethodConfiguration139", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration137", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
methodPluginSelection140: BinaryAssociation = BinaryAssociation(
    name="methodPluginSelection140",
    ends={
        Property(name="spem_MethodPlugin", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration141", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 9999))
    }
)
ownedProcessParameter114: BinaryAssociation = BinaryAssociation(
    name="ownedProcessParameter114",
    ends={
        Property(name="spem_ProcessParameter116", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse115", type=spem_ProcessParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregatedRole117: BinaryAssociation = BinaryAssociation(
    name="aggregatedRole117",
    ends={
        Property(name="spem_RoleDefinition118", type=spem_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_CompositeRole", type=spem_RoleDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
subTeam120: BinaryAssociation = BinaryAssociation(
    name="subTeam120",
    ends={
        Property(name="TeamProfile", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="superTeam", type=spem_TeamProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTeam122: BinaryAssociation = BinaryAssociation(
    name="superTeam122",
    ends={
        Property(name="TeamProfile123", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="subTeam", type=spem_TeamProfile, multiplicity=Multiplicity(0, 1))
    }
)
ownedProcessPackage160: BinaryAssociation = BinaryAssociation(
    name="ownedProcessPackage160",
    ends={
        Property(name="spem_ProcessPackage162", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin161", type=spem_ProcessPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePlugin164: BinaryAssociation = BinaryAssociation(
    name="basePlugin164",
    ends={
        Property(name="spem_MethodPlugin165", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin163", type=spem_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodPlugin166: BinaryAssociation = BinaryAssociation(
    name="ownedMethodPlugin166",
    ends={
        Property(name="spem_MethodPlugin167", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary", type=spem_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predefinedConfiguration168: BinaryAssociation = BinaryAssociation(
    name="predefinedConfiguration168",
    ends={
        Property(name="spem_MethodConfiguration170", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary169", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configurationPackage171: BinaryAssociation = BinaryAssociation(
    name="configurationPackage171",
    ends={
        Property(name="spem_MethodContentPackage173", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary172", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
portType174: BinaryAssociation = BinaryAssociation(
    name="portType174",
    ends={
        Property(name="spem_WorkProductDefinition176", type=spem_WorkProductPort, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductPort175", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1))
    }
)
connectedPort177: BinaryAssociation = BinaryAssociation(
    name="connectedPort177",
    ends={
        Property(name="spem_WorkProductPort178", type=spem_WorkProductPortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductPortConnector", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999))
    }
)
processPackageSelection142: BinaryAssociation = BinaryAssociation(
    name="processPackageSelection142",
    ends={
        Property(name="spem_ProcessPackage144", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration143", type=spem_ProcessPackage, multiplicity=Multiplicity(0, 9999))
    }
)
contentPackageSelection145: BinaryAssociation = BinaryAssociation(
    name="contentPackageSelection145",
    ends={
        Property(name="spem_MethodContentPackage147", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration146", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999))
    }
)
substractedCategory148: BinaryAssociation = BinaryAssociation(
    name="substractedCategory148",
    ends={
        Property(name="spem_Category150", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration149", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
defaultView151: BinaryAssociation = BinaryAssociation(
    name="defaultView151",
    ends={
        Property(name="spem_Category153", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration152", type=spem_Category, multiplicity=Multiplicity(1, 1))
    }
)
processView154: BinaryAssociation = BinaryAssociation(
    name="processView154",
    ends={
        Property(name="spem_Category156", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration155", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodContentPackage157: BinaryAssociation = BinaryAssociation(
    name="ownedMethodContentPackage157",
    ends={
        Property(name="spem_MethodContentPackage159", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin158", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deliveredProduct180: BinaryAssociation = BinaryAssociation(
    name="deliveredProduct180",
    ends={
        Property(name="uma_spem_WorkProductUse", type=spem_uma_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Deliverable", type=uma_spem_WorkProductUse, multiplicity=Multiplicity(0, 9999))
    }
)
includedPattern181: BinaryAssociation = BinaryAssociation(
    name="includedPattern181",
    ends={
        Property(name="CapabilityPattern", type=spem_uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Process", type=CapabilityPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedConnector182: BinaryAssociation = BinaryAssociation(
    name="includedConnector182",
    ends={
        Property(name="uma_spem_WorkProductPortConnector", type=spem_uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Process183", type=uma_spem_WorkProductPortConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communicationMaterial184: BinaryAssociation = BinaryAssociation(
    name="communicationMaterial184",
    ends={
        Property(name="SupportingMaterial", type=spem_uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_DeliveryProcess", type=SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
educationalMaterial185: BinaryAssociation = BinaryAssociation(
    name="educationalMaterial185",
    ends={
        Property(name="SupportingMaterial187", type=spem_uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_DeliveryProcess186", type=SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
containedArtifact179: BinaryAssociation = BinaryAssociation(
    name="containedArtifact179",
    ends={
        Property(name="Artifact", type=spem_uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Artifact", type=Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedTask188: BinaryAssociation = BinaryAssociation(
    name="relatedTask188",
    ends={
        Property(name="uma_spem_TaskDefinition", type=spem_uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Discipline", type=uma_spem_TaskDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
relatedWorflow189: BinaryAssociation = BinaryAssociation(
    name="relatedWorflow189",
    ends={
        Property(name="Process", type=spem_uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Discipline190", type=Process, multiplicity=Multiplicity(0, 9999))
    }
)
methodConfiguration191: BinaryAssociation = BinaryAssociation(
    name="methodConfiguration191",
    ends={
        Property(name="uma_spem_MethodConfiguration", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root", type=uma_spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodLibrary192: BinaryAssociation = BinaryAssociation(
    name="methodLibrary192",
    ends={
        Property(name="uma_spem_MethodLibrary", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root193", type=uma_spem_MethodLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MethodPlugin194: BinaryAssociation = BinaryAssociation(
    name="MethodPlugin194",
    ends={
        Property(name="uma_spem_MethodPlugin", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root195", type=uma_spem_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedProduct196: BinaryAssociation = BinaryAssociation(
    name="relatedProduct196",
    ends={
        Property(name="uma_spem_WorkProductDefinition", type=spem_uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Domain", type=uma_spem_WorkProductDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
baseProcess202: BinaryAssociation = BinaryAssociation(
    name="baseProcess202",
    ends={
        Property(name="Process203", type=spem_uma_ProcessPlanningTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_ProcessPlanningTemplate", type=Process, multiplicity=Multiplicity(0, 9999))
    }
)
subPractice197: BinaryAssociation = BinaryAssociation(
    name="subPractice197",
    ends={
        Property(name="Practice", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice", type=Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedActivity198: BinaryAssociation = BinaryAssociation(
    name="referencedActivity198",
    ends={
        Property(name="uma_spem_Activity", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice199", type=uma_spem_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
contentReference200: BinaryAssociation = BinaryAssociation(
    name="contentReference200",
    ends={
        Property(name="uma_spem_MethodContentElement", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice201", type=uma_spem_MethodContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConfiguration204: BinaryAssociation = BinaryAssociation(
    name="ownedConfiguration204",
    ends={
        Property(name="uma_spem_MethodConfiguration205", type=spem_uma_ConfigurationPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_ConfigurationPackage", type=uma_spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role206: BinaryAssociation = BinaryAssociation(
    name="role206",
    ends={
        Property(name="uma_spem_RoleDefinition", type=spem_uma_RoleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_RoleSet", type=uma_spem_RoleDefinition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_spem_Kind_ExtensibleElement = Generalization(general=ExtensibleElement, specific=spem_Kind)
gen_spem_WorkSequence_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkSequence)
gen_spem_Activity_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_Activity)
gen_spem_Activity_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_Activity)
gen_spem_Activity_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_Activity)
gen_spem_BreakdownElement_ProcessElement = Generalization(general=ProcessElement, specific=spem_BreakdownElement)
gen_spem_WorkBreakdownElement_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkBreakdownElement)
gen_spem_RoleUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_RoleUse)
gen_spem_ProcessResponsibilityAssignment_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_ProcessResponsibilityAssignment)
gen_spem_WorkProductUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_WorkProductUse)
gen_spem_WorkProductUseRelationship_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkProductUseRelationship)
gen_spem_ProcessPerformer_WorkDefinitionPerformer = Generalization(general=WorkDefinitionPerformer, specific=spem_ProcessPerformer)
gen_spem_ProcessPerformer_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_ProcessPerformer)
gen_spem_Category_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Category)
gen_spem_Guidance_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Guidance)
gen_spem_Metric_DescribableElement = Generalization(general=DescribableElement, specific=spem_Metric)
gen_spem_MethodContentElement_DescribableElement = Generalization(general=DescribableElement, specific=spem_MethodContentElement)
gen_spem_MethodContentElement_MethodContentPackageableElement = Generalization(general=MethodContentPackageableElement, specific=spem_MethodContentElement)
gen_spem_MethodContentElement_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_MethodContentElement)
gen_spem_ProcessParameter_WorkDefinitionParameter = Generalization(general=WorkDefinitionParameter, specific=spem_ProcessParameter)
gen_spem_ProcessParameter_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_ProcessParameter)
gen_spem_Milestone_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_Milestone)
gen_spem_ProcessElement_DescribableElement = Generalization(general=DescribableElement, specific=spem_ProcessElement)
gen_spem_ProcessElement_ProcessPackageableElement = Generalization(general=ProcessPackageableElement, specific=spem_ProcessElement)
gen_spem_DescribableElement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=spem_DescribableElement)
gen_spem_Step_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_Step)
gen_spem_Step_DescribableElement = Generalization(general=DescribableElement, specific=spem_Step)
gen_spem_Step_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_Step)
gen_spem_WorkProductDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_WorkProductDefinition)
gen_spem_RoleDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_RoleDefinition)
gen_spem_WorkProductDefinitionRelationship_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_WorkProductDefinitionRelationship)
gen_spem_Default_TaskDefinitionPerformer_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Default_TaskDefinitionPerformer)
gen_spem_Default_ResponsibilityAssignment_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Default_ResponsibilityAssignment)
gen_spem_ToolDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_ToolDefinition)
gen_spem_TaskDefinition_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_TaskDefinition)
gen_spem_TaskDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_TaskDefinition)
gen_spem_MethodContentPackage_MethodContentPackageableElement = Generalization(general=MethodContentPackageableElement, specific=spem_MethodContentPackage)
gen_spem_MethodContentPackage_MethodPluginPackageableElement = Generalization(general=MethodPluginPackageableElement, specific=spem_MethodContentPackage)
gen_spem_ProcessPackage_ProcessPackageableElement = Generalization(general=ProcessPackageableElement, specific=spem_ProcessPackage)
gen_spem_ProcessPackage_MethodPluginPackageableElement = Generalization(general=MethodPluginPackageableElement, specific=spem_ProcessPackage)
gen_spem_MethodContentKind_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_MethodContentKind)
gen_spem_MethodContentKind_Kind = Generalization(general=Kind, specific=spem_MethodContentKind)
gen_spem_ProcessKind_ProcessElement = Generalization(general=ProcessElement, specific=spem_ProcessKind)
gen_spem_ProcessKind_Kind = Generalization(general=Kind, specific=spem_ProcessKind)
gen_spem_PlanningData_ProcessElement = Generalization(general=ProcessElement, specific=spem_PlanningData)
gen_spem_MethodContentUse_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_MethodContentUse)
gen_spem_TaskUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_TaskUse)
gen_spem_TaskUse_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_TaskUse)
gen_spem_Default_TaskDefinitionParameter_WorkDefinitionParameter = Generalization(general=WorkDefinitionParameter, specific=spem_Default_TaskDefinitionParameter)
gen_spem_Qualification_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Qualification)
gen_spem_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_ProcessComponent)
gen_spem_ProcessComponentUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_ProcessComponentUse)
gen_spem_MethodConfiguration_MethodLibraryPackageableElement = Generalization(general=MethodLibraryPackageableElement, specific=spem_MethodConfiguration)
gen_spem_CompositeRole_RoleUse = Generalization(general=RoleUse, specific=spem_CompositeRole)
gen_spem_TeamProfile_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_TeamProfile)
gen_spem_WorkProductPort_ProcessElement = Generalization(general=ProcessElement, specific=spem_WorkProductPort)
gen_spem_WorkProductPortConnector_ProcessElement = Generalization(general=ProcessElement, specific=spem_WorkProductPortConnector)
gen_spem_MethodPlugin_MethodLibraryPackageableElement = Generalization(general=MethodLibraryPackageableElement, specific=spem_MethodPlugin)
gen_spem_uma_Process_Activity = Generalization(general=Activity, specific=spem_uma_Process)
gen_spem_uma_DeliveryProcess_Process = Generalization(general=Process, specific=spem_uma_DeliveryProcess)
gen_spem_uma_Artifact_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Artifact)
gen_spem_uma_CapabilityPattern_Process = Generalization(general=Process, specific=spem_uma_CapabilityPattern)
gen_spem_uma_Checklist_Guidance = Generalization(general=Guidance, specific=spem_uma_Checklist)
gen_spem_uma_Concept_Guidance = Generalization(general=Guidance, specific=spem_uma_Concept)
gen_spem_uma_CategoryPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_CategoryPackage)
gen_spem_uma_CustomCategory_Category = Generalization(general=Category, specific=spem_uma_CustomCategory)
gen_spem_uma_Deliverable_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Deliverable)
gen_spem_uma_Discipline_Category = Generalization(general=Category, specific=spem_uma_Discipline)
gen_spem_uma_DisciplineGrouping_Category = Generalization(general=Category, specific=spem_uma_DisciplineGrouping)
gen_spem_uma_Domain_Category = Generalization(general=Category, specific=spem_uma_Domain)
gen_spem_uma_EstimatingConsideration_Guidance = Generalization(general=Guidance, specific=spem_uma_EstimatingConsideration)
gen_spem_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=spem_uma_ProcessPlanningTemplate)
gen_spem_uma_Report_Guidance = Generalization(general=Guidance, specific=spem_uma_Report)
gen_spem_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=spem_uma_ReusableAsset)
gen_spem_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=spem_uma_Roadmap)
gen_spem_uma_Template_Guidance = Generalization(general=Guidance, specific=spem_uma_Template)
gen_spem_uma_TermDefinition_Guidance = Generalization(general=Guidance, specific=spem_uma_TermDefinition)
gen_spem_uma_ToolMentor_Guidance = Generalization(general=Guidance, specific=spem_uma_ToolMentor)
gen_spem_uma_Whitepaper_Concept = Generalization(general=Concept, specific=spem_uma_Whitepaper)
gen_spem_uma_Guideline_Guidance = Generalization(general=Guidance, specific=spem_uma_Guideline)
gen_spem_uma_SupportingMaterial_Guidance = Generalization(general=Guidance, specific=spem_uma_SupportingMaterial)
gen_spem_uma_RoleDefinitionPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_RoleDefinitionPackage)
gen_spem_uma_TaskDefinitionPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_TaskDefinitionPackage)
gen_spem_uma_WorkProductDefinitionPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_WorkProductDefinitionPackage)
gen_spem_uma_GuidancePackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_GuidancePackage)
gen_spem_uma_DisciplinePackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_DisciplinePackage)
gen_spem_uma_DomainPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_DomainPackage)
gen_spem_uma_WorkProductKindPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_WorkProductKindPackage)
gen_spem_uma_RoleSetPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_RoleSetPackage)
gen_spem_uma_ToolDefinitionPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_ToolDefinitionPackage)
gen_spem_uma_Example_Guidance = Generalization(general=Guidance, specific=spem_uma_Example)
gen_spem_uma_Iteration_Activity = Generalization(general=Activity, specific=spem_uma_Iteration)
gen_spem_uma_Outcome_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Outcome)
gen_spem_uma_Phase_Activity = Generalization(general=Activity, specific=spem_uma_Phase)
gen_spem_uma_Practice_Guidance = Generalization(general=Guidance, specific=spem_uma_Practice)
gen_spem_uma_WorkProductKind_Kind = Generalization(general=Kind, specific=spem_uma_WorkProductKind)
gen_spem_uma_WorkProductKind_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_uma_WorkProductKind)
gen_spem_uma_ConfigurationPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_ConfigurationPackage)
gen_spem_uma_CapabilityPatternPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_CapabilityPatternPackage)
gen_spem_uma_DeliveryProcessPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_DeliveryProcessPackage)
gen_spem_uma_RoleSet_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_uma_RoleSet)
gen_spem_uma_QualificationPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_QualificationPackage)
gen_spem_uma_ProcessComponentPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_ProcessComponentPackage)

# Domain Model
domain_model = DomainModel(
    name="spem",
    types={spem_ExtensibleElement, spem_Kind, ExtensibleElement, spem_WorkDefinitionPerformer, spem_WorkDefinition, spem_WorkDefinitionParameter, spem_WorkSequence, spem_Activity, WorkDefinition, WorkBreakdownElement, VariabilityElement, spem_BreakdownElement, ProcessElement, spem_PlanningData, spem_WorkBreakdownElement, BreakdownElement, spem_RoleUse, spem_TaskUse, MethodContentUse, spem_RoleDefinition, spem_Qualification, spem_ProcessResponsibilityAssignment, spem_WorkProductUse, spem_WorkProductDefinition, spem_WorkProductUseRelationship, spem_ProcessParameter, spem_MethodConfiguration, spem_ProcessPerformer, WorkDefinitionPerformer, spem_Guidance, spem_Metric, spem_Category, MethodContentElement, spem_MethodContentElement, MethodContentPackageableElement, spem_MethodContentKind, WorkDefinitionParameter, spem_Milestone, spem_ProcessElement, DescribableElement, ProcessPackageableElement, spem_ProcessKind, spem_DescribableElement, spem_WorkProductDefinitionRelationship, spem_Default_TaskDefinitionPerformer, spem_Default_ResponsibilityAssignment, spem_ToolDefinition, spem_TaskDefinition, spem_Default_TaskDefinitionParameter, spem_Step, spem_MethodContentPackage, MethodPluginPackageableElement, spem_ProcessPackage, Kind, spem_MethodContentUse, spem_MethodContentPackageableElement, spem_ProcessPackageableElement, spem_VariabilityElement, spem_ProcessComponent, ProcessPackage, spem_WorkProductPort, spem_ProcessComponentUse, spem_MethodLibraryPackageableElement, spem_MethodPluginPackageableElement, MethodLibraryPackageableElement, spem_MethodPlugin, spem_CompositeRole, RoleUse, spem_TeamProfile, spem_MethodLibrary, spem_WorkProductPortConnector, spem_uma_Process, Activity, CapabilityPattern, uma_spem_WorkProductPortConnector, spem_uma_DeliveryProcess, SupportingMaterial, spem_uma_Artifact, WorkProductUse, Artifact, spem_uma_CapabilityPattern, Process, spem_uma_Checklist, Guidance, spem_uma_Concept, spem_uma_CategoryPackage, MethodContentPackage, spem_uma_CustomCategory, Category, spem_uma_Deliverable, uma_spem_WorkProductUse, spem_uma_Discipline, uma_spem_TaskDefinition, spem_uma_DisciplineGrouping, spem_uma_Root, uma_spem_MethodConfiguration, uma_spem_MethodLibrary, uma_spem_MethodPlugin, spem_uma_Domain, uma_spem_WorkProductDefinition, spem_uma_EstimatingConsideration, spem_uma_ProcessPlanningTemplate, spem_uma_Report, spem_uma_ReusableAsset, spem_uma_Roadmap, spem_uma_Template, spem_uma_TermDefinition, spem_uma_ToolMentor, spem_uma_Whitepaper, Concept, spem_uma_Guideline, spem_uma_SupportingMaterial, spem_uma_RoleDefinitionPackage, spem_uma_TaskDefinitionPackage, spem_uma_WorkProductDefinitionPackage, spem_uma_GuidancePackage, spem_uma_DisciplinePackage, spem_uma_DomainPackage, spem_uma_WorkProductKindPackage, spem_uma_RoleSetPackage, spem_uma_ToolDefinitionPackage, spem_uma_Example, spem_uma_Iteration, spem_uma_Outcome, spem_uma_Phase, spem_uma_Practice, Practice, uma_spem_Activity, uma_spem_MethodContentElement, spem_uma_WorkProductKind, spem_uma_ConfigurationPackage, spem_uma_CapabilityPatternPackage, spem_uma_DeliveryProcessPackage, spem_uma_RoleSet, uma_spem_RoleDefinition, spem_uma_QualificationPackage, spem_uma_ProcessComponentPackage, WorkSequenceKind, ParameterDirectionKind, ActivityUseKind, OptionalityKind, VariabilityType, WorkProductRelationshipKind, RiskLevel, EstimatingTechnique, ContractKind, ExpertiseLevel},
    associations={kind0, linkedWorkDefinition1, ownedParameter2, linkToPredecessor5, linkToSuccessor6, predecessor8, successor9, usedActivity12, nestedBreakdownElement13, planningData4, linkedRoleUse26, linkedActivity27, linkedTaskUse30, role32, appliedQualification34, linkedRoleUse36, linkedWorkProductUse38, workProduct40, source42, target44, suppressedBreakdownElement16, ownedProcessParameter19, defaultContext21, validContext23, guidance53, metric54, category56, subCategory58, categorizedElement59, parameterType47, requiredResult50, processKind52, predecessor73, successor76, providedQualification79, source82, target84, linkedTaskDefinition87, linkedRoleDefinition89, linkedRoleDefinition92, methodContentKind60, managedWorkProduct61, ownedTaskDefinitionParameter63, usedTool64, step67, requiredQualification69, ownedMethodContentMember100, reusedPackage102, ownedProcessMember104, task105, usedQualification108, selectedStep111, linkedWorkProductDefinition94, parameterType97, teamRole124, variabilityBasedOnElement127, process128, ownedPort130, processComponent132, usedPort134, baseConfiguration138, methodPluginSelection140, ownedProcessParameter114, aggregatedRole117, subTeam120, superTeam122, ownedProcessPackage160, basePlugin164, ownedMethodPlugin166, predefinedConfiguration168, configurationPackage171, portType174, connectedPort177, processPackageSelection142, contentPackageSelection145, substractedCategory148, defaultView151, processView154, ownedMethodContentPackage157, deliveredProduct180, includedPattern181, includedConnector182, communicationMaterial184, educationalMaterial185, containedArtifact179, relatedTask188, relatedWorflow189, methodConfiguration191, methodLibrary192, MethodPlugin194, relatedProduct196, baseProcess202, subPractice197, referencedActivity198, contentReference200, ownedConfiguration204, role206},
    generalizations={gen_spem_Kind_ExtensibleElement, gen_spem_WorkSequence_BreakdownElement, gen_spem_Activity_WorkDefinition, gen_spem_Activity_WorkBreakdownElement, gen_spem_Activity_VariabilityElement, gen_spem_BreakdownElement_ProcessElement, gen_spem_WorkBreakdownElement_BreakdownElement, gen_spem_RoleUse_MethodContentUse, gen_spem_ProcessResponsibilityAssignment_BreakdownElement, gen_spem_WorkProductUse_MethodContentUse, gen_spem_WorkProductUseRelationship_BreakdownElement, gen_spem_ProcessPerformer_WorkDefinitionPerformer, gen_spem_ProcessPerformer_BreakdownElement, gen_spem_Category_MethodContentElement, gen_spem_Guidance_MethodContentElement, gen_spem_Metric_DescribableElement, gen_spem_MethodContentElement_DescribableElement, gen_spem_MethodContentElement_MethodContentPackageableElement, gen_spem_MethodContentElement_VariabilityElement, gen_spem_ProcessParameter_WorkDefinitionParameter, gen_spem_ProcessParameter_BreakdownElement, gen_spem_Milestone_WorkBreakdownElement, gen_spem_ProcessElement_DescribableElement, gen_spem_ProcessElement_ProcessPackageableElement, gen_spem_DescribableElement_ExtensibleElement, gen_spem_Step_WorkDefinition, gen_spem_Step_DescribableElement, gen_spem_Step_VariabilityElement, gen_spem_WorkProductDefinition_MethodContentElement, gen_spem_RoleDefinition_MethodContentElement, gen_spem_WorkProductDefinitionRelationship_MethodContentElement, gen_spem_Default_TaskDefinitionPerformer_MethodContentElement, gen_spem_Default_ResponsibilityAssignment_MethodContentElement, gen_spem_ToolDefinition_MethodContentElement, gen_spem_TaskDefinition_WorkDefinition, gen_spem_TaskDefinition_MethodContentElement, gen_spem_MethodContentPackage_MethodContentPackageableElement, gen_spem_MethodContentPackage_MethodPluginPackageableElement, gen_spem_ProcessPackage_ProcessPackageableElement, gen_spem_ProcessPackage_MethodPluginPackageableElement, gen_spem_MethodContentKind_MethodContentElement, gen_spem_MethodContentKind_Kind, gen_spem_ProcessKind_ProcessElement, gen_spem_ProcessKind_Kind, gen_spem_PlanningData_ProcessElement, gen_spem_MethodContentUse_BreakdownElement, gen_spem_TaskUse_MethodContentUse, gen_spem_TaskUse_WorkBreakdownElement, gen_spem_Default_TaskDefinitionParameter_WorkDefinitionParameter, gen_spem_Qualification_MethodContentElement, gen_spem_ProcessComponent_ProcessPackage, gen_spem_ProcessComponentUse_MethodContentUse, gen_spem_MethodConfiguration_MethodLibraryPackageableElement, gen_spem_CompositeRole_RoleUse, gen_spem_TeamProfile_BreakdownElement, gen_spem_WorkProductPort_ProcessElement, gen_spem_WorkProductPortConnector_ProcessElement, gen_spem_MethodPlugin_MethodLibraryPackageableElement, gen_spem_uma_Process_Activity, gen_spem_uma_DeliveryProcess_Process, gen_spem_uma_Artifact_WorkProductUse, gen_spem_uma_CapabilityPattern_Process, gen_spem_uma_Checklist_Guidance, gen_spem_uma_Concept_Guidance, gen_spem_uma_CategoryPackage_MethodContentPackage, gen_spem_uma_CustomCategory_Category, gen_spem_uma_Deliverable_WorkProductUse, gen_spem_uma_Discipline_Category, gen_spem_uma_DisciplineGrouping_Category, gen_spem_uma_Domain_Category, gen_spem_uma_EstimatingConsideration_Guidance, gen_spem_uma_ProcessPlanningTemplate_Process, gen_spem_uma_Report_Guidance, gen_spem_uma_ReusableAsset_Guidance, gen_spem_uma_Roadmap_Guidance, gen_spem_uma_Template_Guidance, gen_spem_uma_TermDefinition_Guidance, gen_spem_uma_ToolMentor_Guidance, gen_spem_uma_Whitepaper_Concept, gen_spem_uma_Guideline_Guidance, gen_spem_uma_SupportingMaterial_Guidance, gen_spem_uma_RoleDefinitionPackage_MethodContentPackage, gen_spem_uma_TaskDefinitionPackage_MethodContentPackage, gen_spem_uma_WorkProductDefinitionPackage_MethodContentPackage, gen_spem_uma_GuidancePackage_MethodContentPackage, gen_spem_uma_DisciplinePackage_MethodContentPackage, gen_spem_uma_DomainPackage_MethodContentPackage, gen_spem_uma_WorkProductKindPackage_MethodContentPackage, gen_spem_uma_RoleSetPackage_MethodContentPackage, gen_spem_uma_ToolDefinitionPackage_MethodContentPackage, gen_spem_uma_Example_Guidance, gen_spem_uma_Iteration_Activity, gen_spem_uma_Outcome_WorkProductUse, gen_spem_uma_Phase_Activity, gen_spem_uma_Practice_Guidance, gen_spem_uma_WorkProductKind_Kind, gen_spem_uma_WorkProductKind_MethodContentElement, gen_spem_uma_ConfigurationPackage_MethodContentPackage, gen_spem_uma_CapabilityPatternPackage_ProcessPackage, gen_spem_uma_DeliveryProcessPackage_ProcessPackage, gen_spem_uma_RoleSet_MethodContentElement, gen_spem_uma_QualificationPackage_MethodContentPackage, gen_spem_uma_ProcessComponentPackage_ProcessPackage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)