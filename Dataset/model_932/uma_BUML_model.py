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
WorkOrderType: Enumeration = Enumeration(
    name="WorkOrderType",
    literals={
            EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish"),
			EnumerationLiteral(name="finishToStart")
    }
)

VariabilityType: Enumeration = Enumeration(
    name="VariabilityType",
    literals={
            EnumerationLiteral(name="na"),
			EnumerationLiteral(name="contributes"),
			EnumerationLiteral(name="extends"),
			EnumerationLiteral(name="replaces")
    }
)

# Classes
uma_Classifier = Class(name="uma::Classifier", is_abstract=True)
Type = Class(name="Type")
uma_Type = Class(name="uma::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
uma_Element = Class(name="uma::Element", is_abstract=True)
uma_NamedElement = Class(name="uma::NamedElement", is_abstract=True)
Element = Class(name="Element")
uma_PackageableElement = Class(name="uma::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
uma_Package = Class(name="uma::Package")
Namespace = Class(name="Namespace")
uma_MethodElement = Class(name="uma::MethodElement", is_abstract=True)
uma_Constraint = Class(name="uma::Constraint")
MethodElement = Class(name="MethodElement")
uma_ContentElement = Class(name="uma::ContentElement", is_abstract=True)
DescribableElement = Class(name="DescribableElement")
VariabilityElement = Class(name="VariabilityElement")
uma_SupportingMaterial = Class(name="uma::SupportingMaterial")
uma_Concept = Class(name="uma::Concept")
uma_Checklist = Class(name="uma::Checklist")
uma_Guideline = Class(name="uma::Guideline")
uma_Example = Class(name="uma::Example")
uma_ReusableAsset = Class(name="uma::ReusableAsset")
uma_DescribableElement = Class(name="uma::DescribableElement", is_abstract=True)
Classifier = Class(name="Classifier")
uma_Namespace = Class(name="uma::Namespace", is_abstract=True)
MethodUnit = Class(name="MethodUnit")
uma_Section = Class(name="uma::Section")
uma_Role = Class(name="uma::Role")
ContentElement = Class(name="ContentElement")
uma_WorkProduct = Class(name="uma::WorkProduct", is_abstract=True)
uma_Estimate = Class(name="uma::Estimate")
uma_Report = Class(name="uma::Report")
uma_ContentDescription = Class(name="uma::ContentDescription")
uma_Task = Class(name="uma::Task")
WorkDefinition = Class(name="WorkDefinition")
uma_Step = Class(name="uma::Step")
uma_WorkDefinition = Class(name="uma::WorkDefinition", is_abstract=True)
Section = Class(name="Section")
uma_Guidance = Class(name="uma::Guidance", is_abstract=True)
uma_Artifact = Class(name="uma::Artifact")
WorkProduct = Class(name="WorkProduct")
uma_Deliverable = Class(name="uma::Deliverable")
uma_Template = Class(name="uma::Template")
uma_ToolMentor = Class(name="uma::ToolMentor")
uma_Outcome = Class(name="uma::Outcome")
uma_MethodPackage = Class(name="uma::MethodPackage", is_abstract=True)
Package = Class(name="Package")
uma_ContentPackage = Class(name="uma::ContentPackage")
MethodPackage = Class(name="MethodPackage")
uma_ArtifactDescription = Class(name="uma::ArtifactDescription")
WorkProductDescription = Class(name="WorkProductDescription")
uma_WorkProductDescription = Class(name="uma::WorkProductDescription")
ContentDescription = Class(name="ContentDescription")
uma_DeliverableDescription = Class(name="uma::DeliverableDescription")
uma_TaskDescription = Class(name="uma::TaskDescription")
uma_GuidanceDescription = Class(name="uma::GuidanceDescription")
uma_PracticeDescription = Class(name="uma::PracticeDescription")
uma_Point = Class(name="uma::Point")
uma_GraphElement = Class(name="uma::GraphElement", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
uma_DiagramElement = Class(name="uma::DiagramElement", is_abstract=True)
uma_DiagramLink = Class(name="uma::DiagramLink")
uma_RoleDescription = Class(name="uma::RoleDescription")
uma_Reference = Class(name="uma::Reference")
uma_Property = Class(name="uma::Property")
uma_Diagram = Class(name="uma::Diagram")
GraphElement = Class(name="GraphElement")
uma_GraphEdge = Class(name="uma::GraphEdge")
uma_Dimension = Class(name="uma::Dimension")
uma_GraphConnector = Class(name="uma::GraphConnector")
uma_SemanticModelBridge = Class(name="uma::SemanticModelBridge", is_abstract=True)
GraphNode = Class(name="GraphNode")
uma_GraphNode = Class(name="uma::GraphNode")
uma_SimpleSemanticModelElement = Class(name="uma::SimpleSemanticModelElement")
SemanticModelBridge = Class(name="SemanticModelBridge")
uma_UMASemanticModelBridge = Class(name="uma::UMASemanticModelBridge")
uma_CoreSemanticModelBridge = Class(name="uma::CoreSemanticModelBridge")
uma_LeafElement = Class(name="uma::LeafElement", is_abstract=True)
uma_TextElement = Class(name="uma::TextElement")
LeafElement = Class(name="LeafElement")
uma_Image = Class(name="uma::Image")
uma_GraphicPrimitive = Class(name="uma::GraphicPrimitive", is_abstract=True)
uma_Polyline = Class(name="uma::Polyline")
GraphicPrimitive = Class(name="GraphicPrimitive")
uma_Ellipse = Class(name="uma::Ellipse")
uma_Activity = Class(name="uma::Activity")
WorkBreakdownElement = Class(name="WorkBreakdownElement")
uma_BreakdownElement = Class(name="uma::BreakdownElement", is_abstract=True)
uma_Roadmap = Class(name="uma::Roadmap")
uma_WorkBreakdownElement = Class(name="uma::WorkBreakdownElement", is_abstract=True)
BreakdownElement = Class(name="BreakdownElement")
uma_WorkOrder = Class(name="uma::WorkOrder")
ProcessElement = Class(name="ProcessElement")
uma_PlanningData = Class(name="uma::PlanningData")
uma_Milestone = Class(name="uma::Milestone")
uma_Iteration = Class(name="uma::Iteration")
Activity = Class(name="Activity")
uma_Phase = Class(name="uma::Phase")
uma_TeamProfile = Class(name="uma::TeamProfile")
uma_RoleDescriptor = Class(name="uma::RoleDescriptor")
Descriptor = Class(name="Descriptor")
uma_TaskDescriptor = Class(name="uma::TaskDescriptor")
uma_WorkProductDescriptor = Class(name="uma::WorkProductDescriptor")
uma_ProcessElement = Class(name="uma::ProcessElement", is_abstract=True)
uma_Descriptor = Class(name="uma::Descriptor", is_abstract=True)
uma_CompositeRole = Class(name="uma::CompositeRole")
RoleDescriptor = Class(name="RoleDescriptor")
uma_BreakdownElementDescription = Class(name="uma::BreakdownElementDescription")
uma_ActivityDescription = Class(name="uma::ActivityDescription")
BreakdownElementDescription = Class(name="BreakdownElementDescription")
uma_DeliveryProcessDescription = Class(name="uma::DeliveryProcessDescription")
ProcessDescription = Class(name="ProcessDescription")
uma_ProcessDescription = Class(name="uma::ProcessDescription")
ActivityDescription = Class(name="ActivityDescription")
uma_DescriptorDescription = Class(name="uma::DescriptorDescription")
Guidance = Class(name="Guidance")
uma_EstimationConsiderations = Class(name="uma::EstimationConsiderations")
uma_Whitepaper = Class(name="uma::Whitepaper")
Concept = Class(name="Concept")
uma_TermDefinition = Class(name="uma::TermDefinition")
uma_Practice = Class(name="uma::Practice")
uma_Discipline = Class(name="uma::Discipline")
ContentCategory = Class(name="ContentCategory")
uma_EstimatingMetric = Class(name="uma::EstimatingMetric")
uma_ContentCategory = Class(name="uma::ContentCategory", is_abstract=True)
uma_RoleSet = Class(name="uma::RoleSet")
uma_Domain = Class(name="uma::Domain")
uma_WorkProductType = Class(name="uma::WorkProductType")
uma_DisciplineGrouping = Class(name="uma::DisciplineGrouping")
uma_Tool = Class(name="uma::Tool")
uma_RoleSetGrouping = Class(name="uma::RoleSetGrouping")
uma_CustomCategory = Class(name="uma::CustomCategory")
uma_Process = Class(name="uma::Process", is_abstract=True)
uma_CapabilityPattern = Class(name="uma::CapabilityPattern")
uma_MethodConfiguration = Class(name="uma::MethodConfiguration")
uma_ProcessPlanningTemplate = Class(name="uma::ProcessPlanningTemplate")
uma_ProcessComponent = Class(name="uma::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
uma_ProcessComponentInterface = Class(name="uma::ProcessComponentInterface")
uma_ProcessPackage = Class(name="uma::ProcessPackage")
uma_DeliveryProcess = Class(name="uma::DeliveryProcess")
Process = Class(name="Process")
uma_ProcessComponentDescriptor = Class(name="uma::ProcessComponentDescriptor")
uma_MethodPlugin = Class(name="uma::MethodPlugin")
uma_VariabilityElement = Class(name="uma::VariabilityElement", is_abstract=True)
uma_ProcessContribution = Class(name="uma::ProcessContribution")
uma_MethodUnit = Class(name="uma::MethodUnit", is_abstract=True)
uma_ProcessFamily = Class(name="uma::ProcessFamily")
MethodConfiguration = Class(name="MethodConfiguration")
uma_MethodLibrary = Class(name="uma::MethodLibrary")

# uma_Classifier class attributes and methods

# Type class attributes and methods

# uma_Type class attributes and methods

# PackageableElement class attributes and methods

# uma_Element class attributes and methods

# uma_NamedElement class attributes and methods
uma_NamedElement_name: Property = Property(name="name", type=StringType)
uma_NamedElement.attributes={uma_NamedElement_name}

# Element class attributes and methods

# uma_PackageableElement class attributes and methods

# NamedElement class attributes and methods

# uma_Package class attributes and methods

# Namespace class attributes and methods

# uma_MethodElement class attributes and methods
uma_MethodElement_guid: Property = Property(name="guid", type=StringType)
uma_MethodElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
uma_MethodElement_suppressed: Property = Property(name="suppressed", type=StringType)
uma_MethodElement_orderingGuide: Property = Property(name="orderingGuide", type=StringType)
uma_MethodElement.attributes={uma_MethodElement_suppressed, uma_MethodElement_orderingGuide, uma_MethodElement_guid, uma_MethodElement_briefDescription}

# uma_Constraint class attributes and methods
uma_Constraint_body: Property = Property(name="body", type=StringType)
uma_Constraint.attributes={uma_Constraint_body}

# MethodElement class attributes and methods

# uma_ContentElement class attributes and methods

# DescribableElement class attributes and methods

# VariabilityElement class attributes and methods

# uma_SupportingMaterial class attributes and methods

# uma_Concept class attributes and methods

# uma_Checklist class attributes and methods

# uma_Guideline class attributes and methods

# uma_Example class attributes and methods

# uma_ReusableAsset class attributes and methods

# uma_DescribableElement class attributes and methods
uma_DescribableElement_shapeicon: Property = Property(name="shapeicon", type=StringType)
uma_DescribableElement_nodeicon: Property = Property(name="nodeicon", type=StringType)
uma_DescribableElement_presentationName: Property = Property(name="presentationName", type=StringType)
uma_DescribableElement.attributes={uma_DescribableElement_nodeicon, uma_DescribableElement_shapeicon, uma_DescribableElement_presentationName}

# Classifier class attributes and methods

# uma_Namespace class attributes and methods

# MethodUnit class attributes and methods

# uma_Section class attributes and methods
uma_Section_sectionName: Property = Property(name="sectionName", type=StringType)
uma_Section_sectionDescription: Property = Property(name="sectionDescription", type=StringType)
uma_Section.attributes={uma_Section_sectionDescription, uma_Section_sectionName}

# uma_Role class attributes and methods

# ContentElement class attributes and methods

# uma_WorkProduct class attributes and methods

# uma_Estimate class attributes and methods

# uma_Report class attributes and methods

# uma_ContentDescription class attributes and methods
uma_ContentDescription_mainDescription: Property = Property(name="mainDescription", type=StringType)
uma_ContentDescription_keyConsiderations: Property = Property(name="keyConsiderations", type=StringType)
uma_ContentDescription.attributes={uma_ContentDescription_mainDescription, uma_ContentDescription_keyConsiderations}

# uma_Task class attributes and methods

# WorkDefinition class attributes and methods

# uma_Step class attributes and methods

# uma_WorkDefinition class attributes and methods

# Section class attributes and methods

# uma_Guidance class attributes and methods

# uma_Artifact class attributes and methods

# WorkProduct class attributes and methods

# uma_Deliverable class attributes and methods

# uma_Template class attributes and methods

# uma_ToolMentor class attributes and methods

# uma_Outcome class attributes and methods

# uma_MethodPackage class attributes and methods
uma_MethodPackage_global: Property = Property(name="global", type=StringType)
uma_MethodPackage.attributes={uma_MethodPackage_global}

# Package class attributes and methods

# uma_ContentPackage class attributes and methods

# MethodPackage class attributes and methods

# uma_ArtifactDescription class attributes and methods
uma_ArtifactDescription_briefOutline: Property = Property(name="briefOutline", type=StringType)
uma_ArtifactDescription_representationOptions: Property = Property(name="representationOptions", type=StringType)
uma_ArtifactDescription.attributes={uma_ArtifactDescription_representationOptions, uma_ArtifactDescription_briefOutline}

# WorkProductDescription class attributes and methods

# uma_WorkProductDescription class attributes and methods
uma_WorkProductDescription_externalId: Property = Property(name="externalId", type=StringType)
uma_WorkProductDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_WorkProductDescription_impactOfNotHaving: Property = Property(name="impactOfNotHaving", type=StringType)
uma_WorkProductDescription_reasonsForNotNeeding: Property = Property(name="reasonsForNotNeeding", type=StringType)
uma_WorkProductDescription.attributes={uma_WorkProductDescription_impactOfNotHaving, uma_WorkProductDescription_reasonsForNotNeeding, uma_WorkProductDescription_purpose, uma_WorkProductDescription_externalId}

# ContentDescription class attributes and methods

# uma_DeliverableDescription class attributes and methods
uma_DeliverableDescription_externalDescription: Property = Property(name="externalDescription", type=StringType)
uma_DeliverableDescription_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
uma_DeliverableDescription.attributes={uma_DeliverableDescription_externalDescription, uma_DeliverableDescription_packagingGuidance}

# uma_TaskDescription class attributes and methods
uma_TaskDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_TaskDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_TaskDescription.attributes={uma_TaskDescription_alternatives, uma_TaskDescription_purpose}

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
uma_PracticeDescription.attributes={uma_PracticeDescription_goals, uma_PracticeDescription_background, uma_PracticeDescription_application, uma_PracticeDescription_problem, uma_PracticeDescription_levelsOfAdoption, uma_PracticeDescription_additionalInfo}

# uma_Point class attributes and methods
uma_Point_x: Property = Property(name="x", type=StringType)
uma_Point_y: Property = Property(name="y", type=StringType)
uma_Point.attributes={uma_Point_x, uma_Point_y}

# uma_GraphElement class attributes and methods

# DiagramElement class attributes and methods

# uma_DiagramElement class attributes and methods
uma_DiagramElement_isVisible: Property = Property(name="isVisible", type=StringType)
uma_DiagramElement.attributes={uma_DiagramElement_isVisible}

# uma_DiagramLink class attributes and methods
uma_DiagramLink_zoom: Property = Property(name="zoom", type=StringType)
uma_DiagramLink.attributes={uma_DiagramLink_zoom}

# uma_RoleDescription class attributes and methods
uma_RoleDescription_assignmentApproaches: Property = Property(name="assignmentApproaches", type=StringType)
uma_RoleDescription_synonyms: Property = Property(name="synonyms", type=StringType)
uma_RoleDescription_skills: Property = Property(name="skills", type=StringType)
uma_RoleDescription.attributes={uma_RoleDescription_skills, uma_RoleDescription_synonyms, uma_RoleDescription_assignmentApproaches}

# uma_Reference class attributes and methods
uma_Reference_isIndividualRepresentation: Property = Property(name="isIndividualRepresentation", type=StringType)
uma_Reference.attributes={uma_Reference_isIndividualRepresentation}

# uma_Property class attributes and methods
uma_Property_key: Property = Property(name="key", type=StringType)
uma_Property_value: Property = Property(name="value", type=StringType)
uma_Property.attributes={uma_Property_key, uma_Property_value}

# uma_Diagram class attributes and methods
uma_Diagram_zoom: Property = Property(name="zoom", type=StringType)
uma_Diagram.attributes={uma_Diagram_zoom}

# GraphElement class attributes and methods

# uma_GraphEdge class attributes and methods

# uma_Dimension class attributes and methods
uma_Dimension_width: Property = Property(name="width", type=StringType)
uma_Dimension_height: Property = Property(name="height", type=StringType)
uma_Dimension.attributes={uma_Dimension_width, uma_Dimension_height}

# uma_GraphConnector class attributes and methods

# uma_SemanticModelBridge class attributes and methods
uma_SemanticModelBridge_presentation: Property = Property(name="presentation", type=StringType)
uma_SemanticModelBridge.attributes={uma_SemanticModelBridge_presentation}

# GraphNode class attributes and methods

# uma_GraphNode class attributes and methods

# uma_SimpleSemanticModelElement class attributes and methods
uma_SimpleSemanticModelElement_typeInfo: Property = Property(name="typeInfo", type=StringType)
uma_SimpleSemanticModelElement.attributes={uma_SimpleSemanticModelElement_typeInfo}

# SemanticModelBridge class attributes and methods

# uma_UMASemanticModelBridge class attributes and methods

# uma_CoreSemanticModelBridge class attributes and methods

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
uma_Ellipse.attributes={uma_Ellipse_radiusX, uma_Ellipse_radiusY, uma_Ellipse_startAngle, uma_Ellipse_rotation, uma_Ellipse_endAngle}

# uma_Activity class attributes and methods

# WorkBreakdownElement class attributes and methods

# uma_BreakdownElement class attributes and methods
uma_BreakdownElement_prefix: Property = Property(name="prefix", type=StringType)
uma_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=StringType)
uma_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=StringType)
uma_BreakdownElement_isOptional: Property = Property(name="isOptional", type=StringType)
uma_BreakdownElement.attributes={uma_BreakdownElement_prefix, uma_BreakdownElement_hasMultipleOccurrences, uma_BreakdownElement_isPlanned, uma_BreakdownElement_isOptional}

# uma_Roadmap class attributes and methods

# uma_WorkBreakdownElement class attributes and methods
uma_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=StringType)
uma_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=StringType)
uma_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=StringType)
uma_WorkBreakdownElement.attributes={uma_WorkBreakdownElement_isOngoing, uma_WorkBreakdownElement_isEventDriven, uma_WorkBreakdownElement_isRepeatable}

# BreakdownElement class attributes and methods

# uma_WorkOrder class attributes and methods
uma_WorkOrder_linkType: Property = Property(name="linkType", type=StringType)
uma_WorkOrder.attributes={uma_WorkOrder_linkType}

# ProcessElement class attributes and methods

# uma_PlanningData class attributes and methods
uma_PlanningData_startDate: Property = Property(name="startDate", type=StringType)
uma_PlanningData_finishDate: Property = Property(name="finishDate", type=StringType)
uma_PlanningData_rank: Property = Property(name="rank", type=StringType)
uma_PlanningData.attributes={uma_PlanningData_rank, uma_PlanningData_finishDate, uma_PlanningData_startDate}

# uma_Milestone class attributes and methods

# uma_Iteration class attributes and methods

# Activity class attributes and methods

# uma_Phase class attributes and methods

# uma_TeamProfile class attributes and methods

# uma_RoleDescriptor class attributes and methods

# Descriptor class attributes and methods

# uma_TaskDescriptor class attributes and methods

# uma_WorkProductDescriptor class attributes and methods
uma_WorkProductDescriptor_activityEntryState: Property = Property(name="activityEntryState", type=StringType)
uma_WorkProductDescriptor_activityExitState: Property = Property(name="activityExitState", type=StringType)
uma_WorkProductDescriptor.attributes={uma_WorkProductDescriptor_activityExitState, uma_WorkProductDescriptor_activityEntryState}

# uma_ProcessElement class attributes and methods

# uma_Descriptor class attributes and methods
uma_Descriptor_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=StringType)
uma_Descriptor.attributes={uma_Descriptor_isSynchronizedWithSource}

# uma_CompositeRole class attributes and methods

# RoleDescriptor class attributes and methods

# uma_BreakdownElementDescription class attributes and methods
uma_BreakdownElementDescription_usageGuidance: Property = Property(name="usageGuidance", type=StringType)
uma_BreakdownElementDescription.attributes={uma_BreakdownElementDescription_usageGuidance}

# uma_ActivityDescription class attributes and methods
uma_ActivityDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_ActivityDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_ActivityDescription_howtoStaff: Property = Property(name="howtoStaff", type=StringType)
uma_ActivityDescription.attributes={uma_ActivityDescription_howtoStaff, uma_ActivityDescription_alternatives, uma_ActivityDescription_purpose}

# BreakdownElementDescription class attributes and methods

# uma_DeliveryProcessDescription class attributes and methods
uma_DeliveryProcessDescription_scale: Property = Property(name="scale", type=StringType)
uma_DeliveryProcessDescription_projectCharacteristics: Property = Property(name="projectCharacteristics", type=StringType)
uma_DeliveryProcessDescription_riskLevel: Property = Property(name="riskLevel", type=StringType)
uma_DeliveryProcessDescription_estimatingTechnique: Property = Property(name="estimatingTechnique", type=StringType)
uma_DeliveryProcessDescription_projectMemberExpertise: Property = Property(name="projectMemberExpertise", type=StringType)
uma_DeliveryProcessDescription_typeOfContract: Property = Property(name="typeOfContract", type=StringType)
uma_DeliveryProcessDescription.attributes={uma_DeliveryProcessDescription_riskLevel, uma_DeliveryProcessDescription_estimatingTechnique, uma_DeliveryProcessDescription_scale, uma_DeliveryProcessDescription_projectMemberExpertise, uma_DeliveryProcessDescription_typeOfContract, uma_DeliveryProcessDescription_projectCharacteristics}

# ProcessDescription class attributes and methods

# uma_ProcessDescription class attributes and methods
uma_ProcessDescription_externalId: Property = Property(name="externalId", type=StringType)
uma_ProcessDescription_scope: Property = Property(name="scope", type=StringType)
uma_ProcessDescription_usageNotes: Property = Property(name="usageNotes", type=StringType)
uma_ProcessDescription.attributes={uma_ProcessDescription_scope, uma_ProcessDescription_externalId, uma_ProcessDescription_usageNotes}

# ActivityDescription class attributes and methods

# uma_DescriptorDescription class attributes and methods
uma_DescriptorDescription_refinedDescription: Property = Property(name="refinedDescription", type=StringType)
uma_DescriptorDescription.attributes={uma_DescriptorDescription_refinedDescription}

# Guidance class attributes and methods

# uma_EstimationConsiderations class attributes and methods

# uma_Whitepaper class attributes and methods

# Concept class attributes and methods

# uma_TermDefinition class attributes and methods

# uma_Practice class attributes and methods

# uma_Discipline class attributes and methods

# ContentCategory class attributes and methods

# uma_EstimatingMetric class attributes and methods

# uma_ContentCategory class attributes and methods

# uma_RoleSet class attributes and methods

# uma_Domain class attributes and methods

# uma_WorkProductType class attributes and methods

# uma_DisciplineGrouping class attributes and methods

# uma_Tool class attributes and methods

# uma_RoleSetGrouping class attributes and methods

# uma_CustomCategory class attributes and methods

# uma_Process class attributes and methods

# uma_CapabilityPattern class attributes and methods

# uma_MethodConfiguration class attributes and methods

# uma_ProcessPlanningTemplate class attributes and methods

# uma_ProcessComponent class attributes and methods

# ProcessPackage class attributes and methods

# uma_ProcessComponentInterface class attributes and methods

# uma_ProcessPackage class attributes and methods

# uma_DeliveryProcess class attributes and methods

# Process class attributes and methods

# uma_ProcessComponentDescriptor class attributes and methods

# uma_MethodPlugin class attributes and methods
uma_MethodPlugin_userChangeable: Property = Property(name="userChangeable", type=StringType)
uma_MethodPlugin.attributes={uma_MethodPlugin_userChangeable}

# uma_VariabilityElement class attributes and methods
uma_VariabilityElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_VariabilityElement.attributes={uma_VariabilityElement_variabilityType}

# uma_ProcessContribution class attributes and methods

# uma_MethodUnit class attributes and methods
uma_MethodUnit_changeDescription: Property = Property(name="changeDescription", type=StringType)
uma_MethodUnit_version: Property = Property(name="version", type=StringType)
uma_MethodUnit_authors: Property = Property(name="authors", type=StringType)
uma_MethodUnit_changeDate: Property = Property(name="changeDate", type=StringType)
uma_MethodUnit.attributes={uma_MethodUnit_authors, uma_MethodUnit_changeDate, uma_MethodUnit_changeDescription, uma_MethodUnit_version}

# uma_ProcessFamily class attributes and methods

# MethodConfiguration class attributes and methods

# uma_MethodLibrary class attributes and methods

# Relationships
ownedRules0: BinaryAssociation = BinaryAssociation(
    name="ownedRules0",
    ends={
        Property(name="uma_Constraint", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement", type=uma_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportingMaterials1: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials1",
    ends={
        Property(name="uma_SupportingMaterial", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
conceptsAndPapers2: BinaryAssociation = BinaryAssociation(
    name="conceptsAndPapers2",
    ends={
        Property(name="uma_Concept", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement3", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
checklists4: BinaryAssociation = BinaryAssociation(
    name="checklists4",
    ends={
        Property(name="uma_Checklist", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement5", type=uma_Checklist, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines6: BinaryAssociation = BinaryAssociation(
    name="guidelines6",
    ends={
        Property(name="uma_Guideline", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement7", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
examples8: BinaryAssociation = BinaryAssociation(
    name="examples8",
    ends={
        Property(name="uma_Example", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement9", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
assets10: BinaryAssociation = BinaryAssociation(
    name="assets10",
    ends={
        Property(name="uma_ReusableAsset", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement11", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
presentation12: BinaryAssociation = BinaryAssociation(
    name="presentation12",
    ends={
        Property(name="uma_ContentDescription", type=uma_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DescribableElement", type=uma_ContentDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections13: BinaryAssociation = BinaryAssociation(
    name="sections13",
    ends={
        Property(name="uma_Section", type=uma_ContentDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentDescription14", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections16: BinaryAssociation = BinaryAssociation(
    name="subSections16",
    ends={
        Property(name="uma_Section17", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section15", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor19: BinaryAssociation = BinaryAssociation(
    name="predecessor19",
    ends={
        Property(name="uma_Section20", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section18", type=uma_Section, multiplicity=Multiplicity(0, 1))
    }
)
modifies21: BinaryAssociation = BinaryAssociation(
    name="modifies21",
    ends={
        Property(name="uma_WorkProduct", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor22: BinaryAssociation = BinaryAssociation(
    name="responsibleFor22",
    ends={
        Property(name="uma_WorkProduct24", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role23", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
estimate25: BinaryAssociation = BinaryAssociation(
    name="estimate25",
    ends={
        Property(name="uma_Estimate", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct26", type=uma_Estimate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reports27: BinaryAssociation = BinaryAssociation(
    name="reports27",
    ends={
        Property(name="uma_Report", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct28", type=uma_Report, multiplicity=Multiplicity(0, 9999))
    }
)
performedBy33: BinaryAssociation = BinaryAssociation(
    name="performedBy33",
    ends={
        Property(name="uma_Role34", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task", type=uma_Role, multiplicity=Multiplicity(0, 1))
    }
)
mandatoryInput35: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput35",
    ends={
        Property(name="uma_WorkProduct37", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task36", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
output38: BinaryAssociation = BinaryAssociation(
    name="output38",
    ends={
        Property(name="uma_WorkProduct40", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task39", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
additionallyPerformedBy41: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy41",
    ends={
        Property(name="uma_Role43", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task42", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput44: BinaryAssociation = BinaryAssociation(
    name="optionalInput44",
    ends={
        Property(name="uma_WorkProduct46", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task45", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
steps47: BinaryAssociation = BinaryAssociation(
    name="steps47",
    ends={
        Property(name="uma_Step", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task48", type=uma_Step, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors49: BinaryAssociation = BinaryAssociation(
    name="toolMentors49",
    ends={
        Property(name="uma_ToolMentor51", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task50", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
estimate52: BinaryAssociation = BinaryAssociation(
    name="estimate52",
    ends={
        Property(name="uma_Estimate54", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task53", type=uma_Estimate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
precondition55: BinaryAssociation = BinaryAssociation(
    name="precondition55",
    ends={
        Property(name="uma_Constraint56", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postcondition57: BinaryAssociation = BinaryAssociation(
    name="postcondition57",
    ends={
        Property(name="uma_Constraint59", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition58", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArtifact61: BinaryAssociation = BinaryAssociation(
    name="containerArtifact61",
    ends={
        Property(name="Artifact", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containedArtifacts", type=uma_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
containedArtifacts63: BinaryAssociation = BinaryAssociation(
    name="containedArtifacts63",
    ends={
        Property(name="Artifact64", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArtifact", type=uma_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templates29: BinaryAssociation = BinaryAssociation(
    name="templates29",
    ends={
        Property(name="uma_Template", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct30", type=uma_Template, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors31: BinaryAssociation = BinaryAssociation(
    name="toolMentors31",
    ends={
        Property(name="uma_ToolMentor", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct32", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
reusedPackages68: BinaryAssociation = BinaryAssociation(
    name="reusedPackages68",
    ends={
        Property(name="uma_MethodPackage", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage67", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999))
    }
)
parentPackage70: BinaryAssociation = BinaryAssociation(
    name="parentPackage70",
    ends={
        Property(name="MethodPackage", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="childPackages", type=uma_MethodPackage, multiplicity=Multiplicity(0, 1))
    }
)
childPackages72: BinaryAssociation = BinaryAssociation(
    name="childPackages72",
    ends={
        Property(name="MethodPackage73", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPackage", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentElements74: BinaryAssociation = BinaryAssociation(
    name="contentElements74",
    ends={
        Property(name="uma_ContentElement75", type=uma_ContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentPackage", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deliveredWorkProducts65: BinaryAssociation = BinaryAssociation(
    name="deliveredWorkProducts65",
    ends={
        Property(name="uma_WorkProduct66", type=uma_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Deliverable", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
position76: BinaryAssociation = BinaryAssociation(
    name="position76",
    ends={
        Property(name="uma_Point", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphElement", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contained77: BinaryAssociation = BinaryAssociation(
    name="contained77",
    ends={
        Property(name="DiagramElement", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uma_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link78: BinaryAssociation = BinaryAssociation(
    name="link78",
    ends={
        Property(name="DiagramLink", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container83: BinaryAssociation = BinaryAssociation(
    name="container83",
    ends={
        Property(name="GraphElement", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contained", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
reference84: BinaryAssociation = BinaryAssociation(
    name="reference84",
    ends={
        Property(name="Reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referenced", type=uma_Reference, multiplicity=Multiplicity(0, 9999))
    }
)
property85: BinaryAssociation = BinaryAssociation(
    name="property85",
    ends={
        Property(name="uma_Property", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramElement", type=uma_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewport86: BinaryAssociation = BinaryAssociation(
    name="viewport86",
    ends={
        Property(name="uma_Point87", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramLink", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphElement88: BinaryAssociation = BinaryAssociation(
    name="graphElement88",
    ends={
        Property(name="GraphElement89", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
diagram90: BinaryAssociation = BinaryAssociation(
    name="diagram90",
    ends={
        Property(name="Diagram", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="diagramLink", type=uma_Diagram, multiplicity=Multiplicity(1, 1))
    }
)
graphElement91: BinaryAssociation = BinaryAssociation(
    name="graphElement91",
    ends={
        Property(name="GraphElement92", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchorage", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
graphEdge93: BinaryAssociation = BinaryAssociation(
    name="graphEdge93",
    ends={
        Property(name="GraphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchor", type=uma_GraphEdge, multiplicity=Multiplicity(0, 9999))
    }
)
graphElement94: BinaryAssociation = BinaryAssociation(
    name="graphElement94",
    ends={
        Property(name="GraphElement95", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticModel", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
diagram96: BinaryAssociation = BinaryAssociation(
    name="diagram96",
    ends={
        Property(name="Diagram97", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uma_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
referenced98: BinaryAssociation = BinaryAssociation(
    name="referenced98",
    ends={
        Property(name="DiagramElement99", type=uma_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
anchorage79: BinaryAssociation = BinaryAssociation(
    name="anchorage79",
    ends={
        Property(name="GraphConnector", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement80", type=uma_GraphConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semanticModel81: BinaryAssociation = BinaryAssociation(
    name="semanticModel81",
    ends={
        Property(name="SemanticModelBridge", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement82", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
anchor100: BinaryAssociation = BinaryAssociation(
    name="anchor100",
    ends={
        Property(name="GraphConnector101", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(2, 2))
    }
)
waypoints102: BinaryAssociation = BinaryAssociation(
    name="waypoints102",
    ends={
        Property(name="uma_Point103", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphEdge", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
viewpoint104: BinaryAssociation = BinaryAssociation(
    name="viewpoint104",
    ends={
        Property(name="uma_Point105", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Diagram", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramLink106: BinaryAssociation = BinaryAssociation(
    name="diagramLink106",
    ends={
        Property(name="DiagramLink107", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999))
    }
)
namespace108: BinaryAssociation = BinaryAssociation(
    name="namespace108",
    ends={
        Property(name="SemanticModelBridge110", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram109", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size111: BinaryAssociation = BinaryAssociation(
    name="size111",
    ends={
        Property(name="uma_Dimension", type=uma_GraphNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphNode", type=uma_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element112: BinaryAssociation = BinaryAssociation(
    name="element112",
    ends={
        Property(name="uma_MethodElement113", type=uma_UMASemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_UMASemanticModelBridge", type=uma_MethodElement, multiplicity=Multiplicity(1, 1))
    }
)
element114: BinaryAssociation = BinaryAssociation(
    name="element114",
    ends={
        Property(name="uma_Element", type=uma_CoreSemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CoreSemanticModelBridge", type=uma_Element, multiplicity=Multiplicity(1, 1))
    }
)
center117: BinaryAssociation = BinaryAssociation(
    name="center117",
    ends={
        Property(name="uma_Point118", type=uma_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Ellipse", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakdownElements119: BinaryAssociation = BinaryAssociation(
    name="breakdownElements119",
    ends={
        Property(name="BreakdownElement", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="superActivities", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 9999))
    }
)
roadmaps120: BinaryAssociation = BinaryAssociation(
    name="roadmaps120",
    ends={
        Property(name="uma_Roadmap", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity", type=uma_Roadmap, multiplicity=Multiplicity(0, 9999))
    }
)
waypoints115: BinaryAssociation = BinaryAssociation(
    name="waypoints115",
    ends={
        Property(name="uma_Point116", type=uma_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Polyline", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
checklists124: BinaryAssociation = BinaryAssociation(
    name="checklists124",
    ends={
        Property(name="uma_Activity125", type=uma_Checklist, multiplicity=Multiplicity(0, 9999)),
        Property(name="uma_Checklist126", type=uma_Activity, multiplicity=Multiplicity(1, 1))
    }
)
concepts127: BinaryAssociation = BinaryAssociation(
    name="concepts127",
    ends={
        Property(name="uma_Concept129", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity128", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
examples130: BinaryAssociation = BinaryAssociation(
    name="examples130",
    ends={
        Property(name="uma_Example132", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity131", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines133: BinaryAssociation = BinaryAssociation(
    name="guidelines133",
    ends={
        Property(name="uma_Guideline135", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity134", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
reusableAssets136: BinaryAssociation = BinaryAssociation(
    name="reusableAssets136",
    ends={
        Property(name="uma_ReusableAsset138", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity137", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
linkToPredecessor139: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor139",
    ends={
        Property(name="uma_WorkOrder", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkBreakdownElement", type=uma_WorkOrder, multiplicity=Multiplicity(0, 9999))
    }
)
supportingMaterials121: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials121",
    ends={
        Property(name="uma_SupportingMaterial123", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity122", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
presentedAfter141: BinaryAssociation = BinaryAssociation(
    name="presentedAfter141",
    ends={
        Property(name="uma_BreakdownElement", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement140", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
presentedBefore143: BinaryAssociation = BinaryAssociation(
    name="presentedBefore143",
    ends={
        Property(name="uma_BreakdownElement144", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement142", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
planningData145: BinaryAssociation = BinaryAssociation(
    name="planningData145",
    ends={
        Property(name="uma_PlanningData", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement146", type=uma_PlanningData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superActivities147: BinaryAssociation = BinaryAssociation(
    name="superActivities147",
    ends={
        Property(name="Activity", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="breakdownElements", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
teamRoles148: BinaryAssociation = BinaryAssociation(
    name="teamRoles148",
    ends={
        Property(name="uma_RoleDescriptor", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TeamProfile", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
superTeam150: BinaryAssociation = BinaryAssociation(
    name="superTeam150",
    ends={
        Property(name="TeamProfile", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="subTeam", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1))
    }
)
subTeam152: BinaryAssociation = BinaryAssociation(
    name="subTeam152",
    ends={
        Property(name="TeamProfile153", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="superTeam", type=uma_TeamProfile, multiplicity=Multiplicity(0, 9999))
    }
)
Role154: BinaryAssociation = BinaryAssociation(
    name="Role154",
    ends={
        Property(name="uma_Role156", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor155", type=uma_Role, multiplicity=Multiplicity(0, 1))
    }
)
performsAdditionally157: BinaryAssociation = BinaryAssociation(
    name="performsAdditionally157",
    ends={
        Property(name="TaskDescriptor", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="additionallyPerformedBy", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
assistsIn158: BinaryAssociation = BinaryAssociation(
    name="assistsIn158",
    ends={
        Property(name="TaskDescriptor159", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="assistedBy", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
modifies160: BinaryAssociation = BinaryAssociation(
    name="modifies160",
    ends={
        Property(name="WorkProductDescriptor", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="workedOnBy", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
performsAsOwner161: BinaryAssociation = BinaryAssociation(
    name="performsAsOwner161",
    ends={
        Property(name="TaskDescriptor162", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="performedPrimarilyBy", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
pred165: BinaryAssociation = BinaryAssociation(
    name="pred165",
    ends={
        Property(name="uma_WorkBreakdownElement167", type=uma_WorkOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkOrder166", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
Task168: BinaryAssociation = BinaryAssociation(
    name="Task168",
    ends={
        Property(name="uma_Task169", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor", type=uma_Task, multiplicity=Multiplicity(0, 1))
    }
)
additionallyPerformedBy170: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy170",
    ends={
        Property(name="RoleDescriptor", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="performsAdditionally", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
assistedBy171: BinaryAssociation = BinaryAssociation(
    name="assistedBy171",
    ends={
        Property(name="RoleDescriptor172", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="assistsIn", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
externalInput173: BinaryAssociation = BinaryAssociation(
    name="externalInput173",
    ends={
        Property(name="WorkProductDescriptor174", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="externalInputTo", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryInput175: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput175",
    ends={
        Property(name="WorkProductDescriptor176", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="mandatoryInputTo", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor163: BinaryAssociation = BinaryAssociation(
    name="responsibleFor163",
    ends={
        Property(name="WorkProductDescriptor164", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="responsibleRole", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput177: BinaryAssociation = BinaryAssociation(
    name="optionalInput177",
    ends={
        Property(name="WorkProductDescriptor178", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="OptionalInputTo", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
output179: BinaryAssociation = BinaryAssociation(
    name="output179",
    ends={
        Property(name="WorkProductDescriptor180", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="outputFrom", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
performedPrimarilyBy181: BinaryAssociation = BinaryAssociation(
    name="performedPrimarilyBy181",
    ends={
        Property(name="RoleDescriptor182", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="performsAsOwner", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
selectedSteps183: BinaryAssociation = BinaryAssociation(
    name="selectedSteps183",
    ends={
        Property(name="uma_Section185", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor184", type=uma_Section, multiplicity=Multiplicity(0, 9999))
    }
)
WorkProduct186: BinaryAssociation = BinaryAssociation(
    name="WorkProduct186",
    ends={
        Property(name="uma_WorkProduct187", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor", type=uma_WorkProduct, multiplicity=Multiplicity(0, 1))
    }
)
impacts194: BinaryAssociation = BinaryAssociation(
    name="impacts194",
    ends={
        Property(name="impactedBy", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999)),
        Property(name="WorkProductDescriptor195", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1))
    }
)
mandatoryInputTo196: BinaryAssociation = BinaryAssociation(
    name="mandatoryInputTo196",
    ends={
        Property(name="TaskDescriptor197", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="mandatoryInput", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
workedOnBy198: BinaryAssociation = BinaryAssociation(
    name="workedOnBy198",
    ends={
        Property(name="RoleDescriptor199", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="modifies", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
OptionalInputTo200: BinaryAssociation = BinaryAssociation(
    name="OptionalInputTo200",
    ends={
        Property(name="TaskDescriptor201", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="optionalInput", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
outputFrom202: BinaryAssociation = BinaryAssociation(
    name="outputFrom202",
    ends={
        Property(name="TaskDescriptor203", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="output", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
deliverableParts205: BinaryAssociation = BinaryAssociation(
    name="deliverableParts205",
    ends={
        Property(name="uma_WorkProductDescriptor206", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor204", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleRole207: BinaryAssociation = BinaryAssociation(
    name="responsibleRole207",
    ends={
        Property(name="RoleDescriptor208", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="responsibleFor", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
aggregatedRoles209: BinaryAssociation = BinaryAssociation(
    name="aggregatedRoles209",
    ends={
        Property(name="uma_Role210", type=uma_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CompositeRole", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
externalInputTo188: BinaryAssociation = BinaryAssociation(
    name="externalInputTo188",
    ends={
        Property(name="TaskDescriptor189", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="externalInput", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
impactedBy191: BinaryAssociation = BinaryAssociation(
    name="impactedBy191",
    ends={
        Property(name="WorkProductDescriptor192", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
estimationConderations213: BinaryAssociation = BinaryAssociation(
    name="estimationConderations213",
    ends={
        Property(name="uma_EstimationConsiderations", type=uma_Estimate, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Estimate214", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subPractices216: BinaryAssociation = BinaryAssociation(
    name="subPractices216",
    ends={
        Property(name="uma_Practice", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice215", type=uma_Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentReferences217: BinaryAssociation = BinaryAssociation(
    name="contentReferences217",
    ends={
        Property(name="uma_ContentElement219", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice218", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
activityReferences220: BinaryAssociation = BinaryAssociation(
    name="activityReferences220",
    ends={
        Property(name="uma_Activity222", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice221", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
tasks223: BinaryAssociation = BinaryAssociation(
    name="tasks223",
    ends={
        Property(name="uma_Task224", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline", type=uma_Task, multiplicity=Multiplicity(1, 9999))
    }
)
estimationMetric211: BinaryAssociation = BinaryAssociation(
    name="estimationMetric211",
    ends={
        Property(name="uma_EstimatingMetric", type=uma_Estimate, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Estimate212", type=uma_EstimatingMetric, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
roles228: BinaryAssociation = BinaryAssociation(
    name="roles228",
    ends={
        Property(name="uma_Role229", type=uma_RoleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSet", type=uma_Role, multiplicity=Multiplicity(1, 9999))
    }
)
workProducts230: BinaryAssociation = BinaryAssociation(
    name="workProducts230",
    ends={
        Property(name="uma_WorkProduct231", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
subdomains233: BinaryAssociation = BinaryAssociation(
    name="subdomains233",
    ends={
        Property(name="uma_Domain234", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain232", type=uma_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workProducts235: BinaryAssociation = BinaryAssociation(
    name="workProducts235",
    ends={
        Property(name="uma_WorkProduct236", type=uma_WorkProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductType", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
disciplines237: BinaryAssociation = BinaryAssociation(
    name="disciplines237",
    ends={
        Property(name="uma_Discipline238", type=uma_DisciplineGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DisciplineGrouping", type=uma_Discipline, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors239: BinaryAssociation = BinaryAssociation(
    name="toolMentors239",
    ends={
        Property(name="uma_ToolMentor240", type=uma_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Tool", type=uma_ToolMentor, multiplicity=Multiplicity(1, 9999))
    }
)
roleSets241: BinaryAssociation = BinaryAssociation(
    name="roleSets241",
    ends={
        Property(name="uma_RoleSet242", type=uma_RoleSetGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSetGrouping", type=uma_RoleSet, multiplicity=Multiplicity(0, 9999))
    }
)
categorizedElements243: BinaryAssociation = BinaryAssociation(
    name="categorizedElements243",
    ends={
        Property(name="uma_DescribableElement244", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory", type=uma_DescribableElement, multiplicity=Multiplicity(0, 9999))
    }
)
referenceWorkflows225: BinaryAssociation = BinaryAssociation(
    name="referenceWorkflows225",
    ends={
        Property(name="uma_Activity227", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline226", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
educationMaterials247: BinaryAssociation = BinaryAssociation(
    name="educationMaterials247",
    ends={
        Property(name="uma_SupportingMaterial248", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DeliveryProcess", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
communicationsMaterials249: BinaryAssociation = BinaryAssociation(
    name="communicationsMaterials249",
    ends={
        Property(name="uma_SupportingMaterial251", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DeliveryProcess250", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
includesPatterns252: BinaryAssociation = BinaryAssociation(
    name="includesPatterns252",
    ends={
        Property(name="uma_CapabilityPattern", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process", type=uma_CapabilityPattern, multiplicity=Multiplicity(0, 9999))
    }
)
defaultContext253: BinaryAssociation = BinaryAssociation(
    name="defaultContext253",
    ends={
        Property(name="uma_MethodConfiguration", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process254", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
validContext255: BinaryAssociation = BinaryAssociation(
    name="validContext255",
    ends={
        Property(name="uma_MethodConfiguration257", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process256", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
basedOnProcesses258: BinaryAssociation = BinaryAssociation(
    name="basedOnProcesses258",
    ends={
        Property(name="uma_Process259", type=uma_ProcessPlanningTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPlanningTemplate", type=uma_Process, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces260: BinaryAssociation = BinaryAssociation(
    name="interfaces260",
    ends={
        Property(name="uma_ProcessComponentInterface", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 9999))
    }
)
process261: BinaryAssociation = BinaryAssociation(
    name="process261",
    ends={
        Property(name="uma_Process263", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent262", type=uma_Process, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
processElements264: BinaryAssociation = BinaryAssociation(
    name="processElements264",
    ends={
        Property(name="uma_ProcessElement", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage", type=uma_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams265: BinaryAssociation = BinaryAssociation(
    name="diagrams265",
    ends={
        Property(name="uma_Diagram267", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage266", type=uma_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subCategories245: BinaryAssociation = BinaryAssociation(
    name="subCategories245",
    ends={
        Property(name="uma_ContentCategory", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory246", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
ProcessComponent274: BinaryAssociation = BinaryAssociation(
    name="ProcessComponent274",
    ends={
        Property(name="uma_ProcessComponent275", type=uma_ProcessComponentDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentDescriptor", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
methodPackages276: BinaryAssociation = BinaryAssociation(
    name="methodPackages276",
    ends={
        Property(name="uma_MethodPackage277", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bases279: BinaryAssociation = BinaryAssociation(
    name="bases279",
    ends={
        Property(name="uma_MethodPlugin280", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin278", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
variabilityBasedOnElement282: BinaryAssociation = BinaryAssociation(
    name="variabilityBasedOnElement282",
    ends={
        Property(name="uma_VariabilityElement", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_VariabilityElement281", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1))
    }
)
baseProcess283: BinaryAssociation = BinaryAssociation(
    name="baseProcess283",
    ends={
        Property(name="uma_Process284", type=uma_ProcessContribution, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessContribution", type=uma_Process, multiplicity=Multiplicity(1, 1))
    }
)
interfaceSpecifications268: BinaryAssociation = BinaryAssociation(
    name="interfaceSpecifications268",
    ends={
        Property(name="uma_TaskDescriptor270", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface269", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceIO271: BinaryAssociation = BinaryAssociation(
    name="interfaceIO271",
    ends={
        Property(name="uma_WorkProductDescriptor273", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface272", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyrightStatement285: BinaryAssociation = BinaryAssociation(
    name="copyrightStatement285",
    ends={
        Property(name="uma_SupportingMaterial286", type=uma_MethodUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodUnit", type=uma_SupportingMaterial, multiplicity=Multiplicity(1, 1))
    }
)
methodPluginSelection287: BinaryAssociation = BinaryAssociation(
    name="methodPluginSelection287",
    ends={
        Property(name="uma_MethodPlugin289", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration288", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 9999))
    }
)
methodPackageSelection290: BinaryAssociation = BinaryAssociation(
    name="methodPackageSelection290",
    ends={
        Property(name="uma_MethodPackage292", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration291", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999))
    }
)
processViews293: BinaryAssociation = BinaryAssociation(
    name="processViews293",
    ends={
        Property(name="uma_ContentCategory295", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration294", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
defaultView296: BinaryAssociation = BinaryAssociation(
    name="defaultView296",
    ends={
        Property(name="uma_ContentCategory298", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration297", type=uma_ContentCategory, multiplicity=Multiplicity(1, 1))
    }
)
baseConfigurations300: BinaryAssociation = BinaryAssociation(
    name="baseConfigurations300",
    ends={
        Property(name="uma_MethodConfiguration301", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration299", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
deliveryProcesses302: BinaryAssociation = BinaryAssociation(
    name="deliveryProcesses302",
    ends={
        Property(name="uma_DeliveryProcess303", type=uma_ProcessFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessFamily", type=uma_DeliveryProcess, multiplicity=Multiplicity(0, 9999))
    }
)
methodPlugins304: BinaryAssociation = BinaryAssociation(
    name="methodPlugins304",
    ends={
        Property(name="uma_MethodPlugin305", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predefinedConfigurations306: BinaryAssociation = BinaryAssociation(
    name="predefinedConfigurations306",
    ends={
        Property(name="uma_MethodConfiguration308", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary307", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uma_Classifier_Type = Generalization(general=Type, specific=uma_Classifier)
gen_uma_Type_PackageableElement = Generalization(general=PackageableElement, specific=uma_Type)
gen_uma_NamedElement_Element = Generalization(general=Element, specific=uma_NamedElement)
gen_uma_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uma_PackageableElement)
gen_uma_Package_Namespace = Generalization(general=Namespace, specific=uma_Package)
gen_uma_Package_PackageableElement = Generalization(general=PackageableElement, specific=uma_Package)
gen_uma_MethodElement_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElement)
gen_uma_Constraint_MethodElement = Generalization(general=MethodElement, specific=uma_Constraint)
gen_uma_ContentElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ContentElement)
gen_uma_ContentElement_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_ContentElement)
gen_uma_DescribableElement_MethodElement = Generalization(general=MethodElement, specific=uma_DescribableElement)
gen_uma_DescribableElement_Classifier = Generalization(general=Classifier, specific=uma_DescribableElement)
gen_uma_Namespace_NamedElement = Generalization(general=NamedElement, specific=uma_Namespace)
gen_uma_ContentDescription_MethodUnit = Generalization(general=MethodUnit, specific=uma_ContentDescription)
gen_uma_Section_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_Section)
gen_uma_Role_ContentElement = Generalization(general=ContentElement, specific=uma_Role)
gen_uma_WorkProduct_ContentElement = Generalization(general=ContentElement, specific=uma_WorkProduct)
gen_uma_Task_ContentElement = Generalization(general=ContentElement, specific=uma_Task)
gen_uma_Task_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Task)
gen_uma_WorkDefinition_MethodElement = Generalization(general=MethodElement, specific=uma_WorkDefinition)
gen_uma_Step_Section = Generalization(general=Section, specific=uma_Step)
gen_uma_Step_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Step)
gen_uma_Guidance_ContentElement = Generalization(general=ContentElement, specific=uma_Guidance)
gen_uma_Artifact_WorkProduct = Generalization(general=WorkProduct, specific=uma_Artifact)
gen_uma_Outcome_WorkProduct = Generalization(general=WorkProduct, specific=uma_Outcome)
gen_uma_MethodPackage_MethodElement = Generalization(general=MethodElement, specific=uma_MethodPackage)
gen_uma_MethodPackage_Package = Generalization(general=Package, specific=uma_MethodPackage)
gen_uma_ContentPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ContentPackage)
gen_uma_ArtifactDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_ArtifactDescription)
gen_uma_WorkProductDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_WorkProductDescription)
gen_uma_DeliverableDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_DeliverableDescription)
gen_uma_Deliverable_WorkProduct = Generalization(general=WorkProduct, specific=uma_Deliverable)
gen_uma_TaskDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_TaskDescription)
gen_uma_GuidanceDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_GuidanceDescription)
gen_uma_PracticeDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_PracticeDescription)
gen_uma_GraphElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_GraphElement)
gen_uma_RoleDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_RoleDescription)
gen_uma_DiagramElement_MethodElement = Generalization(general=MethodElement, specific=uma_DiagramElement)
gen_uma_DiagramLink_DiagramElement = Generalization(general=DiagramElement, specific=uma_DiagramLink)
gen_uma_GraphConnector_GraphElement = Generalization(general=GraphElement, specific=uma_GraphConnector)
gen_uma_SemanticModelBridge_DiagramElement = Generalization(general=DiagramElement, specific=uma_SemanticModelBridge)
gen_uma_Reference_DiagramElement = Generalization(general=DiagramElement, specific=uma_Reference)
gen_uma_Property_DiagramElement = Generalization(general=DiagramElement, specific=uma_Property)
gen_uma_Diagram_GraphNode = Generalization(general=GraphNode, specific=uma_Diagram)
gen_uma_GraphNode_GraphElement = Generalization(general=GraphElement, specific=uma_GraphNode)
gen_uma_SimpleSemanticModelElement_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_SimpleSemanticModelElement)
gen_uma_UMASemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_UMASemanticModelBridge)
gen_uma_CoreSemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_CoreSemanticModelBridge)
gen_uma_LeafElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_LeafElement)
gen_uma_TextElement_LeafElement = Generalization(general=LeafElement, specific=uma_TextElement)
gen_uma_Image_LeafElement = Generalization(general=LeafElement, specific=uma_Image)
gen_uma_GraphicPrimitive_LeafElement = Generalization(general=LeafElement, specific=uma_GraphicPrimitive)
gen_uma_Polyline_GraphicPrimitive = Generalization(general=GraphicPrimitive, specific=uma_Polyline)
gen_uma_GraphEdge_GraphElement = Generalization(general=GraphElement, specific=uma_GraphEdge)
gen_uma_Ellipse_GraphicPrimitive = Generalization(general=GraphicPrimitive, specific=uma_Ellipse)
gen_uma_Activity_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Activity)
gen_uma_Activity_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_Activity)
gen_uma_Activity_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Activity)
gen_uma_WorkBreakdownElement_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_WorkBreakdownElement)
gen_uma_BreakdownElement_ProcessElement = Generalization(general=ProcessElement, specific=uma_BreakdownElement)
gen_uma_Milestone_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_Milestone)
gen_uma_Iteration_Activity = Generalization(general=Activity, specific=uma_Iteration)
gen_uma_Phase_Activity = Generalization(general=Activity, specific=uma_Phase)
gen_uma_TeamProfile_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_TeamProfile)
gen_uma_RoleDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_RoleDescriptor)
gen_uma_WorkOrder_ProcessElement = Generalization(general=ProcessElement, specific=uma_WorkOrder)
gen_uma_ProcessElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ProcessElement)
gen_uma_PlanningData_ProcessElement = Generalization(general=ProcessElement, specific=uma_PlanningData)
gen_uma_Descriptor_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_Descriptor)
gen_uma_TaskDescriptor_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_TaskDescriptor)
gen_uma_TaskDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_TaskDescriptor)
gen_uma_WorkProductDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_WorkProductDescriptor)
gen_uma_CompositeRole_RoleDescriptor = Generalization(general=RoleDescriptor, specific=uma_CompositeRole)
gen_uma_BreakdownElementDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_BreakdownElementDescription)
gen_uma_ActivityDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_ActivityDescription)
gen_uma_DeliveryProcessDescription_ProcessDescription = Generalization(general=ProcessDescription, specific=uma_DeliveryProcessDescription)
gen_uma_ProcessDescription_ActivityDescription = Generalization(general=ActivityDescription, specific=uma_ProcessDescription)
gen_uma_DescriptorDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_DescriptorDescription)
gen_uma_Concept_Guidance = Generalization(general=Guidance, specific=uma_Concept)
gen_uma_Checklist_Guidance = Generalization(general=Guidance, specific=uma_Checklist)
gen_uma_Example_Guidance = Generalization(general=Guidance, specific=uma_Example)
gen_uma_Guideline_Guidance = Generalization(general=Guidance, specific=uma_Guideline)
gen_uma_EstimatingMetric_Guidance = Generalization(general=Guidance, specific=uma_EstimatingMetric)
gen_uma_EstimationConsiderations_Guidance = Generalization(general=Guidance, specific=uma_EstimationConsiderations)
gen_uma_Report_Guidance = Generalization(general=Guidance, specific=uma_Report)
gen_uma_Template_Guidance = Generalization(general=Guidance, specific=uma_Template)
gen_uma_SupportingMaterial_Guidance = Generalization(general=Guidance, specific=uma_SupportingMaterial)
gen_uma_ToolMentor_Guidance = Generalization(general=Guidance, specific=uma_ToolMentor)
gen_uma_Whitepaper_Concept = Generalization(general=Concept, specific=uma_Whitepaper)
gen_uma_TermDefinition_Guidance = Generalization(general=Guidance, specific=uma_TermDefinition)
gen_uma_Practice_Guidance = Generalization(general=Guidance, specific=uma_Practice)
gen_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=uma_ReusableAsset)
gen_uma_Discipline_ContentCategory = Generalization(general=ContentCategory, specific=uma_Discipline)
gen_uma_Estimate_Guidance = Generalization(general=Guidance, specific=uma_Estimate)
gen_uma_ContentCategory_ContentElement = Generalization(general=ContentElement, specific=uma_ContentCategory)
gen_uma_RoleSet_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSet)
gen_uma_Domain_ContentCategory = Generalization(general=ContentCategory, specific=uma_Domain)
gen_uma_WorkProductType_ContentCategory = Generalization(general=ContentCategory, specific=uma_WorkProductType)
gen_uma_DisciplineGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_DisciplineGrouping)
gen_uma_Tool_ContentCategory = Generalization(general=ContentCategory, specific=uma_Tool)
gen_uma_RoleSetGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSetGrouping)
gen_uma_CustomCategory_ContentCategory = Generalization(general=ContentCategory, specific=uma_CustomCategory)
gen_uma_Process_Activity = Generalization(general=Activity, specific=uma_Process)
gen_uma_CapabilityPattern_Process = Generalization(general=Process, specific=uma_CapabilityPattern)
gen_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=uma_ProcessPlanningTemplate)
gen_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=uma_Roadmap)
gen_uma_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=uma_ProcessComponent)
gen_uma_ProcessComponent_MethodUnit = Generalization(general=MethodUnit, specific=uma_ProcessComponent)
gen_uma_ProcessPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ProcessPackage)
gen_uma_ProcessComponentInterface_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_ProcessComponentInterface)
gen_uma_DeliveryProcess_Process = Generalization(general=Process, specific=uma_DeliveryProcess)
gen_uma_ProcessComponentDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_ProcessComponentDescriptor)
gen_uma_MethodPlugin_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodPlugin)
gen_uma_MethodPlugin_Package = Generalization(general=Package, specific=uma_MethodPlugin)
gen_uma_VariabilityElement_MethodElement = Generalization(general=MethodElement, specific=uma_VariabilityElement)
gen_uma_ProcessContribution_Process = Generalization(general=Process, specific=uma_ProcessContribution)
gen_uma_MethodUnit_MethodElement = Generalization(general=MethodElement, specific=uma_MethodUnit)
gen_uma_MethodConfiguration_MethodElement = Generalization(general=MethodElement, specific=uma_MethodConfiguration)
gen_uma_ProcessFamily_MethodConfiguration = Generalization(general=MethodConfiguration, specific=uma_ProcessFamily)
gen_uma_MethodLibrary_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodLibrary)
gen_uma_MethodLibrary_Package = Generalization(general=Package, specific=uma_MethodLibrary)

# Domain Model
domain_model = DomainModel(
    name="uma",
    types={uma_Classifier, Type, uma_Type, PackageableElement, uma_Element, uma_NamedElement, Element, uma_PackageableElement, NamedElement, uma_Package, Namespace, uma_MethodElement, uma_Constraint, MethodElement, uma_ContentElement, DescribableElement, VariabilityElement, uma_SupportingMaterial, uma_Concept, uma_Checklist, uma_Guideline, uma_Example, uma_ReusableAsset, uma_DescribableElement, Classifier, uma_Namespace, MethodUnit, uma_Section, uma_Role, ContentElement, uma_WorkProduct, uma_Estimate, uma_Report, uma_ContentDescription, uma_Task, WorkDefinition, uma_Step, uma_WorkDefinition, Section, uma_Guidance, uma_Artifact, WorkProduct, uma_Deliverable, uma_Template, uma_ToolMentor, uma_Outcome, uma_MethodPackage, Package, uma_ContentPackage, MethodPackage, uma_ArtifactDescription, WorkProductDescription, uma_WorkProductDescription, ContentDescription, uma_DeliverableDescription, uma_TaskDescription, uma_GuidanceDescription, uma_PracticeDescription, uma_Point, uma_GraphElement, DiagramElement, uma_DiagramElement, uma_DiagramLink, uma_RoleDescription, uma_Reference, uma_Property, uma_Diagram, GraphElement, uma_GraphEdge, uma_Dimension, uma_GraphConnector, uma_SemanticModelBridge, GraphNode, uma_GraphNode, uma_SimpleSemanticModelElement, SemanticModelBridge, uma_UMASemanticModelBridge, uma_CoreSemanticModelBridge, uma_LeafElement, uma_TextElement, LeafElement, uma_Image, uma_GraphicPrimitive, uma_Polyline, GraphicPrimitive, uma_Ellipse, uma_Activity, WorkBreakdownElement, uma_BreakdownElement, uma_Roadmap, uma_WorkBreakdownElement, BreakdownElement, uma_WorkOrder, ProcessElement, uma_PlanningData, uma_Milestone, uma_Iteration, Activity, uma_Phase, uma_TeamProfile, uma_RoleDescriptor, Descriptor, uma_TaskDescriptor, uma_WorkProductDescriptor, uma_ProcessElement, uma_Descriptor, uma_CompositeRole, RoleDescriptor, uma_BreakdownElementDescription, uma_ActivityDescription, BreakdownElementDescription, uma_DeliveryProcessDescription, ProcessDescription, uma_ProcessDescription, ActivityDescription, uma_DescriptorDescription, Guidance, uma_EstimationConsiderations, uma_Whitepaper, Concept, uma_TermDefinition, uma_Practice, uma_Discipline, ContentCategory, uma_EstimatingMetric, uma_ContentCategory, uma_RoleSet, uma_Domain, uma_WorkProductType, uma_DisciplineGrouping, uma_Tool, uma_RoleSetGrouping, uma_CustomCategory, uma_Process, uma_CapabilityPattern, uma_MethodConfiguration, uma_ProcessPlanningTemplate, uma_ProcessComponent, ProcessPackage, uma_ProcessComponentInterface, uma_ProcessPackage, uma_DeliveryProcess, Process, uma_ProcessComponentDescriptor, uma_MethodPlugin, uma_VariabilityElement, uma_ProcessContribution, uma_MethodUnit, uma_ProcessFamily, MethodConfiguration, uma_MethodLibrary, WorkOrderType, VariabilityType},
    associations={ownedRules0, supportingMaterials1, conceptsAndPapers2, checklists4, guidelines6, examples8, assets10, presentation12, sections13, subSections16, predecessor19, modifies21, responsibleFor22, estimate25, reports27, performedBy33, mandatoryInput35, output38, additionallyPerformedBy41, optionalInput44, steps47, toolMentors49, estimate52, precondition55, postcondition57, containerArtifact61, containedArtifacts63, templates29, toolMentors31, reusedPackages68, parentPackage70, childPackages72, contentElements74, deliveredWorkProducts65, position76, contained77, link78, container83, reference84, property85, viewport86, graphElement88, diagram90, graphElement91, graphEdge93, graphElement94, diagram96, referenced98, anchorage79, semanticModel81, anchor100, waypoints102, viewpoint104, diagramLink106, namespace108, size111, element112, element114, center117, breakdownElements119, roadmaps120, waypoints115, checklists124, concepts127, examples130, guidelines133, reusableAssets136, linkToPredecessor139, supportingMaterials121, presentedAfter141, presentedBefore143, planningData145, superActivities147, teamRoles148, superTeam150, subTeam152, Role154, performsAdditionally157, assistsIn158, modifies160, performsAsOwner161, pred165, Task168, additionallyPerformedBy170, assistedBy171, externalInput173, mandatoryInput175, responsibleFor163, optionalInput177, output179, performedPrimarilyBy181, selectedSteps183, WorkProduct186, impacts194, mandatoryInputTo196, workedOnBy198, OptionalInputTo200, outputFrom202, deliverableParts205, responsibleRole207, aggregatedRoles209, externalInputTo188, impactedBy191, estimationConderations213, subPractices216, contentReferences217, activityReferences220, tasks223, estimationMetric211, roles228, workProducts230, subdomains233, workProducts235, disciplines237, toolMentors239, roleSets241, categorizedElements243, referenceWorkflows225, educationMaterials247, communicationsMaterials249, includesPatterns252, defaultContext253, validContext255, basedOnProcesses258, interfaces260, process261, processElements264, diagrams265, subCategories245, ProcessComponent274, methodPackages276, bases279, variabilityBasedOnElement282, baseProcess283, interfaceSpecifications268, interfaceIO271, copyrightStatement285, methodPluginSelection287, methodPackageSelection290, processViews293, defaultView296, baseConfigurations300, deliveryProcesses302, methodPlugins304, predefinedConfigurations306},
    generalizations={gen_uma_Classifier_Type, gen_uma_Type_PackageableElement, gen_uma_NamedElement_Element, gen_uma_PackageableElement_NamedElement, gen_uma_Package_Namespace, gen_uma_Package_PackageableElement, gen_uma_MethodElement_PackageableElement, gen_uma_Constraint_MethodElement, gen_uma_ContentElement_DescribableElement, gen_uma_ContentElement_VariabilityElement, gen_uma_DescribableElement_MethodElement, gen_uma_DescribableElement_Classifier, gen_uma_Namespace_NamedElement, gen_uma_ContentDescription_MethodUnit, gen_uma_Section_VariabilityElement, gen_uma_Role_ContentElement, gen_uma_WorkProduct_ContentElement, gen_uma_Task_ContentElement, gen_uma_Task_WorkDefinition, gen_uma_WorkDefinition_MethodElement, gen_uma_Step_Section, gen_uma_Step_WorkDefinition, gen_uma_Guidance_ContentElement, gen_uma_Artifact_WorkProduct, gen_uma_Outcome_WorkProduct, gen_uma_MethodPackage_MethodElement, gen_uma_MethodPackage_Package, gen_uma_ContentPackage_MethodPackage, gen_uma_ArtifactDescription_WorkProductDescription, gen_uma_WorkProductDescription_ContentDescription, gen_uma_DeliverableDescription_WorkProductDescription, gen_uma_Deliverable_WorkProduct, gen_uma_TaskDescription_ContentDescription, gen_uma_GuidanceDescription_ContentDescription, gen_uma_PracticeDescription_ContentDescription, gen_uma_GraphElement_DiagramElement, gen_uma_RoleDescription_ContentDescription, gen_uma_DiagramElement_MethodElement, gen_uma_DiagramLink_DiagramElement, gen_uma_GraphConnector_GraphElement, gen_uma_SemanticModelBridge_DiagramElement, gen_uma_Reference_DiagramElement, gen_uma_Property_DiagramElement, gen_uma_Diagram_GraphNode, gen_uma_GraphNode_GraphElement, gen_uma_SimpleSemanticModelElement_SemanticModelBridge, gen_uma_UMASemanticModelBridge_SemanticModelBridge, gen_uma_CoreSemanticModelBridge_SemanticModelBridge, gen_uma_LeafElement_DiagramElement, gen_uma_TextElement_LeafElement, gen_uma_Image_LeafElement, gen_uma_GraphicPrimitive_LeafElement, gen_uma_Polyline_GraphicPrimitive, gen_uma_GraphEdge_GraphElement, gen_uma_Ellipse_GraphicPrimitive, gen_uma_Activity_WorkBreakdownElement, gen_uma_Activity_VariabilityElement, gen_uma_Activity_WorkDefinition, gen_uma_WorkBreakdownElement_BreakdownElement, gen_uma_BreakdownElement_ProcessElement, gen_uma_Milestone_WorkBreakdownElement, gen_uma_Iteration_Activity, gen_uma_Phase_Activity, gen_uma_TeamProfile_BreakdownElement, gen_uma_RoleDescriptor_Descriptor, gen_uma_WorkOrder_ProcessElement, gen_uma_ProcessElement_DescribableElement, gen_uma_PlanningData_ProcessElement, gen_uma_Descriptor_BreakdownElement, gen_uma_TaskDescriptor_WorkBreakdownElement, gen_uma_TaskDescriptor_Descriptor, gen_uma_WorkProductDescriptor_Descriptor, gen_uma_CompositeRole_RoleDescriptor, gen_uma_BreakdownElementDescription_ContentDescription, gen_uma_ActivityDescription_BreakdownElementDescription, gen_uma_DeliveryProcessDescription_ProcessDescription, gen_uma_ProcessDescription_ActivityDescription, gen_uma_DescriptorDescription_BreakdownElementDescription, gen_uma_Concept_Guidance, gen_uma_Checklist_Guidance, gen_uma_Example_Guidance, gen_uma_Guideline_Guidance, gen_uma_EstimatingMetric_Guidance, gen_uma_EstimationConsiderations_Guidance, gen_uma_Report_Guidance, gen_uma_Template_Guidance, gen_uma_SupportingMaterial_Guidance, gen_uma_ToolMentor_Guidance, gen_uma_Whitepaper_Concept, gen_uma_TermDefinition_Guidance, gen_uma_Practice_Guidance, gen_uma_ReusableAsset_Guidance, gen_uma_Discipline_ContentCategory, gen_uma_Estimate_Guidance, gen_uma_ContentCategory_ContentElement, gen_uma_RoleSet_ContentCategory, gen_uma_Domain_ContentCategory, gen_uma_WorkProductType_ContentCategory, gen_uma_DisciplineGrouping_ContentCategory, gen_uma_Tool_ContentCategory, gen_uma_RoleSetGrouping_ContentCategory, gen_uma_CustomCategory_ContentCategory, gen_uma_Process_Activity, gen_uma_CapabilityPattern_Process, gen_uma_ProcessPlanningTemplate_Process, gen_uma_Roadmap_Guidance, gen_uma_ProcessComponent_ProcessPackage, gen_uma_ProcessComponent_MethodUnit, gen_uma_ProcessPackage_MethodPackage, gen_uma_ProcessComponentInterface_BreakdownElement, gen_uma_DeliveryProcess_Process, gen_uma_ProcessComponentDescriptor_Descriptor, gen_uma_MethodPlugin_MethodUnit, gen_uma_MethodPlugin_Package, gen_uma_VariabilityElement_MethodElement, gen_uma_ProcessContribution_Process, gen_uma_MethodUnit_MethodElement, gen_uma_MethodConfiguration_MethodElement, gen_uma_ProcessFamily_MethodConfiguration, gen_uma_MethodLibrary_MethodUnit, gen_uma_MethodLibrary_Package},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)