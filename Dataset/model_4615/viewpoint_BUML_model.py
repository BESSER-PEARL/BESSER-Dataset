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
FontFormat: Enumeration = Enumeration(
    name="FontFormat",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="italic"),
			EnumerationLiteral(name="bold"),
			EnumerationLiteral(name="bold_italic")
    }
)

SyncStatus: Enumeration = Enumeration(
    name="SyncStatus",
    literals={
            EnumerationLiteral(name="dirty"),
			EnumerationLiteral(name="sync")
    }
)

LabelAlignment: Enumeration = Enumeration(
    name="LabelAlignment",
    literals={
            EnumerationLiteral(name="CENTER"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

NavigationTargetType: Enumeration = Enumeration(
    name="NavigationTargetType",
    literals={
            EnumerationLiteral(name="model"),
			EnumerationLiteral(name="file")
    }
)

Position: Enumeration = Enumeration(
    name="Position",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="WEST"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="NORTH_WEST"),
			EnumerationLiteral(name="NORTH_EAST"),
			EnumerationLiteral(name="SOUTH_WEST"),
			EnumerationLiteral(name="SOUTH_EAST"),
			EnumerationLiteral(name="CENTER")
    }
)

SystemColors: Enumeration = Enumeration(
    name="SystemColors",
    literals={
            EnumerationLiteral(name="dark_red"),
			EnumerationLiteral(name="dark_green"),
			EnumerationLiteral(name="dark_yellow"),
			EnumerationLiteral(name="dark_purple"),
			EnumerationLiteral(name="dark_orange"),
			EnumerationLiteral(name="dark_chocolate"),
			EnumerationLiteral(name="dark_gray"),
			EnumerationLiteral(name="light_blue"),
			EnumerationLiteral(name="light_red"),
			EnumerationLiteral(name="light_green"),
			EnumerationLiteral(name="light_yellow"),
			EnumerationLiteral(name="light_purple"),
			EnumerationLiteral(name="light_orange"),
			EnumerationLiteral(name="light_chocolate"),
			EnumerationLiteral(name="light_gray"),
			EnumerationLiteral(name="black"),
			EnumerationLiteral(name="blue"),
			EnumerationLiteral(name="red"),
			EnumerationLiteral(name="green"),
			EnumerationLiteral(name="yellow"),
			EnumerationLiteral(name="purple"),
			EnumerationLiteral(name="orange"),
			EnumerationLiteral(name="chocolate"),
			EnumerationLiteral(name="gray"),
			EnumerationLiteral(name="white"),
			EnumerationLiteral(name="dark_blue")
    }
)

DragSource: Enumeration = Enumeration(
    name="DragSource",
    literals={
            EnumerationLiteral(name="DIAGRAM"),
			EnumerationLiteral(name="PROJECT_EXPLORER"),
			EnumerationLiteral(name="BOTH")
    }
)

ERROR_LEVEL: Enumeration = Enumeration(
    name="ERROR_LEVEL",
    literals={
            EnumerationLiteral(name="INFO"),
			EnumerationLiteral(name="WARNING"),
			EnumerationLiteral(name="ERROR")
    }
)

# Classes
FeatureExtensionDescription = Class(name="FeatureExtensionDescription")
viewpoint_DValidable = Class(name="viewpoint::DValidable", is_abstract=True)
viewpoint_DAnalysis = Class(name="viewpoint::DAnalysis")
viewpoint_EObject = Class(name="viewpoint::EObject")
DAnnotationEntry = Class(name="DAnnotationEntry")
viewpoint_DView = Class(name="viewpoint::DView")
viewpoint_DFeatureExtension = Class(name="viewpoint::DFeatureExtension", is_abstract=True)
viewpoint_DMappingBased = Class(name="viewpoint::DMappingBased", is_abstract=True)
viewpoint_DContainer = Class(name="viewpoint::DContainer", is_abstract=True)
viewpoint_DRepresentationContainer = Class(name="viewpoint::DRepresentationContainer")
DView = Class(name="DView")
viewpoint_DSemanticDecorator = Class(name="viewpoint::DSemanticDecorator", is_abstract=True)
viewpoint_DNavigable = Class(name="viewpoint::DNavigable", is_abstract=True)
viewpoint_DNavigationLink = Class(name="viewpoint::DNavigationLink", is_abstract=True)
viewpoint_DStylizable = Class(name="viewpoint::DStylizable", is_abstract=True)
viewpoint_DRefreshable = Class(name="viewpoint::DRefreshable", is_abstract=True)
viewpoint_DLabelled = Class(name="viewpoint::DLabelled", is_abstract=True)
viewpoint_MetaModelExtension = Class(name="viewpoint::MetaModelExtension")
viewpoint_DRepresentation = Class(name="viewpoint::DRepresentation", is_abstract=True)
description_DocumentedElement = Class(name="description::DocumentedElement")
DRefreshable = Class(name="DRefreshable")
description_DModelElement = Class(name="description::DModelElement")
viewpoint_DRepresentationElement = Class(name="viewpoint::DRepresentationElement", is_abstract=True)
AnnotationEntry = Class(name="AnnotationEntry")
DLabelled = Class(name="DLabelled")
DMappingBased = Class(name="DMappingBased")
DStylizable = Class(name="DStylizable")
DSemanticDecorator = Class(name="DSemanticDecorator")
viewpoint_DSourceFileLink = Class(name="viewpoint::DSourceFileLink")
DNavigationLink = Class(name="DNavigationLink")
viewpoint_DAnalysisCustomData = Class(name="viewpoint::DAnalysisCustomData")
Viewpoint = Class(name="Viewpoint")
viewpoint_Decoration = Class(name="viewpoint::Decoration")
DecorationDescription = Class(name="DecorationDescription")
viewpoint_LabelStyle = Class(name="viewpoint::LabelStyle")
BasicLabelStyle = Class(name="BasicLabelStyle")
viewpoint_Style = Class(name="viewpoint::Style", is_abstract=True)
Customizable = Class(name="Customizable")
viewpoint_SessionManagerEObject = Class(name="viewpoint::SessionManagerEObject")
style_StyleDescription = Class(name="style::StyleDescription")
viewpoint_DResource = Class(name="viewpoint::DResource", is_abstract=True)
viewpoint_RGBValues = Class(name="viewpoint::RGBValues")
viewpoint_DFile = Class(name="viewpoint::DFile")
DResource = Class(name="DResource")
viewpoint_DResourceContainer = Class(name="viewpoint::DResourceContainer")
viewpoint_DAnalysisSessionEObject = Class(name="viewpoint::DAnalysisSessionEObject")
viewpoint_DProject = Class(name="viewpoint::DProject")
DResourceContainer = Class(name="DResourceContainer")
viewpoint_DFolder = Class(name="viewpoint::DFolder")
viewpoint_DModel = Class(name="viewpoint::DModel")
DFile = Class(name="DFile")
viewpoint_BasicLabelStyle = Class(name="viewpoint::BasicLabelStyle")
viewpoint_Customizable = Class(name="viewpoint::Customizable", is_abstract=True)
viewpoint_description_Group = Class(name="viewpoint::description::Group")
SytemColorsPalette = Class(name="SytemColorsPalette")
UserColorsPalette = Class(name="UserColorsPalette")
validation_ValidationSet = Class(name="validation::ValidationSet")
RepresentationDescription = Class(name="RepresentationDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
JavaExtension = Class(name="JavaExtension")
MetamodelExtensionSetting = Class(name="MetamodelExtensionSetting")
RepresentationTemplate = Class(name="RepresentationTemplate")
viewpoint_description_FeatureExtensionDescription = Class(name="viewpoint::description::FeatureExtensionDescription", is_abstract=True)
viewpoint_description_RepresentationDescription = Class(name="viewpoint::description::RepresentationDescription", is_abstract=True)
description_viewpoint_EPackage = Class(name="description::viewpoint::EPackage")
viewpoint_description_Component = Class(name="viewpoint::description::Component", is_abstract=True)
viewpoint_description_Viewpoint = Class(name="viewpoint::description::Viewpoint")
description_Component = Class(name="description::Component")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
viewpoint_description_RepresentationExtensionDescription = Class(name="viewpoint::description::RepresentationExtensionDescription", is_abstract=True)
viewpoint_description_MetamodelExtensionSetting = Class(name="viewpoint::description::MetamodelExtensionSetting")
description_viewpoint_EObject = Class(name="description::viewpoint::EObject")
viewpoint_description_JavaExtension = Class(name="viewpoint::description::JavaExtension")
viewpoint_description_RepresentationElementMapping = Class(name="viewpoint::description::RepresentationElementMapping", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
viewpoint_description_AbstractMappingImport = Class(name="viewpoint::description::AbstractMappingImport", is_abstract=True)
viewpoint_description_DocumentedElement = Class(name="viewpoint::description::DocumentedElement", is_abstract=True)
viewpoint_description_DModelElement = Class(name="viewpoint::description::DModelElement", is_abstract=True)
DAnnotation = Class(name="DAnnotation")
viewpoint_description_DAnnotation = Class(name="viewpoint::description::DAnnotation")
description_viewpoint_EStringToStringMapEntry = Class(name="description::viewpoint::EStringToStringMapEntry")
viewpoint_description_RepresentationTemplate = Class(name="viewpoint::description::RepresentationTemplate", is_abstract=True)
viewpoint_description_RepresentationImportDescription = Class(name="viewpoint::description::RepresentationImportDescription", is_abstract=True)
viewpoint_description_PasteTargetDescription = Class(name="viewpoint::description::PasteTargetDescription", is_abstract=True)
tool_PasteDescription = Class(name="tool::PasteDescription")
viewpoint_description_DecorationDescriptionsSet = Class(name="viewpoint::description::DecorationDescriptionsSet")
viewpoint_description_DecorationDescription = Class(name="viewpoint::description::DecorationDescription", is_abstract=True)
viewpoint_description_SemanticBasedDecoration = Class(name="viewpoint::description::SemanticBasedDecoration")
viewpoint_description_Customization = Class(name="viewpoint::description::Customization")
IVSMElementCustomization = Class(name="IVSMElementCustomization")
viewpoint_description_ConditionalStyleDescription = Class(name="viewpoint::description::ConditionalStyleDescription", is_abstract=True)
EStructuralFeatureCustomization = Class(name="EStructuralFeatureCustomization")
viewpoint_description_VSMElementCustomizationReuse = Class(name="viewpoint::description::VSMElementCustomizationReuse")
viewpoint_description_EStructuralFeatureCustomization = Class(name="viewpoint::description::EStructuralFeatureCustomization", is_abstract=True)
viewpoint_description_EAttributeCustomization = Class(name="viewpoint::description::EAttributeCustomization")
viewpoint_description_EReferenceCustomization = Class(name="viewpoint::description::EReferenceCustomization")
viewpoint_description_SelectionDescription = Class(name="viewpoint::description::SelectionDescription", is_abstract=True)
viewpoint_description_IVSMElementCustomization = Class(name="viewpoint::description::IVSMElementCustomization", is_abstract=True)
viewpoint_description_VSMElementCustomization = Class(name="viewpoint::description::VSMElementCustomization")
viewpoint_description_SystemColor = Class(name="viewpoint::description::SystemColor")
FixedColor = Class(name="FixedColor")
viewpoint_description_InterpolatedColor = Class(name="viewpoint::description::InterpolatedColor")
description_ColorDescription = Class(name="description::ColorDescription")
description_UserColor = Class(name="description::UserColor")
ColorStep = Class(name="ColorStep")
viewpoint_description_ColorStep = Class(name="viewpoint::description::ColorStep")
viewpoint_description_FixedColor = Class(name="viewpoint::description::FixedColor")
ColorDescription = Class(name="ColorDescription")
viewpoint_description_UserFixedColor = Class(name="viewpoint::description::UserFixedColor")
description_FixedColor = Class(name="description::FixedColor")
viewpoint_description_UserColor = Class(name="viewpoint::description::UserColor", is_abstract=True)
viewpoint_description_ColorDescription = Class(name="viewpoint::description::ColorDescription", is_abstract=True)
viewpoint_description_Environment = Class(name="viewpoint::description::Environment")
tool_ToolEntry = Class(name="tool::ToolEntry")
style_LabelBorderStyles = Class(name="style::LabelBorderStyles")
viewpoint_description_SytemColorsPalette = Class(name="viewpoint::description::SytemColorsPalette")
SystemColor = Class(name="SystemColor")
viewpoint_description_UserColorsPalette = Class(name="viewpoint::description::UserColorsPalette")
UserColor = Class(name="UserColor")
viewpoint_description_AnnotationEntry = Class(name="viewpoint::description::AnnotationEntry")
viewpoint_description_EndUserDocumentedElement = Class(name="viewpoint::description::EndUserDocumentedElement", is_abstract=True)
viewpoint_description_IdentifiedElement = Class(name="viewpoint::description::IdentifiedElement")
viewpoint_description_ComputedColor = Class(name="viewpoint::description::ComputedColor")
viewpoint_description_DAnnotationEntry = Class(name="viewpoint::description::DAnnotationEntry")
viewpoint_style_StyleDescription = Class(name="viewpoint::style::StyleDescription", is_abstract=True)
viewpoint_style_BasicLabelStyleDescription = Class(name="viewpoint::style::BasicLabelStyleDescription")
viewpoint_style_LabelStyleDescription = Class(name="viewpoint::style::LabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
viewpoint_style_LabelBorderStyles = Class(name="viewpoint::style::LabelBorderStyles")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
viewpoint_style_LabelBorderStyleDescription = Class(name="viewpoint::style::LabelBorderStyleDescription")
viewpoint_style_TooltipStyleDescription = Class(name="viewpoint::style::TooltipStyleDescription")
viewpoint_tool_AbstractToolDescription = Class(name="viewpoint::tool::AbstractToolDescription", is_abstract=True)
ToolEntry = Class(name="ToolEntry")
tool_ToolFilterDescription = Class(name="tool::ToolFilterDescription")
viewpoint_tool_MappingBasedToolDescription = Class(name="viewpoint::tool::MappingBasedToolDescription", is_abstract=True)
AbstractToolDescription = Class(name="AbstractToolDescription")
viewpoint_tool_ToolDescription = Class(name="viewpoint::tool::ToolDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_ElementVariable = Class(name="tool::ElementVariable")
tool_ElementViewVariable = Class(name="tool::ElementViewVariable")
tool_InitialOperation = Class(name="tool::InitialOperation")
viewpoint_tool_ToolEntry = Class(name="viewpoint::tool::ToolEntry", is_abstract=True)
viewpoint_tool_PasteDescription = Class(name="viewpoint::tool::PasteDescription")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
viewpoint_tool_SelectionWizardDescription = Class(name="viewpoint::tool::SelectionWizardDescription")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
description_SelectionDescription = Class(name="description::SelectionDescription")
viewpoint_tool_PaneBasedSelectionWizardDescription = Class(name="viewpoint::tool::PaneBasedSelectionWizardDescription")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
tool_SelectContainerVariable = Class(name="tool::SelectContainerVariable")
viewpoint_tool_RepresentationCreationDescription = Class(name="viewpoint::tool::RepresentationCreationDescription", is_abstract=True)
tool_NameVariable = Class(name="tool::NameVariable")
viewpoint_tool_RepresentationNavigationDescription = Class(name="viewpoint::tool::RepresentationNavigationDescription", is_abstract=True)
viewpoint_tool_MenuItemOrRef = Class(name="viewpoint::tool::MenuItemOrRef", is_abstract=True)
viewpoint_tool_MenuItemDescription = Class(name="viewpoint::tool::MenuItemDescription", is_abstract=True)
tool_MenuItemOrRef = Class(name="tool::MenuItemOrRef")
viewpoint_tool_MenuItemDescriptionReference = Class(name="viewpoint::tool::MenuItemDescriptionReference")
MenuItemOrRef = Class(name="MenuItemOrRef")
tool_MenuItemDescription = Class(name="tool::MenuItemDescription")
viewpoint_tool_OperationAction = Class(name="viewpoint::tool::OperationAction")
MenuItemDescription = Class(name="MenuItemDescription")
viewpoint_tool_ExternalJavaAction = Class(name="viewpoint::tool::ExternalJavaAction")
tool_ContainerModelOperation = Class(name="tool::ContainerModelOperation")
tool_ExternalJavaActionParameter = Class(name="tool::ExternalJavaActionParameter")
viewpoint_tool_ExternalJavaActionCall = Class(name="viewpoint::tool::ExternalJavaActionCall")
tool_ExternalJavaAction = Class(name="tool::ExternalJavaAction")
viewpoint_tool_PopupMenu = Class(name="viewpoint::tool::PopupMenu")
tool_VariableContainer = Class(name="tool::VariableContainer")
viewpoint_tool_SubVariable = Class(name="viewpoint::tool::SubVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
viewpoint_tool_DialogVariable = Class(name="viewpoint::tool::DialogVariable", is_abstract=True)
viewpoint_tool_ElementDropVariable = Class(name="viewpoint::tool::ElementDropVariable")
tool_AbstractVariable = Class(name="tool::AbstractVariable")
viewpoint_tool_ElementSelectVariable = Class(name="viewpoint::tool::ElementSelectVariable")
viewpoint_tool_ElementVariable = Class(name="viewpoint::tool::ElementVariable")
viewpoint_tool_ElementViewVariable = Class(name="viewpoint::tool::ElementViewVariable")
viewpoint_tool_ElementDeleteVariable = Class(name="viewpoint::tool::ElementDeleteVariable")
viewpoint_tool_DropContainerVariable = Class(name="viewpoint::tool::DropContainerVariable")
viewpoint_tool_SelectContainerVariable = Class(name="viewpoint::tool::SelectContainerVariable")
viewpoint_tool_ContainerViewVariable = Class(name="viewpoint::tool::ContainerViewVariable")
viewpoint_tool_SelectModelElementVariable = Class(name="viewpoint::tool::SelectModelElementVariable")
viewpoint_tool_EditMaskVariables = Class(name="viewpoint::tool::EditMaskVariables")
viewpoint_tool_ContainerModelOperation = Class(name="viewpoint::tool::ContainerModelOperation", is_abstract=True)
ModelOperation = Class(name="ModelOperation")
tool_ModelOperation = Class(name="tool::ModelOperation")
viewpoint_tool_ModelOperation = Class(name="viewpoint::tool::ModelOperation", is_abstract=True)
viewpoint_tool_InitialNodeCreationOperation = Class(name="viewpoint::tool::InitialNodeCreationOperation")
viewpoint_tool_InitialOperation = Class(name="viewpoint::tool::InitialOperation")
viewpoint_tool_InitEdgeCreationOperation = Class(name="viewpoint::tool::InitEdgeCreationOperation")
viewpoint_tool_InitialContainerDropOperation = Class(name="viewpoint::tool::InitialContainerDropOperation")
viewpoint_tool_AbstractVariable = Class(name="viewpoint::tool::AbstractVariable", is_abstract=True)
viewpoint_tool_VariableContainer = Class(name="viewpoint::tool::VariableContainer", is_abstract=True)
tool_SubVariable = Class(name="tool::SubVariable")
viewpoint_tool_AcceleoVariable = Class(name="viewpoint::tool::AcceleoVariable")
viewpoint_tool_ChangeContext = Class(name="viewpoint::tool::ChangeContext")
viewpoint_tool_SetValue = Class(name="viewpoint::tool::SetValue")
viewpoint_tool_SetObject = Class(name="viewpoint::tool::SetObject")
tool_viewpoint_EObject = Class(name="tool::viewpoint::EObject")
viewpoint_tool_Unset = Class(name="viewpoint::tool::Unset")
viewpoint_tool_MoveElement = Class(name="viewpoint::tool::MoveElement")
viewpoint_tool_CreateInstance = Class(name="viewpoint::tool::CreateInstance")
ContainerModelOperation = Class(name="ContainerModelOperation")
viewpoint_tool_If = Class(name="viewpoint::tool::If")
viewpoint_tool_DeleteView = Class(name="viewpoint::tool::DeleteView")
viewpoint_tool_NameVariable = Class(name="viewpoint::tool::NameVariable")
viewpoint_tool_ExternalJavaActionParameter = Class(name="viewpoint::tool::ExternalJavaActionParameter")
viewpoint_tool_ToolFilterDescription = Class(name="viewpoint::tool::ToolFilterDescription")
tool_FeatureChangeListener = Class(name="tool::FeatureChangeListener")
viewpoint_tool_RemoveElement = Class(name="viewpoint::tool::RemoveElement")
viewpoint_tool_For = Class(name="viewpoint::tool::For")
viewpoint_tool_SwitchChild = Class(name="viewpoint::tool::SwitchChild", is_abstract=True)
viewpoint_tool_Default = Class(name="viewpoint::tool::Default")
viewpoint_tool_Switch = Class(name="viewpoint::tool::Switch")
tool_Case = Class(name="tool::Case")
tool_Default = Class(name="tool::Default")
viewpoint_validation_ValidationSet = Class(name="viewpoint::validation::ValidationSet")
DocumentedElement = Class(name="DocumentedElement")
validation_ValidationRule = Class(name="validation::ValidationRule")
viewpoint_validation_ValidationRule = Class(name="viewpoint::validation::ValidationRule", is_abstract=True)
viewpoint_tool_FeatureChangeListener = Class(name="viewpoint::tool::FeatureChangeListener")
viewpoint_tool_Case = Class(name="viewpoint::tool::Case")
SwitchChild = Class(name="SwitchChild")
viewpoint_validation_SemanticValidationRule = Class(name="viewpoint::validation::SemanticValidationRule")
ValidationRule = Class(name="ValidationRule")
viewpoint_validation_ViewValidationRule = Class(name="viewpoint::validation::ViewValidationRule")
RepresentationElementMapping = Class(name="RepresentationElementMapping")
viewpoint_validation_RuleAudit = Class(name="viewpoint::validation::RuleAudit")
viewpoint_validation_ValidationFix = Class(name="viewpoint::validation::ValidationFix")
viewpoint_audit_InformationSection = Class(name="viewpoint::audit::InformationSection", is_abstract=True)
viewpoint_audit_TemplateInformationSection = Class(name="viewpoint::audit::TemplateInformationSection")
InformationSection = Class(name="InformationSection")
validation_RuleAudit = Class(name="validation::RuleAudit")
validation_ValidationFix = Class(name="validation::ValidationFix")

# FeatureExtensionDescription class attributes and methods

# viewpoint_DValidable class attributes and methods
viewpoint_DValidable_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
viewpoint_DValidable.methods={viewpoint_DValidable_m_validate}

# viewpoint_DAnalysis class attributes and methods
viewpoint_DAnalysis_version: Property = Property(name="version", type=StringType)
viewpoint_DAnalysis.attributes={viewpoint_DAnalysis_version}

# viewpoint_EObject class attributes and methods

# DAnnotationEntry class attributes and methods

# viewpoint_DView class attributes and methods
viewpoint_DView_initialized: Property = Property(name="initialized", type=BooleanType)
viewpoint_DView.attributes={viewpoint_DView_initialized}

# viewpoint_DFeatureExtension class attributes and methods

# viewpoint_DMappingBased class attributes and methods
viewpoint_DMappingBased_m_getMapping: Method = Method(name="getMapping", parameters={}, type=StringType)
viewpoint_DMappingBased.methods={viewpoint_DMappingBased_m_getMapping}

# viewpoint_DContainer class attributes and methods

# viewpoint_DRepresentationContainer class attributes and methods

# DView class attributes and methods

# viewpoint_DSemanticDecorator class attributes and methods

# viewpoint_DNavigable class attributes and methods

# viewpoint_DNavigationLink class attributes and methods
viewpoint_DNavigationLink_targetType: Property = Property(name="targetType", type=StringType)
viewpoint_DNavigationLink_label: Property = Property(name="label", type=StringType)
viewpoint_DNavigationLink_m_isAvailable: Method = Method(name="isAvailable", parameters={}, type=BooleanType)
viewpoint_DNavigationLink.attributes={viewpoint_DNavigationLink_label, viewpoint_DNavigationLink_targetType}
viewpoint_DNavigationLink.methods={viewpoint_DNavigationLink_m_isAvailable}

# viewpoint_DStylizable class attributes and methods
viewpoint_DStylizable_m_getStyle: Method = Method(name="getStyle", parameters={}, type=StringType)
viewpoint_DStylizable.methods={viewpoint_DStylizable_m_getStyle}

# viewpoint_DRefreshable class attributes and methods
viewpoint_DRefreshable_m_refresh: Method = Method(name="refresh", parameters={})
viewpoint_DRefreshable.methods={viewpoint_DRefreshable_m_refresh}

# viewpoint_DLabelled class attributes and methods

# viewpoint_MetaModelExtension class attributes and methods

# viewpoint_DRepresentation class attributes and methods
viewpoint_DRepresentation_name: Property = Property(name="name", type=StringType)
viewpoint_DRepresentation.attributes={viewpoint_DRepresentation_name}

# description_DocumentedElement class attributes and methods

# DRefreshable class attributes and methods

# description_DModelElement class attributes and methods

# viewpoint_DRepresentationElement class attributes and methods
viewpoint_DRepresentationElement_name: Property = Property(name="name", type=StringType)
viewpoint_DRepresentationElement.attributes={viewpoint_DRepresentationElement_name}

# AnnotationEntry class attributes and methods

# DLabelled class attributes and methods

# DMappingBased class attributes and methods

# DStylizable class attributes and methods

# DSemanticDecorator class attributes and methods

# viewpoint_DSourceFileLink class attributes and methods
viewpoint_DSourceFileLink_filePath: Property = Property(name="filePath", type=StringType)
viewpoint_DSourceFileLink_startPosition: Property = Property(name="startPosition", type=IntegerType)
viewpoint_DSourceFileLink_endPosition: Property = Property(name="endPosition", type=IntegerType)
viewpoint_DSourceFileLink.attributes={viewpoint_DSourceFileLink_endPosition, viewpoint_DSourceFileLink_filePath, viewpoint_DSourceFileLink_startPosition}

# DNavigationLink class attributes and methods

# viewpoint_DAnalysisCustomData class attributes and methods
viewpoint_DAnalysisCustomData_key: Property = Property(name="key", type=StringType)
viewpoint_DAnalysisCustomData.attributes={viewpoint_DAnalysisCustomData_key}

# Viewpoint class attributes and methods

# viewpoint_Decoration class attributes and methods

# DecorationDescription class attributes and methods

# viewpoint_LabelStyle class attributes and methods
viewpoint_LabelStyle_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
viewpoint_LabelStyle.attributes={viewpoint_LabelStyle_labelAlignment}

# BasicLabelStyle class attributes and methods

# viewpoint_Style class attributes and methods

# Customizable class attributes and methods

# viewpoint_SessionManagerEObject class attributes and methods

# style_StyleDescription class attributes and methods

# viewpoint_DResource class attributes and methods
viewpoint_DResource_name: Property = Property(name="name", type=StringType)
viewpoint_DResource_path: Property = Property(name="path", type=StringType)
viewpoint_DResource.attributes={viewpoint_DResource_name, viewpoint_DResource_path}

# viewpoint_RGBValues class attributes and methods
viewpoint_RGBValues_red: Property = Property(name="red", type=IntegerType)
viewpoint_RGBValues_green: Property = Property(name="green", type=IntegerType)
viewpoint_RGBValues_blue: Property = Property(name="blue", type=IntegerType)
viewpoint_RGBValues.attributes={viewpoint_RGBValues_blue, viewpoint_RGBValues_red, viewpoint_RGBValues_green}

# viewpoint_DFile class attributes and methods

# DResource class attributes and methods

# viewpoint_DResourceContainer class attributes and methods

# viewpoint_DAnalysisSessionEObject class attributes and methods
viewpoint_DAnalysisSessionEObject_synchronizationStatus: Property = Property(name="synchronizationStatus", type=StringType)
viewpoint_DAnalysisSessionEObject_open: Property = Property(name="open", type=BooleanType)
viewpoint_DAnalysisSessionEObject_blocked: Property = Property(name="blocked", type=BooleanType)
viewpoint_DAnalysisSessionEObject_resources: Property = Property(name="resources", type=StringType)
viewpoint_DAnalysisSessionEObject_controlledResources: Property = Property(name="controlledResources", type=StringType)
viewpoint_DAnalysisSessionEObject.attributes={viewpoint_DAnalysisSessionEObject_resources, viewpoint_DAnalysisSessionEObject_controlledResources, viewpoint_DAnalysisSessionEObject_blocked, viewpoint_DAnalysisSessionEObject_synchronizationStatus, viewpoint_DAnalysisSessionEObject_open}

# viewpoint_DProject class attributes and methods

# DResourceContainer class attributes and methods

# viewpoint_DFolder class attributes and methods

# viewpoint_DModel class attributes and methods

# DFile class attributes and methods

# viewpoint_BasicLabelStyle class attributes and methods
viewpoint_BasicLabelStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
viewpoint_BasicLabelStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
viewpoint_BasicLabelStyle_showIcon: Property = Property(name="showIcon", type=BooleanType)
viewpoint_BasicLabelStyle_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_BasicLabelStyle.attributes={viewpoint_BasicLabelStyle_labelFormat, viewpoint_BasicLabelStyle_showIcon, viewpoint_BasicLabelStyle_iconPath, viewpoint_BasicLabelStyle_labelSize}

# viewpoint_Customizable class attributes and methods
viewpoint_Customizable_customFeatures: Property = Property(name="customFeatures", type=StringType)
viewpoint_Customizable.attributes={viewpoint_Customizable_customFeatures}

# viewpoint_description_Group class attributes and methods
viewpoint_description_Group_name: Property = Property(name="name", type=StringType)
viewpoint_description_Group_version: Property = Property(name="version", type=StringType)
viewpoint_description_Group.attributes={viewpoint_description_Group_name, viewpoint_description_Group_version}

# SytemColorsPalette class attributes and methods

# UserColorsPalette class attributes and methods

# validation_ValidationSet class attributes and methods

# RepresentationDescription class attributes and methods

# RepresentationExtensionDescription class attributes and methods

# JavaExtension class attributes and methods

# MetamodelExtensionSetting class attributes and methods

# RepresentationTemplate class attributes and methods

# viewpoint_description_FeatureExtensionDescription class attributes and methods

# viewpoint_description_RepresentationDescription class attributes and methods
viewpoint_description_RepresentationDescription_titleExpression: Property = Property(name="titleExpression", type=StringType)
viewpoint_description_RepresentationDescription_initialisation: Property = Property(name="initialisation", type=BooleanType)
viewpoint_description_RepresentationDescription_showOnStartup: Property = Property(name="showOnStartup", type=BooleanType)
viewpoint_description_RepresentationDescription.attributes={viewpoint_description_RepresentationDescription_showOnStartup, viewpoint_description_RepresentationDescription_initialisation, viewpoint_description_RepresentationDescription_titleExpression}

# description_viewpoint_EPackage class attributes and methods

# viewpoint_description_Component class attributes and methods

# viewpoint_description_Viewpoint class attributes and methods
viewpoint_description_Viewpoint_modelFileExtension: Property = Property(name="modelFileExtension", type=StringType)
viewpoint_description_Viewpoint_icon: Property = Property(name="icon", type=StringType)
viewpoint_description_Viewpoint_conflicts: Property = Property(name="conflicts", type=StringType)
viewpoint_description_Viewpoint_reuses: Property = Property(name="reuses", type=StringType)
viewpoint_description_Viewpoint_customizes: Property = Property(name="customizes", type=StringType)
viewpoint_description_Viewpoint_m_initView: Method = Method(name="initView", parameters={Parameter(name='model')})
viewpoint_description_Viewpoint.attributes={viewpoint_description_Viewpoint_conflicts, viewpoint_description_Viewpoint_reuses, viewpoint_description_Viewpoint_customizes, viewpoint_description_Viewpoint_modelFileExtension, viewpoint_description_Viewpoint_icon}
viewpoint_description_Viewpoint.methods={viewpoint_description_Viewpoint_m_initView}

# description_Component class attributes and methods

# description_EndUserDocumentedElement class attributes and methods

# description_IdentifiedElement class attributes and methods

# viewpoint_description_RepresentationExtensionDescription class attributes and methods
viewpoint_description_RepresentationExtensionDescription_name: Property = Property(name="name", type=StringType)
viewpoint_description_RepresentationExtensionDescription_viewpointURI: Property = Property(name="viewpointURI", type=StringType)
viewpoint_description_RepresentationExtensionDescription_representationName: Property = Property(name="representationName", type=StringType)
viewpoint_description_RepresentationExtensionDescription.attributes={viewpoint_description_RepresentationExtensionDescription_name, viewpoint_description_RepresentationExtensionDescription_viewpointURI, viewpoint_description_RepresentationExtensionDescription_representationName}

# viewpoint_description_MetamodelExtensionSetting class attributes and methods

# description_viewpoint_EObject class attributes and methods

# viewpoint_description_JavaExtension class attributes and methods
viewpoint_description_JavaExtension_qualifiedClassName: Property = Property(name="qualifiedClassName", type=StringType)
viewpoint_description_JavaExtension.attributes={viewpoint_description_JavaExtension_qualifiedClassName}

# viewpoint_description_RepresentationElementMapping class attributes and methods

# IdentifiedElement class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# viewpoint_description_AbstractMappingImport class attributes and methods
viewpoint_description_AbstractMappingImport_hideSubMappings: Property = Property(name="hideSubMappings", type=BooleanType)
viewpoint_description_AbstractMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
viewpoint_description_AbstractMappingImport.attributes={viewpoint_description_AbstractMappingImport_inheritsAncestorFilters, viewpoint_description_AbstractMappingImport_hideSubMappings}

# viewpoint_description_DocumentedElement class attributes and methods
viewpoint_description_DocumentedElement_documentation: Property = Property(name="documentation", type=StringType)
viewpoint_description_DocumentedElement.attributes={viewpoint_description_DocumentedElement_documentation}

# viewpoint_description_DModelElement class attributes and methods
viewpoint_description_DModelElement_m_getDAnnotation: Method = Method(name="getDAnnotation", parameters={Parameter(name='source')}, type=StringType)
viewpoint_description_DModelElement.methods={viewpoint_description_DModelElement_m_getDAnnotation}

# DAnnotation class attributes and methods

# viewpoint_description_DAnnotation class attributes and methods
viewpoint_description_DAnnotation_source: Property = Property(name="source", type=StringType)
viewpoint_description_DAnnotation.attributes={viewpoint_description_DAnnotation_source}

# description_viewpoint_EStringToStringMapEntry class attributes and methods

# viewpoint_description_RepresentationTemplate class attributes and methods
viewpoint_description_RepresentationTemplate_name: Property = Property(name="name", type=StringType)
viewpoint_description_RepresentationTemplate.attributes={viewpoint_description_RepresentationTemplate_name}

# viewpoint_description_RepresentationImportDescription class attributes and methods

# viewpoint_description_PasteTargetDescription class attributes and methods

# tool_PasteDescription class attributes and methods

# viewpoint_description_DecorationDescriptionsSet class attributes and methods

# viewpoint_description_DecorationDescription class attributes and methods
viewpoint_description_DecorationDescription_name: Property = Property(name="name", type=StringType)
viewpoint_description_DecorationDescription_position: Property = Property(name="position", type=StringType)
viewpoint_description_DecorationDescription_decoratorPath: Property = Property(name="decoratorPath", type=StringType)
viewpoint_description_DecorationDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
viewpoint_description_DecorationDescription.attributes={viewpoint_description_DecorationDescription_preconditionExpression, viewpoint_description_DecorationDescription_decoratorPath, viewpoint_description_DecorationDescription_position, viewpoint_description_DecorationDescription_name}

# viewpoint_description_SemanticBasedDecoration class attributes and methods
viewpoint_description_SemanticBasedDecoration_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_description_SemanticBasedDecoration.attributes={viewpoint_description_SemanticBasedDecoration_domainClass}

# viewpoint_description_Customization class attributes and methods

# IVSMElementCustomization class attributes and methods

# viewpoint_description_ConditionalStyleDescription class attributes and methods
viewpoint_description_ConditionalStyleDescription_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
viewpoint_description_ConditionalStyleDescription_m_checkPredicate: Method = Method(name="checkPredicate", parameters={Parameter(name='modelElement'), Parameter(name='containerVariable'), Parameter(name='viewVariable')}, type=BooleanType)
viewpoint_description_ConditionalStyleDescription.attributes={viewpoint_description_ConditionalStyleDescription_predicateExpression}
viewpoint_description_ConditionalStyleDescription.methods={viewpoint_description_ConditionalStyleDescription_m_checkPredicate}

# EStructuralFeatureCustomization class attributes and methods

# viewpoint_description_VSMElementCustomizationReuse class attributes and methods

# viewpoint_description_EStructuralFeatureCustomization class attributes and methods
viewpoint_description_EStructuralFeatureCustomization_applyOnAll: Property = Property(name="applyOnAll", type=BooleanType)
viewpoint_description_EStructuralFeatureCustomization.attributes={viewpoint_description_EStructuralFeatureCustomization_applyOnAll}

# viewpoint_description_EAttributeCustomization class attributes and methods
viewpoint_description_EAttributeCustomization_attributeName: Property = Property(name="attributeName", type=StringType)
viewpoint_description_EAttributeCustomization_value: Property = Property(name="value", type=StringType)
viewpoint_description_EAttributeCustomization.attributes={viewpoint_description_EAttributeCustomization_value, viewpoint_description_EAttributeCustomization_attributeName}

# viewpoint_description_EReferenceCustomization class attributes and methods
viewpoint_description_EReferenceCustomization_referenceName: Property = Property(name="referenceName", type=StringType)
viewpoint_description_EReferenceCustomization.attributes={viewpoint_description_EReferenceCustomization_referenceName}

# viewpoint_description_SelectionDescription class attributes and methods
viewpoint_description_SelectionDescription_candidatesExpression: Property = Property(name="candidatesExpression", type=StringType)
viewpoint_description_SelectionDescription_multiple: Property = Property(name="multiple", type=BooleanType)
viewpoint_description_SelectionDescription_tree: Property = Property(name="tree", type=BooleanType)
viewpoint_description_SelectionDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
viewpoint_description_SelectionDescription_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
viewpoint_description_SelectionDescription_message: Property = Property(name="message", type=StringType)
viewpoint_description_SelectionDescription.attributes={viewpoint_description_SelectionDescription_candidatesExpression, viewpoint_description_SelectionDescription_rootExpression, viewpoint_description_SelectionDescription_childrenExpression, viewpoint_description_SelectionDescription_message, viewpoint_description_SelectionDescription_multiple, viewpoint_description_SelectionDescription_tree}

# viewpoint_description_IVSMElementCustomization class attributes and methods

# viewpoint_description_VSMElementCustomization class attributes and methods
viewpoint_description_VSMElementCustomization_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
viewpoint_description_VSMElementCustomization.attributes={viewpoint_description_VSMElementCustomization_predicateExpression}

# viewpoint_description_SystemColor class attributes and methods
viewpoint_description_SystemColor_name: Property = Property(name="name", type=StringType)
viewpoint_description_SystemColor.attributes={viewpoint_description_SystemColor_name}

# FixedColor class attributes and methods

# viewpoint_description_InterpolatedColor class attributes and methods
viewpoint_description_InterpolatedColor_colorValueComputationExpression: Property = Property(name="colorValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor_minValueComputationExpression: Property = Property(name="minValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor_maxValueComputationExpression: Property = Property(name="maxValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor.attributes={viewpoint_description_InterpolatedColor_minValueComputationExpression, viewpoint_description_InterpolatedColor_maxValueComputationExpression, viewpoint_description_InterpolatedColor_colorValueComputationExpression}

# description_ColorDescription class attributes and methods

# description_UserColor class attributes and methods

# ColorStep class attributes and methods

# viewpoint_description_ColorStep class attributes and methods
viewpoint_description_ColorStep_associatedValue: Property = Property(name="associatedValue", type=StringType)
viewpoint_description_ColorStep.attributes={viewpoint_description_ColorStep_associatedValue}

# viewpoint_description_FixedColor class attributes and methods
viewpoint_description_FixedColor_red: Property = Property(name="red", type=IntegerType)
viewpoint_description_FixedColor_green: Property = Property(name="green", type=IntegerType)
viewpoint_description_FixedColor_blue: Property = Property(name="blue", type=IntegerType)
viewpoint_description_FixedColor.attributes={viewpoint_description_FixedColor_green, viewpoint_description_FixedColor_red, viewpoint_description_FixedColor_blue}

# ColorDescription class attributes and methods

# viewpoint_description_UserFixedColor class attributes and methods

# description_FixedColor class attributes and methods

# viewpoint_description_UserColor class attributes and methods
viewpoint_description_UserColor_name: Property = Property(name="name", type=StringType)
viewpoint_description_UserColor.attributes={viewpoint_description_UserColor_name}

# viewpoint_description_ColorDescription class attributes and methods

# viewpoint_description_Environment class attributes and methods

# tool_ToolEntry class attributes and methods

# style_LabelBorderStyles class attributes and methods

# viewpoint_description_SytemColorsPalette class attributes and methods

# SystemColor class attributes and methods

# viewpoint_description_UserColorsPalette class attributes and methods
viewpoint_description_UserColorsPalette_name: Property = Property(name="name", type=StringType)
viewpoint_description_UserColorsPalette.attributes={viewpoint_description_UserColorsPalette_name}

# UserColor class attributes and methods

# viewpoint_description_AnnotationEntry class attributes and methods
viewpoint_description_AnnotationEntry_source: Property = Property(name="source", type=StringType)
viewpoint_description_AnnotationEntry.attributes={viewpoint_description_AnnotationEntry_source}

# viewpoint_description_EndUserDocumentedElement class attributes and methods
viewpoint_description_EndUserDocumentedElement_endUserDocumentation: Property = Property(name="endUserDocumentation", type=StringType)
viewpoint_description_EndUserDocumentedElement.attributes={viewpoint_description_EndUserDocumentedElement_endUserDocumentation}

# viewpoint_description_IdentifiedElement class attributes and methods
viewpoint_description_IdentifiedElement_name: Property = Property(name="name", type=StringType)
viewpoint_description_IdentifiedElement_label: Property = Property(name="label", type=StringType)
viewpoint_description_IdentifiedElement.attributes={viewpoint_description_IdentifiedElement_label, viewpoint_description_IdentifiedElement_name}

# viewpoint_description_ComputedColor class attributes and methods
viewpoint_description_ComputedColor_red: Property = Property(name="red", type=StringType)
viewpoint_description_ComputedColor_green: Property = Property(name="green", type=StringType)
viewpoint_description_ComputedColor_blue: Property = Property(name="blue", type=StringType)
viewpoint_description_ComputedColor.attributes={viewpoint_description_ComputedColor_green, viewpoint_description_ComputedColor_red, viewpoint_description_ComputedColor_blue}

# viewpoint_description_DAnnotationEntry class attributes and methods
viewpoint_description_DAnnotationEntry_source: Property = Property(name="source", type=StringType)
viewpoint_description_DAnnotationEntry_details: Property = Property(name="details", type=StringType)
viewpoint_description_DAnnotationEntry.attributes={viewpoint_description_DAnnotationEntry_details, viewpoint_description_DAnnotationEntry_source}

# viewpoint_style_StyleDescription class attributes and methods

# viewpoint_style_BasicLabelStyleDescription class attributes and methods
viewpoint_style_BasicLabelStyleDescription_labelSize: Property = Property(name="labelSize", type=IntegerType)
viewpoint_style_BasicLabelStyleDescription_labelFormat: Property = Property(name="labelFormat", type=StringType)
viewpoint_style_BasicLabelStyleDescription_showIcon: Property = Property(name="showIcon", type=BooleanType)
viewpoint_style_BasicLabelStyleDescription_labelExpression: Property = Property(name="labelExpression", type=StringType)
viewpoint_style_BasicLabelStyleDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_style_BasicLabelStyleDescription.attributes={viewpoint_style_BasicLabelStyleDescription_labelFormat, viewpoint_style_BasicLabelStyleDescription_labelSize, viewpoint_style_BasicLabelStyleDescription_labelExpression, viewpoint_style_BasicLabelStyleDescription_showIcon, viewpoint_style_BasicLabelStyleDescription_iconPath}

# viewpoint_style_LabelStyleDescription class attributes and methods
viewpoint_style_LabelStyleDescription_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
viewpoint_style_LabelStyleDescription.attributes={viewpoint_style_LabelStyleDescription_labelAlignment}

# BasicLabelStyleDescription class attributes and methods

# viewpoint_style_LabelBorderStyles class attributes and methods

# style_LabelBorderStyleDescription class attributes and methods

# viewpoint_style_LabelBorderStyleDescription class attributes and methods
viewpoint_style_LabelBorderStyleDescription_id: Property = Property(name="id", type=StringType)
viewpoint_style_LabelBorderStyleDescription_name: Property = Property(name="name", type=StringType)
viewpoint_style_LabelBorderStyleDescription_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
viewpoint_style_LabelBorderStyleDescription_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
viewpoint_style_LabelBorderStyleDescription.attributes={viewpoint_style_LabelBorderStyleDescription_cornerHeight, viewpoint_style_LabelBorderStyleDescription_name, viewpoint_style_LabelBorderStyleDescription_id, viewpoint_style_LabelBorderStyleDescription_cornerWidth}

# viewpoint_style_TooltipStyleDescription class attributes and methods
viewpoint_style_TooltipStyleDescription_tooltipExpression: Property = Property(name="tooltipExpression", type=StringType)
viewpoint_style_TooltipStyleDescription.attributes={viewpoint_style_TooltipStyleDescription_tooltipExpression}

# viewpoint_tool_AbstractToolDescription class attributes and methods
viewpoint_tool_AbstractToolDescription_precondition: Property = Property(name="precondition", type=StringType)
viewpoint_tool_AbstractToolDescription_forceRefresh: Property = Property(name="forceRefresh", type=BooleanType)
viewpoint_tool_AbstractToolDescription.attributes={viewpoint_tool_AbstractToolDescription_forceRefresh, viewpoint_tool_AbstractToolDescription_precondition}

# ToolEntry class attributes and methods

# tool_ToolFilterDescription class attributes and methods

# viewpoint_tool_MappingBasedToolDescription class attributes and methods

# AbstractToolDescription class attributes and methods

# viewpoint_tool_ToolDescription class attributes and methods
viewpoint_tool_ToolDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_ToolDescription.attributes={viewpoint_tool_ToolDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_ElementVariable class attributes and methods

# tool_ElementViewVariable class attributes and methods

# tool_InitialOperation class attributes and methods

# viewpoint_tool_ToolEntry class attributes and methods

# viewpoint_tool_PasteDescription class attributes and methods
viewpoint_tool_PasteDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
viewpoint_tool_PasteDescription.methods={viewpoint_tool_PasteDescription_m_getContainers}

# tool_DropContainerVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# viewpoint_tool_SelectionWizardDescription class attributes and methods
viewpoint_tool_SelectionWizardDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_SelectionWizardDescription_windowTitle: Property = Property(name="windowTitle", type=StringType)
viewpoint_tool_SelectionWizardDescription_windowImagePath: Property = Property(name="windowImagePath", type=StringType)
viewpoint_tool_SelectionWizardDescription.attributes={viewpoint_tool_SelectionWizardDescription_windowTitle, viewpoint_tool_SelectionWizardDescription_iconPath, viewpoint_tool_SelectionWizardDescription_windowImagePath}

# tool_AbstractToolDescription class attributes and methods

# description_SelectionDescription class attributes and methods

# viewpoint_tool_PaneBasedSelectionWizardDescription class attributes and methods
viewpoint_tool_PaneBasedSelectionWizardDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_windowTitle: Property = Property(name="windowTitle", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_windowImagePath: Property = Property(name="windowImagePath", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_message: Property = Property(name="message", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_choiceOfValuesMessage: Property = Property(name="choiceOfValuesMessage", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_candidatesExpression: Property = Property(name="candidatesExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_tree: Property = Property(name="tree", type=BooleanType)
viewpoint_tool_PaneBasedSelectionWizardDescription_selectedValuesMessage: Property = Property(name="selectedValuesMessage", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_preSelectedCandidatesExpression: Property = Property(name="preSelectedCandidatesExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription.attributes={viewpoint_tool_PaneBasedSelectionWizardDescription_iconPath, viewpoint_tool_PaneBasedSelectionWizardDescription_rootExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_choiceOfValuesMessage, viewpoint_tool_PaneBasedSelectionWizardDescription_childrenExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_windowTitle, viewpoint_tool_PaneBasedSelectionWizardDescription_message, viewpoint_tool_PaneBasedSelectionWizardDescription_preSelectedCandidatesExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_tree, viewpoint_tool_PaneBasedSelectionWizardDescription_windowImagePath, viewpoint_tool_PaneBasedSelectionWizardDescription_selectedValuesMessage, viewpoint_tool_PaneBasedSelectionWizardDescription_candidatesExpression}

# tool_ElementSelectVariable class attributes and methods

# tool_SelectContainerVariable class attributes and methods

# viewpoint_tool_RepresentationCreationDescription class attributes and methods
viewpoint_tool_RepresentationCreationDescription_titleExpression: Property = Property(name="titleExpression", type=StringType)
viewpoint_tool_RepresentationCreationDescription_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_RepresentationCreationDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_RepresentationCreationDescription.attributes={viewpoint_tool_RepresentationCreationDescription_titleExpression, viewpoint_tool_RepresentationCreationDescription_browseExpression}
viewpoint_tool_RepresentationCreationDescription.methods={viewpoint_tool_RepresentationCreationDescription_m_getMappings}

# tool_NameVariable class attributes and methods

# viewpoint_tool_RepresentationNavigationDescription class attributes and methods
viewpoint_tool_RepresentationNavigationDescription_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_RepresentationNavigationDescription_navigationNameExpression: Property = Property(name="navigationNameExpression", type=StringType)
viewpoint_tool_RepresentationNavigationDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_RepresentationNavigationDescription.attributes={viewpoint_tool_RepresentationNavigationDescription_navigationNameExpression, viewpoint_tool_RepresentationNavigationDescription_browseExpression}
viewpoint_tool_RepresentationNavigationDescription.methods={viewpoint_tool_RepresentationNavigationDescription_m_getMappings}

# viewpoint_tool_MenuItemOrRef class attributes and methods

# viewpoint_tool_MenuItemDescription class attributes and methods
viewpoint_tool_MenuItemDescription_icon: Property = Property(name="icon", type=StringType)
viewpoint_tool_MenuItemDescription.attributes={viewpoint_tool_MenuItemDescription_icon}

# tool_MenuItemOrRef class attributes and methods

# viewpoint_tool_MenuItemDescriptionReference class attributes and methods

# MenuItemOrRef class attributes and methods

# tool_MenuItemDescription class attributes and methods

# viewpoint_tool_OperationAction class attributes and methods

# MenuItemDescription class attributes and methods

# viewpoint_tool_ExternalJavaAction class attributes and methods
viewpoint_tool_ExternalJavaAction_id: Property = Property(name="id", type=StringType)
viewpoint_tool_ExternalJavaAction.attributes={viewpoint_tool_ExternalJavaAction_id}

# tool_ContainerModelOperation class attributes and methods

# tool_ExternalJavaActionParameter class attributes and methods

# viewpoint_tool_ExternalJavaActionCall class attributes and methods

# tool_ExternalJavaAction class attributes and methods

# viewpoint_tool_PopupMenu class attributes and methods

# tool_VariableContainer class attributes and methods

# viewpoint_tool_SubVariable class attributes and methods

# AbstractVariable class attributes and methods

# viewpoint_tool_DialogVariable class attributes and methods
viewpoint_tool_DialogVariable_dialogPrompt: Property = Property(name="dialogPrompt", type=StringType)
viewpoint_tool_DialogVariable.attributes={viewpoint_tool_DialogVariable_dialogPrompt}

# viewpoint_tool_ElementDropVariable class attributes and methods

# tool_AbstractVariable class attributes and methods

# viewpoint_tool_ElementSelectVariable class attributes and methods

# viewpoint_tool_ElementVariable class attributes and methods

# viewpoint_tool_ElementViewVariable class attributes and methods

# viewpoint_tool_ElementDeleteVariable class attributes and methods

# viewpoint_tool_DropContainerVariable class attributes and methods

# viewpoint_tool_SelectContainerVariable class attributes and methods

# viewpoint_tool_ContainerViewVariable class attributes and methods

# viewpoint_tool_SelectModelElementVariable class attributes and methods

# viewpoint_tool_EditMaskVariables class attributes and methods
viewpoint_tool_EditMaskVariables_mask: Property = Property(name="mask", type=StringType)
viewpoint_tool_EditMaskVariables.attributes={viewpoint_tool_EditMaskVariables_mask}

# viewpoint_tool_ContainerModelOperation class attributes and methods

# ModelOperation class attributes and methods

# tool_ModelOperation class attributes and methods

# viewpoint_tool_ModelOperation class attributes and methods

# viewpoint_tool_InitialNodeCreationOperation class attributes and methods

# viewpoint_tool_InitialOperation class attributes and methods

# viewpoint_tool_InitEdgeCreationOperation class attributes and methods

# viewpoint_tool_InitialContainerDropOperation class attributes and methods

# viewpoint_tool_AbstractVariable class attributes and methods
viewpoint_tool_AbstractVariable_name: Property = Property(name="name", type=StringType)
viewpoint_tool_AbstractVariable.attributes={viewpoint_tool_AbstractVariable_name}

# viewpoint_tool_VariableContainer class attributes and methods

# tool_SubVariable class attributes and methods

# viewpoint_tool_AcceleoVariable class attributes and methods
viewpoint_tool_AcceleoVariable_computationExpression: Property = Property(name="computationExpression", type=StringType)
viewpoint_tool_AcceleoVariable.attributes={viewpoint_tool_AcceleoVariable_computationExpression}

# viewpoint_tool_ChangeContext class attributes and methods
viewpoint_tool_ChangeContext_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_ChangeContext.attributes={viewpoint_tool_ChangeContext_browseExpression}

# viewpoint_tool_SetValue class attributes and methods
viewpoint_tool_SetValue_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_SetValue_valueExpression: Property = Property(name="valueExpression", type=StringType)
viewpoint_tool_SetValue.attributes={viewpoint_tool_SetValue_valueExpression, viewpoint_tool_SetValue_featureName}

# viewpoint_tool_SetObject class attributes and methods
viewpoint_tool_SetObject_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_SetObject.attributes={viewpoint_tool_SetObject_featureName}

# tool_viewpoint_EObject class attributes and methods

# viewpoint_tool_Unset class attributes and methods
viewpoint_tool_Unset_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_Unset_elementExpression: Property = Property(name="elementExpression", type=StringType)
viewpoint_tool_Unset.attributes={viewpoint_tool_Unset_featureName, viewpoint_tool_Unset_elementExpression}

# viewpoint_tool_MoveElement class attributes and methods
viewpoint_tool_MoveElement_newContainerExpression: Property = Property(name="newContainerExpression", type=StringType)
viewpoint_tool_MoveElement_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_MoveElement.attributes={viewpoint_tool_MoveElement_featureName, viewpoint_tool_MoveElement_newContainerExpression}

# viewpoint_tool_CreateInstance class attributes and methods
viewpoint_tool_CreateInstance_typeName: Property = Property(name="typeName", type=StringType)
viewpoint_tool_CreateInstance_referenceName: Property = Property(name="referenceName", type=StringType)
viewpoint_tool_CreateInstance_variableName: Property = Property(name="variableName", type=StringType)
viewpoint_tool_CreateInstance.attributes={viewpoint_tool_CreateInstance_variableName, viewpoint_tool_CreateInstance_typeName, viewpoint_tool_CreateInstance_referenceName}

# ContainerModelOperation class attributes and methods

# viewpoint_tool_If class attributes and methods
viewpoint_tool_If_conditionExpression: Property = Property(name="conditionExpression", type=StringType)
viewpoint_tool_If.attributes={viewpoint_tool_If_conditionExpression}

# viewpoint_tool_DeleteView class attributes and methods

# viewpoint_tool_NameVariable class attributes and methods

# viewpoint_tool_ExternalJavaActionParameter class attributes and methods
viewpoint_tool_ExternalJavaActionParameter_name: Property = Property(name="name", type=StringType)
viewpoint_tool_ExternalJavaActionParameter_value: Property = Property(name="value", type=StringType)
viewpoint_tool_ExternalJavaActionParameter.attributes={viewpoint_tool_ExternalJavaActionParameter_value, viewpoint_tool_ExternalJavaActionParameter_name}

# viewpoint_tool_ToolFilterDescription class attributes and methods
viewpoint_tool_ToolFilterDescription_precondition: Property = Property(name="precondition", type=StringType)
viewpoint_tool_ToolFilterDescription_elementsToListen: Property = Property(name="elementsToListen", type=StringType)
viewpoint_tool_ToolFilterDescription.attributes={viewpoint_tool_ToolFilterDescription_precondition, viewpoint_tool_ToolFilterDescription_elementsToListen}

# tool_FeatureChangeListener class attributes and methods

# viewpoint_tool_RemoveElement class attributes and methods

# viewpoint_tool_For class attributes and methods
viewpoint_tool_For_iteratorName: Property = Property(name="iteratorName", type=StringType)
viewpoint_tool_For_expression: Property = Property(name="expression", type=StringType)
viewpoint_tool_For.attributes={viewpoint_tool_For_expression, viewpoint_tool_For_iteratorName}

# viewpoint_tool_SwitchChild class attributes and methods

# viewpoint_tool_Default class attributes and methods

# viewpoint_tool_Switch class attributes and methods

# tool_Case class attributes and methods

# tool_Default class attributes and methods

# viewpoint_validation_ValidationSet class attributes and methods
viewpoint_validation_ValidationSet_name: Property = Property(name="name", type=StringType)
viewpoint_validation_ValidationSet.attributes={viewpoint_validation_ValidationSet_name}

# DocumentedElement class attributes and methods

# validation_ValidationRule class attributes and methods

# viewpoint_validation_ValidationRule class attributes and methods
viewpoint_validation_ValidationRule_level: Property = Property(name="level", type=StringType)
viewpoint_validation_ValidationRule_message: Property = Property(name="message", type=StringType)
viewpoint_validation_ValidationRule_m_checkRule: Method = Method(name="checkRule", parameters={Parameter(name='eObj')}, type=BooleanType)
viewpoint_validation_ValidationRule_m_getMessage: Method = Method(name="getMessage", parameters={Parameter(name='eObj')}, type=StringType)
viewpoint_validation_ValidationRule.attributes={viewpoint_validation_ValidationRule_level, viewpoint_validation_ValidationRule_message}
viewpoint_validation_ValidationRule.methods={viewpoint_validation_ValidationRule_m_getMessage, viewpoint_validation_ValidationRule_m_checkRule}

# viewpoint_tool_FeatureChangeListener class attributes and methods
viewpoint_tool_FeatureChangeListener_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_tool_FeatureChangeListener_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_FeatureChangeListener.attributes={viewpoint_tool_FeatureChangeListener_featureName, viewpoint_tool_FeatureChangeListener_domainClass}

# viewpoint_tool_Case class attributes and methods
viewpoint_tool_Case_conditionExpression: Property = Property(name="conditionExpression", type=StringType)
viewpoint_tool_Case.attributes={viewpoint_tool_Case_conditionExpression}

# SwitchChild class attributes and methods

# viewpoint_validation_SemanticValidationRule class attributes and methods
viewpoint_validation_SemanticValidationRule_targetClass: Property = Property(name="targetClass", type=StringType)
viewpoint_validation_SemanticValidationRule.attributes={viewpoint_validation_SemanticValidationRule_targetClass}

# ValidationRule class attributes and methods

# viewpoint_validation_ViewValidationRule class attributes and methods

# RepresentationElementMapping class attributes and methods

# viewpoint_validation_RuleAudit class attributes and methods
viewpoint_validation_RuleAudit_auditExpression: Property = Property(name="auditExpression", type=StringType)
viewpoint_validation_RuleAudit.attributes={viewpoint_validation_RuleAudit_auditExpression}

# viewpoint_validation_ValidationFix class attributes and methods
viewpoint_validation_ValidationFix_name: Property = Property(name="name", type=StringType)
viewpoint_validation_ValidationFix.attributes={viewpoint_validation_ValidationFix_name}

# viewpoint_audit_InformationSection class attributes and methods
viewpoint_audit_InformationSection_m_getContent: Method = Method(name="getContent", parameters={Parameter(name='eObj')}, type=StringType)
viewpoint_audit_InformationSection.methods={viewpoint_audit_InformationSection_m_getContent}

# viewpoint_audit_TemplateInformationSection class attributes and methods
viewpoint_audit_TemplateInformationSection_templatePath: Property = Property(name="templatePath", type=StringType)
viewpoint_audit_TemplateInformationSection.attributes={viewpoint_audit_TemplateInformationSection_templatePath}

# InformationSection class attributes and methods

# validation_RuleAudit class attributes and methods

# validation_ValidationFix class attributes and methods

# Relationships
ownedFeatureExtensions11: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureExtensions11",
    ends={
        Property(name="viewpoint_DFeatureExtension", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis12", type=viewpoint_DFeatureExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
description13: BinaryAssociation = BinaryAssociation(
    name="description13",
    ends={
        Property(name="FeatureExtensionDescription", type=viewpoint_DFeatureExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DFeatureExtension14", type=FeatureExtensionDescription, multiplicity=Multiplicity(1, 1))
    }
)
referencedAnalysis1: BinaryAssociation = BinaryAssociation(
    name="referencedAnalysis1",
    ends={
        Property(name="viewpoint_DAnalysis", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis0", type=viewpoint_DAnalysis, multiplicity=Multiplicity(0, 9999))
    }
)
models2: BinaryAssociation = BinaryAssociation(
    name="models2",
    ends={
        Property(name="viewpoint_EObject", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis3", type=viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAnnotations4: BinaryAssociation = BinaryAssociation(
    name="eAnnotations4",
    ends={
        Property(name="DAnnotationEntry", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis5", type=DAnnotationEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedViews6: BinaryAssociation = BinaryAssociation(
    name="ownedViews6",
    ends={
        Property(name="viewpoint_DView", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis7", type=viewpoint_DView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectedViews8: BinaryAssociation = BinaryAssociation(
    name="selectedViews8",
    ends={
        Property(name="viewpoint_DView10", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis9", type=viewpoint_DView, multiplicity=Multiplicity(0, 9999))
    }
)
models16: BinaryAssociation = BinaryAssociation(
    name="models16",
    ends={
        Property(name="viewpoint_EObject17", type=viewpoint_DRepresentationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentationContainer", type=viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
ownedNavigationLinks15: BinaryAssociation = BinaryAssociation(
    name="ownedNavigationLinks15",
    ends={
        Property(name="viewpoint_DNavigationLink", type=viewpoint_DNavigable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DNavigable", type=viewpoint_DNavigationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentations29: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations29",
    ends={
        Property(name="viewpoint_DRepresentation31", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView30", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtensions32: BinaryAssociation = BinaryAssociation(
    name="ownedExtensions32",
    ends={
        Property(name="viewpoint_MetaModelExtension", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView33", type=viewpoint_MetaModelExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allRepresentations34: BinaryAssociation = BinaryAssociation(
    name="allRepresentations34",
    ends={
        Property(name="viewpoint_DRepresentation36", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView35", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="viewpoint_EObject19", type=viewpoint_DSemanticDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DSemanticDecorator", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
ownedRepresentationElements20: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationElements20",
    ends={
        Property(name="viewpoint_DRepresentationElement", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
representationElements21: BinaryAssociation = BinaryAssociation(
    name="representationElements21",
    ends={
        Property(name="viewpoint_DRepresentationElement23", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation22", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnotationEntries24: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotationEntries24",
    ends={
        Property(name="AnnotationEntry", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation25", type=AnnotationEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semanticElements26: BinaryAssociation = BinaryAssociation(
    name="semanticElements26",
    ends={
        Property(name="viewpoint_EObject28", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentationElement27", type=viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
data49: BinaryAssociation = BinaryAssociation(
    name="data49",
    ends={
        Property(name="viewpoint_EObject50", type=viewpoint_DAnalysisCustomData, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisCustomData", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hiddenRepresentations37: BinaryAssociation = BinaryAssociation(
    name="hiddenRepresentations37",
    ends={
        Property(name="viewpoint_DRepresentation39", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView38", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedRepresentations40: BinaryAssociation = BinaryAssociation(
    name="referencedRepresentations40",
    ends={
        Property(name="viewpoint_DRepresentation42", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView41", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999))
    }
)
viewpoint43: BinaryAssociation = BinaryAssociation(
    name="viewpoint43",
    ends={
        Property(name="Viewpoint", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView44", type=Viewpoint, multiplicity=Multiplicity(1, 1))
    }
)
extensionGroup45: BinaryAssociation = BinaryAssociation(
    name="extensionGroup45",
    ends={
        Property(name="viewpoint_EObject47", type=viewpoint_MetaModelExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_MetaModelExtension46", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
description48: BinaryAssociation = BinaryAssociation(
    name="description48",
    ends={
        Property(name="DecorationDescription", type=viewpoint_Decoration, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_Decoration", type=DecorationDescription, multiplicity=Multiplicity(1, 1))
    }
)
description51: BinaryAssociation = BinaryAssociation(
    name="description51",
    ends={
        Property(name="style_StyleDescription", type=viewpoint_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_Style", type=style_StyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
ownedSessions57: BinaryAssociation = BinaryAssociation(
    name="ownedSessions57",
    ends={
        Property(name="viewpoint_DAnalysisSessionEObject58", type=viewpoint_SessionManagerEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_SessionManagerEObject", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members59: BinaryAssociation = BinaryAssociation(
    name="members59",
    ends={
        Property(name="viewpoint_DResource", type=viewpoint_DResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DResourceContainer", type=viewpoint_DResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelColor60: BinaryAssociation = BinaryAssociation(
    name="labelColor60",
    ends={
        Property(name="viewpoint_RGBValues", type=viewpoint_BasicLabelStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_BasicLabelStyle", type=viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedViewpoints61: BinaryAssociation = BinaryAssociation(
    name="ownedViewpoints61",
    ends={
        Property(name="Viewpoint62", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group", type=Viewpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemColorsPalette63: BinaryAssociation = BinaryAssociation(
    name="systemColorsPalette63",
    ends={
        Property(name="SytemColorsPalette", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group64", type=SytemColorsPalette, multiplicity=Multiplicity(1, 1))
    }
)
userColorsPalettes65: BinaryAssociation = BinaryAssociation(
    name="userColorsPalettes65",
    ends={
        Property(name="UserColorsPalette", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group66", type=UserColorsPalette, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activatedViewpoints52: BinaryAssociation = BinaryAssociation(
    name="activatedViewpoints52",
    ends={
        Property(name="Viewpoint53", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisSessionEObject", type=Viewpoint, multiplicity=Multiplicity(0, 9999))
    }
)
analyses54: BinaryAssociation = BinaryAssociation(
    name="analyses54",
    ends={
        Property(name="viewpoint_DAnalysis56", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisSessionEObject55", type=viewpoint_DAnalysis, multiplicity=Multiplicity(0, 9999))
    }
)
validationSet67: BinaryAssociation = BinaryAssociation(
    name="validationSet67",
    ends={
        Property(name="validation_ValidationSet", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRepresentations68: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations68",
    ends={
        Property(name="RepresentationDescription", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint69", type=RepresentationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationExtensions70: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationExtensions70",
    ends={
        Property(name="RepresentationExtensionDescription", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint71", type=RepresentationExtensionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedJavaExtensions72: BinaryAssociation = BinaryAssociation(
    name="ownedJavaExtensions72",
    ends={
        Property(name="JavaExtension", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint73", type=JavaExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMMExtensions74: BinaryAssociation = BinaryAssociation(
    name="ownedMMExtensions74",
    ends={
        Property(name="MetamodelExtensionSetting", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint75", type=MetamodelExtensionSetting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureExtensions76: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureExtensions76",
    ends={
        Property(name="FeatureExtensionDescription78", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint77", type=FeatureExtensionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplates79: BinaryAssociation = BinaryAssociation(
    name="ownedTemplates79",
    ends={
        Property(name="RepresentationTemplate", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint80", type=RepresentationTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel81: BinaryAssociation = BinaryAssociation(
    name="metamodel81",
    ends={
        Property(name="description_viewpoint_EPackage", type=viewpoint_description_RepresentationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationDescription", type=description_viewpoint_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
metamodel84: BinaryAssociation = BinaryAssociation(
    name="metamodel84",
    ends={
        Property(name="description_viewpoint_EPackage85", type=viewpoint_description_RepresentationExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationExtensionDescription", type=description_viewpoint_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
extensionGroup86: BinaryAssociation = BinaryAssociation(
    name="extensionGroup86",
    ends={
        Property(name="description_viewpoint_EObject", type=viewpoint_description_MetamodelExtensionSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_MetamodelExtensionSetting", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
detailDescriptions87: BinaryAssociation = BinaryAssociation(
    name="detailDescriptions87",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=viewpoint_description_RepresentationElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationElementMapping", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
navigationDescriptions88: BinaryAssociation = BinaryAssociation(
    name="navigationDescriptions88",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=viewpoint_description_RepresentationElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationElementMapping89", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
eAnnotations90: BinaryAssociation = BinaryAssociation(
    name="eAnnotations90",
    ends={
        Property(name="DAnnotation", type=viewpoint_description_DModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DModelElement", type=DAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentations82: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations82",
    ends={
        Property(name="RepresentationDescription83", type=viewpoint_description_RepresentationTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationTemplate", type=RepresentationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pasteDescriptions92: BinaryAssociation = BinaryAssociation(
    name="pasteDescriptions92",
    ends={
        Property(name="tool_PasteDescription", type=viewpoint_description_PasteTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_PasteTargetDescription", type=tool_PasteDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptions93: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptions93",
    ends={
        Property(name="DecorationDescription94", type=viewpoint_description_DecorationDescriptionsSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DecorationDescriptionsSet", type=DecorationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details91: BinaryAssociation = BinaryAssociation(
    name="details91",
    ends={
        Property(name="description_viewpoint_EStringToStringMapEntry", type=viewpoint_description_DAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DAnnotation", type=description_viewpoint_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCustomizations96: BinaryAssociation = BinaryAssociation(
    name="featureCustomizations96",
    ends={
        Property(name="EStructuralFeatureCustomization", type=viewpoint_description_VSMElementCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomization", type=EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reuse97: BinaryAssociation = BinaryAssociation(
    name="reuse97",
    ends={
        Property(name="EStructuralFeatureCustomization98", type=viewpoint_description_VSMElementCustomizationReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomizationReuse", type=EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 9999))
    }
)
appliedOn99: BinaryAssociation = BinaryAssociation(
    name="appliedOn99",
    ends={
        Property(name="description_viewpoint_EObject101", type=viewpoint_description_VSMElementCustomizationReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomizationReuse100", type=description_viewpoint_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
appliedOn102: BinaryAssociation = BinaryAssociation(
    name="appliedOn102",
    ends={
        Property(name="description_viewpoint_EObject103", type=viewpoint_description_EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EStructuralFeatureCustomization", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
value104: BinaryAssociation = BinaryAssociation(
    name="value104",
    ends={
        Property(name="description_viewpoint_EObject105", type=viewpoint_description_EReferenceCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EReferenceCustomization", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
vsmElementCustomizations95: BinaryAssociation = BinaryAssociation(
    name="vsmElementCustomizations95",
    ends={
        Property(name="IVSMElementCustomization", type=viewpoint_description_Customization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Customization", type=IVSMElementCustomization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
colorSteps106: BinaryAssociation = BinaryAssociation(
    name="colorSteps106",
    ends={
        Property(name="ColorStep", type=viewpoint_description_InterpolatedColor, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_InterpolatedColor", type=ColorStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associatedColor107: BinaryAssociation = BinaryAssociation(
    name="associatedColor107",
    ends={
        Property(name="FixedColor", type=viewpoint_description_ColorStep, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ColorStep", type=FixedColor, multiplicity=Multiplicity(1, 1))
    }
)
systemColors108: BinaryAssociation = BinaryAssociation(
    name="systemColors108",
    ends={
        Property(name="SytemColorsPalette109", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment", type=SytemColorsPalette, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultTools110: BinaryAssociation = BinaryAssociation(
    name="defaultTools110",
    ends={
        Property(name="tool_ToolEntry", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment111", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelBorderStyles112: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyles112",
    ends={
        Property(name="style_LabelBorderStyles", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment113", type=style_LabelBorderStyles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries114: BinaryAssociation = BinaryAssociation(
    name="entries114",
    ends={
        Property(name="SystemColor", type=viewpoint_description_SytemColorsPalette, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_SytemColorsPalette", type=SystemColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries115: BinaryAssociation = BinaryAssociation(
    name="entries115",
    ends={
        Property(name="UserColor", type=viewpoint_description_UserColorsPalette, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_UserColorsPalette", type=UserColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data116: BinaryAssociation = BinaryAssociation(
    name="data116",
    ends={
        Property(name="description_viewpoint_EObject117", type=viewpoint_description_AnnotationEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_AnnotationEntry", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelColor118: BinaryAssociation = BinaryAssociation(
    name="labelColor118",
    ends={
        Property(name="ColorDescription", type=viewpoint_style_BasicLabelStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_BasicLabelStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyleDescriptions119: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyleDescriptions119",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=viewpoint_style_LabelBorderStyles, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_LabelBorderStyles", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters120: BinaryAssociation = BinaryAssociation(
    name="filters120",
    ends={
        Property(name="tool_ToolFilterDescription", type=viewpoint_tool_AbstractToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_AbstractToolDescription", type=tool_ToolFilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element121: BinaryAssociation = BinaryAssociation(
    name="element121",
    ends={
        Property(name="tool_ElementVariable", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription", type=tool_ElementVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView122: BinaryAssociation = BinaryAssociation(
    name="elementView122",
    ends={
        Property(name="tool_ElementViewVariable", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription123", type=tool_ElementViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation124: BinaryAssociation = BinaryAssociation(
    name="initialOperation124",
    ends={
        Property(name="tool_InitialOperation", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription125", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container126: BinaryAssociation = BinaryAssociation(
    name="container126",
    ends={
        Property(name="tool_DropContainerVariable", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView127: BinaryAssociation = BinaryAssociation(
    name="containerView127",
    ends={
        Property(name="tool_ContainerViewVariable", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription128", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copiedView129: BinaryAssociation = BinaryAssociation(
    name="copiedView129",
    ends={
        Property(name="tool_ElementViewVariable131", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription130", type=tool_ElementViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copiedElement132: BinaryAssociation = BinaryAssociation(
    name="copiedElement132",
    ends={
        Property(name="tool_ElementVariable134", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription133", type=tool_ElementVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation135: BinaryAssociation = BinaryAssociation(
    name="initialOperation135",
    ends={
        Property(name="tool_InitialOperation137", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription136", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container142: BinaryAssociation = BinaryAssociation(
    name="container142",
    ends={
        Property(name="viewpoint_tool_SelectionWizardDescription143", type=tool_SelectContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="tool_SelectContainerVariable", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation144: BinaryAssociation = BinaryAssociation(
    name="initialOperation144",
    ends={
        Property(name="tool_InitialOperation146", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription145", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element147: BinaryAssociation = BinaryAssociation(
    name="element147",
    ends={
        Property(name="tool_ElementSelectVariable148", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView149: BinaryAssociation = BinaryAssociation(
    name="containerView149",
    ends={
        Property(name="tool_ContainerViewVariable151", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription150", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container152: BinaryAssociation = BinaryAssociation(
    name="container152",
    ends={
        Property(name="tool_SelectContainerVariable154", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription153", type=tool_SelectContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation155: BinaryAssociation = BinaryAssociation(
    name="initialOperation155",
    ends={
        Property(name="tool_InitialOperation157", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription156", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element138: BinaryAssociation = BinaryAssociation(
    name="element138",
    ends={
        Property(name="tool_ElementSelectVariable", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView139: BinaryAssociation = BinaryAssociation(
    name="containerView139",
    ends={
        Property(name="tool_ContainerViewVariable141", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription140", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationDescription158: BinaryAssociation = BinaryAssociation(
    name="representationDescription158",
    ends={
        Property(name="RepresentationDescription159", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription", type=RepresentationDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation160: BinaryAssociation = BinaryAssociation(
    name="initialOperation160",
    ends={
        Property(name="tool_InitialOperation162", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription161", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerViewVariable163: BinaryAssociation = BinaryAssociation(
    name="containerViewVariable163",
    ends={
        Property(name="tool_ContainerViewVariable165", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription164", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationNameVariable166: BinaryAssociation = BinaryAssociation(
    name="representationNameVariable166",
    ends={
        Property(name="tool_NameVariable", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription167", type=tool_NameVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationNameVariable176: BinaryAssociation = BinaryAssociation(
    name="representationNameVariable176",
    ends={
        Property(name="tool_NameVariable178", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription177", type=tool_NameVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item179: BinaryAssociation = BinaryAssociation(
    name="item179",
    ends={
        Property(name="tool_MenuItemDescription", type=viewpoint_tool_MenuItemDescriptionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_MenuItemDescriptionReference", type=tool_MenuItemDescription, multiplicity=Multiplicity(1, 1))
    }
)
view180: BinaryAssociation = BinaryAssociation(
    name="view180",
    ends={
        Property(name="tool_ContainerViewVariable181", type=viewpoint_tool_OperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_OperationAction", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation182: BinaryAssociation = BinaryAssociation(
    name="initialOperation182",
    ends={
        Property(name="tool_InitialOperation184", type=viewpoint_tool_OperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_OperationAction183", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters185: BinaryAssociation = BinaryAssociation(
    name="parameters185",
    ends={
        Property(name="tool_ExternalJavaActionParameter", type=viewpoint_tool_ExternalJavaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ExternalJavaAction", type=tool_ExternalJavaActionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action186: BinaryAssociation = BinaryAssociation(
    name="action186",
    ends={
        Property(name="tool_ExternalJavaAction", type=viewpoint_tool_ExternalJavaActionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ExternalJavaActionCall", type=tool_ExternalJavaAction, multiplicity=Multiplicity(1, 1))
    }
)
menuItemDescription187: BinaryAssociation = BinaryAssociation(
    name="menuItemDescription187",
    ends={
        Property(name="tool_MenuItemDescription188", type=viewpoint_tool_PopupMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PopupMenu", type=tool_MenuItemDescription, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
representationDescription168: BinaryAssociation = BinaryAssociation(
    name="representationDescription168",
    ends={
        Property(name="RepresentationDescription169", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription", type=RepresentationDescription, multiplicity=Multiplicity(1, 1))
    }
)
containerViewVariable170: BinaryAssociation = BinaryAssociation(
    name="containerViewVariable170",
    ends={
        Property(name="tool_ContainerViewVariable172", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription171", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerVariable173: BinaryAssociation = BinaryAssociation(
    name="containerVariable173",
    ends={
        Property(name="tool_ElementSelectVariable175", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription174", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subModelOperations190: BinaryAssociation = BinaryAssociation(
    name="subModelOperations190",
    ends={
        Property(name="tool_ModelOperation", type=viewpoint_tool_ContainerModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerModelOperation", type=tool_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstModelOperations191: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations191",
    ends={
        Property(name="tool_ModelOperation192", type=viewpoint_tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialNodeCreationOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations193: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations193",
    ends={
        Property(name="tool_ModelOperation194", type=viewpoint_tool_InitialOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations195: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations195",
    ends={
        Property(name="tool_ModelOperation196", type=viewpoint_tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitEdgeCreationOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations197: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations197",
    ends={
        Property(name="tool_ModelOperation198", type=viewpoint_tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialContainerDropOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subVariables189: BinaryAssociation = BinaryAssociation(
    name="subVariables189",
    ends={
        Property(name="tool_SubVariable", type=viewpoint_tool_VariableContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_VariableContainer", type=tool_SubVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object199: BinaryAssociation = BinaryAssociation(
    name="object199",
    ends={
        Property(name="tool_viewpoint_EObject", type=viewpoint_tool_SetObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SetObject", type=tool_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subModelOperations201: BinaryAssociation = BinaryAssociation(
    name="subModelOperations201",
    ends={
        Property(name="tool_ModelOperation202", type=viewpoint_tool_SwitchChild, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SwitchChild", type=tool_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases203: BinaryAssociation = BinaryAssociation(
    name="cases203",
    ends={
        Property(name="tool_Case", type=viewpoint_tool_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_Switch", type=tool_Case, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
default204: BinaryAssociation = BinaryAssociation(
    name="default204",
    ends={
        Property(name="tool_Default", type=viewpoint_tool_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_Switch205", type=tool_Default, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedRules206: BinaryAssociation = BinaryAssociation(
    name="ownedRules206",
    ends={
        Property(name="validation_ValidationRule", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRules207: BinaryAssociation = BinaryAssociation(
    name="reusedRules207",
    ends={
        Property(name="validation_ValidationRule209", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet208", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
allRules210: BinaryAssociation = BinaryAssociation(
    name="allRules210",
    ends={
        Property(name="validation_ValidationRule212", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet211", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
listeners200: BinaryAssociation = BinaryAssociation(
    name="listeners200",
    ends={
        Property(name="tool_FeatureChangeListener", type=viewpoint_tool_ToolFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolFilterDescription", type=tool_FeatureChangeListener, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targets216: BinaryAssociation = BinaryAssociation(
    name="targets216",
    ends={
        Property(name="RepresentationElementMapping", type=viewpoint_validation_ViewValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ViewValidationRule", type=RepresentationElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
initialOperation217: BinaryAssociation = BinaryAssociation(
    name="initialOperation217",
    ends={
        Property(name="tool_InitialOperation218", type=viewpoint_validation_ValidationFix, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationFix", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
audits213: BinaryAssociation = BinaryAssociation(
    name="audits213",
    ends={
        Property(name="validation_RuleAudit", type=viewpoint_validation_ValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationRule", type=validation_RuleAudit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fixes214: BinaryAssociation = BinaryAssociation(
    name="fixes214",
    ends={
        Property(name="validation_ValidationFix", type=viewpoint_validation_ValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationRule215", type=validation_ValidationFix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_viewpoint_DRepresentationContainer_DView = Generalization(general=DView, specific=viewpoint_DRepresentationContainer)
gen_viewpoint_DRepresentation_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_DRepresentation)
gen_viewpoint_DRepresentation_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DRepresentation)
gen_viewpoint_DRepresentation_description_DModelElement = Generalization(general=description_DModelElement, specific=viewpoint_DRepresentation)
gen_viewpoint_DRepresentationElement_DLabelled = Generalization(general=DLabelled, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DMappingBased = Generalization(general=DMappingBased, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DStylizable = Generalization(general=DStylizable, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DView_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DView)
gen_viewpoint_DSourceFileLink_DNavigationLink = Generalization(general=DNavigationLink, specific=viewpoint_DSourceFileLink)
gen_viewpoint_LabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=viewpoint_LabelStyle)
gen_viewpoint_Style_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_Style)
gen_viewpoint_Style_Customizable = Generalization(general=Customizable, specific=viewpoint_Style)
gen_viewpoint_DFile_DResource = Generalization(general=DResource, specific=viewpoint_DFile)
gen_viewpoint_DResourceContainer_DResource = Generalization(general=DResource, specific=viewpoint_DResourceContainer)
gen_viewpoint_DProject_DResourceContainer = Generalization(general=DResourceContainer, specific=viewpoint_DProject)
gen_viewpoint_DFolder_DResourceContainer = Generalization(general=DResourceContainer, specific=viewpoint_DFolder)
gen_viewpoint_DModel_DFile = Generalization(general=DFile, specific=viewpoint_DModel)
gen_viewpoint_BasicLabelStyle_Customizable = Generalization(general=Customizable, specific=viewpoint_BasicLabelStyle)
gen_viewpoint_description_Group_description_DModelElement = Generalization(general=description_DModelElement, specific=viewpoint_description_Group)
gen_viewpoint_description_Group_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_Group)
gen_viewpoint_description_RepresentationDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_RepresentationDescription_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_RepresentationDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_Viewpoint_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_Component = Generalization(general=description_Component, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_RepresentationElementMapping_IdentifiedElement = Generalization(general=IdentifiedElement, specific=viewpoint_description_RepresentationElementMapping)
gen_viewpoint_description_RepresentationImportDescription_RepresentationDescription = Generalization(general=RepresentationDescription, specific=viewpoint_description_RepresentationImportDescription)
gen_viewpoint_description_SemanticBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=viewpoint_description_SemanticBasedDecoration)
gen_viewpoint_description_VSMElementCustomizationReuse_IVSMElementCustomization = Generalization(general=IVSMElementCustomization, specific=viewpoint_description_VSMElementCustomizationReuse)
gen_viewpoint_description_EAttributeCustomization_EStructuralFeatureCustomization = Generalization(general=EStructuralFeatureCustomization, specific=viewpoint_description_EAttributeCustomization)
gen_viewpoint_description_EReferenceCustomization_EStructuralFeatureCustomization = Generalization(general=EStructuralFeatureCustomization, specific=viewpoint_description_EReferenceCustomization)
gen_viewpoint_description_VSMElementCustomization_IVSMElementCustomization = Generalization(general=IVSMElementCustomization, specific=viewpoint_description_VSMElementCustomization)
gen_viewpoint_description_SystemColor_FixedColor = Generalization(general=FixedColor, specific=viewpoint_description_SystemColor)
gen_viewpoint_description_InterpolatedColor_description_ColorDescription = Generalization(general=description_ColorDescription, specific=viewpoint_description_InterpolatedColor)
gen_viewpoint_description_InterpolatedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_InterpolatedColor)
gen_viewpoint_description_FixedColor_ColorDescription = Generalization(general=ColorDescription, specific=viewpoint_description_FixedColor)
gen_viewpoint_description_UserFixedColor_description_FixedColor = Generalization(general=description_FixedColor, specific=viewpoint_description_UserFixedColor)
gen_viewpoint_description_UserFixedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_UserFixedColor)
gen_viewpoint_description_ComputedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_ComputedColor)
gen_viewpoint_description_ComputedColor_description_ColorDescription = Generalization(general=description_ColorDescription, specific=viewpoint_description_ComputedColor)
gen_viewpoint_style_LabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=viewpoint_style_LabelStyleDescription)
gen_viewpoint_tool_AbstractToolDescription_ToolEntry = Generalization(general=ToolEntry, specific=viewpoint_tool_AbstractToolDescription)
gen_viewpoint_tool_MappingBasedToolDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_MappingBasedToolDescription)
gen_viewpoint_tool_ToolDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_ToolDescription)
gen_viewpoint_tool_ToolEntry_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_tool_ToolEntry)
gen_viewpoint_tool_ToolEntry_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_tool_ToolEntry)
gen_viewpoint_tool_PasteDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_PasteDescription)
gen_viewpoint_tool_SelectionWizardDescription_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=viewpoint_tool_SelectionWizardDescription)
gen_viewpoint_tool_SelectionWizardDescription_description_SelectionDescription = Generalization(general=description_SelectionDescription, specific=viewpoint_tool_SelectionWizardDescription)
gen_viewpoint_tool_PaneBasedSelectionWizardDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_PaneBasedSelectionWizardDescription)
gen_viewpoint_tool_RepresentationCreationDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_RepresentationCreationDescription)
gen_viewpoint_tool_RepresentationNavigationDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_RepresentationNavigationDescription)
gen_viewpoint_tool_MenuItemDescription_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=viewpoint_tool_MenuItemDescription)
gen_viewpoint_tool_MenuItemDescription_tool_MenuItemOrRef = Generalization(general=tool_MenuItemOrRef, specific=viewpoint_tool_MenuItemDescription)
gen_viewpoint_tool_MenuItemDescriptionReference_MenuItemOrRef = Generalization(general=MenuItemOrRef, specific=viewpoint_tool_MenuItemDescriptionReference)
gen_viewpoint_tool_OperationAction_MenuItemDescription = Generalization(general=MenuItemDescription, specific=viewpoint_tool_OperationAction)
gen_viewpoint_tool_ExternalJavaAction_tool_MenuItemDescription = Generalization(general=tool_MenuItemDescription, specific=viewpoint_tool_ExternalJavaAction)
gen_viewpoint_tool_ExternalJavaAction_tool_ContainerModelOperation = Generalization(general=tool_ContainerModelOperation, specific=viewpoint_tool_ExternalJavaAction)
gen_viewpoint_tool_ExternalJavaActionCall_tool_MenuItemDescription = Generalization(general=tool_MenuItemDescription, specific=viewpoint_tool_ExternalJavaActionCall)
gen_viewpoint_tool_ExternalJavaActionCall_tool_ContainerModelOperation = Generalization(general=tool_ContainerModelOperation, specific=viewpoint_tool_ExternalJavaActionCall)
gen_viewpoint_tool_PopupMenu_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_PopupMenu)
gen_viewpoint_tool_AcceleoVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_AcceleoVariable)
gen_viewpoint_tool_AcceleoVariable_tool_SubVariable = Generalization(general=tool_SubVariable, specific=viewpoint_tool_AcceleoVariable)
gen_viewpoint_tool_SubVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_SubVariable)
gen_viewpoint_tool_DialogVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_DialogVariable)
gen_viewpoint_tool_ElementDropVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementDropVariable)
gen_viewpoint_tool_ElementDropVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ElementDropVariable)
gen_viewpoint_tool_ElementSelectVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_ElementSelectVariable)
gen_viewpoint_tool_ElementVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementVariable)
gen_viewpoint_tool_ElementVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ElementVariable)
gen_viewpoint_tool_ElementViewVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementViewVariable)
gen_viewpoint_tool_ElementViewVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ElementViewVariable)
gen_viewpoint_tool_ElementDeleteVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementDeleteVariable)
gen_viewpoint_tool_ElementDeleteVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ElementDeleteVariable)
gen_viewpoint_tool_DropContainerVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_DropContainerVariable)
gen_viewpoint_tool_DropContainerVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_DropContainerVariable)
gen_viewpoint_tool_SelectContainerVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_SelectContainerVariable)
gen_viewpoint_tool_SelectContainerVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_SelectContainerVariable)
gen_viewpoint_tool_ContainerViewVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ContainerViewVariable)
gen_viewpoint_tool_ContainerViewVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ContainerViewVariable)
gen_viewpoint_tool_SelectModelElementVariable_tool_SubVariable = Generalization(general=tool_SubVariable, specific=viewpoint_tool_SelectModelElementVariable)
gen_viewpoint_tool_SelectModelElementVariable_description_SelectionDescription = Generalization(general=description_SelectionDescription, specific=viewpoint_tool_SelectModelElementVariable)
gen_viewpoint_tool_ContainerModelOperation_ModelOperation = Generalization(general=ModelOperation, specific=viewpoint_tool_ContainerModelOperation)
gen_viewpoint_tool_ChangeContext_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_ChangeContext)
gen_viewpoint_tool_SetValue_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_SetValue)
gen_viewpoint_tool_SetObject_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_SetObject)
gen_viewpoint_tool_Unset_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_Unset)
gen_viewpoint_tool_MoveElement_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_MoveElement)
gen_viewpoint_tool_CreateInstance_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_CreateInstance)
gen_viewpoint_tool_If_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_If)
gen_viewpoint_tool_DeleteView_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_DeleteView)
gen_viewpoint_tool_NameVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_NameVariable)
gen_viewpoint_tool_RemoveElement_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_RemoveElement)
gen_viewpoint_tool_For_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_For)
gen_viewpoint_tool_Default_SwitchChild = Generalization(general=SwitchChild, specific=viewpoint_tool_Default)
gen_viewpoint_tool_Switch_ModelOperation = Generalization(general=ModelOperation, specific=viewpoint_tool_Switch)
gen_viewpoint_validation_ValidationSet_DocumentedElement = Generalization(general=DocumentedElement, specific=viewpoint_validation_ValidationSet)
gen_viewpoint_tool_Case_SwitchChild = Generalization(general=SwitchChild, specific=viewpoint_tool_Case)
gen_viewpoint_validation_SemanticValidationRule_ValidationRule = Generalization(general=ValidationRule, specific=viewpoint_validation_SemanticValidationRule)
gen_viewpoint_validation_ViewValidationRule_ValidationRule = Generalization(general=ValidationRule, specific=viewpoint_validation_ViewValidationRule)
gen_viewpoint_audit_TemplateInformationSection_InformationSection = Generalization(general=InformationSection, specific=viewpoint_audit_TemplateInformationSection)

# Domain Model
domain_model = DomainModel(
    name="viewpoint",
    types={FeatureExtensionDescription, viewpoint_DValidable, viewpoint_DAnalysis, viewpoint_EObject, DAnnotationEntry, viewpoint_DView, viewpoint_DFeatureExtension, viewpoint_DMappingBased, viewpoint_DContainer, viewpoint_DRepresentationContainer, DView, viewpoint_DSemanticDecorator, viewpoint_DNavigable, viewpoint_DNavigationLink, viewpoint_DStylizable, viewpoint_DRefreshable, viewpoint_DLabelled, viewpoint_MetaModelExtension, viewpoint_DRepresentation, description_DocumentedElement, DRefreshable, description_DModelElement, viewpoint_DRepresentationElement, AnnotationEntry, DLabelled, DMappingBased, DStylizable, DSemanticDecorator, viewpoint_DSourceFileLink, DNavigationLink, viewpoint_DAnalysisCustomData, Viewpoint, viewpoint_Decoration, DecorationDescription, viewpoint_LabelStyle, BasicLabelStyle, viewpoint_Style, Customizable, viewpoint_SessionManagerEObject, style_StyleDescription, viewpoint_DResource, viewpoint_RGBValues, viewpoint_DFile, DResource, viewpoint_DResourceContainer, viewpoint_DAnalysisSessionEObject, viewpoint_DProject, DResourceContainer, viewpoint_DFolder, viewpoint_DModel, DFile, viewpoint_BasicLabelStyle, viewpoint_Customizable, viewpoint_description_Group, SytemColorsPalette, UserColorsPalette, validation_ValidationSet, RepresentationDescription, RepresentationExtensionDescription, JavaExtension, MetamodelExtensionSetting, RepresentationTemplate, viewpoint_description_FeatureExtensionDescription, viewpoint_description_RepresentationDescription, description_viewpoint_EPackage, viewpoint_description_Component, viewpoint_description_Viewpoint, description_Component, description_EndUserDocumentedElement, description_IdentifiedElement, viewpoint_description_RepresentationExtensionDescription, viewpoint_description_MetamodelExtensionSetting, description_viewpoint_EObject, viewpoint_description_JavaExtension, viewpoint_description_RepresentationElementMapping, IdentifiedElement, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, viewpoint_description_AbstractMappingImport, viewpoint_description_DocumentedElement, viewpoint_description_DModelElement, DAnnotation, viewpoint_description_DAnnotation, description_viewpoint_EStringToStringMapEntry, viewpoint_description_RepresentationTemplate, viewpoint_description_RepresentationImportDescription, viewpoint_description_PasteTargetDescription, tool_PasteDescription, viewpoint_description_DecorationDescriptionsSet, viewpoint_description_DecorationDescription, viewpoint_description_SemanticBasedDecoration, viewpoint_description_Customization, IVSMElementCustomization, viewpoint_description_ConditionalStyleDescription, EStructuralFeatureCustomization, viewpoint_description_VSMElementCustomizationReuse, viewpoint_description_EStructuralFeatureCustomization, viewpoint_description_EAttributeCustomization, viewpoint_description_EReferenceCustomization, viewpoint_description_SelectionDescription, viewpoint_description_IVSMElementCustomization, viewpoint_description_VSMElementCustomization, viewpoint_description_SystemColor, FixedColor, viewpoint_description_InterpolatedColor, description_ColorDescription, description_UserColor, ColorStep, viewpoint_description_ColorStep, viewpoint_description_FixedColor, ColorDescription, viewpoint_description_UserFixedColor, description_FixedColor, viewpoint_description_UserColor, viewpoint_description_ColorDescription, viewpoint_description_Environment, tool_ToolEntry, style_LabelBorderStyles, viewpoint_description_SytemColorsPalette, SystemColor, viewpoint_description_UserColorsPalette, UserColor, viewpoint_description_AnnotationEntry, viewpoint_description_EndUserDocumentedElement, viewpoint_description_IdentifiedElement, viewpoint_description_ComputedColor, viewpoint_description_DAnnotationEntry, viewpoint_style_StyleDescription, viewpoint_style_BasicLabelStyleDescription, viewpoint_style_LabelStyleDescription, BasicLabelStyleDescription, viewpoint_style_LabelBorderStyles, style_LabelBorderStyleDescription, viewpoint_style_LabelBorderStyleDescription, viewpoint_style_TooltipStyleDescription, viewpoint_tool_AbstractToolDescription, ToolEntry, tool_ToolFilterDescription, viewpoint_tool_MappingBasedToolDescription, AbstractToolDescription, viewpoint_tool_ToolDescription, MappingBasedToolDescription, tool_ElementVariable, tool_ElementViewVariable, tool_InitialOperation, viewpoint_tool_ToolEntry, viewpoint_tool_PasteDescription, tool_DropContainerVariable, tool_ContainerViewVariable, viewpoint_tool_SelectionWizardDescription, tool_AbstractToolDescription, description_SelectionDescription, viewpoint_tool_PaneBasedSelectionWizardDescription, tool_ElementSelectVariable, tool_SelectContainerVariable, viewpoint_tool_RepresentationCreationDescription, tool_NameVariable, viewpoint_tool_RepresentationNavigationDescription, viewpoint_tool_MenuItemOrRef, viewpoint_tool_MenuItemDescription, tool_MenuItemOrRef, viewpoint_tool_MenuItemDescriptionReference, MenuItemOrRef, tool_MenuItemDescription, viewpoint_tool_OperationAction, MenuItemDescription, viewpoint_tool_ExternalJavaAction, tool_ContainerModelOperation, tool_ExternalJavaActionParameter, viewpoint_tool_ExternalJavaActionCall, tool_ExternalJavaAction, viewpoint_tool_PopupMenu, tool_VariableContainer, viewpoint_tool_SubVariable, AbstractVariable, viewpoint_tool_DialogVariable, viewpoint_tool_ElementDropVariable, tool_AbstractVariable, viewpoint_tool_ElementSelectVariable, viewpoint_tool_ElementVariable, viewpoint_tool_ElementViewVariable, viewpoint_tool_ElementDeleteVariable, viewpoint_tool_DropContainerVariable, viewpoint_tool_SelectContainerVariable, viewpoint_tool_ContainerViewVariable, viewpoint_tool_SelectModelElementVariable, viewpoint_tool_EditMaskVariables, viewpoint_tool_ContainerModelOperation, ModelOperation, tool_ModelOperation, viewpoint_tool_ModelOperation, viewpoint_tool_InitialNodeCreationOperation, viewpoint_tool_InitialOperation, viewpoint_tool_InitEdgeCreationOperation, viewpoint_tool_InitialContainerDropOperation, viewpoint_tool_AbstractVariable, viewpoint_tool_VariableContainer, tool_SubVariable, viewpoint_tool_AcceleoVariable, viewpoint_tool_ChangeContext, viewpoint_tool_SetValue, viewpoint_tool_SetObject, tool_viewpoint_EObject, viewpoint_tool_Unset, viewpoint_tool_MoveElement, viewpoint_tool_CreateInstance, ContainerModelOperation, viewpoint_tool_If, viewpoint_tool_DeleteView, viewpoint_tool_NameVariable, viewpoint_tool_ExternalJavaActionParameter, viewpoint_tool_ToolFilterDescription, tool_FeatureChangeListener, viewpoint_tool_RemoveElement, viewpoint_tool_For, viewpoint_tool_SwitchChild, viewpoint_tool_Default, viewpoint_tool_Switch, tool_Case, tool_Default, viewpoint_validation_ValidationSet, DocumentedElement, validation_ValidationRule, viewpoint_validation_ValidationRule, viewpoint_tool_FeatureChangeListener, viewpoint_tool_Case, SwitchChild, viewpoint_validation_SemanticValidationRule, ValidationRule, viewpoint_validation_ViewValidationRule, RepresentationElementMapping, viewpoint_validation_RuleAudit, viewpoint_validation_ValidationFix, viewpoint_audit_InformationSection, viewpoint_audit_TemplateInformationSection, InformationSection, validation_RuleAudit, validation_ValidationFix, FontFormat, SyncStatus, LabelAlignment, NavigationTargetType, Position, SystemColors, DragSource, ERROR_LEVEL},
    associations={ownedFeatureExtensions11, description13, referencedAnalysis1, models2, eAnnotations4, ownedViews6, selectedViews8, models16, ownedNavigationLinks15, ownedRepresentations29, ownedExtensions32, allRepresentations34, target18, ownedRepresentationElements20, representationElements21, ownedAnnotationEntries24, semanticElements26, data49, hiddenRepresentations37, referencedRepresentations40, viewpoint43, extensionGroup45, description48, description51, ownedSessions57, members59, labelColor60, ownedViewpoints61, systemColorsPalette63, userColorsPalettes65, activatedViewpoints52, analyses54, validationSet67, ownedRepresentations68, ownedRepresentationExtensions70, ownedJavaExtensions72, ownedMMExtensions74, ownedFeatureExtensions76, ownedTemplates79, metamodel81, metamodel84, extensionGroup86, detailDescriptions87, navigationDescriptions88, eAnnotations90, ownedRepresentations82, pasteDescriptions92, decorationDescriptions93, details91, featureCustomizations96, reuse97, appliedOn99, appliedOn102, value104, vsmElementCustomizations95, colorSteps106, associatedColor107, systemColors108, defaultTools110, labelBorderStyles112, entries114, entries115, data116, labelColor118, labelBorderStyleDescriptions119, filters120, element121, elementView122, initialOperation124, container126, containerView127, copiedView129, copiedElement132, initialOperation135, container142, initialOperation144, element147, containerView149, container152, initialOperation155, element138, containerView139, representationDescription158, initialOperation160, containerViewVariable163, representationNameVariable166, representationNameVariable176, item179, view180, initialOperation182, parameters185, action186, menuItemDescription187, representationDescription168, containerViewVariable170, containerVariable173, subModelOperations190, firstModelOperations191, firstModelOperations193, firstModelOperations195, firstModelOperations197, subVariables189, object199, subModelOperations201, cases203, default204, ownedRules206, reusedRules207, allRules210, listeners200, targets216, initialOperation217, audits213, fixes214},
    generalizations={gen_viewpoint_DRepresentationContainer_DView, gen_viewpoint_DRepresentation_description_DocumentedElement, gen_viewpoint_DRepresentation_DRefreshable, gen_viewpoint_DRepresentation_description_DModelElement, gen_viewpoint_DRepresentationElement_DLabelled, gen_viewpoint_DRepresentationElement_DMappingBased, gen_viewpoint_DRepresentationElement_DStylizable, gen_viewpoint_DRepresentationElement_DRefreshable, gen_viewpoint_DRepresentationElement_DSemanticDecorator, gen_viewpoint_DView_DRefreshable, gen_viewpoint_DSourceFileLink_DNavigationLink, gen_viewpoint_LabelStyle_BasicLabelStyle, gen_viewpoint_Style_DRefreshable, gen_viewpoint_Style_Customizable, gen_viewpoint_DFile_DResource, gen_viewpoint_DResourceContainer_DResource, gen_viewpoint_DProject_DResourceContainer, gen_viewpoint_DFolder_DResourceContainer, gen_viewpoint_DModel_DFile, gen_viewpoint_BasicLabelStyle_Customizable, gen_viewpoint_description_Group_description_DModelElement, gen_viewpoint_description_Group_description_DocumentedElement, gen_viewpoint_description_RepresentationDescription_description_DocumentedElement, gen_viewpoint_description_RepresentationDescription_description_EndUserDocumentedElement, gen_viewpoint_description_RepresentationDescription_description_IdentifiedElement, gen_viewpoint_description_Viewpoint_description_DocumentedElement, gen_viewpoint_description_Viewpoint_description_Component, gen_viewpoint_description_Viewpoint_description_EndUserDocumentedElement, gen_viewpoint_description_Viewpoint_description_IdentifiedElement, gen_viewpoint_description_RepresentationElementMapping_IdentifiedElement, gen_viewpoint_description_RepresentationImportDescription_RepresentationDescription, gen_viewpoint_description_SemanticBasedDecoration_DecorationDescription, gen_viewpoint_description_VSMElementCustomizationReuse_IVSMElementCustomization, gen_viewpoint_description_EAttributeCustomization_EStructuralFeatureCustomization, gen_viewpoint_description_EReferenceCustomization_EStructuralFeatureCustomization, gen_viewpoint_description_VSMElementCustomization_IVSMElementCustomization, gen_viewpoint_description_SystemColor_FixedColor, gen_viewpoint_description_InterpolatedColor_description_ColorDescription, gen_viewpoint_description_InterpolatedColor_description_UserColor, gen_viewpoint_description_FixedColor_ColorDescription, gen_viewpoint_description_UserFixedColor_description_FixedColor, gen_viewpoint_description_UserFixedColor_description_UserColor, gen_viewpoint_description_ComputedColor_description_UserColor, gen_viewpoint_description_ComputedColor_description_ColorDescription, gen_viewpoint_style_LabelStyleDescription_BasicLabelStyleDescription, gen_viewpoint_tool_AbstractToolDescription_ToolEntry, gen_viewpoint_tool_MappingBasedToolDescription_AbstractToolDescription, gen_viewpoint_tool_ToolDescription_MappingBasedToolDescription, gen_viewpoint_tool_ToolEntry_description_DocumentedElement, gen_viewpoint_tool_ToolEntry_description_IdentifiedElement, gen_viewpoint_tool_PasteDescription_MappingBasedToolDescription, gen_viewpoint_tool_SelectionWizardDescription_tool_AbstractToolDescription, gen_viewpoint_tool_SelectionWizardDescription_description_SelectionDescription, gen_viewpoint_tool_PaneBasedSelectionWizardDescription_AbstractToolDescription, gen_viewpoint_tool_RepresentationCreationDescription_AbstractToolDescription, gen_viewpoint_tool_RepresentationNavigationDescription_AbstractToolDescription, gen_viewpoint_tool_MenuItemDescription_tool_AbstractToolDescription, gen_viewpoint_tool_MenuItemDescription_tool_MenuItemOrRef, gen_viewpoint_tool_MenuItemDescriptionReference_MenuItemOrRef, gen_viewpoint_tool_OperationAction_MenuItemDescription, gen_viewpoint_tool_ExternalJavaAction_tool_MenuItemDescription, gen_viewpoint_tool_ExternalJavaAction_tool_ContainerModelOperation, gen_viewpoint_tool_ExternalJavaActionCall_tool_MenuItemDescription, gen_viewpoint_tool_ExternalJavaActionCall_tool_ContainerModelOperation, gen_viewpoint_tool_PopupMenu_AbstractToolDescription, gen_viewpoint_tool_AcceleoVariable_tool_VariableContainer, gen_viewpoint_tool_AcceleoVariable_tool_SubVariable, gen_viewpoint_tool_SubVariable_AbstractVariable, gen_viewpoint_tool_DialogVariable_AbstractVariable, gen_viewpoint_tool_ElementDropVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementDropVariable_tool_VariableContainer, gen_viewpoint_tool_ElementSelectVariable_AbstractVariable, gen_viewpoint_tool_ElementVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementVariable_tool_VariableContainer, gen_viewpoint_tool_ElementViewVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementViewVariable_tool_VariableContainer, gen_viewpoint_tool_ElementDeleteVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementDeleteVariable_tool_VariableContainer, gen_viewpoint_tool_DropContainerVariable_tool_AbstractVariable, gen_viewpoint_tool_DropContainerVariable_tool_VariableContainer, gen_viewpoint_tool_SelectContainerVariable_tool_AbstractVariable, gen_viewpoint_tool_SelectContainerVariable_tool_VariableContainer, gen_viewpoint_tool_ContainerViewVariable_tool_AbstractVariable, gen_viewpoint_tool_ContainerViewVariable_tool_VariableContainer, gen_viewpoint_tool_SelectModelElementVariable_tool_SubVariable, gen_viewpoint_tool_SelectModelElementVariable_description_SelectionDescription, gen_viewpoint_tool_ContainerModelOperation_ModelOperation, gen_viewpoint_tool_ChangeContext_ContainerModelOperation, gen_viewpoint_tool_SetValue_ContainerModelOperation, gen_viewpoint_tool_SetObject_ContainerModelOperation, gen_viewpoint_tool_Unset_ContainerModelOperation, gen_viewpoint_tool_MoveElement_ContainerModelOperation, gen_viewpoint_tool_CreateInstance_ContainerModelOperation, gen_viewpoint_tool_If_ContainerModelOperation, gen_viewpoint_tool_DeleteView_ContainerModelOperation, gen_viewpoint_tool_NameVariable_AbstractVariable, gen_viewpoint_tool_RemoveElement_ContainerModelOperation, gen_viewpoint_tool_For_ContainerModelOperation, gen_viewpoint_tool_Default_SwitchChild, gen_viewpoint_tool_Switch_ModelOperation, gen_viewpoint_validation_ValidationSet_DocumentedElement, gen_viewpoint_tool_Case_SwitchChild, gen_viewpoint_validation_SemanticValidationRule_ValidationRule, gen_viewpoint_validation_ViewValidationRule_ValidationRule, gen_viewpoint_audit_TemplateInformationSection_InformationSection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)