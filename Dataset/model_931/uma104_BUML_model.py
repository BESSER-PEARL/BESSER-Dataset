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
            EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="finishToFinish"),
			EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="startToFinish")
    }
)

PseudoStateKind: Enumeration = Enumeration(
    name="PseudoStateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate")
    }
)

VariabilityType: Enumeration = Enumeration(
    name="VariabilityType",
    literals={
            EnumerationLiteral(name="localContribution"),
			EnumerationLiteral(name="localReplacement"),
			EnumerationLiteral(name="extendsReplaces"),
			EnumerationLiteral(name="na"),
			EnumerationLiteral(name="contributes"),
			EnumerationLiteral(name="extends"),
			EnumerationLiteral(name="replaces")
    }
)

# Classes
uma_Package = Class(name="uma::Package")
uma_Classifier = Class(name="uma::Classifier", is_abstract=True)
Type = Class(name="Type")
uma_Type = Class(name="uma::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
uma_Element = Class(name="uma::Element", is_abstract=True)
uma_NamedElement = Class(name="uma::NamedElement", is_abstract=True)
Element = Class(name="Element")
uma_PackageableElement = Class(name="uma::PackageableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
uma_Example = Class(name="uma::Example")
Namespace = Class(name="Namespace")
uma_Namespace = Class(name="uma::Namespace", is_abstract=True)
uma_MethodElement = Class(name="uma::MethodElement", is_abstract=True)
uma_Constraint = Class(name="uma::Constraint")
uma_MethodElementProperty = Class(name="uma::MethodElementProperty")
MethodElement = Class(name="MethodElement")
uma_ContentElement = Class(name="uma::ContentElement", is_abstract=True)
DescribableElement = Class(name="DescribableElement")
VariabilityElement = Class(name="VariabilityElement")
uma_SupportingMaterial = Class(name="uma::SupportingMaterial")
uma_Concept = Class(name="uma::Concept")
uma_Checklist = Class(name="uma::Checklist")
uma_Guideline = Class(name="uma::Guideline")
uma_WorkProduct = Class(name="uma::WorkProduct", is_abstract=True)
uma_ReusableAsset = Class(name="uma::ReusableAsset")
uma_TermDefinition = Class(name="uma::TermDefinition")
uma_DescribableElement = Class(name="uma::DescribableElement", is_abstract=True)
Classifier = Class(name="Classifier")
uma_ContentDescription = Class(name="uma::ContentDescription")
MethodUnit = Class(name="MethodUnit")
uma_Section = Class(name="uma::Section")
uma_Role = Class(name="uma::Role")
ContentElement = Class(name="ContentElement")
Section = Class(name="Section")
uma_Report = Class(name="uma::Report")
uma_Template = Class(name="uma::Template")
uma_ToolMentor = Class(name="uma::ToolMentor")
uma_EstimationConsiderations = Class(name="uma::EstimationConsiderations")
uma_Task = Class(name="uma::Task")
WorkDefinition = Class(name="WorkDefinition")
uma_Step = Class(name="uma::Step")
uma_WorkDefinition = Class(name="uma::WorkDefinition", is_abstract=True)
uma_WorkProductDescription = Class(name="uma::WorkProductDescription")
ContentDescription = Class(name="ContentDescription")
uma_Guidance = Class(name="uma::Guidance", is_abstract=True)
uma_Artifact = Class(name="uma::Artifact")
WorkProduct = Class(name="WorkProduct")
uma_Deliverable = Class(name="uma::Deliverable")
uma_Outcome = Class(name="uma::Outcome")
uma_MethodPackage = Class(name="uma::MethodPackage", is_abstract=True)
Package = Class(name="Package")
uma_ContentPackage = Class(name="uma::ContentPackage")
MethodPackage = Class(name="MethodPackage")
uma_ArtifactDescription = Class(name="uma::ArtifactDescription")
WorkProductDescription = Class(name="WorkProductDescription")
uma_DeliverableDescription = Class(name="uma::DeliverableDescription")
uma_RoleDescription = Class(name="uma::RoleDescription")
uma_TaskDescription = Class(name="uma::TaskDescription")
uma_GuidanceDescription = Class(name="uma::GuidanceDescription")
uma_PracticeDescription = Class(name="uma::PracticeDescription")
uma_GraphEdge = Class(name="uma::GraphEdge")
uma_Point = Class(name="uma::Point")
uma_GraphElement = Class(name="uma::GraphElement", is_abstract=True)
DiagramElement = Class(name="DiagramElement")
uma_DiagramElement = Class(name="uma::DiagramElement", is_abstract=True)
uma_DiagramLink = Class(name="uma::DiagramLink")
uma_GraphConnector = Class(name="uma::GraphConnector")
uma_SemanticModelBridge = Class(name="uma::SemanticModelBridge", is_abstract=True)
uma_Reference = Class(name="uma::Reference")
uma_Property = Class(name="uma::Property")
uma_Diagram = Class(name="uma::Diagram")
GraphElement = Class(name="GraphElement")
uma_CoreSemanticModelBridge = Class(name="uma::CoreSemanticModelBridge")
uma_Dimension = Class(name="uma::Dimension")
GraphNode = Class(name="GraphNode")
uma_GraphNode = Class(name="uma::GraphNode")
uma_SimpleSemanticModelElement = Class(name="uma::SimpleSemanticModelElement")
SemanticModelBridge = Class(name="SemanticModelBridge")
uma_UMASemanticModelBridge = Class(name="uma::UMASemanticModelBridge")
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
uma_RoleDescriptor = Class(name="uma::RoleDescriptor")
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
Descriptor = Class(name="Descriptor")
uma_WorkProductDescriptor = Class(name="uma::WorkProductDescriptor")
uma_ProcessElement = Class(name="uma::ProcessElement", is_abstract=True)
uma_Descriptor = Class(name="uma::Descriptor", is_abstract=True)
uma_BreakdownElementDescription = Class(name="uma::BreakdownElementDescription")
uma_TaskDescriptor = Class(name="uma::TaskDescriptor")
uma_CompositeRole = Class(name="uma::CompositeRole")
RoleDescriptor = Class(name="RoleDescriptor")
uma_ActivityDescription = Class(name="uma::ActivityDescription")
BreakdownElementDescription = Class(name="BreakdownElementDescription")
uma_DeliveryProcessDescription = Class(name="uma::DeliveryProcessDescription")
ProcessDescription = Class(name="ProcessDescription")
uma_ProcessDescription = Class(name="uma::ProcessDescription")
ActivityDescription = Class(name="ActivityDescription")
uma_DescriptorDescription = Class(name="uma::DescriptorDescription")
Guidance = Class(name="Guidance")
uma_Transition = Class(name="uma::Transition")
uma_Whitepaper = Class(name="uma::Whitepaper")
Concept = Class(name="Concept")
uma_Practice = Class(name="uma::Practice")
uma_State = Class(name="uma::State")
Vertex = Class(name="Vertex")
uma_Region = Class(name="uma::Region")
uma_StateMachine = Class(name="uma::StateMachine")
uma_Vertex = Class(name="uma::Vertex")
uma_ContentCategory = Class(name="uma::ContentCategory", is_abstract=True)
uma_RoleSet = Class(name="uma::RoleSet")
uma_PseudoState = Class(name="uma::PseudoState")
uma_Discipline = Class(name="uma::Discipline")
ContentCategory = Class(name="ContentCategory")
uma_CustomCategory = Class(name="uma::CustomCategory")
uma_Domain = Class(name="uma::Domain")
uma_WorkProductType = Class(name="uma::WorkProductType")
uma_DisciplineGrouping = Class(name="uma::DisciplineGrouping")
uma_Tool = Class(name="uma::Tool")
uma_ProcessPackage = Class(name="uma::ProcessPackage")
uma_RoleSetGrouping = Class(name="uma::RoleSetGrouping")
uma_DeliveryProcess = Class(name="uma::DeliveryProcess")
Process = Class(name="Process")
uma_Process = Class(name="uma::Process", is_abstract=True)
uma_CapabilityPattern = Class(name="uma::CapabilityPattern")
uma_MethodConfiguration = Class(name="uma::MethodConfiguration")
uma_ProcessPlanningTemplate = Class(name="uma::ProcessPlanningTemplate")
uma_ProcessComponent = Class(name="uma::ProcessComponent")
ProcessPackage = Class(name="ProcessPackage")
uma_ProcessComponentInterface = Class(name="uma::ProcessComponentInterface")
uma_ProcessComponentDescriptor = Class(name="uma::ProcessComponentDescriptor")
uma_MethodPlugin = Class(name="uma::MethodPlugin")
uma_MethodUnit = Class(name="uma::MethodUnit", is_abstract=True)
uma_VariabilityElement = Class(name="uma::VariabilityElement", is_abstract=True)
uma_ProcessFamily = Class(name="uma::ProcessFamily")
MethodConfiguration = Class(name="MethodConfiguration")
uma_MethodLibrary = Class(name="uma::MethodLibrary")

# uma_Package class attributes and methods

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

# uma_Example class attributes and methods

# Namespace class attributes and methods

# uma_Namespace class attributes and methods

# uma_MethodElement class attributes and methods
uma_MethodElement_guid: Property = Property(name="guid", type=StringType)
uma_MethodElement_briefDescription: Property = Property(name="briefDescription", type=StringType)
uma_MethodElement_suppressed: Property = Property(name="suppressed", type=StringType)
uma_MethodElement_orderingGuide: Property = Property(name="orderingGuide", type=StringType)
uma_MethodElement.attributes={uma_MethodElement_guid, uma_MethodElement_orderingGuide, uma_MethodElement_suppressed, uma_MethodElement_briefDescription}

# uma_Constraint class attributes and methods
uma_Constraint_body: Property = Property(name="body", type=StringType)
uma_Constraint.attributes={uma_Constraint_body}

# uma_MethodElementProperty class attributes and methods
uma_MethodElementProperty_value: Property = Property(name="value", type=StringType)
uma_MethodElementProperty.attributes={uma_MethodElementProperty_value}

# MethodElement class attributes and methods

# uma_ContentElement class attributes and methods

# DescribableElement class attributes and methods

# VariabilityElement class attributes and methods

# uma_SupportingMaterial class attributes and methods

# uma_Concept class attributes and methods

# uma_Checklist class attributes and methods

# uma_Guideline class attributes and methods

# uma_WorkProduct class attributes and methods

# uma_ReusableAsset class attributes and methods

# uma_TermDefinition class attributes and methods

# uma_DescribableElement class attributes and methods
uma_DescribableElement_presentationName: Property = Property(name="presentationName", type=StringType)
uma_DescribableElement_shapeicon: Property = Property(name="shapeicon", type=StringType)
uma_DescribableElement_nodeicon: Property = Property(name="nodeicon", type=StringType)
uma_DescribableElement.attributes={uma_DescribableElement_shapeicon, uma_DescribableElement_nodeicon, uma_DescribableElement_presentationName}

# Classifier class attributes and methods

# uma_ContentDescription class attributes and methods
uma_ContentDescription_mainDescription: Property = Property(name="mainDescription", type=StringType)
uma_ContentDescription_externalId: Property = Property(name="externalId", type=StringType)
uma_ContentDescription_keyConsiderations: Property = Property(name="keyConsiderations", type=StringType)
uma_ContentDescription.attributes={uma_ContentDescription_keyConsiderations, uma_ContentDescription_mainDescription, uma_ContentDescription_externalId}

# MethodUnit class attributes and methods

# uma_Section class attributes and methods
uma_Section_sectionName: Property = Property(name="sectionName", type=StringType)
uma_Section_sectionDescription: Property = Property(name="sectionDescription", type=StringType)
uma_Section.attributes={uma_Section_sectionName, uma_Section_sectionDescription}

# uma_Role class attributes and methods

# ContentElement class attributes and methods

# Section class attributes and methods

# uma_Report class attributes and methods

# uma_Template class attributes and methods

# uma_ToolMentor class attributes and methods

# uma_EstimationConsiderations class attributes and methods

# uma_Task class attributes and methods

# WorkDefinition class attributes and methods

# uma_Step class attributes and methods

# uma_WorkDefinition class attributes and methods

# uma_WorkProductDescription class attributes and methods
uma_WorkProductDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_WorkProductDescription_impactOfNotHaving: Property = Property(name="impactOfNotHaving", type=StringType)
uma_WorkProductDescription_reasonsForNotNeeding: Property = Property(name="reasonsForNotNeeding", type=StringType)
uma_WorkProductDescription.attributes={uma_WorkProductDescription_purpose, uma_WorkProductDescription_impactOfNotHaving, uma_WorkProductDescription_reasonsForNotNeeding}

# ContentDescription class attributes and methods

# uma_Guidance class attributes and methods

# uma_Artifact class attributes and methods

# WorkProduct class attributes and methods

# uma_Deliverable class attributes and methods

# uma_Outcome class attributes and methods

# uma_MethodPackage class attributes and methods
uma_MethodPackage_global: Property = Property(name="global", type=StringType)
uma_MethodPackage.attributes={uma_MethodPackage_global}

# Package class attributes and methods

# uma_ContentPackage class attributes and methods

# MethodPackage class attributes and methods

# uma_ArtifactDescription class attributes and methods
uma_ArtifactDescription_representation: Property = Property(name="representation", type=StringType)
uma_ArtifactDescription_notation: Property = Property(name="notation", type=StringType)
uma_ArtifactDescription_briefOutline: Property = Property(name="briefOutline", type=StringType)
uma_ArtifactDescription_representationOptions: Property = Property(name="representationOptions", type=StringType)
uma_ArtifactDescription.attributes={uma_ArtifactDescription_representationOptions, uma_ArtifactDescription_representation, uma_ArtifactDescription_briefOutline, uma_ArtifactDescription_notation}

# WorkProductDescription class attributes and methods

# uma_DeliverableDescription class attributes and methods
uma_DeliverableDescription_externalDescription: Property = Property(name="externalDescription", type=StringType)
uma_DeliverableDescription_packagingGuidance: Property = Property(name="packagingGuidance", type=StringType)
uma_DeliverableDescription.attributes={uma_DeliverableDescription_externalDescription, uma_DeliverableDescription_packagingGuidance}

# uma_RoleDescription class attributes and methods
uma_RoleDescription_skills: Property = Property(name="skills", type=StringType)
uma_RoleDescription_assignmentApproaches: Property = Property(name="assignmentApproaches", type=StringType)
uma_RoleDescription_synonyms: Property = Property(name="synonyms", type=StringType)
uma_RoleDescription.attributes={uma_RoleDescription_synonyms, uma_RoleDescription_assignmentApproaches, uma_RoleDescription_skills}

# uma_TaskDescription class attributes and methods
uma_TaskDescription_purpose: Property = Property(name="purpose", type=StringType)
uma_TaskDescription_alternatives: Property = Property(name="alternatives", type=StringType)
uma_TaskDescription.attributes={uma_TaskDescription_alternatives, uma_TaskDescription_purpose}

# uma_GuidanceDescription class attributes and methods
uma_GuidanceDescription_attachments: Property = Property(name="attachments", type=StringType)
uma_GuidanceDescription.attributes={uma_GuidanceDescription_attachments}

# uma_PracticeDescription class attributes and methods
uma_PracticeDescription_goals: Property = Property(name="goals", type=StringType)
uma_PracticeDescription_additionalInfo: Property = Property(name="additionalInfo", type=StringType)
uma_PracticeDescription_problem: Property = Property(name="problem", type=StringType)
uma_PracticeDescription_background: Property = Property(name="background", type=StringType)
uma_PracticeDescription_application: Property = Property(name="application", type=StringType)
uma_PracticeDescription_levelsOfAdoption: Property = Property(name="levelsOfAdoption", type=StringType)
uma_PracticeDescription.attributes={uma_PracticeDescription_levelsOfAdoption, uma_PracticeDescription_application, uma_PracticeDescription_additionalInfo, uma_PracticeDescription_goals, uma_PracticeDescription_background, uma_PracticeDescription_problem}

# uma_GraphEdge class attributes and methods

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

# uma_GraphConnector class attributes and methods

# uma_SemanticModelBridge class attributes and methods
uma_SemanticModelBridge_presentation: Property = Property(name="presentation", type=StringType)
uma_SemanticModelBridge.attributes={uma_SemanticModelBridge_presentation}

# uma_Reference class attributes and methods
uma_Reference_isIndividualRepresentation: Property = Property(name="isIndividualRepresentation", type=StringType)
uma_Reference.attributes={uma_Reference_isIndividualRepresentation}

# uma_Property class attributes and methods
uma_Property_key: Property = Property(name="key", type=StringType)
uma_Property_value: Property = Property(name="value", type=StringType)
uma_Property.attributes={uma_Property_value, uma_Property_key}

# uma_Diagram class attributes and methods
uma_Diagram_zoom: Property = Property(name="zoom", type=StringType)
uma_Diagram.attributes={uma_Diagram_zoom}

# GraphElement class attributes and methods

# uma_CoreSemanticModelBridge class attributes and methods

# uma_Dimension class attributes and methods
uma_Dimension_width: Property = Property(name="width", type=StringType)
uma_Dimension_height: Property = Property(name="height", type=StringType)
uma_Dimension.attributes={uma_Dimension_width, uma_Dimension_height}

# GraphNode class attributes and methods

# uma_GraphNode class attributes and methods

# uma_SimpleSemanticModelElement class attributes and methods
uma_SimpleSemanticModelElement_typeInfo: Property = Property(name="typeInfo", type=StringType)
uma_SimpleSemanticModelElement.attributes={uma_SimpleSemanticModelElement_typeInfo}

# SemanticModelBridge class attributes and methods

# uma_UMASemanticModelBridge class attributes and methods

# uma_LeafElement class attributes and methods

# uma_TextElement class attributes and methods
uma_TextElement_text: Property = Property(name="text", type=StringType)
uma_TextElement.attributes={uma_TextElement_text}

# LeafElement class attributes and methods

# uma_Image class attributes and methods
uma_Image_uri: Property = Property(name="uri", type=StringType)
uma_Image_mimeType: Property = Property(name="mimeType", type=StringType)
uma_Image.attributes={uma_Image_mimeType, uma_Image_uri}

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
uma_Ellipse.attributes={uma_Ellipse_startAngle, uma_Ellipse_radiusX, uma_Ellipse_endAngle, uma_Ellipse_rotation, uma_Ellipse_radiusY}

# uma_Activity class attributes and methods
uma_Activity_isEnactable: Property = Property(name="isEnactable", type=StringType)
uma_Activity.attributes={uma_Activity_isEnactable}

# WorkBreakdownElement class attributes and methods

# uma_BreakdownElement class attributes and methods
uma_BreakdownElement_prefix: Property = Property(name="prefix", type=StringType)
uma_BreakdownElement_isPlanned: Property = Property(name="isPlanned", type=StringType)
uma_BreakdownElement_hasMultipleOccurrences: Property = Property(name="hasMultipleOccurrences", type=StringType)
uma_BreakdownElement_isOptional: Property = Property(name="isOptional", type=StringType)
uma_BreakdownElement.attributes={uma_BreakdownElement_isOptional, uma_BreakdownElement_hasMultipleOccurrences, uma_BreakdownElement_isPlanned, uma_BreakdownElement_prefix}

# uma_Roadmap class attributes and methods

# uma_RoleDescriptor class attributes and methods

# uma_WorkBreakdownElement class attributes and methods
uma_WorkBreakdownElement_isRepeatable: Property = Property(name="isRepeatable", type=StringType)
uma_WorkBreakdownElement_isOngoing: Property = Property(name="isOngoing", type=StringType)
uma_WorkBreakdownElement_isEventDriven: Property = Property(name="isEventDriven", type=StringType)
uma_WorkBreakdownElement.attributes={uma_WorkBreakdownElement_isRepeatable, uma_WorkBreakdownElement_isOngoing, uma_WorkBreakdownElement_isEventDriven}

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

# Descriptor class attributes and methods

# uma_WorkProductDescriptor class attributes and methods
uma_WorkProductDescriptor_activityEntryState: Property = Property(name="activityEntryState", type=StringType)
uma_WorkProductDescriptor_activityExitState: Property = Property(name="activityExitState", type=StringType)
uma_WorkProductDescriptor.attributes={uma_WorkProductDescriptor_activityEntryState, uma_WorkProductDescriptor_activityExitState}

# uma_ProcessElement class attributes and methods

# uma_Descriptor class attributes and methods
uma_Descriptor_isSynchronizedWithSource: Property = Property(name="isSynchronizedWithSource", type=StringType)
uma_Descriptor.attributes={uma_Descriptor_isSynchronizedWithSource}

# uma_BreakdownElementDescription class attributes and methods
uma_BreakdownElementDescription_usageGuidance: Property = Property(name="usageGuidance", type=StringType)
uma_BreakdownElementDescription.attributes={uma_BreakdownElementDescription_usageGuidance}

# uma_TaskDescriptor class attributes and methods

# uma_CompositeRole class attributes and methods

# RoleDescriptor class attributes and methods

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
uma_DeliveryProcessDescription.attributes={uma_DeliveryProcessDescription_typeOfContract, uma_DeliveryProcessDescription_projectCharacteristics, uma_DeliveryProcessDescription_riskLevel, uma_DeliveryProcessDescription_estimatingTechnique, uma_DeliveryProcessDescription_scale, uma_DeliveryProcessDescription_projectMemberExpertise}

# ProcessDescription class attributes and methods

# uma_ProcessDescription class attributes and methods
uma_ProcessDescription_scope: Property = Property(name="scope", type=StringType)
uma_ProcessDescription_usageNotes: Property = Property(name="usageNotes", type=StringType)
uma_ProcessDescription.attributes={uma_ProcessDescription_usageNotes, uma_ProcessDescription_scope}

# ActivityDescription class attributes and methods

# uma_DescriptorDescription class attributes and methods
uma_DescriptorDescription_refinedDescription: Property = Property(name="refinedDescription", type=StringType)
uma_DescriptorDescription.attributes={uma_DescriptorDescription_refinedDescription}

# Guidance class attributes and methods

# uma_Transition class attributes and methods

# uma_Whitepaper class attributes and methods

# Concept class attributes and methods

# uma_Practice class attributes and methods

# uma_State class attributes and methods

# Vertex class attributes and methods

# uma_Region class attributes and methods

# uma_StateMachine class attributes and methods

# uma_Vertex class attributes and methods

# uma_ContentCategory class attributes and methods

# uma_RoleSet class attributes and methods

# uma_PseudoState class attributes and methods

# uma_Discipline class attributes and methods

# ContentCategory class attributes and methods

# uma_CustomCategory class attributes and methods

# uma_Domain class attributes and methods

# uma_WorkProductType class attributes and methods

# uma_DisciplineGrouping class attributes and methods

# uma_Tool class attributes and methods

# uma_ProcessPackage class attributes and methods

# uma_RoleSetGrouping class attributes and methods

# uma_DeliveryProcess class attributes and methods

# Process class attributes and methods

# uma_Process class attributes and methods

# uma_CapabilityPattern class attributes and methods

# uma_MethodConfiguration class attributes and methods

# uma_ProcessPlanningTemplate class attributes and methods

# uma_ProcessComponent class attributes and methods

# ProcessPackage class attributes and methods

# uma_ProcessComponentInterface class attributes and methods

# uma_ProcessComponentDescriptor class attributes and methods

# uma_MethodPlugin class attributes and methods
uma_MethodPlugin_userChangeable: Property = Property(name="userChangeable", type=StringType)
uma_MethodPlugin.attributes={uma_MethodPlugin_userChangeable}

# uma_MethodUnit class attributes and methods
uma_MethodUnit_authors: Property = Property(name="authors", type=StringType)
uma_MethodUnit_changeDate: Property = Property(name="changeDate", type=StringType)
uma_MethodUnit_changeDescription: Property = Property(name="changeDescription", type=StringType)
uma_MethodUnit_version: Property = Property(name="version", type=StringType)
uma_MethodUnit.attributes={uma_MethodUnit_version, uma_MethodUnit_authors, uma_MethodUnit_changeDate, uma_MethodUnit_changeDescription}

# uma_VariabilityElement class attributes and methods
uma_VariabilityElement_variabilityType: Property = Property(name="variabilityType", type=StringType)
uma_VariabilityElement.attributes={uma_VariabilityElement_variabilityType}

# uma_ProcessFamily class attributes and methods

# MethodConfiguration class attributes and methods

# uma_MethodLibrary class attributes and methods

# Relationships
examples10: BinaryAssociation = BinaryAssociation(
    name="examples10",
    ends={
        Property(name="uma_Example", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement11", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRules0: BinaryAssociation = BinaryAssociation(
    name="ownedRules0",
    ends={
        Property(name="uma_Constraint", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement", type=uma_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodElementProperty1: BinaryAssociation = BinaryAssociation(
    name="methodElementProperty1",
    ends={
        Property(name="uma_MethodElementProperty", type=uma_MethodElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodElement2", type=uma_MethodElementProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportingMaterials3: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials3",
    ends={
        Property(name="uma_SupportingMaterial", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
conceptsAndPapers4: BinaryAssociation = BinaryAssociation(
    name="conceptsAndPapers4",
    ends={
        Property(name="uma_Concept", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement5", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
checklists6: BinaryAssociation = BinaryAssociation(
    name="checklists6",
    ends={
        Property(name="uma_Checklist", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement7", type=uma_Checklist, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines8: BinaryAssociation = BinaryAssociation(
    name="guidelines8",
    ends={
        Property(name="uma_Guideline", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement9", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
modifies25: BinaryAssociation = BinaryAssociation(
    name="modifies25",
    ends={
        Property(name="uma_WorkProduct", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
assets12: BinaryAssociation = BinaryAssociation(
    name="assets12",
    ends={
        Property(name="uma_ReusableAsset", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement13", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor26: BinaryAssociation = BinaryAssociation(
    name="responsibleFor26",
    ends={
        Property(name="uma_WorkProduct28", type=uma_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Role27", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
termDefinition14: BinaryAssociation = BinaryAssociation(
    name="termDefinition14",
    ends={
        Property(name="uma_TermDefinition", type=uma_ContentElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentElement15", type=uma_TermDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
presentation16: BinaryAssociation = BinaryAssociation(
    name="presentation16",
    ends={
        Property(name="uma_ContentDescription", type=uma_DescribableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DescribableElement", type=uma_ContentDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections17: BinaryAssociation = BinaryAssociation(
    name="sections17",
    ends={
        Property(name="uma_Section", type=uma_ContentDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentDescription18", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subSections20: BinaryAssociation = BinaryAssociation(
    name="subSections20",
    ends={
        Property(name="uma_Section21", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section19", type=uma_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor23: BinaryAssociation = BinaryAssociation(
    name="predecessor23",
    ends={
        Property(name="uma_Section24", type=uma_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Section22", type=uma_Section, multiplicity=Multiplicity(0, 1))
    }
)
postcondition61: BinaryAssociation = BinaryAssociation(
    name="postcondition61",
    ends={
        Property(name="uma_Constraint63", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition62", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reports29: BinaryAssociation = BinaryAssociation(
    name="reports29",
    ends={
        Property(name="uma_Report", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct30", type=uma_Report, multiplicity=Multiplicity(0, 9999))
    }
)
templates31: BinaryAssociation = BinaryAssociation(
    name="templates31",
    ends={
        Property(name="uma_Template", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct32", type=uma_Template, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors33: BinaryAssociation = BinaryAssociation(
    name="toolMentors33",
    ends={
        Property(name="uma_ToolMentor", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct34", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
estimationConsiderations35: BinaryAssociation = BinaryAssociation(
    name="estimationConsiderations35",
    ends={
        Property(name="uma_EstimationConsiderations", type=uma_WorkProduct, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProduct36", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 9999))
    }
)
performedBy37: BinaryAssociation = BinaryAssociation(
    name="performedBy37",
    ends={
        Property(name="uma_Role38", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task", type=uma_Role, multiplicity=Multiplicity(0, 1))
    }
)
mandatoryInput39: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput39",
    ends={
        Property(name="uma_WorkProduct41", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task40", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
output42: BinaryAssociation = BinaryAssociation(
    name="output42",
    ends={
        Property(name="uma_WorkProduct44", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task43", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
additionallyPerformedBy45: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy45",
    ends={
        Property(name="uma_Role47", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task46", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput48: BinaryAssociation = BinaryAssociation(
    name="optionalInput48",
    ends={
        Property(name="uma_WorkProduct50", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task49", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
steps51: BinaryAssociation = BinaryAssociation(
    name="steps51",
    ends={
        Property(name="uma_Step", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task52", type=uma_Step, multiplicity=Multiplicity(0, 9999))
    }
)
toolMentors53: BinaryAssociation = BinaryAssociation(
    name="toolMentors53",
    ends={
        Property(name="uma_ToolMentor55", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task54", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
estimationConsiderations56: BinaryAssociation = BinaryAssociation(
    name="estimationConsiderations56",
    ends={
        Property(name="uma_EstimationConsiderations58", type=uma_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Task57", type=uma_EstimationConsiderations, multiplicity=Multiplicity(0, 9999))
    }
)
precondition59: BinaryAssociation = BinaryAssociation(
    name="precondition59",
    ends={
        Property(name="uma_Constraint60", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkDefinition", type=uma_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerArtifact65: BinaryAssociation = BinaryAssociation(
    name="containerArtifact65",
    ends={
        Property(name="Artifact", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containedArtifacts", type=uma_Artifact, multiplicity=Multiplicity(0, 1))
    }
)
containedArtifacts67: BinaryAssociation = BinaryAssociation(
    name="containedArtifacts67",
    ends={
        Property(name="Artifact68", type=uma_Artifact, multiplicity=Multiplicity(1, 1)),
        Property(name="containerArtifact", type=uma_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deliveredWorkProducts69: BinaryAssociation = BinaryAssociation(
    name="deliveredWorkProducts69",
    ends={
        Property(name="uma_WorkProduct70", type=uma_Deliverable, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Deliverable", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
reusedPackages72: BinaryAssociation = BinaryAssociation(
    name="reusedPackages72",
    ends={
        Property(name="uma_MethodPackage", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage71", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999))
    }
)
childPackages74: BinaryAssociation = BinaryAssociation(
    name="childPackages74",
    ends={
        Property(name="uma_MethodPackage75", type=uma_MethodPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPackage73", type=uma_MethodPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentElements76: BinaryAssociation = BinaryAssociation(
    name="contentElements76",
    ends={
        Property(name="uma_ContentElement77", type=uma_ContentPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ContentPackage", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphElement93: BinaryAssociation = BinaryAssociation(
    name="graphElement93",
    ends={
        Property(name="GraphElement94", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchorage", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
graphEdge95: BinaryAssociation = BinaryAssociation(
    name="graphEdge95",
    ends={
        Property(name="GraphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="anchor", type=uma_GraphEdge, multiplicity=Multiplicity(0, 9999))
    }
)
position78: BinaryAssociation = BinaryAssociation(
    name="position78",
    ends={
        Property(name="uma_Point", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphElement", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contained79: BinaryAssociation = BinaryAssociation(
    name="contained79",
    ends={
        Property(name="DiagramElement", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uma_DiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link80: BinaryAssociation = BinaryAssociation(
    name="link80",
    ends={
        Property(name="DiagramLink", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anchorage81: BinaryAssociation = BinaryAssociation(
    name="anchorage81",
    ends={
        Property(name="GraphConnector", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement82", type=uma_GraphConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semanticModel83: BinaryAssociation = BinaryAssociation(
    name="semanticModel83",
    ends={
        Property(name="SemanticModelBridge", type=uma_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphElement84", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container85: BinaryAssociation = BinaryAssociation(
    name="container85",
    ends={
        Property(name="GraphElement", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contained", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
reference86: BinaryAssociation = BinaryAssociation(
    name="reference86",
    ends={
        Property(name="Reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referenced", type=uma_Reference, multiplicity=Multiplicity(0, 9999))
    }
)
property87: BinaryAssociation = BinaryAssociation(
    name="property87",
    ends={
        Property(name="uma_Property", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramElement", type=uma_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
viewport88: BinaryAssociation = BinaryAssociation(
    name="viewport88",
    ends={
        Property(name="uma_Point89", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DiagramLink", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphElement90: BinaryAssociation = BinaryAssociation(
    name="graphElement90",
    ends={
        Property(name="GraphElement91", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=uma_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
diagram92: BinaryAssociation = BinaryAssociation(
    name="diagram92",
    ends={
        Property(name="Diagram", type=uma_DiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="diagramLink", type=uma_Diagram, multiplicity=Multiplicity(1, 1))
    }
)
element114: BinaryAssociation = BinaryAssociation(
    name="element114",
    ends={
        Property(name="uma_MethodElement115", type=uma_UMASemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_UMASemanticModelBridge", type=uma_MethodElement, multiplicity=Multiplicity(1, 1))
    }
)
graphElement96: BinaryAssociation = BinaryAssociation(
    name="graphElement96",
    ends={
        Property(name="GraphElement97", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="semanticModel", type=uma_GraphElement, multiplicity=Multiplicity(0, 1))
    }
)
diagram98: BinaryAssociation = BinaryAssociation(
    name="diagram98",
    ends={
        Property(name="Diagram99", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=uma_Diagram, multiplicity=Multiplicity(0, 1))
    }
)
referenced100: BinaryAssociation = BinaryAssociation(
    name="referenced100",
    ends={
        Property(name="DiagramElement101", type=uma_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="reference", type=uma_DiagramElement, multiplicity=Multiplicity(1, 1))
    }
)
anchor102: BinaryAssociation = BinaryAssociation(
    name="anchor102",
    ends={
        Property(name="GraphConnector103", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphEdge", type=uma_GraphConnector, multiplicity=Multiplicity(2, 2))
    }
)
waypoints104: BinaryAssociation = BinaryAssociation(
    name="waypoints104",
    ends={
        Property(name="uma_Point105", type=uma_GraphEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphEdge", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
viewpoint106: BinaryAssociation = BinaryAssociation(
    name="viewpoint106",
    ends={
        Property(name="uma_Point107", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Diagram", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramLink108: BinaryAssociation = BinaryAssociation(
    name="diagramLink108",
    ends={
        Property(name="DiagramLink109", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram", type=uma_DiagramLink, multiplicity=Multiplicity(0, 9999))
    }
)
namespace110: BinaryAssociation = BinaryAssociation(
    name="namespace110",
    ends={
        Property(name="SemanticModelBridge112", type=uma_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="diagram111", type=uma_SemanticModelBridge, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size113: BinaryAssociation = BinaryAssociation(
    name="size113",
    ends={
        Property(name="uma_Dimension", type=uma_GraphNode, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_GraphNode", type=uma_Dimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusableAssets138: BinaryAssociation = BinaryAssociation(
    name="reusableAssets138",
    ends={
        Property(name="uma_ReusableAsset140", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity139", type=uma_ReusableAsset, multiplicity=Multiplicity(0, 9999))
    }
)
element116: BinaryAssociation = BinaryAssociation(
    name="element116",
    ends={
        Property(name="uma_Element", type=uma_CoreSemanticModelBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CoreSemanticModelBridge", type=uma_Element, multiplicity=Multiplicity(1, 1))
    }
)
waypoints117: BinaryAssociation = BinaryAssociation(
    name="waypoints117",
    ends={
        Property(name="uma_Point118", type=uma_Polyline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Polyline", type=uma_Point, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
center119: BinaryAssociation = BinaryAssociation(
    name="center119",
    ends={
        Property(name="uma_Point120", type=uma_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Ellipse", type=uma_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakdownElements121: BinaryAssociation = BinaryAssociation(
    name="breakdownElements121",
    ends={
        Property(name="BreakdownElement", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="superActivities", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 9999))
    }
)
roadmaps122: BinaryAssociation = BinaryAssociation(
    name="roadmaps122",
    ends={
        Property(name="uma_Roadmap", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity", type=uma_Roadmap, multiplicity=Multiplicity(0, 9999))
    }
)
supportingMaterials123: BinaryAssociation = BinaryAssociation(
    name="supportingMaterials123",
    ends={
        Property(name="uma_SupportingMaterial125", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity124", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
checklists126: BinaryAssociation = BinaryAssociation(
    name="checklists126",
    ends={
        Property(name="uma_Checklist128", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity127", type=uma_Checklist, multiplicity=Multiplicity(0, 9999))
    }
)
concepts129: BinaryAssociation = BinaryAssociation(
    name="concepts129",
    ends={
        Property(name="uma_Concept131", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity130", type=uma_Concept, multiplicity=Multiplicity(0, 9999))
    }
)
examples132: BinaryAssociation = BinaryAssociation(
    name="examples132",
    ends={
        Property(name="uma_Example134", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity133", type=uma_Example, multiplicity=Multiplicity(0, 9999))
    }
)
guidelines135: BinaryAssociation = BinaryAssociation(
    name="guidelines135",
    ends={
        Property(name="uma_Guideline137", type=uma_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Activity136", type=uma_Guideline, multiplicity=Multiplicity(0, 9999))
    }
)
teamRoles150: BinaryAssociation = BinaryAssociation(
    name="teamRoles150",
    ends={
        Property(name="uma_RoleDescriptor", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TeamProfile", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
superTeam152: BinaryAssociation = BinaryAssociation(
    name="superTeam152",
    ends={
        Property(name="TeamProfile", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="subTeam", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1))
    }
)
linkToPredecessor141: BinaryAssociation = BinaryAssociation(
    name="linkToPredecessor141",
    ends={
        Property(name="uma_WorkOrder", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkBreakdownElement", type=uma_WorkOrder, multiplicity=Multiplicity(0, 9999))
    }
)
presentedAfter143: BinaryAssociation = BinaryAssociation(
    name="presentedAfter143",
    ends={
        Property(name="uma_BreakdownElement", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement142", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
presentedBefore145: BinaryAssociation = BinaryAssociation(
    name="presentedBefore145",
    ends={
        Property(name="uma_BreakdownElement146", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement144", type=uma_BreakdownElement, multiplicity=Multiplicity(0, 1))
    }
)
planningData147: BinaryAssociation = BinaryAssociation(
    name="planningData147",
    ends={
        Property(name="uma_PlanningData", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_BreakdownElement148", type=uma_PlanningData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superActivities149: BinaryAssociation = BinaryAssociation(
    name="superActivities149",
    ends={
        Property(name="Activity", type=uma_BreakdownElement, multiplicity=Multiplicity(1, 1)),
        Property(name="breakdownElements", type=uma_Activity, multiplicity=Multiplicity(1, 1))
    }
)
subTeam154: BinaryAssociation = BinaryAssociation(
    name="subTeam154",
    ends={
        Property(name="TeamProfile155", type=uma_TeamProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="superTeam", type=uma_TeamProfile, multiplicity=Multiplicity(0, 9999))
    }
)
Role156: BinaryAssociation = BinaryAssociation(
    name="Role156",
    ends={
        Property(name="uma_Role158", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor157", type=uma_Role, multiplicity=Multiplicity(0, 1))
    }
)
modifies159: BinaryAssociation = BinaryAssociation(
    name="modifies159",
    ends={
        Property(name="uma_WorkProductDescriptor", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor160", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
responsibleFor161: BinaryAssociation = BinaryAssociation(
    name="responsibleFor161",
    ends={
        Property(name="uma_WorkProductDescriptor163", type=uma_RoleDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleDescriptor162", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
pred164: BinaryAssociation = BinaryAssociation(
    name="pred164",
    ends={
        Property(name="uma_WorkBreakdownElement166", type=uma_WorkOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkOrder165", type=uma_WorkBreakdownElement, multiplicity=Multiplicity(1, 1))
    }
)
aggregatedRoles204: BinaryAssociation = BinaryAssociation(
    name="aggregatedRoles204",
    ends={
        Property(name="uma_Role205", type=uma_CompositeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CompositeRole", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
WorkProduct167: BinaryAssociation = BinaryAssociation(
    name="WorkProduct167",
    ends={
        Property(name="uma_WorkProduct169", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor168", type=uma_WorkProduct, multiplicity=Multiplicity(0, 1))
    }
)
impactedBy171: BinaryAssociation = BinaryAssociation(
    name="impactedBy171",
    ends={
        Property(name="WorkProductDescriptor", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
impacts173: BinaryAssociation = BinaryAssociation(
    name="impacts173",
    ends={
        Property(name="WorkProductDescriptor174", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="impactedBy", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
deliverableParts176: BinaryAssociation = BinaryAssociation(
    name="deliverableParts176",
    ends={
        Property(name="uma_WorkProductDescriptor177", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductDescriptor175", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
Task178: BinaryAssociation = BinaryAssociation(
    name="Task178",
    ends={
        Property(name="uma_Task179", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor", type=uma_Task, multiplicity=Multiplicity(0, 1))
    }
)
additionallyPerformedBy180: BinaryAssociation = BinaryAssociation(
    name="additionallyPerformedBy180",
    ends={
        Property(name="uma_RoleDescriptor182", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor181", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
assistedBy183: BinaryAssociation = BinaryAssociation(
    name="assistedBy183",
    ends={
        Property(name="uma_RoleDescriptor185", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor184", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
externalInput186: BinaryAssociation = BinaryAssociation(
    name="externalInput186",
    ends={
        Property(name="uma_WorkProductDescriptor188", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor187", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
mandatoryInput189: BinaryAssociation = BinaryAssociation(
    name="mandatoryInput189",
    ends={
        Property(name="uma_WorkProductDescriptor191", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor190", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
optionalInput192: BinaryAssociation = BinaryAssociation(
    name="optionalInput192",
    ends={
        Property(name="uma_WorkProductDescriptor194", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor193", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
output195: BinaryAssociation = BinaryAssociation(
    name="output195",
    ends={
        Property(name="uma_WorkProductDescriptor197", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor196", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999))
    }
)
performedPrimarilyBy198: BinaryAssociation = BinaryAssociation(
    name="performedPrimarilyBy198",
    ends={
        Property(name="uma_RoleDescriptor200", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor199", type=uma_RoleDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
selectedSteps201: BinaryAssociation = BinaryAssociation(
    name="selectedSteps201",
    ends={
        Property(name="uma_Section203", type=uma_TaskDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_TaskDescriptor202", type=uma_Section, multiplicity=Multiplicity(0, 9999))
    }
)
container219: BinaryAssociation = BinaryAssociation(
    name="container219",
    ends={
        Property(name="Region220", type=uma_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="Vertex", type=uma_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing221: BinaryAssociation = BinaryAssociation(
    name="outgoing221",
    ends={
        Property(name="Transition", type=uma_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=uma_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming222: BinaryAssociation = BinaryAssociation(
    name="incoming222",
    ends={
        Property(name="Transition223", type=uma_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=uma_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
Vertex224: BinaryAssociation = BinaryAssociation(
    name="Vertex224",
    ends={
        Property(name="Vertex226", type=uma_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container225", type=uma_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subPractices207: BinaryAssociation = BinaryAssociation(
    name="subPractices207",
    ends={
        Property(name="uma_Practice", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice206", type=uma_Practice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentReferences208: BinaryAssociation = BinaryAssociation(
    name="contentReferences208",
    ends={
        Property(name="uma_ContentElement210", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice209", type=uma_ContentElement, multiplicity=Multiplicity(0, 9999))
    }
)
activityReferences211: BinaryAssociation = BinaryAssociation(
    name="activityReferences211",
    ends={
        Property(name="uma_Activity213", type=uma_Practice, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Practice212", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
WorkProduct214: BinaryAssociation = BinaryAssociation(
    name="WorkProduct214",
    ends={
        Property(name="uma_WorkProduct215", type=uma_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_State", type=uma_WorkProduct, multiplicity=Multiplicity(1, 9999))
    }
)
Region216: BinaryAssociation = BinaryAssociation(
    name="Region216",
    ends={
        Property(name="Region", type=uma_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State", type=uma_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine217: BinaryAssociation = BinaryAssociation(
    name="submachine217",
    ends={
        Property(name="uma_StateMachine", type=uma_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_State218", type=uma_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
referenceWorkflows252: BinaryAssociation = BinaryAssociation(
    name="referenceWorkflows252",
    ends={
        Property(name="uma_Activity254", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline253", type=uma_Activity, multiplicity=Multiplicity(0, 9999))
    }
)
Transition227: BinaryAssociation = BinaryAssociation(
    name="Transition227",
    ends={
        Property(name="Transition229", type=uma_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container228", type=uma_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
State230: BinaryAssociation = BinaryAssociation(
    name="State230",
    ends={
        Property(name="State232", type=uma_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="Region231", type=uma_State, multiplicity=Multiplicity(0, 1))
    }
)
StateMachine233: BinaryAssociation = BinaryAssociation(
    name="StateMachine233",
    ends={
        Property(name="StateMachine", type=uma_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="Region234", type=uma_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
Region235: BinaryAssociation = BinaryAssociation(
    name="Region235",
    ends={
        Property(name="Region237", type=uma_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine236", type=uma_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
WorkDefinition238: BinaryAssociation = BinaryAssociation(
    name="WorkDefinition238",
    ends={
        Property(name="uma_WorkDefinition239", type=uma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Transition", type=uma_WorkDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
container240: BinaryAssociation = BinaryAssociation(
    name="container240",
    ends={
        Property(name="Region242", type=uma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Transition241", type=uma_Region, multiplicity=Multiplicity(1, 1))
    }
)
source243: BinaryAssociation = BinaryAssociation(
    name="source243",
    ends={
        Property(name="Vertex244", type=uma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=uma_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target245: BinaryAssociation = BinaryAssociation(
    name="target245",
    ends={
        Property(name="Vertex246", type=uma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=uma_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
tasks247: BinaryAssociation = BinaryAssociation(
    name="tasks247",
    ends={
        Property(name="uma_Task248", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline", type=uma_Task, multiplicity=Multiplicity(0, 9999))
    }
)
subdiscipline250: BinaryAssociation = BinaryAssociation(
    name="subdiscipline250",
    ends={
        Property(name="uma_Discipline251", type=uma_Discipline, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Discipline249", type=uma_Discipline, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roleSets268: BinaryAssociation = BinaryAssociation(
    name="roleSets268",
    ends={
        Property(name="uma_RoleSet269", type=uma_RoleSetGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSetGrouping", type=uma_RoleSet, multiplicity=Multiplicity(0, 9999))
    }
)
roles255: BinaryAssociation = BinaryAssociation(
    name="roles255",
    ends={
        Property(name="uma_Role256", type=uma_RoleSet, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_RoleSet", type=uma_Role, multiplicity=Multiplicity(0, 9999))
    }
)
workProducts257: BinaryAssociation = BinaryAssociation(
    name="workProducts257",
    ends={
        Property(name="uma_WorkProduct258", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
subdomains260: BinaryAssociation = BinaryAssociation(
    name="subdomains260",
    ends={
        Property(name="uma_Domain261", type=uma_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Domain259", type=uma_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workProducts262: BinaryAssociation = BinaryAssociation(
    name="workProducts262",
    ends={
        Property(name="uma_WorkProduct263", type=uma_WorkProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_WorkProductType", type=uma_WorkProduct, multiplicity=Multiplicity(0, 9999))
    }
)
disciplines264: BinaryAssociation = BinaryAssociation(
    name="disciplines264",
    ends={
        Property(name="uma_Discipline265", type=uma_DisciplineGrouping, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DisciplineGrouping", type=uma_Discipline, multiplicity=Multiplicity(0, 9999))
    }
)
process288: BinaryAssociation = BinaryAssociation(
    name="process288",
    ends={
        Property(name="uma_ProcessComponent289", type=uma_Process, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="uma_Process290", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
toolMentors266: BinaryAssociation = BinaryAssociation(
    name="toolMentors266",
    ends={
        Property(name="uma_ToolMentor267", type=uma_Tool, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Tool", type=uma_ToolMentor, multiplicity=Multiplicity(0, 9999))
    }
)
categorizedElements270: BinaryAssociation = BinaryAssociation(
    name="categorizedElements270",
    ends={
        Property(name="uma_DescribableElement271", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory", type=uma_DescribableElement, multiplicity=Multiplicity(0, 9999))
    }
)
subCategories272: BinaryAssociation = BinaryAssociation(
    name="subCategories272",
    ends={
        Property(name="uma_ContentCategory", type=uma_CustomCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_CustomCategory273", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
educationMaterials274: BinaryAssociation = BinaryAssociation(
    name="educationMaterials274",
    ends={
        Property(name="uma_SupportingMaterial275", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DeliveryProcess", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
communicationsMaterials276: BinaryAssociation = BinaryAssociation(
    name="communicationsMaterials276",
    ends={
        Property(name="uma_SupportingMaterial278", type=uma_DeliveryProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_DeliveryProcess277", type=uma_SupportingMaterial, multiplicity=Multiplicity(0, 9999))
    }
)
includesPatterns279: BinaryAssociation = BinaryAssociation(
    name="includesPatterns279",
    ends={
        Property(name="uma_CapabilityPattern", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process", type=uma_CapabilityPattern, multiplicity=Multiplicity(0, 9999))
    }
)
defaultContext280: BinaryAssociation = BinaryAssociation(
    name="defaultContext280",
    ends={
        Property(name="uma_MethodConfiguration", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process281", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1))
    }
)
validContext282: BinaryAssociation = BinaryAssociation(
    name="validContext282",
    ends={
        Property(name="uma_MethodConfiguration284", type=uma_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_Process283", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
basedOnProcesses285: BinaryAssociation = BinaryAssociation(
    name="basedOnProcesses285",
    ends={
        Property(name="uma_Process286", type=uma_ProcessPlanningTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPlanningTemplate", type=uma_Process, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces287: BinaryAssociation = BinaryAssociation(
    name="interfaces287",
    ends={
        Property(name="uma_ProcessComponentInterface", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponent", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 9999))
    }
)
processElements291: BinaryAssociation = BinaryAssociation(
    name="processElements291",
    ends={
        Property(name="uma_ProcessElement", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage", type=uma_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams292: BinaryAssociation = BinaryAssociation(
    name="diagrams292",
    ends={
        Property(name="uma_Diagram294", type=uma_ProcessPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessPackage293", type=uma_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceSpecifications295: BinaryAssociation = BinaryAssociation(
    name="interfaceSpecifications295",
    ends={
        Property(name="uma_TaskDescriptor297", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface296", type=uma_TaskDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceIO298: BinaryAssociation = BinaryAssociation(
    name="interfaceIO298",
    ends={
        Property(name="uma_WorkProductDescriptor300", type=uma_ProcessComponentInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentInterface299", type=uma_WorkProductDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ProcessComponent301: BinaryAssociation = BinaryAssociation(
    name="ProcessComponent301",
    ends={
        Property(name="uma_ProcessComponent302", type=uma_ProcessComponentDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessComponentDescriptor", type=uma_ProcessComponent, multiplicity=Multiplicity(1, 1))
    }
)
methodPackages303: BinaryAssociation = BinaryAssociation(
    name="methodPackages303",
    ends={
        Property(name="uma_MethodPackage304", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
copyrightStatement310: BinaryAssociation = BinaryAssociation(
    name="copyrightStatement310",
    ends={
        Property(name="uma_SupportingMaterial311", type=uma_MethodUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodUnit", type=uma_SupportingMaterial, multiplicity=Multiplicity(1, 1))
    }
)
methodPluginSelection312: BinaryAssociation = BinaryAssociation(
    name="methodPluginSelection312",
    ends={
        Property(name="uma_MethodPlugin314", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration313", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 9999))
    }
)
methodPackageSelection315: BinaryAssociation = BinaryAssociation(
    name="methodPackageSelection315",
    ends={
        Property(name="uma_MethodPackage317", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration316", type=uma_MethodPackage, multiplicity=Multiplicity(1, 9999))
    }
)
processViews318: BinaryAssociation = BinaryAssociation(
    name="processViews318",
    ends={
        Property(name="uma_ContentCategory320", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration319", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
defaultView321: BinaryAssociation = BinaryAssociation(
    name="defaultView321",
    ends={
        Property(name="uma_ContentCategory323", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration322", type=uma_ContentCategory, multiplicity=Multiplicity(1, 1))
    }
)
baseConfigurations325: BinaryAssociation = BinaryAssociation(
    name="baseConfigurations325",
    ends={
        Property(name="uma_MethodConfiguration326", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration324", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999))
    }
)
bases306: BinaryAssociation = BinaryAssociation(
    name="bases306",
    ends={
        Property(name="uma_MethodPlugin307", type=uma_MethodPlugin, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodPlugin305", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999))
    }
)
variabilityBasedOnElement309: BinaryAssociation = BinaryAssociation(
    name="variabilityBasedOnElement309",
    ends={
        Property(name="uma_VariabilityElement", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_VariabilityElement308", type=uma_VariabilityElement, multiplicity=Multiplicity(1, 1))
    }
)
predefinedConfigurations337: BinaryAssociation = BinaryAssociation(
    name="predefinedConfigurations337",
    ends={
        Property(name="uma_MethodConfiguration339", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary338", type=uma_MethodConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subtractedCategory327: BinaryAssociation = BinaryAssociation(
    name="subtractedCategory327",
    ends={
        Property(name="uma_ContentCategory329", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration328", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
addedCategory330: BinaryAssociation = BinaryAssociation(
    name="addedCategory330",
    ends={
        Property(name="uma_ContentCategory332", type=uma_MethodConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodConfiguration331", type=uma_ContentCategory, multiplicity=Multiplicity(0, 9999))
    }
)
deliveryProcesses333: BinaryAssociation = BinaryAssociation(
    name="deliveryProcesses333",
    ends={
        Property(name="uma_DeliveryProcess334", type=uma_ProcessFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_ProcessFamily", type=uma_DeliveryProcess, multiplicity=Multiplicity(0, 9999))
    }
)
methodPlugins335: BinaryAssociation = BinaryAssociation(
    name="methodPlugins335",
    ends={
        Property(name="uma_MethodPlugin336", type=uma_MethodLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="uma_MethodLibrary", type=uma_MethodPlugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uma_Classifier_Type = Generalization(general=Type, specific=uma_Classifier)
gen_uma_Type_PackageableElement = Generalization(general=PackageableElement, specific=uma_Type)
gen_uma_NamedElement_Element = Generalization(general=Element, specific=uma_NamedElement)
gen_uma_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=uma_PackageableElement)
gen_uma_Package_Namespace = Generalization(general=Namespace, specific=uma_Package)
gen_uma_Package_PackageableElement = Generalization(general=PackageableElement, specific=uma_Package)
gen_uma_Namespace_NamedElement = Generalization(general=NamedElement, specific=uma_Namespace)
gen_uma_MethodElement_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElement)
gen_uma_Constraint_MethodElement = Generalization(general=MethodElement, specific=uma_Constraint)
gen_uma_MethodElementProperty_PackageableElement = Generalization(general=PackageableElement, specific=uma_MethodElementProperty)
gen_uma_ContentElement_DescribableElement = Generalization(general=DescribableElement, specific=uma_ContentElement)
gen_uma_ContentElement_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_ContentElement)
gen_uma_WorkProduct_ContentElement = Generalization(general=ContentElement, specific=uma_WorkProduct)
gen_uma_DescribableElement_MethodElement = Generalization(general=MethodElement, specific=uma_DescribableElement)
gen_uma_DescribableElement_Classifier = Generalization(general=Classifier, specific=uma_DescribableElement)
gen_uma_ContentDescription_MethodUnit = Generalization(general=MethodUnit, specific=uma_ContentDescription)
gen_uma_Section_VariabilityElement = Generalization(general=VariabilityElement, specific=uma_Section)
gen_uma_Role_ContentElement = Generalization(general=ContentElement, specific=uma_Role)
gen_uma_Step_Section = Generalization(general=Section, specific=uma_Step)
gen_uma_Step_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Step)
gen_uma_Task_ContentElement = Generalization(general=ContentElement, specific=uma_Task)
gen_uma_Task_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_Task)
gen_uma_WorkDefinition_MethodElement = Generalization(general=MethodElement, specific=uma_WorkDefinition)
gen_uma_WorkProductDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_WorkProductDescription)
gen_uma_Guidance_ContentElement = Generalization(general=ContentElement, specific=uma_Guidance)
gen_uma_Artifact_WorkProduct = Generalization(general=WorkProduct, specific=uma_Artifact)
gen_uma_Deliverable_WorkProduct = Generalization(general=WorkProduct, specific=uma_Deliverable)
gen_uma_Outcome_WorkProduct = Generalization(general=WorkProduct, specific=uma_Outcome)
gen_uma_MethodPackage_MethodElement = Generalization(general=MethodElement, specific=uma_MethodPackage)
gen_uma_MethodPackage_Package = Generalization(general=Package, specific=uma_MethodPackage)
gen_uma_ContentPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ContentPackage)
gen_uma_ArtifactDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_ArtifactDescription)
gen_uma_DeliverableDescription_WorkProductDescription = Generalization(general=WorkProductDescription, specific=uma_DeliverableDescription)
gen_uma_RoleDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_RoleDescription)
gen_uma_TaskDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_TaskDescription)
gen_uma_GuidanceDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_GuidanceDescription)
gen_uma_PracticeDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_PracticeDescription)
gen_uma_GraphElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_GraphElement)
gen_uma_DiagramElement_MethodElement = Generalization(general=MethodElement, specific=uma_DiagramElement)
gen_uma_DiagramLink_DiagramElement = Generalization(general=DiagramElement, specific=uma_DiagramLink)
gen_uma_GraphConnector_GraphElement = Generalization(general=GraphElement, specific=uma_GraphConnector)
gen_uma_CoreSemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_CoreSemanticModelBridge)
gen_uma_SemanticModelBridge_DiagramElement = Generalization(general=DiagramElement, specific=uma_SemanticModelBridge)
gen_uma_Reference_DiagramElement = Generalization(general=DiagramElement, specific=uma_Reference)
gen_uma_Property_DiagramElement = Generalization(general=DiagramElement, specific=uma_Property)
gen_uma_GraphEdge_GraphElement = Generalization(general=GraphElement, specific=uma_GraphEdge)
gen_uma_Diagram_GraphNode = Generalization(general=GraphNode, specific=uma_Diagram)
gen_uma_GraphNode_GraphElement = Generalization(general=GraphElement, specific=uma_GraphNode)
gen_uma_SimpleSemanticModelElement_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_SimpleSemanticModelElement)
gen_uma_UMASemanticModelBridge_SemanticModelBridge = Generalization(general=SemanticModelBridge, specific=uma_UMASemanticModelBridge)
gen_uma_LeafElement_DiagramElement = Generalization(general=DiagramElement, specific=uma_LeafElement)
gen_uma_TextElement_LeafElement = Generalization(general=LeafElement, specific=uma_TextElement)
gen_uma_Image_LeafElement = Generalization(general=LeafElement, specific=uma_Image)
gen_uma_GraphicPrimitive_LeafElement = Generalization(general=LeafElement, specific=uma_GraphicPrimitive)
gen_uma_Polyline_GraphicPrimitive = Generalization(general=GraphicPrimitive, specific=uma_Polyline)
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
gen_uma_WorkProductDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_WorkProductDescriptor)
gen_uma_BreakdownElementDescription_ContentDescription = Generalization(general=ContentDescription, specific=uma_BreakdownElementDescription)
gen_uma_TaskDescriptor_WorkBreakdownElement = Generalization(general=WorkBreakdownElement, specific=uma_TaskDescriptor)
gen_uma_TaskDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_TaskDescriptor)
gen_uma_CompositeRole_RoleDescriptor = Generalization(general=RoleDescriptor, specific=uma_CompositeRole)
gen_uma_Guideline_Guidance = Generalization(general=Guidance, specific=uma_Guideline)
gen_uma_Report_Guidance = Generalization(general=Guidance, specific=uma_Report)
gen_uma_ActivityDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_ActivityDescription)
gen_uma_DeliveryProcessDescription_ProcessDescription = Generalization(general=ProcessDescription, specific=uma_DeliveryProcessDescription)
gen_uma_ProcessDescription_ActivityDescription = Generalization(general=ActivityDescription, specific=uma_ProcessDescription)
gen_uma_DescriptorDescription_BreakdownElementDescription = Generalization(general=BreakdownElementDescription, specific=uma_DescriptorDescription)
gen_uma_Concept_Guidance = Generalization(general=Guidance, specific=uma_Concept)
gen_uma_Checklist_Guidance = Generalization(general=Guidance, specific=uma_Checklist)
gen_uma_Example_Guidance = Generalization(general=Guidance, specific=uma_Example)
gen_uma_Template_Guidance = Generalization(general=Guidance, specific=uma_Template)
gen_uma_SupportingMaterial_Guidance = Generalization(general=Guidance, specific=uma_SupportingMaterial)
gen_uma_ToolMentor_Guidance = Generalization(general=Guidance, specific=uma_ToolMentor)
gen_uma_Whitepaper_Concept = Generalization(general=Concept, specific=uma_Whitepaper)
gen_uma_TermDefinition_Guidance = Generalization(general=Guidance, specific=uma_TermDefinition)
gen_uma_Practice_Guidance = Generalization(general=Guidance, specific=uma_Practice)
gen_uma_EstimationConsiderations_Guidance = Generalization(general=Guidance, specific=uma_EstimationConsiderations)
gen_uma_ReusableAsset_Guidance = Generalization(general=Guidance, specific=uma_ReusableAsset)
gen_uma_State_Vertex = Generalization(general=Vertex, specific=uma_State)
gen_uma_ContentCategory_ContentElement = Generalization(general=ContentElement, specific=uma_ContentCategory)
gen_uma_RoleSet_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSet)
gen_uma_StateMachine_WorkDefinition = Generalization(general=WorkDefinition, specific=uma_StateMachine)
gen_uma_PseudoState_Vertex = Generalization(general=Vertex, specific=uma_PseudoState)
gen_uma_Discipline_ContentCategory = Generalization(general=ContentCategory, specific=uma_Discipline)
gen_uma_Domain_ContentCategory = Generalization(general=ContentCategory, specific=uma_Domain)
gen_uma_WorkProductType_ContentCategory = Generalization(general=ContentCategory, specific=uma_WorkProductType)
gen_uma_DisciplineGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_DisciplineGrouping)
gen_uma_Tool_ContentCategory = Generalization(general=ContentCategory, specific=uma_Tool)
gen_uma_ProcessPackage_MethodPackage = Generalization(general=MethodPackage, specific=uma_ProcessPackage)
gen_uma_RoleSetGrouping_ContentCategory = Generalization(general=ContentCategory, specific=uma_RoleSetGrouping)
gen_uma_CustomCategory_ContentCategory = Generalization(general=ContentCategory, specific=uma_CustomCategory)
gen_uma_DeliveryProcess_Process = Generalization(general=Process, specific=uma_DeliveryProcess)
gen_uma_Process_Activity = Generalization(general=Activity, specific=uma_Process)
gen_uma_CapabilityPattern_Process = Generalization(general=Process, specific=uma_CapabilityPattern)
gen_uma_ProcessPlanningTemplate_Process = Generalization(general=Process, specific=uma_ProcessPlanningTemplate)
gen_uma_Roadmap_Guidance = Generalization(general=Guidance, specific=uma_Roadmap)
gen_uma_ProcessComponent_ProcessPackage = Generalization(general=ProcessPackage, specific=uma_ProcessComponent)
gen_uma_ProcessComponent_MethodUnit = Generalization(general=MethodUnit, specific=uma_ProcessComponent)
gen_uma_ProcessComponentInterface_BreakdownElement = Generalization(general=BreakdownElement, specific=uma_ProcessComponentInterface)
gen_uma_ProcessComponentDescriptor_Descriptor = Generalization(general=Descriptor, specific=uma_ProcessComponentDescriptor)
gen_uma_MethodPlugin_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodPlugin)
gen_uma_MethodPlugin_Package = Generalization(general=Package, specific=uma_MethodPlugin)
gen_uma_MethodUnit_MethodElement = Generalization(general=MethodElement, specific=uma_MethodUnit)
gen_uma_MethodConfiguration_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodConfiguration)
gen_uma_VariabilityElement_MethodElement = Generalization(general=MethodElement, specific=uma_VariabilityElement)
gen_uma_ProcessFamily_MethodConfiguration = Generalization(general=MethodConfiguration, specific=uma_ProcessFamily)
gen_uma_MethodLibrary_MethodUnit = Generalization(general=MethodUnit, specific=uma_MethodLibrary)
gen_uma_MethodLibrary_Package = Generalization(general=Package, specific=uma_MethodLibrary)

# Domain Model
domain_model = DomainModel(
    name="uma",
    types={uma_Package, uma_Classifier, Type, uma_Type, PackageableElement, uma_Element, uma_NamedElement, Element, uma_PackageableElement, NamedElement, uma_Example, Namespace, uma_Namespace, uma_MethodElement, uma_Constraint, uma_MethodElementProperty, MethodElement, uma_ContentElement, DescribableElement, VariabilityElement, uma_SupportingMaterial, uma_Concept, uma_Checklist, uma_Guideline, uma_WorkProduct, uma_ReusableAsset, uma_TermDefinition, uma_DescribableElement, Classifier, uma_ContentDescription, MethodUnit, uma_Section, uma_Role, ContentElement, Section, uma_Report, uma_Template, uma_ToolMentor, uma_EstimationConsiderations, uma_Task, WorkDefinition, uma_Step, uma_WorkDefinition, uma_WorkProductDescription, ContentDescription, uma_Guidance, uma_Artifact, WorkProduct, uma_Deliverable, uma_Outcome, uma_MethodPackage, Package, uma_ContentPackage, MethodPackage, uma_ArtifactDescription, WorkProductDescription, uma_DeliverableDescription, uma_RoleDescription, uma_TaskDescription, uma_GuidanceDescription, uma_PracticeDescription, uma_GraphEdge, uma_Point, uma_GraphElement, DiagramElement, uma_DiagramElement, uma_DiagramLink, uma_GraphConnector, uma_SemanticModelBridge, uma_Reference, uma_Property, uma_Diagram, GraphElement, uma_CoreSemanticModelBridge, uma_Dimension, GraphNode, uma_GraphNode, uma_SimpleSemanticModelElement, SemanticModelBridge, uma_UMASemanticModelBridge, uma_LeafElement, uma_TextElement, LeafElement, uma_Image, uma_GraphicPrimitive, uma_Polyline, GraphicPrimitive, uma_Ellipse, uma_Activity, WorkBreakdownElement, uma_BreakdownElement, uma_Roadmap, uma_RoleDescriptor, uma_WorkBreakdownElement, BreakdownElement, uma_WorkOrder, ProcessElement, uma_PlanningData, uma_Milestone, uma_Iteration, Activity, uma_Phase, uma_TeamProfile, Descriptor, uma_WorkProductDescriptor, uma_ProcessElement, uma_Descriptor, uma_BreakdownElementDescription, uma_TaskDescriptor, uma_CompositeRole, RoleDescriptor, uma_ActivityDescription, BreakdownElementDescription, uma_DeliveryProcessDescription, ProcessDescription, uma_ProcessDescription, ActivityDescription, uma_DescriptorDescription, Guidance, uma_Transition, uma_Whitepaper, Concept, uma_Practice, uma_State, Vertex, uma_Region, uma_StateMachine, uma_Vertex, uma_ContentCategory, uma_RoleSet, uma_PseudoState, uma_Discipline, ContentCategory, uma_CustomCategory, uma_Domain, uma_WorkProductType, uma_DisciplineGrouping, uma_Tool, uma_ProcessPackage, uma_RoleSetGrouping, uma_DeliveryProcess, Process, uma_Process, uma_CapabilityPattern, uma_MethodConfiguration, uma_ProcessPlanningTemplate, uma_ProcessComponent, ProcessPackage, uma_ProcessComponentInterface, uma_ProcessComponentDescriptor, uma_MethodPlugin, uma_MethodUnit, uma_VariabilityElement, uma_ProcessFamily, MethodConfiguration, uma_MethodLibrary, WorkOrderType, PseudoStateKind, VariabilityType},
    associations={examples10, ownedRules0, methodElementProperty1, supportingMaterials3, conceptsAndPapers4, checklists6, guidelines8, modifies25, assets12, responsibleFor26, termDefinition14, presentation16, sections17, subSections20, predecessor23, postcondition61, reports29, templates31, toolMentors33, estimationConsiderations35, performedBy37, mandatoryInput39, output42, additionallyPerformedBy45, optionalInput48, steps51, toolMentors53, estimationConsiderations56, precondition59, containerArtifact65, containedArtifacts67, deliveredWorkProducts69, reusedPackages72, childPackages74, contentElements76, graphElement93, graphEdge95, position78, contained79, link80, anchorage81, semanticModel83, container85, reference86, property87, viewport88, graphElement90, diagram92, element114, graphElement96, diagram98, referenced100, anchor102, waypoints104, viewpoint106, diagramLink108, namespace110, size113, reusableAssets138, element116, waypoints117, center119, breakdownElements121, roadmaps122, supportingMaterials123, checklists126, concepts129, examples132, guidelines135, teamRoles150, superTeam152, linkToPredecessor141, presentedAfter143, presentedBefore145, planningData147, superActivities149, subTeam154, Role156, modifies159, responsibleFor161, pred164, aggregatedRoles204, WorkProduct167, impactedBy171, impacts173, deliverableParts176, Task178, additionallyPerformedBy180, assistedBy183, externalInput186, mandatoryInput189, optionalInput192, output195, performedPrimarilyBy198, selectedSteps201, container219, outgoing221, incoming222, Vertex224, subPractices207, contentReferences208, activityReferences211, WorkProduct214, Region216, submachine217, referenceWorkflows252, Transition227, State230, StateMachine233, Region235, WorkDefinition238, container240, source243, target245, tasks247, subdiscipline250, roleSets268, roles255, workProducts257, subdomains260, workProducts262, disciplines264, process288, toolMentors266, categorizedElements270, subCategories272, educationMaterials274, communicationsMaterials276, includesPatterns279, defaultContext280, validContext282, basedOnProcesses285, interfaces287, processElements291, diagrams292, interfaceSpecifications295, interfaceIO298, ProcessComponent301, methodPackages303, copyrightStatement310, methodPluginSelection312, methodPackageSelection315, processViews318, defaultView321, baseConfigurations325, bases306, variabilityBasedOnElement309, predefinedConfigurations337, subtractedCategory327, addedCategory330, deliveryProcesses333, methodPlugins335},
    generalizations={gen_uma_Classifier_Type, gen_uma_Type_PackageableElement, gen_uma_NamedElement_Element, gen_uma_PackageableElement_NamedElement, gen_uma_Package_Namespace, gen_uma_Package_PackageableElement, gen_uma_Namespace_NamedElement, gen_uma_MethodElement_PackageableElement, gen_uma_Constraint_MethodElement, gen_uma_MethodElementProperty_PackageableElement, gen_uma_ContentElement_DescribableElement, gen_uma_ContentElement_VariabilityElement, gen_uma_WorkProduct_ContentElement, gen_uma_DescribableElement_MethodElement, gen_uma_DescribableElement_Classifier, gen_uma_ContentDescription_MethodUnit, gen_uma_Section_VariabilityElement, gen_uma_Role_ContentElement, gen_uma_Step_Section, gen_uma_Step_WorkDefinition, gen_uma_Task_ContentElement, gen_uma_Task_WorkDefinition, gen_uma_WorkDefinition_MethodElement, gen_uma_WorkProductDescription_ContentDescription, gen_uma_Guidance_ContentElement, gen_uma_Artifact_WorkProduct, gen_uma_Deliverable_WorkProduct, gen_uma_Outcome_WorkProduct, gen_uma_MethodPackage_MethodElement, gen_uma_MethodPackage_Package, gen_uma_ContentPackage_MethodPackage, gen_uma_ArtifactDescription_WorkProductDescription, gen_uma_DeliverableDescription_WorkProductDescription, gen_uma_RoleDescription_ContentDescription, gen_uma_TaskDescription_ContentDescription, gen_uma_GuidanceDescription_ContentDescription, gen_uma_PracticeDescription_ContentDescription, gen_uma_GraphElement_DiagramElement, gen_uma_DiagramElement_MethodElement, gen_uma_DiagramLink_DiagramElement, gen_uma_GraphConnector_GraphElement, gen_uma_CoreSemanticModelBridge_SemanticModelBridge, gen_uma_SemanticModelBridge_DiagramElement, gen_uma_Reference_DiagramElement, gen_uma_Property_DiagramElement, gen_uma_GraphEdge_GraphElement, gen_uma_Diagram_GraphNode, gen_uma_GraphNode_GraphElement, gen_uma_SimpleSemanticModelElement_SemanticModelBridge, gen_uma_UMASemanticModelBridge_SemanticModelBridge, gen_uma_LeafElement_DiagramElement, gen_uma_TextElement_LeafElement, gen_uma_Image_LeafElement, gen_uma_GraphicPrimitive_LeafElement, gen_uma_Polyline_GraphicPrimitive, gen_uma_Ellipse_GraphicPrimitive, gen_uma_Activity_WorkBreakdownElement, gen_uma_Activity_VariabilityElement, gen_uma_Activity_WorkDefinition, gen_uma_WorkBreakdownElement_BreakdownElement, gen_uma_BreakdownElement_ProcessElement, gen_uma_Milestone_WorkBreakdownElement, gen_uma_Iteration_Activity, gen_uma_Phase_Activity, gen_uma_TeamProfile_BreakdownElement, gen_uma_RoleDescriptor_Descriptor, gen_uma_WorkOrder_ProcessElement, gen_uma_ProcessElement_DescribableElement, gen_uma_PlanningData_ProcessElement, gen_uma_Descriptor_BreakdownElement, gen_uma_WorkProductDescriptor_Descriptor, gen_uma_BreakdownElementDescription_ContentDescription, gen_uma_TaskDescriptor_WorkBreakdownElement, gen_uma_TaskDescriptor_Descriptor, gen_uma_CompositeRole_RoleDescriptor, gen_uma_Guideline_Guidance, gen_uma_Report_Guidance, gen_uma_ActivityDescription_BreakdownElementDescription, gen_uma_DeliveryProcessDescription_ProcessDescription, gen_uma_ProcessDescription_ActivityDescription, gen_uma_DescriptorDescription_BreakdownElementDescription, gen_uma_Concept_Guidance, gen_uma_Checklist_Guidance, gen_uma_Example_Guidance, gen_uma_Template_Guidance, gen_uma_SupportingMaterial_Guidance, gen_uma_ToolMentor_Guidance, gen_uma_Whitepaper_Concept, gen_uma_TermDefinition_Guidance, gen_uma_Practice_Guidance, gen_uma_EstimationConsiderations_Guidance, gen_uma_ReusableAsset_Guidance, gen_uma_State_Vertex, gen_uma_ContentCategory_ContentElement, gen_uma_RoleSet_ContentCategory, gen_uma_StateMachine_WorkDefinition, gen_uma_PseudoState_Vertex, gen_uma_Discipline_ContentCategory, gen_uma_Domain_ContentCategory, gen_uma_WorkProductType_ContentCategory, gen_uma_DisciplineGrouping_ContentCategory, gen_uma_Tool_ContentCategory, gen_uma_ProcessPackage_MethodPackage, gen_uma_RoleSetGrouping_ContentCategory, gen_uma_CustomCategory_ContentCategory, gen_uma_DeliveryProcess_Process, gen_uma_Process_Activity, gen_uma_CapabilityPattern_Process, gen_uma_ProcessPlanningTemplate_Process, gen_uma_Roadmap_Guidance, gen_uma_ProcessComponent_ProcessPackage, gen_uma_ProcessComponent_MethodUnit, gen_uma_ProcessComponentInterface_BreakdownElement, gen_uma_ProcessComponentDescriptor_Descriptor, gen_uma_MethodPlugin_MethodUnit, gen_uma_MethodPlugin_Package, gen_uma_MethodUnit_MethodElement, gen_uma_MethodConfiguration_MethodUnit, gen_uma_VariabilityElement_MethodElement, gen_uma_ProcessFamily_MethodConfiguration, gen_uma_MethodLibrary_MethodUnit, gen_uma_MethodLibrary_Package},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)