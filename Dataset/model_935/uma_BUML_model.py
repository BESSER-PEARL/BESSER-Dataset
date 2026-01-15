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
VariabilityType: Enumeration = Enumeration(
    name="VariabilityType",
    literals={
            EnumerationLiteral(name="na"),
			EnumerationLiteral(name="contributes"),
			EnumerationLiteral(name="extends"),
			EnumerationLiteral(name="replaces"),
			EnumerationLiteral(name="localContribution"),
			EnumerationLiteral(name="localReplacement"),
			EnumerationLiteral(name="extendsReplaces")
    }
)

WorkOrderType: Enumeration = Enumeration(
    name="WorkOrderType",
    literals={
            EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish")
    }
)

# Classes
uma_ApplicableMetaClassInfo = Class(name="uma::ApplicableMetaClassInfo")
PackageableElement = Class(name="PackageableElement")
uma_Artifact = Class(name="uma::Artifact")
WorkProduct = Class(name="WorkProduct")
uma_ActivityDescription = Class(name="uma::ActivityDescription")
BreakdownElementDescription = Class(name="BreakdownElementDescription")
uma_ArtifactDescription = Class(name="uma::ArtifactDescription")
WorkProductDescription = Class(name="WorkProductDescription")
uma_BreakdownElement = Class(name="uma::BreakdownElement")
ProcessElement = Class(name="ProcessElement")
uma_BreakdownElementDescription = Class(name="uma::BreakdownElementDescription")
ContentDescription = Class(name="ContentDescription")
uma_ContentCategoryPackage = Class(name="uma::ContentCategoryPackage")
MethodPackage = Class(name="MethodPackage")
uma_CapabilityPattern = Class(name="uma::CapabilityPattern")
Process = Class(name="Process")
uma_Checklist = Class(name="uma::Checklist")
Guidance = Class(name="Guidance")
uma_CompositeRole = Class(name="uma::CompositeRole")
RoleDescriptor = Class(name="RoleDescriptor")
uma_Role = Class(name="uma::Role")
uma_Concept = Class(name="uma::Concept")
uma_Constraint = Class(name="uma::Constraint")
MethodElement = Class(name="MethodElement")
uma_ContentCategory = Class(name="uma::ContentCategory")
ContentElement = Class(name="ContentElement")
uma_ContentDescription = Class(name="uma::ContentDescription")
MethodUnit = Class(name="MethodUnit")
uma_Section = Class(name="uma::Section")
uma_ContentElement = Class(name="uma::ContentElement")
DescribableElement = Class(name="DescribableElement")
uma_Activity = Class(name="uma::Activity")
WorkBreakdownElement = Class(name="WorkBreakdownElement")
uma_Deliverable = Class(name="uma::Deliverable")
uma_ContentPackage = Class(name="uma::ContentPackage")
uma_CustomCategory = Class(name="uma::CustomCategory")
ContentCategory = Class(name="ContentCategory")
uma_DeliverableDescription = Class(name="uma::DeliverableDescription")
uma_DeliveryProcess = Class(name="uma::DeliveryProcess")
uma_DeliveryProcessDescription = Class(name="uma::DeliveryProcessDescription")
ProcessDescription = Class(name="ProcessDescription")
uma_Discipline = Class(name="uma::Discipline")
uma_DescribableElement = Class(name="uma::DescribableElement")
uma_Descriptor = Class(name="uma::Descriptor")
BreakdownElement = Class(name="BreakdownElement")
uma_DescriptorDescription = Class(name="uma::DescriptorDescription")
uma_MethodConfiguration = Class(name="uma::MethodConfiguration")
uma_MethodLibrary = Class(name="uma::MethodLibrary")
uma_DisciplineGrouping = Class(name="uma::DisciplineGrouping")
uma_DocumentRoot = Class(name="uma::DocumentRoot")
uma_EStringToStringMapEntry = Class(name="uma::EStringToStringMapEntry")
uma_EstimatingMetric = Class(name="uma::EstimatingMetric")
uma_MethodPlugin = Class(name="uma::MethodPlugin")
uma_Domain = Class(name="uma::Domain")
uma_Element = Class(name="uma::Element")
uma_Estimate = Class(name="uma::Estimate")
uma_EstimationConsiderations = Class(name="uma::EstimationConsiderations")
uma_Example = Class(name="uma::Example")
uma_Guidance = Class(name="uma::Guidance")
uma_GuidanceDescription = Class(name="uma::GuidanceDescription")
uma_Guideline = Class(name="uma::Guideline")
uma_Iteration = Class(name="uma::Iteration")
Activity = Class(name="Activity")
uma_Kind = Class(name="uma::Kind")
uma_MethodElement = Class(name="uma::MethodElement")
uma_MethodElementProperty = Class(name="uma::MethodElementProperty")
uma_MethodPackage = Class(name="uma::MethodPackage")
uma_NamedElement = Class(name="uma::NamedElement")
Element = Class(name="Element")
uma_Outcome = Class(name="uma::Outcome")
uma_MethodUnit = Class(name="uma::MethodUnit")
uma_Milestone = Class(name="uma::Milestone")
uma_PracticeDescription = Class(name="uma::PracticeDescription")
uma_PackageableElement = Class(name="uma::PackageableElement")
NamedElement = Class(name="NamedElement")
uma_Phase = Class(name="uma::Phase")
uma_PlanningData = Class(name="uma::PlanningData")
uma_Practice = Class(name="uma::Practice")
uma_ProcessComponentInterface = Class(name="uma::ProcessComponentInterface")
uma_Process = Class(name="uma::Process")
uma_ProcessComponent = Class(name="uma::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
uma_ProcessElement = Class(name="uma::ProcessElement")
uma_TaskDescriptor = Class(name="uma::TaskDescriptor")
uma_WorkProductDescriptor = Class(name="uma::WorkProductDescriptor")
uma_ProcessDescription = Class(name="uma::ProcessDescription")
ActivityDescription = Class(name="ActivityDescription")
uma_RoleDescription = Class(name="uma::RoleDescription")
uma_ProcessPackage = Class(name="uma::ProcessPackage")
uma_ProcessPlanningTemplate = Class(name="uma::ProcessPlanningTemplate")
uma_Report = Class(name="uma::Report")
uma_ReusableAsset = Class(name="uma::ReusableAsset")
uma_Roadmap = Class(name="uma::Roadmap")
uma_RoleDescriptor = Class(name="uma::RoleDescriptor")
Descriptor = Class(name="Descriptor")
uma_RoleSet = Class(name="uma::RoleSet")
uma_RoleSetGrouping = Class(name="uma::RoleSetGrouping")
uma_SupportingMaterial = Class(name="uma::SupportingMaterial")
uma_Task = Class(name="uma::Task")
uma_TaskDescription = Class(name="uma::TaskDescription")
uma_Template = Class(name="uma::Template")
uma_TermDefinition = Class(name="uma::TermDefinition")
uma_TeamProfile = Class(name="uma::TeamProfile")
uma_WorkBreakdownElement = Class(name="uma::WorkBreakdownElement")
uma_WorkOrder = Class(name="uma::WorkOrder")
uma_Tool = Class(name="uma::Tool")
uma_ToolMentor = Class(name="uma::ToolMentor")
uma_Whitepaper = Class(name="uma::Whitepaper")
Concept = Class(name="Concept")
uma_WorkDefinition = Class(name="uma::WorkDefinition")
uma_WorkProduct = Class(name="uma::WorkProduct")
uma_WorkProductDescription = Class(name="uma::WorkProductDescription")
uma_WorkProductType = Class(name="uma::WorkProductType")

# uma_ApplicableMetaClassInfo class attributes and methods
uma_ApplicableMetaClassInfo_isPrimaryExtension: Property = Property(name="isPrimaryExtension", type=StringType)
uma_ApplicableMetaClassInfo.attributes={uma_ApplicableMetaClassInfo_isPrimaryExtension}

# PackageableElement class attributes and methods

# uma_Artifact class attributes and methods
uma_Artifact_group3: Property = Property(name="group3", type=StringType)
uma_Artifact.attributes={uma_Artifact_group3}

# WorkProduct class attributes and methods

# uma_ActivityDescription class attributes and methods
uma_ActivityDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_ActivityDescription_howToStaff: Property = Property(name="howToStaff", type=StringType)
uma_ActivityDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_ActivityDescription.attributes={uma_ActivityDescription_howToStaff, uma_ActivityDescription_purpose, uma_ActivityDescription_alternatives}

# BreakdownElementDescription class attributes and methods

# uma_ArtifactDescription class attributes and methods
uma_ArtifactDescription_briefOutline: Property = Property(name="briefOutline", type=StringType)
uma_ArtifactDescription_representationOptions: Property = Property(name="representationOptions", type=StringType)
uma_ArtifactDescription_representation: Property = Property(name="representation", type=StringType)
uma_ArtifactDescription_notation: Property = Property(name="notation", type=StringType)
uma_ArtifactDescription.attributes={uma_ArtifactDescription_notation, uma_ArtifactDescription_representationOptions, uma_ArtifactDescription_briefOutline, uma_ArtifactDescription_representation}

# WorkProductDescription class attributes and methods

# uma_BreakdownElement class attributes and methods
uma_BreakdownElement_planningData: Property = Property(name="planningData", type=StringType)
uma_BreakdownElement_superActivity: Property = Property(name="superActivity", type=StringType)
uma_BreakdownElement_group1: Property = Property(name="group1", type=StringType)
uma_BreakdownElement_presentedAfter: Property = Property(name="presentedAfter", type=StringType)
uma_BreakdownElement_presentedBefore: Property = Property(name="presentedBefore", type=StringType)
uma_BreakdownElement_checklist: Property = Property(name="checklist", type=StringType)
uma_BreakdownElement_concept: Property = Property(name="concept", type=StringType)
uma_BreakdownElement_example: Property = Property(name="example", type=StringType)
uma_BreakdownElement_guideline: Property = Property(name="guideline", type=StringType)
uma_BreakdownElement_reusableAsset: Property = Property(name="reusableAsset", type=StringType)
uma_BreakdownElement_supportingMaterial: Property = Property(name="supportingMaterial", type=StringType)
uma_BreakdownElement_whitepaper: Property = Property(name="whitepaper", type=StringType)
uma_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=StringType)
uma_BreakdownElement_isOptional: Property = Property(name="isOptional", type=StringType)
uma_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=StringType)
uma_BreakdownElement_prefix: Property = Property(name="prefix", type=StringType)
uma_BreakdownElement.attributes={uma_BreakdownElement_example, uma_BreakdownElement_reusableAsset, uma_BreakdownElement_supportingMaterial, uma_BreakdownElement_isOptional, uma_BreakdownElement_prefix, uma_BreakdownElement_superActivity, uma_BreakdownElement_guideline, uma_BreakdownElement_hasMultipleOccurrences, uma_BreakdownElement_planningData, uma_BreakdownElement_presentedBefore, uma_BreakdownElement_group1, uma_BreakdownElement_checklist, uma_BreakdownElement_concept, uma_BreakdownElement_whitepaper, uma_BreakdownElement_isPlanned, uma_BreakdownElement_presentedAfter}

# ProcessElement class attributes and methods

# uma_BreakdownElementDescription class attributes and methods
uma_BreakdownElementDescription_usageGuidance: Property = Property(name="usageGuidance", type=StringType)
uma_BreakdownElementDescription.attributes={uma_BreakdownElementDescription_usageGuidance}

# ContentDescription class attributes and methods

# uma_ContentCategoryPackage class attributes and methods
uma_ContentCategoryPackage_group2: Property = Property(name="group2", type=StringType)
uma_ContentCategoryPackage.attributes={uma_ContentCategoryPackage_group2}

# MethodPackage class attributes and methods

# uma_CapabilityPattern class attributes and methods

# Process class attributes and methods

# uma_Checklist class attributes and methods

# Guidance class attributes and methods

# uma_CompositeRole class attributes and methods
uma_CompositeRole_group2: Property = Property(name="group2", type=StringType)
uma_CompositeRole.attributes={uma_CompositeRole_group2}

# RoleDescriptor class attributes and methods

# uma_Role class attributes and methods
uma_Role_group2: Property = Property(name="group2", type=StringType)
uma_Role_responsibleFor: Property = Property(name="responsibleFor", type=StringType)
uma_Role.attributes={uma_Role_group2, uma_Role_responsibleFor}

# uma_Concept class attributes and methods

# uma_Constraint class attributes and methods
uma_Constraint_mainDescription: Property = Property(name="mainDescription", type=StringType)
uma_Constraint.attributes={uma_Constraint_mainDescription}

# MethodElement class attributes and methods

# uma_ContentCategory class attributes and methods

# ContentElement class attributes and methods

# uma_ContentDescription class attributes and methods
uma_ContentDescription_mainDescription: Property = Property(name="mainDescription", type=StringType)
uma_ContentDescription_keyConsiderations: Property = Property(name="keyConsiderations", type=StringType)
uma_ContentDescription_externalId: Property = Property(name="externalId", type=StringType)
uma_ContentDescription.attributes={uma_ContentDescription_keyConsiderations, uma_ContentDescription_externalId, uma_ContentDescription_mainDescription}

# MethodUnit class attributes and methods

# uma_Section class attributes and methods
uma_Section_predecessor: Property = Property(name="predecessor", type=StringType)
uma_Section_description: Property = Property(name="description", type=StringType)
uma_Section_sectionName: Property = Property(name="sectionName", type=StringType)
uma_Section_variabilityBasedOnElement: Property = Property(name="variabilityBasedOnElement", type=StringType)
uma_Section_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_Section.attributes={uma_Section_variabilityBasedOnElement, uma_Section_variabilityType, uma_Section_description, uma_Section_predecessor, uma_Section_sectionName}

# uma_ContentElement class attributes and methods
uma_ContentElement_concept: Property = Property(name="concept", type=StringType)
uma_ContentElement_example: Property = Property(name="example", type=StringType)
uma_ContentElement_group1: Property = Property(name="group1", type=StringType)
uma_ContentElement_checklist: Property = Property(name="checklist", type=StringType)
uma_ContentElement_guideline: Property = Property(name="guideline", type=StringType)
uma_ContentElement_reusableAsset: Property = Property(name="reusableAsset", type=StringType)
uma_ContentElement_supportingMaterial: Property = Property(name="supportingMaterial", type=StringType)
uma_ContentElement_whitepaper: Property = Property(name="whitepaper", type=StringType)
uma_ContentElement_variabilityBasedOnElement: Property = Property(name="variabilityBasedOnElement", type=StringType)
uma_ContentElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_ContentElement.attributes={uma_ContentElement_concept, uma_ContentElement_checklist, uma_ContentElement_example, uma_ContentElement_variabilityType, uma_ContentElement_guideline, uma_ContentElement_variabilityBasedOnElement, uma_ContentElement_group1, uma_ContentElement_supportingMaterial, uma_ContentElement_reusableAsset, uma_ContentElement_whitepaper}

# DescribableElement class attributes and methods

# uma_Activity class attributes and methods
uma_Activity_isEnactable: Property = Property(name="isEnactable", type=StringType)
uma_Activity_roadmap: Property = Property(name="roadmap", type=StringType)
uma_Activity_precondition: Property = Property(name="precondition", type=StringType)
uma_Activity_postcondition: Property = Property(name="postcondition", type=StringType)
uma_Activity_group3: Property = Property(name="group3", type=StringType)
uma_Activity_variabilityBasedOnElement: Property = Property(name="variabilityBasedOnElement", type=StringType)
uma_Activity_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_Activity.attributes={uma_Activity_group3, uma_Activity_postcondition, uma_Activity_variabilityBasedOnElement, uma_Activity_variabilityType, uma_Activity_precondition, uma_Activity_roadmap, uma_Activity_isEnactable}

# WorkBreakdownElement class attributes and methods

# uma_Deliverable class attributes and methods
uma_Deliverable_group3: Property = Property(name="group3", type=StringType)
uma_Deliverable_deliveredWorkProduct: Property = Property(name="deliveredWorkProduct", type=StringType)
uma_Deliverable.attributes={uma_Deliverable_group3, uma_Deliverable_deliveredWorkProduct}

# uma_ContentPackage class attributes and methods
uma_ContentPackage_group2: Property = Property(name="group2", type=StringType)
uma_ContentPackage.attributes={uma_ContentPackage_group2}

# uma_CustomCategory class attributes and methods
uma_CustomCategory_group2: Property = Property(name="group2", type=StringType)
uma_CustomCategory_categorizedElement: Property = Property(name="categorizedElement", type=StringType)
uma_CustomCategory_subCategory: Property = Property(name="subCategory", type=StringType)
uma_CustomCategory.attributes={uma_CustomCategory_group2, uma_CustomCategory_categorizedElement, uma_CustomCategory_subCategory}

# ContentCategory class attributes and methods

# uma_DeliverableDescription class attributes and methods
uma_DeliverableDescription_externalDescription: Property = Property(name="externalDescription", type=StringType)
uma_DeliverableDescription_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
uma_DeliverableDescription.attributes={uma_DeliverableDescription_packagingGuidance, uma_DeliverableDescription_externalDescription}

# uma_DeliveryProcess class attributes and methods
uma_DeliveryProcess_group4: Property = Property(name="group4", type=StringType)
uma_DeliveryProcess_communicationsMaterial: Property = Property(name="communicationsMaterial", type=StringType)
uma_DeliveryProcess_educationMaterial: Property = Property(name="educationMaterial", type=StringType)
uma_DeliveryProcess.attributes={uma_DeliveryProcess_educationMaterial, uma_DeliveryProcess_communicationsMaterial, uma_DeliveryProcess_group4}

# uma_DeliveryProcessDescription class attributes and methods
uma_DeliveryProcessDescription_projectCharacteristics: Property = Property(name="projectCharacteristics", type=StringType)
uma_DeliveryProcessDescription_riskLevel: Property = Property(name="riskLevel", type=StringType)
uma_DeliveryProcessDescription_estimatingTechnique: Property = Property(name="estimatingTechnique", type=StringType)
uma_DeliveryProcessDescription_scale: Property = Property(name="scale", type=StringType)
uma_DeliveryProcessDescription_projectMemberExpertise: Property = Property(name="projectMemberExpertise", type=StringType)
uma_DeliveryProcessDescription_typeOfContract: Property = Property(name="typeOfContract", type=StringType)
uma_DeliveryProcessDescription.attributes={uma_DeliveryProcessDescription_projectCharacteristics, uma_DeliveryProcessDescription_typeOfContract, uma_DeliveryProcessDescription_projectMemberExpertise, uma_DeliveryProcessDescription_scale, uma_DeliveryProcessDescription_estimatingTechnique, uma_DeliveryProcessDescription_riskLevel}

# ProcessDescription class attributes and methods

# uma_Discipline class attributes and methods
uma_Discipline_group2: Property = Property(name="group2", type=StringType)
uma_Discipline_task: Property = Property(name="task", type=StringType)
uma_Discipline_referenceWorkflow: Property = Property(name="referenceWorkflow", type=StringType)
uma_Discipline.attributes={uma_Discipline_referenceWorkflow, uma_Discipline_group2, uma_Discipline_task}

# uma_DescribableElement class attributes and methods
uma_DescribableElement_fulfill: Property = Property(name="fulfill", type=StringType)
uma_DescribableElement_isAbstract: Property = Property(name="isAbstract", type=StringType)
uma_DescribableElement_nodeicon: Property = Property(name="nodeicon", type=StringType)
uma_DescribableElement_shapeicon: Property = Property(name="shapeicon", type=StringType)
uma_DescribableElement.attributes={uma_DescribableElement_shapeicon, uma_DescribableElement_nodeicon, uma_DescribableElement_fulfill, uma_DescribableElement_isAbstract}

# uma_Descriptor class attributes and methods
uma_Descriptor_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=StringType)
uma_Descriptor.attributes={uma_Descriptor_isSynchronizedWithSource}

# BreakdownElement class attributes and methods

# uma_DescriptorDescription class attributes and methods
uma_DescriptorDescription_refinedDescription: Property = Property(name="refinedDescription", type=StringType)
uma_DescriptorDescription.attributes={uma_DescriptorDescription_refinedDescription}

# uma_MethodConfiguration class attributes and methods
uma_MethodConfiguration_baseConfiguration: Property = Property(name="baseConfiguration", type=StringType)
uma_MethodConfiguration_methodPluginSelection: Property = Property(name="methodPluginSelection", type=StringType)
uma_MethodConfiguration_methodPackageSelection: Property = Property(name="methodPackageSelection", type=StringType)
uma_MethodConfiguration_defaultView: Property = Property(name="defaultView", type=StringType)
uma_MethodConfiguration_processView: Property = Property(name="processView", type=StringType)
uma_MethodConfiguration_subtractedCategory: Property = Property(name="subtractedCategory", type=StringType)
uma_MethodConfiguration_addedCategory: Property = Property(name="addedCategory", type=StringType)
uma_MethodConfiguration.attributes={uma_MethodConfiguration_methodPluginSelection, uma_MethodConfiguration_defaultView, uma_MethodConfiguration_subtractedCategory, uma_MethodConfiguration_methodPackageSelection, uma_MethodConfiguration_baseConfiguration, uma_MethodConfiguration_processView, uma_MethodConfiguration_addedCategory}

# uma_MethodLibrary class attributes and methods
uma_MethodLibrary_tool: Property = Property(name="tool", type=StringType)
uma_MethodLibrary.attributes={uma_MethodLibrary_tool}

# uma_DisciplineGrouping class attributes and methods
uma_DisciplineGrouping_group2: Property = Property(name="group2", type=StringType)
uma_DisciplineGrouping_discipline: Property = Property(name="discipline", type=StringType)
uma_DisciplineGrouping.attributes={uma_DisciplineGrouping_group2, uma_DisciplineGrouping_discipline}

# uma_DocumentRoot class attributes and methods
uma_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
uma_DocumentRoot.attributes={uma_DocumentRoot_mixed}

# uma_EStringToStringMapEntry class attributes and methods

# uma_EstimatingMetric class attributes and methods

# uma_MethodPlugin class attributes and methods
uma_MethodPlugin_referencedMethodPlugin: Property = Property(name="referencedMethodPlugin", type=StringType)
uma_MethodPlugin_supporting: Property = Property(name="supporting", type=StringType)
uma_MethodPlugin_userChangeable: Property = Property(name="userChangeable", type=StringType)
uma_MethodPlugin.attributes={uma_MethodPlugin_userChangeable, uma_MethodPlugin_supporting, uma_MethodPlugin_referencedMethodPlugin}

# uma_Domain class attributes and methods
uma_Domain_group2: Property = Property(name="group2", type=StringType)
uma_Domain_workProduct: Property = Property(name="workProduct", type=StringType)
uma_Domain.attributes={uma_Domain_workProduct, uma_Domain_group2}

# uma_Element class attributes and methods

# uma_Estimate class attributes and methods
uma_Estimate_estimationConsiderations: Property = Property(name="estimationConsiderations", type=StringType)
uma_Estimate_group2: Property = Property(name="group2", type=StringType)
uma_Estimate_estimationMetric: Property = Property(name="estimationMetric", type=StringType)
uma_Estimate.attributes={uma_Estimate_group2, uma_Estimate_estimationMetric, uma_Estimate_estimationConsiderations}

# uma_EstimationConsiderations class attributes and methods

# uma_Example class attributes and methods

# uma_Guidance class attributes and methods

# uma_GuidanceDescription class attributes and methods
uma_GuidanceDescription_attachment: Property = Property(name="attachment", type=StringType)
uma_GuidanceDescription.attributes={uma_GuidanceDescription_attachment}

# uma_Guideline class attributes and methods

# uma_Iteration class attributes and methods

# Activity class attributes and methods

# uma_Kind class attributes and methods
uma_Kind_applicableMetaClassInfo: Property = Property(name="applicableMetaClassInfo", type=StringType)
uma_Kind.attributes={uma_Kind_applicableMetaClassInfo}

# uma_MethodElement class attributes and methods
uma_MethodElement_id: Property = Property(name="id", type=StringType)
uma_MethodElement_orderingGuide: Property = Property(name="orderingGuide", type=StringType)
uma_MethodElement_presentationName: Property = Property(name="presentationName", type=StringType)
uma_MethodElement_group: Property = Property(name="group", type=StringType)
uma_MethodElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
uma_MethodElement_suppressed: Property = Property(name="suppressed", type=StringType)
uma_MethodElement.attributes={uma_MethodElement_group, uma_MethodElement_orderingGuide, uma_MethodElement_suppressed, uma_MethodElement_id, uma_MethodElement_briefDescription, uma_MethodElement_presentationName}

# uma_MethodElementProperty class attributes and methods
uma_MethodElementProperty_value: Property = Property(name="value", type=StringType)
uma_MethodElementProperty.attributes={uma_MethodElementProperty_value}

# uma_MethodPackage class attributes and methods
uma_MethodPackage_global: Property = Property(name="global", type=StringType)
uma_MethodPackage_group1: Property = Property(name="group1", type=StringType)
uma_MethodPackage_reusedPackage: Property = Property(name="reusedPackage", type=StringType)
uma_MethodPackage.attributes={uma_MethodPackage_group1, uma_MethodPackage_global, uma_MethodPackage_reusedPackage}

# uma_NamedElement class attributes and methods
uma_NamedElement_name: Property = Property(name="name", type=StringType)
uma_NamedElement.attributes={uma_NamedElement_name}

# Element class attributes and methods

# uma_Outcome class attributes and methods

# uma_MethodUnit class attributes and methods
uma_MethodUnit_copyright: Property = Property(name="copyright", type=StringType)
uma_MethodUnit_authors: Property = Property(name="authors", type=StringType)
uma_MethodUnit_changeDate: Property = Property(name="changeDate", type=StringType)
uma_MethodUnit_changeDescription: Property = Property(name="changeDescription", type=StringType)
uma_MethodUnit_version: Property = Property(name="version", type=StringType)
uma_MethodUnit.attributes={uma_MethodUnit_authors, uma_MethodUnit_version, uma_MethodUnit_changeDate, uma_MethodUnit_changeDescription, uma_MethodUnit_copyright}

# uma_Milestone class attributes and methods
uma_Milestone_requiredResult: Property = Property(name="requiredResult", type=StringType)
uma_Milestone.attributes={uma_Milestone_requiredResult}

# uma_PracticeDescription class attributes and methods
uma_PracticeDescription_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
uma_PracticeDescription_application: Property = Property(name="application", type=StringType)
uma_PracticeDescription_background: Property = Property(name="background", type=StringType)
uma_PracticeDescription_goals: Property = Property(name="goals", type=StringType)
uma_PracticeDescription_levelsOfAdoption: Property = Property(name="levelsOfAdoption", type=StringType)
uma_PracticeDescription_problem: Property = Property(name="problem", type=StringType)
uma_PracticeDescription.attributes={uma_PracticeDescription_problem, uma_PracticeDescription_background, uma_PracticeDescription_levelsOfAdoption, uma_PracticeDescription_goals, uma_PracticeDescription_application, uma_PracticeDescription_additionalInfo}

# uma_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# uma_Phase class attributes and methods

# uma_PlanningData class attributes and methods
uma_PlanningData_finishDate: Property = Property(name="finishDate", type=StringType)
uma_PlanningData_rank: Property = Property(name="rank", type=StringType)
uma_PlanningData_startDate: Property = Property(name="startDate", type=StringType)
uma_PlanningData.attributes={uma_PlanningData_finishDate, uma_PlanningData_startDate, uma_PlanningData_rank}

# uma_Practice class attributes and methods
uma_Practice_group2: Property = Property(name="group2", type=StringType)
uma_Practice_activityReference: Property = Property(name="activityReference", type=StringType)
uma_Practice_contentReference: Property = Property(name="contentReference", type=StringType)
uma_Practice.attributes={uma_Practice_contentReference, uma_Practice_activityReference, uma_Practice_group2}

# uma_ProcessComponentInterface class attributes and methods
uma_ProcessComponentInterface_group2: Property = Property(name="group2", type=StringType)
uma_ProcessComponentInterface.attributes={uma_ProcessComponentInterface_group2}

# uma_Process class attributes and methods
uma_Process_includesPattern: Property = Property(name="includesPattern", type=StringType)
uma_Process_defaultContext: Property = Property(name="defaultContext", type=StringType)
uma_Process_validContext: Property = Property(name="validContext", type=StringType)
uma_Process_diagramURI: Property = Property(name="diagramURI", type=StringType)
uma_Process.attributes={uma_Process_diagramURI, uma_Process_includesPattern, uma_Process_validContext, uma_Process_defaultContext}

# uma_ProcessComponent class attributes and methods
uma_ProcessComponent_copyright: Property = Property(name="copyright", type=StringType)
uma_ProcessComponent_authors: Property = Property(name="authors", type=StringType)
uma_ProcessComponent_changeDate: Property = Property(name="changeDate", type=StringType)
uma_ProcessComponent_changeDescription: Property = Property(name="changeDescription", type=StringType)
uma_ProcessComponent_version: Property = Property(name="version", type=StringType)
uma_ProcessComponent.attributes={uma_ProcessComponent_authors, uma_ProcessComponent_changeDate, uma_ProcessComponent_changeDescription, uma_ProcessComponent_copyright, uma_ProcessComponent_version}

# ProcessPackage class attributes and methods

# uma_ProcessElement class attributes and methods

# uma_TaskDescriptor class attributes and methods
uma_TaskDescriptor_group3: Property = Property(name="group3", type=StringType)
uma_TaskDescriptor_performedPrimarilyBy: Property = Property(name="performedPrimarilyBy", type=StringType)
uma_TaskDescriptor_additionallyPerformedBy: Property = Property(name="additionallyPerformedBy", type=StringType)
uma_TaskDescriptor_assistedBy: Property = Property(name="assistedBy", type=StringType)
uma_TaskDescriptor_task: Property = Property(name="task", type=StringType)
uma_TaskDescriptor_externalInput: Property = Property(name="externalInput", type=StringType)
uma_TaskDescriptor_mandatoryInput: Property = Property(name="mandatoryInput", type=StringType)
uma_TaskDescriptor_optionalInput: Property = Property(name="optionalInput", type=StringType)
uma_TaskDescriptor_output: Property = Property(name="output", type=StringType)
uma_TaskDescriptor_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=StringType)
uma_TaskDescriptor.attributes={uma_TaskDescriptor_performedPrimarilyBy, uma_TaskDescriptor_externalInput, uma_TaskDescriptor_mandatoryInput, uma_TaskDescriptor_optionalInput, uma_TaskDescriptor_isSynchronizedWithSource, uma_TaskDescriptor_assistedBy, uma_TaskDescriptor_output, uma_TaskDescriptor_additionallyPerformedBy, uma_TaskDescriptor_task, uma_TaskDescriptor_group3}

# uma_WorkProductDescriptor class attributes and methods
uma_WorkProductDescriptor_activityEntryState: Property = Property(name="activityEntryState", type=StringType)
uma_WorkProductDescriptor_activityExitState: Property = Property(name="activityExitState", type=StringType)
uma_WorkProductDescriptor_workProduct: Property = Property(name="workProduct", type=StringType)
uma_WorkProductDescriptor_responsibleRole: Property = Property(name="responsibleRole", type=StringType)
uma_WorkProductDescriptor_group2: Property = Property(name="group2", type=StringType)
uma_WorkProductDescriptor_externalInputTo: Property = Property(name="externalInputTo", type=StringType)
uma_WorkProductDescriptor_impactedBy: Property = Property(name="impactedBy", type=StringType)
uma_WorkProductDescriptor_impacts: Property = Property(name="impacts", type=StringType)
uma_WorkProductDescriptor_mandatoryInputTo: Property = Property(name="mandatoryInputTo", type=StringType)
uma_WorkProductDescriptor_optionalInputTo: Property = Property(name="optionalInputTo", type=StringType)
uma_WorkProductDescriptor_outputFrom: Property = Property(name="outputFrom", type=StringType)
uma_WorkProductDescriptor_deliverableParts: Property = Property(name="deliverableParts", type=StringType)
uma_WorkProductDescriptor.attributes={uma_WorkProductDescriptor_externalInputTo, uma_WorkProductDescriptor_impactedBy, uma_WorkProductDescriptor_optionalInputTo, uma_WorkProductDescriptor_activityEntryState, uma_WorkProductDescriptor_outputFrom, uma_WorkProductDescriptor_deliverableParts, uma_WorkProductDescriptor_group2, uma_WorkProductDescriptor_activityExitState, uma_WorkProductDescriptor_impacts, uma_WorkProductDescriptor_responsibleRole, uma_WorkProductDescriptor_mandatoryInputTo, uma_WorkProductDescriptor_workProduct}

# uma_ProcessDescription class attributes and methods
uma_ProcessDescription_scope: Property = Property(name="scope", type=StringType)
uma_ProcessDescription_usageNotes: Property = Property(name="usageNotes", type=StringType)
uma_ProcessDescription.attributes={uma_ProcessDescription_scope, uma_ProcessDescription_usageNotes}

# ActivityDescription class attributes and methods

# uma_RoleDescription class attributes and methods
uma_RoleDescription_assignmentApproaches: Property = Property(name="assignmentApproaches", type=StringType)
uma_RoleDescription_skills: Property = Property(name="skills", type=StringType)
uma_RoleDescription_synonyms: Property = Property(name="synonyms", type=StringType)
uma_RoleDescription.attributes={uma_RoleDescription_synonyms, uma_RoleDescription_skills, uma_RoleDescription_assignmentApproaches}

# uma_ProcessPackage class attributes and methods
uma_ProcessPackage_group2: Property = Property(name="group2", type=StringType)
uma_ProcessPackage.attributes={uma_ProcessPackage_group2}

# uma_ProcessPlanningTemplate class attributes and methods
uma_ProcessPlanningTemplate_group4: Property = Property(name="group4", type=StringType)
uma_ProcessPlanningTemplate_baseProcess: Property = Property(name="baseProcess", type=StringType)
uma_ProcessPlanningTemplate.attributes={uma_ProcessPlanningTemplate_group4, uma_ProcessPlanningTemplate_baseProcess}

# uma_Report class attributes and methods

# uma_ReusableAsset class attributes and methods

# uma_Roadmap class attributes and methods

# uma_RoleDescriptor class attributes and methods
uma_RoleDescriptor_role: Property = Property(name="role", type=StringType)
uma_RoleDescriptor_responsibleFor: Property = Property(name="responsibleFor", type=StringType)
uma_RoleDescriptor.attributes={uma_RoleDescriptor_role, uma_RoleDescriptor_responsibleFor}

# Descriptor class attributes and methods

# uma_RoleSet class attributes and methods
uma_RoleSet_group2: Property = Property(name="group2", type=StringType)
uma_RoleSet_role: Property = Property(name="role", type=StringType)
uma_RoleSet.attributes={uma_RoleSet_group2, uma_RoleSet_role}

# uma_RoleSetGrouping class attributes and methods
uma_RoleSetGrouping_roleSet: Property = Property(name="roleSet", type=StringType)
uma_RoleSetGrouping_group2: Property = Property(name="group2", type=StringType)
uma_RoleSetGrouping.attributes={uma_RoleSetGrouping_group2, uma_RoleSetGrouping_roleSet}

# uma_SupportingMaterial class attributes and methods

# uma_Task class attributes and methods
uma_Task_group2: Property = Property(name="group2", type=StringType)
uma_Task_mandatoryInput: Property = Property(name="mandatoryInput", type=StringType)
uma_Task_output: Property = Property(name="output", type=StringType)
uma_Task_additionallyPerformedBy: Property = Property(name="additionallyPerformedBy", type=StringType)
uma_Task_precondition: Property = Property(name="precondition", type=StringType)
uma_Task_postcondition: Property = Property(name="postcondition", type=StringType)
uma_Task_performedBy: Property = Property(name="performedBy", type=StringType)
uma_Task_optionalInput: Property = Property(name="optionalInput", type=StringType)
uma_Task_estimate: Property = Property(name="estimate", type=StringType)
uma_Task_estimationConsiderations: Property = Property(name="estimationConsiderations", type=StringType)
uma_Task_toolMentor: Property = Property(name="toolMentor", type=StringType)
uma_Task.attributes={uma_Task_precondition, uma_Task_estimationConsiderations, uma_Task_toolMentor, uma_Task_output, uma_Task_group2, uma_Task_postcondition, uma_Task_optionalInput, uma_Task_performedBy, uma_Task_additionallyPerformedBy, uma_Task_estimate, uma_Task_mandatoryInput}

# uma_TaskDescription class attributes and methods
uma_TaskDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_TaskDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_TaskDescription.attributes={uma_TaskDescription_alternatives, uma_TaskDescription_purpose}

# uma_Template class attributes and methods

# uma_TermDefinition class attributes and methods

# uma_TeamProfile class attributes and methods
uma_TeamProfile_superTeam: Property = Property(name="superTeam", type=StringType)
uma_TeamProfile_subTeam: Property = Property(name="subTeam", type=StringType)
uma_TeamProfile_group2: Property = Property(name="group2", type=StringType)
uma_TeamProfile_role: Property = Property(name="role", type=StringType)
uma_TeamProfile.attributes={uma_TeamProfile_subTeam, uma_TeamProfile_superTeam, uma_TeamProfile_group2, uma_TeamProfile_role}

# uma_WorkBreakdownElement class attributes and methods
uma_WorkBreakdownElement_group2: Property = Property(name="group2", type=StringType)
uma_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=StringType)
uma_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=StringType)
uma_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=StringType)
uma_WorkBreakdownElement.attributes={uma_WorkBreakdownElement_group2, uma_WorkBreakdownElement_isEventDriven, uma_WorkBreakdownElement_isRepeatable, uma_WorkBreakdownElement_isOngoing}

# uma_WorkOrder class attributes and methods
uma_WorkOrder_linkType: Property = Property(name="linkType", type=StringType)
uma_WorkOrder_properties: Property = Property(name="properties", type=StringType)
uma_WorkOrder_value: Property = Property(name="value", type=StringType)
uma_WorkOrder_id: Property = Property(name="id", type=StringType)
uma_WorkOrder.attributes={uma_WorkOrder_value, uma_WorkOrder_properties, uma_WorkOrder_linkType, uma_WorkOrder_id}

# uma_Tool class attributes and methods
uma_Tool_group2: Property = Property(name="group2", type=StringType)
uma_Tool_toolMentor: Property = Property(name="toolMentor", type=StringType)
uma_Tool.attributes={uma_Tool_group2, uma_Tool_toolMentor}

# uma_ToolMentor class attributes and methods

# uma_Whitepaper class attributes and methods

# Concept class attributes and methods

# uma_WorkDefinition class attributes and methods
uma_WorkDefinition_precondition: Property = Property(name="precondition", type=StringType)
uma_WorkDefinition_postcondition: Property = Property(name="postcondition", type=StringType)
uma_WorkDefinition.attributes={uma_WorkDefinition_postcondition, uma_WorkDefinition_precondition}

# uma_WorkProduct class attributes and methods
uma_WorkProduct_group2: Property = Property(name="group2", type=StringType)
uma_WorkProduct_estimate: Property = Property(name="estimate", type=StringType)
uma_WorkProduct_estimationConsiderations: Property = Property(name="estimationConsiderations", type=StringType)
uma_WorkProduct_report: Property = Property(name="report", type=StringType)
uma_WorkProduct_template: Property = Property(name="template", type=StringType)
uma_WorkProduct_toolMentor: Property = Property(name="toolMentor", type=StringType)
uma_WorkProduct.attributes={uma_WorkProduct_report, uma_WorkProduct_group2, uma_WorkProduct_toolMentor, uma_WorkProduct_template, uma_WorkProduct_estimationConsiderations, uma_WorkProduct_estimate}

# uma_WorkProductDescription class attributes and methods
uma_WorkProductDescription_impactOfNotHaving: Property = Property(name="impactOfNotHaving", type=StringType)
uma_WorkProductDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_WorkProductDescription_reasonsForNotNeeding: Property = Property(name="reasonsForNotNeeding", type=StringType)
uma_WorkProductDescription.attributes={uma_WorkProductDescription_reasonsForNotNeeding, uma_WorkProductDescription_purpose, uma_WorkProductDescription_impactOfNotHaving}

# uma_WorkProductType class attributes and methods
uma_WorkProductType_group2: Property = Property(name="group2", type=StringType)
uma_WorkProductType_workProduct: Property = Property(name="workProduct", type=StringType)
uma_WorkProductType.attributes={uma_WorkProductType_group2, uma_WorkProductType_workProduct}

# Relationships
containedArtifact1: BinaryAssociation = BinaryAssociation(
    name="containedArtifact1",
    ends={
        Property(name="uma_Artifact", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Artifact0", type=uma_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentCategory3: BinaryAssociation = BinaryAssociation(
    name="contentCategory3",
    ends={
        Property(name="uma_ContentCategory", type=uma_ContentCategoryPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentCategoryPackage", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregatedRole2: BinaryAssociation = BinaryAssociation(
    name="aggregatedRole2",
    ends={
        Property(name="uma_Role", type=uma_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CompositeRole", type=uma_Role, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
section4: BinaryAssociation = BinaryAssociation(
    name="section4",
    ends={
        Property(name="uma_Section", type=uma_ContentDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentDescription", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
breakdownElement5: BinaryAssociation = BinaryAssociation(
    name="breakdownElement5",
    ends={
        Property(name="uma_BreakdownElement", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentElement6: BinaryAssociation = BinaryAssociation(
    name="contentElement6",
    ends={
        Property(name="uma_ContentElement", type=uma_ContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentPackage", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentation7: BinaryAssociation = BinaryAssociation(
    name="presentation7",
    ends={
        Property(name="uma_ContentDescription8", type=uma_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DescribableElement", type=uma_ContentDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodConfiguration15: BinaryAssociation = BinaryAssociation(
    name="methodConfiguration15",
    ends={
        Property(name="uma_MethodConfiguration", type=uma_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DocumentRoot16", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodLibrary17: BinaryAssociation = BinaryAssociation(
    name="methodLibrary17",
    ends={
        Property(name="uma_MethodLibrary", type=uma_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DocumentRoot18", type=uma_MethodLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subDiscipline10: BinaryAssociation = BinaryAssociation(
    name="subDiscipline10",
    ends={
        Property(name="uma_Discipline", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline9", type=uma_Discipline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap11: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap11",
    ends={
        Property(name="uma_EStringToStringMapEntry", type=uma_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DocumentRoot", type=uma_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation12: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation12",
    ends={
        Property(name="uma_EStringToStringMapEntry14", type=uma_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DocumentRoot13", type=uma_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodPlugin19: BinaryAssociation = BinaryAssociation(
    name="methodPlugin19",
    ends={
        Property(name="uma_MethodPlugin", type=uma_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DocumentRoot20", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subdomain22: BinaryAssociation = BinaryAssociation(
    name="subdomain22",
    ends={
        Property(name="uma_Domain", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain21", type=uma_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule23: BinaryAssociation = BinaryAssociation(
    name="ownedRule23",
    ends={
        Property(name="uma_Constraint", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement", type=uma_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodElementProperty24: BinaryAssociation = BinaryAssociation(
    name="methodElementProperty24",
    ends={
        Property(name="uma_MethodElementProperty", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement25", type=uma_MethodElementProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodPlugin26: BinaryAssociation = BinaryAssociation(
    name="methodPlugin26",
    ends={
        Property(name="uma_MethodPlugin28", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary27", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodConfiguration29: BinaryAssociation = BinaryAssociation(
    name="methodConfiguration29",
    ends={
        Property(name="uma_MethodConfiguration31", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary30", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodPackage33: BinaryAssociation = BinaryAssociation(
    name="methodPackage33",
    ends={
        Property(name="uma_MethodPackage", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage32", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodPackage34: BinaryAssociation = BinaryAssociation(
    name="methodPackage34",
    ends={
        Property(name="uma_MethodPackage36", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin35", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPractice38: BinaryAssociation = BinaryAssociation(
    name="subPractice38",
    ends={
        Property(name="uma_Practice", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice37", type=uma_Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface39: BinaryAssociation = BinaryAssociation(
    name="interface39",
    ends={
        Property(name="uma_ProcessComponentInterface", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
process40: BinaryAssociation = BinaryAssociation(
    name="process40",
    ends={
        Property(name="uma_Process", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent41", type=uma_Process, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interfaceSpecification42: BinaryAssociation = BinaryAssociation(
    name="interfaceSpecification42",
    ends={
        Property(name="uma_TaskDescriptor", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface43", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceIO44: BinaryAssociation = BinaryAssociation(
    name="interfaceIO44",
    ends={
        Property(name="uma_WorkProductDescriptor", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface45", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
processElement46: BinaryAssociation = BinaryAssociation(
    name="processElement46",
    ends={
        Property(name="uma_ProcessElement", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage", type=uma_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSection48: BinaryAssociation = BinaryAssociation(
    name="subSection48",
    ends={
        Property(name="uma_Section49", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section47", type=uma_Section, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
step50: BinaryAssociation = BinaryAssociation(
    name="step50",
    ends={
        Property(name="uma_Section52", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor51", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor53: BinaryAssociation = BinaryAssociation(
    name="predecessor53",
    ends={
        Property(name="uma_WorkOrder", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkBreakdownElement", type=uma_WorkOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uma_ApplicableMetaClassInfo_PackageableElement = Generalization(general=PackageableElement, specific=uma_ApplicableMetaClassInfo)
gen_uma_Artifact_WorkProduct = Generalization(general=WorkProduct, specific=uma_Artifact)
gen_uma_ActivityDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_ActivityDescription)
gen_uma_ArtifactDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_ArtifactDescription)
gen_uma_BreakdownElement_ProcessElement = Generalization(general=ProcessElement, specific=uma_BreakdownElement)
gen_uma_BreakdownElementDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_BreakdownElementDescription)
gen_uma_ContentCategoryPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ContentCategoryPackage)
gen_uma_CapabilityPattern_Process = Generalization(general=Process, specific=uma_CapabilityPattern)
gen_uma_Checklist_Guidance = Generalization(general=Guidance, specific=uma_Checklist)
gen_uma_CompositeRole_RoleDescriptor = Generalization(general=RoleDescriptor, specific=uma_CompositeRole)
gen_uma_Concept_Guidance = Generalization(general=Guidance, specific=uma_Concept)
gen_uma_Constraint_MethodElement = Generalization(general=MethodElement, specific=uma_Constraint)
gen_uma_ContentCategory_ContentElement = Generalization(general=ContentElement, specific=uma_ContentCategory)
gen_uma_ContentDescription_MethodUnit = Generalization(general=MethodUnit, specific=uma_ContentDescription)
gen_uma_ContentElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ContentElement)
gen_uma_Activity_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Activity)
gen_uma_Deliverable_WorkProduct = Generalization(general=WorkProduct, specific=uma_Deliverable)
gen_uma_ContentPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ContentPackage)
gen_uma_CustomCategory_ContentCategory = Generalization(general=ContentCategory, specific=uma_CustomCategory)
gen_uma_DeliverableDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_DeliverableDescription)
gen_uma_DeliveryProcess_Process = Generalization(general=Process, specific=uma_DeliveryProcess)
gen_uma_DeliveryProcessDescription_ProcessDescription = Generalization(general=ProcessDescription, specific=uma_DeliveryProcessDescription)
gen_uma_Discipline_ContentCategory = Generalization(general=ContentCategory, specific=uma_Discipline)
gen_uma_DescribableElement_MethodElement = Generalization(general=MethodElement, specific=uma_DescribableElement)
gen_uma_Descriptor_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_Descriptor)
gen_uma_DescriptorDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_DescriptorDescription)
gen_uma_DisciplineGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_DisciplineGrouping)
gen_uma_EstimatingMetric_Guidance = Generalization(general=Guidance, specific=uma_EstimatingMetric)
gen_uma_Domain_ContentCategory = Generalization(general=ContentCategory, specific=uma_Domain)
gen_uma_Estimate_Guidance = Generalization(general=Guidance, specific=uma_Estimate)
gen_uma_MethodConfiguration_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodConfiguration)
gen_uma_EstimationConsiderations_Guidance = Generalization(general=Guidance, specific=uma_EstimationConsiderations)
gen_uma_Example_Guidance = Generalization(general=Guidance, specific=uma_Example)
gen_uma_Guidance_ContentElement = Generalization(general=ContentElement, specific=uma_Guidance)
gen_uma_GuidanceDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_GuidanceDescription)
gen_uma_Guideline_Guidance = Generalization(general=Guidance, specific=uma_Guideline)
gen_uma_Iteration_Activity = Generalization(general=Activity, specific=uma_Iteration)
gen_uma_Kind_ContentElement = Generalization(general=ContentElement, specific=uma_Kind)
gen_uma_MethodElement_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElement)
gen_uma_MethodPlugin_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodPlugin)
gen_uma_MethodElementProperty_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElementProperty)
gen_uma_MethodLibrary_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodLibrary)
gen_uma_MethodPackage_MethodElement = Generalization(general=MethodElement, specific=uma_MethodPackage)
gen_uma_NamedElement_Element = Generalization(general=Element, specific=uma_NamedElement)
gen_uma_Outcome_WorkProduct = Generalization(general=WorkProduct, specific=uma_Outcome)
gen_uma_MethodUnit_MethodElement = Generalization(general=MethodElement, specific=uma_MethodUnit)
gen_uma_Milestone_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Milestone)
gen_uma_PracticeDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_PracticeDescription)
gen_uma_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uma_PackageableElement)
gen_uma_Phase_Activity = Generalization(general=Activity, specific=uma_Phase)
gen_uma_PlanningData_ProcessElement = Generalization(general=ProcessElement, specific=uma_PlanningData)
gen_uma_Practice_Guidance = Generalization(general=Guidance, specific=uma_Practice)
gen_uma_Process_Activity = Generalization(general=Activity, specific=uma_Process)
gen_uma_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=uma_ProcessComponent)
gen_uma_ProcessElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ProcessElement)
gen_uma_ProcessComponentInterface_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_ProcessComponentInterface)
gen_uma_ProcessDescription_ActivityDescription = Generalization(general=ActivityDescription, specific=uma_ProcessDescription)
gen_uma_RoleDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_RoleDescription)
gen_uma_ProcessPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ProcessPackage)
gen_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=uma_ProcessPlanningTemplate)
gen_uma_Report_Guidance = Generalization(general=Guidance, specific=uma_Report)
gen_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=uma_ReusableAsset)
gen_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=uma_Roadmap)
gen_uma_Role_ContentElement = Generalization(general=ContentElement, specific=uma_Role)
gen_uma_Section_MethodElement = Generalization(general=MethodElement, specific=uma_Section)
gen_uma_RoleDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_RoleDescriptor)
gen_uma_RoleSet_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSet)
gen_uma_RoleSetGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSetGrouping)
gen_uma_SupportingMaterial_Guidance = Generalization(general=Guidance, specific=uma_SupportingMaterial)
gen_uma_Task_ContentElement = Generalization(general=ContentElement, specific=uma_Task)
gen_uma_TaskDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_TaskDescription)
gen_uma_TaskDescriptor_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_TaskDescriptor)
gen_uma_Template_Guidance = Generalization(general=Guidance, specific=uma_Template)
gen_uma_TeamProfile_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_TeamProfile)
gen_uma_WorkBreakdownElement_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_WorkBreakdownElement)
gen_uma_TermDefinition_Guidance = Generalization(general=Guidance, specific=uma_TermDefinition)
gen_uma_Tool_ContentCategory = Generalization(general=ContentCategory, specific=uma_Tool)
gen_uma_ToolMentor_Guidance = Generalization(general=Guidance, specific=uma_ToolMentor)
gen_uma_Whitepaper_Concept = Generalization(general=Concept, specific=uma_Whitepaper)
gen_uma_WorkDefinition_MethodElement = Generalization(general=MethodElement, specific=uma_WorkDefinition)
gen_uma_WorkProductDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_WorkProductDescriptor)
gen_uma_WorkProduct_ContentElement = Generalization(general=ContentElement, specific=uma_WorkProduct)
gen_uma_WorkProductDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_WorkProductDescription)
gen_uma_WorkProductType_ContentCategory = Generalization(general=ContentCategory, specific=uma_WorkProductType)

# Domain Model
domain_model = DomainModel(
    name="uma",
    types={uma_ApplicableMetaClassInfo, PackageableElement, uma_Artifact, WorkProduct, uma_ActivityDescription, BreakdownElementDescription, uma_ArtifactDescription, WorkProductDescription, uma_BreakdownElement, ProcessElement, uma_BreakdownElementDescription, ContentDescription, uma_ContentCategoryPackage, MethodPackage, uma_CapabilityPattern, Process, uma_Checklist, Guidance, uma_CompositeRole, RoleDescriptor, uma_Role, uma_Concept, uma_Constraint, MethodElement, uma_ContentCategory, ContentElement, uma_ContentDescription, MethodUnit, uma_Section, uma_ContentElement, DescribableElement, uma_Activity, WorkBreakdownElement, uma_Deliverable, uma_ContentPackage, uma_CustomCategory, ContentCategory, uma_DeliverableDescription, uma_DeliveryProcess, uma_DeliveryProcessDescription, ProcessDescription, uma_Discipline, uma_DescribableElement, uma_Descriptor, BreakdownElement, uma_DescriptorDescription, uma_MethodConfiguration, uma_MethodLibrary, uma_DisciplineGrouping, uma_DocumentRoot, uma_EStringToStringMapEntry, uma_EstimatingMetric, uma_MethodPlugin, uma_Domain, uma_Element, uma_Estimate, uma_EstimationConsiderations, uma_Example, uma_Guidance, uma_GuidanceDescription, uma_Guideline, uma_Iteration, Activity, uma_Kind, uma_MethodElement, uma_MethodElementProperty, uma_MethodPackage, uma_NamedElement, Element, uma_Outcome, uma_MethodUnit, uma_Milestone, uma_PracticeDescription, uma_PackageableElement, NamedElement, uma_Phase, uma_PlanningData, uma_Practice, uma_ProcessComponentInterface, uma_Process, uma_ProcessComponent, ProcessPackage, uma_ProcessElement, uma_TaskDescriptor, uma_WorkProductDescriptor, uma_ProcessDescription, ActivityDescription, uma_RoleDescription, uma_ProcessPackage, uma_ProcessPlanningTemplate, uma_Report, uma_ReusableAsset, uma_Roadmap, uma_RoleDescriptor, Descriptor, uma_RoleSet, uma_RoleSetGrouping, uma_SupportingMaterial, uma_Task, uma_TaskDescription, uma_Template, uma_TermDefinition, uma_TeamProfile, uma_WorkBreakdownElement, uma_WorkOrder, uma_Tool, uma_ToolMentor, uma_Whitepaper, Concept, uma_WorkDefinition, uma_WorkProduct, uma_WorkProductDescription, uma_WorkProductType, VariabilityType, WorkOrderType},
    associations={containedArtifact1, contentCategory3, aggregatedRole2, section4, breakdownElement5, contentElement6, presentation7, methodConfiguration15, methodLibrary17, subDiscipline10, xMLNSPrefixMap11, xSISchemaLocation12, methodPlugin19, subdomain22, ownedRule23, methodElementProperty24, methodPlugin26, methodConfiguration29, methodPackage33, methodPackage34, subPractice38, interface39, process40, interfaceSpecification42, interfaceIO44, processElement46, subSection48, step50, predecessor53},
    generalizations={gen_uma_ApplicableMetaClassInfo_PackageableElement, gen_uma_Artifact_WorkProduct, gen_uma_ActivityDescription_BreakdownElementDescription, gen_uma_ArtifactDescription_WorkProductDescription, gen_uma_BreakdownElement_ProcessElement, gen_uma_BreakdownElementDescription_ContentDescription, gen_uma_ContentCategoryPackage_MethodPackage, gen_uma_CapabilityPattern_Process, gen_uma_Checklist_Guidance, gen_uma_CompositeRole_RoleDescriptor, gen_uma_Concept_Guidance, gen_uma_Constraint_MethodElement, gen_uma_ContentCategory_ContentElement, gen_uma_ContentDescription_MethodUnit, gen_uma_ContentElement_DescribableElement, gen_uma_Activity_WorkBreakdownElement, gen_uma_Deliverable_WorkProduct, gen_uma_ContentPackage_MethodPackage, gen_uma_CustomCategory_ContentCategory, gen_uma_DeliverableDescription_WorkProductDescription, gen_uma_DeliveryProcess_Process, gen_uma_DeliveryProcessDescription_ProcessDescription, gen_uma_Discipline_ContentCategory, gen_uma_DescribableElement_MethodElement, gen_uma_Descriptor_BreakdownElement, gen_uma_DescriptorDescription_BreakdownElementDescription, gen_uma_DisciplineGrouping_ContentCategory, gen_uma_EstimatingMetric_Guidance, gen_uma_Domain_ContentCategory, gen_uma_Estimate_Guidance, gen_uma_MethodConfiguration_MethodUnit, gen_uma_EstimationConsiderations_Guidance, gen_uma_Example_Guidance, gen_uma_Guidance_ContentElement, gen_uma_GuidanceDescription_ContentDescription, gen_uma_Guideline_Guidance, gen_uma_Iteration_Activity, gen_uma_Kind_ContentElement, gen_uma_MethodElement_PackageableElement, gen_uma_MethodPlugin_MethodUnit, gen_uma_MethodElementProperty_PackageableElement, gen_uma_MethodLibrary_MethodUnit, gen_uma_MethodPackage_MethodElement, gen_uma_NamedElement_Element, gen_uma_Outcome_WorkProduct, gen_uma_MethodUnit_MethodElement, gen_uma_Milestone_WorkBreakdownElement, gen_uma_PracticeDescription_ContentDescription, gen_uma_PackageableElement_NamedElement, gen_uma_Phase_Activity, gen_uma_PlanningData_ProcessElement, gen_uma_Practice_Guidance, gen_uma_Process_Activity, gen_uma_ProcessComponent_ProcessPackage, gen_uma_ProcessElement_DescribableElement, gen_uma_ProcessComponentInterface_BreakdownElement, gen_uma_ProcessDescription_ActivityDescription, gen_uma_RoleDescription_ContentDescription, gen_uma_ProcessPackage_MethodPackage, gen_uma_ProcessPlanningTemplate_Process, gen_uma_Report_Guidance, gen_uma_ReusableAsset_Guidance, gen_uma_Roadmap_Guidance, gen_uma_Role_ContentElement, gen_uma_Section_MethodElement, gen_uma_RoleDescriptor_Descriptor, gen_uma_RoleSet_ContentCategory, gen_uma_RoleSetGrouping_ContentCategory, gen_uma_SupportingMaterial_Guidance, gen_uma_Task_ContentElement, gen_uma_TaskDescription_ContentDescription, gen_uma_TaskDescriptor_WorkBreakdownElement, gen_uma_Template_Guidance, gen_uma_TeamProfile_BreakdownElement, gen_uma_WorkBreakdownElement_BreakdownElement, gen_uma_TermDefinition_Guidance, gen_uma_Tool_ContentCategory, gen_uma_ToolMentor_Guidance, gen_uma_Whitepaper_Concept, gen_uma_WorkDefinition_MethodElement, gen_uma_WorkProductDescriptor_Descriptor, gen_uma_WorkProduct_ContentElement, gen_uma_WorkProductDescription_ContentDescription, gen_uma_WorkProductType_ContentCategory},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)