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
uma_NamedElement = Class(name="uma::NamedElement", is_abstract=True)
Element = Class(name="Element")
uma_Element = Class(name="uma::Element", is_abstract=True)
uma_Package = Class(name="uma::Package")
Namespace = Class(name="Namespace")
uma_Namespace = Class(name="uma::Namespace", is_abstract=True)
uma_Constraint = Class(name="uma::Constraint")
MethodElement = Class(name="MethodElement")
uma_Classifier = Class(name="uma::Classifier", is_abstract=True)
Type = Class(name="Type")
uma_Type = Class(name="uma::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
uma_PackageableElement = Class(name="uma::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
uma_MethodElementProperty = Class(name="uma::MethodElementProperty")
uma_Kind = Class(name="uma::Kind")
ContentElement = Class(name="ContentElement")
uma_ApplicableMetaClassInfo = Class(name="uma::ApplicableMetaClassInfo")
uma_ContentElement = Class(name="uma::ContentElement", is_abstract=True)
DescribableElement = Class(name="DescribableElement")
VariabilityElement = Class(name="VariabilityElement")
uma_SupportingMaterial = Class(name="uma::SupportingMaterial")
uma_Concept = Class(name="uma::Concept")
uma_MethodElement = Class(name="uma::MethodElement", is_abstract=True)
uma_ContentDescription = Class(name="uma::ContentDescription")
MethodUnit = Class(name="MethodUnit")
uma_Section = Class(name="uma::Section")
uma_MethodUnit = Class(name="uma::MethodUnit", is_abstract=True)
uma_Checklist = Class(name="uma::Checklist")
uma_Guideline = Class(name="uma::Guideline")
uma_Example = Class(name="uma::Example")
uma_ReusableAsset = Class(name="uma::ReusableAsset")
uma_TermDefinition = Class(name="uma::TermDefinition")
uma_DescribableElement = Class(name="uma::DescribableElement", is_abstract=True)
Classifier = Class(name="Classifier")
uma_VariabilityElement = Class(name="uma::VariabilityElement", is_abstract=True)
Guidance = Class(name="Guidance")
uma_Guidance = Class(name="uma::Guidance", is_abstract=True)
uma_Artifact = Class(name="uma::Artifact")
WorkProduct = Class(name="WorkProduct")
uma_WorkProduct = Class(name="uma::WorkProduct")
FulfillableElement = Class(name="FulfillableElement")
uma_Deliverable = Class(name="uma::Deliverable")
uma_Outcome = Class(name="uma::Outcome")
uma_Step = Class(name="uma::Step")
Section = Class(name="Section")
WorkDefinition = Class(name="WorkDefinition")
uma_WorkDefinition = Class(name="uma::WorkDefinition", is_abstract=True)
uma_Report = Class(name="uma::Report")
uma_Template = Class(name="uma::Template")
uma_ToolMentor = Class(name="uma::ToolMentor")
uma_EstimationConsiderations = Class(name="uma::EstimationConsiderations")
uma_FulfillableElement = Class(name="uma::FulfillableElement")
uma_Whitepaper = Class(name="uma::Whitepaper")
Concept = Class(name="Concept")
uma_Task = Class(name="uma::Task")
uma_Role = Class(name="uma::Role")
uma_DeliverableDescription = Class(name="uma::DeliverableDescription")
uma_RoleDescription = Class(name="uma::RoleDescription")
uma_TaskDescription = Class(name="uma::TaskDescription")
uma_GuidanceDescription = Class(name="uma::GuidanceDescription")
uma_PracticeDescription = Class(name="uma::PracticeDescription")
uma_ArtifactDescription = Class(name="uma::ArtifactDescription")
WorkProductDescription = Class(name="WorkProductDescription")
uma_WorkProductDescription = Class(name="uma::WorkProductDescription")
ContentDescription = Class(name="ContentDescription")
ContentCategory = Class(name="ContentCategory")
uma_ContentCategory = Class(name="uma::ContentCategory", is_abstract=True)
uma_Domain = Class(name="uma::Domain")
uma_WorkProductType = Class(name="uma::WorkProductType")
uma_DisciplineGrouping = Class(name="uma::DisciplineGrouping")
uma_Discipline = Class(name="uma::Discipline")
uma_RoleSet = Class(name="uma::RoleSet")
BreakdownElement = Class(name="BreakdownElement")
uma_WorkOrder = Class(name="uma::WorkOrder")
ProcessElement = Class(name="ProcessElement")
uma_Activity = Class(name="uma::Activity")
WorkBreakdownElement = Class(name="WorkBreakdownElement")
uma_BreakdownElement = Class(name="uma::BreakdownElement", is_abstract=True)
uma_Roadmap = Class(name="uma::Roadmap")
uma_WorkBreakdownElement = Class(name="uma::WorkBreakdownElement", is_abstract=True)
uma_PlanningData = Class(name="uma::PlanningData")
uma_ProcessElement = Class(name="uma::ProcessElement", is_abstract=True)
uma_Tool = Class(name="uma::Tool")
uma_RoleSetGrouping = Class(name="uma::RoleSetGrouping")
uma_CustomCategory = Class(name="uma::CustomCategory")
uma_Milestone = Class(name="uma::Milestone")
uma_WorkProductDescriptor = Class(name="uma::WorkProductDescriptor")
Descriptor = Class(name="Descriptor")
uma_Descriptor = Class(name="uma::Descriptor", is_abstract=True)
uma_MethodPackage = Class(name="uma::MethodPackage", is_abstract=True)
Package = Class(name="Package")
uma_ContentPackage = Class(name="uma::ContentPackage")
MethodPackage = Class(name="MethodPackage")
uma_TaskDescriptor = Class(name="uma::TaskDescriptor")
uma_Iteration = Class(name="uma::Iteration")
Activity = Class(name="Activity")
uma_Phase = Class(name="uma::Phase")
uma_TeamProfile = Class(name="uma::TeamProfile")
uma_RoleDescriptor = Class(name="uma::RoleDescriptor")
uma_Process = Class(name="uma::Process", is_abstract=True)
uma_CapabilityPattern = Class(name="uma::CapabilityPattern")
uma_MethodConfiguration = Class(name="uma::MethodConfiguration")
uma_MethodPlugin = Class(name="uma::MethodPlugin")
uma_CompositeRole = Class(name="uma::CompositeRole")
RoleDescriptor = Class(name="RoleDescriptor")
uma_DeliveryProcess = Class(name="uma::DeliveryProcess")
Process = Class(name="Process")
uma_Practice = Class(name="uma::Practice")
uma_BreakdownElementDescription = Class(name="uma::BreakdownElementDescription")
uma_ActivityDescription = Class(name="uma::ActivityDescription")
BreakdownElementDescription = Class(name="BreakdownElementDescription")
uma_DeliveryProcessDescription = Class(name="uma::DeliveryProcessDescription")
ProcessDescription = Class(name="ProcessDescription")
uma_ProcessPlanningTemplate = Class(name="uma::ProcessPlanningTemplate")
uma_DescriptorDescription = Class(name="uma::DescriptorDescription")
uma_ProcessComponentDescriptor = Class(name="uma::ProcessComponentDescriptor")
uma_ProcessComponent = Class(name="uma::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
uma_ProcessComponentInterface = Class(name="uma::ProcessComponentInterface")
uma_ProcessPackage = Class(name="uma::ProcessPackage")
uma_Diagram = Class(name="uma::Diagram")
uma_ProcessDescription = Class(name="uma::ProcessDescription")
ActivityDescription = Class(name="ActivityDescription")
uma_DiagramElement = Class(name="uma::DiagramElement", is_abstract=True)
uma_GraphConnector = Class(name="uma::GraphConnector")
uma_Reference = Class(name="uma::Reference")
uma_Property = Class(name="uma::Property")
GraphNode = Class(name="GraphNode")
uma_DiagramLink = Class(name="uma::DiagramLink")
uma_SemanticModelBridge = Class(name="uma::SemanticModelBridge", is_abstract=True)
uma_Point = Class(name="uma::Point")
uma_GraphNode = Class(name="uma::GraphNode")
GraphElement = Class(name="GraphElement")
uma_Dimension = Class(name="uma::Dimension")
uma_GraphElement = Class(name="uma::GraphElement", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
uma_GraphEdge = Class(name="uma::GraphEdge")
uma_LeafElement = Class(name="uma::LeafElement", is_abstract=True)
uma_TextElement = Class(name="uma::TextElement")
LeafElement = Class(name="LeafElement")
uma_Image = Class(name="uma::Image")
uma_GraphicPrimitive = Class(name="uma::GraphicPrimitive", is_abstract=True)
uma_Polyline = Class(name="uma::Polyline")
GraphicPrimitive = Class(name="GraphicPrimitive")
uma_Ellipse = Class(name="uma::Ellipse")
uma_SimpleSemanticModelElement = Class(name="uma::SimpleSemanticModelElement")
SemanticModelBridge = Class(name="SemanticModelBridge")
uma_UMASemanticModelBridge = Class(name="uma::UMASemanticModelBridge")
uma_CoreSemanticModelBridge = Class(name="uma::CoreSemanticModelBridge")
uma_ProcessFamily = Class(name="uma::ProcessFamily")
MethodConfiguration = Class(name="MethodConfiguration")
uma_MethodLibrary = Class(name="uma::MethodLibrary")

# uma_NamedElement class attributes and methods
uma_NamedElement_name: Property = Property(name="name", type=StringType)
uma_NamedElement.attributes={uma_NamedElement_name}

# Element class attributes and methods

# uma_Element class attributes and methods

# uma_Package class attributes and methods

# Namespace class attributes and methods

# uma_Namespace class attributes and methods

# uma_Constraint class attributes and methods
uma_Constraint_body: Property = Property(name="body", type=StringType)
uma_Constraint.attributes={uma_Constraint_body}

# MethodElement class attributes and methods

# uma_Classifier class attributes and methods
uma_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
uma_Classifier.attributes={uma_Classifier_isAbstract}

# Type class attributes and methods

# uma_Type class attributes and methods

# PackageableElement class attributes and methods

# uma_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# uma_MethodElementProperty class attributes and methods
uma_MethodElementProperty_value: Property = Property(name="value", type=StringType)
uma_MethodElementProperty.attributes={uma_MethodElementProperty_value}

# uma_Kind class attributes and methods

# ContentElement class attributes and methods

# uma_ApplicableMetaClassInfo class attributes and methods
uma_ApplicableMetaClassInfo_isPrimaryExtension: Property = Property(name="isPrimaryExtension", type=StringType)
uma_ApplicableMetaClassInfo.attributes={uma_ApplicableMetaClassInfo_isPrimaryExtension}

# uma_ContentElement class attributes and methods

# DescribableElement class attributes and methods

# VariabilityElement class attributes and methods

# uma_SupportingMaterial class attributes and methods

# uma_Concept class attributes and methods

# uma_MethodElement class attributes and methods
uma_MethodElement_suppressed: Property = Property(name="suppressed", type=StringType)
uma_MethodElement_orderingGuide: Property = Property(name="orderingGuide", type=StringType)
uma_MethodElement_guid: Property = Property(name="guid", type=StringType)
uma_MethodElement_presentationName: Property = Property(name="presentationName", type=StringType)
uma_MethodElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
uma_MethodElement.attributes={uma_MethodElement_briefDescription, uma_MethodElement_suppressed, uma_MethodElement_guid, uma_MethodElement_orderingGuide, uma_MethodElement_presentationName}

# uma_ContentDescription class attributes and methods
uma_ContentDescription_mainDescription: Property = Property(name="mainDescription", type=StringType)
uma_ContentDescription_externalId: Property = Property(name="externalId", type=StringType)
uma_ContentDescription_keyConsiderations: Property = Property(name="keyConsiderations", type=StringType)
uma_ContentDescription_longPresentationName: Property = Property(name="longPresentationName", type=StringType)
uma_ContentDescription.attributes={uma_ContentDescription_mainDescription, uma_ContentDescription_keyConsiderations, uma_ContentDescription_longPresentationName, uma_ContentDescription_externalId}

# MethodUnit class attributes and methods

# uma_Section class attributes and methods
uma_Section_sectionName: Property = Property(name="sectionName", type=StringType)
uma_Section_sectionDescription: Property = Property(name="sectionDescription", type=StringType)
uma_Section.attributes={uma_Section_sectionName, uma_Section_sectionDescription}

# uma_MethodUnit class attributes and methods
uma_MethodUnit_authors: Property = Property(name="authors", type=StringType)
uma_MethodUnit_changeDate: Property = Property(name="changeDate", type=StringType)
uma_MethodUnit_changeDescription: Property = Property(name="changeDescription", type=StringType)
uma_MethodUnit_version: Property = Property(name="version", type=StringType)
uma_MethodUnit.attributes={uma_MethodUnit_authors, uma_MethodUnit_changeDate, uma_MethodUnit_version, uma_MethodUnit_changeDescription}

# uma_Checklist class attributes and methods

# uma_Guideline class attributes and methods

# uma_Example class attributes and methods

# uma_ReusableAsset class attributes and methods

# uma_TermDefinition class attributes and methods

# uma_DescribableElement class attributes and methods
uma_DescribableElement_shapeicon: Property = Property(name="shapeicon", type=StringType)
uma_DescribableElement_nodeicon: Property = Property(name="nodeicon", type=StringType)
uma_DescribableElement.attributes={uma_DescribableElement_shapeicon, uma_DescribableElement_nodeicon}

# Classifier class attributes and methods

# uma_VariabilityElement class attributes and methods
uma_VariabilityElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_VariabilityElement.attributes={uma_VariabilityElement_variabilityType}

# Guidance class attributes and methods

# uma_Guidance class attributes and methods

# uma_Artifact class attributes and methods

# WorkProduct class attributes and methods

# uma_WorkProduct class attributes and methods

# FulfillableElement class attributes and methods

# uma_Deliverable class attributes and methods

# uma_Outcome class attributes and methods

# uma_Step class attributes and methods

# Section class attributes and methods

# WorkDefinition class attributes and methods

# uma_WorkDefinition class attributes and methods

# uma_Report class attributes and methods

# uma_Template class attributes and methods

# uma_ToolMentor class attributes and methods

# uma_EstimationConsiderations class attributes and methods

# uma_FulfillableElement class attributes and methods

# uma_Whitepaper class attributes and methods

# Concept class attributes and methods

# uma_Task class attributes and methods

# uma_Role class attributes and methods

# uma_DeliverableDescription class attributes and methods
uma_DeliverableDescription_externalDescription: Property = Property(name="externalDescription", type=StringType)
uma_DeliverableDescription_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
uma_DeliverableDescription.attributes={uma_DeliverableDescription_packagingGuidance, uma_DeliverableDescription_externalDescription}

# uma_RoleDescription class attributes and methods
uma_RoleDescription_skills: Property = Property(name="skills", type=StringType)
uma_RoleDescription_assignmentApproaches: Property = Property(name="assignmentApproaches", type=StringType)
uma_RoleDescription_synonyms: Property = Property(name="synonyms", type=StringType)
uma_RoleDescription.attributes={uma_RoleDescription_synonyms, uma_RoleDescription_skills, uma_RoleDescription_assignmentApproaches}

# uma_TaskDescription class attributes and methods
uma_TaskDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_TaskDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_TaskDescription.attributes={uma_TaskDescription_purpose, uma_TaskDescription_alternatives}

# uma_GuidanceDescription class attributes and methods
uma_GuidanceDescription_attachments: Property = Property(name="attachments", type=StringType)
uma_GuidanceDescription.attributes={uma_GuidanceDescription_attachments}

# uma_PracticeDescription class attributes and methods
uma_PracticeDescription_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
uma_PracticeDescription_problem: Property = Property(name="problem", type=StringType)
uma_PracticeDescription_background: Property = Property(name="background", type=StringType)
uma_PracticeDescription_goals: Property = Property(name="goals", type=StringType)
uma_PracticeDescription_application: Property = Property(name="application", type=StringType)
uma_PracticeDescription_levelsOfAdoption: Property = Property(name="levelsOfAdoption", type=StringType)
uma_PracticeDescription.attributes={uma_PracticeDescription_background, uma_PracticeDescription_goals, uma_PracticeDescription_levelsOfAdoption, uma_PracticeDescription_problem, uma_PracticeDescription_application, uma_PracticeDescription_additionalInfo}

# uma_ArtifactDescription class attributes and methods
uma_ArtifactDescription_briefOutline: Property = Property(name="briefOutline", type=StringType)
uma_ArtifactDescription_representationOptions: Property = Property(name="representationOptions", type=StringType)
uma_ArtifactDescription_representation: Property = Property(name="representation", type=StringType)
uma_ArtifactDescription_notation: Property = Property(name="notation", type=StringType)
uma_ArtifactDescription.attributes={uma_ArtifactDescription_representationOptions, uma_ArtifactDescription_notation, uma_ArtifactDescription_briefOutline, uma_ArtifactDescription_representation}

# WorkProductDescription class attributes and methods

# uma_WorkProductDescription class attributes and methods
uma_WorkProductDescription_reasonsForNotNeeding: Property = Property(name="reasonsForNotNeeding", type=StringType)
uma_WorkProductDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_WorkProductDescription_impactOfNotHaving: Property = Property(name="impactOfNotHaving", type=StringType)
uma_WorkProductDescription.attributes={uma_WorkProductDescription_purpose, uma_WorkProductDescription_impactOfNotHaving, uma_WorkProductDescription_reasonsForNotNeeding}

# ContentDescription class attributes and methods

# ContentCategory class attributes and methods

# uma_ContentCategory class attributes and methods

# uma_Domain class attributes and methods

# uma_WorkProductType class attributes and methods

# uma_DisciplineGrouping class attributes and methods

# uma_Discipline class attributes and methods

# uma_RoleSet class attributes and methods

# BreakdownElement class attributes and methods

# uma_WorkOrder class attributes and methods
uma_WorkOrder_linkType: Property = Property(name="linkType", type=StringType)
uma_WorkOrder.attributes={uma_WorkOrder_linkType}

# ProcessElement class attributes and methods

# uma_Activity class attributes and methods

# WorkBreakdownElement class attributes and methods

# uma_BreakdownElement class attributes and methods
uma_BreakdownElement_prefix: Property = Property(name="prefix", type=StringType)
uma_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=StringType)
uma_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=StringType)
uma_BreakdownElement_isOptional: Property = Property(name="isOptional", type=StringType)
uma_BreakdownElement.attributes={uma_BreakdownElement_isPlanned, uma_BreakdownElement_prefix, uma_BreakdownElement_isOptional, uma_BreakdownElement_hasMultipleOccurrences}

# uma_Roadmap class attributes and methods

# uma_WorkBreakdownElement class attributes and methods
uma_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=StringType)
uma_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=StringType)
uma_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=StringType)
uma_WorkBreakdownElement.attributes={uma_WorkBreakdownElement_isRepeatable, uma_WorkBreakdownElement_isOngoing, uma_WorkBreakdownElement_isEventDriven}

# uma_PlanningData class attributes and methods
uma_PlanningData_startDate: Property = Property(name="startDate", type=StringType)
uma_PlanningData_finishDate: Property = Property(name="finishDate", type=StringType)
uma_PlanningData_rank: Property = Property(name="rank", type=StringType)
uma_PlanningData.attributes={uma_PlanningData_startDate, uma_PlanningData_finishDate, uma_PlanningData_rank}

# uma_ProcessElement class attributes and methods

# uma_Tool class attributes and methods

# uma_RoleSetGrouping class attributes and methods

# uma_CustomCategory class attributes and methods

# uma_Milestone class attributes and methods

# uma_WorkProductDescriptor class attributes and methods
uma_WorkProductDescriptor_activityEntryState: Property = Property(name="activityEntryState", type=StringType)
uma_WorkProductDescriptor_activityExitState: Property = Property(name="activityExitState", type=StringType)
uma_WorkProductDescriptor.attributes={uma_WorkProductDescriptor_activityExitState, uma_WorkProductDescriptor_activityEntryState}

# Descriptor class attributes and methods

# uma_Descriptor class attributes and methods
uma_Descriptor_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=StringType)
uma_Descriptor.attributes={uma_Descriptor_isSynchronizedWithSource}

# uma_MethodPackage class attributes and methods
uma_MethodPackage_global: Property = Property(name="global", type=StringType)
uma_MethodPackage.attributes={uma_MethodPackage_global}

# Package class attributes and methods

# uma_ContentPackage class attributes and methods

# MethodPackage class attributes and methods

# uma_TaskDescriptor class attributes and methods

# uma_Iteration class attributes and methods

# Activity class attributes and methods

# uma_Phase class attributes and methods

# uma_TeamProfile class attributes and methods

# uma_RoleDescriptor class attributes and methods

# uma_Process class attributes and methods

# uma_CapabilityPattern class attributes and methods

# uma_MethodConfiguration class attributes and methods

# uma_MethodPlugin class attributes and methods
uma_MethodPlugin_userChangeable: Property = Property(name="userChangeable", type=StringType)
uma_MethodPlugin_supporting: Property = Property(name="supporting", type=BooleanType)
uma_MethodPlugin.attributes={uma_MethodPlugin_userChangeable, uma_MethodPlugin_supporting}

# uma_CompositeRole class attributes and methods

# RoleDescriptor class attributes and methods

# uma_DeliveryProcess class attributes and methods

# Process class attributes and methods

# uma_Practice class attributes and methods

# uma_BreakdownElementDescription class attributes and methods
uma_BreakdownElementDescription_usageGuidance: Property = Property(name="usageGuidance", type=StringType)
uma_BreakdownElementDescription.attributes={uma_BreakdownElementDescription_usageGuidance}

# uma_ActivityDescription class attributes and methods
uma_ActivityDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_ActivityDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_ActivityDescription_howtoStaff: Property = Property(name="howtoStaff", type=StringType)
uma_ActivityDescription.attributes={uma_ActivityDescription_alternatives, uma_ActivityDescription_howtoStaff, uma_ActivityDescription_purpose}

# BreakdownElementDescription class attributes and methods

# uma_DeliveryProcessDescription class attributes and methods
uma_DeliveryProcessDescription_scale: Property = Property(name="scale", type=StringType)
uma_DeliveryProcessDescription_projectCharacteristics: Property = Property(name="projectCharacteristics", type=StringType)
uma_DeliveryProcessDescription_riskLevel: Property = Property(name="riskLevel", type=StringType)
uma_DeliveryProcessDescription_estimatingTechnique: Property = Property(name="estimatingTechnique", type=StringType)
uma_DeliveryProcessDescription_projectMemberExpertise: Property = Property(name="projectMemberExpertise", type=StringType)
uma_DeliveryProcessDescription_typeOfContract: Property = Property(name="typeOfContract", type=StringType)
uma_DeliveryProcessDescription.attributes={uma_DeliveryProcessDescription_projectCharacteristics, uma_DeliveryProcessDescription_riskLevel, uma_DeliveryProcessDescription_estimatingTechnique, uma_DeliveryProcessDescription_typeOfContract, uma_DeliveryProcessDescription_projectMemberExpertise, uma_DeliveryProcessDescription_scale}

# ProcessDescription class attributes and methods

# uma_ProcessPlanningTemplate class attributes and methods

# uma_DescriptorDescription class attributes and methods
uma_DescriptorDescription_refinedDescription: Property = Property(name="refinedDescription", type=StringType)
uma_DescriptorDescription.attributes={uma_DescriptorDescription_refinedDescription}

# uma_ProcessComponentDescriptor class attributes and methods

# uma_ProcessComponent class attributes and methods

# ProcessPackage class attributes and methods

# uma_ProcessComponentInterface class attributes and methods

# uma_ProcessPackage class attributes and methods

# uma_Diagram class attributes and methods
uma_Diagram_zoom: Property = Property(name="zoom", type=StringType)
uma_Diagram.attributes={uma_Diagram_zoom}

# uma_ProcessDescription class attributes and methods
uma_ProcessDescription_usageNotes: Property = Property(name="usageNotes", type=StringType)
uma_ProcessDescription_scope: Property = Property(name="scope", type=StringType)
uma_ProcessDescription.attributes={uma_ProcessDescription_usageNotes, uma_ProcessDescription_scope}

# ActivityDescription class attributes and methods

# uma_DiagramElement class attributes and methods
uma_DiagramElement_isVisible: Property = Property(name="isVisible", type=StringType)
uma_DiagramElement.attributes={uma_DiagramElement_isVisible}

# uma_GraphConnector class attributes and methods

# uma_Reference class attributes and methods
uma_Reference_isIndividualRepresentation: Property = Property(name="isIndividualRepresentation", type=StringType)
uma_Reference.attributes={uma_Reference_isIndividualRepresentation}

# uma_Property class attributes and methods
uma_Property_key: Property = Property(name="key", type=StringType)
uma_Property_value: Property = Property(name="value", type=StringType)
uma_Property.attributes={uma_Property_key, uma_Property_value}

# GraphNode class attributes and methods

# uma_DiagramLink class attributes and methods
uma_DiagramLink_zoom: Property = Property(name="zoom", type=StringType)
uma_DiagramLink.attributes={uma_DiagramLink_zoom}

# uma_SemanticModelBridge class attributes and methods
uma_SemanticModelBridge_presentation: Property = Property(name="presentation", type=StringType)
uma_SemanticModelBridge.attributes={uma_SemanticModelBridge_presentation}

# uma_Point class attributes and methods
uma_Point_x: Property = Property(name="x", type=StringType)
uma_Point_y: Property = Property(name="y", type=StringType)
uma_Point.attributes={uma_Point_x, uma_Point_y}

# uma_GraphNode class attributes and methods

# GraphElement class attributes and methods

# uma_Dimension class attributes and methods
uma_Dimension_width: Property = Property(name="width", type=StringType)
uma_Dimension_height: Property = Property(name="height", type=StringType)
uma_Dimension.attributes={uma_Dimension_height, uma_Dimension_width}

# uma_GraphElement class attributes and methods

# DiagramElement class attributes and methods

# uma_GraphEdge class attributes and methods

# uma_LeafElement class attributes and methods

# uma_TextElement class attributes and methods
uma_TextElement_text: Property = Property(name="text", type=StringType)
uma_TextElement.attributes={uma_TextElement_text}

# LeafElement class attributes and methods

# uma_Image class attributes and methods
uma_Image_uri: Property = Property(name="uri", type=StringType)
uma_Image_mimeType: Property = Property(name="mimeType", type=StringType)
uma_Image.attributes={uma_Image_uri, uma_Image_mimeType}

# uma_GraphicPrimitive class attributes and methods

# uma_Polyline class attributes and methods
uma_Polyline_closed: Property = Property(name="closed", type=StringType)
uma_Polyline.attributes={uma_Polyline_closed}

# GraphicPrimitive class attributes and methods

# uma_Ellipse class attributes and methods
uma_Ellipse_radiusX: Property = Property(name="radiusX", type=StringType)
uma_Ellipse_radiusY: Property = Property(name="radiusY", type=StringType)
uma_Ellipse_rotation: Property = Property(name="rotation", type=StringType)
uma_Ellipse_startAngle: Property = Property(name="startAngle", type=StringType)
uma_Ellipse_endAngle: Property = Property(name="endAngle", type=StringType)
uma_Ellipse.attributes={uma_Ellipse_radiusY, uma_Ellipse_startAngle, uma_Ellipse_rotation, uma_Ellipse_endAngle, uma_Ellipse_radiusX}

# uma_SimpleSemanticModelElement class attributes and methods
uma_SimpleSemanticModelElement_typeInfo: Property = Property(name="typeInfo", type=StringType)
uma_SimpleSemanticModelElement.attributes={uma_SimpleSemanticModelElement_typeInfo}

# SemanticModelBridge class attributes and methods

# uma_UMASemanticModelBridge class attributes and methods

# uma_CoreSemanticModelBridge class attributes and methods

# uma_ProcessFamily class attributes and methods

# MethodConfiguration class attributes and methods

# uma_MethodLibrary class attributes and methods

# Relationships
ownedRules0: BinaryAssociation = BinaryAssociation(
    name="ownedRules0",
    ends={
        Property(name="uma_MethodElement", type=uma_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="uma_Constraint", type=uma_MethodElement, multiplicity=Multiplicity(1, 1))
    }
)
methodElementProperty1: BinaryAssociation = BinaryAssociation(
    name="methodElementProperty1",
    ends={
        Property(name="uma_MethodElementProperty", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement2", type=uma_MethodElementProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kind3: BinaryAssociation = BinaryAssociation(
    name="kind3",
    ends={
        Property(name="uma_Kind", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement4", type=uma_Kind, multiplicity=Multiplicity(0, 9999))
    }
)
applicableMetaClassInfo5: BinaryAssociation = BinaryAssociation(
    name="applicableMetaClassInfo5",
    ends={
        Property(name="uma_ApplicableMetaClassInfo", type=uma_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Kind6", type=uma_ApplicableMetaClassInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportingMaterials7: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials7",
    ends={
        Property(name="uma_SupportingMaterial", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
conceptsAndPapers8: BinaryAssociation = BinaryAssociation(
    name="conceptsAndPapers8",
    ends={
        Property(name="uma_Concept", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement9", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
presentation20: BinaryAssociation = BinaryAssociation(
    name="presentation20",
    ends={
        Property(name="uma_ContentDescription", type=uma_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DescribableElement", type=uma_ContentDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections21: BinaryAssociation = BinaryAssociation(
    name="sections21",
    ends={
        Property(name="uma_Section", type=uma_ContentDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentDescription22", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checklists10: BinaryAssociation = BinaryAssociation(
    name="checklists10",
    ends={
        Property(name="uma_Checklist", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement11", type=uma_Checklist, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines12: BinaryAssociation = BinaryAssociation(
    name="guidelines12",
    ends={
        Property(name="uma_Guideline", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement13", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
examples14: BinaryAssociation = BinaryAssociation(
    name="examples14",
    ends={
        Property(name="uma_Example", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement15", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
assets16: BinaryAssociation = BinaryAssociation(
    name="assets16",
    ends={
        Property(name="uma_ReusableAsset", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement17", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
termdefinition18: BinaryAssociation = BinaryAssociation(
    name="termdefinition18",
    ends={
        Property(name="uma_TermDefinition", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement19", type=uma_TermDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
subSections26: BinaryAssociation = BinaryAssociation(
    name="subSections26",
    ends={
        Property(name="uma_Section27", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section25", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor29: BinaryAssociation = BinaryAssociation(
    name="predecessor29",
    ends={
        Property(name="uma_Section30", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section28", type=uma_Section, multiplicity=Multiplicity(0, 1))
    }
)
variabilityBasedOnElement32: BinaryAssociation = BinaryAssociation(
    name="variabilityBasedOnElement32",
    ends={
        Property(name="uma_VariabilityElement", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_VariabilityElement31", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1))
    }
)
copyrightStatement23: BinaryAssociation = BinaryAssociation(
    name="copyrightStatement23",
    ends={
        Property(name="uma_SupportingMaterial24", type=uma_MethodUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodUnit", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 1))
    }
)
containerArtifact34: BinaryAssociation = BinaryAssociation(
    name="containerArtifact34",
    ends={
        Property(name="Artifact", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containedArtifacts", type=uma_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
containedArtifacts36: BinaryAssociation = BinaryAssociation(
    name="containedArtifacts36",
    ends={
        Property(name="Artifact37", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArtifact", type=uma_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fulfills46: BinaryAssociation = BinaryAssociation(
    name="fulfills46",
    ends={
        Property(name="uma_FulfillableElement", type=uma_FulfillableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_FulfillableElement45", type=uma_FulfillableElement, multiplicity=Multiplicity(0, 9999))
    }
)
deliveredWorkProducts47: BinaryAssociation = BinaryAssociation(
    name="deliveredWorkProducts47",
    ends={
        Property(name="uma_WorkProduct48", type=uma_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Deliverable", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
reports38: BinaryAssociation = BinaryAssociation(
    name="reports38",
    ends={
        Property(name="uma_Report", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct", type=uma_Report, multiplicity=Multiplicity(0, 9999))
    }
)
templates39: BinaryAssociation = BinaryAssociation(
    name="templates39",
    ends={
        Property(name="uma_Template", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct40", type=uma_Template, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors41: BinaryAssociation = BinaryAssociation(
    name="toolMentors41",
    ends={
        Property(name="uma_ToolMentor", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct42", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
estimationConsiderations43: BinaryAssociation = BinaryAssociation(
    name="estimationConsiderations43",
    ends={
        Property(name="uma_EstimationConsiderations", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct44", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 9999))
    }
)
performedBy54: BinaryAssociation = BinaryAssociation(
    name="performedBy54",
    ends={
        Property(name="uma_Role", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryInput55: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput55",
    ends={
        Property(name="uma_WorkProduct57", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task56", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
output58: BinaryAssociation = BinaryAssociation(
    name="output58",
    ends={
        Property(name="uma_WorkProduct60", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task59", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
additionallyPerformedBy61: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy61",
    ends={
        Property(name="uma_Role63", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task62", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput64: BinaryAssociation = BinaryAssociation(
    name="optionalInput64",
    ends={
        Property(name="uma_WorkProduct66", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task65", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
steps67: BinaryAssociation = BinaryAssociation(
    name="steps67",
    ends={
        Property(name="uma_Step", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task68", type=uma_Step, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors69: BinaryAssociation = BinaryAssociation(
    name="toolMentors69",
    ends={
        Property(name="uma_ToolMentor71", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task70", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
estimationConsiderations72: BinaryAssociation = BinaryAssociation(
    name="estimationConsiderations72",
    ends={
        Property(name="uma_EstimationConsiderations74", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task73", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 9999))
    }
)
modifies75: BinaryAssociation = BinaryAssociation(
    name="modifies75",
    ends={
        Property(name="uma_WorkProduct77", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role76", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor78: BinaryAssociation = BinaryAssociation(
    name="responsibleFor78",
    ends={
        Property(name="uma_WorkProduct80", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role79", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
precondition49: BinaryAssociation = BinaryAssociation(
    name="precondition49",
    ends={
        Property(name="uma_Constraint50", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postcondition51: BinaryAssociation = BinaryAssociation(
    name="postcondition51",
    ends={
        Property(name="uma_Constraint53", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition52", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles81: BinaryAssociation = BinaryAssociation(
    name="roles81",
    ends={
        Property(name="uma_Role82", type=uma_RoleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSet", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
workProducts83: BinaryAssociation = BinaryAssociation(
    name="workProducts83",
    ends={
        Property(name="uma_WorkProduct84", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
subdomains86: BinaryAssociation = BinaryAssociation(
    name="subdomains86",
    ends={
        Property(name="uma_Domain87", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain85", type=uma_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workProducts88: BinaryAssociation = BinaryAssociation(
    name="workProducts88",
    ends={
        Property(name="uma_WorkProduct89", type=uma_WorkProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductType", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
disciplines90: BinaryAssociation = BinaryAssociation(
    name="disciplines90",
    ends={
        Property(name="uma_Discipline", type=uma_DisciplineGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DisciplineGrouping", type=uma_Discipline, multiplicity=Multiplicity(0, 9999))
    }
)
tasks91: BinaryAssociation = BinaryAssociation(
    name="tasks91",
    ends={
        Property(name="uma_Task93", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline92", type=uma_Task, multiplicity=Multiplicity(0, 9999))
    }
)
linkToPredecessor102: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor102",
    ends={
        Property(name="uma_WorkOrder", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkBreakdownElement", type=uma_WorkOrder, multiplicity=Multiplicity(0, 9999))
    }
)
presentedAfter104: BinaryAssociation = BinaryAssociation(
    name="presentedAfter104",
    ends={
        Property(name="uma_BreakdownElement", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement103", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
presentedBefore106: BinaryAssociation = BinaryAssociation(
    name="presentedBefore106",
    ends={
        Property(name="uma_BreakdownElement107", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement105", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
subdiscipline95: BinaryAssociation = BinaryAssociation(
    name="subdiscipline95",
    ends={
        Property(name="uma_Discipline96", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline94", type=uma_Discipline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceWorkflows97: BinaryAssociation = BinaryAssociation(
    name="referenceWorkflows97",
    ends={
        Property(name="uma_Activity", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline98", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
breakdownElements99: BinaryAssociation = BinaryAssociation(
    name="breakdownElements99",
    ends={
        Property(name="BreakdownElement", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="superActivities", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 9999))
    }
)
roadmaps100: BinaryAssociation = BinaryAssociation(
    name="roadmaps100",
    ends={
        Property(name="uma_Roadmap", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity101", type=uma_Roadmap, multiplicity=Multiplicity(0, 9999))
    }
)
checklists111: BinaryAssociation = BinaryAssociation(
    name="checklists111",
    ends={
        Property(name="uma_Checklist113", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement112", type=uma_Checklist, multiplicity=Multiplicity(0, 9999))
    }
)
concepts114: BinaryAssociation = BinaryAssociation(
    name="concepts114",
    ends={
        Property(name="uma_Concept116", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement115", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
examples117: BinaryAssociation = BinaryAssociation(
    name="examples117",
    ends={
        Property(name="uma_Example119", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement118", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
planningData108: BinaryAssociation = BinaryAssociation(
    name="planningData108",
    ends={
        Property(name="uma_PlanningData", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement109", type=uma_PlanningData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superActivities110: BinaryAssociation = BinaryAssociation(
    name="superActivities110",
    ends={
        Property(name="Activity", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="breakdownElements", type=uma_Activity, multiplicity=Multiplicity(1, 1))
    }
)
reports132: BinaryAssociation = BinaryAssociation(
    name="reports132",
    ends={
        Property(name="uma_Report134", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement133", type=uma_Report, multiplicity=Multiplicity(0, 9999))
    }
)
estimationconsiderations135: BinaryAssociation = BinaryAssociation(
    name="estimationconsiderations135",
    ends={
        Property(name="uma_EstimationConsiderations137", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement136", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 9999))
    }
)
toolmentor138: BinaryAssociation = BinaryAssociation(
    name="toolmentor138",
    ends={
        Property(name="uma_ToolMentor140", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement139", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines120: BinaryAssociation = BinaryAssociation(
    name="guidelines120",
    ends={
        Property(name="uma_Guideline122", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement121", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
reusableAssets123: BinaryAssociation = BinaryAssociation(
    name="reusableAssets123",
    ends={
        Property(name="uma_ReusableAsset125", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement124", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
supportingMaterials126: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials126",
    ends={
        Property(name="uma_SupportingMaterial128", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement127", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
templates129: BinaryAssociation = BinaryAssociation(
    name="templates129",
    ends={
        Property(name="uma_Template131", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement130", type=uma_Template, multiplicity=Multiplicity(0, 9999))
    }
)
pred141: BinaryAssociation = BinaryAssociation(
    name="pred141",
    ends={
        Property(name="uma_WorkOrder142", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkBreakdownElement143", type=uma_WorkOrder, multiplicity=Multiplicity(1, 1))
    }
)
toolMentors144: BinaryAssociation = BinaryAssociation(
    name="toolMentors144",
    ends={
        Property(name="uma_ToolMentor145", type=uma_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Tool", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
roleSets146: BinaryAssociation = BinaryAssociation(
    name="roleSets146",
    ends={
        Property(name="uma_RoleSet147", type=uma_RoleSetGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSetGrouping", type=uma_RoleSet, multiplicity=Multiplicity(0, 9999))
    }
)
categorizedElements148: BinaryAssociation = BinaryAssociation(
    name="categorizedElements148",
    ends={
        Property(name="uma_DescribableElement149", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory", type=uma_DescribableElement, multiplicity=Multiplicity(0, 9999))
    }
)
contentElements157: BinaryAssociation = BinaryAssociation(
    name="contentElements157",
    ends={
        Property(name="uma_ContentElement158", type=uma_ContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentPackage", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredResults159: BinaryAssociation = BinaryAssociation(
    name="requiredResults159",
    ends={
        Property(name="uma_WorkProductDescriptor", type=uma_Milestone, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Milestone", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
WorkProduct160: BinaryAssociation = BinaryAssociation(
    name="WorkProduct160",
    ends={
        Property(name="uma_WorkProduct162", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor161", type=uma_WorkProduct, multiplicity=Multiplicity(0, 1))
    }
)
impactedBy164: BinaryAssociation = BinaryAssociation(
    name="impactedBy164",
    ends={
        Property(name="WorkProductDescriptor", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
impacts166: BinaryAssociation = BinaryAssociation(
    name="impacts166",
    ends={
        Property(name="WorkProductDescriptor167", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="impactedBy", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
deliverableParts169: BinaryAssociation = BinaryAssociation(
    name="deliverableParts169",
    ends={
        Property(name="uma_WorkProductDescriptor170", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor168", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
subCategories150: BinaryAssociation = BinaryAssociation(
    name="subCategories150",
    ends={
        Property(name="uma_ContentCategory", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory151", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
reusedPackages153: BinaryAssociation = BinaryAssociation(
    name="reusedPackages153",
    ends={
        Property(name="uma_MethodPackage", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage152", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999))
    }
)
childPackages155: BinaryAssociation = BinaryAssociation(
    name="childPackages155",
    ends={
        Property(name="uma_MethodPackage156", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage154", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Role177: BinaryAssociation = BinaryAssociation(
    name="Role177",
    ends={
        Property(name="uma_Role179", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor178", type=uma_Role, multiplicity=Multiplicity(0, 1))
    }
)
modifies180: BinaryAssociation = BinaryAssociation(
    name="modifies180",
    ends={
        Property(name="uma_WorkProductDescriptor182", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor181", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor183: BinaryAssociation = BinaryAssociation(
    name="responsibleFor183",
    ends={
        Property(name="uma_WorkProductDescriptor185", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor184", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
Task186: BinaryAssociation = BinaryAssociation(
    name="Task186",
    ends={
        Property(name="uma_Task187", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor", type=uma_Task, multiplicity=Multiplicity(0, 1))
    }
)
additionallyPerformedBy188: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy188",
    ends={
        Property(name="uma_RoleDescriptor190", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor189", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
assistedBy191: BinaryAssociation = BinaryAssociation(
    name="assistedBy191",
    ends={
        Property(name="uma_RoleDescriptor193", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor192", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
externalInput194: BinaryAssociation = BinaryAssociation(
    name="externalInput194",
    ends={
        Property(name="uma_WorkProductDescriptor196", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor195", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryInput197: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput197",
    ends={
        Property(name="uma_WorkProductDescriptor199", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor198", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput200: BinaryAssociation = BinaryAssociation(
    name="optionalInput200",
    ends={
        Property(name="uma_WorkProductDescriptor202", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor201", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
teamRoles171: BinaryAssociation = BinaryAssociation(
    name="teamRoles171",
    ends={
        Property(name="uma_RoleDescriptor", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TeamProfile", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
superTeam173: BinaryAssociation = BinaryAssociation(
    name="superTeam173",
    ends={
        Property(name="TeamProfile", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="subTeam", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1))
    }
)
subTeam175: BinaryAssociation = BinaryAssociation(
    name="subTeam175",
    ends={
        Property(name="TeamProfile176", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="superTeam", type=uma_TeamProfile, multiplicity=Multiplicity(0, 9999))
    }
)
communicationsMaterials216: BinaryAssociation = BinaryAssociation(
    name="communicationsMaterials216",
    ends={
        Property(name="uma_DeliveryProcess217", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999)),
        Property(name="uma_SupportingMaterial218", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1))
    }
)
includesPatterns219: BinaryAssociation = BinaryAssociation(
    name="includesPatterns219",
    ends={
        Property(name="uma_CapabilityPattern", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process", type=uma_CapabilityPattern, multiplicity=Multiplicity(0, 9999))
    }
)
defaultContext220: BinaryAssociation = BinaryAssociation(
    name="defaultContext220",
    ends={
        Property(name="uma_MethodConfiguration", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process221", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
validContext222: BinaryAssociation = BinaryAssociation(
    name="validContext222",
    ends={
        Property(name="uma_MethodConfiguration224", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process223", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
methodPluginSelection225: BinaryAssociation = BinaryAssociation(
    name="methodPluginSelection225",
    ends={
        Property(name="uma_MethodPlugin", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration226", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 9999))
    }
)
methodPackageSelection227: BinaryAssociation = BinaryAssociation(
    name="methodPackageSelection227",
    ends={
        Property(name="uma_MethodPackage229", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration228", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999))
    }
)
processViews230: BinaryAssociation = BinaryAssociation(
    name="processViews230",
    ends={
        Property(name="uma_ContentCategory232", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration231", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
defaultView233: BinaryAssociation = BinaryAssociation(
    name="defaultView233",
    ends={
        Property(name="uma_ContentCategory235", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration234", type=uma_ContentCategory, multiplicity=Multiplicity(1, 1))
    }
)
baseConfigurations237: BinaryAssociation = BinaryAssociation(
    name="baseConfigurations237",
    ends={
        Property(name="uma_MethodConfiguration238", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration236", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
output203: BinaryAssociation = BinaryAssociation(
    name="output203",
    ends={
        Property(name="uma_WorkProductDescriptor205", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor204", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
performedPrimarilyBy206: BinaryAssociation = BinaryAssociation(
    name="performedPrimarilyBy206",
    ends={
        Property(name="uma_RoleDescriptor208", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor207", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
selectedSteps209: BinaryAssociation = BinaryAssociation(
    name="selectedSteps209",
    ends={
        Property(name="uma_Section211", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor210", type=uma_Section, multiplicity=Multiplicity(0, 9999))
    }
)
aggregatedRoles212: BinaryAssociation = BinaryAssociation(
    name="aggregatedRoles212",
    ends={
        Property(name="uma_Role213", type=uma_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CompositeRole", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
educationMaterials214: BinaryAssociation = BinaryAssociation(
    name="educationMaterials214",
    ends={
        Property(name="uma_SupportingMaterial215", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DeliveryProcess", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
basedOnProcesses251: BinaryAssociation = BinaryAssociation(
    name="basedOnProcesses251",
    ends={
        Property(name="uma_Process252", type=uma_ProcessPlanningTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPlanningTemplate", type=uma_Process, multiplicity=Multiplicity(0, 9999))
    }
)
subPractices254: BinaryAssociation = BinaryAssociation(
    name="subPractices254",
    ends={
        Property(name="uma_Practice", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice253", type=uma_Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentReferences255: BinaryAssociation = BinaryAssociation(
    name="contentReferences255",
    ends={
        Property(name="uma_ContentElement257", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice256", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
activityReferences258: BinaryAssociation = BinaryAssociation(
    name="activityReferences258",
    ends={
        Property(name="uma_Activity260", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice259", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
subtractedCategory239: BinaryAssociation = BinaryAssociation(
    name="subtractedCategory239",
    ends={
        Property(name="uma_ContentCategory241", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration240", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
addedCategory242: BinaryAssociation = BinaryAssociation(
    name="addedCategory242",
    ends={
        Property(name="uma_ContentCategory244", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration243", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
methodPackages245: BinaryAssociation = BinaryAssociation(
    name="methodPackages245",
    ends={
        Property(name="uma_MethodPackage247", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin246", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bases249: BinaryAssociation = BinaryAssociation(
    name="bases249",
    ends={
        Property(name="uma_MethodPlugin250", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin248", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
_processComponent261: BinaryAssociation = BinaryAssociation(
    name="_processComponent261",
    ends={
        Property(name="uma_ProcessComponent", type=uma_ProcessComponentDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentDescriptor", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
interfaces262: BinaryAssociation = BinaryAssociation(
    name="interfaces262",
    ends={
        Property(name="uma_ProcessComponentInterface", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent263", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 9999))
    }
)
process264: BinaryAssociation = BinaryAssociation(
    name="process264",
    ends={
        Property(name="uma_Process266", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent265", type=uma_Process, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
processElements267: BinaryAssociation = BinaryAssociation(
    name="processElements267",
    ends={
        Property(name="uma_ProcessElement", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage", type=uma_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams268: BinaryAssociation = BinaryAssociation(
    name="diagrams268",
    ends={
        Property(name="uma_Diagram", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage269", type=uma_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contained276: BinaryAssociation = BinaryAssociation(
    name="contained276",
    ends={
        Property(name="DiagramElement", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uma_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position277: BinaryAssociation = BinaryAssociation(
    name="position277",
    ends={
        Property(name="uma_Point278", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphElement", type=uma_Point, multiplicity=Multiplicity(1, 1))
    }
)
link279: BinaryAssociation = BinaryAssociation(
    name="link279",
    ends={
        Property(name="DiagramLink280", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anchorage281: BinaryAssociation = BinaryAssociation(
    name="anchorage281",
    ends={
        Property(name="GraphConnector", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement282", type=uma_GraphConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semanticModel283: BinaryAssociation = BinaryAssociation(
    name="semanticModel283",
    ends={
        Property(name="SemanticModelBridge285", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement284", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container286: BinaryAssociation = BinaryAssociation(
    name="container286",
    ends={
        Property(name="GraphElement", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contained", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
reference287: BinaryAssociation = BinaryAssociation(
    name="reference287",
    ends={
        Property(name="Reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referenced", type=uma_Reference, multiplicity=Multiplicity(0, 9999))
    }
)
property288: BinaryAssociation = BinaryAssociation(
    name="property288",
    ends={
        Property(name="uma_Property", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramElement", type=uma_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramLink270: BinaryAssociation = BinaryAssociation(
    name="diagramLink270",
    ends={
        Property(name="DiagramLink", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999))
    }
)
namespace271: BinaryAssociation = BinaryAssociation(
    name="namespace271",
    ends={
        Property(name="SemanticModelBridge", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram272", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewpoint273: BinaryAssociation = BinaryAssociation(
    name="viewpoint273",
    ends={
        Property(name="uma_Point", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Diagram274", type=uma_Point, multiplicity=Multiplicity(1, 1))
    }
)
size275: BinaryAssociation = BinaryAssociation(
    name="size275",
    ends={
        Property(name="uma_Dimension", type=uma_GraphNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphNode", type=uma_Dimension, multiplicity=Multiplicity(1, 1))
    }
)
graphEdge296: BinaryAssociation = BinaryAssociation(
    name="graphEdge296",
    ends={
        Property(name="GraphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchor", type=uma_GraphEdge, multiplicity=Multiplicity(0, 9999))
    }
)
graphElement297: BinaryAssociation = BinaryAssociation(
    name="graphElement297",
    ends={
        Property(name="GraphElement298", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchorage", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
waypoints299: BinaryAssociation = BinaryAssociation(
    name="waypoints299",
    ends={
        Property(name="uma_Point300", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphEdge", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
anchor301: BinaryAssociation = BinaryAssociation(
    name="anchor301",
    ends={
        Property(name="GraphConnector302", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(2, 2))
    }
)
diagram303: BinaryAssociation = BinaryAssociation(
    name="diagram303",
    ends={
        Property(name="Diagram304", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uma_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
graphElement305: BinaryAssociation = BinaryAssociation(
    name="graphElement305",
    ends={
        Property(name="GraphElement306", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticModel", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
referenced289: BinaryAssociation = BinaryAssociation(
    name="referenced289",
    ends={
        Property(name="DiagramElement290", type=uma_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
viewport291: BinaryAssociation = BinaryAssociation(
    name="viewport291",
    ends={
        Property(name="uma_Point292", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramLink", type=uma_Point, multiplicity=Multiplicity(1, 1))
    }
)
diagram293: BinaryAssociation = BinaryAssociation(
    name="diagram293",
    ends={
        Property(name="Diagram", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="diagramLink", type=uma_Diagram, multiplicity=Multiplicity(1, 1))
    }
)
graphElement294: BinaryAssociation = BinaryAssociation(
    name="graphElement294",
    ends={
        Property(name="GraphElement295", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
element315: BinaryAssociation = BinaryAssociation(
    name="element315",
    ends={
        Property(name="uma_Element", type=uma_CoreSemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CoreSemanticModelBridge", type=uma_Element, multiplicity=Multiplicity(1, 1))
    }
)
waypoints316: BinaryAssociation = BinaryAssociation(
    name="waypoints316",
    ends={
        Property(name="uma_Point317", type=uma_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Polyline", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
center318: BinaryAssociation = BinaryAssociation(
    name="center318",
    ends={
        Property(name="uma_Point319", type=uma_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Ellipse", type=uma_Point, multiplicity=Multiplicity(1, 1))
    }
)
interfaceSpecifications307: BinaryAssociation = BinaryAssociation(
    name="interfaceSpecifications307",
    ends={
        Property(name="uma_TaskDescriptor309", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface308", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceIO310: BinaryAssociation = BinaryAssociation(
    name="interfaceIO310",
    ends={
        Property(name="uma_WorkProductDescriptor312", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface311", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element313: BinaryAssociation = BinaryAssociation(
    name="element313",
    ends={
        Property(name="uma_MethodElement314", type=uma_UMASemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_UMASemanticModelBridge", type=uma_MethodElement, multiplicity=Multiplicity(1, 1))
    }
)
deliveryProcesses320: BinaryAssociation = BinaryAssociation(
    name="deliveryProcesses320",
    ends={
        Property(name="uma_DeliveryProcess321", type=uma_ProcessFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessFamily", type=uma_DeliveryProcess, multiplicity=Multiplicity(0, 9999))
    }
)
methodPlugins322: BinaryAssociation = BinaryAssociation(
    name="methodPlugins322",
    ends={
        Property(name="uma_MethodPlugin323", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predefinedConfigurations324: BinaryAssociation = BinaryAssociation(
    name="predefinedConfigurations324",
    ends={
        Property(name="uma_MethodConfiguration326", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary325", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uma_NamedElement_Element = Generalization(general=Element, specific=uma_NamedElement)
gen_uma_Package_Namespace = Generalization(general=Namespace, specific=uma_Package)
gen_uma_Package_PackageableElement = Generalization(general=PackageableElement, specific=uma_Package)
gen_uma_Namespace_NamedElement = Generalization(general=NamedElement, specific=uma_Namespace)
gen_uma_Constraint_MethodElement = Generalization(general=MethodElement, specific=uma_Constraint)
gen_uma_Classifier_Type = Generalization(general=Type, specific=uma_Classifier)
gen_uma_Type_PackageableElement = Generalization(general=PackageableElement, specific=uma_Type)
gen_uma_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uma_PackageableElement)
gen_uma_MethodElementProperty_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElementProperty)
gen_uma_Kind_ContentElement = Generalization(general=ContentElement, specific=uma_Kind)
gen_uma_ContentElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ContentElement)
gen_uma_ContentElement_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_ContentElement)
gen_uma_MethodElement_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElement)
gen_uma_ContentDescription_MethodUnit = Generalization(general=MethodUnit, specific=uma_ContentDescription)
gen_uma_MethodUnit_MethodElement = Generalization(general=MethodElement, specific=uma_MethodUnit)
gen_uma_DescribableElement_MethodElement = Generalization(general=MethodElement, specific=uma_DescribableElement)
gen_uma_DescribableElement_Classifier = Generalization(general=Classifier, specific=uma_DescribableElement)
gen_uma_VariabilityElement_MethodElement = Generalization(general=MethodElement, specific=uma_VariabilityElement)
gen_uma_SupportingMaterial_Guidance = Generalization(general=Guidance, specific=uma_SupportingMaterial)
gen_uma_Guidance_ContentElement = Generalization(general=ContentElement, specific=uma_Guidance)
gen_uma_Section_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_Section)
gen_uma_Checklist_Guidance = Generalization(general=Guidance, specific=uma_Checklist)
gen_uma_Guideline_Guidance = Generalization(general=Guidance, specific=uma_Guideline)
gen_uma_Example_Guidance = Generalization(general=Guidance, specific=uma_Example)
gen_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=uma_ReusableAsset)
gen_uma_TermDefinition_Guidance = Generalization(general=Guidance, specific=uma_TermDefinition)
gen_uma_ApplicableMetaClassInfo_Classifier = Generalization(general=Classifier, specific=uma_ApplicableMetaClassInfo)
gen_uma_Artifact_WorkProduct = Generalization(general=WorkProduct, specific=uma_Artifact)
gen_uma_WorkProduct_ContentElement = Generalization(general=ContentElement, specific=uma_WorkProduct)
gen_uma_WorkProduct_FulfillableElement = Generalization(general=FulfillableElement, specific=uma_WorkProduct)
gen_uma_Concept_Guidance = Generalization(general=Guidance, specific=uma_Concept)
gen_uma_Report_Guidance = Generalization(general=Guidance, specific=uma_Report)
gen_uma_Template_Guidance = Generalization(general=Guidance, specific=uma_Template)
gen_uma_ToolMentor_Guidance = Generalization(general=Guidance, specific=uma_ToolMentor)
gen_uma_EstimationConsiderations_Guidance = Generalization(general=Guidance, specific=uma_EstimationConsiderations)
gen_uma_Deliverable_WorkProduct = Generalization(general=WorkProduct, specific=uma_Deliverable)
gen_uma_Outcome_WorkProduct = Generalization(general=WorkProduct, specific=uma_Outcome)
gen_uma_Step_Section = Generalization(general=Section, specific=uma_Step)
gen_uma_Step_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Step)
gen_uma_WorkDefinition_MethodElement = Generalization(general=MethodElement, specific=uma_WorkDefinition)
gen_uma_FulfillableElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_FulfillableElement)
gen_uma_Role_ContentElement = Generalization(general=ContentElement, specific=uma_Role)
gen_uma_Role_FulfillableElement = Generalization(general=FulfillableElement, specific=uma_Role)
gen_uma_Whitepaper_Concept = Generalization(general=Concept, specific=uma_Whitepaper)
gen_uma_Task_ContentElement = Generalization(general=ContentElement, specific=uma_Task)
gen_uma_Task_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Task)
gen_uma_DeliverableDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_DeliverableDescription)
gen_uma_RoleDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_RoleDescription)
gen_uma_TaskDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_TaskDescription)
gen_uma_GuidanceDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_GuidanceDescription)
gen_uma_ArtifactDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_ArtifactDescription)
gen_uma_WorkProductDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_WorkProductDescription)
gen_uma_RoleSet_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSet)
gen_uma_ContentCategory_ContentElement = Generalization(general=ContentElement, specific=uma_ContentCategory)
gen_uma_Domain_ContentCategory = Generalization(general=ContentCategory, specific=uma_Domain)
gen_uma_WorkProductType_ContentCategory = Generalization(general=ContentCategory, specific=uma_WorkProductType)
gen_uma_DisciplineGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_DisciplineGrouping)
gen_uma_Discipline_ContentCategory = Generalization(general=ContentCategory, specific=uma_Discipline)
gen_uma_PracticeDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_PracticeDescription)
gen_uma_WorkBreakdownElement_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_WorkBreakdownElement)
gen_uma_BreakdownElement_ProcessElement = Generalization(general=ProcessElement, specific=uma_BreakdownElement)
gen_uma_Activity_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Activity)
gen_uma_Activity_FulfillableElement = Generalization(general=FulfillableElement, specific=uma_Activity)
gen_uma_Activity_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_Activity)
gen_uma_Activity_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Activity)
gen_uma_ProcessElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ProcessElement)
gen_uma_PlanningData_ProcessElement = Generalization(general=ProcessElement, specific=uma_PlanningData)
gen_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=uma_Roadmap)
gen_uma_Tool_ContentCategory = Generalization(general=ContentCategory, specific=uma_Tool)
gen_uma_RoleSetGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSetGrouping)
gen_uma_CustomCategory_ContentCategory = Generalization(general=ContentCategory, specific=uma_CustomCategory)
gen_uma_WorkOrder_ProcessElement = Generalization(general=ProcessElement, specific=uma_WorkOrder)
gen_uma_Milestone_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Milestone)
gen_uma_WorkProductDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_WorkProductDescriptor)
gen_uma_Descriptor_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_Descriptor)
gen_uma_MethodPackage_MethodElement = Generalization(general=MethodElement, specific=uma_MethodPackage)
gen_uma_MethodPackage_Package = Generalization(general=Package, specific=uma_MethodPackage)
gen_uma_ContentPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ContentPackage)
gen_uma_RoleDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_RoleDescriptor)
gen_uma_TaskDescriptor_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_TaskDescriptor)
gen_uma_TaskDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_TaskDescriptor)
gen_uma_Iteration_Activity = Generalization(general=Activity, specific=uma_Iteration)
gen_uma_Phase_Activity = Generalization(general=Activity, specific=uma_Phase)
gen_uma_TeamProfile_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_TeamProfile)
gen_uma_Process_Activity = Generalization(general=Activity, specific=uma_Process)
gen_uma_CapabilityPattern_Process = Generalization(general=Process, specific=uma_CapabilityPattern)
gen_uma_MethodConfiguration_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodConfiguration)
gen_uma_CompositeRole_RoleDescriptor = Generalization(general=RoleDescriptor, specific=uma_CompositeRole)
gen_uma_DeliveryProcess_Process = Generalization(general=Process, specific=uma_DeliveryProcess)
gen_uma_Practice_Guidance = Generalization(general=Guidance, specific=uma_Practice)
gen_uma_BreakdownElementDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_BreakdownElementDescription)
gen_uma_ActivityDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_ActivityDescription)
gen_uma_DeliveryProcessDescription_ProcessDescription = Generalization(general=ProcessDescription, specific=uma_DeliveryProcessDescription)
gen_uma_MethodPlugin_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodPlugin)
gen_uma_MethodPlugin_Package = Generalization(general=Package, specific=uma_MethodPlugin)
gen_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=uma_ProcessPlanningTemplate)
gen_uma_DescriptorDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_DescriptorDescription)
gen_uma_ProcessComponentDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_ProcessComponentDescriptor)
gen_uma_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=uma_ProcessComponent)
gen_uma_ProcessComponent_MethodUnit = Generalization(general=MethodUnit, specific=uma_ProcessComponent)
gen_uma_ProcessPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ProcessPackage)
gen_uma_ProcessDescription_ActivityDescription = Generalization(general=ActivityDescription, specific=uma_ProcessDescription)
gen_uma_DiagramElement_MethodElement = Generalization(general=MethodElement, specific=uma_DiagramElement)
gen_uma_Reference_DiagramElement = Generalization(general=DiagramElement, specific=uma_Reference)
gen_uma_Diagram_GraphNode = Generalization(general=GraphNode, specific=uma_Diagram)
gen_uma_GraphNode_GraphElement = Generalization(general=GraphElement, specific=uma_GraphNode)
gen_uma_GraphElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_GraphElement)
gen_uma_GraphConnector_GraphElement = Generalization(general=GraphElement, specific=uma_GraphConnector)
gen_uma_GraphEdge_GraphElement = Generalization(general=GraphElement, specific=uma_GraphEdge)
gen_uma_SemanticModelBridge_DiagramElement = Generalization(general=DiagramElement, specific=uma_SemanticModelBridge)
gen_uma_ProcessComponentInterface_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_ProcessComponentInterface)
gen_uma_Property_DiagramElement = Generalization(general=DiagramElement, specific=uma_Property)
gen_uma_DiagramLink_DiagramElement = Generalization(general=DiagramElement, specific=uma_DiagramLink)
gen_uma_LeafElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_LeafElement)
gen_uma_TextElement_LeafElement = Generalization(general=LeafElement, specific=uma_TextElement)
gen_uma_Image_LeafElement = Generalization(general=LeafElement, specific=uma_Image)
gen_uma_GraphicPrimitive_LeafElement = Generalization(general=LeafElement, specific=uma_GraphicPrimitive)
gen_uma_Polyline_GraphicPrimitive = Generalization(general=GraphicPrimitive, specific=uma_Polyline)
gen_uma_Ellipse_GraphicPrimitive = Generalization(general=GraphicPrimitive, specific=uma_Ellipse)
gen_uma_SimpleSemanticModelElement_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_SimpleSemanticModelElement)
gen_uma_UMASemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_UMASemanticModelBridge)
gen_uma_CoreSemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_CoreSemanticModelBridge)
gen_uma_ProcessFamily_MethodConfiguration = Generalization(general=MethodConfiguration, specific=uma_ProcessFamily)
gen_uma_MethodLibrary_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodLibrary)
gen_uma_MethodLibrary_Package = Generalization(general=Package, specific=uma_MethodLibrary)

# Domain Model
domain_model = DomainModel(
    name="uma",
    types={uma_NamedElement, Element, uma_Element, uma_Package, Namespace, uma_Namespace, uma_Constraint, MethodElement, uma_Classifier, Type, uma_Type, PackageableElement, uma_PackageableElement, NamedElement, uma_MethodElementProperty, uma_Kind, ContentElement, uma_ApplicableMetaClassInfo, uma_ContentElement, DescribableElement, VariabilityElement, uma_SupportingMaterial, uma_Concept, uma_MethodElement, uma_ContentDescription, MethodUnit, uma_Section, uma_MethodUnit, uma_Checklist, uma_Guideline, uma_Example, uma_ReusableAsset, uma_TermDefinition, uma_DescribableElement, Classifier, uma_VariabilityElement, Guidance, uma_Guidance, uma_Artifact, WorkProduct, uma_WorkProduct, FulfillableElement, uma_Deliverable, uma_Outcome, uma_Step, Section, WorkDefinition, uma_WorkDefinition, uma_Report, uma_Template, uma_ToolMentor, uma_EstimationConsiderations, uma_FulfillableElement, uma_Whitepaper, Concept, uma_Task, uma_Role, uma_DeliverableDescription, uma_RoleDescription, uma_TaskDescription, uma_GuidanceDescription, uma_PracticeDescription, uma_ArtifactDescription, WorkProductDescription, uma_WorkProductDescription, ContentDescription, ContentCategory, uma_ContentCategory, uma_Domain, uma_WorkProductType, uma_DisciplineGrouping, uma_Discipline, uma_RoleSet, BreakdownElement, uma_WorkOrder, ProcessElement, uma_Activity, WorkBreakdownElement, uma_BreakdownElement, uma_Roadmap, uma_WorkBreakdownElement, uma_PlanningData, uma_ProcessElement, uma_Tool, uma_RoleSetGrouping, uma_CustomCategory, uma_Milestone, uma_WorkProductDescriptor, Descriptor, uma_Descriptor, uma_MethodPackage, Package, uma_ContentPackage, MethodPackage, uma_TaskDescriptor, uma_Iteration, Activity, uma_Phase, uma_TeamProfile, uma_RoleDescriptor, uma_Process, uma_CapabilityPattern, uma_MethodConfiguration, uma_MethodPlugin, uma_CompositeRole, RoleDescriptor, uma_DeliveryProcess, Process, uma_Practice, uma_BreakdownElementDescription, uma_ActivityDescription, BreakdownElementDescription, uma_DeliveryProcessDescription, ProcessDescription, uma_ProcessPlanningTemplate, uma_DescriptorDescription, uma_ProcessComponentDescriptor, uma_ProcessComponent, ProcessPackage, uma_ProcessComponentInterface, uma_ProcessPackage, uma_Diagram, uma_ProcessDescription, ActivityDescription, uma_DiagramElement, uma_GraphConnector, uma_Reference, uma_Property, GraphNode, uma_DiagramLink, uma_SemanticModelBridge, uma_Point, uma_GraphNode, GraphElement, uma_Dimension, uma_GraphElement, DiagramElement, uma_GraphEdge, uma_LeafElement, uma_TextElement, LeafElement, uma_Image, uma_GraphicPrimitive, uma_Polyline, GraphicPrimitive, uma_Ellipse, uma_SimpleSemanticModelElement, SemanticModelBridge, uma_UMASemanticModelBridge, uma_CoreSemanticModelBridge, uma_ProcessFamily, MethodConfiguration, uma_MethodLibrary, VariabilityType, WorkOrderType},
    associations={ownedRules0, methodElementProperty1, kind3, applicableMetaClassInfo5, supportingMaterials7, conceptsAndPapers8, presentation20, sections21, checklists10, guidelines12, examples14, assets16, termdefinition18, subSections26, predecessor29, variabilityBasedOnElement32, copyrightStatement23, containerArtifact34, containedArtifacts36, fulfills46, deliveredWorkProducts47, reports38, templates39, toolMentors41, estimationConsiderations43, performedBy54, mandatoryInput55, output58, additionallyPerformedBy61, optionalInput64, steps67, toolMentors69, estimationConsiderations72, modifies75, responsibleFor78, precondition49, postcondition51, roles81, workProducts83, subdomains86, workProducts88, disciplines90, tasks91, linkToPredecessor102, presentedAfter104, presentedBefore106, subdiscipline95, referenceWorkflows97, breakdownElements99, roadmaps100, checklists111, concepts114, examples117, planningData108, superActivities110, reports132, estimationconsiderations135, toolmentor138, guidelines120, reusableAssets123, supportingMaterials126, templates129, pred141, toolMentors144, roleSets146, categorizedElements148, contentElements157, requiredResults159, WorkProduct160, impactedBy164, impacts166, deliverableParts169, subCategories150, reusedPackages153, childPackages155, Role177, modifies180, responsibleFor183, Task186, additionallyPerformedBy188, assistedBy191, externalInput194, mandatoryInput197, optionalInput200, teamRoles171, superTeam173, subTeam175, communicationsMaterials216, includesPatterns219, defaultContext220, validContext222, methodPluginSelection225, methodPackageSelection227, processViews230, defaultView233, baseConfigurations237, output203, performedPrimarilyBy206, selectedSteps209, aggregatedRoles212, educationMaterials214, basedOnProcesses251, subPractices254, contentReferences255, activityReferences258, subtractedCategory239, addedCategory242, methodPackages245, bases249, _processComponent261, interfaces262, process264, processElements267, diagrams268, contained276, position277, link279, anchorage281, semanticModel283, container286, reference287, property288, diagramLink270, namespace271, viewpoint273, size275, graphEdge296, graphElement297, waypoints299, anchor301, diagram303, graphElement305, referenced289, viewport291, diagram293, graphElement294, element315, waypoints316, center318, interfaceSpecifications307, interfaceIO310, element313, deliveryProcesses320, methodPlugins322, predefinedConfigurations324},
    generalizations={gen_uma_NamedElement_Element, gen_uma_Package_Namespace, gen_uma_Package_PackageableElement, gen_uma_Namespace_NamedElement, gen_uma_Constraint_MethodElement, gen_uma_Classifier_Type, gen_uma_Type_PackageableElement, gen_uma_PackageableElement_NamedElement, gen_uma_MethodElementProperty_PackageableElement, gen_uma_Kind_ContentElement, gen_uma_ContentElement_DescribableElement, gen_uma_ContentElement_VariabilityElement, gen_uma_MethodElement_PackageableElement, gen_uma_ContentDescription_MethodUnit, gen_uma_MethodUnit_MethodElement, gen_uma_DescribableElement_MethodElement, gen_uma_DescribableElement_Classifier, gen_uma_VariabilityElement_MethodElement, gen_uma_SupportingMaterial_Guidance, gen_uma_Guidance_ContentElement, gen_uma_Section_VariabilityElement, gen_uma_Checklist_Guidance, gen_uma_Guideline_Guidance, gen_uma_Example_Guidance, gen_uma_ReusableAsset_Guidance, gen_uma_TermDefinition_Guidance, gen_uma_ApplicableMetaClassInfo_Classifier, gen_uma_Artifact_WorkProduct, gen_uma_WorkProduct_ContentElement, gen_uma_WorkProduct_FulfillableElement, gen_uma_Concept_Guidance, gen_uma_Report_Guidance, gen_uma_Template_Guidance, gen_uma_ToolMentor_Guidance, gen_uma_EstimationConsiderations_Guidance, gen_uma_Deliverable_WorkProduct, gen_uma_Outcome_WorkProduct, gen_uma_Step_Section, gen_uma_Step_WorkDefinition, gen_uma_WorkDefinition_MethodElement, gen_uma_FulfillableElement_DescribableElement, gen_uma_Role_ContentElement, gen_uma_Role_FulfillableElement, gen_uma_Whitepaper_Concept, gen_uma_Task_ContentElement, gen_uma_Task_WorkDefinition, gen_uma_DeliverableDescription_WorkProductDescription, gen_uma_RoleDescription_ContentDescription, gen_uma_TaskDescription_ContentDescription, gen_uma_GuidanceDescription_ContentDescription, gen_uma_ArtifactDescription_WorkProductDescription, gen_uma_WorkProductDescription_ContentDescription, gen_uma_RoleSet_ContentCategory, gen_uma_ContentCategory_ContentElement, gen_uma_Domain_ContentCategory, gen_uma_WorkProductType_ContentCategory, gen_uma_DisciplineGrouping_ContentCategory, gen_uma_Discipline_ContentCategory, gen_uma_PracticeDescription_ContentDescription, gen_uma_WorkBreakdownElement_BreakdownElement, gen_uma_BreakdownElement_ProcessElement, gen_uma_Activity_WorkBreakdownElement, gen_uma_Activity_FulfillableElement, gen_uma_Activity_VariabilityElement, gen_uma_Activity_WorkDefinition, gen_uma_ProcessElement_DescribableElement, gen_uma_PlanningData_ProcessElement, gen_uma_Roadmap_Guidance, gen_uma_Tool_ContentCategory, gen_uma_RoleSetGrouping_ContentCategory, gen_uma_CustomCategory_ContentCategory, gen_uma_WorkOrder_ProcessElement, gen_uma_Milestone_WorkBreakdownElement, gen_uma_WorkProductDescriptor_Descriptor, gen_uma_Descriptor_BreakdownElement, gen_uma_MethodPackage_MethodElement, gen_uma_MethodPackage_Package, gen_uma_ContentPackage_MethodPackage, gen_uma_RoleDescriptor_Descriptor, gen_uma_TaskDescriptor_WorkBreakdownElement, gen_uma_TaskDescriptor_Descriptor, gen_uma_Iteration_Activity, gen_uma_Phase_Activity, gen_uma_TeamProfile_BreakdownElement, gen_uma_Process_Activity, gen_uma_CapabilityPattern_Process, gen_uma_MethodConfiguration_MethodUnit, gen_uma_CompositeRole_RoleDescriptor, gen_uma_DeliveryProcess_Process, gen_uma_Practice_Guidance, gen_uma_BreakdownElementDescription_ContentDescription, gen_uma_ActivityDescription_BreakdownElementDescription, gen_uma_DeliveryProcessDescription_ProcessDescription, gen_uma_MethodPlugin_MethodUnit, gen_uma_MethodPlugin_Package, gen_uma_ProcessPlanningTemplate_Process, gen_uma_DescriptorDescription_BreakdownElementDescription, gen_uma_ProcessComponentDescriptor_Descriptor, gen_uma_ProcessComponent_ProcessPackage, gen_uma_ProcessComponent_MethodUnit, gen_uma_ProcessPackage_MethodPackage, gen_uma_ProcessDescription_ActivityDescription, gen_uma_DiagramElement_MethodElement, gen_uma_Reference_DiagramElement, gen_uma_Diagram_GraphNode, gen_uma_GraphNode_GraphElement, gen_uma_GraphElement_DiagramElement, gen_uma_GraphConnector_GraphElement, gen_uma_GraphEdge_GraphElement, gen_uma_SemanticModelBridge_DiagramElement, gen_uma_ProcessComponentInterface_BreakdownElement, gen_uma_Property_DiagramElement, gen_uma_DiagramLink_DiagramElement, gen_uma_LeafElement_DiagramElement, gen_uma_TextElement_LeafElement, gen_uma_Image_LeafElement, gen_uma_GraphicPrimitive_LeafElement, gen_uma_Polyline_GraphicPrimitive, gen_uma_Ellipse_GraphicPrimitive, gen_uma_SimpleSemanticModelElement_SemanticModelBridge, gen_uma_UMASemanticModelBridge_SemanticModelBridge, gen_uma_CoreSemanticModelBridge_SemanticModelBridge, gen_uma_ProcessFamily_MethodConfiguration, gen_uma_MethodLibrary_MethodUnit, gen_uma_MethodLibrary_Package},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)