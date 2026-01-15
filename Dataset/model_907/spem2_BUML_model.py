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
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

WorkSequenceKind: Enumeration = Enumeration(
    name="WorkSequenceKind",
    literals={
            EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish")
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

ExpertiseLevel: Enumeration = Enumeration(
    name="ExpertiseLevel",
    literals={
            EnumerationLiteral(name="LOW"),
			EnumerationLiteral(name="MID"),
			EnumerationLiteral(name="LEVEL")
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

# Classes
spem_BreakdownElement = Class(name="spem::BreakdownElement", is_abstract=True)
ProcessElement = Class(name="ProcessElement")
spem_PlanningData = Class(name="spem::PlanningData")
spem_Guidance = Class(name="spem::Guidance")
spem_WorkBreakdownElement = Class(name="spem::WorkBreakdownElement", is_abstract=True)
BreakdownElement = Class(name="BreakdownElement")
spem_ExtensibleElement = Class(name="spem::ExtensibleElement", is_abstract=True)
spem_Kind = Class(name="spem::Kind", is_abstract=True)
ExtensibleElement = Class(name="ExtensibleElement")
spem_WorkDefinitionPerformer = Class(name="spem::WorkDefinitionPerformer", is_abstract=True)
spem_WorkDefinition = Class(name="spem::WorkDefinition", is_abstract=True)
spem_WorkDefinitionParameter = Class(name="spem::WorkDefinitionParameter")
spem_WorkProductDefinition = Class(name="spem::WorkProductDefinition")
spem_ProcessParameter = Class(name="spem::ProcessParameter")
spem_MethodConfiguration = Class(name="spem::MethodConfiguration")
spem_WorkSequence = Class(name="spem::WorkSequence")
spem_Activity = Class(name="spem::Activity")
WorkDefinition = Class(name="WorkDefinition")
WorkBreakdownElement = Class(name="WorkBreakdownElement")
VariabilityElement = Class(name="VariabilityElement")
spem_LifeCycleSpecification = Class(name="spem::LifeCycleSpecification", is_abstract=True)
spem_WorkProductUseRelationship = Class(name="spem::WorkProductUseRelationship")
WorkDefinitionParameter = Class(name="WorkDefinitionParameter")
spem_Milestone = Class(name="spem::Milestone")
spem_ProcessElement = Class(name="spem::ProcessElement", is_abstract=True)
DescribableElement = Class(name="DescribableElement")
spem_ProcessPerformer = Class(name="spem::ProcessPerformer")
WorkDefinitionPerformer = Class(name="WorkDefinitionPerformer")
spem_RoleUse = Class(name="spem::RoleUse")
spem_TaskUse = Class(name="spem::TaskUse")
MethodContentUse = Class(name="MethodContentUse")
spem_RoleDefinition = Class(name="spem::RoleDefinition")
spem_ProcessResponsibilityAssignment = Class(name="spem::ProcessResponsibilityAssignment")
spem_WorkProductUse = Class(name="spem::WorkProductUse")
MethodContentElement = Class(name="MethodContentElement")
Guidance = Class(name="Guidance")
spem_MethodContentElement = Class(name="spem::MethodContentElement", is_abstract=True)
MethodContentPackageableElement = Class(name="MethodContentPackageableElement")
spem_MethodContentKind = Class(name="spem::MethodContentKind", is_abstract=True)
ProcessPackageableElement = Class(name="ProcessPackageableElement")
spem_ProcessKind = Class(name="spem::ProcessKind", is_abstract=True)
spem_DescribableElement = Class(name="spem::DescribableElement", is_abstract=True)
spem_Metric = Class(name="spem::Metric")
EstimatingConsideration = Class(name="EstimatingConsideration")
spem_Category = Class(name="spem::Category")
Report = Class(name="Report")
Template = Class(name="Template")
spem_ToolDefinition = Class(name="spem::ToolDefinition")
ToolMentor = Class(name="ToolMentor")
spem_TaskDefinition = Class(name="spem::TaskDefinition")
spem_Step = Class(name="spem::Step")
spem_Qualification = Class(name="spem::Qualification")
spem_MethodContentPackageableElement = Class(name="spem::MethodContentPackageableElement", is_abstract=True)
spem_ProcessPackageableElement = Class(name="spem::ProcessPackageableElement", is_abstract=True)
spem_MethodContentPackage = Class(name="spem::MethodContentPackage")
MethodPluginPackageableElement = Class(name="MethodPluginPackageableElement")
spem_ProcessPackage = Class(name="spem::ProcessPackage")
spem_WorkProductDefinitionRelationship = Class(name="spem::WorkProductDefinitionRelationship")
spem_Default_TaskDefinitionPerformer = Class(name="spem::Default::TaskDefinitionPerformer")
spem_Default_ResponsibilityAssignment = Class(name="spem::Default::ResponsibilityAssignment")
spem_Default_TaskDefinitionParameter = Class(name="spem::Default::TaskDefinitionParameter")
RoleUse = Class(name="RoleUse")
spem_TeamProfile = Class(name="spem::TeamProfile")
spem_VariabilityElement = Class(name="spem::VariabilityElement", is_abstract=True)
spem_ProcessComponent = Class(name="spem::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
Kind = Class(name="Kind")
spem_MethodContentUse = Class(name="spem::MethodContentUse", is_abstract=True)
spem_CompositeRole = Class(name="spem::CompositeRole")
spem_MethodLibraryPackageableElement = Class(name="spem::MethodLibraryPackageableElement", is_abstract=True)
spem_MethodPluginPackageableElement = Class(name="spem::MethodPluginPackageableElement", is_abstract=True)
MethodLibraryPackageableElement = Class(name="MethodLibraryPackageableElement")
spem_MethodPlugin = Class(name="spem::MethodPlugin")
spem_WorkProductPort = Class(name="spem::WorkProductPort")
spem_ProcessComponentUse = Class(name="spem::ProcessComponentUse")
ConfigurationPackage = Class(name="ConfigurationPackage")
spem_EObject = Class(name="spem::EObject")
spem_WorkProductPortConnector = Class(name="spem::WorkProductPortConnector")
spem_MethodLibrary = Class(name="spem::MethodLibrary")
spem_uma_Process = Class(name="spem::uma::Process")
Activity = Class(name="Activity")
CapabilityPattern = Class(name="CapabilityPattern")
uma_spem_WorkProductPortConnector = Class(name="uma::spem::WorkProductPortConnector")
spem_uma_DeliveryProcess = Class(name="spem::uma::DeliveryProcess")
spem_WorkProductKind = Class(name="spem::WorkProductKind")
MethodContentKind = Class(name="MethodContentKind")
spem_uma_Artifact = Class(name="spem::uma::Artifact")
WorkProductUse = Class(name="WorkProductUse")
Artifact = Class(name="Artifact")
spem_uma_CapabilityPattern = Class(name="spem::uma::CapabilityPattern")
Process = Class(name="Process")
spem_uma_Checklist = Class(name="spem::uma::Checklist")
spem_uma_Concept = Class(name="spem::uma::Concept")
spem_uma_CategoryPackage = Class(name="spem::uma::CategoryPackage")
MethodContentPackage = Class(name="MethodContentPackage")
spem_uma_CustomCategory = Class(name="spem::uma::CustomCategory")
Category = Class(name="Category")
spem_uma_Deliverable = Class(name="spem::uma::Deliverable")
uma_spem_WorkProductUse = Class(name="uma::spem::WorkProductUse")
spem_uma_DisciplineGrouping = Class(name="spem::uma::DisciplineGrouping")
spem_uma_Root = Class(name="spem::uma::Root")
uma_spem_MethodConfiguration = Class(name="uma::spem::MethodConfiguration")
uma_spem_MethodLibrary = Class(name="uma::spem::MethodLibrary")
uma_spem_MethodPlugin = Class(name="uma::spem::MethodPlugin")
spem_uma_Domain = Class(name="spem::uma::Domain")
uma_spem_WorkProductDefinition = Class(name="uma::spem::WorkProductDefinition")
spem_uma_EstimatingConsideration = Class(name="spem::uma::EstimatingConsideration")
spem_uma_Example = Class(name="spem::uma::Example")
spem_uma_Iteration = Class(name="spem::uma::Iteration")
spem_uma_Outcome = Class(name="spem::uma::Outcome")
spem_uma_Phase = Class(name="spem::uma::Phase")
SupportingMaterial = Class(name="SupportingMaterial")
spem_uma_Discipline = Class(name="spem::uma::Discipline")
uma_spem_TaskDefinition = Class(name="uma::spem::TaskDefinition")
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
spem_uma_Practice = Class(name="spem::uma::Practice")
Practice = Class(name="Practice")
uma_spem_Activity = Class(name="uma::spem::Activity")
uma_spem_MethodContentElement = Class(name="uma::spem::MethodContentElement")
spem_uma_ProcessPlanningTemplate = Class(name="spem::uma::ProcessPlanningTemplate")
spem_uma_Report = Class(name="spem::uma::Report")
spem_uma_ReusableAsset = Class(name="spem::uma::ReusableAsset")
spem_uma_Roadmap = Class(name="spem::uma::Roadmap")
spem_uma_ToolDefinitionPackage = Class(name="spem::uma::ToolDefinitionPackage")
spem_uma_ConfigurationPackage = Class(name="spem::uma::ConfigurationPackage")
spem_uma_CapabilityPatternPackage = Class(name="spem::uma::CapabilityPatternPackage")
spem_uma_DeliveryProcessPackage = Class(name="spem::uma::DeliveryProcessPackage")
spem_uma_RoleSet = Class(name="spem::uma::RoleSet")
uma_spem_RoleDefinition = Class(name="uma::spem::RoleDefinition")
spem_uma_QualificationPackage = Class(name="spem::uma::QualificationPackage")
spem_uma_ProcessComponentPackage = Class(name="spem::uma::ProcessComponentPackage")

# spem_BreakdownElement class attributes and methods
spem_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=BooleanType)
spem_BreakdownElement_isOptional: Property = Property(name="isOptional", type=BooleanType)
spem_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=BooleanType)
spem_BreakdownElement.attributes={spem_BreakdownElement_isPlanned, spem_BreakdownElement_hasMultipleOccurrences, spem_BreakdownElement_isOptional}

# ProcessElement class attributes and methods

# spem_PlanningData class attributes and methods
spem_PlanningData_startDate: Property = Property(name="startDate", type=DateType)
spem_PlanningData_finishDate: Property = Property(name="finishDate", type=DateType)
spem_PlanningData_rank: Property = Property(name="rank", type=IntegerType)
spem_PlanningData_duration: Property = Property(name="duration", type=StringType)
spem_PlanningData.attributes={spem_PlanningData_finishDate, spem_PlanningData_duration, spem_PlanningData_rank, spem_PlanningData_startDate}

# spem_Guidance class attributes and methods
spem_Guidance_attachment: Property = Property(name="attachment", type=StringType)
spem_Guidance.attributes={spem_Guidance_attachment}

# spem_WorkBreakdownElement class attributes and methods
spem_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=BooleanType)
spem_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=BooleanType)
spem_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=BooleanType)
spem_WorkBreakdownElement.attributes={spem_WorkBreakdownElement_isEventDriven, spem_WorkBreakdownElement_isRepeatable, spem_WorkBreakdownElement_isOngoing}

# BreakdownElement class attributes and methods

# spem_ExtensibleElement class attributes and methods

# spem_Kind class attributes and methods

# ExtensibleElement class attributes and methods

# spem_WorkDefinitionPerformer class attributes and methods

# spem_WorkDefinition class attributes and methods
spem_WorkDefinition_preCondition: Property = Property(name="preCondition", type=StringType)
spem_WorkDefinition_postCondition: Property = Property(name="postCondition", type=StringType)
spem_WorkDefinition.attributes={spem_WorkDefinition_postCondition, spem_WorkDefinition_preCondition}

# spem_WorkDefinitionParameter class attributes and methods
spem_WorkDefinitionParameter_name: Property = Property(name="name", type=StringType)
spem_WorkDefinitionParameter_direction: Property = Property(name="direction", type=StringType)
spem_WorkDefinitionParameter_optionality: Property = Property(name="optionality", type=StringType)
spem_WorkDefinitionParameter.attributes={spem_WorkDefinitionParameter_direction, spem_WorkDefinitionParameter_optionality, spem_WorkDefinitionParameter_name}

# spem_WorkProductDefinition class attributes and methods
spem_WorkProductDefinition_impactOfNotHaving: Property = Property(name="impactOfNotHaving", type=StringType)
spem_WorkProductDefinition_reasonForNotNeeding: Property = Property(name="reasonForNotNeeding", type=StringType)
spem_WorkProductDefinition.attributes={spem_WorkProductDefinition_reasonForNotNeeding, spem_WorkProductDefinition_impactOfNotHaving}

# spem_ProcessParameter class attributes and methods

# spem_MethodConfiguration class attributes and methods

# spem_WorkSequence class attributes and methods
spem_WorkSequence_linkKind: Property = Property(name="linkKind", type=StringType)
spem_WorkSequence.attributes={spem_WorkSequence_linkKind}

# spem_Activity class attributes and methods
spem_Activity_useKind: Property = Property(name="useKind", type=StringType)
spem_Activity_howToStaff: Property = Property(name="howToStaff", type=StringType)
spem_Activity_isEnactable: Property = Property(name="isEnactable", type=BooleanType)
spem_Activity.attributes={spem_Activity_useKind, spem_Activity_howToStaff, spem_Activity_isEnactable}

# WorkDefinition class attributes and methods

# WorkBreakdownElement class attributes and methods

# VariabilityElement class attributes and methods

# spem_LifeCycleSpecification class attributes and methods

# spem_WorkProductUseRelationship class attributes and methods

# WorkDefinitionParameter class attributes and methods

# spem_Milestone class attributes and methods

# spem_ProcessElement class attributes and methods

# DescribableElement class attributes and methods

# spem_ProcessPerformer class attributes and methods

# WorkDefinitionPerformer class attributes and methods

# spem_RoleUse class attributes and methods

# spem_TaskUse class attributes and methods
spem_TaskUse_preCondition: Property = Property(name="preCondition", type=StringType)
spem_TaskUse_postCondition: Property = Property(name="postCondition", type=StringType)
spem_TaskUse.attributes={spem_TaskUse_postCondition, spem_TaskUse_preCondition}

# MethodContentUse class attributes and methods

# spem_RoleDefinition class attributes and methods
spem_RoleDefinition_synonym: Property = Property(name="synonym", type=StringType)
spem_RoleDefinition.attributes={spem_RoleDefinition_synonym}

# spem_ProcessResponsibilityAssignment class attributes and methods

# spem_WorkProductUse class attributes and methods

# MethodContentElement class attributes and methods

# Guidance class attributes and methods

# spem_MethodContentElement class attributes and methods
spem_MethodContentElement_copyright: Property = Property(name="copyright", type=StringType)
spem_MethodContentElement_author: Property = Property(name="author", type=StringType)
spem_MethodContentElement_changeDate: Property = Property(name="changeDate", type=DateType)
spem_MethodContentElement_changeDescription: Property = Property(name="changeDescription", type=StringType)
spem_MethodContentElement_version: Property = Property(name="version", type=StringType)
spem_MethodContentElement.attributes={spem_MethodContentElement_copyright, spem_MethodContentElement_author, spem_MethodContentElement_version, spem_MethodContentElement_changeDate, spem_MethodContentElement_changeDescription}

# MethodContentPackageableElement class attributes and methods

# spem_MethodContentKind class attributes and methods

# ProcessPackageableElement class attributes and methods

# spem_ProcessKind class attributes and methods

# spem_DescribableElement class attributes and methods
spem_DescribableElement_presentationName: Property = Property(name="presentationName", type=StringType)
spem_DescribableElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
spem_DescribableElement_purpose: Property = Property(name="purpose", type=StringType)
spem_DescribableElement_mainDescription: Property = Property(name="mainDescription", type=StringType)
spem_DescribableElement.attributes={spem_DescribableElement_briefDescription, spem_DescribableElement_presentationName, spem_DescribableElement_mainDescription, spem_DescribableElement_purpose}

# spem_Metric class attributes and methods
spem_Metric_expression: Property = Property(name="expression", type=StringType)
spem_Metric.attributes={spem_Metric_expression}

# EstimatingConsideration class attributes and methods

# spem_Category class attributes and methods

# Report class attributes and methods

# Template class attributes and methods

# spem_ToolDefinition class attributes and methods

# ToolMentor class attributes and methods

# spem_TaskDefinition class attributes and methods

# spem_Step class attributes and methods
spem_Step_name: Property = Property(name="name", type=StringType)
spem_Step.attributes={spem_Step_name}

# spem_Qualification class attributes and methods

# spem_MethodContentPackageableElement class attributes and methods
spem_MethodContentPackageableElement_name: Property = Property(name="name", type=StringType)
spem_MethodContentPackageableElement.attributes={spem_MethodContentPackageableElement_name}

# spem_ProcessPackageableElement class attributes and methods
spem_ProcessPackageableElement_name: Property = Property(name="name", type=StringType)
spem_ProcessPackageableElement.attributes={spem_ProcessPackageableElement_name}

# spem_MethodContentPackage class attributes and methods

# MethodPluginPackageableElement class attributes and methods

# spem_ProcessPackage class attributes and methods

# spem_WorkProductDefinitionRelationship class attributes and methods

# spem_Default_TaskDefinitionPerformer class attributes and methods

# spem_Default_ResponsibilityAssignment class attributes and methods

# spem_Default_TaskDefinitionParameter class attributes and methods

# RoleUse class attributes and methods

# spem_TeamProfile class attributes and methods

# spem_VariabilityElement class attributes and methods
spem_VariabilityElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
spem_VariabilityElement.attributes={spem_VariabilityElement_variabilityType}

# spem_ProcessComponent class attributes and methods
spem_ProcessComponent_copyright: Property = Property(name="copyright", type=StringType)
spem_ProcessComponent_author: Property = Property(name="author", type=StringType)
spem_ProcessComponent_version: Property = Property(name="version", type=StringType)
spem_ProcessComponent_changeDate: Property = Property(name="changeDate", type=DateType)
spem_ProcessComponent_changeDescription: Property = Property(name="changeDescription", type=StringType)
spem_ProcessComponent.attributes={spem_ProcessComponent_author, spem_ProcessComponent_changeDate, spem_ProcessComponent_changeDescription, spem_ProcessComponent_version, spem_ProcessComponent_copyright}

# ProcessPackage class attributes and methods

# Kind class attributes and methods

# spem_MethodContentUse class attributes and methods
spem_MethodContentUse_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=BooleanType)
spem_MethodContentUse.attributes={spem_MethodContentUse_isSynchronizedWithSource}

# spem_CompositeRole class attributes and methods

# spem_MethodLibraryPackageableElement class attributes and methods
spem_MethodLibraryPackageableElement_name: Property = Property(name="name", type=StringType)
spem_MethodLibraryPackageableElement.attributes={spem_MethodLibraryPackageableElement_name}

# spem_MethodPluginPackageableElement class attributes and methods

# MethodLibraryPackageableElement class attributes and methods

# spem_MethodPlugin class attributes and methods
spem_MethodPlugin_userChangeable: Property = Property(name="userChangeable", type=BooleanType)
spem_MethodPlugin_supporting: Property = Property(name="supporting", type=StringType)
spem_MethodPlugin.attributes={spem_MethodPlugin_userChangeable, spem_MethodPlugin_supporting}

# spem_WorkProductPort class attributes and methods
spem_WorkProductPort_isOptional: Property = Property(name="isOptional", type=BooleanType)
spem_WorkProductPort_portKind: Property = Property(name="portKind", type=StringType)
spem_WorkProductPort.attributes={spem_WorkProductPort_portKind, spem_WorkProductPort_isOptional}

# spem_ProcessComponentUse class attributes and methods

# ConfigurationPackage class attributes and methods

# spem_EObject class attributes and methods

# spem_WorkProductPortConnector class attributes and methods

# spem_MethodLibrary class attributes and methods
spem_MethodLibrary_name: Property = Property(name="name", type=StringType)
spem_MethodLibrary.attributes={spem_MethodLibrary_name}

# spem_uma_Process class attributes and methods
spem_uma_Process_scope: Property = Property(name="scope", type=StringType)
spem_uma_Process_usageNote: Property = Property(name="usageNote", type=StringType)
spem_uma_Process.attributes={spem_uma_Process_usageNote, spem_uma_Process_scope}

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
spem_uma_DeliveryProcess.attributes={spem_uma_DeliveryProcess_typeOfContract, spem_uma_DeliveryProcess_projectCharacteristics, spem_uma_DeliveryProcess_estimatingTechnique, spem_uma_DeliveryProcess_riskLevel, spem_uma_DeliveryProcess_scale, spem_uma_DeliveryProcess_projectMemberExpertise}

# spem_WorkProductKind class attributes and methods

# MethodContentKind class attributes and methods

# spem_uma_Artifact class attributes and methods

# WorkProductUse class attributes and methods

# Artifact class attributes and methods

# spem_uma_CapabilityPattern class attributes and methods

# Process class attributes and methods

# spem_uma_Checklist class attributes and methods

# spem_uma_Concept class attributes and methods

# spem_uma_CategoryPackage class attributes and methods

# MethodContentPackage class attributes and methods

# spem_uma_CustomCategory class attributes and methods

# Category class attributes and methods

# spem_uma_Deliverable class attributes and methods
spem_uma_Deliverable_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
spem_uma_Deliverable_externalDescription: Property = Property(name="externalDescription", type=StringType)
spem_uma_Deliverable.attributes={spem_uma_Deliverable_externalDescription, spem_uma_Deliverable_packagingGuidance}

# uma_spem_WorkProductUse class attributes and methods

# spem_uma_DisciplineGrouping class attributes and methods

# spem_uma_Root class attributes and methods

# uma_spem_MethodConfiguration class attributes and methods

# uma_spem_MethodLibrary class attributes and methods

# uma_spem_MethodPlugin class attributes and methods

# spem_uma_Domain class attributes and methods

# uma_spem_WorkProductDefinition class attributes and methods

# spem_uma_EstimatingConsideration class attributes and methods

# spem_uma_Example class attributes and methods

# spem_uma_Iteration class attributes and methods

# spem_uma_Outcome class attributes and methods

# spem_uma_Phase class attributes and methods

# SupportingMaterial class attributes and methods

# spem_uma_Discipline class attributes and methods

# uma_spem_TaskDefinition class attributes and methods

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

# spem_uma_Practice class attributes and methods
spem_uma_Practice_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
spem_uma_Practice_application: Property = Property(name="application", type=StringType)
spem_uma_Practice_background: Property = Property(name="background", type=StringType)
spem_uma_Practice_goal: Property = Property(name="goal", type=StringType)
spem_uma_Practice_levelOfAdoption: Property = Property(name="levelOfAdoption", type=StringType)
spem_uma_Practice_problem: Property = Property(name="problem", type=StringType)
spem_uma_Practice.attributes={spem_uma_Practice_goal, spem_uma_Practice_application, spem_uma_Practice_problem, spem_uma_Practice_background, spem_uma_Practice_levelOfAdoption, spem_uma_Practice_additionalInfo}

# Practice class attributes and methods

# uma_spem_Activity class attributes and methods

# uma_spem_MethodContentElement class attributes and methods

# spem_uma_ProcessPlanningTemplate class attributes and methods

# spem_uma_Report class attributes and methods

# spem_uma_ReusableAsset class attributes and methods

# spem_uma_Roadmap class attributes and methods

# spem_uma_ToolDefinitionPackage class attributes and methods

# spem_uma_ConfigurationPackage class attributes and methods

# spem_uma_CapabilityPatternPackage class attributes and methods

# spem_uma_DeliveryProcessPackage class attributes and methods

# spem_uma_RoleSet class attributes and methods

# uma_spem_RoleDefinition class attributes and methods

# spem_uma_QualificationPackage class attributes and methods

# spem_uma_ProcessComponentPackage class attributes and methods

# Relationships
parameterType2: BinaryAssociation = BinaryAssociation(
    name="parameterType2",
    ends={
        Property(name="spem_WorkDefinitionParameter3", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1)),
        Property(name="spem_WorkProductDefinition", type=spem_WorkDefinitionParameter, multiplicity=Multiplicity(1, 1))
    }
)
planningData4: BinaryAssociation = BinaryAssociation(
    name="planningData4",
    ends={
        Property(name="spem_PlanningData", type=spem_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_BreakdownElement", type=spem_PlanningData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageGuidance5: BinaryAssociation = BinaryAssociation(
    name="usageGuidance5",
    ends={
        Property(name="spem_Guidance", type=spem_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_BreakdownElement6", type=spem_Guidance, multiplicity=Multiplicity(0, 1))
    }
)
kind0: BinaryAssociation = BinaryAssociation(
    name="kind0",
    ends={
        Property(name="spem_Kind", type=spem_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ExtensibleElement", type=spem_Kind, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter1: BinaryAssociation = BinaryAssociation(
    name="ownedParameter1",
    ends={
        Property(name="spem_WorkDefinitionParameter", type=spem_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkDefinition", type=spem_WorkDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedActivity14: BinaryAssociation = BinaryAssociation(
    name="usedActivity14",
    ends={
        Property(name="spem_Activity", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity13", type=spem_Activity, multiplicity=Multiplicity(0, 1))
    }
)
nestedBreakdownElement15: BinaryAssociation = BinaryAssociation(
    name="nestedBreakdownElement15",
    ends={
        Property(name="spem_BreakdownElement17", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity16", type=spem_BreakdownElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suppressedBreakdownElement18: BinaryAssociation = BinaryAssociation(
    name="suppressedBreakdownElement18",
    ends={
        Property(name="spem_BreakdownElement20", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity19", type=spem_BreakdownElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedProcessParameter21: BinaryAssociation = BinaryAssociation(
    name="ownedProcessParameter21",
    ends={
        Property(name="spem_ProcessParameter", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity22", type=spem_ProcessParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultContext23: BinaryAssociation = BinaryAssociation(
    name="defaultContext23",
    ends={
        Property(name="spem_MethodConfiguration", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity24", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 1))
    }
)
validContext25: BinaryAssociation = BinaryAssociation(
    name="validContext25",
    ends={
        Property(name="spem_MethodConfiguration27", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity26", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
alternatives29: BinaryAssociation = BinaryAssociation(
    name="alternatives29",
    ends={
        Property(name="spem_Activity30", type=spem_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Activity28", type=spem_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
linkToPredecessor7: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor7",
    ends={
        Property(name="WorkSequence", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linkToSuccessor8: BinaryAssociation = BinaryAssociation(
    name="linkToSuccessor8",
    ends={
        Property(name="WorkSequence9", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=spem_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor10: BinaryAssociation = BinaryAssociation(
    name="predecessor10",
    ends={
        Property(name="WorkBreakdownElement", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToSuccessor", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
successor11: BinaryAssociation = BinaryAssociation(
    name="successor11",
    ends={
        Property(name="WorkBreakdownElement12", type=spem_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linkToPredecessor", type=spem_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
workProduct43: BinaryAssociation = BinaryAssociation(
    name="workProduct43",
    ends={
        Property(name="spem_WorkProductDefinition45", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUse44", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1))
    }
)
lifeCycle46: BinaryAssociation = BinaryAssociation(
    name="lifeCycle46",
    ends={
        Property(name="spem_LifeCycleSpecification", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUse47", type=spem_LifeCycleSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source48: BinaryAssociation = BinaryAssociation(
    name="source48",
    ends={
        Property(name="spem_WorkProductUse49", type=spem_WorkProductUseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUseRelationship", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1))
    }
)
target50: BinaryAssociation = BinaryAssociation(
    name="target50",
    ends={
        Property(name="spem_WorkProductUse52", type=spem_WorkProductUseRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductUseRelationship51", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 9999))
    }
)
requiredResult53: BinaryAssociation = BinaryAssociation(
    name="requiredResult53",
    ends={
        Property(name="spem_WorkProductUse54", type=spem_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Milestone", type=spem_WorkProductUse, multiplicity=Multiplicity(0, 9999))
    }
)
linkedRoleUse31: BinaryAssociation = BinaryAssociation(
    name="linkedRoleUse31",
    ends={
        Property(name="spem_RoleUse", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer", type=spem_RoleUse, multiplicity=Multiplicity(1, 9999))
    }
)
linkedActivity32: BinaryAssociation = BinaryAssociation(
    name="linkedActivity32",
    ends={
        Property(name="spem_Activity34", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer33", type=spem_Activity, multiplicity=Multiplicity(0, 1))
    }
)
linkedTaskUse35: BinaryAssociation = BinaryAssociation(
    name="linkedTaskUse35",
    ends={
        Property(name="spem_TaskUse", type=spem_ProcessPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPerformer36", type=spem_TaskUse, multiplicity=Multiplicity(0, 1))
    }
)
role37: BinaryAssociation = BinaryAssociation(
    name="role37",
    ends={
        Property(name="spem_RoleDefinition", type=spem_RoleUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_RoleUse38", type=spem_RoleDefinition, multiplicity=Multiplicity(0, 1))
    }
)
linkedRoleUse39: BinaryAssociation = BinaryAssociation(
    name="linkedRoleUse39",
    ends={
        Property(name="spem_RoleUse40", type=spem_ProcessResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessResponsibilityAssignment", type=spem_RoleUse, multiplicity=Multiplicity(1, 9999))
    }
)
linkedWorkProductUse41: BinaryAssociation = BinaryAssociation(
    name="linkedWorkProductUse41",
    ends={
        Property(name="spem_WorkProductUse", type=spem_ProcessResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessResponsibilityAssignment42", type=spem_WorkProductUse, multiplicity=Multiplicity(1, 1))
    }
)
subCategory71: BinaryAssociation = BinaryAssociation(
    name="subCategory71",
    ends={
        Property(name="spem_Category72", type=spem_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Category70", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
suppressedMethodContentElement74: BinaryAssociation = BinaryAssociation(
    name="suppressedMethodContentElement74",
    ends={
        Property(name="spem_MethodContentElement", type=spem_MethodContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentElement73", type=spem_MethodContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
methodContentKind75: BinaryAssociation = BinaryAssociation(
    name="methodContentKind75",
    ends={
        Property(name="spem_MethodContentKind", type=spem_MethodContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentElement76", type=spem_MethodContentKind, multiplicity=Multiplicity(0, 1))
    }
)
processKind55: BinaryAssociation = BinaryAssociation(
    name="processKind55",
    ends={
        Property(name="spem_ProcessKind", type=spem_ProcessElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessElement", type=spem_ProcessKind, multiplicity=Multiplicity(0, 1))
    }
)
guidance56: BinaryAssociation = BinaryAssociation(
    name="guidance56",
    ends={
        Property(name="spem_Guidance57", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement", type=spem_Guidance, multiplicity=Multiplicity(0, 9999))
    }
)
metric58: BinaryAssociation = BinaryAssociation(
    name="metric58",
    ends={
        Property(name="spem_Metric", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement59", type=spem_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
presentedAfter61: BinaryAssociation = BinaryAssociation(
    name="presentedAfter61",
    ends={
        Property(name="spem_DescribableElement62", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement60", type=spem_DescribableElement, multiplicity=Multiplicity(0, 1))
    }
)
presentedBefore64: BinaryAssociation = BinaryAssociation(
    name="presentedBefore64",
    ends={
        Property(name="spem_DescribableElement65", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement63", type=spem_DescribableElement, multiplicity=Multiplicity(0, 1))
    }
)
keyConsideration66: BinaryAssociation = BinaryAssociation(
    name="keyConsideration66",
    ends={
        Property(name="EstimatingConsideration", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement67", type=EstimatingConsideration, multiplicity=Multiplicity(0, 9999))
    }
)
category68: BinaryAssociation = BinaryAssociation(
    name="category68",
    ends={
        Property(name="spem_Category", type=spem_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_DescribableElement69", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor91: BinaryAssociation = BinaryAssociation(
    name="predecessor91",
    ends={
        Property(name="spem_Step92", type=spem_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Step90", type=spem_Step, multiplicity=Multiplicity(0, 1))
    }
)
estimatingConsideration93: BinaryAssociation = BinaryAssociation(
    name="estimatingConsideration93",
    ends={
        Property(name="EstimatingConsideration95", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinition94", type=EstimatingConsideration, multiplicity=Multiplicity(0, 9999))
    }
)
report96: BinaryAssociation = BinaryAssociation(
    name="report96",
    ends={
        Property(name="Report", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinition97", type=Report, multiplicity=Multiplicity(0, 9999))
    }
)
template98: BinaryAssociation = BinaryAssociation(
    name="template98",
    ends={
        Property(name="Template", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinition99", type=Template, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentor100: BinaryAssociation = BinaryAssociation(
    name="toolMentor100",
    ends={
        Property(name="ToolMentor102", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinition101", type=ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
managedWorkProduct77: BinaryAssociation = BinaryAssociation(
    name="managedWorkProduct77",
    ends={
        Property(name="spem_WorkProductDefinition78", type=spem_ToolDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ToolDefinition", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentor79: BinaryAssociation = BinaryAssociation(
    name="toolMentor79",
    ends={
        Property(name="ToolMentor", type=spem_ToolDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ToolDefinition80", type=ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
usedTool81: BinaryAssociation = BinaryAssociation(
    name="usedTool81",
    ends={
        Property(name="spem_ToolDefinition82", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition", type=spem_ToolDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
step83: BinaryAssociation = BinaryAssociation(
    name="step83",
    ends={
        Property(name="spem_Step", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition84", type=spem_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternative86: BinaryAssociation = BinaryAssociation(
    name="alternative86",
    ends={
        Property(name="spem_TaskDefinition87", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition85", type=spem_TaskDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
requiredQualification88: BinaryAssociation = BinaryAssociation(
    name="requiredQualification88",
    ends={
        Property(name="spem_Qualification", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskDefinition89", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodContentMember121: BinaryAssociation = BinaryAssociation(
    name="ownedMethodContentMember121",
    ends={
        Property(name="spem_MethodContentPackageableElement", type=spem_MethodContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentPackage", type=spem_MethodContentPackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedPackage123: BinaryAssociation = BinaryAssociation(
    name="reusedPackage123",
    ends={
        Property(name="spem_MethodContentPackage124", type=spem_MethodContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodContentPackage122", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedProcessMember125: BinaryAssociation = BinaryAssociation(
    name="ownedProcessMember125",
    ends={
        Property(name="spem_ProcessPackageableElement", type=spem_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessPackage", type=spem_ProcessPackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredQualification103: BinaryAssociation = BinaryAssociation(
    name="requiredQualification103",
    ends={
        Property(name="spem_Qualification105", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_RoleDefinition104", type=spem_Qualification, multiplicity=Multiplicity(0, 9999))
    }
)
source106: BinaryAssociation = BinaryAssociation(
    name="source106",
    ends={
        Property(name="spem_WorkProductDefinition107", type=spem_WorkProductDefinitionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinitionRelationship", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1))
    }
)
target108: BinaryAssociation = BinaryAssociation(
    name="target108",
    ends={
        Property(name="spem_WorkProductDefinition110", type=spem_WorkProductDefinitionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductDefinitionRelationship109", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
linkedTaskDefinition111: BinaryAssociation = BinaryAssociation(
    name="linkedTaskDefinition111",
    ends={
        Property(name="spem_TaskDefinition112", type=spem_Default_TaskDefinitionPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_TaskDefinitionPerformer", type=spem_TaskDefinition, multiplicity=Multiplicity(1, 1))
    }
)
linkedRoleDefinition113: BinaryAssociation = BinaryAssociation(
    name="linkedRoleDefinition113",
    ends={
        Property(name="spem_RoleDefinition115", type=spem_Default_TaskDefinitionPerformer, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_TaskDefinitionPerformer114", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
linkedRoleDefinition116: BinaryAssociation = BinaryAssociation(
    name="linkedRoleDefinition116",
    ends={
        Property(name="spem_RoleDefinition117", type=spem_Default_ResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_ResponsibilityAssignment", type=spem_RoleDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
linkedWorkProductDefinition118: BinaryAssociation = BinaryAssociation(
    name="linkedWorkProductDefinition118",
    ends={
        Property(name="spem_WorkProductDefinition120", type=spem_Default_ResponsibilityAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_Default_ResponsibilityAssignment119", type=spem_WorkProductDefinition, multiplicity=Multiplicity(1, 1))
    }
)
aggregatedRole135: BinaryAssociation = BinaryAssociation(
    name="aggregatedRole135",
    ends={
        Property(name="spem_RoleDefinition136", type=spem_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_CompositeRole", type=spem_RoleDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
subTeam138: BinaryAssociation = BinaryAssociation(
    name="subTeam138",
    ends={
        Property(name="TeamProfile", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="superTeam", type=spem_TeamProfile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTeam140: BinaryAssociation = BinaryAssociation(
    name="superTeam140",
    ends={
        Property(name="TeamProfile141", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="subTeam", type=spem_TeamProfile, multiplicity=Multiplicity(0, 1))
    }
)
teamRole142: BinaryAssociation = BinaryAssociation(
    name="teamRole142",
    ends={
        Property(name="spem_RoleUse143", type=spem_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TeamProfile", type=spem_RoleUse, multiplicity=Multiplicity(0, 9999))
    }
)
variabilityBasedOnElement145: BinaryAssociation = BinaryAssociation(
    name="variabilityBasedOnElement145",
    ends={
        Property(name="spem_VariabilityElement", type=spem_VariabilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_VariabilityElement144", type=spem_VariabilityElement, multiplicity=Multiplicity(0, 1))
    }
)
task126: BinaryAssociation = BinaryAssociation(
    name="task126",
    ends={
        Property(name="spem_TaskDefinition128", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse127", type=spem_TaskDefinition, multiplicity=Multiplicity(0, 1))
    }
)
ownedProcessParameter129: BinaryAssociation = BinaryAssociation(
    name="ownedProcessParameter129",
    ends={
        Property(name="spem_ProcessParameter131", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse130", type=spem_ProcessParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedStep132: BinaryAssociation = BinaryAssociation(
    name="selectedStep132",
    ends={
        Property(name="spem_Step134", type=spem_TaskUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_TaskUse133", type=spem_Step, multiplicity=Multiplicity(0, 9999))
    }
)
baseConfiguration156: BinaryAssociation = BinaryAssociation(
    name="baseConfiguration156",
    ends={
        Property(name="spem_MethodConfiguration157", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration155", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
methodPluginSelection158: BinaryAssociation = BinaryAssociation(
    name="methodPluginSelection158",
    ends={
        Property(name="spem_MethodPlugin", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration159", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 9999))
    }
)
processPackageSelection160: BinaryAssociation = BinaryAssociation(
    name="processPackageSelection160",
    ends={
        Property(name="spem_ProcessPackage162", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration161", type=spem_ProcessPackage, multiplicity=Multiplicity(0, 9999))
    }
)
contentPackageSelection163: BinaryAssociation = BinaryAssociation(
    name="contentPackageSelection163",
    ends={
        Property(name="spem_MethodContentPackage165", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration164", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999))
    }
)
addedCategory166: BinaryAssociation = BinaryAssociation(
    name="addedCategory166",
    ends={
        Property(name="spem_Category168", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration167", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
substractedCategory169: BinaryAssociation = BinaryAssociation(
    name="substractedCategory169",
    ends={
        Property(name="spem_Category171", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration170", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
process146: BinaryAssociation = BinaryAssociation(
    name="process146",
    ends={
        Property(name="spem_Activity147", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponent", type=spem_Activity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPort148: BinaryAssociation = BinaryAssociation(
    name="ownedPort148",
    ends={
        Property(name="spem_WorkProductPort", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponent149", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processComponent150: BinaryAssociation = BinaryAssociation(
    name="processComponent150",
    ends={
        Property(name="spem_ProcessComponent151", type=spem_ProcessComponentUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponentUse", type=spem_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
usedPort152: BinaryAssociation = BinaryAssociation(
    name="usedPort152",
    ends={
        Property(name="spem_WorkProductPort154", type=spem_ProcessComponentUse, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_ProcessComponentUse153", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tool195: BinaryAssociation = BinaryAssociation(
    name="tool195",
    ends={
        Property(name="spem_ToolDefinition197", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary196", type=spem_ToolDefinition, multiplicity=Multiplicity(0, 1))
    }
)
configurationPackage198: BinaryAssociation = BinaryAssociation(
    name="configurationPackage198",
    ends={
        Property(name="ConfigurationPackage", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary199", type=ConfigurationPackage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
any200: BinaryAssociation = BinaryAssociation(
    name="any200",
    ends={
        Property(name="spem_EObject", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary201", type=spem_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
portType202: BinaryAssociation = BinaryAssociation(
    name="portType202",
    ends={
        Property(name="spem_WorkProductDefinition204", type=spem_WorkProductPort, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductPort203", type=spem_WorkProductDefinition, multiplicity=Multiplicity(0, 1))
    }
)
connectedPort205: BinaryAssociation = BinaryAssociation(
    name="connectedPort205",
    ends={
        Property(name="spem_WorkProductPort206", type=spem_WorkProductPortConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_WorkProductPortConnector", type=spem_WorkProductPort, multiplicity=Multiplicity(0, 9999))
    }
)
defaultView172: BinaryAssociation = BinaryAssociation(
    name="defaultView172",
    ends={
        Property(name="spem_Category174", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration173", type=spem_Category, multiplicity=Multiplicity(1, 1))
    }
)
processView175: BinaryAssociation = BinaryAssociation(
    name="processView175",
    ends={
        Property(name="spem_Category177", type=spem_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodConfiguration176", type=spem_Category, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodContentPackage178: BinaryAssociation = BinaryAssociation(
    name="ownedMethodContentPackage178",
    ends={
        Property(name="spem_MethodContentPackage180", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin179", type=spem_MethodContentPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProcessPackage181: BinaryAssociation = BinaryAssociation(
    name="ownedProcessPackage181",
    ends={
        Property(name="spem_ProcessPackage183", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin182", type=spem_ProcessPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basePlugin185: BinaryAssociation = BinaryAssociation(
    name="basePlugin185",
    ends={
        Property(name="spem_MethodPlugin186", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin184", type=spem_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
referencedMethodPlugin188: BinaryAssociation = BinaryAssociation(
    name="referencedMethodPlugin188",
    ends={
        Property(name="spem_MethodPlugin189", type=spem_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodPlugin187", type=spem_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMethodPlugin190: BinaryAssociation = BinaryAssociation(
    name="ownedMethodPlugin190",
    ends={
        Property(name="spem_MethodPlugin191", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary", type=spem_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predefinedConfiguration192: BinaryAssociation = BinaryAssociation(
    name="predefinedConfiguration192",
    ends={
        Property(name="spem_MethodConfiguration194", type=spem_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_MethodLibrary193", type=spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedPattern209: BinaryAssociation = BinaryAssociation(
    name="includedPattern209",
    ends={
        Property(name="CapabilityPattern", type=spem_uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Process", type=CapabilityPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedConnector210: BinaryAssociation = BinaryAssociation(
    name="includedConnector210",
    ends={
        Property(name="uma_spem_WorkProductPortConnector", type=spem_uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Process211", type=uma_spem_WorkProductPortConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containedArtifact207: BinaryAssociation = BinaryAssociation(
    name="containedArtifact207",
    ends={
        Property(name="Artifact", type=spem_uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Artifact", type=Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deliveredProduct208: BinaryAssociation = BinaryAssociation(
    name="deliveredProduct208",
    ends={
        Property(name="uma_spem_WorkProductUse", type=spem_uma_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Deliverable", type=uma_spem_WorkProductUse, multiplicity=Multiplicity(0, 9999))
    }
)
methodConfiguration219: BinaryAssociation = BinaryAssociation(
    name="methodConfiguration219",
    ends={
        Property(name="uma_spem_MethodConfiguration", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root", type=uma_spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodLibrary220: BinaryAssociation = BinaryAssociation(
    name="methodLibrary220",
    ends={
        Property(name="uma_spem_MethodLibrary", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root221", type=uma_spem_MethodLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MethodPlugin222: BinaryAssociation = BinaryAssociation(
    name="MethodPlugin222",
    ends={
        Property(name="uma_spem_MethodPlugin", type=spem_uma_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Root223", type=uma_spem_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedProduct224: BinaryAssociation = BinaryAssociation(
    name="relatedProduct224",
    ends={
        Property(name="uma_spem_WorkProductDefinition", type=spem_uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Domain", type=uma_spem_WorkProductDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
communicationMaterial212: BinaryAssociation = BinaryAssociation(
    name="communicationMaterial212",
    ends={
        Property(name="SupportingMaterial", type=spem_uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_DeliveryProcess", type=SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
educationalMaterial213: BinaryAssociation = BinaryAssociation(
    name="educationalMaterial213",
    ends={
        Property(name="SupportingMaterial215", type=spem_uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_DeliveryProcess214", type=SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
relatedTask216: BinaryAssociation = BinaryAssociation(
    name="relatedTask216",
    ends={
        Property(name="uma_spem_TaskDefinition", type=spem_uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Discipline", type=uma_spem_TaskDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
relatedWorflow217: BinaryAssociation = BinaryAssociation(
    name="relatedWorflow217",
    ends={
        Property(name="Process", type=spem_uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Discipline218", type=Process, multiplicity=Multiplicity(0, 9999))
    }
)
subPractice225: BinaryAssociation = BinaryAssociation(
    name="subPractice225",
    ends={
        Property(name="Practice", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice", type=Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedActivity226: BinaryAssociation = BinaryAssociation(
    name="referencedActivity226",
    ends={
        Property(name="uma_spem_Activity", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice227", type=uma_spem_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
contentReference228: BinaryAssociation = BinaryAssociation(
    name="contentReference228",
    ends={
        Property(name="uma_spem_MethodContentElement", type=spem_uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_Practice229", type=uma_spem_MethodContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
baseProcess230: BinaryAssociation = BinaryAssociation(
    name="baseProcess230",
    ends={
        Property(name="Process231", type=spem_uma_ProcessPlanningTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_ProcessPlanningTemplate", type=Process, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConfiguration232: BinaryAssociation = BinaryAssociation(
    name="ownedConfiguration232",
    ends={
        Property(name="uma_spem_MethodConfiguration233", type=spem_uma_ConfigurationPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_ConfigurationPackage", type=uma_spem_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
role234: BinaryAssociation = BinaryAssociation(
    name="role234",
    ends={
        Property(name="uma_spem_RoleDefinition", type=spem_uma_RoleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="spem_uma_RoleSet", type=uma_spem_RoleDefinition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_spem_BreakdownElement_ProcessElement = Generalization(general=ProcessElement, specific=spem_BreakdownElement)
gen_spem_WorkBreakdownElement_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkBreakdownElement)
gen_spem_Kind_ExtensibleElement = Generalization(general=ExtensibleElement, specific=spem_Kind)
gen_spem_WorkSequence_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkSequence)
gen_spem_Activity_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_Activity)
gen_spem_Activity_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_Activity)
gen_spem_Activity_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_Activity)
gen_spem_WorkProductUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_WorkProductUse)
gen_spem_WorkProductUseRelationship_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_WorkProductUseRelationship)
gen_spem_ProcessParameter_WorkDefinitionParameter = Generalization(general=WorkDefinitionParameter, specific=spem_ProcessParameter)
gen_spem_Milestone_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_Milestone)
gen_spem_ProcessPerformer_WorkDefinitionPerformer = Generalization(general=WorkDefinitionPerformer, specific=spem_ProcessPerformer)
gen_spem_ProcessPerformer_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_ProcessPerformer)
gen_spem_RoleUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_RoleUse)
gen_spem_ProcessResponsibilityAssignment_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_ProcessResponsibilityAssignment)
gen_spem_Category_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Category)
gen_spem_Guidance_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Guidance)
gen_spem_Metric_Guidance = Generalization(general=Guidance, specific=spem_Metric)
gen_spem_MethodContentElement_DescribableElement = Generalization(general=DescribableElement, specific=spem_MethodContentElement)
gen_spem_MethodContentElement_MethodContentPackageableElement = Generalization(general=MethodContentPackageableElement, specific=spem_MethodContentElement)
gen_spem_MethodContentElement_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_MethodContentElement)
gen_spem_ProcessElement_DescribableElement = Generalization(general=DescribableElement, specific=spem_ProcessElement)
gen_spem_ProcessElement_ProcessPackageableElement = Generalization(general=ProcessPackageableElement, specific=spem_ProcessElement)
gen_spem_DescribableElement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=spem_DescribableElement)
gen_spem_WorkProductDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_WorkProductDefinition)
gen_spem_RoleDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_RoleDefinition)
gen_spem_ToolDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_ToolDefinition)
gen_spem_TaskDefinition_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_TaskDefinition)
gen_spem_TaskDefinition_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_TaskDefinition)
gen_spem_Step_WorkDefinition = Generalization(general=WorkDefinition, specific=spem_Step)
gen_spem_Step_DescribableElement = Generalization(general=DescribableElement, specific=spem_Step)
gen_spem_Step_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_Step)
gen_spem_MethodContentPackageableElement_VariabilityElement = Generalization(general=VariabilityElement, specific=spem_MethodContentPackageableElement)
gen_spem_MethodContentPackage_MethodContentPackageableElement = Generalization(general=MethodContentPackageableElement, specific=spem_MethodContentPackage)
gen_spem_MethodContentPackage_MethodPluginPackageableElement = Generalization(general=MethodPluginPackageableElement, specific=spem_MethodContentPackage)
gen_spem_ProcessPackage_ProcessPackageableElement = Generalization(general=ProcessPackageableElement, specific=spem_ProcessPackage)
gen_spem_ProcessPackage_MethodPluginPackageableElement = Generalization(general=MethodPluginPackageableElement, specific=spem_ProcessPackage)
gen_spem_MethodContentKind_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_MethodContentKind)
gen_spem_WorkProductDefinitionRelationship_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_WorkProductDefinitionRelationship)
gen_spem_Default_TaskDefinitionPerformer_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Default_TaskDefinitionPerformer)
gen_spem_Default_ResponsibilityAssignment_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Default_ResponsibilityAssignment)
gen_spem_Default_TaskDefinitionParameter_WorkDefinitionParameter = Generalization(general=WorkDefinitionParameter, specific=spem_Default_TaskDefinitionParameter)
gen_spem_Qualification_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_Qualification)
gen_spem_CompositeRole_RoleUse = Generalization(general=RoleUse, specific=spem_CompositeRole)
gen_spem_TeamProfile_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_TeamProfile)
gen_spem_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_ProcessComponent)
gen_spem_MethodContentKind_Kind = Generalization(general=Kind, specific=spem_MethodContentKind)
gen_spem_ProcessKind_ProcessElement = Generalization(general=ProcessElement, specific=spem_ProcessKind)
gen_spem_ProcessKind_Kind = Generalization(general=Kind, specific=spem_ProcessKind)
gen_spem_PlanningData_ProcessElement = Generalization(general=ProcessElement, specific=spem_PlanningData)
gen_spem_MethodContentUse_BreakdownElement = Generalization(general=BreakdownElement, specific=spem_MethodContentUse)
gen_spem_TaskUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_TaskUse)
gen_spem_TaskUse_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=spem_TaskUse)
gen_spem_MethodConfiguration_MethodLibraryPackageableElement = Generalization(general=MethodLibraryPackageableElement, specific=spem_MethodConfiguration)
gen_spem_ProcessComponentUse_MethodContentUse = Generalization(general=MethodContentUse, specific=spem_ProcessComponentUse)
gen_spem_WorkProductPort_ProcessElement = Generalization(general=ProcessElement, specific=spem_WorkProductPort)
gen_spem_WorkProductPortConnector_ProcessElement = Generalization(general=ProcessElement, specific=spem_WorkProductPortConnector)
gen_spem_MethodPlugin_MethodLibraryPackageableElement = Generalization(general=MethodLibraryPackageableElement, specific=spem_MethodPlugin)
gen_spem_uma_Process_Activity = Generalization(general=Activity, specific=spem_uma_Process)
gen_spem_uma_DeliveryProcess_Process = Generalization(general=Process, specific=spem_uma_DeliveryProcess)
gen_spem_WorkProductKind_MethodContentKind = Generalization(general=MethodContentKind, specific=spem_WorkProductKind)
gen_spem_uma_Artifact_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Artifact)
gen_spem_uma_CapabilityPattern_Process = Generalization(general=Process, specific=spem_uma_CapabilityPattern)
gen_spem_uma_Checklist_Guidance = Generalization(general=Guidance, specific=spem_uma_Checklist)
gen_spem_uma_Concept_Guidance = Generalization(general=Guidance, specific=spem_uma_Concept)
gen_spem_uma_CategoryPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_CategoryPackage)
gen_spem_uma_CustomCategory_Category = Generalization(general=Category, specific=spem_uma_CustomCategory)
gen_spem_uma_Deliverable_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Deliverable)
gen_spem_uma_DisciplineGrouping_Category = Generalization(general=Category, specific=spem_uma_DisciplineGrouping)
gen_spem_uma_Domain_Category = Generalization(general=Category, specific=spem_uma_Domain)
gen_spem_uma_EstimatingConsideration_Guidance = Generalization(general=Guidance, specific=spem_uma_EstimatingConsideration)
gen_spem_uma_Example_Guidance = Generalization(general=Guidance, specific=spem_uma_Example)
gen_spem_uma_Iteration_Activity = Generalization(general=Activity, specific=spem_uma_Iteration)
gen_spem_uma_Outcome_WorkProductUse = Generalization(general=WorkProductUse, specific=spem_uma_Outcome)
gen_spem_uma_Phase_Activity = Generalization(general=Activity, specific=spem_uma_Phase)
gen_spem_uma_Discipline_Category = Generalization(general=Category, specific=spem_uma_Discipline)
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
gen_spem_uma_Practice_Guidance = Generalization(general=Guidance, specific=spem_uma_Practice)
gen_spem_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=spem_uma_ProcessPlanningTemplate)
gen_spem_uma_Report_Guidance = Generalization(general=Guidance, specific=spem_uma_Report)
gen_spem_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=spem_uma_ReusableAsset)
gen_spem_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=spem_uma_Roadmap)
gen_spem_uma_ToolDefinitionPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_ToolDefinitionPackage)
gen_spem_uma_ConfigurationPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_ConfigurationPackage)
gen_spem_uma_CapabilityPatternPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_CapabilityPatternPackage)
gen_spem_uma_DeliveryProcessPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_DeliveryProcessPackage)
gen_spem_uma_RoleSet_MethodContentElement = Generalization(general=MethodContentElement, specific=spem_uma_RoleSet)
gen_spem_uma_QualificationPackage_MethodContentPackage = Generalization(general=MethodContentPackage, specific=spem_uma_QualificationPackage)
gen_spem_uma_ProcessComponentPackage_ProcessPackage = Generalization(general=ProcessPackage, specific=spem_uma_ProcessComponentPackage)

# Domain Model
domain_model = DomainModel(
    name="spem",
    types={spem_BreakdownElement, ProcessElement, spem_PlanningData, spem_Guidance, spem_WorkBreakdownElement, BreakdownElement, spem_ExtensibleElement, spem_Kind, ExtensibleElement, spem_WorkDefinitionPerformer, spem_WorkDefinition, spem_WorkDefinitionParameter, spem_WorkProductDefinition, spem_ProcessParameter, spem_MethodConfiguration, spem_WorkSequence, spem_Activity, WorkDefinition, WorkBreakdownElement, VariabilityElement, spem_LifeCycleSpecification, spem_WorkProductUseRelationship, WorkDefinitionParameter, spem_Milestone, spem_ProcessElement, DescribableElement, spem_ProcessPerformer, WorkDefinitionPerformer, spem_RoleUse, spem_TaskUse, MethodContentUse, spem_RoleDefinition, spem_ProcessResponsibilityAssignment, spem_WorkProductUse, MethodContentElement, Guidance, spem_MethodContentElement, MethodContentPackageableElement, spem_MethodContentKind, ProcessPackageableElement, spem_ProcessKind, spem_DescribableElement, spem_Metric, EstimatingConsideration, spem_Category, Report, Template, spem_ToolDefinition, ToolMentor, spem_TaskDefinition, spem_Step, spem_Qualification, spem_MethodContentPackageableElement, spem_ProcessPackageableElement, spem_MethodContentPackage, MethodPluginPackageableElement, spem_ProcessPackage, spem_WorkProductDefinitionRelationship, spem_Default_TaskDefinitionPerformer, spem_Default_ResponsibilityAssignment, spem_Default_TaskDefinitionParameter, RoleUse, spem_TeamProfile, spem_VariabilityElement, spem_ProcessComponent, ProcessPackage, Kind, spem_MethodContentUse, spem_CompositeRole, spem_MethodLibraryPackageableElement, spem_MethodPluginPackageableElement, MethodLibraryPackageableElement, spem_MethodPlugin, spem_WorkProductPort, spem_ProcessComponentUse, ConfigurationPackage, spem_EObject, spem_WorkProductPortConnector, spem_MethodLibrary, spem_uma_Process, Activity, CapabilityPattern, uma_spem_WorkProductPortConnector, spem_uma_DeliveryProcess, spem_WorkProductKind, MethodContentKind, spem_uma_Artifact, WorkProductUse, Artifact, spem_uma_CapabilityPattern, Process, spem_uma_Checklist, spem_uma_Concept, spem_uma_CategoryPackage, MethodContentPackage, spem_uma_CustomCategory, Category, spem_uma_Deliverable, uma_spem_WorkProductUse, spem_uma_DisciplineGrouping, spem_uma_Root, uma_spem_MethodConfiguration, uma_spem_MethodLibrary, uma_spem_MethodPlugin, spem_uma_Domain, uma_spem_WorkProductDefinition, spem_uma_EstimatingConsideration, spem_uma_Example, spem_uma_Iteration, spem_uma_Outcome, spem_uma_Phase, SupportingMaterial, spem_uma_Discipline, uma_spem_TaskDefinition, spem_uma_Template, spem_uma_TermDefinition, spem_uma_ToolMentor, spem_uma_Whitepaper, Concept, spem_uma_Guideline, spem_uma_SupportingMaterial, spem_uma_RoleDefinitionPackage, spem_uma_TaskDefinitionPackage, spem_uma_WorkProductDefinitionPackage, spem_uma_GuidancePackage, spem_uma_DisciplinePackage, spem_uma_DomainPackage, spem_uma_WorkProductKindPackage, spem_uma_RoleSetPackage, spem_uma_Practice, Practice, uma_spem_Activity, uma_spem_MethodContentElement, spem_uma_ProcessPlanningTemplate, spem_uma_Report, spem_uma_ReusableAsset, spem_uma_Roadmap, spem_uma_ToolDefinitionPackage, spem_uma_ConfigurationPackage, spem_uma_CapabilityPatternPackage, spem_uma_DeliveryProcessPackage, spem_uma_RoleSet, uma_spem_RoleDefinition, spem_uma_QualificationPackage, spem_uma_ProcessComponentPackage, ParameterDirectionKind, WorkSequenceKind, ActivityUseKind, OptionalityKind, VariabilityType, RiskLevel, EstimatingTechnique, ExpertiseLevel, ContractKind},
    associations={parameterType2, planningData4, usageGuidance5, kind0, ownedParameter1, usedActivity14, nestedBreakdownElement15, suppressedBreakdownElement18, ownedProcessParameter21, defaultContext23, validContext25, alternatives29, linkToPredecessor7, linkToSuccessor8, predecessor10, successor11, workProduct43, lifeCycle46, source48, target50, requiredResult53, linkedRoleUse31, linkedActivity32, linkedTaskUse35, role37, linkedRoleUse39, linkedWorkProductUse41, subCategory71, suppressedMethodContentElement74, methodContentKind75, processKind55, guidance56, metric58, presentedAfter61, presentedBefore64, keyConsideration66, category68, predecessor91, estimatingConsideration93, report96, template98, toolMentor100, managedWorkProduct77, toolMentor79, usedTool81, step83, alternative86, requiredQualification88, ownedMethodContentMember121, reusedPackage123, ownedProcessMember125, requiredQualification103, source106, target108, linkedTaskDefinition111, linkedRoleDefinition113, linkedRoleDefinition116, linkedWorkProductDefinition118, aggregatedRole135, subTeam138, superTeam140, teamRole142, variabilityBasedOnElement145, task126, ownedProcessParameter129, selectedStep132, baseConfiguration156, methodPluginSelection158, processPackageSelection160, contentPackageSelection163, addedCategory166, substractedCategory169, process146, ownedPort148, processComponent150, usedPort152, tool195, configurationPackage198, any200, portType202, connectedPort205, defaultView172, processView175, ownedMethodContentPackage178, ownedProcessPackage181, basePlugin185, referencedMethodPlugin188, ownedMethodPlugin190, predefinedConfiguration192, includedPattern209, includedConnector210, containedArtifact207, deliveredProduct208, methodConfiguration219, methodLibrary220, MethodPlugin222, relatedProduct224, communicationMaterial212, educationalMaterial213, relatedTask216, relatedWorflow217, subPractice225, referencedActivity226, contentReference228, baseProcess230, ownedConfiguration232, role234},
    generalizations={gen_spem_BreakdownElement_ProcessElement, gen_spem_WorkBreakdownElement_BreakdownElement, gen_spem_Kind_ExtensibleElement, gen_spem_WorkSequence_BreakdownElement, gen_spem_Activity_WorkDefinition, gen_spem_Activity_WorkBreakdownElement, gen_spem_Activity_VariabilityElement, gen_spem_WorkProductUse_MethodContentUse, gen_spem_WorkProductUseRelationship_BreakdownElement, gen_spem_ProcessParameter_WorkDefinitionParameter, gen_spem_Milestone_WorkBreakdownElement, gen_spem_ProcessPerformer_WorkDefinitionPerformer, gen_spem_ProcessPerformer_BreakdownElement, gen_spem_RoleUse_MethodContentUse, gen_spem_ProcessResponsibilityAssignment_BreakdownElement, gen_spem_Category_MethodContentElement, gen_spem_Guidance_MethodContentElement, gen_spem_Metric_Guidance, gen_spem_MethodContentElement_DescribableElement, gen_spem_MethodContentElement_MethodContentPackageableElement, gen_spem_MethodContentElement_VariabilityElement, gen_spem_ProcessElement_DescribableElement, gen_spem_ProcessElement_ProcessPackageableElement, gen_spem_DescribableElement_ExtensibleElement, gen_spem_WorkProductDefinition_MethodContentElement, gen_spem_RoleDefinition_MethodContentElement, gen_spem_ToolDefinition_MethodContentElement, gen_spem_TaskDefinition_WorkDefinition, gen_spem_TaskDefinition_MethodContentElement, gen_spem_Step_WorkDefinition, gen_spem_Step_DescribableElement, gen_spem_Step_VariabilityElement, gen_spem_MethodContentPackageableElement_VariabilityElement, gen_spem_MethodContentPackage_MethodContentPackageableElement, gen_spem_MethodContentPackage_MethodPluginPackageableElement, gen_spem_ProcessPackage_ProcessPackageableElement, gen_spem_ProcessPackage_MethodPluginPackageableElement, gen_spem_MethodContentKind_MethodContentElement, gen_spem_WorkProductDefinitionRelationship_MethodContentElement, gen_spem_Default_TaskDefinitionPerformer_MethodContentElement, gen_spem_Default_ResponsibilityAssignment_MethodContentElement, gen_spem_Default_TaskDefinitionParameter_WorkDefinitionParameter, gen_spem_Qualification_MethodContentElement, gen_spem_CompositeRole_RoleUse, gen_spem_TeamProfile_BreakdownElement, gen_spem_ProcessComponent_ProcessPackage, gen_spem_MethodContentKind_Kind, gen_spem_ProcessKind_ProcessElement, gen_spem_ProcessKind_Kind, gen_spem_PlanningData_ProcessElement, gen_spem_MethodContentUse_BreakdownElement, gen_spem_TaskUse_MethodContentUse, gen_spem_TaskUse_WorkBreakdownElement, gen_spem_MethodConfiguration_MethodLibraryPackageableElement, gen_spem_ProcessComponentUse_MethodContentUse, gen_spem_WorkProductPort_ProcessElement, gen_spem_WorkProductPortConnector_ProcessElement, gen_spem_MethodPlugin_MethodLibraryPackageableElement, gen_spem_uma_Process_Activity, gen_spem_uma_DeliveryProcess_Process, gen_spem_WorkProductKind_MethodContentKind, gen_spem_uma_Artifact_WorkProductUse, gen_spem_uma_CapabilityPattern_Process, gen_spem_uma_Checklist_Guidance, gen_spem_uma_Concept_Guidance, gen_spem_uma_CategoryPackage_MethodContentPackage, gen_spem_uma_CustomCategory_Category, gen_spem_uma_Deliverable_WorkProductUse, gen_spem_uma_DisciplineGrouping_Category, gen_spem_uma_Domain_Category, gen_spem_uma_EstimatingConsideration_Guidance, gen_spem_uma_Example_Guidance, gen_spem_uma_Iteration_Activity, gen_spem_uma_Outcome_WorkProductUse, gen_spem_uma_Phase_Activity, gen_spem_uma_Discipline_Category, gen_spem_uma_Template_Guidance, gen_spem_uma_TermDefinition_Guidance, gen_spem_uma_ToolMentor_Guidance, gen_spem_uma_Whitepaper_Concept, gen_spem_uma_Guideline_Guidance, gen_spem_uma_SupportingMaterial_Guidance, gen_spem_uma_RoleDefinitionPackage_MethodContentPackage, gen_spem_uma_TaskDefinitionPackage_MethodContentPackage, gen_spem_uma_WorkProductDefinitionPackage_MethodContentPackage, gen_spem_uma_GuidancePackage_MethodContentPackage, gen_spem_uma_DisciplinePackage_MethodContentPackage, gen_spem_uma_DomainPackage_MethodContentPackage, gen_spem_uma_WorkProductKindPackage_MethodContentPackage, gen_spem_uma_RoleSetPackage_MethodContentPackage, gen_spem_uma_Practice_Guidance, gen_spem_uma_ProcessPlanningTemplate_Process, gen_spem_uma_Report_Guidance, gen_spem_uma_ReusableAsset_Guidance, gen_spem_uma_Roadmap_Guidance, gen_spem_uma_ToolDefinitionPackage_MethodContentPackage, gen_spem_uma_ConfigurationPackage_MethodContentPackage, gen_spem_uma_CapabilityPatternPackage_ProcessPackage, gen_spem_uma_DeliveryProcessPackage_ProcessPackage, gen_spem_uma_RoleSet_MethodContentElement, gen_spem_uma_QualificationPackage_MethodContentPackage, gen_spem_uma_ProcessComponentPackage_ProcessPackage},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)