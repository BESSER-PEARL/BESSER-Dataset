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
			EnumerationLiteral(name="dark_blue"),
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
			EnumerationLiteral(name="light_gray")
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

ContainerLayout: Enumeration = Enumeration(
    name="ContainerLayout",
    literals={
            EnumerationLiteral(name="FreeForm"),
			EnumerationLiteral(name="List"),
			EnumerationLiteral(name="HorizontalStack"),
			EnumerationLiteral(name="VerticalStack")
    }
)

LabelPosition: Enumeration = Enumeration(
    name="LabelPosition",
    literals={
            EnumerationLiteral(name="border"),
			EnumerationLiteral(name="node")
    }
)

ContainerShape: Enumeration = Enumeration(
    name="ContainerShape",
    literals={
            EnumerationLiteral(name="parallelogram")
    }
)

BackgroundStyle: Enumeration = Enumeration(
    name="BackgroundStyle",
    literals={
            EnumerationLiteral(name="GradientLeftToRight"),
			EnumerationLiteral(name="Liquid"),
			EnumerationLiteral(name="GradientTopToBottom")
    }
)

BundledImageShape: Enumeration = Enumeration(
    name="BundledImageShape",
    literals={
            EnumerationLiteral(name="square"),
			EnumerationLiteral(name="stroke"),
			EnumerationLiteral(name="triangle"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="ring")
    }
)

LineStyle: Enumeration = Enumeration(
    name="LineStyle",
    literals={
            EnumerationLiteral(name="solid"),
			EnumerationLiteral(name="dash"),
			EnumerationLiteral(name="dot"),
			EnumerationLiteral(name="dash_dot")
    }
)

EdgeArrows: Enumeration = Enumeration(
    name="EdgeArrows",
    literals={
            EnumerationLiteral(name="NoDecoration"),
			EnumerationLiteral(name="OutputArrow"),
			EnumerationLiteral(name="InputArrow"),
			EnumerationLiteral(name="InputArrowWithDiamond"),
			EnumerationLiteral(name="InputArrowWithFillDiamond"),
			EnumerationLiteral(name="OutputClosedArrow"),
			EnumerationLiteral(name="InputClosedArrow"),
			EnumerationLiteral(name="OutputFillClosedArrow"),
			EnumerationLiteral(name="InputFillClosedArrow"),
			EnumerationLiteral(name="Diamond"),
			EnumerationLiteral(name="FillDiamond")
    }
)

EdgeRouting: Enumeration = Enumeration(
    name="EdgeRouting",
    literals={
            EnumerationLiteral(name="straight"),
			EnumerationLiteral(name="manhattan"),
			EnumerationLiteral(name="tree")
    }
)

AlignmentKind: Enumeration = Enumeration(
    name="AlignmentKind",
    literals={
            EnumerationLiteral(name="VERTICAL"),
			EnumerationLiteral(name="HORIZONTAL"),
			EnumerationLiteral(name="SQUARE")
    }
)

ArrangeConstraint: Enumeration = Enumeration(
    name="ArrangeConstraint",
    literals={
            EnumerationLiteral(name="KEEP_LOCATION"),
			EnumerationLiteral(name="KEEP_SIZE"),
			EnumerationLiteral(name="KEEP_RATIO")
    }
)

ResizeKind: Enumeration = Enumeration(
    name="ResizeKind",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="NSEW"),
			EnumerationLiteral(name="NORTH_SOUTH"),
			EnumerationLiteral(name="EAST_WEST")
    }
)

FoldingStyle: Enumeration = Enumeration(
    name="FoldingStyle",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="SOURCE"),
			EnumerationLiteral(name="TARGET")
    }
)

LayoutDirection: Enumeration = Enumeration(
    name="LayoutDirection",
    literals={
            EnumerationLiteral(name="TopToBottom"),
			EnumerationLiteral(name="LeftToRight"),
			EnumerationLiteral(name="BottomToTop")
    }
)

ReconnectionKind: Enumeration = Enumeration(
    name="ReconnectionKind",
    literals={
            EnumerationLiteral(name="RECONNECT_TARGET"),
			EnumerationLiteral(name="RECONNECT_SOURCE"),
			EnumerationLiteral(name="RECONNECT_BOTH")
    }
)

FilterKind: Enumeration = Enumeration(
    name="FilterKind",
    literals={
            EnumerationLiteral(name="HIDE"),
			EnumerationLiteral(name="COLLAPSE")
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
viewpoint_DAnalysis = Class(name="viewpoint::DAnalysis")
viewpoint_EObject = Class(name="viewpoint::EObject")
FeatureExtensionDescription = Class(name="FeatureExtensionDescription")
viewpoint_DValidable = Class(name="viewpoint::DValidable", is_abstract=True)
viewpoint_DNavigable = Class(name="viewpoint::DNavigable", is_abstract=True)
viewpoint_DNavigationLink = Class(name="viewpoint::DNavigationLink", is_abstract=True)
viewpoint_DStylizable = Class(name="viewpoint::DStylizable", is_abstract=True)
viewpoint_DRefreshable = Class(name="viewpoint::DRefreshable", is_abstract=True)
viewpoint_DLabelled = Class(name="viewpoint::DLabelled", is_abstract=True)
viewpoint_DMappingBased = Class(name="viewpoint::DMappingBased", is_abstract=True)
viewpoint_DContainer = Class(name="viewpoint::DContainer", is_abstract=True)
viewpoint_DRepresentationContainer = Class(name="viewpoint::DRepresentationContainer")
DView = Class(name="DView")
DAnnotationEntry = Class(name="DAnnotationEntry")
viewpoint_DView = Class(name="viewpoint::DView")
viewpoint_DFeatureExtension = Class(name="viewpoint::DFeatureExtension", is_abstract=True)
description_DModelElement = Class(name="description::DModelElement")
viewpoint_DRepresentationElement = Class(name="viewpoint::DRepresentationElement", is_abstract=True)
AnnotationEntry = Class(name="AnnotationEntry")
DLabelled = Class(name="DLabelled")
DMappingBased = Class(name="DMappingBased")
DStylizable = Class(name="DStylizable")
DSemanticDecorator = Class(name="DSemanticDecorator")
DDiagramSet = Class(name="DDiagramSet")
viewpoint_DSemanticDecorator = Class(name="viewpoint::DSemanticDecorator", is_abstract=True)
viewpoint_DRepresentation = Class(name="viewpoint::DRepresentation", is_abstract=True)
description_DocumentedElement = Class(name="description::DocumentedElement")
DRefreshable = Class(name="DRefreshable")
viewpoint_MetaModelExtension = Class(name="viewpoint::MetaModelExtension")
viewpoint_Decoration = Class(name="viewpoint::Decoration")
DecorationDescription = Class(name="DecorationDescription")
viewpoint_DEObjectLink = Class(name="viewpoint::DEObjectLink")
DNavigationLink = Class(name="DNavigationLink")
Viewpoint = Class(name="Viewpoint")
viewpoint_DAnalysisCustomData = Class(name="viewpoint::DAnalysisCustomData")
viewpoint_LabelStyle = Class(name="viewpoint::LabelStyle")
BasicLabelStyle = Class(name="BasicLabelStyle")
viewpoint_Style = Class(name="viewpoint::Style", is_abstract=True)
Customizable = Class(name="Customizable")
style_StyleDescription = Class(name="style::StyleDescription")
viewpoint_DragAndDropTarget = Class(name="viewpoint::DragAndDropTarget")
viewpoint_DSourceFileLink = Class(name="viewpoint::DSourceFileLink")
viewpoint_SessionManagerEObject = Class(name="viewpoint::SessionManagerEObject")
viewpoint_DResource = Class(name="viewpoint::DResource", is_abstract=True)
viewpoint_DFile = Class(name="viewpoint::DFile")
DResource = Class(name="DResource")
viewpoint_RGBValues = Class(name="viewpoint::RGBValues")
viewpoint_DAnalysisSessionEObject = Class(name="viewpoint::DAnalysisSessionEObject")
viewpoint_DProject = Class(name="viewpoint::DProject")
DResourceContainer = Class(name="DResourceContainer")
viewpoint_DFolder = Class(name="viewpoint::DFolder")
viewpoint_DModel = Class(name="viewpoint::DModel")
DFile = Class(name="DFile")
viewpoint_BasicLabelStyle = Class(name="viewpoint::BasicLabelStyle")
viewpoint_DResourceContainer = Class(name="viewpoint::DResourceContainer")
viewpoint_Customizable = Class(name="viewpoint::Customizable", is_abstract=True)
viewpoint_description_Group = Class(name="viewpoint::description::Group")
validation_ValidationSet = Class(name="validation::ValidationSet")
RepresentationDescription = Class(name="RepresentationDescription")
RepresentationExtensionDescription = Class(name="RepresentationExtensionDescription")
JavaExtension = Class(name="JavaExtension")
MetamodelExtensionSetting = Class(name="MetamodelExtensionSetting")
SytemColorsPalette = Class(name="SytemColorsPalette")
UserColorsPalette = Class(name="UserColorsPalette")
viewpoint_description_Component = Class(name="viewpoint::description::Component", is_abstract=True)
viewpoint_description_Viewpoint = Class(name="viewpoint::description::Viewpoint")
description_Component = Class(name="description::Component")
description_EndUserDocumentedElement = Class(name="description::EndUserDocumentedElement")
description_IdentifiedElement = Class(name="description::IdentifiedElement")
viewpoint_description_MetamodelExtensionSetting = Class(name="viewpoint::description::MetamodelExtensionSetting")
description_viewpoint_EObject = Class(name="description::viewpoint::EObject")
viewpoint_description_JavaExtension = Class(name="viewpoint::description::JavaExtension")
viewpoint_description_RepresentationElementMapping = Class(name="viewpoint::description::RepresentationElementMapping", is_abstract=True)
IdentifiedElement = Class(name="IdentifiedElement")
tool_RepresentationCreationDescription = Class(name="tool::RepresentationCreationDescription")
tool_RepresentationNavigationDescription = Class(name="tool::RepresentationNavigationDescription")
RepresentationTemplate = Class(name="RepresentationTemplate")
viewpoint_description_FeatureExtensionDescription = Class(name="viewpoint::description::FeatureExtensionDescription", is_abstract=True)
viewpoint_description_RepresentationDescription = Class(name="viewpoint::description::RepresentationDescription", is_abstract=True)
description_viewpoint_EPackage = Class(name="description::viewpoint::EPackage")
viewpoint_description_RepresentationTemplate = Class(name="viewpoint::description::RepresentationTemplate", is_abstract=True)
viewpoint_description_RepresentationImportDescription = Class(name="viewpoint::description::RepresentationImportDescription", is_abstract=True)
viewpoint_description_RepresentationExtensionDescription = Class(name="viewpoint::description::RepresentationExtensionDescription", is_abstract=True)
viewpoint_description_DragAndDropTargetDescription = Class(name="viewpoint::description::DragAndDropTargetDescription", is_abstract=True)
tool_ContainerDropDescription = Class(name="tool::ContainerDropDescription")
viewpoint_description_PasteTargetDescription = Class(name="viewpoint::description::PasteTargetDescription", is_abstract=True)
tool_PasteDescription = Class(name="tool::PasteDescription")
viewpoint_description_DecorationDescriptionsSet = Class(name="viewpoint::description::DecorationDescriptionsSet")
viewpoint_description_DecorationDescription = Class(name="viewpoint::description::DecorationDescription", is_abstract=True)
viewpoint_description_AbstractMappingImport = Class(name="viewpoint::description::AbstractMappingImport", is_abstract=True)
viewpoint_description_DocumentedElement = Class(name="viewpoint::description::DocumentedElement", is_abstract=True)
viewpoint_description_DModelElement = Class(name="viewpoint::description::DModelElement", is_abstract=True)
DAnnotation = Class(name="DAnnotation")
viewpoint_description_DAnnotation = Class(name="viewpoint::description::DAnnotation")
description_viewpoint_EStringToStringMapEntry = Class(name="description::viewpoint::EStringToStringMapEntry")
viewpoint_description_ConditionalStyleDescription = Class(name="viewpoint::description::ConditionalStyleDescription", is_abstract=True)
viewpoint_description_VSMElementCustomization = Class(name="viewpoint::description::VSMElementCustomization")
EStructuralFeatureCustomization = Class(name="EStructuralFeatureCustomization")
viewpoint_description_VSMElementCustomizationReuse = Class(name="viewpoint::description::VSMElementCustomizationReuse")
viewpoint_description_EStructuralFeatureCustomization = Class(name="viewpoint::description::EStructuralFeatureCustomization", is_abstract=True)
viewpoint_description_EAttributeCustomization = Class(name="viewpoint::description::EAttributeCustomization")
viewpoint_description_SemanticBasedDecoration = Class(name="viewpoint::description::SemanticBasedDecoration")
viewpoint_description_Customization = Class(name="viewpoint::description::Customization")
IVSMElementCustomization = Class(name="IVSMElementCustomization")
viewpoint_description_IVSMElementCustomization = Class(name="viewpoint::description::IVSMElementCustomization", is_abstract=True)
viewpoint_description_ColorDescription = Class(name="viewpoint::description::ColorDescription", is_abstract=True)
viewpoint_description_SystemColor = Class(name="viewpoint::description::SystemColor")
FixedColor = Class(name="FixedColor")
viewpoint_description_InterpolatedColor = Class(name="viewpoint::description::InterpolatedColor")
description_ColorDescription = Class(name="description::ColorDescription")
description_UserColor = Class(name="description::UserColor")
viewpoint_description_EReferenceCustomization = Class(name="viewpoint::description::EReferenceCustomization")
viewpoint_description_SelectionDescription = Class(name="viewpoint::description::SelectionDescription", is_abstract=True)
ColorStep = Class(name="ColorStep")
viewpoint_description_ColorStep = Class(name="viewpoint::description::ColorStep")
viewpoint_description_FixedColor = Class(name="viewpoint::description::FixedColor")
ColorDescription = Class(name="ColorDescription")
viewpoint_description_UserFixedColor = Class(name="viewpoint::description::UserFixedColor")
description_FixedColor = Class(name="description::FixedColor")
viewpoint_description_UserColor = Class(name="viewpoint::description::UserColor", is_abstract=True)
viewpoint_description_ComputedColor = Class(name="viewpoint::description::ComputedColor")
viewpoint_description_DAnnotationEntry = Class(name="viewpoint::description::DAnnotationEntry")
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
viewpoint_style_LabelBorderStyles = Class(name="viewpoint::style::LabelBorderStyles")
style_LabelBorderStyleDescription = Class(name="style::LabelBorderStyleDescription")
viewpoint_style_LabelBorderStyleDescription = Class(name="viewpoint::style::LabelBorderStyleDescription")
viewpoint_style_TooltipStyleDescription = Class(name="viewpoint::style::TooltipStyleDescription")
viewpoint_tool_ToolEntry = Class(name="viewpoint::tool::ToolEntry", is_abstract=True)
viewpoint_tool_AbstractToolDescription = Class(name="viewpoint::tool::AbstractToolDescription", is_abstract=True)
ToolEntry = Class(name="ToolEntry")
viewpoint_style_StyleDescription = Class(name="viewpoint::style::StyleDescription", is_abstract=True)
viewpoint_style_BasicLabelStyleDescription = Class(name="viewpoint::style::BasicLabelStyleDescription")
viewpoint_style_LabelStyleDescription = Class(name="viewpoint::style::LabelStyleDescription")
BasicLabelStyleDescription = Class(name="BasicLabelStyleDescription")
tool_InitialOperation = Class(name="tool::InitialOperation")
viewpoint_tool_ContainerDropDescription = Class(name="viewpoint::tool::ContainerDropDescription")
description_DiagramElementMapping = Class(name="description::DiagramElementMapping")
tool_DropContainerVariable = Class(name="tool::DropContainerVariable")
tool_ToolFilterDescription = Class(name="tool::ToolFilterDescription")
viewpoint_tool_MappingBasedToolDescription = Class(name="viewpoint::tool::MappingBasedToolDescription", is_abstract=True)
AbstractToolDescription = Class(name="AbstractToolDescription")
viewpoint_tool_ToolDescription = Class(name="viewpoint::tool::ToolDescription")
MappingBasedToolDescription = Class(name="MappingBasedToolDescription")
tool_ElementVariable = Class(name="tool::ElementVariable")
tool_ElementViewVariable = Class(name="tool::ElementViewVariable")
viewpoint_tool_SelectionWizardDescription = Class(name="viewpoint::tool::SelectionWizardDescription")
tool_AbstractToolDescription = Class(name="tool::AbstractToolDescription")
description_SelectionDescription = Class(name="description::SelectionDescription")
tool_ElementSelectVariable = Class(name="tool::ElementSelectVariable")
tool_ElementDropVariable = Class(name="tool::ElementDropVariable")
tool_ContainerViewVariable = Class(name="tool::ContainerViewVariable")
tool_InitialContainerDropOperation = Class(name="tool::InitialContainerDropOperation")
viewpoint_tool_PasteDescription = Class(name="viewpoint::tool::PasteDescription")
tool_SelectContainerVariable = Class(name="tool::SelectContainerVariable")
viewpoint_tool_PaneBasedSelectionWizardDescription = Class(name="viewpoint::tool::PaneBasedSelectionWizardDescription")
tool_NameVariable = Class(name="tool::NameVariable")
viewpoint_tool_RepresentationNavigationDescription = Class(name="viewpoint::tool::RepresentationNavigationDescription", is_abstract=True)
viewpoint_tool_RepresentationCreationDescription = Class(name="viewpoint::tool::RepresentationCreationDescription", is_abstract=True)
viewpoint_tool_ExternalJavaAction = Class(name="viewpoint::tool::ExternalJavaAction")
tool_ContainerModelOperation = Class(name="tool::ContainerModelOperation")
tool_ExternalJavaActionParameter = Class(name="tool::ExternalJavaActionParameter")
viewpoint_tool_ExternalJavaActionCall = Class(name="viewpoint::tool::ExternalJavaActionCall")
tool_ExternalJavaAction = Class(name="tool::ExternalJavaAction")
viewpoint_tool_PopupMenu = Class(name="viewpoint::tool::PopupMenu")
viewpoint_tool_MenuItemOrRef = Class(name="viewpoint::tool::MenuItemOrRef", is_abstract=True)
viewpoint_tool_MenuItemDescription = Class(name="viewpoint::tool::MenuItemDescription", is_abstract=True)
tool_MenuItemOrRef = Class(name="tool::MenuItemOrRef")
viewpoint_tool_MenuItemDescriptionReference = Class(name="viewpoint::tool::MenuItemDescriptionReference")
MenuItemOrRef = Class(name="MenuItemOrRef")
tool_MenuItemDescription = Class(name="tool::MenuItemDescription")
viewpoint_tool_OperationAction = Class(name="viewpoint::tool::OperationAction")
MenuItemDescription = Class(name="MenuItemDescription")
viewpoint_tool_AcceleoVariable = Class(name="viewpoint::tool::AcceleoVariable")
tool_VariableContainer = Class(name="tool::VariableContainer")
viewpoint_tool_SubVariable = Class(name="viewpoint::tool::SubVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
viewpoint_tool_DialogVariable = Class(name="viewpoint::tool::DialogVariable", is_abstract=True)
viewpoint_tool_ElementDropVariable = Class(name="viewpoint::tool::ElementDropVariable")
tool_AbstractVariable = Class(name="tool::AbstractVariable")
viewpoint_tool_AbstractVariable = Class(name="viewpoint::tool::AbstractVariable", is_abstract=True)
viewpoint_tool_VariableContainer = Class(name="viewpoint::tool::VariableContainer", is_abstract=True)
tool_SubVariable = Class(name="tool::SubVariable")
viewpoint_tool_SelectModelElementVariable = Class(name="viewpoint::tool::SelectModelElementVariable")
viewpoint_tool_EditMaskVariables = Class(name="viewpoint::tool::EditMaskVariables")
viewpoint_tool_ContainerModelOperation = Class(name="viewpoint::tool::ContainerModelOperation", is_abstract=True)
ModelOperation = Class(name="ModelOperation")
tool_ModelOperation = Class(name="tool::ModelOperation")
viewpoint_tool_ModelOperation = Class(name="viewpoint::tool::ModelOperation", is_abstract=True)
viewpoint_tool_InitialNodeCreationOperation = Class(name="viewpoint::tool::InitialNodeCreationOperation")
viewpoint_tool_ElementSelectVariable = Class(name="viewpoint::tool::ElementSelectVariable")
viewpoint_tool_ElementVariable = Class(name="viewpoint::tool::ElementVariable")
viewpoint_tool_ElementViewVariable = Class(name="viewpoint::tool::ElementViewVariable")
viewpoint_tool_ElementDeleteVariable = Class(name="viewpoint::tool::ElementDeleteVariable")
viewpoint_tool_DropContainerVariable = Class(name="viewpoint::tool::DropContainerVariable")
viewpoint_tool_SelectContainerVariable = Class(name="viewpoint::tool::SelectContainerVariable")
viewpoint_tool_ContainerViewVariable = Class(name="viewpoint::tool::ContainerViewVariable")
viewpoint_tool_CreateInstance = Class(name="viewpoint::tool::CreateInstance")
ContainerModelOperation = Class(name="ContainerModelOperation")
viewpoint_tool_ChangeContext = Class(name="viewpoint::tool::ChangeContext")
viewpoint_tool_InitialOperation = Class(name="viewpoint::tool::InitialOperation")
viewpoint_tool_InitEdgeCreationOperation = Class(name="viewpoint::tool::InitEdgeCreationOperation")
viewpoint_tool_InitialContainerDropOperation = Class(name="viewpoint::tool::InitialContainerDropOperation")
viewpoint_tool_SetObject = Class(name="viewpoint::tool::SetObject")
tool_viewpoint_EObject = Class(name="tool::viewpoint::EObject")
viewpoint_tool_Unset = Class(name="viewpoint::tool::Unset")
viewpoint_tool_SetValue = Class(name="viewpoint::tool::SetValue")
viewpoint_tool_RemoveElement = Class(name="viewpoint::tool::RemoveElement")
viewpoint_tool_For = Class(name="viewpoint::tool::For")
viewpoint_tool_MoveElement = Class(name="viewpoint::tool::MoveElement")
viewpoint_tool_ToolFilterDescription = Class(name="viewpoint::tool::ToolFilterDescription")
viewpoint_tool_If = Class(name="viewpoint::tool::If")
viewpoint_tool_DeleteView = Class(name="viewpoint::tool::DeleteView")
viewpoint_tool_NameVariable = Class(name="viewpoint::tool::NameVariable")
viewpoint_tool_ExternalJavaActionParameter = Class(name="viewpoint::tool::ExternalJavaActionParameter")
viewpoint_tool_SwitchChild = Class(name="viewpoint::tool::SwitchChild", is_abstract=True)
viewpoint_tool_Default = Class(name="viewpoint::tool::Default")
viewpoint_tool_Switch = Class(name="viewpoint::tool::Switch")
tool_Case = Class(name="tool::Case")
tool_FeatureChangeListener = Class(name="tool::FeatureChangeListener")
viewpoint_tool_FeatureChangeListener = Class(name="viewpoint::tool::FeatureChangeListener")
viewpoint_tool_Case = Class(name="viewpoint::tool::Case")
SwitchChild = Class(name="SwitchChild")
viewpoint_audit_TemplateInformationSection = Class(name="viewpoint::audit::TemplateInformationSection")
InformationSection = Class(name="InformationSection")
viewpoint_diagram_DDiagram = Class(name="viewpoint::diagram::DDiagram")
DRepresentation = Class(name="DRepresentation")
DragAndDropTarget = Class(name="DragAndDropTarget")
DValidable = Class(name="DValidable")
DContainer = Class(name="DContainer")
tool_Default = Class(name="tool::Default")
viewpoint_audit_InformationSection = Class(name="viewpoint::audit::InformationSection", is_abstract=True)
DDiagramElement = Class(name="DDiagramElement")
description_DiagramDescription = Class(name="description::DiagramDescription")
DNode = Class(name="DNode")
DNodeListElement = Class(name="DNodeListElement")
DDiagramElementContainer = Class(name="DDiagramElementContainer")
DDiagram = Class(name="DDiagram")
DEdge = Class(name="DEdge")
validation_ValidationRule = Class(name="validation::ValidationRule")
tool_BehaviorTool = Class(name="tool::BehaviorTool")
FilterVariableHistory = Class(name="FilterVariableHistory")
description_Layer = Class(name="description::Layer")
concern_ConcernDescription = Class(name="concern::ConcernDescription")
filter_FilterDescription = Class(name="filter::FilterDescription")
viewpoint_diagram_DDiagramElement = Class(name="viewpoint::diagram::DDiagramElement", is_abstract=True)
DRepresentationElement = Class(name="DRepresentationElement")
DNavigable = Class(name="DNavigable")
viewpoint_diagram_DSemanticDiagram = Class(name="viewpoint::diagram::DSemanticDiagram")
diagram_DDiagram = Class(name="diagram::DDiagram")
GraphicalFilter = Class(name="GraphicalFilter")
viewpoint_diagram_GraphicalFilter = Class(name="viewpoint::diagram::GraphicalFilter", is_abstract=True)
viewpoint_diagram_HideFilter = Class(name="viewpoint::diagram::HideFilter")
viewpoint_diagram_HideLabelFilter = Class(name="viewpoint::diagram::HideLabelFilter")
viewpoint_diagram_FoldingPointFilter = Class(name="viewpoint::diagram::FoldingPointFilter")
viewpoint_diagram_FoldingFilter = Class(name="viewpoint::diagram::FoldingFilter")
diagram_viewpoint_Decoration = Class(name="diagram::viewpoint::Decoration")
viewpoint_diagram_DDiagramLink = Class(name="viewpoint::diagram::DDiagramLink")
EdgeTarget = Class(name="EdgeTarget")
viewpoint_diagram_AbstractDNode = Class(name="viewpoint::diagram::AbstractDNode", is_abstract=True)
viewpoint_diagram_AppliedCompositeFilters = Class(name="viewpoint::diagram::AppliedCompositeFilters")
filter_CompositeFilterDescription = Class(name="filter::CompositeFilterDescription")
viewpoint_diagram_AbsoluteBoundsFilter = Class(name="viewpoint::diagram::AbsoluteBoundsFilter")
NodeStyle = Class(name="NodeStyle")
viewpoint_diagram_DNode = Class(name="viewpoint::diagram::DNode")
diagram_AbstractDNode = Class(name="diagram::AbstractDNode")
diagram_EdgeTarget = Class(name="diagram::EdgeTarget")
viewpoint_diagram_DDiagramElementContainer = Class(name="viewpoint::diagram::DDiagramElementContainer", is_abstract=True)
diagram_viewpoint_Style = Class(name="diagram::viewpoint::Style")
description_NodeMapping = Class(name="description::NodeMapping")
ContainerStyle = Class(name="ContainerStyle")
viewpoint_diagram_DNodeContainer = Class(name="viewpoint::diagram::DNodeContainer")
viewpoint_diagram_DNodeList = Class(name="viewpoint::diagram::DNodeList")
description_ContainerMapping = Class(name="description::ContainerMapping")
viewpoint_diagram_DNodeListElement = Class(name="viewpoint::diagram::DNodeListElement")
AbstractDNode = Class(name="AbstractDNode")
description_IEdgeMapping = Class(name="description::IEdgeMapping")
viewpoint_diagram_DEdge = Class(name="viewpoint::diagram::DEdge")
diagram_DDiagramElement = Class(name="diagram::DDiagramElement")
EdgeStyle = Class(name="EdgeStyle")
viewpoint_diagram_DDiagramSet = Class(name="viewpoint::diagram::DDiagramSet")
viewpoint_diagram_Dot = Class(name="viewpoint::diagram::Dot")
diagram_viewpoint_RGBValues = Class(name="diagram::viewpoint::RGBValues")
diagram_viewpoint_DRepresentationContainer = Class(name="diagram::viewpoint::DRepresentationContainer")
viewpoint_diagram_NodeStyle = Class(name="viewpoint::diagram::NodeStyle", is_abstract=True)
LabelStyle = Class(name="LabelStyle")
Style = Class(name="Style")
diagram_BorderedStyle = Class(name="diagram::BorderedStyle")
viewpoint_diagram_ContainerStyle = Class(name="viewpoint::diagram::ContainerStyle", is_abstract=True)
viewpoint_diagram_FlatContainerStyle = Class(name="viewpoint::diagram::FlatContainerStyle")
viewpoint_diagram_GaugeSection = Class(name="viewpoint::diagram::GaugeSection")
viewpoint_diagram_Square = Class(name="viewpoint::diagram::Square")
viewpoint_diagram_ShapeContainerStyle = Class(name="viewpoint::diagram::ShapeContainerStyle")
viewpoint_diagram_Lozenge = Class(name="viewpoint::diagram::Lozenge")
viewpoint_diagram_Ellipse = Class(name="viewpoint::diagram::Ellipse")
viewpoint_diagram_WorkspaceImage = Class(name="viewpoint::diagram::WorkspaceImage")
diagram_NodeStyle = Class(name="diagram::NodeStyle")
diagram_ContainerStyle = Class(name="diagram::ContainerStyle")
viewpoint_diagram_CustomStyle = Class(name="viewpoint::diagram::CustomStyle")
viewpoint_diagram_BundledImage = Class(name="viewpoint::diagram::BundledImage")
viewpoint_diagram_EdgeTarget = Class(name="viewpoint::diagram::EdgeTarget", is_abstract=True)
viewpoint_diagram_EdgeStyle = Class(name="viewpoint::diagram::EdgeStyle")
BeginLabelStyle = Class(name="BeginLabelStyle")
CenterLabelStyle = Class(name="CenterLabelStyle")
EndLabelStyle = Class(name="EndLabelStyle")
viewpoint_diagram_GaugeCompositeStyle = Class(name="viewpoint::diagram::GaugeCompositeStyle")
viewpoint_diagram_Note = Class(name="viewpoint::diagram::Note")
viewpoint_diagram_FilterVariableHistory = Class(name="viewpoint::diagram::FilterVariableHistory")
FilterVariableValue = Class(name="FilterVariableValue")
GaugeSection = Class(name="GaugeSection")
viewpoint_diagram_BorderedStyle = Class(name="viewpoint::diagram::BorderedStyle")
viewpoint_diagram_CollapseFilter = Class(name="viewpoint::diagram::CollapseFilter")
viewpoint_diagram_IndirectlyCollapseFilter = Class(name="viewpoint::diagram::IndirectlyCollapseFilter")
CollapseFilter = Class(name="CollapseFilter")
viewpoint_diagram_BeginLabelStyle = Class(name="viewpoint::diagram::BeginLabelStyle")
viewpoint_diagram_FilterVariableValue = Class(name="viewpoint::diagram::FilterVariableValue")
filter_FilterVariable = Class(name="filter::FilterVariable")
diagram_viewpoint_EObject = Class(name="diagram::viewpoint::EObject")
viewpoint_diagram_EndLabelStyle = Class(name="viewpoint::diagram::EndLabelStyle")
viewpoint_diagram_CenterLabelStyle = Class(name="viewpoint::diagram::CenterLabelStyle")
viewpoint_diagram_DiagramElementMapping2ModelElement = Class(name="viewpoint::diagram::DiagramElementMapping2ModelElement")
ModelElement2ViewVariable = Class(name="ModelElement2ViewVariable")
viewpoint_diagram_BracketEdgeStyle = Class(name="viewpoint::diagram::BracketEdgeStyle")
viewpoint_diagram_ComputedStyleDescriptionRegistry = Class(name="viewpoint::diagram::ComputedStyleDescriptionRegistry")
DiagramElementMapping2ModelElement = Class(name="DiagramElementMapping2ModelElement")
ContainerVariable2StyleDescription = Class(name="ContainerVariable2StyleDescription")
viewpoint_diagram_ContainerVariable2StyleDescription = Class(name="viewpoint::diagram::ContainerVariable2StyleDescription")
viewpoint_diagram_ModelElement2ViewVariable = Class(name="viewpoint::diagram::ModelElement2ViewVariable")
ViewVariable2ContainerVariable = Class(name="ViewVariable2ContainerVariable")
viewpoint_diagram_ViewVariable2ContainerVariable = Class(name="viewpoint::diagram::ViewVariable2ContainerVariable")
description_EdgeMapping = Class(name="description::EdgeMapping")
viewpoint_description_DiagramDescription = Class(name="viewpoint::description::DiagramDescription")
description_DragAndDropTargetDescription = Class(name="description::DragAndDropTargetDescription")
description_RepresentationDescription = Class(name="description::RepresentationDescription")
description_PasteTargetDescription = Class(name="description::PasteTargetDescription")
concern_ConcernSet = Class(name="concern::ConcernSet")
description_Layout = Class(name="description::Layout")
description_AdditionalLayer = Class(name="description::AdditionalLayer")
tool_ToolSection = Class(name="tool::ToolSection")
viewpoint_description_DiagramImportDescription = Class(name="viewpoint::description::DiagramImportDescription")
description_RepresentationImportDescription = Class(name="description::RepresentationImportDescription")
viewpoint_description_DiagramExtensionDescription = Class(name="viewpoint::description::DiagramExtensionDescription")
description_EdgeMappingImport = Class(name="description::EdgeMappingImport")
viewpoint_description_DiagramElementMapping = Class(name="viewpoint::description::DiagramElementMapping", is_abstract=True)
description_RepresentationElementMapping = Class(name="description::RepresentationElementMapping")
tool_DeleteElementDescription = Class(name="tool::DeleteElementDescription")
tool_DirectEditLabel = Class(name="tool::DirectEditLabel")
tool_DoubleClickDescription = Class(name="tool::DoubleClickDescription")
viewpoint_description_AbstractNodeMapping = Class(name="viewpoint::description::AbstractNodeMapping", is_abstract=True)
viewpoint_description_NodeMapping = Class(name="viewpoint::description::NodeMapping")
description_AbstractNodeMapping = Class(name="description::AbstractNodeMapping")
style_NodeStyleDescription = Class(name="style::NodeStyleDescription")
description_ConditionalNodeStyleDescription = Class(name="description::ConditionalNodeStyleDescription")
viewpoint_description_ContainerMapping = Class(name="viewpoint::description::ContainerMapping")
style_ContainerStyleDescription = Class(name="style::ContainerStyleDescription")
description_ConditionalContainerStyleDescription = Class(name="description::ConditionalContainerStyleDescription")
viewpoint_description_NodeMappingImport = Class(name="viewpoint::description::NodeMappingImport")
description_AbstractMappingImport = Class(name="description::AbstractMappingImport")
viewpoint_description_ContainerMappingImport = Class(name="viewpoint::description::ContainerMappingImport")
viewpoint_description_EdgeMapping = Class(name="viewpoint::description::EdgeMapping")
description_ConditionalEdgeStyleDescription = Class(name="description::ConditionalEdgeStyleDescription")
style_EdgeStyleDescription = Class(name="style::EdgeStyleDescription")
viewpoint_description_ConditionalNodeStyleDescription = Class(name="viewpoint::description::ConditionalNodeStyleDescription")
ConditionalStyleDescription = Class(name="ConditionalStyleDescription")
viewpoint_description_ConditionalEdgeStyleDescription = Class(name="viewpoint::description::ConditionalEdgeStyleDescription")
tool_ReconnectEdgeDescription = Class(name="tool::ReconnectEdgeDescription")
viewpoint_description_IEdgeMapping = Class(name="viewpoint::description::IEdgeMapping", is_abstract=True)
viewpoint_description_EdgeMappingImport = Class(name="viewpoint::description::EdgeMappingImport")
viewpoint_description_ConditionalContainerStyleDescription = Class(name="viewpoint::description::ConditionalContainerStyleDescription")
viewpoint_description_Layout = Class(name="viewpoint::description::Layout", is_abstract=True)
DocumentedElement = Class(name="DocumentedElement")
viewpoint_description_OrderedTreeLayout = Class(name="viewpoint::description::OrderedTreeLayout")
Layout = Class(name="Layout")
viewpoint_description_CompositeLayout = Class(name="viewpoint::description::CompositeLayout")
viewpoint_description_MappingBasedDecoration = Class(name="viewpoint::description::MappingBasedDecoration")
viewpoint_description_Layer = Class(name="viewpoint::description::Layer")
viewpoint_style_BorderedStyleDescription = Class(name="viewpoint::style::BorderedStyleDescription")
StyleDescription = Class(name="StyleDescription")
DecorationDescriptionsSet = Class(name="DecorationDescriptionsSet")
Customization = Class(name="Customization")
viewpoint_description_AdditionalLayer = Class(name="viewpoint::description::AdditionalLayer")
Layer = Class(name="Layer")
viewpoint_style_NodeStyleDescription = Class(name="viewpoint::style::NodeStyleDescription", is_abstract=True)
style_BorderedStyleDescription = Class(name="style::BorderedStyleDescription")
style_LabelStyleDescription = Class(name="style::LabelStyleDescription")
style_TooltipStyleDescription = Class(name="style::TooltipStyleDescription")
viewpoint_style_CustomStyleDescription = Class(name="viewpoint::style::CustomStyleDescription")
NodeStyleDescription = Class(name="NodeStyleDescription")
viewpoint_style_SquareDescription = Class(name="viewpoint::style::SquareDescription")
viewpoint_style_LozengeNodeDescription = Class(name="viewpoint::style::LozengeNodeDescription")
viewpoint_style_EllipseNodeDescription = Class(name="viewpoint::style::EllipseNodeDescription")
viewpoint_style_BundledImageDescription = Class(name="viewpoint::style::BundledImageDescription")
viewpoint_style_NoteDescription = Class(name="viewpoint::style::NoteDescription")
viewpoint_style_RoundedCornerStyleDescription = Class(name="viewpoint::style::RoundedCornerStyleDescription", is_abstract=True)
viewpoint_style_DotDescription = Class(name="viewpoint::style::DotDescription")
viewpoint_style_GaugeCompositeStyleDescription = Class(name="viewpoint::style::GaugeCompositeStyleDescription")
style_GaugeSectionDescription = Class(name="style::GaugeSectionDescription")
viewpoint_style_GaugeSectionDescription = Class(name="viewpoint::style::GaugeSectionDescription")
viewpoint_style_SizeComputationContainerStyleDescription = Class(name="viewpoint::style::SizeComputationContainerStyleDescription", is_abstract=True)
viewpoint_style_ContainerStyleDescription = Class(name="viewpoint::style::ContainerStyleDescription", is_abstract=True)
style_RoundedCornerStyleDescription = Class(name="style::RoundedCornerStyleDescription")
viewpoint_style_FlatContainerStyleDescription = Class(name="viewpoint::style::FlatContainerStyleDescription")
style_SizeComputationContainerStyleDescription = Class(name="style::SizeComputationContainerStyleDescription")
viewpoint_style_ShapeContainerStyleDescription = Class(name="viewpoint::style::ShapeContainerStyleDescription")
viewpoint_style_WorkspaceImageDescription = Class(name="viewpoint::style::WorkspaceImageDescription")
viewpoint_style_EdgeStyleDescription = Class(name="viewpoint::style::EdgeStyleDescription")
style_BeginLabelStyleDescription = Class(name="style::BeginLabelStyleDescription")
style_CenterLabelStyleDescription = Class(name="style::CenterLabelStyleDescription")
style_EndLabelStyleDescription = Class(name="style::EndLabelStyleDescription")
viewpoint_style_BeginLabelStyleDescription = Class(name="viewpoint::style::BeginLabelStyleDescription")
viewpoint_style_CenterLabelStyleDescription = Class(name="viewpoint::style::CenterLabelStyleDescription")
viewpoint_style_EndLabelStyleDescription = Class(name="viewpoint::style::EndLabelStyleDescription")
viewpoint_style_BracketEdgeStyleDescription = Class(name="viewpoint::style::BracketEdgeStyleDescription")
EdgeStyleDescription = Class(name="EdgeStyleDescription")
viewpoint_tool_ToolSection = Class(name="viewpoint::tool::ToolSection")
tool_ToolGroupExtension = Class(name="tool::ToolGroupExtension")
viewpoint_tool_ToolGroup = Class(name="viewpoint::tool::ToolGroup")
tool_PopupMenu = Class(name="tool::PopupMenu")
viewpoint_tool_ToolGroupExtension = Class(name="viewpoint::tool::ToolGroupExtension")
tool_ToolGroup = Class(name="tool::ToolGroup")
viewpoint_tool_NodeCreationDescription = Class(name="viewpoint::tool::NodeCreationDescription")
tool_NodeCreationVariable = Class(name="tool::NodeCreationVariable")
tool_InitialNodeCreationOperation = Class(name="tool::InitialNodeCreationOperation")
viewpoint_tool_EdgeCreationDescription = Class(name="viewpoint::tool::EdgeCreationDescription")
tool_SourceEdgeCreationVariable = Class(name="tool::SourceEdgeCreationVariable")
tool_TargetEdgeCreationVariable = Class(name="tool::TargetEdgeCreationVariable")
tool_SourceEdgeViewCreationVariable = Class(name="tool::SourceEdgeViewCreationVariable")
tool_TargetEdgeViewCreationVariable = Class(name="tool::TargetEdgeViewCreationVariable")
tool_InitEdgeCreationOperation = Class(name="tool::InitEdgeCreationOperation")
viewpoint_tool_ContainerCreationDescription = Class(name="viewpoint::tool::ContainerCreationDescription")
viewpoint_tool_DeleteElementDescription = Class(name="viewpoint::tool::DeleteElementDescription")
tool_ElementDeleteVariable = Class(name="tool::ElementDeleteVariable")
tool_DeleteHook = Class(name="tool::DeleteHook")
viewpoint_tool_DoubleClickDescription = Class(name="viewpoint::tool::DoubleClickDescription")
tool_ElementDoubleClickVariable = Class(name="tool::ElementDoubleClickVariable")
viewpoint_tool_DeleteHook = Class(name="viewpoint::tool::DeleteHook")
tool_DeleteHookParameter = Class(name="tool::DeleteHookParameter")
viewpoint_tool_DeleteHookParameter = Class(name="viewpoint::tool::DeleteHookParameter")
viewpoint_tool_ReconnectEdgeDescription = Class(name="viewpoint::tool::ReconnectEdgeDescription")
viewpoint_tool_RequestDescription = Class(name="viewpoint::tool::RequestDescription")
viewpoint_tool_DirectEditLabel = Class(name="viewpoint::tool::DirectEditLabel")
tool_EditMaskVariables = Class(name="tool::EditMaskVariables")
viewpoint_tool_BehaviorTool = Class(name="viewpoint::tool::BehaviorTool")
viewpoint_tool_SourceEdgeCreationVariable = Class(name="viewpoint::tool::SourceEdgeCreationVariable")
viewpoint_tool_SourceEdgeViewCreationVariable = Class(name="viewpoint::tool::SourceEdgeViewCreationVariable")
viewpoint_tool_TargetEdgeCreationVariable = Class(name="viewpoint::tool::TargetEdgeCreationVariable")
viewpoint_tool_TargetEdgeViewCreationVariable = Class(name="viewpoint::tool::TargetEdgeViewCreationVariable")
viewpoint_tool_ElementDoubleClickVariable = Class(name="viewpoint::tool::ElementDoubleClickVariable")
viewpoint_tool_NodeCreationVariable = Class(name="viewpoint::tool::NodeCreationVariable")
viewpoint_tool_CreateView = Class(name="viewpoint::tool::CreateView")
viewpoint_tool_CreateEdgeView = Class(name="viewpoint::tool::CreateEdgeView")
CreateView = Class(name="CreateView")
viewpoint_tool_DiagramCreationDescription = Class(name="viewpoint::tool::DiagramCreationDescription")
RepresentationCreationDescription = Class(name="RepresentationCreationDescription")
viewpoint_tool_DiagramNavigationDescription = Class(name="viewpoint::tool::DiagramNavigationDescription")
RepresentationNavigationDescription = Class(name="RepresentationNavigationDescription")
viewpoint_filter_FilterDescription = Class(name="viewpoint::filter::FilterDescription", is_abstract=True)
viewpoint_filter_Filter = Class(name="viewpoint::filter::Filter", is_abstract=True)
viewpoint_filter_MappingFilter = Class(name="viewpoint::filter::MappingFilter")
Filter = Class(name="Filter")
filter_Filter = Class(name="filter::Filter")
viewpoint_tool_Navigation = Class(name="viewpoint::tool::Navigation")
viewpoint_filter_VariableFilter = Class(name="viewpoint::filter::VariableFilter")
viewpoint_filter_FilterVariable = Class(name="viewpoint::filter::FilterVariable")
SelectionDescription = Class(name="SelectionDescription")
viewpoint_validation_ValidationSet = Class(name="viewpoint::validation::ValidationSet")
viewpoint_filter_CompositeFilterDescription = Class(name="viewpoint::filter::CompositeFilterDescription")
FilterDescription = Class(name="FilterDescription")
validation_RuleAudit = Class(name="validation::RuleAudit")
validation_ValidationFix = Class(name="validation::ValidationFix")
viewpoint_validation_SemanticValidationRule = Class(name="viewpoint::validation::SemanticValidationRule")
ValidationRule = Class(name="ValidationRule")
viewpoint_validation_ViewValidationRule = Class(name="viewpoint::validation::ViewValidationRule")
viewpoint_validation_RuleAudit = Class(name="viewpoint::validation::RuleAudit")
viewpoint_validation_ValidationRule = Class(name="viewpoint::validation::ValidationRule", is_abstract=True)
viewpoint_concern_ConcernSet = Class(name="viewpoint::concern::ConcernSet")
viewpoint_concern_ConcernDescription = Class(name="viewpoint::concern::ConcernDescription")
viewpoint_validation_ValidationFix = Class(name="viewpoint::validation::ValidationFix")

# viewpoint_DAnalysis class attributes and methods
viewpoint_DAnalysis_version: Property = Property(name="version", type=StringType)
viewpoint_DAnalysis.attributes={viewpoint_DAnalysis_version}

# viewpoint_EObject class attributes and methods

# FeatureExtensionDescription class attributes and methods

# viewpoint_DValidable class attributes and methods
viewpoint_DValidable_m_validate: Method = Method(name="validate", parameters={}, type=BooleanType)
viewpoint_DValidable.methods={viewpoint_DValidable_m_validate}

# viewpoint_DNavigable class attributes and methods

# viewpoint_DNavigationLink class attributes and methods
viewpoint_DNavigationLink_targetType: Property = Property(name="targetType", type=StringType)
viewpoint_DNavigationLink_label: Property = Property(name="label", type=StringType)
viewpoint_DNavigationLink_m_isAvailable: Method = Method(name="isAvailable", parameters={}, type=BooleanType)
viewpoint_DNavigationLink.attributes={viewpoint_DNavigationLink_targetType, viewpoint_DNavigationLink_label}
viewpoint_DNavigationLink.methods={viewpoint_DNavigationLink_m_isAvailable}

# viewpoint_DStylizable class attributes and methods
viewpoint_DStylizable_m_getStyle: Method = Method(name="getStyle", parameters={}, type=StringType)
viewpoint_DStylizable.methods={viewpoint_DStylizable_m_getStyle}

# viewpoint_DRefreshable class attributes and methods
viewpoint_DRefreshable_m_refresh: Method = Method(name="refresh", parameters={})
viewpoint_DRefreshable.methods={viewpoint_DRefreshable_m_refresh}

# viewpoint_DLabelled class attributes and methods

# viewpoint_DMappingBased class attributes and methods
viewpoint_DMappingBased_m_getMapping: Method = Method(name="getMapping", parameters={}, type=StringType)
viewpoint_DMappingBased.methods={viewpoint_DMappingBased_m_getMapping}

# viewpoint_DContainer class attributes and methods

# viewpoint_DRepresentationContainer class attributes and methods
viewpoint_DRepresentationContainer_m_addSemanticDiagram: Method = Method(name="addSemanticDiagram", parameters={Parameter(name='diagram')})
viewpoint_DRepresentationContainer.methods={viewpoint_DRepresentationContainer_m_addSemanticDiagram}

# DView class attributes and methods

# DAnnotationEntry class attributes and methods

# viewpoint_DView class attributes and methods
viewpoint_DView_initialized: Property = Property(name="initialized", type=BooleanType)
viewpoint_DView.attributes={viewpoint_DView_initialized}

# viewpoint_DFeatureExtension class attributes and methods

# description_DModelElement class attributes and methods

# viewpoint_DRepresentationElement class attributes and methods
viewpoint_DRepresentationElement_name: Property = Property(name="name", type=StringType)
viewpoint_DRepresentationElement.attributes={viewpoint_DRepresentationElement_name}

# AnnotationEntry class attributes and methods

# DLabelled class attributes and methods

# DMappingBased class attributes and methods

# DStylizable class attributes and methods

# DSemanticDecorator class attributes and methods

# DDiagramSet class attributes and methods

# viewpoint_DSemanticDecorator class attributes and methods

# viewpoint_DRepresentation class attributes and methods
viewpoint_DRepresentation_name: Property = Property(name="name", type=StringType)
viewpoint_DRepresentation_m_createContents: Method = Method(name="createContents", parameters={})
viewpoint_DRepresentation_m_createContents: Method = Method(name="createContents", parameters={Parameter(name='rootElement')})
viewpoint_DRepresentation_m_updateContent: Method = Method(name="updateContent", parameters={})
viewpoint_DRepresentation.attributes={viewpoint_DRepresentation_name}
viewpoint_DRepresentation.methods={viewpoint_DRepresentation_m_createContents, viewpoint_DRepresentation_m_updateContent, viewpoint_DRepresentation_m_createContents}

# description_DocumentedElement class attributes and methods

# DRefreshable class attributes and methods

# viewpoint_MetaModelExtension class attributes and methods

# viewpoint_Decoration class attributes and methods

# DecorationDescription class attributes and methods

# viewpoint_DEObjectLink class attributes and methods

# DNavigationLink class attributes and methods

# Viewpoint class attributes and methods

# viewpoint_DAnalysisCustomData class attributes and methods
viewpoint_DAnalysisCustomData_key: Property = Property(name="key", type=StringType)
viewpoint_DAnalysisCustomData.attributes={viewpoint_DAnalysisCustomData_key}

# viewpoint_LabelStyle class attributes and methods
viewpoint_LabelStyle_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
viewpoint_LabelStyle.attributes={viewpoint_LabelStyle_labelAlignment}

# BasicLabelStyle class attributes and methods

# viewpoint_Style class attributes and methods

# Customizable class attributes and methods

# style_StyleDescription class attributes and methods

# viewpoint_DragAndDropTarget class attributes and methods
viewpoint_DragAndDropTarget_m_getDragAndDropDescription: Method = Method(name="getDragAndDropDescription", parameters={}, type=StringType)
viewpoint_DragAndDropTarget.methods={viewpoint_DragAndDropTarget_m_getDragAndDropDescription}

# viewpoint_DSourceFileLink class attributes and methods
viewpoint_DSourceFileLink_endPosition: Property = Property(name="endPosition", type=IntegerType)
viewpoint_DSourceFileLink_filePath: Property = Property(name="filePath", type=StringType)
viewpoint_DSourceFileLink_startPosition: Property = Property(name="startPosition", type=IntegerType)
viewpoint_DSourceFileLink.attributes={viewpoint_DSourceFileLink_endPosition, viewpoint_DSourceFileLink_startPosition, viewpoint_DSourceFileLink_filePath}

# viewpoint_SessionManagerEObject class attributes and methods

# viewpoint_DResource class attributes and methods
viewpoint_DResource_name: Property = Property(name="name", type=StringType)
viewpoint_DResource_path: Property = Property(name="path", type=StringType)
viewpoint_DResource.attributes={viewpoint_DResource_path, viewpoint_DResource_name}

# viewpoint_DFile class attributes and methods

# DResource class attributes and methods

# viewpoint_RGBValues class attributes and methods
viewpoint_RGBValues_red: Property = Property(name="red", type=IntegerType)
viewpoint_RGBValues_green: Property = Property(name="green", type=IntegerType)
viewpoint_RGBValues_blue: Property = Property(name="blue", type=IntegerType)
viewpoint_RGBValues.attributes={viewpoint_RGBValues_green, viewpoint_RGBValues_blue, viewpoint_RGBValues_red}

# viewpoint_DAnalysisSessionEObject class attributes and methods
viewpoint_DAnalysisSessionEObject_open: Property = Property(name="open", type=BooleanType)
viewpoint_DAnalysisSessionEObject_blocked: Property = Property(name="blocked", type=BooleanType)
viewpoint_DAnalysisSessionEObject_resources: Property = Property(name="resources", type=StringType)
viewpoint_DAnalysisSessionEObject_controlledResources: Property = Property(name="controlledResources", type=StringType)
viewpoint_DAnalysisSessionEObject_synchronizationStatus: Property = Property(name="synchronizationStatus", type=StringType)
viewpoint_DAnalysisSessionEObject.attributes={viewpoint_DAnalysisSessionEObject_controlledResources, viewpoint_DAnalysisSessionEObject_open, viewpoint_DAnalysisSessionEObject_resources, viewpoint_DAnalysisSessionEObject_blocked, viewpoint_DAnalysisSessionEObject_synchronizationStatus}

# viewpoint_DProject class attributes and methods

# DResourceContainer class attributes and methods

# viewpoint_DFolder class attributes and methods

# viewpoint_DModel class attributes and methods

# DFile class attributes and methods

# viewpoint_BasicLabelStyle class attributes and methods
viewpoint_BasicLabelStyle_labelSize: Property = Property(name="labelSize", type=IntegerType)
viewpoint_BasicLabelStyle_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_BasicLabelStyle_labelFormat: Property = Property(name="labelFormat", type=StringType)
viewpoint_BasicLabelStyle_showIcon: Property = Property(name="showIcon", type=BooleanType)
viewpoint_BasicLabelStyle.attributes={viewpoint_BasicLabelStyle_iconPath, viewpoint_BasicLabelStyle_labelSize, viewpoint_BasicLabelStyle_showIcon, viewpoint_BasicLabelStyle_labelFormat}

# viewpoint_DResourceContainer class attributes and methods

# viewpoint_Customizable class attributes and methods
viewpoint_Customizable_customFeatures: Property = Property(name="customFeatures", type=StringType)
viewpoint_Customizable.attributes={viewpoint_Customizable_customFeatures}

# viewpoint_description_Group class attributes and methods
viewpoint_description_Group_name: Property = Property(name="name", type=StringType)
viewpoint_description_Group_version: Property = Property(name="version", type=StringType)
viewpoint_description_Group.attributes={viewpoint_description_Group_version, viewpoint_description_Group_name}

# validation_ValidationSet class attributes and methods

# RepresentationDescription class attributes and methods

# RepresentationExtensionDescription class attributes and methods

# JavaExtension class attributes and methods

# MetamodelExtensionSetting class attributes and methods

# SytemColorsPalette class attributes and methods

# UserColorsPalette class attributes and methods

# viewpoint_description_Component class attributes and methods

# viewpoint_description_Viewpoint class attributes and methods
viewpoint_description_Viewpoint_modelFileExtension: Property = Property(name="modelFileExtension", type=StringType)
viewpoint_description_Viewpoint_icon: Property = Property(name="icon", type=StringType)
viewpoint_description_Viewpoint_conflicts: Property = Property(name="conflicts", type=StringType)
viewpoint_description_Viewpoint_reuses: Property = Property(name="reuses", type=StringType)
viewpoint_description_Viewpoint_customizes: Property = Property(name="customizes", type=StringType)
viewpoint_description_Viewpoint_m_initView: Method = Method(name="initView", parameters={Parameter(name='model')})
viewpoint_description_Viewpoint.attributes={viewpoint_description_Viewpoint_customizes, viewpoint_description_Viewpoint_reuses, viewpoint_description_Viewpoint_conflicts, viewpoint_description_Viewpoint_icon, viewpoint_description_Viewpoint_modelFileExtension}
viewpoint_description_Viewpoint.methods={viewpoint_description_Viewpoint_m_initView}

# description_Component class attributes and methods

# description_EndUserDocumentedElement class attributes and methods

# description_IdentifiedElement class attributes and methods

# viewpoint_description_MetamodelExtensionSetting class attributes and methods

# description_viewpoint_EObject class attributes and methods

# viewpoint_description_JavaExtension class attributes and methods
viewpoint_description_JavaExtension_qualifiedClassName: Property = Property(name="qualifiedClassName", type=StringType)
viewpoint_description_JavaExtension.attributes={viewpoint_description_JavaExtension_qualifiedClassName}

# viewpoint_description_RepresentationElementMapping class attributes and methods

# IdentifiedElement class attributes and methods

# tool_RepresentationCreationDescription class attributes and methods

# tool_RepresentationNavigationDescription class attributes and methods

# RepresentationTemplate class attributes and methods

# viewpoint_description_FeatureExtensionDescription class attributes and methods

# viewpoint_description_RepresentationDescription class attributes and methods
viewpoint_description_RepresentationDescription_titleExpression: Property = Property(name="titleExpression", type=StringType)
viewpoint_description_RepresentationDescription_initialisation: Property = Property(name="initialisation", type=BooleanType)
viewpoint_description_RepresentationDescription_showOnStartup: Property = Property(name="showOnStartup", type=BooleanType)
viewpoint_description_RepresentationDescription.attributes={viewpoint_description_RepresentationDescription_titleExpression, viewpoint_description_RepresentationDescription_showOnStartup, viewpoint_description_RepresentationDescription_initialisation}

# description_viewpoint_EPackage class attributes and methods

# viewpoint_description_RepresentationTemplate class attributes and methods
viewpoint_description_RepresentationTemplate_name: Property = Property(name="name", type=StringType)
viewpoint_description_RepresentationTemplate.attributes={viewpoint_description_RepresentationTemplate_name}

# viewpoint_description_RepresentationImportDescription class attributes and methods

# viewpoint_description_RepresentationExtensionDescription class attributes and methods
viewpoint_description_RepresentationExtensionDescription_representationName: Property = Property(name="representationName", type=StringType)
viewpoint_description_RepresentationExtensionDescription_name: Property = Property(name="name", type=StringType)
viewpoint_description_RepresentationExtensionDescription_viewpointURI: Property = Property(name="viewpointURI", type=StringType)
viewpoint_description_RepresentationExtensionDescription.attributes={viewpoint_description_RepresentationExtensionDescription_name, viewpoint_description_RepresentationExtensionDescription_viewpointURI, viewpoint_description_RepresentationExtensionDescription_representationName}

# viewpoint_description_DragAndDropTargetDescription class attributes and methods

# tool_ContainerDropDescription class attributes and methods

# viewpoint_description_PasteTargetDescription class attributes and methods

# tool_PasteDescription class attributes and methods

# viewpoint_description_DecorationDescriptionsSet class attributes and methods

# viewpoint_description_DecorationDescription class attributes and methods
viewpoint_description_DecorationDescription_name: Property = Property(name="name", type=StringType)
viewpoint_description_DecorationDescription_position: Property = Property(name="position", type=StringType)
viewpoint_description_DecorationDescription_decoratorPath: Property = Property(name="decoratorPath", type=StringType)
viewpoint_description_DecorationDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
viewpoint_description_DecorationDescription.attributes={viewpoint_description_DecorationDescription_name, viewpoint_description_DecorationDescription_decoratorPath, viewpoint_description_DecorationDescription_preconditionExpression, viewpoint_description_DecorationDescription_position}

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

# viewpoint_description_ConditionalStyleDescription class attributes and methods
viewpoint_description_ConditionalStyleDescription_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
viewpoint_description_ConditionalStyleDescription_m_checkPredicate: Method = Method(name="checkPredicate", parameters={Parameter(name='modelElement'), Parameter(name='viewVariable'), Parameter(name='containerVariable')}, type=BooleanType)
viewpoint_description_ConditionalStyleDescription.attributes={viewpoint_description_ConditionalStyleDescription_predicateExpression}
viewpoint_description_ConditionalStyleDescription.methods={viewpoint_description_ConditionalStyleDescription_m_checkPredicate}

# viewpoint_description_VSMElementCustomization class attributes and methods
viewpoint_description_VSMElementCustomization_predicateExpression: Property = Property(name="predicateExpression", type=StringType)
viewpoint_description_VSMElementCustomization.attributes={viewpoint_description_VSMElementCustomization_predicateExpression}

# EStructuralFeatureCustomization class attributes and methods

# viewpoint_description_VSMElementCustomizationReuse class attributes and methods

# viewpoint_description_EStructuralFeatureCustomization class attributes and methods
viewpoint_description_EStructuralFeatureCustomization_applyOnAll: Property = Property(name="applyOnAll", type=BooleanType)
viewpoint_description_EStructuralFeatureCustomization.attributes={viewpoint_description_EStructuralFeatureCustomization_applyOnAll}

# viewpoint_description_EAttributeCustomization class attributes and methods
viewpoint_description_EAttributeCustomization_attributeName: Property = Property(name="attributeName", type=StringType)
viewpoint_description_EAttributeCustomization_value: Property = Property(name="value", type=StringType)
viewpoint_description_EAttributeCustomization.attributes={viewpoint_description_EAttributeCustomization_value, viewpoint_description_EAttributeCustomization_attributeName}

# viewpoint_description_SemanticBasedDecoration class attributes and methods
viewpoint_description_SemanticBasedDecoration_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_description_SemanticBasedDecoration.attributes={viewpoint_description_SemanticBasedDecoration_domainClass}

# viewpoint_description_Customization class attributes and methods

# IVSMElementCustomization class attributes and methods

# viewpoint_description_IVSMElementCustomization class attributes and methods

# viewpoint_description_ColorDescription class attributes and methods

# viewpoint_description_SystemColor class attributes and methods
viewpoint_description_SystemColor_name: Property = Property(name="name", type=StringType)
viewpoint_description_SystemColor.attributes={viewpoint_description_SystemColor_name}

# FixedColor class attributes and methods

# viewpoint_description_InterpolatedColor class attributes and methods
viewpoint_description_InterpolatedColor_colorValueComputationExpression: Property = Property(name="colorValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor_minValueComputationExpression: Property = Property(name="minValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor_maxValueComputationExpression: Property = Property(name="maxValueComputationExpression", type=StringType)
viewpoint_description_InterpolatedColor.attributes={viewpoint_description_InterpolatedColor_maxValueComputationExpression, viewpoint_description_InterpolatedColor_minValueComputationExpression, viewpoint_description_InterpolatedColor_colorValueComputationExpression}

# description_ColorDescription class attributes and methods

# description_UserColor class attributes and methods

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
viewpoint_description_SelectionDescription.attributes={viewpoint_description_SelectionDescription_multiple, viewpoint_description_SelectionDescription_rootExpression, viewpoint_description_SelectionDescription_message, viewpoint_description_SelectionDescription_tree, viewpoint_description_SelectionDescription_childrenExpression, viewpoint_description_SelectionDescription_candidatesExpression}

# ColorStep class attributes and methods

# viewpoint_description_ColorStep class attributes and methods
viewpoint_description_ColorStep_associatedValue: Property = Property(name="associatedValue", type=StringType)
viewpoint_description_ColorStep.attributes={viewpoint_description_ColorStep_associatedValue}

# viewpoint_description_FixedColor class attributes and methods
viewpoint_description_FixedColor_red: Property = Property(name="red", type=IntegerType)
viewpoint_description_FixedColor_green: Property = Property(name="green", type=IntegerType)
viewpoint_description_FixedColor_blue: Property = Property(name="blue", type=IntegerType)
viewpoint_description_FixedColor.attributes={viewpoint_description_FixedColor_blue, viewpoint_description_FixedColor_green, viewpoint_description_FixedColor_red}

# ColorDescription class attributes and methods

# viewpoint_description_UserFixedColor class attributes and methods

# description_FixedColor class attributes and methods

# viewpoint_description_UserColor class attributes and methods
viewpoint_description_UserColor_name: Property = Property(name="name", type=StringType)
viewpoint_description_UserColor.attributes={viewpoint_description_UserColor_name}

# viewpoint_description_ComputedColor class attributes and methods
viewpoint_description_ComputedColor_red: Property = Property(name="red", type=StringType)
viewpoint_description_ComputedColor_green: Property = Property(name="green", type=StringType)
viewpoint_description_ComputedColor_blue: Property = Property(name="blue", type=StringType)
viewpoint_description_ComputedColor.attributes={viewpoint_description_ComputedColor_blue, viewpoint_description_ComputedColor_green, viewpoint_description_ComputedColor_red}

# viewpoint_description_DAnnotationEntry class attributes and methods
viewpoint_description_DAnnotationEntry_source: Property = Property(name="source", type=StringType)
viewpoint_description_DAnnotationEntry_details: Property = Property(name="details", type=StringType)
viewpoint_description_DAnnotationEntry.attributes={viewpoint_description_DAnnotationEntry_source, viewpoint_description_DAnnotationEntry_details}

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
viewpoint_description_IdentifiedElement_label: Property = Property(name="label", type=StringType)
viewpoint_description_IdentifiedElement_name: Property = Property(name="name", type=StringType)
viewpoint_description_IdentifiedElement.attributes={viewpoint_description_IdentifiedElement_name, viewpoint_description_IdentifiedElement_label}

# viewpoint_style_LabelBorderStyles class attributes and methods

# style_LabelBorderStyleDescription class attributes and methods

# viewpoint_style_LabelBorderStyleDescription class attributes and methods
viewpoint_style_LabelBorderStyleDescription_id: Property = Property(name="id", type=StringType)
viewpoint_style_LabelBorderStyleDescription_name: Property = Property(name="name", type=StringType)
viewpoint_style_LabelBorderStyleDescription_cornerHeight: Property = Property(name="cornerHeight", type=IntegerType)
viewpoint_style_LabelBorderStyleDescription_cornerWidth: Property = Property(name="cornerWidth", type=IntegerType)
viewpoint_style_LabelBorderStyleDescription.attributes={viewpoint_style_LabelBorderStyleDescription_id, viewpoint_style_LabelBorderStyleDescription_cornerWidth, viewpoint_style_LabelBorderStyleDescription_cornerHeight, viewpoint_style_LabelBorderStyleDescription_name}

# viewpoint_style_TooltipStyleDescription class attributes and methods
viewpoint_style_TooltipStyleDescription_tooltipExpression: Property = Property(name="tooltipExpression", type=StringType)
viewpoint_style_TooltipStyleDescription.attributes={viewpoint_style_TooltipStyleDescription_tooltipExpression}

# viewpoint_tool_ToolEntry class attributes and methods

# viewpoint_tool_AbstractToolDescription class attributes and methods
viewpoint_tool_AbstractToolDescription_precondition: Property = Property(name="precondition", type=StringType)
viewpoint_tool_AbstractToolDescription_forceRefresh: Property = Property(name="forceRefresh", type=BooleanType)
viewpoint_tool_AbstractToolDescription.attributes={viewpoint_tool_AbstractToolDescription_forceRefresh, viewpoint_tool_AbstractToolDescription_precondition}

# ToolEntry class attributes and methods

# viewpoint_style_StyleDescription class attributes and methods

# viewpoint_style_BasicLabelStyleDescription class attributes and methods
viewpoint_style_BasicLabelStyleDescription_labelSize: Property = Property(name="labelSize", type=IntegerType)
viewpoint_style_BasicLabelStyleDescription_labelFormat: Property = Property(name="labelFormat", type=StringType)
viewpoint_style_BasicLabelStyleDescription_showIcon: Property = Property(name="showIcon", type=BooleanType)
viewpoint_style_BasicLabelStyleDescription_labelExpression: Property = Property(name="labelExpression", type=StringType)
viewpoint_style_BasicLabelStyleDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_style_BasicLabelStyleDescription.attributes={viewpoint_style_BasicLabelStyleDescription_iconPath, viewpoint_style_BasicLabelStyleDescription_labelSize, viewpoint_style_BasicLabelStyleDescription_labelFormat, viewpoint_style_BasicLabelStyleDescription_labelExpression, viewpoint_style_BasicLabelStyleDescription_showIcon}

# viewpoint_style_LabelStyleDescription class attributes and methods
viewpoint_style_LabelStyleDescription_labelAlignment: Property = Property(name="labelAlignment", type=StringType)
viewpoint_style_LabelStyleDescription.attributes={viewpoint_style_LabelStyleDescription_labelAlignment}

# BasicLabelStyleDescription class attributes and methods

# tool_InitialOperation class attributes and methods

# viewpoint_tool_ContainerDropDescription class attributes and methods
viewpoint_tool_ContainerDropDescription_dragSource: Property = Property(name="dragSource", type=StringType)
viewpoint_tool_ContainerDropDescription_moveEdges: Property = Property(name="moveEdges", type=BooleanType)
viewpoint_tool_ContainerDropDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='targetContainer'), Parameter(name='droppedElement')}, type=StringType)
viewpoint_tool_ContainerDropDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
viewpoint_tool_ContainerDropDescription.attributes={viewpoint_tool_ContainerDropDescription_moveEdges, viewpoint_tool_ContainerDropDescription_dragSource}
viewpoint_tool_ContainerDropDescription.methods={viewpoint_tool_ContainerDropDescription_m_getContainers, viewpoint_tool_ContainerDropDescription_m_getBestMapping}

# description_DiagramElementMapping class attributes and methods

# tool_DropContainerVariable class attributes and methods

# tool_ToolFilterDescription class attributes and methods

# viewpoint_tool_MappingBasedToolDescription class attributes and methods

# AbstractToolDescription class attributes and methods

# viewpoint_tool_ToolDescription class attributes and methods
viewpoint_tool_ToolDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_ToolDescription.attributes={viewpoint_tool_ToolDescription_iconPath}

# MappingBasedToolDescription class attributes and methods

# tool_ElementVariable class attributes and methods

# tool_ElementViewVariable class attributes and methods

# viewpoint_tool_SelectionWizardDescription class attributes and methods
viewpoint_tool_SelectionWizardDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_SelectionWizardDescription_windowTitle: Property = Property(name="windowTitle", type=StringType)
viewpoint_tool_SelectionWizardDescription_windowImagePath: Property = Property(name="windowImagePath", type=StringType)
viewpoint_tool_SelectionWizardDescription.attributes={viewpoint_tool_SelectionWizardDescription_iconPath, viewpoint_tool_SelectionWizardDescription_windowTitle, viewpoint_tool_SelectionWizardDescription_windowImagePath}

# tool_AbstractToolDescription class attributes and methods

# description_SelectionDescription class attributes and methods

# tool_ElementSelectVariable class attributes and methods

# tool_ElementDropVariable class attributes and methods

# tool_ContainerViewVariable class attributes and methods

# tool_InitialContainerDropOperation class attributes and methods

# viewpoint_tool_PasteDescription class attributes and methods
viewpoint_tool_PasteDescription_m_getContainers: Method = Method(name="getContainers", parameters={}, type=StringType)
viewpoint_tool_PasteDescription.methods={viewpoint_tool_PasteDescription_m_getContainers}

# tool_SelectContainerVariable class attributes and methods

# viewpoint_tool_PaneBasedSelectionWizardDescription class attributes and methods
viewpoint_tool_PaneBasedSelectionWizardDescription_windowImagePath: Property = Property(name="windowImagePath", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_message: Property = Property(name="message", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_choiceOfValuesMessage: Property = Property(name="choiceOfValuesMessage", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_candidatesExpression: Property = Property(name="candidatesExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_tree: Property = Property(name="tree", type=BooleanType)
viewpoint_tool_PaneBasedSelectionWizardDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_windowTitle: Property = Property(name="windowTitle", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_selectedValuesMessage: Property = Property(name="selectedValuesMessage", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription_preSelectedCandidatesExpression: Property = Property(name="preSelectedCandidatesExpression", type=StringType)
viewpoint_tool_PaneBasedSelectionWizardDescription.attributes={viewpoint_tool_PaneBasedSelectionWizardDescription_iconPath, viewpoint_tool_PaneBasedSelectionWizardDescription_preSelectedCandidatesExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_rootExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_windowTitle, viewpoint_tool_PaneBasedSelectionWizardDescription_message, viewpoint_tool_PaneBasedSelectionWizardDescription_tree, viewpoint_tool_PaneBasedSelectionWizardDescription_windowImagePath, viewpoint_tool_PaneBasedSelectionWizardDescription_candidatesExpression, viewpoint_tool_PaneBasedSelectionWizardDescription_selectedValuesMessage, viewpoint_tool_PaneBasedSelectionWizardDescription_choiceOfValuesMessage, viewpoint_tool_PaneBasedSelectionWizardDescription_childrenExpression}

# tool_NameVariable class attributes and methods

# viewpoint_tool_RepresentationNavigationDescription class attributes and methods
viewpoint_tool_RepresentationNavigationDescription_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_RepresentationNavigationDescription_navigationNameExpression: Property = Property(name="navigationNameExpression", type=StringType)
viewpoint_tool_RepresentationNavigationDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_RepresentationNavigationDescription.attributes={viewpoint_tool_RepresentationNavigationDescription_browseExpression, viewpoint_tool_RepresentationNavigationDescription_navigationNameExpression}
viewpoint_tool_RepresentationNavigationDescription.methods={viewpoint_tool_RepresentationNavigationDescription_m_getMappings}

# viewpoint_tool_RepresentationCreationDescription class attributes and methods
viewpoint_tool_RepresentationCreationDescription_titleExpression: Property = Property(name="titleExpression", type=StringType)
viewpoint_tool_RepresentationCreationDescription_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_RepresentationCreationDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_RepresentationCreationDescription.attributes={viewpoint_tool_RepresentationCreationDescription_browseExpression, viewpoint_tool_RepresentationCreationDescription_titleExpression}
viewpoint_tool_RepresentationCreationDescription.methods={viewpoint_tool_RepresentationCreationDescription_m_getMappings}

# viewpoint_tool_ExternalJavaAction class attributes and methods
viewpoint_tool_ExternalJavaAction_id: Property = Property(name="id", type=StringType)
viewpoint_tool_ExternalJavaAction.attributes={viewpoint_tool_ExternalJavaAction_id}

# tool_ContainerModelOperation class attributes and methods

# tool_ExternalJavaActionParameter class attributes and methods

# viewpoint_tool_ExternalJavaActionCall class attributes and methods

# tool_ExternalJavaAction class attributes and methods

# viewpoint_tool_PopupMenu class attributes and methods

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

# viewpoint_tool_AcceleoVariable class attributes and methods
viewpoint_tool_AcceleoVariable_computationExpression: Property = Property(name="computationExpression", type=StringType)
viewpoint_tool_AcceleoVariable.attributes={viewpoint_tool_AcceleoVariable_computationExpression}

# tool_VariableContainer class attributes and methods

# viewpoint_tool_SubVariable class attributes and methods

# AbstractVariable class attributes and methods

# viewpoint_tool_DialogVariable class attributes and methods
viewpoint_tool_DialogVariable_dialogPrompt: Property = Property(name="dialogPrompt", type=StringType)
viewpoint_tool_DialogVariable.attributes={viewpoint_tool_DialogVariable_dialogPrompt}

# viewpoint_tool_ElementDropVariable class attributes and methods

# tool_AbstractVariable class attributes and methods

# viewpoint_tool_AbstractVariable class attributes and methods
viewpoint_tool_AbstractVariable_name: Property = Property(name="name", type=StringType)
viewpoint_tool_AbstractVariable.attributes={viewpoint_tool_AbstractVariable_name}

# viewpoint_tool_VariableContainer class attributes and methods

# tool_SubVariable class attributes and methods

# viewpoint_tool_SelectModelElementVariable class attributes and methods

# viewpoint_tool_EditMaskVariables class attributes and methods
viewpoint_tool_EditMaskVariables_mask: Property = Property(name="mask", type=StringType)
viewpoint_tool_EditMaskVariables.attributes={viewpoint_tool_EditMaskVariables_mask}

# viewpoint_tool_ContainerModelOperation class attributes and methods

# ModelOperation class attributes and methods

# tool_ModelOperation class attributes and methods

# viewpoint_tool_ModelOperation class attributes and methods

# viewpoint_tool_InitialNodeCreationOperation class attributes and methods

# viewpoint_tool_ElementSelectVariable class attributes and methods

# viewpoint_tool_ElementVariable class attributes and methods

# viewpoint_tool_ElementViewVariable class attributes and methods

# viewpoint_tool_ElementDeleteVariable class attributes and methods

# viewpoint_tool_DropContainerVariable class attributes and methods

# viewpoint_tool_SelectContainerVariable class attributes and methods

# viewpoint_tool_ContainerViewVariable class attributes and methods

# viewpoint_tool_CreateInstance class attributes and methods
viewpoint_tool_CreateInstance_typeName: Property = Property(name="typeName", type=StringType)
viewpoint_tool_CreateInstance_referenceName: Property = Property(name="referenceName", type=StringType)
viewpoint_tool_CreateInstance_variableName: Property = Property(name="variableName", type=StringType)
viewpoint_tool_CreateInstance.attributes={viewpoint_tool_CreateInstance_variableName, viewpoint_tool_CreateInstance_referenceName, viewpoint_tool_CreateInstance_typeName}

# ContainerModelOperation class attributes and methods

# viewpoint_tool_ChangeContext class attributes and methods
viewpoint_tool_ChangeContext_browseExpression: Property = Property(name="browseExpression", type=StringType)
viewpoint_tool_ChangeContext.attributes={viewpoint_tool_ChangeContext_browseExpression}

# viewpoint_tool_InitialOperation class attributes and methods

# viewpoint_tool_InitEdgeCreationOperation class attributes and methods

# viewpoint_tool_InitialContainerDropOperation class attributes and methods

# viewpoint_tool_SetObject class attributes and methods
viewpoint_tool_SetObject_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_SetObject.attributes={viewpoint_tool_SetObject_featureName}

# tool_viewpoint_EObject class attributes and methods

# viewpoint_tool_Unset class attributes and methods
viewpoint_tool_Unset_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_Unset_elementExpression: Property = Property(name="elementExpression", type=StringType)
viewpoint_tool_Unset.attributes={viewpoint_tool_Unset_elementExpression, viewpoint_tool_Unset_featureName}

# viewpoint_tool_SetValue class attributes and methods
viewpoint_tool_SetValue_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_SetValue_valueExpression: Property = Property(name="valueExpression", type=StringType)
viewpoint_tool_SetValue.attributes={viewpoint_tool_SetValue_featureName, viewpoint_tool_SetValue_valueExpression}

# viewpoint_tool_RemoveElement class attributes and methods

# viewpoint_tool_For class attributes and methods
viewpoint_tool_For_expression: Property = Property(name="expression", type=StringType)
viewpoint_tool_For_iteratorName: Property = Property(name="iteratorName", type=StringType)
viewpoint_tool_For.attributes={viewpoint_tool_For_iteratorName, viewpoint_tool_For_expression}

# viewpoint_tool_MoveElement class attributes and methods
viewpoint_tool_MoveElement_newContainerExpression: Property = Property(name="newContainerExpression", type=StringType)
viewpoint_tool_MoveElement_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_MoveElement.attributes={viewpoint_tool_MoveElement_featureName, viewpoint_tool_MoveElement_newContainerExpression}

# viewpoint_tool_ToolFilterDescription class attributes and methods
viewpoint_tool_ToolFilterDescription_precondition: Property = Property(name="precondition", type=StringType)
viewpoint_tool_ToolFilterDescription_elementsToListen: Property = Property(name="elementsToListen", type=StringType)
viewpoint_tool_ToolFilterDescription.attributes={viewpoint_tool_ToolFilterDescription_precondition, viewpoint_tool_ToolFilterDescription_elementsToListen}

# viewpoint_tool_If class attributes and methods
viewpoint_tool_If_conditionExpression: Property = Property(name="conditionExpression", type=StringType)
viewpoint_tool_If.attributes={viewpoint_tool_If_conditionExpression}

# viewpoint_tool_DeleteView class attributes and methods

# viewpoint_tool_NameVariable class attributes and methods

# viewpoint_tool_ExternalJavaActionParameter class attributes and methods
viewpoint_tool_ExternalJavaActionParameter_name: Property = Property(name="name", type=StringType)
viewpoint_tool_ExternalJavaActionParameter_value: Property = Property(name="value", type=StringType)
viewpoint_tool_ExternalJavaActionParameter.attributes={viewpoint_tool_ExternalJavaActionParameter_name, viewpoint_tool_ExternalJavaActionParameter_value}

# viewpoint_tool_SwitchChild class attributes and methods

# viewpoint_tool_Default class attributes and methods

# viewpoint_tool_Switch class attributes and methods

# tool_Case class attributes and methods

# tool_FeatureChangeListener class attributes and methods

# viewpoint_tool_FeatureChangeListener class attributes and methods
viewpoint_tool_FeatureChangeListener_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_tool_FeatureChangeListener_featureName: Property = Property(name="featureName", type=StringType)
viewpoint_tool_FeatureChangeListener.attributes={viewpoint_tool_FeatureChangeListener_domainClass, viewpoint_tool_FeatureChangeListener_featureName}

# viewpoint_tool_Case class attributes and methods
viewpoint_tool_Case_conditionExpression: Property = Property(name="conditionExpression", type=StringType)
viewpoint_tool_Case.attributes={viewpoint_tool_Case_conditionExpression}

# SwitchChild class attributes and methods

# viewpoint_audit_TemplateInformationSection class attributes and methods
viewpoint_audit_TemplateInformationSection_templatePath: Property = Property(name="templatePath", type=StringType)
viewpoint_audit_TemplateInformationSection.attributes={viewpoint_audit_TemplateInformationSection_templatePath}

# InformationSection class attributes and methods

# viewpoint_diagram_DDiagram class attributes and methods
viewpoint_diagram_DDiagram_info: Property = Property(name="info", type=StringType)
viewpoint_diagram_DDiagram_synchronized: Property = Property(name="synchronized", type=BooleanType)
viewpoint_diagram_DDiagram_isInLayoutingMode: Property = Property(name="isInLayoutingMode", type=BooleanType)
viewpoint_diagram_DDiagram_headerHeight: Property = Property(name="headerHeight", type=IntegerType)
viewpoint_diagram_DDiagram_m_clean: Method = Method(name="clean", parameters={})
viewpoint_diagram_DDiagram_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
viewpoint_diagram_DDiagram_m_findDiagramElements: Method = Method(name="findDiagramElements", parameters={Parameter(name='type'), Parameter(name='semanticElement')}, type=StringType)
viewpoint_diagram_DDiagram_m_getEdgesFromMapping: Method = Method(name="getEdgesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
viewpoint_diagram_DDiagram_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
viewpoint_diagram_DDiagram.attributes={viewpoint_diagram_DDiagram_headerHeight, viewpoint_diagram_DDiagram_isInLayoutingMode, viewpoint_diagram_DDiagram_info, viewpoint_diagram_DDiagram_synchronized}
viewpoint_diagram_DDiagram.methods={viewpoint_diagram_DDiagram_m_getContainersFromMapping, viewpoint_diagram_DDiagram_m_getNodesFromMapping, viewpoint_diagram_DDiagram_m_clean, viewpoint_diagram_DDiagram_m_findDiagramElements, viewpoint_diagram_DDiagram_m_getEdgesFromMapping}

# DRepresentation class attributes and methods

# DragAndDropTarget class attributes and methods

# DValidable class attributes and methods

# DContainer class attributes and methods

# tool_Default class attributes and methods

# viewpoint_audit_InformationSection class attributes and methods
viewpoint_audit_InformationSection_m_getContent: Method = Method(name="getContent", parameters={Parameter(name='eObj')}, type=StringType)
viewpoint_audit_InformationSection.methods={viewpoint_audit_InformationSection_m_getContent}

# DDiagramElement class attributes and methods

# description_DiagramDescription class attributes and methods

# DNode class attributes and methods

# DNodeListElement class attributes and methods

# DDiagramElementContainer class attributes and methods

# DDiagram class attributes and methods

# DEdge class attributes and methods

# validation_ValidationRule class attributes and methods

# tool_BehaviorTool class attributes and methods

# FilterVariableHistory class attributes and methods

# description_Layer class attributes and methods

# concern_ConcernDescription class attributes and methods

# filter_FilterDescription class attributes and methods

# viewpoint_diagram_DDiagramElement class attributes and methods
viewpoint_diagram_DDiagramElement_visible: Property = Property(name="visible", type=BooleanType)
viewpoint_diagram_DDiagramElement_tooltipText: Property = Property(name="tooltipText", type=StringType)
viewpoint_diagram_DDiagramElement_m_getParentDiagram: Method = Method(name="getParentDiagram", parameters={}, type=StringType)
viewpoint_diagram_DDiagramElement_m_isFold: Method = Method(name="isFold", parameters={Parameter(name='alreadyManagedElements')}, type=BooleanType)
viewpoint_diagram_DDiagramElement.attributes={viewpoint_diagram_DDiagramElement_tooltipText, viewpoint_diagram_DDiagramElement_visible}
viewpoint_diagram_DDiagramElement.methods={viewpoint_diagram_DDiagramElement_m_getParentDiagram, viewpoint_diagram_DDiagramElement_m_isFold}

# DRepresentationElement class attributes and methods

# DNavigable class attributes and methods

# viewpoint_diagram_DSemanticDiagram class attributes and methods
viewpoint_diagram_DSemanticDiagram_m_getRootContent: Method = Method(name="getRootContent", parameters={}, type=StringType)
viewpoint_diagram_DSemanticDiagram.methods={viewpoint_diagram_DSemanticDiagram_m_getRootContent}

# diagram_DDiagram class attributes and methods

# GraphicalFilter class attributes and methods

# viewpoint_diagram_GraphicalFilter class attributes and methods

# viewpoint_diagram_HideFilter class attributes and methods

# viewpoint_diagram_HideLabelFilter class attributes and methods

# viewpoint_diagram_FoldingPointFilter class attributes and methods

# viewpoint_diagram_FoldingFilter class attributes and methods

# diagram_viewpoint_Decoration class attributes and methods

# viewpoint_diagram_DDiagramLink class attributes and methods

# EdgeTarget class attributes and methods

# viewpoint_diagram_AbstractDNode class attributes and methods
viewpoint_diagram_AbstractDNode_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
viewpoint_diagram_AbstractDNode.attributes={viewpoint_diagram_AbstractDNode_arrangeConstraints}

# viewpoint_diagram_AppliedCompositeFilters class attributes and methods

# filter_CompositeFilterDescription class attributes and methods

# viewpoint_diagram_AbsoluteBoundsFilter class attributes and methods
viewpoint_diagram_AbsoluteBoundsFilter_height: Property = Property(name="height", type=StringType)
viewpoint_diagram_AbsoluteBoundsFilter_width: Property = Property(name="width", type=StringType)
viewpoint_diagram_AbsoluteBoundsFilter_x: Property = Property(name="x", type=StringType)
viewpoint_diagram_AbsoluteBoundsFilter_y: Property = Property(name="y", type=StringType)
viewpoint_diagram_AbsoluteBoundsFilter.attributes={viewpoint_diagram_AbsoluteBoundsFilter_x, viewpoint_diagram_AbsoluteBoundsFilter_y, viewpoint_diagram_AbsoluteBoundsFilter_width, viewpoint_diagram_AbsoluteBoundsFilter_height}

# NodeStyle class attributes and methods

# viewpoint_diagram_DNode class attributes and methods
viewpoint_diagram_DNode_height: Property = Property(name="height", type=StringType)
viewpoint_diagram_DNode_labelPosition: Property = Property(name="labelPosition", type=StringType)
viewpoint_diagram_DNode_resizeKind: Property = Property(name="resizeKind", type=StringType)
viewpoint_diagram_DNode_width: Property = Property(name="width", type=StringType)
viewpoint_diagram_DNode.attributes={viewpoint_diagram_DNode_labelPosition, viewpoint_diagram_DNode_width, viewpoint_diagram_DNode_height, viewpoint_diagram_DNode_resizeKind}

# diagram_AbstractDNode class attributes and methods

# diagram_EdgeTarget class attributes and methods

# viewpoint_diagram_DDiagramElementContainer class attributes and methods
viewpoint_diagram_DDiagramElementContainer_height: Property = Property(name="height", type=StringType)
viewpoint_diagram_DDiagramElementContainer_width: Property = Property(name="width", type=StringType)
viewpoint_diagram_DDiagramElementContainer_m_getNodesFromMapping: Method = Method(name="getNodesFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
viewpoint_diagram_DDiagramElementContainer_m_getContainersFromMapping: Method = Method(name="getContainersFromMapping", parameters={Parameter(name='mapping')}, type=StringType)
viewpoint_diagram_DDiagramElementContainer.attributes={viewpoint_diagram_DDiagramElementContainer_height, viewpoint_diagram_DDiagramElementContainer_width}
viewpoint_diagram_DDiagramElementContainer.methods={viewpoint_diagram_DDiagramElementContainer_m_getNodesFromMapping, viewpoint_diagram_DDiagramElementContainer_m_getContainersFromMapping}

# diagram_viewpoint_Style class attributes and methods

# description_NodeMapping class attributes and methods

# ContainerStyle class attributes and methods

# viewpoint_diagram_DNodeContainer class attributes and methods
viewpoint_diagram_DNodeContainer_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
viewpoint_diagram_DNodeContainer.attributes={viewpoint_diagram_DNodeContainer_childrenPresentation}

# viewpoint_diagram_DNodeList class attributes and methods
viewpoint_diagram_DNodeList_lineWidth: Property = Property(name="lineWidth", type=IntegerType)
viewpoint_diagram_DNodeList.attributes={viewpoint_diagram_DNodeList_lineWidth}

# description_ContainerMapping class attributes and methods

# viewpoint_diagram_DNodeListElement class attributes and methods

# AbstractDNode class attributes and methods

# description_IEdgeMapping class attributes and methods

# viewpoint_diagram_DEdge class attributes and methods
viewpoint_diagram_DEdge_routingStyle: Property = Property(name="routingStyle", type=StringType)
viewpoint_diagram_DEdge_size: Property = Property(name="size", type=StringType)
viewpoint_diagram_DEdge_beginLabel: Property = Property(name="beginLabel", type=StringType)
viewpoint_diagram_DEdge_endLabel: Property = Property(name="endLabel", type=StringType)
viewpoint_diagram_DEdge_isFold: Property = Property(name="isFold", type=BooleanType)
viewpoint_diagram_DEdge_isMockEdge: Property = Property(name="isMockEdge", type=BooleanType)
viewpoint_diagram_DEdge_arrangeConstraints: Property = Property(name="arrangeConstraints", type=StringType)
viewpoint_diagram_DEdge_m_isRootFolding: Method = Method(name="isRootFolding", parameters={}, type=BooleanType)
viewpoint_diagram_DEdge.attributes={viewpoint_diagram_DEdge_routingStyle, viewpoint_diagram_DEdge_arrangeConstraints, viewpoint_diagram_DEdge_beginLabel, viewpoint_diagram_DEdge_endLabel, viewpoint_diagram_DEdge_isMockEdge, viewpoint_diagram_DEdge_isFold, viewpoint_diagram_DEdge_size}
viewpoint_diagram_DEdge.methods={viewpoint_diagram_DEdge_m_isRootFolding}

# diagram_DDiagramElement class attributes and methods

# EdgeStyle class attributes and methods

# viewpoint_diagram_DDiagramSet class attributes and methods

# viewpoint_diagram_Dot class attributes and methods
viewpoint_diagram_Dot_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
viewpoint_diagram_Dot.attributes={viewpoint_diagram_Dot_strokeSizeComputationExpression}

# diagram_viewpoint_RGBValues class attributes and methods

# diagram_viewpoint_DRepresentationContainer class attributes and methods

# viewpoint_diagram_NodeStyle class attributes and methods
viewpoint_diagram_NodeStyle_labelPosition: Property = Property(name="labelPosition", type=StringType)
viewpoint_diagram_NodeStyle_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
viewpoint_diagram_NodeStyle.attributes={viewpoint_diagram_NodeStyle_hideLabelByDefault, viewpoint_diagram_NodeStyle_labelPosition}

# LabelStyle class attributes and methods

# Style class attributes and methods

# diagram_BorderedStyle class attributes and methods

# viewpoint_diagram_ContainerStyle class attributes and methods

# viewpoint_diagram_FlatContainerStyle class attributes and methods
viewpoint_diagram_FlatContainerStyle_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
viewpoint_diagram_FlatContainerStyle.attributes={viewpoint_diagram_FlatContainerStyle_backgroundStyle}

# viewpoint_diagram_GaugeSection class attributes and methods
viewpoint_diagram_GaugeSection_label: Property = Property(name="label", type=StringType)
viewpoint_diagram_GaugeSection_min: Property = Property(name="min", type=StringType)
viewpoint_diagram_GaugeSection_max: Property = Property(name="max", type=StringType)
viewpoint_diagram_GaugeSection_value: Property = Property(name="value", type=StringType)
viewpoint_diagram_GaugeSection.attributes={viewpoint_diagram_GaugeSection_min, viewpoint_diagram_GaugeSection_label, viewpoint_diagram_GaugeSection_value, viewpoint_diagram_GaugeSection_max}

# viewpoint_diagram_Square class attributes and methods
viewpoint_diagram_Square_width: Property = Property(name="width", type=StringType)
viewpoint_diagram_Square_height: Property = Property(name="height", type=StringType)
viewpoint_diagram_Square.attributes={viewpoint_diagram_Square_width, viewpoint_diagram_Square_height}

# viewpoint_diagram_ShapeContainerStyle class attributes and methods
viewpoint_diagram_ShapeContainerStyle_shape: Property = Property(name="shape", type=StringType)
viewpoint_diagram_ShapeContainerStyle.attributes={viewpoint_diagram_ShapeContainerStyle_shape}

# viewpoint_diagram_Lozenge class attributes and methods
viewpoint_diagram_Lozenge_width: Property = Property(name="width", type=StringType)
viewpoint_diagram_Lozenge_height: Property = Property(name="height", type=StringType)
viewpoint_diagram_Lozenge.attributes={viewpoint_diagram_Lozenge_width, viewpoint_diagram_Lozenge_height}

# viewpoint_diagram_Ellipse class attributes and methods
viewpoint_diagram_Ellipse_horizontalDiameter: Property = Property(name="horizontalDiameter", type=StringType)
viewpoint_diagram_Ellipse_verticalDiameter: Property = Property(name="verticalDiameter", type=StringType)
viewpoint_diagram_Ellipse.attributes={viewpoint_diagram_Ellipse_verticalDiameter, viewpoint_diagram_Ellipse_horizontalDiameter}

# viewpoint_diagram_WorkspaceImage class attributes and methods
viewpoint_diagram_WorkspaceImage_workspacePath: Property = Property(name="workspacePath", type=StringType)
viewpoint_diagram_WorkspaceImage.attributes={viewpoint_diagram_WorkspaceImage_workspacePath}

# diagram_NodeStyle class attributes and methods

# diagram_ContainerStyle class attributes and methods

# viewpoint_diagram_CustomStyle class attributes and methods
viewpoint_diagram_CustomStyle_id: Property = Property(name="id", type=StringType)
viewpoint_diagram_CustomStyle.attributes={viewpoint_diagram_CustomStyle_id}

# viewpoint_diagram_BundledImage class attributes and methods
viewpoint_diagram_BundledImage_shape: Property = Property(name="shape", type=StringType)
viewpoint_diagram_BundledImage.attributes={viewpoint_diagram_BundledImage_shape}

# viewpoint_diagram_EdgeTarget class attributes and methods

# viewpoint_diagram_EdgeStyle class attributes and methods
viewpoint_diagram_EdgeStyle_lineStyle: Property = Property(name="lineStyle", type=StringType)
viewpoint_diagram_EdgeStyle_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
viewpoint_diagram_EdgeStyle_targetArrow: Property = Property(name="targetArrow", type=StringType)
viewpoint_diagram_EdgeStyle_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
viewpoint_diagram_EdgeStyle_size: Property = Property(name="size", type=StringType)
viewpoint_diagram_EdgeStyle_routingStyle: Property = Property(name="routingStyle", type=StringType)
viewpoint_diagram_EdgeStyle.attributes={viewpoint_diagram_EdgeStyle_targetArrow, viewpoint_diagram_EdgeStyle_routingStyle, viewpoint_diagram_EdgeStyle_sourceArrow, viewpoint_diagram_EdgeStyle_lineStyle, viewpoint_diagram_EdgeStyle_foldingStyle, viewpoint_diagram_EdgeStyle_size}

# BeginLabelStyle class attributes and methods

# CenterLabelStyle class attributes and methods

# EndLabelStyle class attributes and methods

# viewpoint_diagram_GaugeCompositeStyle class attributes and methods
viewpoint_diagram_GaugeCompositeStyle_alignment: Property = Property(name="alignment", type=StringType)
viewpoint_diagram_GaugeCompositeStyle.attributes={viewpoint_diagram_GaugeCompositeStyle_alignment}

# viewpoint_diagram_Note class attributes and methods

# viewpoint_diagram_FilterVariableHistory class attributes and methods

# FilterVariableValue class attributes and methods

# GaugeSection class attributes and methods

# viewpoint_diagram_BorderedStyle class attributes and methods
viewpoint_diagram_BorderedStyle_borderSize: Property = Property(name="borderSize", type=StringType)
viewpoint_diagram_BorderedStyle_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
viewpoint_diagram_BorderedStyle.attributes={viewpoint_diagram_BorderedStyle_borderSizeComputationExpression, viewpoint_diagram_BorderedStyle_borderSize}

# viewpoint_diagram_CollapseFilter class attributes and methods
viewpoint_diagram_CollapseFilter_width: Property = Property(name="width", type=IntegerType)
viewpoint_diagram_CollapseFilter_height: Property = Property(name="height", type=IntegerType)
viewpoint_diagram_CollapseFilter.attributes={viewpoint_diagram_CollapseFilter_width, viewpoint_diagram_CollapseFilter_height}

# viewpoint_diagram_IndirectlyCollapseFilter class attributes and methods

# CollapseFilter class attributes and methods

# viewpoint_diagram_BeginLabelStyle class attributes and methods
viewpoint_diagram_BeginLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
viewpoint_diagram_BeginLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
viewpoint_diagram_BeginLabelStyle.methods={viewpoint_diagram_BeginLabelStyle_m_setDescription, viewpoint_diagram_BeginLabelStyle_m_getDescription}

# viewpoint_diagram_FilterVariableValue class attributes and methods

# filter_FilterVariable class attributes and methods

# diagram_viewpoint_EObject class attributes and methods

# viewpoint_diagram_EndLabelStyle class attributes and methods
viewpoint_diagram_EndLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
viewpoint_diagram_EndLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
viewpoint_diagram_EndLabelStyle.methods={viewpoint_diagram_EndLabelStyle_m_getDescription, viewpoint_diagram_EndLabelStyle_m_setDescription}

# viewpoint_diagram_CenterLabelStyle class attributes and methods
viewpoint_diagram_CenterLabelStyle_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
viewpoint_diagram_CenterLabelStyle_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='description')})
viewpoint_diagram_CenterLabelStyle.methods={viewpoint_diagram_CenterLabelStyle_m_setDescription, viewpoint_diagram_CenterLabelStyle_m_getDescription}

# viewpoint_diagram_DiagramElementMapping2ModelElement class attributes and methods

# ModelElement2ViewVariable class attributes and methods

# viewpoint_diagram_BracketEdgeStyle class attributes and methods

# viewpoint_diagram_ComputedStyleDescriptionRegistry class attributes and methods

# DiagramElementMapping2ModelElement class attributes and methods

# ContainerVariable2StyleDescription class attributes and methods

# viewpoint_diagram_ContainerVariable2StyleDescription class attributes and methods

# viewpoint_diagram_ModelElement2ViewVariable class attributes and methods

# ViewVariable2ContainerVariable class attributes and methods

# viewpoint_diagram_ViewVariable2ContainerVariable class attributes and methods

# description_EdgeMapping class attributes and methods

# viewpoint_description_DiagramDescription class attributes and methods
viewpoint_description_DiagramDescription_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
viewpoint_description_DiagramDescription_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_description_DiagramDescription_rootExpression: Property = Property(name="rootExpression", type=StringType)
viewpoint_description_DiagramDescription_enablePopupBars: Property = Property(name="enablePopupBars", type=BooleanType)
viewpoint_description_DiagramDescription_m_createDiagram: Method = Method(name="createDiagram", parameters={}, type=StringType)
viewpoint_description_DiagramDescription.attributes={viewpoint_description_DiagramDescription_enablePopupBars, viewpoint_description_DiagramDescription_preconditionExpression, viewpoint_description_DiagramDescription_domainClass, viewpoint_description_DiagramDescription_rootExpression}
viewpoint_description_DiagramDescription.methods={viewpoint_description_DiagramDescription_m_createDiagram}

# description_DragAndDropTargetDescription class attributes and methods

# description_RepresentationDescription class attributes and methods

# description_PasteTargetDescription class attributes and methods

# concern_ConcernSet class attributes and methods

# description_Layout class attributes and methods

# description_AdditionalLayer class attributes and methods

# tool_ToolSection class attributes and methods

# viewpoint_description_DiagramImportDescription class attributes and methods

# description_RepresentationImportDescription class attributes and methods

# viewpoint_description_DiagramExtensionDescription class attributes and methods

# description_EdgeMappingImport class attributes and methods

# viewpoint_description_DiagramElementMapping class attributes and methods
viewpoint_description_DiagramElementMapping_preconditionExpression: Property = Property(name="preconditionExpression", type=StringType)
viewpoint_description_DiagramElementMapping_semanticCandidatesExpression: Property = Property(name="semanticCandidatesExpression", type=StringType)
viewpoint_description_DiagramElementMapping_createElements: Property = Property(name="createElements", type=BooleanType)
viewpoint_description_DiagramElementMapping_semanticElements: Property = Property(name="semanticElements", type=StringType)
viewpoint_description_DiagramElementMapping_synchronizationLock: Property = Property(name="synchronizationLock", type=BooleanType)
viewpoint_description_DiagramElementMapping_m_isFrom: Method = Method(name="isFrom", parameters={Parameter(name='element')}, type=BooleanType)
viewpoint_description_DiagramElementMapping_m_checkPrecondition: Method = Method(name="checkPrecondition", parameters={Parameter(name='container'), Parameter(name='modelElement'), Parameter(name='containerView')}, type=BooleanType)
viewpoint_description_DiagramElementMapping_m_getAllMappings: Method = Method(name="getAllMappings", parameters={}, type=StringType)
viewpoint_description_DiagramElementMapping.attributes={viewpoint_description_DiagramElementMapping_createElements, viewpoint_description_DiagramElementMapping_preconditionExpression, viewpoint_description_DiagramElementMapping_synchronizationLock, viewpoint_description_DiagramElementMapping_semanticElements, viewpoint_description_DiagramElementMapping_semanticCandidatesExpression}
viewpoint_description_DiagramElementMapping.methods={viewpoint_description_DiagramElementMapping_m_checkPrecondition, viewpoint_description_DiagramElementMapping_m_isFrom, viewpoint_description_DiagramElementMapping_m_getAllMappings}

# description_RepresentationElementMapping class attributes and methods

# tool_DeleteElementDescription class attributes and methods

# tool_DirectEditLabel class attributes and methods

# tool_DoubleClickDescription class attributes and methods

# viewpoint_description_AbstractNodeMapping class attributes and methods
viewpoint_description_AbstractNodeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_description_AbstractNodeMapping_m_getAllBorderedNodeMappings: Method = Method(name="getAllBorderedNodeMappings", parameters={}, type=StringType)
viewpoint_description_AbstractNodeMapping_m_getDNodesDone: Method = Method(name="getDNodesDone", parameters={}, type=StringType)
viewpoint_description_AbstractNodeMapping_m_findDNodeFromEObject: Method = Method(name="findDNodeFromEObject", parameters={Parameter(name='eObject')}, type=StringType)
viewpoint_description_AbstractNodeMapping_m_clearDNodesDone: Method = Method(name="clearDNodesDone", parameters={})
viewpoint_description_AbstractNodeMapping_m_addDoneNode: Method = Method(name="addDoneNode", parameters={Parameter(name='node')})
viewpoint_description_AbstractNodeMapping.attributes={viewpoint_description_AbstractNodeMapping_domainClass}
viewpoint_description_AbstractNodeMapping.methods={viewpoint_description_AbstractNodeMapping_m_getDNodesDone, viewpoint_description_AbstractNodeMapping_m_addDoneNode, viewpoint_description_AbstractNodeMapping_m_clearDNodesDone, viewpoint_description_AbstractNodeMapping_m_getAllBorderedNodeMappings, viewpoint_description_AbstractNodeMapping_m_findDNodeFromEObject}

# viewpoint_description_NodeMapping class attributes and methods
viewpoint_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='container'), Parameter(name='semanticOrigin'), Parameter(name='containerView')}, type=StringType)
viewpoint_description_NodeMapping_m_createNode: Method = Method(name="createNode", parameters={Parameter(name='modelElement'), Parameter(name='container'), Parameter(name='viewPoint')}, type=StringType)
viewpoint_description_NodeMapping_m_updateNode: Method = Method(name="updateNode", parameters={Parameter(name='node')})
viewpoint_description_NodeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='modelElement'), Parameter(name='containerVariable'), Parameter(name='viewVariable')}, type=StringType)
viewpoint_description_NodeMapping_m_createListElement: Method = Method(name="createListElement", parameters={Parameter(name='modelElement'), Parameter(name='diagram')}, type=StringType)
viewpoint_description_NodeMapping_m_updateListElement: Method = Method(name="updateListElement", parameters={Parameter(name='listElement')})
viewpoint_description_NodeMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='container'), Parameter(name='semanticOrigin')}, type=StringType)
viewpoint_description_NodeMapping.methods={viewpoint_description_NodeMapping_m_getBestStyle, viewpoint_description_NodeMapping_m_getNodesCandidates, viewpoint_description_NodeMapping_m_getNodesCandidates, viewpoint_description_NodeMapping_m_updateNode, viewpoint_description_NodeMapping_m_updateListElement, viewpoint_description_NodeMapping_m_createNode, viewpoint_description_NodeMapping_m_createListElement}

# description_AbstractNodeMapping class attributes and methods

# style_NodeStyleDescription class attributes and methods

# description_ConditionalNodeStyleDescription class attributes and methods

# viewpoint_description_ContainerMapping class attributes and methods
viewpoint_description_ContainerMapping_childrenPresentation: Property = Property(name="childrenPresentation", type=StringType)
viewpoint_description_ContainerMapping_m_createContainer: Method = Method(name="createContainer", parameters={Parameter(name='container'), Parameter(name='viewPoint'), Parameter(name='modelElement')}, type=StringType)
viewpoint_description_ContainerMapping_m_updateContainer: Method = Method(name="updateContainer", parameters={Parameter(name='node')})
viewpoint_description_ContainerMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='containerVariable'), Parameter(name='viewVariable'), Parameter(name='modelElement')}, type=StringType)
viewpoint_description_ContainerMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
viewpoint_description_ContainerMapping_m_getNodesCandidates: Method = Method(name="getNodesCandidates", parameters={Parameter(name='containerView'), Parameter(name='container'), Parameter(name='semanticOrigin')}, type=StringType)
viewpoint_description_ContainerMapping.attributes={viewpoint_description_ContainerMapping_childrenPresentation}
viewpoint_description_ContainerMapping.methods={viewpoint_description_ContainerMapping_m_getBestStyle, viewpoint_description_ContainerMapping_m_createContainer, viewpoint_description_ContainerMapping_m_getNodesCandidates, viewpoint_description_ContainerMapping_m_updateContainer, viewpoint_description_ContainerMapping_m_getNodesCandidates}

# style_ContainerStyleDescription class attributes and methods

# description_ConditionalContainerStyleDescription class attributes and methods

# viewpoint_description_NodeMappingImport class attributes and methods

# description_AbstractMappingImport class attributes and methods

# viewpoint_description_ContainerMappingImport class attributes and methods

# viewpoint_description_EdgeMapping class attributes and methods
viewpoint_description_EdgeMapping_targetFinderExpression: Property = Property(name="targetFinderExpression", type=StringType)
viewpoint_description_EdgeMapping_sourceFinderExpression: Property = Property(name="sourceFinderExpression", type=StringType)
viewpoint_description_EdgeMapping_targetExpression: Property = Property(name="targetExpression", type=StringType)
viewpoint_description_EdgeMapping_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_description_EdgeMapping_useDomainElement: Property = Property(name="useDomainElement", type=BooleanType)
viewpoint_description_EdgeMapping_pathExpression: Property = Property(name="pathExpression", type=StringType)
viewpoint_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='target'), Parameter(name='container'), Parameter(name='semanticTarget'), Parameter(name='source')}, type=StringType)
viewpoint_description_EdgeMapping_m_createEdge: Method = Method(name="createEdge", parameters={Parameter(name='target'), Parameter(name='semanticTarget'), Parameter(name='source')}, type=StringType)
viewpoint_description_EdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='containerVariable'), Parameter(name='viewVariable'), Parameter(name='modelElement')}, type=StringType)
viewpoint_description_EdgeMapping_m_updateEdge: Method = Method(name="updateEdge", parameters={Parameter(name='viewEdge')})
viewpoint_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='viewPoint'), Parameter(name='semanticOrigin')}, type=StringType)
viewpoint_description_EdgeMapping_m_getEdgeSourceCandidates: Method = Method(name="getEdgeSourceCandidates", parameters={Parameter(name='semanticOrigin'), Parameter(name='viewPoint')}, type=StringType)
viewpoint_description_EdgeMapping_m_getEdgeTargetCandidates: Method = Method(name="getEdgeTargetCandidates", parameters={Parameter(name='containerView'), Parameter(name='semanticOrigin'), Parameter(name='container')}, type=StringType)
viewpoint_description_EdgeMapping.attributes={viewpoint_description_EdgeMapping_domainClass, viewpoint_description_EdgeMapping_targetFinderExpression, viewpoint_description_EdgeMapping_targetExpression, viewpoint_description_EdgeMapping_useDomainElement, viewpoint_description_EdgeMapping_pathExpression, viewpoint_description_EdgeMapping_sourceFinderExpression}
viewpoint_description_EdgeMapping.methods={viewpoint_description_EdgeMapping_m_createEdge, viewpoint_description_EdgeMapping_m_getEdgeTargetCandidates, viewpoint_description_EdgeMapping_m_getEdgeTargetCandidates, viewpoint_description_EdgeMapping_m_updateEdge, viewpoint_description_EdgeMapping_m_createEdge, viewpoint_description_EdgeMapping_m_getBestStyle, viewpoint_description_EdgeMapping_m_getEdgeSourceCandidates}

# description_ConditionalEdgeStyleDescription class attributes and methods

# style_EdgeStyleDescription class attributes and methods

# viewpoint_description_ConditionalNodeStyleDescription class attributes and methods

# ConditionalStyleDescription class attributes and methods

# viewpoint_description_ConditionalEdgeStyleDescription class attributes and methods

# tool_ReconnectEdgeDescription class attributes and methods

# viewpoint_description_IEdgeMapping class attributes and methods
viewpoint_description_IEdgeMapping_m_getBestStyle: Method = Method(name="getBestStyle", parameters={Parameter(name='viewVariable'), Parameter(name='modelElement'), Parameter(name='containerVariable')}, type=StringType)
viewpoint_description_IEdgeMapping.methods={viewpoint_description_IEdgeMapping_m_getBestStyle}

# viewpoint_description_EdgeMappingImport class attributes and methods
viewpoint_description_EdgeMappingImport_inheritsAncestorFilters: Property = Property(name="inheritsAncestorFilters", type=BooleanType)
viewpoint_description_EdgeMappingImport.attributes={viewpoint_description_EdgeMappingImport_inheritsAncestorFilters}

# viewpoint_description_ConditionalContainerStyleDescription class attributes and methods

# viewpoint_description_Layout class attributes and methods

# DocumentedElement class attributes and methods

# viewpoint_description_OrderedTreeLayout class attributes and methods
viewpoint_description_OrderedTreeLayout_childrenExpression: Property = Property(name="childrenExpression", type=StringType)
viewpoint_description_OrderedTreeLayout.attributes={viewpoint_description_OrderedTreeLayout_childrenExpression}

# Layout class attributes and methods

# viewpoint_description_CompositeLayout class attributes and methods
viewpoint_description_CompositeLayout_padding: Property = Property(name="padding", type=IntegerType)
viewpoint_description_CompositeLayout_direction: Property = Property(name="direction", type=StringType)
viewpoint_description_CompositeLayout.attributes={viewpoint_description_CompositeLayout_direction, viewpoint_description_CompositeLayout_padding}

# viewpoint_description_MappingBasedDecoration class attributes and methods

# viewpoint_description_Layer class attributes and methods
viewpoint_description_Layer_icon: Property = Property(name="icon", type=StringType)
viewpoint_description_Layer.attributes={viewpoint_description_Layer_icon}

# viewpoint_style_BorderedStyleDescription class attributes and methods
viewpoint_style_BorderedStyleDescription_borderSizeComputationExpression: Property = Property(name="borderSizeComputationExpression", type=StringType)
viewpoint_style_BorderedStyleDescription.attributes={viewpoint_style_BorderedStyleDescription_borderSizeComputationExpression}

# StyleDescription class attributes and methods

# DecorationDescriptionsSet class attributes and methods

# Customization class attributes and methods

# viewpoint_description_AdditionalLayer class attributes and methods
viewpoint_description_AdditionalLayer_activeByDefault: Property = Property(name="activeByDefault", type=BooleanType)
viewpoint_description_AdditionalLayer_optional: Property = Property(name="optional", type=BooleanType)
viewpoint_description_AdditionalLayer.attributes={viewpoint_description_AdditionalLayer_optional, viewpoint_description_AdditionalLayer_activeByDefault}

# Layer class attributes and methods

# viewpoint_style_NodeStyleDescription class attributes and methods
viewpoint_style_NodeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
viewpoint_style_NodeStyleDescription_labelPosition: Property = Property(name="labelPosition", type=StringType)
viewpoint_style_NodeStyleDescription_hideLabelByDefault: Property = Property(name="hideLabelByDefault", type=BooleanType)
viewpoint_style_NodeStyleDescription_resizeKind: Property = Property(name="resizeKind", type=StringType)
viewpoint_style_NodeStyleDescription.attributes={viewpoint_style_NodeStyleDescription_resizeKind, viewpoint_style_NodeStyleDescription_labelPosition, viewpoint_style_NodeStyleDescription_sizeComputationExpression, viewpoint_style_NodeStyleDescription_hideLabelByDefault}

# style_BorderedStyleDescription class attributes and methods

# style_LabelStyleDescription class attributes and methods

# style_TooltipStyleDescription class attributes and methods

# viewpoint_style_CustomStyleDescription class attributes and methods
viewpoint_style_CustomStyleDescription_id: Property = Property(name="id", type=StringType)
viewpoint_style_CustomStyleDescription.attributes={viewpoint_style_CustomStyleDescription_id}

# NodeStyleDescription class attributes and methods

# viewpoint_style_SquareDescription class attributes and methods
viewpoint_style_SquareDescription_height: Property = Property(name="height", type=StringType)
viewpoint_style_SquareDescription_width: Property = Property(name="width", type=StringType)
viewpoint_style_SquareDescription.attributes={viewpoint_style_SquareDescription_width, viewpoint_style_SquareDescription_height}

# viewpoint_style_LozengeNodeDescription class attributes and methods
viewpoint_style_LozengeNodeDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
viewpoint_style_LozengeNodeDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
viewpoint_style_LozengeNodeDescription.attributes={viewpoint_style_LozengeNodeDescription_heightComputationExpression, viewpoint_style_LozengeNodeDescription_widthComputationExpression}

# viewpoint_style_EllipseNodeDescription class attributes and methods
viewpoint_style_EllipseNodeDescription_horizontalDiameterComputationExpression: Property = Property(name="horizontalDiameterComputationExpression", type=StringType)
viewpoint_style_EllipseNodeDescription_verticalDiameterComputationExpression: Property = Property(name="verticalDiameterComputationExpression", type=StringType)
viewpoint_style_EllipseNodeDescription.attributes={viewpoint_style_EllipseNodeDescription_verticalDiameterComputationExpression, viewpoint_style_EllipseNodeDescription_horizontalDiameterComputationExpression}

# viewpoint_style_BundledImageDescription class attributes and methods
viewpoint_style_BundledImageDescription_shape: Property = Property(name="shape", type=StringType)
viewpoint_style_BundledImageDescription.attributes={viewpoint_style_BundledImageDescription_shape}

# viewpoint_style_NoteDescription class attributes and methods

# viewpoint_style_RoundedCornerStyleDescription class attributes and methods
viewpoint_style_RoundedCornerStyleDescription_arcWidth: Property = Property(name="arcWidth", type=StringType)
viewpoint_style_RoundedCornerStyleDescription_arcHeight: Property = Property(name="arcHeight", type=StringType)
viewpoint_style_RoundedCornerStyleDescription.attributes={viewpoint_style_RoundedCornerStyleDescription_arcHeight, viewpoint_style_RoundedCornerStyleDescription_arcWidth}

# viewpoint_style_DotDescription class attributes and methods
viewpoint_style_DotDescription_strokeSizeComputationExpression: Property = Property(name="strokeSizeComputationExpression", type=StringType)
viewpoint_style_DotDescription.attributes={viewpoint_style_DotDescription_strokeSizeComputationExpression}

# viewpoint_style_GaugeCompositeStyleDescription class attributes and methods
viewpoint_style_GaugeCompositeStyleDescription_alignment: Property = Property(name="alignment", type=StringType)
viewpoint_style_GaugeCompositeStyleDescription.attributes={viewpoint_style_GaugeCompositeStyleDescription_alignment}

# style_GaugeSectionDescription class attributes and methods

# viewpoint_style_GaugeSectionDescription class attributes and methods
viewpoint_style_GaugeSectionDescription_minValueExpression: Property = Property(name="minValueExpression", type=StringType)
viewpoint_style_GaugeSectionDescription_maxValueExpression: Property = Property(name="maxValueExpression", type=StringType)
viewpoint_style_GaugeSectionDescription_valueExpression: Property = Property(name="valueExpression", type=StringType)
viewpoint_style_GaugeSectionDescription_label: Property = Property(name="label", type=StringType)
viewpoint_style_GaugeSectionDescription.attributes={viewpoint_style_GaugeSectionDescription_valueExpression, viewpoint_style_GaugeSectionDescription_minValueExpression, viewpoint_style_GaugeSectionDescription_label, viewpoint_style_GaugeSectionDescription_maxValueExpression}

# viewpoint_style_SizeComputationContainerStyleDescription class attributes and methods
viewpoint_style_SizeComputationContainerStyleDescription_heightComputationExpression: Property = Property(name="heightComputationExpression", type=StringType)
viewpoint_style_SizeComputationContainerStyleDescription_widthComputationExpression: Property = Property(name="widthComputationExpression", type=StringType)
viewpoint_style_SizeComputationContainerStyleDescription.attributes={viewpoint_style_SizeComputationContainerStyleDescription_heightComputationExpression, viewpoint_style_SizeComputationContainerStyleDescription_widthComputationExpression}

# viewpoint_style_ContainerStyleDescription class attributes and methods
viewpoint_style_ContainerStyleDescription_roundedCorner: Property = Property(name="roundedCorner", type=BooleanType)
viewpoint_style_ContainerStyleDescription.attributes={viewpoint_style_ContainerStyleDescription_roundedCorner}

# style_RoundedCornerStyleDescription class attributes and methods

# viewpoint_style_FlatContainerStyleDescription class attributes and methods
viewpoint_style_FlatContainerStyleDescription_backgroundStyle: Property = Property(name="backgroundStyle", type=StringType)
viewpoint_style_FlatContainerStyleDescription.attributes={viewpoint_style_FlatContainerStyleDescription_backgroundStyle}

# style_SizeComputationContainerStyleDescription class attributes and methods

# viewpoint_style_ShapeContainerStyleDescription class attributes and methods
viewpoint_style_ShapeContainerStyleDescription_shape: Property = Property(name="shape", type=StringType)
viewpoint_style_ShapeContainerStyleDescription.attributes={viewpoint_style_ShapeContainerStyleDescription_shape}

# viewpoint_style_WorkspaceImageDescription class attributes and methods
viewpoint_style_WorkspaceImageDescription_workspacePath: Property = Property(name="workspacePath", type=StringType)
viewpoint_style_WorkspaceImageDescription.attributes={viewpoint_style_WorkspaceImageDescription_workspacePath}

# viewpoint_style_EdgeStyleDescription class attributes and methods
viewpoint_style_EdgeStyleDescription_lineStyle: Property = Property(name="lineStyle", type=StringType)
viewpoint_style_EdgeStyleDescription_sourceArrow: Property = Property(name="sourceArrow", type=StringType)
viewpoint_style_EdgeStyleDescription_targetArrow: Property = Property(name="targetArrow", type=StringType)
viewpoint_style_EdgeStyleDescription_sizeComputationExpression: Property = Property(name="sizeComputationExpression", type=StringType)
viewpoint_style_EdgeStyleDescription_routingStyle: Property = Property(name="routingStyle", type=StringType)
viewpoint_style_EdgeStyleDescription_foldingStyle: Property = Property(name="foldingStyle", type=StringType)
viewpoint_style_EdgeStyleDescription.attributes={viewpoint_style_EdgeStyleDescription_lineStyle, viewpoint_style_EdgeStyleDescription_sourceArrow, viewpoint_style_EdgeStyleDescription_routingStyle, viewpoint_style_EdgeStyleDescription_targetArrow, viewpoint_style_EdgeStyleDescription_sizeComputationExpression, viewpoint_style_EdgeStyleDescription_foldingStyle}

# style_BeginLabelStyleDescription class attributes and methods

# style_CenterLabelStyleDescription class attributes and methods

# style_EndLabelStyleDescription class attributes and methods

# viewpoint_style_BeginLabelStyleDescription class attributes and methods

# viewpoint_style_CenterLabelStyleDescription class attributes and methods

# viewpoint_style_EndLabelStyleDescription class attributes and methods

# viewpoint_style_BracketEdgeStyleDescription class attributes and methods

# EdgeStyleDescription class attributes and methods

# viewpoint_tool_ToolSection class attributes and methods
viewpoint_tool_ToolSection_icon: Property = Property(name="icon", type=StringType)
viewpoint_tool_ToolSection.attributes={viewpoint_tool_ToolSection_icon}

# tool_ToolGroupExtension class attributes and methods

# viewpoint_tool_ToolGroup class attributes and methods

# tool_PopupMenu class attributes and methods

# viewpoint_tool_ToolGroupExtension class attributes and methods

# tool_ToolGroup class attributes and methods

# viewpoint_tool_NodeCreationDescription class attributes and methods
viewpoint_tool_NodeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_NodeCreationDescription.attributes={viewpoint_tool_NodeCreationDescription_iconPath}

# tool_NodeCreationVariable class attributes and methods

# tool_InitialNodeCreationOperation class attributes and methods

# viewpoint_tool_EdgeCreationDescription class attributes and methods
viewpoint_tool_EdgeCreationDescription_connectionStartPrecondition: Property = Property(name="connectionStartPrecondition", type=StringType)
viewpoint_tool_EdgeCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_EdgeCreationDescription_m_getBestMapping: Method = Method(name="getBestMapping", parameters={Parameter(name='source'), Parameter(name='target'), Parameter(name='createdElements')}, type=StringType)
viewpoint_tool_EdgeCreationDescription.attributes={viewpoint_tool_EdgeCreationDescription_connectionStartPrecondition, viewpoint_tool_EdgeCreationDescription_iconPath}
viewpoint_tool_EdgeCreationDescription.methods={viewpoint_tool_EdgeCreationDescription_m_getBestMapping}

# tool_SourceEdgeCreationVariable class attributes and methods

# tool_TargetEdgeCreationVariable class attributes and methods

# tool_SourceEdgeViewCreationVariable class attributes and methods

# tool_TargetEdgeViewCreationVariable class attributes and methods

# tool_InitEdgeCreationOperation class attributes and methods

# viewpoint_tool_ContainerCreationDescription class attributes and methods
viewpoint_tool_ContainerCreationDescription_iconPath: Property = Property(name="iconPath", type=StringType)
viewpoint_tool_ContainerCreationDescription.attributes={viewpoint_tool_ContainerCreationDescription_iconPath}

# viewpoint_tool_DeleteElementDescription class attributes and methods
viewpoint_tool_DeleteElementDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_DeleteElementDescription.methods={viewpoint_tool_DeleteElementDescription_m_getMappings}

# tool_ElementDeleteVariable class attributes and methods

# tool_DeleteHook class attributes and methods

# viewpoint_tool_DoubleClickDescription class attributes and methods

# tool_ElementDoubleClickVariable class attributes and methods

# viewpoint_tool_DeleteHook class attributes and methods
viewpoint_tool_DeleteHook_id: Property = Property(name="id", type=StringType)
viewpoint_tool_DeleteHook.attributes={viewpoint_tool_DeleteHook_id}

# tool_DeleteHookParameter class attributes and methods

# viewpoint_tool_DeleteHookParameter class attributes and methods
viewpoint_tool_DeleteHookParameter_name: Property = Property(name="name", type=StringType)
viewpoint_tool_DeleteHookParameter_value: Property = Property(name="value", type=StringType)
viewpoint_tool_DeleteHookParameter.attributes={viewpoint_tool_DeleteHookParameter_name, viewpoint_tool_DeleteHookParameter_value}

# viewpoint_tool_ReconnectEdgeDescription class attributes and methods
viewpoint_tool_ReconnectEdgeDescription_reconnectionKind: Property = Property(name="reconnectionKind", type=StringType)
viewpoint_tool_ReconnectEdgeDescription_m_getMappings: Method = Method(name="getMappings", parameters={}, type=StringType)
viewpoint_tool_ReconnectEdgeDescription.attributes={viewpoint_tool_ReconnectEdgeDescription_reconnectionKind}
viewpoint_tool_ReconnectEdgeDescription.methods={viewpoint_tool_ReconnectEdgeDescription_m_getMappings}

# viewpoint_tool_RequestDescription class attributes and methods
viewpoint_tool_RequestDescription_type: Property = Property(name="type", type=StringType)
viewpoint_tool_RequestDescription.attributes={viewpoint_tool_RequestDescription_type}

# viewpoint_tool_DirectEditLabel class attributes and methods
viewpoint_tool_DirectEditLabel_inputLabelExpression: Property = Property(name="inputLabelExpression", type=StringType)
viewpoint_tool_DirectEditLabel_m_getMapping: Method = Method(name="getMapping", parameters={}, type=StringType)
viewpoint_tool_DirectEditLabel.attributes={viewpoint_tool_DirectEditLabel_inputLabelExpression}
viewpoint_tool_DirectEditLabel.methods={viewpoint_tool_DirectEditLabel_m_getMapping}

# tool_EditMaskVariables class attributes and methods

# viewpoint_tool_BehaviorTool class attributes and methods
viewpoint_tool_BehaviorTool_domainClass: Property = Property(name="domainClass", type=StringType)
viewpoint_tool_BehaviorTool.attributes={viewpoint_tool_BehaviorTool_domainClass}

# viewpoint_tool_SourceEdgeCreationVariable class attributes and methods

# viewpoint_tool_SourceEdgeViewCreationVariable class attributes and methods

# viewpoint_tool_TargetEdgeCreationVariable class attributes and methods

# viewpoint_tool_TargetEdgeViewCreationVariable class attributes and methods

# viewpoint_tool_ElementDoubleClickVariable class attributes and methods

# viewpoint_tool_NodeCreationVariable class attributes and methods

# viewpoint_tool_CreateView class attributes and methods
viewpoint_tool_CreateView_containerViewExpression: Property = Property(name="containerViewExpression", type=StringType)
viewpoint_tool_CreateView_variableName: Property = Property(name="variableName", type=StringType)
viewpoint_tool_CreateView.attributes={viewpoint_tool_CreateView_containerViewExpression, viewpoint_tool_CreateView_variableName}

# viewpoint_tool_CreateEdgeView class attributes and methods
viewpoint_tool_CreateEdgeView_sourceExpression: Property = Property(name="sourceExpression", type=StringType)
viewpoint_tool_CreateEdgeView_targetExpression: Property = Property(name="targetExpression", type=StringType)
viewpoint_tool_CreateEdgeView.attributes={viewpoint_tool_CreateEdgeView_targetExpression, viewpoint_tool_CreateEdgeView_sourceExpression}

# CreateView class attributes and methods

# viewpoint_tool_DiagramCreationDescription class attributes and methods

# RepresentationCreationDescription class attributes and methods

# viewpoint_tool_DiagramNavigationDescription class attributes and methods

# RepresentationNavigationDescription class attributes and methods

# viewpoint_filter_FilterDescription class attributes and methods
viewpoint_filter_FilterDescription_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
viewpoint_filter_FilterDescription.methods={viewpoint_filter_FilterDescription_m_isVisible}

# viewpoint_filter_Filter class attributes and methods
viewpoint_filter_Filter_filterKind: Property = Property(name="filterKind", type=StringType)
viewpoint_filter_Filter_m_isVisible: Method = Method(name="isVisible", parameters={Parameter(name='element')}, type=BooleanType)
viewpoint_filter_Filter.attributes={viewpoint_filter_Filter_filterKind}
viewpoint_filter_Filter.methods={viewpoint_filter_Filter_m_isVisible}

# viewpoint_filter_MappingFilter class attributes and methods
viewpoint_filter_MappingFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
viewpoint_filter_MappingFilter_viewConditionExpression: Property = Property(name="viewConditionExpression", type=StringType)
viewpoint_filter_MappingFilter.attributes={viewpoint_filter_MappingFilter_viewConditionExpression, viewpoint_filter_MappingFilter_semanticConditionExpression}

# Filter class attributes and methods

# filter_Filter class attributes and methods

# viewpoint_tool_Navigation class attributes and methods
viewpoint_tool_Navigation_createIfNotExistent: Property = Property(name="createIfNotExistent", type=BooleanType)
viewpoint_tool_Navigation.attributes={viewpoint_tool_Navigation_createIfNotExistent}

# viewpoint_filter_VariableFilter class attributes and methods
viewpoint_filter_VariableFilter_semanticConditionExpression: Property = Property(name="semanticConditionExpression", type=StringType)
viewpoint_filter_VariableFilter_m_setFilterContext: Method = Method(name="setFilterContext", parameters={Parameter(name='variables')})
viewpoint_filter_VariableFilter.attributes={viewpoint_filter_VariableFilter_semanticConditionExpression}
viewpoint_filter_VariableFilter.methods={viewpoint_filter_VariableFilter_m_setFilterContext}

# viewpoint_filter_FilterVariable class attributes and methods
viewpoint_filter_FilterVariable_name: Property = Property(name="name", type=StringType)
viewpoint_filter_FilterVariable.attributes={viewpoint_filter_FilterVariable_name}

# SelectionDescription class attributes and methods

# viewpoint_validation_ValidationSet class attributes and methods
viewpoint_validation_ValidationSet_name: Property = Property(name="name", type=StringType)
viewpoint_validation_ValidationSet.attributes={viewpoint_validation_ValidationSet_name}

# viewpoint_filter_CompositeFilterDescription class attributes and methods

# FilterDescription class attributes and methods

# validation_RuleAudit class attributes and methods

# validation_ValidationFix class attributes and methods

# viewpoint_validation_SemanticValidationRule class attributes and methods
viewpoint_validation_SemanticValidationRule_targetClass: Property = Property(name="targetClass", type=StringType)
viewpoint_validation_SemanticValidationRule.attributes={viewpoint_validation_SemanticValidationRule_targetClass}

# ValidationRule class attributes and methods

# viewpoint_validation_ViewValidationRule class attributes and methods

# viewpoint_validation_RuleAudit class attributes and methods
viewpoint_validation_RuleAudit_auditExpression: Property = Property(name="auditExpression", type=StringType)
viewpoint_validation_RuleAudit.attributes={viewpoint_validation_RuleAudit_auditExpression}

# viewpoint_validation_ValidationRule class attributes and methods
viewpoint_validation_ValidationRule_level: Property = Property(name="level", type=StringType)
viewpoint_validation_ValidationRule_message: Property = Property(name="message", type=StringType)
viewpoint_validation_ValidationRule_m_getMessage: Method = Method(name="getMessage", parameters={Parameter(name='eObj')}, type=StringType)
viewpoint_validation_ValidationRule_m_checkRule: Method = Method(name="checkRule", parameters={Parameter(name='eObj')}, type=BooleanType)
viewpoint_validation_ValidationRule.attributes={viewpoint_validation_ValidationRule_message, viewpoint_validation_ValidationRule_level}
viewpoint_validation_ValidationRule.methods={viewpoint_validation_ValidationRule_m_getMessage, viewpoint_validation_ValidationRule_m_checkRule}

# viewpoint_concern_ConcernSet class attributes and methods

# viewpoint_concern_ConcernDescription class attributes and methods

# viewpoint_validation_ValidationFix class attributes and methods
viewpoint_validation_ValidationFix_name: Property = Property(name="name", type=StringType)
viewpoint_validation_ValidationFix.attributes={viewpoint_validation_ValidationFix_name}

# Relationships
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
description13: BinaryAssociation = BinaryAssociation(
    name="description13",
    ends={
        Property(name="FeatureExtensionDescription", type=viewpoint_DFeatureExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DFeatureExtension14", type=FeatureExtensionDescription, multiplicity=Multiplicity(1, 1))
    }
)
ownedNavigationLinks15: BinaryAssociation = BinaryAssociation(
    name="ownedNavigationLinks15",
    ends={
        Property(name="viewpoint_DNavigationLink", type=viewpoint_DNavigable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DNavigable", type=viewpoint_DNavigationLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
ownedFeatureExtensions11: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureExtensions11",
    ends={
        Property(name="viewpoint_DFeatureExtension", type=viewpoint_DAnalysis, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysis12", type=viewpoint_DFeatureExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationElements22: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationElements22",
    ends={
        Property(name="viewpoint_DRepresentationElement", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
representationElements23: BinaryAssociation = BinaryAssociation(
    name="representationElements23",
    ends={
        Property(name="viewpoint_DRepresentationElement25", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation24", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnotationEntries26: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotationEntries26",
    ends={
        Property(name="AnnotationEntry", type=viewpoint_DRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentation27", type=AnnotationEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramSet16: BinaryAssociation = BinaryAssociation(
    name="diagramSet16",
    ends={
        Property(name="DDiagramSet", type=viewpoint_DRepresentationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentationContainer", type=DDiagramSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models17: BinaryAssociation = BinaryAssociation(
    name="models17",
    ends={
        Property(name="viewpoint_EObject19", type=viewpoint_DRepresentationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentationContainer18", type=viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="viewpoint_EObject21", type=viewpoint_DSemanticDecorator, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DSemanticDecorator", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
ownedRepresentations31: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations31",
    ends={
        Property(name="viewpoint_DRepresentation33", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView32", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtensions34: BinaryAssociation = BinaryAssociation(
    name="ownedExtensions34",
    ends={
        Property(name="viewpoint_MetaModelExtension", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView35", type=viewpoint_MetaModelExtension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allRepresentations36: BinaryAssociation = BinaryAssociation(
    name="allRepresentations36",
    ends={
        Property(name="viewpoint_DRepresentation38", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView37", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999))
    }
)
hiddenRepresentations39: BinaryAssociation = BinaryAssociation(
    name="hiddenRepresentations39",
    ends={
        Property(name="viewpoint_DRepresentation41", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView40", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
semanticElements28: BinaryAssociation = BinaryAssociation(
    name="semanticElements28",
    ends={
        Property(name="viewpoint_EObject30", type=viewpoint_DRepresentationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DRepresentationElement29", type=viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
extensionGroup47: BinaryAssociation = BinaryAssociation(
    name="extensionGroup47",
    ends={
        Property(name="viewpoint_EObject49", type=viewpoint_MetaModelExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_MetaModelExtension48", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
description50: BinaryAssociation = BinaryAssociation(
    name="description50",
    ends={
        Property(name="DecorationDescription", type=viewpoint_Decoration, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_Decoration", type=DecorationDescription, multiplicity=Multiplicity(1, 1))
    }
)
target51: BinaryAssociation = BinaryAssociation(
    name="target51",
    ends={
        Property(name="viewpoint_EObject52", type=viewpoint_DEObjectLink, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DEObjectLink", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
referencedRepresentations42: BinaryAssociation = BinaryAssociation(
    name="referencedRepresentations42",
    ends={
        Property(name="viewpoint_DRepresentation44", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView43", type=viewpoint_DRepresentation, multiplicity=Multiplicity(0, 9999))
    }
)
viewpoint45: BinaryAssociation = BinaryAssociation(
    name="viewpoint45",
    ends={
        Property(name="Viewpoint", type=viewpoint_DView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DView46", type=Viewpoint, multiplicity=Multiplicity(1, 1))
    }
)
data53: BinaryAssociation = BinaryAssociation(
    name="data53",
    ends={
        Property(name="viewpoint_EObject54", type=viewpoint_DAnalysisCustomData, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisCustomData", type=viewpoint_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
description55: BinaryAssociation = BinaryAssociation(
    name="description55",
    ends={
        Property(name="style_StyleDescription", type=viewpoint_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_Style", type=style_StyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
activatedViewpoints56: BinaryAssociation = BinaryAssociation(
    name="activatedViewpoints56",
    ends={
        Property(name="Viewpoint57", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisSessionEObject", type=Viewpoint, multiplicity=Multiplicity(0, 9999))
    }
)
analyses58: BinaryAssociation = BinaryAssociation(
    name="analyses58",
    ends={
        Property(name="viewpoint_DAnalysis60", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DAnalysisSessionEObject59", type=viewpoint_DAnalysis, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSessions61: BinaryAssociation = BinaryAssociation(
    name="ownedSessions61",
    ends={
        Property(name="viewpoint_DAnalysisSessionEObject62", type=viewpoint_SessionManagerEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_SessionManagerEObject", type=viewpoint_DAnalysisSessionEObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members63: BinaryAssociation = BinaryAssociation(
    name="members63",
    ends={
        Property(name="viewpoint_DResource", type=viewpoint_DResourceContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_DResourceContainer", type=viewpoint_DResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelColor64: BinaryAssociation = BinaryAssociation(
    name="labelColor64",
    ends={
        Property(name="viewpoint_RGBValues", type=viewpoint_BasicLabelStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_BasicLabelStyle", type=viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
validationSet71: BinaryAssociation = BinaryAssociation(
    name="validationSet71",
    ends={
        Property(name="validation_ValidationSet", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRepresentations72: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations72",
    ends={
        Property(name="RepresentationDescription", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint73", type=RepresentationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRepresentationExtensions74: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentationExtensions74",
    ends={
        Property(name="RepresentationExtensionDescription", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint75", type=RepresentationExtensionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedJavaExtensions76: BinaryAssociation = BinaryAssociation(
    name="ownedJavaExtensions76",
    ends={
        Property(name="JavaExtension", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint77", type=JavaExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMMExtensions78: BinaryAssociation = BinaryAssociation(
    name="ownedMMExtensions78",
    ends={
        Property(name="MetamodelExtensionSetting", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint79", type=MetamodelExtensionSetting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFeatureExtensions80: BinaryAssociation = BinaryAssociation(
    name="ownedFeatureExtensions80",
    ends={
        Property(name="FeatureExtensionDescription82", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint81", type=FeatureExtensionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedViewpoints65: BinaryAssociation = BinaryAssociation(
    name="ownedViewpoints65",
    ends={
        Property(name="Viewpoint66", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group", type=Viewpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systemColorsPalette67: BinaryAssociation = BinaryAssociation(
    name="systemColorsPalette67",
    ends={
        Property(name="SytemColorsPalette", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group68", type=SytemColorsPalette, multiplicity=Multiplicity(1, 1))
    }
)
userColorsPalettes69: BinaryAssociation = BinaryAssociation(
    name="userColorsPalettes69",
    ends={
        Property(name="UserColorsPalette", type=viewpoint_description_Group, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Group70", type=UserColorsPalette, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel88: BinaryAssociation = BinaryAssociation(
    name="metamodel88",
    ends={
        Property(name="description_viewpoint_EPackage89", type=viewpoint_description_RepresentationExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationExtensionDescription", type=description_viewpoint_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
extensionGroup90: BinaryAssociation = BinaryAssociation(
    name="extensionGroup90",
    ends={
        Property(name="description_viewpoint_EObject", type=viewpoint_description_MetamodelExtensionSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_MetamodelExtensionSetting", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
detailDescriptions91: BinaryAssociation = BinaryAssociation(
    name="detailDescriptions91",
    ends={
        Property(name="tool_RepresentationCreationDescription", type=viewpoint_description_RepresentationElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationElementMapping", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTemplates83: BinaryAssociation = BinaryAssociation(
    name="ownedTemplates83",
    ends={
        Property(name="RepresentationTemplate", type=viewpoint_description_Viewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Viewpoint84", type=RepresentationTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel85: BinaryAssociation = BinaryAssociation(
    name="metamodel85",
    ends={
        Property(name="description_viewpoint_EPackage", type=viewpoint_description_RepresentationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationDescription", type=description_viewpoint_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRepresentations86: BinaryAssociation = BinaryAssociation(
    name="ownedRepresentations86",
    ends={
        Property(name="RepresentationDescription87", type=viewpoint_description_RepresentationTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationTemplate", type=RepresentationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dropDescriptions96: BinaryAssociation = BinaryAssociation(
    name="dropDescriptions96",
    ends={
        Property(name="tool_ContainerDropDescription", type=viewpoint_description_DragAndDropTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DragAndDropTargetDescription", type=tool_ContainerDropDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pasteDescriptions97: BinaryAssociation = BinaryAssociation(
    name="pasteDescriptions97",
    ends={
        Property(name="tool_PasteDescription", type=viewpoint_description_PasteTargetDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_PasteTargetDescription", type=tool_PasteDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptions98: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptions98",
    ends={
        Property(name="DecorationDescription99", type=viewpoint_description_DecorationDescriptionsSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DecorationDescriptionsSet", type=DecorationDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navigationDescriptions92: BinaryAssociation = BinaryAssociation(
    name="navigationDescriptions92",
    ends={
        Property(name="tool_RepresentationNavigationDescription", type=viewpoint_description_RepresentationElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_RepresentationElementMapping93", type=tool_RepresentationNavigationDescription, multiplicity=Multiplicity(0, 9999))
    }
)
eAnnotations94: BinaryAssociation = BinaryAssociation(
    name="eAnnotations94",
    ends={
        Property(name="DAnnotation", type=viewpoint_description_DModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DModelElement", type=DAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details95: BinaryAssociation = BinaryAssociation(
    name="details95",
    ends={
        Property(name="description_viewpoint_EStringToStringMapEntry", type=viewpoint_description_DAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DAnnotation", type=description_viewpoint_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCustomizations101: BinaryAssociation = BinaryAssociation(
    name="featureCustomizations101",
    ends={
        Property(name="EStructuralFeatureCustomization", type=viewpoint_description_VSMElementCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomization", type=EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reuse102: BinaryAssociation = BinaryAssociation(
    name="reuse102",
    ends={
        Property(name="EStructuralFeatureCustomization103", type=viewpoint_description_VSMElementCustomizationReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomizationReuse", type=EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 9999))
    }
)
appliedOn104: BinaryAssociation = BinaryAssociation(
    name="appliedOn104",
    ends={
        Property(name="description_viewpoint_EObject106", type=viewpoint_description_VSMElementCustomizationReuse, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_VSMElementCustomizationReuse105", type=description_viewpoint_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
appliedOn107: BinaryAssociation = BinaryAssociation(
    name="appliedOn107",
    ends={
        Property(name="description_viewpoint_EObject108", type=viewpoint_description_EStructuralFeatureCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EStructuralFeatureCustomization", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
vsmElementCustomizations100: BinaryAssociation = BinaryAssociation(
    name="vsmElementCustomizations100",
    ends={
        Property(name="IVSMElementCustomization", type=viewpoint_description_Customization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Customization", type=IVSMElementCustomization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value109: BinaryAssociation = BinaryAssociation(
    name="value109",
    ends={
        Property(name="description_viewpoint_EObject110", type=viewpoint_description_EReferenceCustomization, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EReferenceCustomization", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
colorSteps111: BinaryAssociation = BinaryAssociation(
    name="colorSteps111",
    ends={
        Property(name="ColorStep", type=viewpoint_description_InterpolatedColor, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_InterpolatedColor", type=ColorStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associatedColor112: BinaryAssociation = BinaryAssociation(
    name="associatedColor112",
    ends={
        Property(name="FixedColor", type=viewpoint_description_ColorStep, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ColorStep", type=FixedColor, multiplicity=Multiplicity(1, 1))
    }
)
systemColors113: BinaryAssociation = BinaryAssociation(
    name="systemColors113",
    ends={
        Property(name="SytemColorsPalette114", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment", type=SytemColorsPalette, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultTools115: BinaryAssociation = BinaryAssociation(
    name="defaultTools115",
    ends={
        Property(name="tool_ToolEntry", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment116", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelBorderStyles117: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyles117",
    ends={
        Property(name="style_LabelBorderStyles", type=viewpoint_description_Environment, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Environment118", type=style_LabelBorderStyles, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entries119: BinaryAssociation = BinaryAssociation(
    name="entries119",
    ends={
        Property(name="SystemColor", type=viewpoint_description_SytemColorsPalette, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_SytemColorsPalette", type=SystemColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries120: BinaryAssociation = BinaryAssociation(
    name="entries120",
    ends={
        Property(name="UserColor", type=viewpoint_description_UserColorsPalette, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_UserColorsPalette", type=UserColor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data121: BinaryAssociation = BinaryAssociation(
    name="data121",
    ends={
        Property(name="description_viewpoint_EObject122", type=viewpoint_description_AnnotationEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_AnnotationEntry", type=description_viewpoint_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labelBorderStyleDescriptions124: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyleDescriptions124",
    ends={
        Property(name="style_LabelBorderStyleDescription", type=viewpoint_style_LabelBorderStyles, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_LabelBorderStyles", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelColor123: BinaryAssociation = BinaryAssociation(
    name="labelColor123",
    ends={
        Property(name="ColorDescription", type=viewpoint_style_BasicLabelStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_BasicLabelStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation129: BinaryAssociation = BinaryAssociation(
    name="initialOperation129",
    ends={
        Property(name="tool_InitialOperation", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription130", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings131: BinaryAssociation = BinaryAssociation(
    name="mappings131",
    ends={
        Property(name="description_DiagramElementMapping", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
oldContainer132: BinaryAssociation = BinaryAssociation(
    name="oldContainer132",
    ends={
        Property(name="tool_DropContainerVariable", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription133", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filters125: BinaryAssociation = BinaryAssociation(
    name="filters125",
    ends={
        Property(name="tool_ToolFilterDescription", type=viewpoint_tool_AbstractToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_AbstractToolDescription", type=tool_ToolFilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element126: BinaryAssociation = BinaryAssociation(
    name="element126",
    ends={
        Property(name="tool_ElementVariable", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription", type=tool_ElementVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView127: BinaryAssociation = BinaryAssociation(
    name="elementView127",
    ends={
        Property(name="tool_ElementViewVariable", type=viewpoint_tool_ToolDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolDescription128", type=tool_ElementViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView145: BinaryAssociation = BinaryAssociation(
    name="containerView145",
    ends={
        Property(name="tool_ContainerViewVariable147", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription146", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copiedView148: BinaryAssociation = BinaryAssociation(
    name="copiedView148",
    ends={
        Property(name="tool_ElementViewVariable150", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription149", type=tool_ElementViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
copiedElement151: BinaryAssociation = BinaryAssociation(
    name="copiedElement151",
    ends={
        Property(name="tool_ElementVariable153", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription152", type=tool_ElementVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation154: BinaryAssociation = BinaryAssociation(
    name="initialOperation154",
    ends={
        Property(name="tool_InitialOperation156", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription155", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element157: BinaryAssociation = BinaryAssociation(
    name="element157",
    ends={
        Property(name="tool_ElementSelectVariable", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newContainer134: BinaryAssociation = BinaryAssociation(
    name="newContainer134",
    ends={
        Property(name="tool_DropContainerVariable136", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription135", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element137: BinaryAssociation = BinaryAssociation(
    name="element137",
    ends={
        Property(name="tool_ElementDropVariable", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription138", type=tool_ElementDropVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newViewContainer139: BinaryAssociation = BinaryAssociation(
    name="newViewContainer139",
    ends={
        Property(name="tool_ContainerViewVariable", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription140", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation141: BinaryAssociation = BinaryAssociation(
    name="initialOperation141",
    ends={
        Property(name="tool_InitialContainerDropOperation", type=viewpoint_tool_ContainerDropDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerDropDescription142", type=tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container143: BinaryAssociation = BinaryAssociation(
    name="container143",
    ends={
        Property(name="tool_DropContainerVariable144", type=viewpoint_tool_PasteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PasteDescription", type=tool_DropContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView158: BinaryAssociation = BinaryAssociation(
    name="containerView158",
    ends={
        Property(name="tool_ContainerViewVariable160", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription159", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container161: BinaryAssociation = BinaryAssociation(
    name="container161",
    ends={
        Property(name="tool_SelectContainerVariable", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription162", type=tool_SelectContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation163: BinaryAssociation = BinaryAssociation(
    name="initialOperation163",
    ends={
        Property(name="tool_InitialOperation165", type=viewpoint_tool_SelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SelectionWizardDescription164", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element166: BinaryAssociation = BinaryAssociation(
    name="element166",
    ends={
        Property(name="tool_ElementSelectVariable167", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerView168: BinaryAssociation = BinaryAssociation(
    name="containerView168",
    ends={
        Property(name="tool_ContainerViewVariable170", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription169", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container171: BinaryAssociation = BinaryAssociation(
    name="container171",
    ends={
        Property(name="tool_SelectContainerVariable173", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription172", type=tool_SelectContainerVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation174: BinaryAssociation = BinaryAssociation(
    name="initialOperation174",
    ends={
        Property(name="tool_InitialOperation176", type=viewpoint_tool_PaneBasedSelectionWizardDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PaneBasedSelectionWizardDescription175", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerViewVariable182: BinaryAssociation = BinaryAssociation(
    name="containerViewVariable182",
    ends={
        Property(name="tool_ContainerViewVariable184", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription183", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationNameVariable185: BinaryAssociation = BinaryAssociation(
    name="representationNameVariable185",
    ends={
        Property(name="tool_NameVariable", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription186", type=tool_NameVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationDescription177: BinaryAssociation = BinaryAssociation(
    name="representationDescription177",
    ends={
        Property(name="RepresentationDescription178", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription", type=RepresentationDescription, multiplicity=Multiplicity(1, 1))
    }
)
initialOperation179: BinaryAssociation = BinaryAssociation(
    name="initialOperation179",
    ends={
        Property(name="tool_InitialOperation181", type=viewpoint_tool_RepresentationCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationCreationDescription180", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation201: BinaryAssociation = BinaryAssociation(
    name="initialOperation201",
    ends={
        Property(name="tool_InitialOperation203", type=viewpoint_tool_OperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_OperationAction202", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters204: BinaryAssociation = BinaryAssociation(
    name="parameters204",
    ends={
        Property(name="tool_ExternalJavaActionParameter", type=viewpoint_tool_ExternalJavaAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ExternalJavaAction", type=tool_ExternalJavaActionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action205: BinaryAssociation = BinaryAssociation(
    name="action205",
    ends={
        Property(name="tool_ExternalJavaAction", type=viewpoint_tool_ExternalJavaActionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ExternalJavaActionCall", type=tool_ExternalJavaAction, multiplicity=Multiplicity(1, 1))
    }
)
menuItemDescription206: BinaryAssociation = BinaryAssociation(
    name="menuItemDescription206",
    ends={
        Property(name="tool_MenuItemDescription207", type=viewpoint_tool_PopupMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_PopupMenu", type=tool_MenuItemDescription, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
representationDescription187: BinaryAssociation = BinaryAssociation(
    name="representationDescription187",
    ends={
        Property(name="RepresentationDescription188", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription", type=RepresentationDescription, multiplicity=Multiplicity(1, 1))
    }
)
containerViewVariable189: BinaryAssociation = BinaryAssociation(
    name="containerViewVariable189",
    ends={
        Property(name="tool_ContainerViewVariable191", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription190", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerVariable192: BinaryAssociation = BinaryAssociation(
    name="containerVariable192",
    ends={
        Property(name="tool_ElementSelectVariable194", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription193", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representationNameVariable195: BinaryAssociation = BinaryAssociation(
    name="representationNameVariable195",
    ends={
        Property(name="tool_NameVariable197", type=viewpoint_tool_RepresentationNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_RepresentationNavigationDescription196", type=tool_NameVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item198: BinaryAssociation = BinaryAssociation(
    name="item198",
    ends={
        Property(name="tool_MenuItemDescription", type=viewpoint_tool_MenuItemDescriptionReference, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_MenuItemDescriptionReference", type=tool_MenuItemDescription, multiplicity=Multiplicity(1, 1))
    }
)
view199: BinaryAssociation = BinaryAssociation(
    name="view199",
    ends={
        Property(name="tool_ContainerViewVariable200", type=viewpoint_tool_OperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_OperationAction", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subVariables208: BinaryAssociation = BinaryAssociation(
    name="subVariables208",
    ends={
        Property(name="viewpoint_tool_VariableContainer", type=tool_SubVariable, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="tool_SubVariable", type=viewpoint_tool_VariableContainer, multiplicity=Multiplicity(1, 1))
    }
)
subModelOperations209: BinaryAssociation = BinaryAssociation(
    name="subModelOperations209",
    ends={
        Property(name="tool_ModelOperation", type=viewpoint_tool_ContainerModelOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerModelOperation", type=tool_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstModelOperations210: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations210",
    ends={
        Property(name="tool_ModelOperation211", type=viewpoint_tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialNodeCreationOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations212: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations212",
    ends={
        Property(name="tool_ModelOperation213", type=viewpoint_tool_InitialOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations214: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations214",
    ends={
        Property(name="tool_ModelOperation215", type=viewpoint_tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitEdgeCreationOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
firstModelOperations216: BinaryAssociation = BinaryAssociation(
    name="firstModelOperations216",
    ends={
        Property(name="tool_ModelOperation217", type=viewpoint_tool_InitialContainerDropOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_InitialContainerDropOperation", type=tool_ModelOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
object218: BinaryAssociation = BinaryAssociation(
    name="object218",
    ends={
        Property(name="tool_viewpoint_EObject", type=viewpoint_tool_SetObject, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SetObject", type=tool_viewpoint_EObject, multiplicity=Multiplicity(0, 1))
    }
)
subModelOperations220: BinaryAssociation = BinaryAssociation(
    name="subModelOperations220",
    ends={
        Property(name="tool_ModelOperation221", type=viewpoint_tool_SwitchChild, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_SwitchChild", type=tool_ModelOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listeners219: BinaryAssociation = BinaryAssociation(
    name="listeners219",
    ends={
        Property(name="tool_FeatureChangeListener", type=viewpoint_tool_ToolFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolFilterDescription", type=tool_FeatureChangeListener, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cases222: BinaryAssociation = BinaryAssociation(
    name="cases222",
    ends={
        Property(name="tool_Case", type=viewpoint_tool_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_Switch", type=tool_Case, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
default223: BinaryAssociation = BinaryAssociation(
    name="default223",
    ends={
        Property(name="tool_Default", type=viewpoint_tool_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_Switch224", type=tool_Default, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedDiagramElements225: BinaryAssociation = BinaryAssociation(
    name="ownedDiagramElements225",
    ends={
        Property(name="DDiagramElement", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram", type=DDiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElements226: BinaryAssociation = BinaryAssociation(
    name="diagramElements226",
    ends={
        Property(name="DDiagramElement228", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram227", type=DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
nodes235: BinaryAssociation = BinaryAssociation(
    name="nodes235",
    ends={
        Property(name="DNode", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram236", type=DNode, multiplicity=Multiplicity(0, 9999))
    }
)
nodeListElements237: BinaryAssociation = BinaryAssociation(
    name="nodeListElements237",
    ends={
        Property(name="DNodeListElement", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram238", type=DNodeListElement, multiplicity=Multiplicity(0, 9999))
    }
)
containers239: BinaryAssociation = BinaryAssociation(
    name="containers239",
    ends={
        Property(name="DDiagramElementContainer", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram240", type=DDiagramElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)
description229: BinaryAssociation = BinaryAssociation(
    name="description229",
    ends={
        Property(name="description_DiagramDescription", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram230", type=description_DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
subDiagrams231: BinaryAssociation = BinaryAssociation(
    name="subDiagrams231",
    ends={
        Property(name="DDiagram", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram232", type=DDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges233: BinaryAssociation = BinaryAssociation(
    name="edges233",
    ends={
        Property(name="DEdge", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram234", type=DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activatedRules248: BinaryAssociation = BinaryAssociation(
    name="activatedRules248",
    ends={
        Property(name="validation_ValidationRule", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram249", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
activateBehaviors250: BinaryAssociation = BinaryAssociation(
    name="activateBehaviors250",
    ends={
        Property(name="tool_BehaviorTool", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram251", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)
filterVariableHistory252: BinaryAssociation = BinaryAssociation(
    name="filterVariableHistory252",
    ends={
        Property(name="FilterVariableHistory", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram253", type=FilterVariableHistory, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
activatedLayers254: BinaryAssociation = BinaryAssociation(
    name="activatedLayers254",
    ends={
        Property(name="description_Layer", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram255", type=description_Layer, multiplicity=Multiplicity(0, 9999))
    }
)
currentConcern241: BinaryAssociation = BinaryAssociation(
    name="currentConcern241",
    ends={
        Property(name="concern_ConcernDescription", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram242", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
activatedFilters243: BinaryAssociation = BinaryAssociation(
    name="activatedFilters243",
    ends={
        Property(name="filter_FilterDescription", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram244", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allFilters245: BinaryAssociation = BinaryAssociation(
    name="allFilters245",
    ends={
        Property(name="filter_FilterDescription247", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram246", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
hiddenElements256: BinaryAssociation = BinaryAssociation(
    name="hiddenElements256",
    ends={
        Property(name="DDiagramElement258", type=viewpoint_diagram_DDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagram257", type=DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
graphicalFilters266: BinaryAssociation = BinaryAssociation(
    name="graphicalFilters266",
    ends={
        Property(name="GraphicalFilter", type=viewpoint_diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElement267", type=GraphicalFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentLayers259: BinaryAssociation = BinaryAssociation(
    name="parentLayers259",
    ends={
        Property(name="description_Layer260", type=viewpoint_diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElement", type=description_Layer, multiplicity=Multiplicity(0, 9999))
    }
)
decorations261: BinaryAssociation = BinaryAssociation(
    name="decorations261",
    ends={
        Property(name="diagram_viewpoint_Decoration", type=viewpoint_diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElement262", type=diagram_viewpoint_Decoration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagramElementMapping263: BinaryAssociation = BinaryAssociation(
    name="diagramElementMapping263",
    ends={
        Property(name="description_DiagramElementMapping265", type=viewpoint_diagram_DDiagramElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElement264", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 1))
    }
)
target269: BinaryAssociation = BinaryAssociation(
    name="target269",
    ends={
        Property(name="DDiagram270", type=viewpoint_diagram_DDiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramLink", type=DDiagram, multiplicity=Multiplicity(1, 1))
    }
)
node271: BinaryAssociation = BinaryAssociation(
    name="node271",
    ends={
        Property(name="EdgeTarget", type=viewpoint_diagram_DDiagramLink, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramLink272", type=EdgeTarget, multiplicity=Multiplicity(0, 1))
    }
)
compositeFilterDescriptions268: BinaryAssociation = BinaryAssociation(
    name="compositeFilterDescriptions268",
    ends={
        Property(name="filter_CompositeFilterDescription", type=viewpoint_diagram_AppliedCompositeFilters, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_AppliedCompositeFilters", type=filter_CompositeFilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle275: BinaryAssociation = BinaryAssociation(
    name="ownedStyle275",
    ends={
        Property(name="NodeStyle", type=viewpoint_diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNode", type=NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDetails276: BinaryAssociation = BinaryAssociation(
    name="ownedDetails276",
    ends={
        Property(name="DDiagram278", type=viewpoint_diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNode277", type=DDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBorderedNodes273: BinaryAssociation = BinaryAssociation(
    name="ownedBorderedNodes273",
    ends={
        Property(name="DNode274", type=viewpoint_diagram_AbstractDNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_AbstractDNode", type=DNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalStyle279: BinaryAssociation = BinaryAssociation(
    name="originalStyle279",
    ends={
        Property(name="diagram_viewpoint_Style", type=viewpoint_diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNode280", type=diagram_viewpoint_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping281: BinaryAssociation = BinaryAssociation(
    name="actualMapping281",
    ends={
        Property(name="description_NodeMapping", type=viewpoint_diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNode282", type=description_NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping283: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping283",
    ends={
        Property(name="description_NodeMapping285", type=viewpoint_diagram_DNode, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNode284", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
elements291: BinaryAssociation = BinaryAssociation(
    name="elements291",
    ends={
        Property(name="DDiagramElement293", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer292", type=DDiagramElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle294: BinaryAssociation = BinaryAssociation(
    name="ownedStyle294",
    ends={
        Property(name="ContainerStyle", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer295", type=ContainerStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDetails296: BinaryAssociation = BinaryAssociation(
    name="ownedDetails296",
    ends={
        Property(name="DDiagram298", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer297", type=DDiagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalStyle299: BinaryAssociation = BinaryAssociation(
    name="originalStyle299",
    ends={
        Property(name="diagram_viewpoint_Style301", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer300", type=diagram_viewpoint_Style, multiplicity=Multiplicity(0, 1))
    }
)
nodes286: BinaryAssociation = BinaryAssociation(
    name="nodes286",
    ends={
        Property(name="DNode287", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer", type=DNode, multiplicity=Multiplicity(0, 9999))
    }
)
containers288: BinaryAssociation = BinaryAssociation(
    name="containers288",
    ends={
        Property(name="DDiagramElementContainer290", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer289", type=DDiagramElementContainer, multiplicity=Multiplicity(0, 9999))
    }
)
ownedDiagramElements307: BinaryAssociation = BinaryAssociation(
    name="ownedDiagramElements307",
    ends={
        Property(name="DDiagramElement308", type=viewpoint_diagram_DNodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeContainer", type=DDiagramElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actualMapping302: BinaryAssociation = BinaryAssociation(
    name="actualMapping302",
    ends={
        Property(name="description_ContainerMapping", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer303", type=description_ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping304: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping304",
    ends={
        Property(name="description_ContainerMapping306", type=viewpoint_diagram_DDiagramElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramElementContainer305", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStyle311: BinaryAssociation = BinaryAssociation(
    name="ownedStyle311",
    ends={
        Property(name="NodeStyle312", type=viewpoint_diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeListElement", type=NodeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalStyle313: BinaryAssociation = BinaryAssociation(
    name="originalStyle313",
    ends={
        Property(name="diagram_viewpoint_Style315", type=viewpoint_diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeListElement314", type=diagram_viewpoint_Style, multiplicity=Multiplicity(0, 1))
    }
)
actualMapping316: BinaryAssociation = BinaryAssociation(
    name="actualMapping316",
    ends={
        Property(name="description_NodeMapping318", type=viewpoint_diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeListElement317", type=description_NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
candidatesMapping319: BinaryAssociation = BinaryAssociation(
    name="candidatesMapping319",
    ends={
        Property(name="description_NodeMapping321", type=viewpoint_diagram_DNodeListElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeListElement320", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElements309: BinaryAssociation = BinaryAssociation(
    name="ownedElements309",
    ends={
        Property(name="DNodeListElement310", type=viewpoint_diagram_DNodeList, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DNodeList", type=DNodeListElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceNode323: BinaryAssociation = BinaryAssociation(
    name="sourceNode323",
    ends={
        Property(name="diagram", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="EdgeTarget324", type=EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
targetNode325: BinaryAssociation = BinaryAssociation(
    name="targetNode325",
    ends={
        Property(name="diagram327", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="EdgeTarget326", type=EdgeTarget, multiplicity=Multiplicity(1, 1))
    }
)
actualMapping328: BinaryAssociation = BinaryAssociation(
    name="actualMapping328",
    ends={
        Property(name="description_IEdgeMapping", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DEdge329", type=description_IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
ownedStyle322: BinaryAssociation = BinaryAssociation(
    name="ownedStyle322",
    ends={
        Property(name="EdgeStyle", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DEdge", type=EdgeStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description336: BinaryAssociation = BinaryAssociation(
    name="description336",
    ends={
        Property(name="description_DiagramDescription337", type=viewpoint_diagram_DDiagramSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramSet", type=description_DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
diagrams338: BinaryAssociation = BinaryAssociation(
    name="diagrams338",
    ends={
        Property(name="DDiagram340", type=viewpoint_diagram_DDiagramSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramSet339", type=DDiagram, multiplicity=Multiplicity(0, 9999))
    }
)
originalStyle330: BinaryAssociation = BinaryAssociation(
    name="originalStyle330",
    ends={
        Property(name="diagram_viewpoint_Style332", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DEdge331", type=diagram_viewpoint_Style, multiplicity=Multiplicity(0, 1))
    }
)
path333: BinaryAssociation = BinaryAssociation(
    name="path333",
    ends={
        Property(name="EdgeTarget335", type=viewpoint_diagram_DEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DEdge334", type=EdgeTarget, multiplicity=Multiplicity(0, 9999))
    }
)
backgroundColor343: BinaryAssociation = BinaryAssociation(
    name="backgroundColor343",
    ends={
        Property(name="diagram_viewpoint_RGBValues", type=viewpoint_diagram_Dot, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_Dot", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
view341: BinaryAssociation = BinaryAssociation(
    name="view341",
    ends={
        Property(name="diagram_viewpoint_DRepresentationContainer", type=viewpoint_diagram_DDiagramSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DDiagramSet342", type=diagram_viewpoint_DRepresentationContainer, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor344: BinaryAssociation = BinaryAssociation(
    name="backgroundColor344",
    ends={
        Property(name="diagram_viewpoint_RGBValues345", type=viewpoint_diagram_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_GaugeSection", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor346: BinaryAssociation = BinaryAssociation(
    name="foregroundColor346",
    ends={
        Property(name="diagram_viewpoint_RGBValues348", type=viewpoint_diagram_GaugeSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_GaugeSection347", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
backgroundColor354: BinaryAssociation = BinaryAssociation(
    name="backgroundColor354",
    ends={
        Property(name="diagram_viewpoint_RGBValues355", type=viewpoint_diagram_ShapeContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ShapeContainerStyle", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
backgroundColor349: BinaryAssociation = BinaryAssociation(
    name="backgroundColor349",
    ends={
        Property(name="diagram_viewpoint_RGBValues350", type=viewpoint_diagram_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_FlatContainerStyle", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foregroundColor351: BinaryAssociation = BinaryAssociation(
    name="foregroundColor351",
    ends={
        Property(name="diagram_viewpoint_RGBValues353", type=viewpoint_diagram_FlatContainerStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_FlatContainerStyle352", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color358: BinaryAssociation = BinaryAssociation(
    name="color358",
    ends={
        Property(name="diagram_viewpoint_RGBValues359", type=viewpoint_diagram_Ellipse, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_Ellipse", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color356: BinaryAssociation = BinaryAssociation(
    name="color356",
    ends={
        Property(name="diagram_viewpoint_RGBValues357", type=viewpoint_diagram_Square, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_Square", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color360: BinaryAssociation = BinaryAssociation(
    name="color360",
    ends={
        Property(name="diagram_viewpoint_RGBValues361", type=viewpoint_diagram_Lozenge, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_Lozenge", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color362: BinaryAssociation = BinaryAssociation(
    name="color362",
    ends={
        Property(name="diagram_viewpoint_RGBValues363", type=viewpoint_diagram_BundledImage, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_BundledImage", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
strokeColor370: BinaryAssociation = BinaryAssociation(
    name="strokeColor370",
    ends={
        Property(name="diagram_viewpoint_RGBValues371", type=viewpoint_diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_EdgeStyle", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingEdges364: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges364",
    ends={
        Property(name="diagram366", type=viewpoint_diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="DEdge365", type=DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomingEdges367: BinaryAssociation = BinaryAssociation(
    name="incomingEdges367",
    ends={
        Property(name="diagram369", type=viewpoint_diagram_EdgeTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="DEdge368", type=DEdge, multiplicity=Multiplicity(0, 9999))
    }
)
endLabelStyle376: BinaryAssociation = BinaryAssociation(
    name="endLabelStyle376",
    ends={
        Property(name="viewpoint_diagram_EdgeStyle377", type=EndLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="EndLabelStyle", type=viewpoint_diagram_EdgeStyle, multiplicity=Multiplicity(1, 1))
    }
)
beginLabelStyle372: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyle372",
    ends={
        Property(name="BeginLabelStyle", type=viewpoint_diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_EdgeStyle373", type=BeginLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyle374: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyle374",
    ends={
        Property(name="CenterLabelStyle", type=viewpoint_diagram_EdgeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_EdgeStyle375", type=CenterLabelStyle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
borderColor379: BinaryAssociation = BinaryAssociation(
    name="borderColor379",
    ends={
        Property(name="diagram_viewpoint_RGBValues380", type=viewpoint_diagram_BorderedStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_BorderedStyle", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color381: BinaryAssociation = BinaryAssociation(
    name="color381",
    ends={
        Property(name="diagram_viewpoint_RGBValues382", type=viewpoint_diagram_Note, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_Note", type=diagram_viewpoint_RGBValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedValues383: BinaryAssociation = BinaryAssociation(
    name="ownedValues383",
    ends={
        Property(name="FilterVariableValue", type=viewpoint_diagram_FilterVariableHistory, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_FilterVariableHistory", type=FilterVariableValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections378: BinaryAssociation = BinaryAssociation(
    name="sections378",
    ends={
        Property(name="GaugeSection", type=viewpoint_diagram_GaugeCompositeStyle, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_GaugeCompositeStyle", type=GaugeSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDefinition384: BinaryAssociation = BinaryAssociation(
    name="variableDefinition384",
    ends={
        Property(name="filter_FilterVariable", type=viewpoint_diagram_FilterVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_FilterVariableValue", type=filter_FilterVariable, multiplicity=Multiplicity(1, 1))
    }
)
modelElement385: BinaryAssociation = BinaryAssociation(
    name="modelElement385",
    ends={
        Property(name="diagram_viewpoint_EObject", type=viewpoint_diagram_FilterVariableValue, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_FilterVariableValue386", type=diagram_viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
cache389: BinaryAssociation = BinaryAssociation(
    name="cache389",
    ends={
        Property(name="viewpoint_diagram_ComputedStyleDescriptionRegistry390", type=DiagramElementMapping2ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="DiagramElementMapping2ModelElement", type=viewpoint_diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1))
    }
)
key391: BinaryAssociation = BinaryAssociation(
    name="key391",
    ends={
        Property(name="description_DiagramElementMapping392", type=viewpoint_diagram_DiagramElementMapping2ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DiagramElementMapping2ModelElement", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
value393: BinaryAssociation = BinaryAssociation(
    name="value393",
    ends={
        Property(name="ModelElement2ViewVariable", type=viewpoint_diagram_DiagramElementMapping2ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_DiagramElementMapping2ModelElement394", type=ModelElement2ViewVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
computedStyleDescriptions387: BinaryAssociation = BinaryAssociation(
    name="computedStyleDescriptions387",
    ends={
        Property(name="style_StyleDescription388", type=viewpoint_diagram_ComputedStyleDescriptionRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ComputedStyleDescriptionRegistry", type=style_StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value401: BinaryAssociation = BinaryAssociation(
    name="value401",
    ends={
        Property(name="ContainerVariable2StyleDescription", type=viewpoint_diagram_ViewVariable2ContainerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ViewVariable2ContainerVariable402", type=ContainerVariable2StyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key403: BinaryAssociation = BinaryAssociation(
    name="key403",
    ends={
        Property(name="diagram_viewpoint_EObject404", type=viewpoint_diagram_ContainerVariable2StyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ContainerVariable2StyleDescription", type=diagram_viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value405: BinaryAssociation = BinaryAssociation(
    name="value405",
    ends={
        Property(name="style_StyleDescription407", type=viewpoint_diagram_ContainerVariable2StyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ContainerVariable2StyleDescription406", type=style_StyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
key395: BinaryAssociation = BinaryAssociation(
    name="key395",
    ends={
        Property(name="diagram_viewpoint_EObject396", type=viewpoint_diagram_ModelElement2ViewVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ModelElement2ViewVariable", type=diagram_viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value397: BinaryAssociation = BinaryAssociation(
    name="value397",
    ends={
        Property(name="ViewVariable2ContainerVariable", type=viewpoint_diagram_ModelElement2ViewVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ModelElement2ViewVariable398", type=ViewVariable2ContainerVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key399: BinaryAssociation = BinaryAssociation(
    name="key399",
    ends={
        Property(name="diagram_viewpoint_EObject400", type=viewpoint_diagram_ViewVariable2ContainerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_diagram_ViewVariable2ContainerVariable", type=diagram_viewpoint_EObject, multiplicity=Multiplicity(1, 1))
    }
)
allEdgeMappings410: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings410",
    ends={
        Property(name="description_EdgeMapping", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription411", type=description_EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allNodeMappings412: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings412",
    ends={
        Property(name="description_NodeMapping414", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription413", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings415: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings415",
    ends={
        Property(name="description_ContainerMapping417", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription416", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
filters408: BinaryAssociation = BinaryAssociation(
    name="filters408",
    ends={
        Property(name="filter_FilterDescription409", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultConcern425: BinaryAssociation = BinaryAssociation(
    name="defaultConcern425",
    ends={
        Property(name="concern_ConcernDescription427", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription426", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 1))
    }
)
validationSet418: BinaryAssociation = BinaryAssociation(
    name="validationSet418",
    ends={
        Property(name="validation_ValidationSet420", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription419", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns421: BinaryAssociation = BinaryAssociation(
    name="concerns421",
    ends={
        Property(name="concern_ConcernSet", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription422", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allTools423: BinaryAssociation = BinaryAssociation(
    name="allTools423",
    ends={
        Property(name="tool_AbstractToolDescription", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription424", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
allActivatedTools444: BinaryAssociation = BinaryAssociation(
    name="allActivatedTools444",
    ends={
        Property(name="tool_AbstractToolDescription446", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription445", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
nodeMappings447: BinaryAssociation = BinaryAssociation(
    name="nodeMappings447",
    ends={
        Property(name="description_NodeMapping449", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription448", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappings450: BinaryAssociation = BinaryAssociation(
    name="edgeMappings450",
    ends={
        Property(name="description_EdgeMapping452", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription451", type=description_EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init428: BinaryAssociation = BinaryAssociation(
    name="init428",
    ends={
        Property(name="tool_RepresentationCreationDescription430", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription429", type=tool_RepresentationCreationDescription, multiplicity=Multiplicity(0, 1))
    }
)
layout431: BinaryAssociation = BinaryAssociation(
    name="layout431",
    ends={
        Property(name="description_Layout", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription432", type=description_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagramInitialisation433: BinaryAssociation = BinaryAssociation(
    name="diagramInitialisation433",
    ends={
        Property(name="tool_InitialOperation435", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription434", type=tool_InitialOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultLayer436: BinaryAssociation = BinaryAssociation(
    name="defaultLayer436",
    ends={
        Property(name="description_Layer438", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription437", type=description_Layer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalLayers439: BinaryAssociation = BinaryAssociation(
    name="additionalLayers439",
    ends={
        Property(name="description_AdditionalLayer", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription440", type=description_AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allLayers441: BinaryAssociation = BinaryAssociation(
    name="allLayers441",
    ends={
        Property(name="description_Layer443", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription442", type=description_Layer, multiplicity=Multiplicity(0, 9999))
    }
)
toolSection461: BinaryAssociation = BinaryAssociation(
    name="toolSection461",
    ends={
        Property(name="tool_ToolSection", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription462", type=tool_ToolSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reusedTools463: BinaryAssociation = BinaryAssociation(
    name="reusedTools463",
    ends={
        Property(name="tool_AbstractToolDescription465", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription464", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
importedDiagram466: BinaryAssociation = BinaryAssociation(
    name="importedDiagram466",
    ends={
        Property(name="description_DiagramDescription467", type=viewpoint_description_DiagramImportDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramImportDescription", type=description_DiagramDescription, multiplicity=Multiplicity(0, 1))
    }
)
layers468: BinaryAssociation = BinaryAssociation(
    name="layers468",
    ends={
        Property(name="description_AdditionalLayer469", type=viewpoint_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramExtensionDescription", type=description_AdditionalLayer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports453: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports453",
    ends={
        Property(name="description_EdgeMappingImport", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription454", type=description_EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings455: BinaryAssociation = BinaryAssociation(
    name="containerMappings455",
    ends={
        Property(name="description_ContainerMapping457", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription456", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings458: BinaryAssociation = BinaryAssociation(
    name="reusedMappings458",
    ends={
        Property(name="description_DiagramElementMapping460", type=viewpoint_description_DiagramDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramDescription459", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
validationSet470: BinaryAssociation = BinaryAssociation(
    name="validationSet470",
    ends={
        Property(name="validation_ValidationSet472", type=viewpoint_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramExtensionDescription471", type=validation_ValidationSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
concerns473: BinaryAssociation = BinaryAssociation(
    name="concerns473",
    ends={
        Property(name="concern_ConcernSet475", type=viewpoint_description_DiagramExtensionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramExtensionDescription474", type=concern_ConcernSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deletionDescription476: BinaryAssociation = BinaryAssociation(
    name="deletionDescription476",
    ends={
        Property(name="tool_DeleteElementDescription", type=viewpoint_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramElementMapping", type=tool_DeleteElementDescription, multiplicity=Multiplicity(0, 1))
    }
)
labelDirectEdit477: BinaryAssociation = BinaryAssociation(
    name="labelDirectEdit477",
    ends={
        Property(name="tool_DirectEditLabel", type=viewpoint_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_DiagramElementMapping478", type=tool_DirectEditLabel, multiplicity=Multiplicity(0, 1))
    }
)
doubleClickDescription479: BinaryAssociation = BinaryAssociation(
    name="doubleClickDescription479",
    ends={
        Property(name="diagram480", type=viewpoint_description_DiagramElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="description", type=tool_DoubleClickDescription, multiplicity=Multiplicity(0, 1))
    }
)
borderedNodeMappings481: BinaryAssociation = BinaryAssociation(
    name="borderedNodeMappings481",
    ends={
        Property(name="description_NodeMapping482", type=viewpoint_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_AbstractNodeMapping", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedBorderedNodeMappings483: BinaryAssociation = BinaryAssociation(
    name="reusedBorderedNodeMappings483",
    ends={
        Property(name="description_NodeMapping485", type=viewpoint_description_AbstractNodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_AbstractNodeMapping484", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedNodeMappings494: BinaryAssociation = BinaryAssociation(
    name="reusedNodeMappings494",
    ends={
        Property(name="description_NodeMapping496", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping495", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
subContainerMappings497: BinaryAssociation = BinaryAssociation(
    name="subContainerMappings497",
    ends={
        Property(name="description_ContainerMapping499", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping498", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style486: BinaryAssociation = BinaryAssociation(
    name="style486",
    ends={
        Property(name="style_NodeStyleDescription", type=viewpoint_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_NodeMapping", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles487: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles487",
    ends={
        Property(name="description_ConditionalNodeStyleDescription", type=viewpoint_description_NodeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_NodeMapping488", type=description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodeMappings489: BinaryAssociation = BinaryAssociation(
    name="subNodeMappings489",
    ends={
        Property(name="description_NodeMapping490", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allNodeMappings491: BinaryAssociation = BinaryAssociation(
    name="allNodeMappings491",
    ends={
        Property(name="description_NodeMapping493", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping492", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
reusedContainerMappings500: BinaryAssociation = BinaryAssociation(
    name="reusedContainerMappings500",
    ends={
        Property(name="description_ContainerMapping502", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping501", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allContainerMappings503: BinaryAssociation = BinaryAssociation(
    name="allContainerMappings503",
    ends={
        Property(name="description_ContainerMapping505", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping504", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999))
    }
)
style506: BinaryAssociation = BinaryAssociation(
    name="style506",
    ends={
        Property(name="style_ContainerStyleDescription", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping507", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditionnalStyles508: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles508",
    ends={
        Property(name="description_ConditionalContainerStyleDescription", type=viewpoint_description_ContainerMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMapping509", type=description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMapping510: BinaryAssociation = BinaryAssociation(
    name="importedMapping510",
    ends={
        Property(name="description_NodeMapping511", type=viewpoint_description_NodeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_NodeMappingImport", type=description_NodeMapping, multiplicity=Multiplicity(1, 1))
    }
)
importedMapping512: BinaryAssociation = BinaryAssociation(
    name="importedMapping512",
    ends={
        Property(name="description_ContainerMapping513", type=viewpoint_description_ContainerMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ContainerMappingImport", type=description_ContainerMapping, multiplicity=Multiplicity(1, 1))
    }
)
style519: BinaryAssociation = BinaryAssociation(
    name="style519",
    ends={
        Property(name="viewpoint_description_EdgeMapping520", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="style_EdgeStyleDescription", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles521: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles521",
    ends={
        Property(name="description_ConditionalEdgeStyleDescription", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMapping522", type=description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceMapping514: BinaryAssociation = BinaryAssociation(
    name="sourceMapping514",
    ends={
        Property(name="description_DiagramElementMapping515", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMapping", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
targetMapping516: BinaryAssociation = BinaryAssociation(
    name="targetMapping516",
    ends={
        Property(name="description_DiagramElementMapping518", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMapping517", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
style532: BinaryAssociation = BinaryAssociation(
    name="style532",
    ends={
        Property(name="style_NodeStyleDescription533", type=viewpoint_description_ConditionalNodeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ConditionalNodeStyleDescription", type=style_NodeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style534: BinaryAssociation = BinaryAssociation(
    name="style534",
    ends={
        Property(name="style_EdgeStyleDescription535", type=viewpoint_description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ConditionalEdgeStyleDescription", type=style_EdgeStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reconnections523: BinaryAssociation = BinaryAssociation(
    name="reconnections523",
    ends={
        Property(name="tool_ReconnectEdgeDescription", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMapping524", type=tool_ReconnectEdgeDescription, multiplicity=Multiplicity(0, 9999))
    }
)
pathNodeMapping525: BinaryAssociation = BinaryAssociation(
    name="pathNodeMapping525",
    ends={
        Property(name="description_AbstractNodeMapping", type=viewpoint_description_EdgeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMapping526", type=description_AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
importedMapping527: BinaryAssociation = BinaryAssociation(
    name="importedMapping527",
    ends={
        Property(name="description_IEdgeMapping528", type=viewpoint_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMappingImport", type=description_IEdgeMapping, multiplicity=Multiplicity(1, 1))
    }
)
conditionnalStyles529: BinaryAssociation = BinaryAssociation(
    name="conditionnalStyles529",
    ends={
        Property(name="description_ConditionalEdgeStyleDescription531", type=viewpoint_description_EdgeMappingImport, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_EdgeMappingImport530", type=description_ConditionalEdgeStyleDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style536: BinaryAssociation = BinaryAssociation(
    name="style536",
    ends={
        Property(name="style_ContainerStyleDescription537", type=viewpoint_description_ConditionalContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_ConditionalContainerStyleDescription", type=style_ContainerStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeMapping538: BinaryAssociation = BinaryAssociation(
    name="nodeMapping538",
    ends={
        Property(name="description_AbstractNodeMapping539", type=viewpoint_description_OrderedTreeLayout, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_OrderedTreeLayout", type=description_AbstractNodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
mappings540: BinaryAssociation = BinaryAssociation(
    name="mappings540",
    ends={
        Property(name="description_DiagramElementMapping541", type=viewpoint_description_MappingBasedDecoration, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_MappingBasedDecoration", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
edgeMappings544: BinaryAssociation = BinaryAssociation(
    name="edgeMappings544",
    ends={
        Property(name="description_EdgeMapping546", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer545", type=description_EdgeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings542: BinaryAssociation = BinaryAssociation(
    name="nodeMappings542",
    ends={
        Property(name="description_NodeMapping543", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer", type=description_NodeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edgeMappingImports547: BinaryAssociation = BinaryAssociation(
    name="edgeMappingImports547",
    ends={
        Property(name="description_EdgeMappingImport549", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer548", type=description_EdgeMappingImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerMappings550: BinaryAssociation = BinaryAssociation(
    name="containerMappings550",
    ends={
        Property(name="description_ContainerMapping552", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer551", type=description_ContainerMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedMappings553: BinaryAssociation = BinaryAssociation(
    name="reusedMappings553",
    ends={
        Property(name="description_DiagramElementMapping555", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer554", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
allTools556: BinaryAssociation = BinaryAssociation(
    name="allTools556",
    ends={
        Property(name="tool_AbstractToolDescription558", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer557", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
toolSections559: BinaryAssociation = BinaryAssociation(
    name="toolSections559",
    ends={
        Property(name="tool_ToolSection561", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer560", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedTools562: BinaryAssociation = BinaryAssociation(
    name="reusedTools562",
    ends={
        Property(name="tool_AbstractToolDescription564", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer563", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999))
    }
)
decorationDescriptionsSet565: BinaryAssociation = BinaryAssociation(
    name="decorationDescriptionsSet565",
    ends={
        Property(name="DecorationDescriptionsSet", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer566", type=DecorationDescriptionsSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allEdgeMappings567: BinaryAssociation = BinaryAssociation(
    name="allEdgeMappings567",
    ends={
        Property(name="description_EdgeMapping569", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer568", type=description_EdgeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
customization570: BinaryAssociation = BinaryAssociation(
    name="customization570",
    ends={
        Property(name="Customization", type=viewpoint_description_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_description_Layer571", type=Customization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color574: BinaryAssociation = BinaryAssociation(
    name="color574",
    ends={
        Property(name="ColorDescription575", type=viewpoint_style_SquareDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_SquareDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
borderColor572: BinaryAssociation = BinaryAssociation(
    name="borderColor572",
    ends={
        Property(name="ColorDescription573", type=viewpoint_style_BorderedStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_BorderedStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color580: BinaryAssociation = BinaryAssociation(
    name="color580",
    ends={
        Property(name="ColorDescription581", type=viewpoint_style_BundledImageDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_BundledImageDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color576: BinaryAssociation = BinaryAssociation(
    name="color576",
    ends={
        Property(name="ColorDescription577", type=viewpoint_style_LozengeNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_LozengeNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color578: BinaryAssociation = BinaryAssociation(
    name="color578",
    ends={
        Property(name="ColorDescription579", type=viewpoint_style_EllipseNodeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_EllipseNodeDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
color582: BinaryAssociation = BinaryAssociation(
    name="color582",
    ends={
        Property(name="ColorDescription583", type=viewpoint_style_NoteDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_NoteDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor584: BinaryAssociation = BinaryAssociation(
    name="backgroundColor584",
    ends={
        Property(name="ColorDescription585", type=viewpoint_style_DotDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_DotDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
sections586: BinaryAssociation = BinaryAssociation(
    name="sections586",
    ends={
        Property(name="style_GaugeSectionDescription", type=viewpoint_style_GaugeCompositeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_GaugeCompositeStyleDescription", type=style_GaugeSectionDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
backgroundColor587: BinaryAssociation = BinaryAssociation(
    name="backgroundColor587",
    ends={
        Property(name="ColorDescription588", type=viewpoint_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_GaugeSectionDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor589: BinaryAssociation = BinaryAssociation(
    name="foregroundColor589",
    ends={
        Property(name="ColorDescription591", type=viewpoint_style_GaugeSectionDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_GaugeSectionDescription590", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
backgroundColor592: BinaryAssociation = BinaryAssociation(
    name="backgroundColor592",
    ends={
        Property(name="ColorDescription593", type=viewpoint_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_FlatContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
foregroundColor594: BinaryAssociation = BinaryAssociation(
    name="foregroundColor594",
    ends={
        Property(name="ColorDescription596", type=viewpoint_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_FlatContainerStyleDescription595", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
labelBorderStyle597: BinaryAssociation = BinaryAssociation(
    name="labelBorderStyle597",
    ends={
        Property(name="style_LabelBorderStyleDescription599", type=viewpoint_style_FlatContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_FlatContainerStyleDescription598", type=style_LabelBorderStyleDescription, multiplicity=Multiplicity(0, 1))
    }
)
backgroundColor600: BinaryAssociation = BinaryAssociation(
    name="backgroundColor600",
    ends={
        Property(name="ColorDescription601", type=viewpoint_style_ShapeContainerStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_ShapeContainerStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
strokeColor602: BinaryAssociation = BinaryAssociation(
    name="strokeColor602",
    ends={
        Property(name="ColorDescription603", type=viewpoint_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_EdgeStyleDescription", type=ColorDescription, multiplicity=Multiplicity(1, 1))
    }
)
subSections612: BinaryAssociation = BinaryAssociation(
    name="subSections612",
    ends={
        Property(name="tool_ToolSection614", type=viewpoint_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolSection613", type=tool_ToolSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
beginLabelStyleDescription604: BinaryAssociation = BinaryAssociation(
    name="beginLabelStyleDescription604",
    ends={
        Property(name="style_BeginLabelStyleDescription", type=viewpoint_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_EdgeStyleDescription605", type=style_BeginLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
centerLabelStyleDescription606: BinaryAssociation = BinaryAssociation(
    name="centerLabelStyleDescription606",
    ends={
        Property(name="style_CenterLabelStyleDescription", type=viewpoint_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_EdgeStyleDescription607", type=style_CenterLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endLabelStyleDescription608: BinaryAssociation = BinaryAssociation(
    name="endLabelStyleDescription608",
    ends={
        Property(name="style_EndLabelStyleDescription", type=viewpoint_style_EdgeStyleDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_style_EdgeStyleDescription609", type=style_EndLabelStyleDescription, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTools610: BinaryAssociation = BinaryAssociation(
    name="ownedTools610",
    ends={
        Property(name="tool_ToolEntry611", type=viewpoint_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolSection", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupExtensions620: BinaryAssociation = BinaryAssociation(
    name="groupExtensions620",
    ends={
        Property(name="tool_ToolGroupExtension", type=viewpoint_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolSection621", type=tool_ToolGroupExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tools622: BinaryAssociation = BinaryAssociation(
    name="tools622",
    ends={
        Property(name="tool_AbstractToolDescription623", type=viewpoint_tool_ToolGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolGroup", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
popupMenus615: BinaryAssociation = BinaryAssociation(
    name="popupMenus615",
    ends={
        Property(name="tool_PopupMenu", type=viewpoint_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolSection616", type=tool_PopupMenu, multiplicity=Multiplicity(0, 9999))
    }
)
reusedTools617: BinaryAssociation = BinaryAssociation(
    name="reusedTools617",
    ends={
        Property(name="tool_ToolEntry619", type=viewpoint_tool_ToolSection, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolSection618", type=tool_ToolEntry, multiplicity=Multiplicity(0, 9999))
    }
)
group624: BinaryAssociation = BinaryAssociation(
    name="group624",
    ends={
        Property(name="tool_ToolGroup", type=viewpoint_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolGroupExtension", type=tool_ToolGroup, multiplicity=Multiplicity(1, 1))
    }
)
tools625: BinaryAssociation = BinaryAssociation(
    name="tools625",
    ends={
        Property(name="tool_AbstractToolDescription627", type=viewpoint_tool_ToolGroupExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ToolGroupExtension626", type=tool_AbstractToolDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeMappings628: BinaryAssociation = BinaryAssociation(
    name="nodeMappings628",
    ends={
        Property(name="description_NodeMapping629", type=viewpoint_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_NodeCreationDescription", type=description_NodeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable630: BinaryAssociation = BinaryAssociation(
    name="variable630",
    ends={
        Property(name="tool_NodeCreationVariable", type=viewpoint_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_NodeCreationDescription631", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable632: BinaryAssociation = BinaryAssociation(
    name="viewVariable632",
    ends={
        Property(name="tool_ContainerViewVariable634", type=viewpoint_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_NodeCreationDescription633", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation635: BinaryAssociation = BinaryAssociation(
    name="initialOperation635",
    ends={
        Property(name="tool_InitialNodeCreationOperation", type=viewpoint_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_NodeCreationDescription636", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings637: BinaryAssociation = BinaryAssociation(
    name="extraMappings637",
    ends={
        Property(name="description_AbstractNodeMapping639", type=viewpoint_tool_NodeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_NodeCreationDescription638", type=description_AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
edgeMappings640: BinaryAssociation = BinaryAssociation(
    name="edgeMappings640",
    ends={
        Property(name="description_EdgeMapping641", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription", type=description_EdgeMapping, multiplicity=Multiplicity(1, 9999))
    }
)
sourceVariable642: BinaryAssociation = BinaryAssociation(
    name="sourceVariable642",
    ends={
        Property(name="tool_SourceEdgeCreationVariable", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription643", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable644: BinaryAssociation = BinaryAssociation(
    name="targetVariable644",
    ends={
        Property(name="tool_TargetEdgeCreationVariable", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription645", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceViewVariable646: BinaryAssociation = BinaryAssociation(
    name="sourceViewVariable646",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription647", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetViewVariable648: BinaryAssociation = BinaryAssociation(
    name="targetViewVariable648",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription649", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation650: BinaryAssociation = BinaryAssociation(
    name="initialOperation650",
    ends={
        Property(name="tool_InitEdgeCreationOperation", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription651", type=tool_InitEdgeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerMappings658: BinaryAssociation = BinaryAssociation(
    name="containerMappings658",
    ends={
        Property(name="description_ContainerMapping659", type=viewpoint_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerCreationDescription", type=description_ContainerMapping, multiplicity=Multiplicity(1, 9999))
    }
)
variable660: BinaryAssociation = BinaryAssociation(
    name="variable660",
    ends={
        Property(name="tool_NodeCreationVariable662", type=viewpoint_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerCreationDescription661", type=tool_NodeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewVariable663: BinaryAssociation = BinaryAssociation(
    name="viewVariable663",
    ends={
        Property(name="tool_ContainerViewVariable665", type=viewpoint_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerCreationDescription664", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation666: BinaryAssociation = BinaryAssociation(
    name="initialOperation666",
    ends={
        Property(name="tool_InitialNodeCreationOperation668", type=viewpoint_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerCreationDescription667", type=tool_InitialNodeCreationOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraMappings669: BinaryAssociation = BinaryAssociation(
    name="extraMappings669",
    ends={
        Property(name="description_AbstractNodeMapping671", type=viewpoint_tool_ContainerCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ContainerCreationDescription670", type=description_AbstractNodeMapping, multiplicity=Multiplicity(0, 9999))
    }
)
element672: BinaryAssociation = BinaryAssociation(
    name="element672",
    ends={
        Property(name="tool_ElementDeleteVariable", type=viewpoint_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteElementDescription", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extraSourceMappings652: BinaryAssociation = BinaryAssociation(
    name="extraSourceMappings652",
    ends={
        Property(name="description_DiagramElementMapping654", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription653", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
extraTargetMappings655: BinaryAssociation = BinaryAssociation(
    name="extraTargetMappings655",
    ends={
        Property(name="description_DiagramElementMapping657", type=viewpoint_tool_EdgeCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_EdgeCreationDescription656", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
initialOperation679: BinaryAssociation = BinaryAssociation(
    name="initialOperation679",
    ends={
        Property(name="tool_InitialOperation681", type=viewpoint_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteElementDescription680", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hook682: BinaryAssociation = BinaryAssociation(
    name="hook682",
    ends={
        Property(name="tool_DeleteHook", type=viewpoint_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteElementDescription683", type=tool_DeleteHook, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappings684: BinaryAssociation = BinaryAssociation(
    name="mappings684",
    ends={
        Property(name="diagram686", type=viewpoint_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="description685", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 9999))
    }
)
element687: BinaryAssociation = BinaryAssociation(
    name="element687",
    ends={
        Property(name="tool_ElementDoubleClickVariable", type=viewpoint_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DoubleClickDescription", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementView688: BinaryAssociation = BinaryAssociation(
    name="elementView688",
    ends={
        Property(name="tool_ElementDoubleClickVariable690", type=viewpoint_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DoubleClickDescription689", type=tool_ElementDoubleClickVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialOperation691: BinaryAssociation = BinaryAssociation(
    name="initialOperation691",
    ends={
        Property(name="tool_InitialOperation693", type=viewpoint_tool_DoubleClickDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DoubleClickDescription692", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters694: BinaryAssociation = BinaryAssociation(
    name="parameters694",
    ends={
        Property(name="tool_DeleteHookParameter", type=viewpoint_tool_DeleteHook, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteHook", type=tool_DeleteHookParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementView673: BinaryAssociation = BinaryAssociation(
    name="elementView673",
    ends={
        Property(name="tool_ElementDeleteVariable675", type=viewpoint_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteElementDescription674", type=tool_ElementDeleteVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containerView676: BinaryAssociation = BinaryAssociation(
    name="containerView676",
    ends={
        Property(name="tool_ContainerViewVariable678", type=viewpoint_tool_DeleteElementDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DeleteElementDescription677", type=tool_ContainerViewVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target697: BinaryAssociation = BinaryAssociation(
    name="target697",
    ends={
        Property(name="tool_TargetEdgeCreationVariable699", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription698", type=tool_TargetEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceView700: BinaryAssociation = BinaryAssociation(
    name="sourceView700",
    ends={
        Property(name="tool_SourceEdgeViewCreationVariable702", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription701", type=tool_SourceEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetView703: BinaryAssociation = BinaryAssociation(
    name="targetView703",
    ends={
        Property(name="tool_TargetEdgeViewCreationVariable705", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription704", type=tool_TargetEdgeViewCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element706: BinaryAssociation = BinaryAssociation(
    name="element706",
    ends={
        Property(name="tool_ElementSelectVariable708", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription707", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation709: BinaryAssociation = BinaryAssociation(
    name="initialOperation709",
    ends={
        Property(name="tool_InitialOperation711", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription710", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edgeView712: BinaryAssociation = BinaryAssociation(
    name="edgeView712",
    ends={
        Property(name="tool_ElementSelectVariable714", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription713", type=tool_ElementSelectVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mask715: BinaryAssociation = BinaryAssociation(
    name="mask715",
    ends={
        Property(name="tool_EditMaskVariables", type=viewpoint_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DirectEditLabel", type=tool_EditMaskVariables, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation716: BinaryAssociation = BinaryAssociation(
    name="initialOperation716",
    ends={
        Property(name="tool_InitialOperation718", type=viewpoint_tool_DirectEditLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DirectEditLabel717", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source695: BinaryAssociation = BinaryAssociation(
    name="source695",
    ends={
        Property(name="tool_SourceEdgeCreationVariable696", type=viewpoint_tool_ReconnectEdgeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_ReconnectEdgeDescription", type=tool_SourceEdgeCreationVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialOperation719: BinaryAssociation = BinaryAssociation(
    name="initialOperation719",
    ends={
        Property(name="tool_InitialOperation720", type=viewpoint_tool_BehaviorTool, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_BehaviorTool", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapping721: BinaryAssociation = BinaryAssociation(
    name="mapping721",
    ends={
        Property(name="description_DiagramElementMapping722", type=viewpoint_tool_CreateView, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_CreateView", type=description_DiagramElementMapping, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription723: BinaryAssociation = BinaryAssociation(
    name="diagramDescription723",
    ends={
        Property(name="description_DiagramDescription724", type=viewpoint_tool_Navigation, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_Navigation", type=description_DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription725: BinaryAssociation = BinaryAssociation(
    name="diagramDescription725",
    ends={
        Property(name="description_DiagramDescription726", type=viewpoint_tool_DiagramCreationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DiagramCreationDescription", type=description_DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
diagramDescription727: BinaryAssociation = BinaryAssociation(
    name="diagramDescription727",
    ends={
        Property(name="description_DiagramDescription728", type=viewpoint_tool_DiagramNavigationDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_tool_DiagramNavigationDescription", type=description_DiagramDescription, multiplicity=Multiplicity(1, 1))
    }
)
mappings729: BinaryAssociation = BinaryAssociation(
    name="mappings729",
    ends={
        Property(name="description_DiagramElementMapping730", type=viewpoint_filter_MappingFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_filter_MappingFilter", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
filters731: BinaryAssociation = BinaryAssociation(
    name="filters731",
    ends={
        Property(name="filter_Filter", type=viewpoint_filter_CompositeFilterDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_filter_CompositeFilterDescription", type=filter_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedVariables732: BinaryAssociation = BinaryAssociation(
    name="ownedVariables732",
    ends={
        Property(name="filter_FilterVariable733", type=viewpoint_filter_VariableFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_filter_VariableFilter", type=filter_FilterVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRules734: BinaryAssociation = BinaryAssociation(
    name="ownedRules734",
    ends={
        Property(name="validation_ValidationRule735", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reusedRules736: BinaryAssociation = BinaryAssociation(
    name="reusedRules736",
    ends={
        Property(name="validation_ValidationRule738", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet737", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
allRules739: BinaryAssociation = BinaryAssociation(
    name="allRules739",
    ends={
        Property(name="validation_ValidationRule741", type=viewpoint_validation_ValidationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationSet740", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
audits742: BinaryAssociation = BinaryAssociation(
    name="audits742",
    ends={
        Property(name="validation_RuleAudit", type=viewpoint_validation_ValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationRule", type=validation_RuleAudit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fixes743: BinaryAssociation = BinaryAssociation(
    name="fixes743",
    ends={
        Property(name="validation_ValidationFix", type=viewpoint_validation_ValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationRule744", type=validation_ValidationFix, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targets745: BinaryAssociation = BinaryAssociation(
    name="targets745",
    ends={
        Property(name="description_DiagramElementMapping746", type=viewpoint_validation_ViewValidationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ViewValidationRule", type=description_DiagramElementMapping, multiplicity=Multiplicity(0, 9999))
    }
)
initialOperation747: BinaryAssociation = BinaryAssociation(
    name="initialOperation747",
    ends={
        Property(name="tool_InitialOperation748", type=viewpoint_validation_ValidationFix, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_validation_ValidationFix", type=tool_InitialOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedConcernDescriptions749: BinaryAssociation = BinaryAssociation(
    name="ownedConcernDescriptions749",
    ends={
        Property(name="concern_ConcernDescription750", type=viewpoint_concern_ConcernSet, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_concern_ConcernSet", type=concern_ConcernDescription, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters751: BinaryAssociation = BinaryAssociation(
    name="filters751",
    ends={
        Property(name="filter_FilterDescription752", type=viewpoint_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_concern_ConcernDescription", type=filter_FilterDescription, multiplicity=Multiplicity(0, 9999))
    }
)
rules753: BinaryAssociation = BinaryAssociation(
    name="rules753",
    ends={
        Property(name="validation_ValidationRule755", type=viewpoint_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_concern_ConcernDescription754", type=validation_ValidationRule, multiplicity=Multiplicity(0, 9999))
    }
)
behaviors756: BinaryAssociation = BinaryAssociation(
    name="behaviors756",
    ends={
        Property(name="tool_BehaviorTool758", type=viewpoint_concern_ConcernDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="viewpoint_concern_ConcernDescription757", type=tool_BehaviorTool, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_viewpoint_DRepresentationContainer_DView = Generalization(general=DView, specific=viewpoint_DRepresentationContainer)
gen_viewpoint_DRepresentation_description_DModelElement = Generalization(general=description_DModelElement, specific=viewpoint_DRepresentation)
gen_viewpoint_DRepresentationElement_DLabelled = Generalization(general=DLabelled, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DMappingBased = Generalization(general=DMappingBased, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DStylizable = Generalization(general=DStylizable, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentationElement_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=viewpoint_DRepresentationElement)
gen_viewpoint_DRepresentation_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_DRepresentation)
gen_viewpoint_DRepresentation_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DRepresentation)
gen_viewpoint_DView_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_DView)
gen_viewpoint_DEObjectLink_DNavigationLink = Generalization(general=DNavigationLink, specific=viewpoint_DEObjectLink)
gen_viewpoint_LabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=viewpoint_LabelStyle)
gen_viewpoint_Style_DRefreshable = Generalization(general=DRefreshable, specific=viewpoint_Style)
gen_viewpoint_Style_Customizable = Generalization(general=Customizable, specific=viewpoint_Style)
gen_viewpoint_DSourceFileLink_DNavigationLink = Generalization(general=DNavigationLink, specific=viewpoint_DSourceFileLink)
gen_viewpoint_DFile_DResource = Generalization(general=DResource, specific=viewpoint_DFile)
gen_viewpoint_DProject_DResourceContainer = Generalization(general=DResourceContainer, specific=viewpoint_DProject)
gen_viewpoint_DFolder_DResourceContainer = Generalization(general=DResourceContainer, specific=viewpoint_DFolder)
gen_viewpoint_DModel_DFile = Generalization(general=DFile, specific=viewpoint_DModel)
gen_viewpoint_BasicLabelStyle_Customizable = Generalization(general=Customizable, specific=viewpoint_BasicLabelStyle)
gen_viewpoint_DResourceContainer_DResource = Generalization(general=DResource, specific=viewpoint_DResourceContainer)
gen_viewpoint_description_Group_description_DModelElement = Generalization(general=description_DModelElement, specific=viewpoint_description_Group)
gen_viewpoint_description_Group_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_Group)
gen_viewpoint_description_Viewpoint_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_Component = Generalization(general=description_Component, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_Viewpoint_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_Viewpoint)
gen_viewpoint_description_RepresentationElementMapping_IdentifiedElement = Generalization(general=IdentifiedElement, specific=viewpoint_description_RepresentationElementMapping)
gen_viewpoint_description_RepresentationDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_RepresentationDescription_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_RepresentationDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_RepresentationDescription)
gen_viewpoint_description_RepresentationImportDescription_RepresentationDescription = Generalization(general=RepresentationDescription, specific=viewpoint_description_RepresentationImportDescription)
gen_viewpoint_description_VSMElementCustomization_IVSMElementCustomization = Generalization(general=IVSMElementCustomization, specific=viewpoint_description_VSMElementCustomization)
gen_viewpoint_description_VSMElementCustomizationReuse_IVSMElementCustomization = Generalization(general=IVSMElementCustomization, specific=viewpoint_description_VSMElementCustomizationReuse)
gen_viewpoint_description_EAttributeCustomization_EStructuralFeatureCustomization = Generalization(general=EStructuralFeatureCustomization, specific=viewpoint_description_EAttributeCustomization)
gen_viewpoint_description_SemanticBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=viewpoint_description_SemanticBasedDecoration)
gen_viewpoint_description_SystemColor_FixedColor = Generalization(general=FixedColor, specific=viewpoint_description_SystemColor)
gen_viewpoint_description_InterpolatedColor_description_ColorDescription = Generalization(general=description_ColorDescription, specific=viewpoint_description_InterpolatedColor)
gen_viewpoint_description_InterpolatedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_InterpolatedColor)
gen_viewpoint_description_EReferenceCustomization_EStructuralFeatureCustomization = Generalization(general=EStructuralFeatureCustomization, specific=viewpoint_description_EReferenceCustomization)
gen_viewpoint_description_FixedColor_ColorDescription = Generalization(general=ColorDescription, specific=viewpoint_description_FixedColor)
gen_viewpoint_description_UserFixedColor_description_FixedColor = Generalization(general=description_FixedColor, specific=viewpoint_description_UserFixedColor)
gen_viewpoint_description_UserFixedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_UserFixedColor)
gen_viewpoint_description_ComputedColor_description_UserColor = Generalization(general=description_UserColor, specific=viewpoint_description_ComputedColor)
gen_viewpoint_description_ComputedColor_description_ColorDescription = Generalization(general=description_ColorDescription, specific=viewpoint_description_ComputedColor)
gen_viewpoint_tool_ToolEntry_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_tool_ToolEntry)
gen_viewpoint_tool_ToolEntry_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_tool_ToolEntry)
gen_viewpoint_style_LabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=viewpoint_style_LabelStyleDescription)
gen_viewpoint_tool_ContainerDropDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_ContainerDropDescription)
gen_viewpoint_tool_AbstractToolDescription_ToolEntry = Generalization(general=ToolEntry, specific=viewpoint_tool_AbstractToolDescription)
gen_viewpoint_tool_MappingBasedToolDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_MappingBasedToolDescription)
gen_viewpoint_tool_ToolDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_ToolDescription)
gen_viewpoint_tool_SelectionWizardDescription_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=viewpoint_tool_SelectionWizardDescription)
gen_viewpoint_tool_SelectionWizardDescription_description_SelectionDescription = Generalization(general=description_SelectionDescription, specific=viewpoint_tool_SelectionWizardDescription)
gen_viewpoint_tool_PasteDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_PasteDescription)
gen_viewpoint_tool_PaneBasedSelectionWizardDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_PaneBasedSelectionWizardDescription)
gen_viewpoint_tool_RepresentationNavigationDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_RepresentationNavigationDescription)
gen_viewpoint_tool_RepresentationCreationDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_RepresentationCreationDescription)
gen_viewpoint_tool_ExternalJavaAction_tool_MenuItemDescription = Generalization(general=tool_MenuItemDescription, specific=viewpoint_tool_ExternalJavaAction)
gen_viewpoint_tool_ExternalJavaAction_tool_ContainerModelOperation = Generalization(general=tool_ContainerModelOperation, specific=viewpoint_tool_ExternalJavaAction)
gen_viewpoint_tool_ExternalJavaActionCall_tool_MenuItemDescription = Generalization(general=tool_MenuItemDescription, specific=viewpoint_tool_ExternalJavaActionCall)
gen_viewpoint_tool_ExternalJavaActionCall_tool_ContainerModelOperation = Generalization(general=tool_ContainerModelOperation, specific=viewpoint_tool_ExternalJavaActionCall)
gen_viewpoint_tool_PopupMenu_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_PopupMenu)
gen_viewpoint_tool_MenuItemDescription_tool_AbstractToolDescription = Generalization(general=tool_AbstractToolDescription, specific=viewpoint_tool_MenuItemDescription)
gen_viewpoint_tool_MenuItemDescription_tool_MenuItemOrRef = Generalization(general=tool_MenuItemOrRef, specific=viewpoint_tool_MenuItemDescription)
gen_viewpoint_tool_MenuItemDescriptionReference_MenuItemOrRef = Generalization(general=MenuItemOrRef, specific=viewpoint_tool_MenuItemDescriptionReference)
gen_viewpoint_tool_OperationAction_MenuItemDescription = Generalization(general=MenuItemDescription, specific=viewpoint_tool_OperationAction)
gen_viewpoint_tool_AcceleoVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_AcceleoVariable)
gen_viewpoint_tool_AcceleoVariable_tool_SubVariable = Generalization(general=tool_SubVariable, specific=viewpoint_tool_AcceleoVariable)
gen_viewpoint_tool_SubVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_SubVariable)
gen_viewpoint_tool_DialogVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_DialogVariable)
gen_viewpoint_tool_ElementDropVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementDropVariable)
gen_viewpoint_tool_SelectModelElementVariable_tool_SubVariable = Generalization(general=tool_SubVariable, specific=viewpoint_tool_SelectModelElementVariable)
gen_viewpoint_tool_SelectModelElementVariable_description_SelectionDescription = Generalization(general=description_SelectionDescription, specific=viewpoint_tool_SelectModelElementVariable)
gen_viewpoint_tool_ContainerModelOperation_ModelOperation = Generalization(general=ModelOperation, specific=viewpoint_tool_ContainerModelOperation)
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
gen_viewpoint_tool_CreateInstance_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_CreateInstance)
gen_viewpoint_tool_ChangeContext_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_ChangeContext)
gen_viewpoint_tool_SetObject_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_SetObject)
gen_viewpoint_tool_Unset_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_Unset)
gen_viewpoint_tool_SetValue_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_SetValue)
gen_viewpoint_tool_RemoveElement_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_RemoveElement)
gen_viewpoint_tool_For_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_For)
gen_viewpoint_tool_MoveElement_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_MoveElement)
gen_viewpoint_tool_If_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_If)
gen_viewpoint_tool_DeleteView_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_DeleteView)
gen_viewpoint_tool_NameVariable_AbstractVariable = Generalization(general=AbstractVariable, specific=viewpoint_tool_NameVariable)
gen_viewpoint_tool_Default_SwitchChild = Generalization(general=SwitchChild, specific=viewpoint_tool_Default)
gen_viewpoint_tool_Switch_ModelOperation = Generalization(general=ModelOperation, specific=viewpoint_tool_Switch)
gen_viewpoint_tool_Case_SwitchChild = Generalization(general=SwitchChild, specific=viewpoint_tool_Case)
gen_viewpoint_audit_TemplateInformationSection_InformationSection = Generalization(general=InformationSection, specific=viewpoint_audit_TemplateInformationSection)
gen_viewpoint_diagram_DDiagram_DRepresentation = Generalization(general=DRepresentation, specific=viewpoint_diagram_DDiagram)
gen_viewpoint_diagram_DDiagram_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_diagram_DDiagram)
gen_viewpoint_diagram_DDiagram_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=viewpoint_diagram_DDiagram)
gen_viewpoint_diagram_DDiagram_DValidable = Generalization(general=DValidable, specific=viewpoint_diagram_DDiagram)
gen_viewpoint_diagram_DDiagram_DContainer = Generalization(general=DContainer, specific=viewpoint_diagram_DDiagram)
gen_viewpoint_diagram_DDiagramElement_DRepresentationElement = Generalization(general=DRepresentationElement, specific=viewpoint_diagram_DDiagramElement)
gen_viewpoint_diagram_DDiagramElement_DValidable = Generalization(general=DValidable, specific=viewpoint_diagram_DDiagramElement)
gen_viewpoint_diagram_DDiagramElement_DNavigable = Generalization(general=DNavigable, specific=viewpoint_diagram_DDiagramElement)
gen_viewpoint_diagram_DSemanticDiagram_diagram_DDiagram = Generalization(general=diagram_DDiagram, specific=viewpoint_diagram_DSemanticDiagram)
gen_viewpoint_diagram_DSemanticDiagram_DSemanticDecorator = Generalization(general=DSemanticDecorator, specific=viewpoint_diagram_DSemanticDiagram)
gen_viewpoint_diagram_HideFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_HideFilter)
gen_viewpoint_diagram_HideLabelFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_HideLabelFilter)
gen_viewpoint_diagram_FoldingPointFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_FoldingPointFilter)
gen_viewpoint_diagram_DDiagramLink_DNavigationLink = Generalization(general=DNavigationLink, specific=viewpoint_diagram_DDiagramLink)
gen_viewpoint_diagram_AbstractDNode_DDiagramElement = Generalization(general=DDiagramElement, specific=viewpoint_diagram_AbstractDNode)
gen_viewpoint_diagram_FoldingFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_FoldingFilter)
gen_viewpoint_diagram_AppliedCompositeFilters_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_AppliedCompositeFilters)
gen_viewpoint_diagram_AbsoluteBoundsFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_AbsoluteBoundsFilter)
gen_viewpoint_diagram_DNode_diagram_AbstractDNode = Generalization(general=diagram_AbstractDNode, specific=viewpoint_diagram_DNode)
gen_viewpoint_diagram_DNode_diagram_EdgeTarget = Generalization(general=diagram_EdgeTarget, specific=viewpoint_diagram_DNode)
gen_viewpoint_diagram_DNode_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=viewpoint_diagram_DNode)
gen_viewpoint_diagram_DDiagramElementContainer_diagram_AbstractDNode = Generalization(general=diagram_AbstractDNode, specific=viewpoint_diagram_DDiagramElementContainer)
gen_viewpoint_diagram_DDiagramElementContainer_diagram_EdgeTarget = Generalization(general=diagram_EdgeTarget, specific=viewpoint_diagram_DDiagramElementContainer)
gen_viewpoint_diagram_DDiagramElementContainer_DragAndDropTarget = Generalization(general=DragAndDropTarget, specific=viewpoint_diagram_DDiagramElementContainer)
gen_viewpoint_diagram_DDiagramElementContainer_DContainer = Generalization(general=DContainer, specific=viewpoint_diagram_DDiagramElementContainer)
gen_viewpoint_diagram_DNodeContainer_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=viewpoint_diagram_DNodeContainer)
gen_viewpoint_diagram_DNodeList_DDiagramElementContainer = Generalization(general=DDiagramElementContainer, specific=viewpoint_diagram_DNodeList)
gen_viewpoint_diagram_DNodeListElement_AbstractDNode = Generalization(general=AbstractDNode, specific=viewpoint_diagram_DNodeListElement)
gen_viewpoint_diagram_DEdge_diagram_DDiagramElement = Generalization(general=diagram_DDiagramElement, specific=viewpoint_diagram_DEdge)
gen_viewpoint_diagram_DEdge_diagram_EdgeTarget = Generalization(general=diagram_EdgeTarget, specific=viewpoint_diagram_DEdge)
gen_viewpoint_diagram_Dot_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_Dot)
gen_viewpoint_diagram_NodeStyle_LabelStyle = Generalization(general=LabelStyle, specific=viewpoint_diagram_NodeStyle)
gen_viewpoint_diagram_NodeStyle_Style = Generalization(general=Style, specific=viewpoint_diagram_NodeStyle)
gen_viewpoint_diagram_NodeStyle_diagram_BorderedStyle = Generalization(general=diagram_BorderedStyle, specific=viewpoint_diagram_NodeStyle)
gen_viewpoint_diagram_ContainerStyle_LabelStyle = Generalization(general=LabelStyle, specific=viewpoint_diagram_ContainerStyle)
gen_viewpoint_diagram_ContainerStyle_Style = Generalization(general=Style, specific=viewpoint_diagram_ContainerStyle)
gen_viewpoint_diagram_ContainerStyle_diagram_BorderedStyle = Generalization(general=diagram_BorderedStyle, specific=viewpoint_diagram_ContainerStyle)
gen_viewpoint_diagram_FlatContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=viewpoint_diagram_FlatContainerStyle)
gen_viewpoint_diagram_GaugeSection_Customizable = Generalization(general=Customizable, specific=viewpoint_diagram_GaugeSection)
gen_viewpoint_diagram_Square_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_Square)
gen_viewpoint_diagram_ShapeContainerStyle_ContainerStyle = Generalization(general=ContainerStyle, specific=viewpoint_diagram_ShapeContainerStyle)
gen_viewpoint_diagram_Lozenge_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_Lozenge)
gen_viewpoint_diagram_Ellipse_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_Ellipse)
gen_viewpoint_diagram_WorkspaceImage_diagram_NodeStyle = Generalization(general=diagram_NodeStyle, specific=viewpoint_diagram_WorkspaceImage)
gen_viewpoint_diagram_WorkspaceImage_diagram_ContainerStyle = Generalization(general=diagram_ContainerStyle, specific=viewpoint_diagram_WorkspaceImage)
gen_viewpoint_diagram_CustomStyle_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_CustomStyle)
gen_viewpoint_diagram_BundledImage_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_BundledImage)
gen_viewpoint_diagram_EdgeStyle_Style = Generalization(general=Style, specific=viewpoint_diagram_EdgeStyle)
gen_viewpoint_diagram_GaugeCompositeStyle_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_GaugeCompositeStyle)
gen_viewpoint_diagram_Note_NodeStyle = Generalization(general=NodeStyle, specific=viewpoint_diagram_Note)
gen_viewpoint_diagram_BorderedStyle_Style = Generalization(general=Style, specific=viewpoint_diagram_BorderedStyle)
gen_viewpoint_diagram_CollapseFilter_GraphicalFilter = Generalization(general=GraphicalFilter, specific=viewpoint_diagram_CollapseFilter)
gen_viewpoint_diagram_IndirectlyCollapseFilter_CollapseFilter = Generalization(general=CollapseFilter, specific=viewpoint_diagram_IndirectlyCollapseFilter)
gen_viewpoint_diagram_BeginLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=viewpoint_diagram_BeginLabelStyle)
gen_viewpoint_diagram_EndLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=viewpoint_diagram_EndLabelStyle)
gen_viewpoint_diagram_CenterLabelStyle_BasicLabelStyle = Generalization(general=BasicLabelStyle, specific=viewpoint_diagram_CenterLabelStyle)
gen_viewpoint_diagram_BracketEdgeStyle_EdgeStyle = Generalization(general=EdgeStyle, specific=viewpoint_diagram_BracketEdgeStyle)
gen_viewpoint_description_DiagramDescription_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=viewpoint_description_DiagramDescription)
gen_viewpoint_description_DiagramDescription_description_RepresentationDescription = Generalization(general=description_RepresentationDescription, specific=viewpoint_description_DiagramDescription)
gen_viewpoint_description_DiagramDescription_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=viewpoint_description_DiagramDescription)
gen_viewpoint_description_DiagramImportDescription_description_RepresentationImportDescription = Generalization(general=description_RepresentationImportDescription, specific=viewpoint_description_DiagramImportDescription)
gen_viewpoint_description_DiagramImportDescription_description_DiagramDescription = Generalization(general=description_DiagramDescription, specific=viewpoint_description_DiagramImportDescription)
gen_viewpoint_description_DiagramExtensionDescription_RepresentationExtensionDescription = Generalization(general=RepresentationExtensionDescription, specific=viewpoint_description_DiagramExtensionDescription)
gen_viewpoint_description_DiagramElementMapping_description_RepresentationElementMapping = Generalization(general=description_RepresentationElementMapping, specific=viewpoint_description_DiagramElementMapping)
gen_viewpoint_description_DiagramElementMapping_description_PasteTargetDescription = Generalization(general=description_PasteTargetDescription, specific=viewpoint_description_DiagramElementMapping)
gen_viewpoint_description_AbstractNodeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=viewpoint_description_AbstractNodeMapping)
gen_viewpoint_description_AbstractNodeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_AbstractNodeMapping)
gen_viewpoint_description_NodeMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=viewpoint_description_NodeMapping)
gen_viewpoint_description_NodeMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=viewpoint_description_NodeMapping)
gen_viewpoint_description_ContainerMapping_description_AbstractNodeMapping = Generalization(general=description_AbstractNodeMapping, specific=viewpoint_description_ContainerMapping)
gen_viewpoint_description_ContainerMapping_description_DragAndDropTargetDescription = Generalization(general=description_DragAndDropTargetDescription, specific=viewpoint_description_ContainerMapping)
gen_viewpoint_description_NodeMappingImport_description_NodeMapping = Generalization(general=description_NodeMapping, specific=viewpoint_description_NodeMappingImport)
gen_viewpoint_description_NodeMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=viewpoint_description_NodeMappingImport)
gen_viewpoint_description_ContainerMappingImport_description_ContainerMapping = Generalization(general=description_ContainerMapping, specific=viewpoint_description_ContainerMappingImport)
gen_viewpoint_description_ContainerMappingImport_description_AbstractMappingImport = Generalization(general=description_AbstractMappingImport, specific=viewpoint_description_ContainerMappingImport)
gen_viewpoint_description_EdgeMapping_description_DiagramElementMapping = Generalization(general=description_DiagramElementMapping, specific=viewpoint_description_EdgeMapping)
gen_viewpoint_description_EdgeMapping_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_EdgeMapping)
gen_viewpoint_description_EdgeMapping_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=viewpoint_description_EdgeMapping)
gen_viewpoint_description_ConditionalNodeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=viewpoint_description_ConditionalNodeStyleDescription)
gen_viewpoint_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=viewpoint_description_ConditionalEdgeStyleDescription)
gen_viewpoint_description_EdgeMappingImport_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_EdgeMappingImport)
gen_viewpoint_description_EdgeMappingImport_description_IEdgeMapping = Generalization(general=description_IEdgeMapping, specific=viewpoint_description_EdgeMappingImport)
gen_viewpoint_description_EdgeMappingImport_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_EdgeMappingImport)
gen_viewpoint_description_ConditionalContainerStyleDescription_ConditionalStyleDescription = Generalization(general=ConditionalStyleDescription, specific=viewpoint_description_ConditionalContainerStyleDescription)
gen_viewpoint_description_Layout_DocumentedElement = Generalization(general=DocumentedElement, specific=viewpoint_description_Layout)
gen_viewpoint_description_OrderedTreeLayout_Layout = Generalization(general=Layout, specific=viewpoint_description_OrderedTreeLayout)
gen_viewpoint_description_CompositeLayout_Layout = Generalization(general=Layout, specific=viewpoint_description_CompositeLayout)
gen_viewpoint_description_MappingBasedDecoration_DecorationDescription = Generalization(general=DecorationDescription, specific=viewpoint_description_MappingBasedDecoration)
gen_viewpoint_description_Layer_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_description_Layer)
gen_viewpoint_description_Layer_description_EndUserDocumentedElement = Generalization(general=description_EndUserDocumentedElement, specific=viewpoint_description_Layer)
gen_viewpoint_description_Layer_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_description_Layer)
gen_viewpoint_style_BorderedStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=viewpoint_style_BorderedStyleDescription)
gen_viewpoint_description_AdditionalLayer_Layer = Generalization(general=Layer, specific=viewpoint_description_AdditionalLayer)
gen_viewpoint_style_NodeStyleDescription_style_StyleDescription = Generalization(general=style_StyleDescription, specific=viewpoint_style_NodeStyleDescription)
gen_viewpoint_style_NodeStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=viewpoint_style_NodeStyleDescription)
gen_viewpoint_style_NodeStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=viewpoint_style_NodeStyleDescription)
gen_viewpoint_style_NodeStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=viewpoint_style_NodeStyleDescription)
gen_viewpoint_style_CustomStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_CustomStyleDescription)
gen_viewpoint_style_SquareDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_SquareDescription)
gen_viewpoint_style_LozengeNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_LozengeNodeDescription)
gen_viewpoint_style_EllipseNodeDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_EllipseNodeDescription)
gen_viewpoint_style_BundledImageDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_BundledImageDescription)
gen_viewpoint_style_NoteDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_NoteDescription)
gen_viewpoint_style_RoundedCornerStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=viewpoint_style_RoundedCornerStyleDescription)
gen_viewpoint_style_DotDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_DotDescription)
gen_viewpoint_style_GaugeCompositeStyleDescription_NodeStyleDescription = Generalization(general=NodeStyleDescription, specific=viewpoint_style_GaugeCompositeStyleDescription)
gen_viewpoint_style_ContainerStyleDescription_style_RoundedCornerStyleDescription = Generalization(general=style_RoundedCornerStyleDescription, specific=viewpoint_style_ContainerStyleDescription)
gen_viewpoint_style_ContainerStyleDescription_style_BorderedStyleDescription = Generalization(general=style_BorderedStyleDescription, specific=viewpoint_style_ContainerStyleDescription)
gen_viewpoint_style_ContainerStyleDescription_style_LabelStyleDescription = Generalization(general=style_LabelStyleDescription, specific=viewpoint_style_ContainerStyleDescription)
gen_viewpoint_style_ContainerStyleDescription_style_TooltipStyleDescription = Generalization(general=style_TooltipStyleDescription, specific=viewpoint_style_ContainerStyleDescription)
gen_viewpoint_style_FlatContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=viewpoint_style_FlatContainerStyleDescription)
gen_viewpoint_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=viewpoint_style_FlatContainerStyleDescription)
gen_viewpoint_style_ShapeContainerStyleDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=viewpoint_style_ShapeContainerStyleDescription)
gen_viewpoint_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription = Generalization(general=style_SizeComputationContainerStyleDescription, specific=viewpoint_style_ShapeContainerStyleDescription)
gen_viewpoint_style_WorkspaceImageDescription_style_NodeStyleDescription = Generalization(general=style_NodeStyleDescription, specific=viewpoint_style_WorkspaceImageDescription)
gen_viewpoint_style_WorkspaceImageDescription_style_ContainerStyleDescription = Generalization(general=style_ContainerStyleDescription, specific=viewpoint_style_WorkspaceImageDescription)
gen_viewpoint_style_EdgeStyleDescription_StyleDescription = Generalization(general=StyleDescription, specific=viewpoint_style_EdgeStyleDescription)
gen_viewpoint_style_BeginLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=viewpoint_style_BeginLabelStyleDescription)
gen_viewpoint_style_CenterLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=viewpoint_style_CenterLabelStyleDescription)
gen_viewpoint_style_EndLabelStyleDescription_BasicLabelStyleDescription = Generalization(general=BasicLabelStyleDescription, specific=viewpoint_style_EndLabelStyleDescription)
gen_viewpoint_style_BracketEdgeStyleDescription_EdgeStyleDescription = Generalization(general=EdgeStyleDescription, specific=viewpoint_style_BracketEdgeStyleDescription)
gen_viewpoint_tool_ToolSection_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_tool_ToolSection)
gen_viewpoint_tool_ToolSection_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_tool_ToolSection)
gen_viewpoint_tool_ToolGroup_ToolEntry = Generalization(general=ToolEntry, specific=viewpoint_tool_ToolGroup)
gen_viewpoint_tool_NodeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_NodeCreationDescription)
gen_viewpoint_tool_EdgeCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_EdgeCreationDescription)
gen_viewpoint_tool_ContainerCreationDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_ContainerCreationDescription)
gen_viewpoint_tool_DeleteElementDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_DeleteElementDescription)
gen_viewpoint_tool_DoubleClickDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_DoubleClickDescription)
gen_viewpoint_tool_ReconnectEdgeDescription_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_ReconnectEdgeDescription)
gen_viewpoint_tool_RequestDescription_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_RequestDescription)
gen_viewpoint_tool_DirectEditLabel_MappingBasedToolDescription = Generalization(general=MappingBasedToolDescription, specific=viewpoint_tool_DirectEditLabel)
gen_viewpoint_tool_BehaviorTool_AbstractToolDescription = Generalization(general=AbstractToolDescription, specific=viewpoint_tool_BehaviorTool)
gen_viewpoint_tool_SourceEdgeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_SourceEdgeCreationVariable)
gen_viewpoint_tool_SourceEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_SourceEdgeCreationVariable)
gen_viewpoint_tool_SourceEdgeViewCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_SourceEdgeViewCreationVariable)
gen_viewpoint_tool_SourceEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_SourceEdgeViewCreationVariable)
gen_viewpoint_tool_TargetEdgeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_TargetEdgeCreationVariable)
gen_viewpoint_tool_TargetEdgeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_TargetEdgeCreationVariable)
gen_viewpoint_tool_TargetEdgeViewCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_TargetEdgeViewCreationVariable)
gen_viewpoint_tool_TargetEdgeViewCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_TargetEdgeViewCreationVariable)
gen_viewpoint_tool_ElementDoubleClickVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_ElementDoubleClickVariable)
gen_viewpoint_tool_ElementDoubleClickVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_ElementDoubleClickVariable)
gen_viewpoint_tool_NodeCreationVariable_tool_AbstractVariable = Generalization(general=tool_AbstractVariable, specific=viewpoint_tool_NodeCreationVariable)
gen_viewpoint_tool_NodeCreationVariable_tool_VariableContainer = Generalization(general=tool_VariableContainer, specific=viewpoint_tool_NodeCreationVariable)
gen_viewpoint_tool_CreateView_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_CreateView)
gen_viewpoint_tool_CreateEdgeView_CreateView = Generalization(general=CreateView, specific=viewpoint_tool_CreateEdgeView)
gen_viewpoint_tool_DiagramCreationDescription_RepresentationCreationDescription = Generalization(general=RepresentationCreationDescription, specific=viewpoint_tool_DiagramCreationDescription)
gen_viewpoint_tool_DiagramNavigationDescription_RepresentationNavigationDescription = Generalization(general=RepresentationNavigationDescription, specific=viewpoint_tool_DiagramNavigationDescription)
gen_viewpoint_filter_FilterDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_filter_FilterDescription)
gen_viewpoint_filter_FilterDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_filter_FilterDescription)
gen_viewpoint_filter_MappingFilter_Filter = Generalization(general=Filter, specific=viewpoint_filter_MappingFilter)
gen_viewpoint_tool_Navigation_ContainerModelOperation = Generalization(general=ContainerModelOperation, specific=viewpoint_tool_Navigation)
gen_viewpoint_filter_VariableFilter_Filter = Generalization(general=Filter, specific=viewpoint_filter_VariableFilter)
gen_viewpoint_filter_FilterVariable_SelectionDescription = Generalization(general=SelectionDescription, specific=viewpoint_filter_FilterVariable)
gen_viewpoint_validation_ValidationSet_DocumentedElement = Generalization(general=DocumentedElement, specific=viewpoint_validation_ValidationSet)
gen_viewpoint_filter_CompositeFilterDescription_FilterDescription = Generalization(general=FilterDescription, specific=viewpoint_filter_CompositeFilterDescription)
gen_viewpoint_validation_SemanticValidationRule_ValidationRule = Generalization(general=ValidationRule, specific=viewpoint_validation_SemanticValidationRule)
gen_viewpoint_validation_ViewValidationRule_ValidationRule = Generalization(general=ValidationRule, specific=viewpoint_validation_ViewValidationRule)
gen_viewpoint_concern_ConcernSet_DocumentedElement = Generalization(general=DocumentedElement, specific=viewpoint_concern_ConcernSet)
gen_viewpoint_concern_ConcernDescription_description_DocumentedElement = Generalization(general=description_DocumentedElement, specific=viewpoint_concern_ConcernDescription)
gen_viewpoint_concern_ConcernDescription_description_IdentifiedElement = Generalization(general=description_IdentifiedElement, specific=viewpoint_concern_ConcernDescription)

# Domain Model
domain_model = DomainModel(
    name="viewpoint",
    types={viewpoint_DAnalysis, viewpoint_EObject, FeatureExtensionDescription, viewpoint_DValidable, viewpoint_DNavigable, viewpoint_DNavigationLink, viewpoint_DStylizable, viewpoint_DRefreshable, viewpoint_DLabelled, viewpoint_DMappingBased, viewpoint_DContainer, viewpoint_DRepresentationContainer, DView, DAnnotationEntry, viewpoint_DView, viewpoint_DFeatureExtension, description_DModelElement, viewpoint_DRepresentationElement, AnnotationEntry, DLabelled, DMappingBased, DStylizable, DSemanticDecorator, DDiagramSet, viewpoint_DSemanticDecorator, viewpoint_DRepresentation, description_DocumentedElement, DRefreshable, viewpoint_MetaModelExtension, viewpoint_Decoration, DecorationDescription, viewpoint_DEObjectLink, DNavigationLink, Viewpoint, viewpoint_DAnalysisCustomData, viewpoint_LabelStyle, BasicLabelStyle, viewpoint_Style, Customizable, style_StyleDescription, viewpoint_DragAndDropTarget, viewpoint_DSourceFileLink, viewpoint_SessionManagerEObject, viewpoint_DResource, viewpoint_DFile, DResource, viewpoint_RGBValues, viewpoint_DAnalysisSessionEObject, viewpoint_DProject, DResourceContainer, viewpoint_DFolder, viewpoint_DModel, DFile, viewpoint_BasicLabelStyle, viewpoint_DResourceContainer, viewpoint_Customizable, viewpoint_description_Group, validation_ValidationSet, RepresentationDescription, RepresentationExtensionDescription, JavaExtension, MetamodelExtensionSetting, SytemColorsPalette, UserColorsPalette, viewpoint_description_Component, viewpoint_description_Viewpoint, description_Component, description_EndUserDocumentedElement, description_IdentifiedElement, viewpoint_description_MetamodelExtensionSetting, description_viewpoint_EObject, viewpoint_description_JavaExtension, viewpoint_description_RepresentationElementMapping, IdentifiedElement, tool_RepresentationCreationDescription, tool_RepresentationNavigationDescription, RepresentationTemplate, viewpoint_description_FeatureExtensionDescription, viewpoint_description_RepresentationDescription, description_viewpoint_EPackage, viewpoint_description_RepresentationTemplate, viewpoint_description_RepresentationImportDescription, viewpoint_description_RepresentationExtensionDescription, viewpoint_description_DragAndDropTargetDescription, tool_ContainerDropDescription, viewpoint_description_PasteTargetDescription, tool_PasteDescription, viewpoint_description_DecorationDescriptionsSet, viewpoint_description_DecorationDescription, viewpoint_description_AbstractMappingImport, viewpoint_description_DocumentedElement, viewpoint_description_DModelElement, DAnnotation, viewpoint_description_DAnnotation, description_viewpoint_EStringToStringMapEntry, viewpoint_description_ConditionalStyleDescription, viewpoint_description_VSMElementCustomization, EStructuralFeatureCustomization, viewpoint_description_VSMElementCustomizationReuse, viewpoint_description_EStructuralFeatureCustomization, viewpoint_description_EAttributeCustomization, viewpoint_description_SemanticBasedDecoration, viewpoint_description_Customization, IVSMElementCustomization, viewpoint_description_IVSMElementCustomization, viewpoint_description_ColorDescription, viewpoint_description_SystemColor, FixedColor, viewpoint_description_InterpolatedColor, description_ColorDescription, description_UserColor, viewpoint_description_EReferenceCustomization, viewpoint_description_SelectionDescription, ColorStep, viewpoint_description_ColorStep, viewpoint_description_FixedColor, ColorDescription, viewpoint_description_UserFixedColor, description_FixedColor, viewpoint_description_UserColor, viewpoint_description_ComputedColor, viewpoint_description_DAnnotationEntry, viewpoint_description_Environment, tool_ToolEntry, style_LabelBorderStyles, viewpoint_description_SytemColorsPalette, SystemColor, viewpoint_description_UserColorsPalette, UserColor, viewpoint_description_AnnotationEntry, viewpoint_description_EndUserDocumentedElement, viewpoint_description_IdentifiedElement, viewpoint_style_LabelBorderStyles, style_LabelBorderStyleDescription, viewpoint_style_LabelBorderStyleDescription, viewpoint_style_TooltipStyleDescription, viewpoint_tool_ToolEntry, viewpoint_tool_AbstractToolDescription, ToolEntry, viewpoint_style_StyleDescription, viewpoint_style_BasicLabelStyleDescription, viewpoint_style_LabelStyleDescription, BasicLabelStyleDescription, tool_InitialOperation, viewpoint_tool_ContainerDropDescription, description_DiagramElementMapping, tool_DropContainerVariable, tool_ToolFilterDescription, viewpoint_tool_MappingBasedToolDescription, AbstractToolDescription, viewpoint_tool_ToolDescription, MappingBasedToolDescription, tool_ElementVariable, tool_ElementViewVariable, viewpoint_tool_SelectionWizardDescription, tool_AbstractToolDescription, description_SelectionDescription, tool_ElementSelectVariable, tool_ElementDropVariable, tool_ContainerViewVariable, tool_InitialContainerDropOperation, viewpoint_tool_PasteDescription, tool_SelectContainerVariable, viewpoint_tool_PaneBasedSelectionWizardDescription, tool_NameVariable, viewpoint_tool_RepresentationNavigationDescription, viewpoint_tool_RepresentationCreationDescription, viewpoint_tool_ExternalJavaAction, tool_ContainerModelOperation, tool_ExternalJavaActionParameter, viewpoint_tool_ExternalJavaActionCall, tool_ExternalJavaAction, viewpoint_tool_PopupMenu, viewpoint_tool_MenuItemOrRef, viewpoint_tool_MenuItemDescription, tool_MenuItemOrRef, viewpoint_tool_MenuItemDescriptionReference, MenuItemOrRef, tool_MenuItemDescription, viewpoint_tool_OperationAction, MenuItemDescription, viewpoint_tool_AcceleoVariable, tool_VariableContainer, viewpoint_tool_SubVariable, AbstractVariable, viewpoint_tool_DialogVariable, viewpoint_tool_ElementDropVariable, tool_AbstractVariable, viewpoint_tool_AbstractVariable, viewpoint_tool_VariableContainer, tool_SubVariable, viewpoint_tool_SelectModelElementVariable, viewpoint_tool_EditMaskVariables, viewpoint_tool_ContainerModelOperation, ModelOperation, tool_ModelOperation, viewpoint_tool_ModelOperation, viewpoint_tool_InitialNodeCreationOperation, viewpoint_tool_ElementSelectVariable, viewpoint_tool_ElementVariable, viewpoint_tool_ElementViewVariable, viewpoint_tool_ElementDeleteVariable, viewpoint_tool_DropContainerVariable, viewpoint_tool_SelectContainerVariable, viewpoint_tool_ContainerViewVariable, viewpoint_tool_CreateInstance, ContainerModelOperation, viewpoint_tool_ChangeContext, viewpoint_tool_InitialOperation, viewpoint_tool_InitEdgeCreationOperation, viewpoint_tool_InitialContainerDropOperation, viewpoint_tool_SetObject, tool_viewpoint_EObject, viewpoint_tool_Unset, viewpoint_tool_SetValue, viewpoint_tool_RemoveElement, viewpoint_tool_For, viewpoint_tool_MoveElement, viewpoint_tool_ToolFilterDescription, viewpoint_tool_If, viewpoint_tool_DeleteView, viewpoint_tool_NameVariable, viewpoint_tool_ExternalJavaActionParameter, viewpoint_tool_SwitchChild, viewpoint_tool_Default, viewpoint_tool_Switch, tool_Case, tool_FeatureChangeListener, viewpoint_tool_FeatureChangeListener, viewpoint_tool_Case, SwitchChild, viewpoint_audit_TemplateInformationSection, InformationSection, viewpoint_diagram_DDiagram, DRepresentation, DragAndDropTarget, DValidable, DContainer, tool_Default, viewpoint_audit_InformationSection, DDiagramElement, description_DiagramDescription, DNode, DNodeListElement, DDiagramElementContainer, DDiagram, DEdge, validation_ValidationRule, tool_BehaviorTool, FilterVariableHistory, description_Layer, concern_ConcernDescription, filter_FilterDescription, viewpoint_diagram_DDiagramElement, DRepresentationElement, DNavigable, viewpoint_diagram_DSemanticDiagram, diagram_DDiagram, GraphicalFilter, viewpoint_diagram_GraphicalFilter, viewpoint_diagram_HideFilter, viewpoint_diagram_HideLabelFilter, viewpoint_diagram_FoldingPointFilter, viewpoint_diagram_FoldingFilter, diagram_viewpoint_Decoration, viewpoint_diagram_DDiagramLink, EdgeTarget, viewpoint_diagram_AbstractDNode, viewpoint_diagram_AppliedCompositeFilters, filter_CompositeFilterDescription, viewpoint_diagram_AbsoluteBoundsFilter, NodeStyle, viewpoint_diagram_DNode, diagram_AbstractDNode, diagram_EdgeTarget, viewpoint_diagram_DDiagramElementContainer, diagram_viewpoint_Style, description_NodeMapping, ContainerStyle, viewpoint_diagram_DNodeContainer, viewpoint_diagram_DNodeList, description_ContainerMapping, viewpoint_diagram_DNodeListElement, AbstractDNode, description_IEdgeMapping, viewpoint_diagram_DEdge, diagram_DDiagramElement, EdgeStyle, viewpoint_diagram_DDiagramSet, viewpoint_diagram_Dot, diagram_viewpoint_RGBValues, diagram_viewpoint_DRepresentationContainer, viewpoint_diagram_NodeStyle, LabelStyle, Style, diagram_BorderedStyle, viewpoint_diagram_ContainerStyle, viewpoint_diagram_FlatContainerStyle, viewpoint_diagram_GaugeSection, viewpoint_diagram_Square, viewpoint_diagram_ShapeContainerStyle, viewpoint_diagram_Lozenge, viewpoint_diagram_Ellipse, viewpoint_diagram_WorkspaceImage, diagram_NodeStyle, diagram_ContainerStyle, viewpoint_diagram_CustomStyle, viewpoint_diagram_BundledImage, viewpoint_diagram_EdgeTarget, viewpoint_diagram_EdgeStyle, BeginLabelStyle, CenterLabelStyle, EndLabelStyle, viewpoint_diagram_GaugeCompositeStyle, viewpoint_diagram_Note, viewpoint_diagram_FilterVariableHistory, FilterVariableValue, GaugeSection, viewpoint_diagram_BorderedStyle, viewpoint_diagram_CollapseFilter, viewpoint_diagram_IndirectlyCollapseFilter, CollapseFilter, viewpoint_diagram_BeginLabelStyle, viewpoint_diagram_FilterVariableValue, filter_FilterVariable, diagram_viewpoint_EObject, viewpoint_diagram_EndLabelStyle, viewpoint_diagram_CenterLabelStyle, viewpoint_diagram_DiagramElementMapping2ModelElement, ModelElement2ViewVariable, viewpoint_diagram_BracketEdgeStyle, viewpoint_diagram_ComputedStyleDescriptionRegistry, DiagramElementMapping2ModelElement, ContainerVariable2StyleDescription, viewpoint_diagram_ContainerVariable2StyleDescription, viewpoint_diagram_ModelElement2ViewVariable, ViewVariable2ContainerVariable, viewpoint_diagram_ViewVariable2ContainerVariable, description_EdgeMapping, viewpoint_description_DiagramDescription, description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription, concern_ConcernSet, description_Layout, description_AdditionalLayer, tool_ToolSection, viewpoint_description_DiagramImportDescription, description_RepresentationImportDescription, viewpoint_description_DiagramExtensionDescription, description_EdgeMappingImport, viewpoint_description_DiagramElementMapping, description_RepresentationElementMapping, tool_DeleteElementDescription, tool_DirectEditLabel, tool_DoubleClickDescription, viewpoint_description_AbstractNodeMapping, viewpoint_description_NodeMapping, description_AbstractNodeMapping, style_NodeStyleDescription, description_ConditionalNodeStyleDescription, viewpoint_description_ContainerMapping, style_ContainerStyleDescription, description_ConditionalContainerStyleDescription, viewpoint_description_NodeMappingImport, description_AbstractMappingImport, viewpoint_description_ContainerMappingImport, viewpoint_description_EdgeMapping, description_ConditionalEdgeStyleDescription, style_EdgeStyleDescription, viewpoint_description_ConditionalNodeStyleDescription, ConditionalStyleDescription, viewpoint_description_ConditionalEdgeStyleDescription, tool_ReconnectEdgeDescription, viewpoint_description_IEdgeMapping, viewpoint_description_EdgeMappingImport, viewpoint_description_ConditionalContainerStyleDescription, viewpoint_description_Layout, DocumentedElement, viewpoint_description_OrderedTreeLayout, Layout, viewpoint_description_CompositeLayout, viewpoint_description_MappingBasedDecoration, viewpoint_description_Layer, viewpoint_style_BorderedStyleDescription, StyleDescription, DecorationDescriptionsSet, Customization, viewpoint_description_AdditionalLayer, Layer, viewpoint_style_NodeStyleDescription, style_BorderedStyleDescription, style_LabelStyleDescription, style_TooltipStyleDescription, viewpoint_style_CustomStyleDescription, NodeStyleDescription, viewpoint_style_SquareDescription, viewpoint_style_LozengeNodeDescription, viewpoint_style_EllipseNodeDescription, viewpoint_style_BundledImageDescription, viewpoint_style_NoteDescription, viewpoint_style_RoundedCornerStyleDescription, viewpoint_style_DotDescription, viewpoint_style_GaugeCompositeStyleDescription, style_GaugeSectionDescription, viewpoint_style_GaugeSectionDescription, viewpoint_style_SizeComputationContainerStyleDescription, viewpoint_style_ContainerStyleDescription, style_RoundedCornerStyleDescription, viewpoint_style_FlatContainerStyleDescription, style_SizeComputationContainerStyleDescription, viewpoint_style_ShapeContainerStyleDescription, viewpoint_style_WorkspaceImageDescription, viewpoint_style_EdgeStyleDescription, style_BeginLabelStyleDescription, style_CenterLabelStyleDescription, style_EndLabelStyleDescription, viewpoint_style_BeginLabelStyleDescription, viewpoint_style_CenterLabelStyleDescription, viewpoint_style_EndLabelStyleDescription, viewpoint_style_BracketEdgeStyleDescription, EdgeStyleDescription, viewpoint_tool_ToolSection, tool_ToolGroupExtension, viewpoint_tool_ToolGroup, tool_PopupMenu, viewpoint_tool_ToolGroupExtension, tool_ToolGroup, viewpoint_tool_NodeCreationDescription, tool_NodeCreationVariable, tool_InitialNodeCreationOperation, viewpoint_tool_EdgeCreationDescription, tool_SourceEdgeCreationVariable, tool_TargetEdgeCreationVariable, tool_SourceEdgeViewCreationVariable, tool_TargetEdgeViewCreationVariable, tool_InitEdgeCreationOperation, viewpoint_tool_ContainerCreationDescription, viewpoint_tool_DeleteElementDescription, tool_ElementDeleteVariable, tool_DeleteHook, viewpoint_tool_DoubleClickDescription, tool_ElementDoubleClickVariable, viewpoint_tool_DeleteHook, tool_DeleteHookParameter, viewpoint_tool_DeleteHookParameter, viewpoint_tool_ReconnectEdgeDescription, viewpoint_tool_RequestDescription, viewpoint_tool_DirectEditLabel, tool_EditMaskVariables, viewpoint_tool_BehaviorTool, viewpoint_tool_SourceEdgeCreationVariable, viewpoint_tool_SourceEdgeViewCreationVariable, viewpoint_tool_TargetEdgeCreationVariable, viewpoint_tool_TargetEdgeViewCreationVariable, viewpoint_tool_ElementDoubleClickVariable, viewpoint_tool_NodeCreationVariable, viewpoint_tool_CreateView, viewpoint_tool_CreateEdgeView, CreateView, viewpoint_tool_DiagramCreationDescription, RepresentationCreationDescription, viewpoint_tool_DiagramNavigationDescription, RepresentationNavigationDescription, viewpoint_filter_FilterDescription, viewpoint_filter_Filter, viewpoint_filter_MappingFilter, Filter, filter_Filter, viewpoint_tool_Navigation, viewpoint_filter_VariableFilter, viewpoint_filter_FilterVariable, SelectionDescription, viewpoint_validation_ValidationSet, viewpoint_filter_CompositeFilterDescription, FilterDescription, validation_RuleAudit, validation_ValidationFix, viewpoint_validation_SemanticValidationRule, ValidationRule, viewpoint_validation_ViewValidationRule, viewpoint_validation_RuleAudit, viewpoint_validation_ValidationRule, viewpoint_concern_ConcernSet, viewpoint_concern_ConcernDescription, viewpoint_validation_ValidationFix, FontFormat, SyncStatus, LabelAlignment, NavigationTargetType, Position, SystemColors, DragSource, ContainerLayout, LabelPosition, ContainerShape, BackgroundStyle, BundledImageShape, LineStyle, EdgeArrows, EdgeRouting, AlignmentKind, ArrangeConstraint, ResizeKind, FoldingStyle, LayoutDirection, ReconnectionKind, FilterKind, ERROR_LEVEL},
    associations={referencedAnalysis1, models2, description13, ownedNavigationLinks15, eAnnotations4, ownedViews6, selectedViews8, ownedFeatureExtensions11, ownedRepresentationElements22, representationElements23, ownedAnnotationEntries26, diagramSet16, models17, target20, ownedRepresentations31, ownedExtensions34, allRepresentations36, hiddenRepresentations39, semanticElements28, extensionGroup47, description50, target51, referencedRepresentations42, viewpoint45, data53, description55, activatedViewpoints56, analyses58, ownedSessions61, members63, labelColor64, validationSet71, ownedRepresentations72, ownedRepresentationExtensions74, ownedJavaExtensions76, ownedMMExtensions78, ownedFeatureExtensions80, ownedViewpoints65, systemColorsPalette67, userColorsPalettes69, metamodel88, extensionGroup90, detailDescriptions91, ownedTemplates83, metamodel85, ownedRepresentations86, dropDescriptions96, pasteDescriptions97, decorationDescriptions98, navigationDescriptions92, eAnnotations94, details95, featureCustomizations101, reuse102, appliedOn104, appliedOn107, vsmElementCustomizations100, value109, colorSteps111, associatedColor112, systemColors113, defaultTools115, labelBorderStyles117, entries119, entries120, data121, labelBorderStyleDescriptions124, labelColor123, initialOperation129, mappings131, oldContainer132, filters125, element126, elementView127, containerView145, copiedView148, copiedElement151, initialOperation154, element157, newContainer134, element137, newViewContainer139, initialOperation141, container143, containerView158, container161, initialOperation163, element166, containerView168, container171, initialOperation174, containerViewVariable182, representationNameVariable185, representationDescription177, initialOperation179, initialOperation201, parameters204, action205, menuItemDescription206, representationDescription187, containerViewVariable189, containerVariable192, representationNameVariable195, item198, view199, subVariables208, subModelOperations209, firstModelOperations210, firstModelOperations212, firstModelOperations214, firstModelOperations216, object218, subModelOperations220, listeners219, cases222, default223, ownedDiagramElements225, diagramElements226, nodes235, nodeListElements237, containers239, description229, subDiagrams231, edges233, activatedRules248, activateBehaviors250, filterVariableHistory252, activatedLayers254, currentConcern241, activatedFilters243, allFilters245, hiddenElements256, graphicalFilters266, parentLayers259, decorations261, diagramElementMapping263, target269, node271, compositeFilterDescriptions268, ownedStyle275, ownedDetails276, ownedBorderedNodes273, originalStyle279, actualMapping281, candidatesMapping283, elements291, ownedStyle294, ownedDetails296, originalStyle299, nodes286, containers288, ownedDiagramElements307, actualMapping302, candidatesMapping304, ownedStyle311, originalStyle313, actualMapping316, candidatesMapping319, ownedElements309, sourceNode323, targetNode325, actualMapping328, ownedStyle322, description336, diagrams338, originalStyle330, path333, backgroundColor343, view341, backgroundColor344, foregroundColor346, backgroundColor354, backgroundColor349, foregroundColor351, color358, color356, color360, color362, strokeColor370, outgoingEdges364, incomingEdges367, endLabelStyle376, beginLabelStyle372, centerLabelStyle374, borderColor379, color381, ownedValues383, sections378, variableDefinition384, modelElement385, cache389, key391, value393, computedStyleDescriptions387, value401, key403, value405, key395, value397, key399, allEdgeMappings410, allNodeMappings412, allContainerMappings415, filters408, defaultConcern425, validationSet418, concerns421, allTools423, allActivatedTools444, nodeMappings447, edgeMappings450, init428, layout431, diagramInitialisation433, defaultLayer436, additionalLayers439, allLayers441, toolSection461, reusedTools463, importedDiagram466, layers468, edgeMappingImports453, containerMappings455, reusedMappings458, validationSet470, concerns473, deletionDescription476, labelDirectEdit477, doubleClickDescription479, borderedNodeMappings481, reusedBorderedNodeMappings483, reusedNodeMappings494, subContainerMappings497, style486, conditionnalStyles487, subNodeMappings489, allNodeMappings491, reusedContainerMappings500, allContainerMappings503, style506, conditionnalStyles508, importedMapping510, importedMapping512, style519, conditionnalStyles521, sourceMapping514, targetMapping516, style532, style534, reconnections523, pathNodeMapping525, importedMapping527, conditionnalStyles529, style536, nodeMapping538, mappings540, edgeMappings544, nodeMappings542, edgeMappingImports547, containerMappings550, reusedMappings553, allTools556, toolSections559, reusedTools562, decorationDescriptionsSet565, allEdgeMappings567, customization570, color574, borderColor572, color580, color576, color578, color582, backgroundColor584, sections586, backgroundColor587, foregroundColor589, backgroundColor592, foregroundColor594, labelBorderStyle597, backgroundColor600, strokeColor602, subSections612, beginLabelStyleDescription604, centerLabelStyleDescription606, endLabelStyleDescription608, ownedTools610, groupExtensions620, tools622, popupMenus615, reusedTools617, group624, tools625, nodeMappings628, variable630, viewVariable632, initialOperation635, extraMappings637, edgeMappings640, sourceVariable642, targetVariable644, sourceViewVariable646, targetViewVariable648, initialOperation650, containerMappings658, variable660, viewVariable663, initialOperation666, extraMappings669, element672, extraSourceMappings652, extraTargetMappings655, initialOperation679, hook682, mappings684, element687, elementView688, initialOperation691, parameters694, elementView673, containerView676, target697, sourceView700, targetView703, element706, initialOperation709, edgeView712, mask715, initialOperation716, source695, initialOperation719, mapping721, diagramDescription723, diagramDescription725, diagramDescription727, mappings729, filters731, ownedVariables732, ownedRules734, reusedRules736, allRules739, audits742, fixes743, targets745, initialOperation747, ownedConcernDescriptions749, filters751, rules753, behaviors756},
    generalizations={gen_viewpoint_DRepresentationContainer_DView, gen_viewpoint_DRepresentation_description_DModelElement, gen_viewpoint_DRepresentationElement_DLabelled, gen_viewpoint_DRepresentationElement_DMappingBased, gen_viewpoint_DRepresentationElement_DStylizable, gen_viewpoint_DRepresentationElement_DRefreshable, gen_viewpoint_DRepresentationElement_DSemanticDecorator, gen_viewpoint_DRepresentation_description_DocumentedElement, gen_viewpoint_DRepresentation_DRefreshable, gen_viewpoint_DView_DRefreshable, gen_viewpoint_DEObjectLink_DNavigationLink, gen_viewpoint_LabelStyle_BasicLabelStyle, gen_viewpoint_Style_DRefreshable, gen_viewpoint_Style_Customizable, gen_viewpoint_DSourceFileLink_DNavigationLink, gen_viewpoint_DFile_DResource, gen_viewpoint_DProject_DResourceContainer, gen_viewpoint_DFolder_DResourceContainer, gen_viewpoint_DModel_DFile, gen_viewpoint_BasicLabelStyle_Customizable, gen_viewpoint_DResourceContainer_DResource, gen_viewpoint_description_Group_description_DModelElement, gen_viewpoint_description_Group_description_DocumentedElement, gen_viewpoint_description_Viewpoint_description_DocumentedElement, gen_viewpoint_description_Viewpoint_description_Component, gen_viewpoint_description_Viewpoint_description_EndUserDocumentedElement, gen_viewpoint_description_Viewpoint_description_IdentifiedElement, gen_viewpoint_description_RepresentationElementMapping_IdentifiedElement, gen_viewpoint_description_RepresentationDescription_description_DocumentedElement, gen_viewpoint_description_RepresentationDescription_description_EndUserDocumentedElement, gen_viewpoint_description_RepresentationDescription_description_IdentifiedElement, gen_viewpoint_description_RepresentationImportDescription_RepresentationDescription, gen_viewpoint_description_VSMElementCustomization_IVSMElementCustomization, gen_viewpoint_description_VSMElementCustomizationReuse_IVSMElementCustomization, gen_viewpoint_description_EAttributeCustomization_EStructuralFeatureCustomization, gen_viewpoint_description_SemanticBasedDecoration_DecorationDescription, gen_viewpoint_description_SystemColor_FixedColor, gen_viewpoint_description_InterpolatedColor_description_ColorDescription, gen_viewpoint_description_InterpolatedColor_description_UserColor, gen_viewpoint_description_EReferenceCustomization_EStructuralFeatureCustomization, gen_viewpoint_description_FixedColor_ColorDescription, gen_viewpoint_description_UserFixedColor_description_FixedColor, gen_viewpoint_description_UserFixedColor_description_UserColor, gen_viewpoint_description_ComputedColor_description_UserColor, gen_viewpoint_description_ComputedColor_description_ColorDescription, gen_viewpoint_tool_ToolEntry_description_DocumentedElement, gen_viewpoint_tool_ToolEntry_description_IdentifiedElement, gen_viewpoint_style_LabelStyleDescription_BasicLabelStyleDescription, gen_viewpoint_tool_ContainerDropDescription_MappingBasedToolDescription, gen_viewpoint_tool_AbstractToolDescription_ToolEntry, gen_viewpoint_tool_MappingBasedToolDescription_AbstractToolDescription, gen_viewpoint_tool_ToolDescription_MappingBasedToolDescription, gen_viewpoint_tool_SelectionWizardDescription_tool_AbstractToolDescription, gen_viewpoint_tool_SelectionWizardDescription_description_SelectionDescription, gen_viewpoint_tool_PasteDescription_MappingBasedToolDescription, gen_viewpoint_tool_PaneBasedSelectionWizardDescription_AbstractToolDescription, gen_viewpoint_tool_RepresentationNavigationDescription_AbstractToolDescription, gen_viewpoint_tool_RepresentationCreationDescription_AbstractToolDescription, gen_viewpoint_tool_ExternalJavaAction_tool_MenuItemDescription, gen_viewpoint_tool_ExternalJavaAction_tool_ContainerModelOperation, gen_viewpoint_tool_ExternalJavaActionCall_tool_MenuItemDescription, gen_viewpoint_tool_ExternalJavaActionCall_tool_ContainerModelOperation, gen_viewpoint_tool_PopupMenu_AbstractToolDescription, gen_viewpoint_tool_MenuItemDescription_tool_AbstractToolDescription, gen_viewpoint_tool_MenuItemDescription_tool_MenuItemOrRef, gen_viewpoint_tool_MenuItemDescriptionReference_MenuItemOrRef, gen_viewpoint_tool_OperationAction_MenuItemDescription, gen_viewpoint_tool_AcceleoVariable_tool_VariableContainer, gen_viewpoint_tool_AcceleoVariable_tool_SubVariable, gen_viewpoint_tool_SubVariable_AbstractVariable, gen_viewpoint_tool_DialogVariable_AbstractVariable, gen_viewpoint_tool_ElementDropVariable_tool_AbstractVariable, gen_viewpoint_tool_SelectModelElementVariable_tool_SubVariable, gen_viewpoint_tool_SelectModelElementVariable_description_SelectionDescription, gen_viewpoint_tool_ContainerModelOperation_ModelOperation, gen_viewpoint_tool_ElementDropVariable_tool_VariableContainer, gen_viewpoint_tool_ElementSelectVariable_AbstractVariable, gen_viewpoint_tool_ElementVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementVariable_tool_VariableContainer, gen_viewpoint_tool_ElementViewVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementViewVariable_tool_VariableContainer, gen_viewpoint_tool_ElementDeleteVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementDeleteVariable_tool_VariableContainer, gen_viewpoint_tool_DropContainerVariable_tool_AbstractVariable, gen_viewpoint_tool_DropContainerVariable_tool_VariableContainer, gen_viewpoint_tool_SelectContainerVariable_tool_AbstractVariable, gen_viewpoint_tool_SelectContainerVariable_tool_VariableContainer, gen_viewpoint_tool_ContainerViewVariable_tool_AbstractVariable, gen_viewpoint_tool_ContainerViewVariable_tool_VariableContainer, gen_viewpoint_tool_CreateInstance_ContainerModelOperation, gen_viewpoint_tool_ChangeContext_ContainerModelOperation, gen_viewpoint_tool_SetObject_ContainerModelOperation, gen_viewpoint_tool_Unset_ContainerModelOperation, gen_viewpoint_tool_SetValue_ContainerModelOperation, gen_viewpoint_tool_RemoveElement_ContainerModelOperation, gen_viewpoint_tool_For_ContainerModelOperation, gen_viewpoint_tool_MoveElement_ContainerModelOperation, gen_viewpoint_tool_If_ContainerModelOperation, gen_viewpoint_tool_DeleteView_ContainerModelOperation, gen_viewpoint_tool_NameVariable_AbstractVariable, gen_viewpoint_tool_Default_SwitchChild, gen_viewpoint_tool_Switch_ModelOperation, gen_viewpoint_tool_Case_SwitchChild, gen_viewpoint_audit_TemplateInformationSection_InformationSection, gen_viewpoint_diagram_DDiagram_DRepresentation, gen_viewpoint_diagram_DDiagram_description_DocumentedElement, gen_viewpoint_diagram_DDiagram_DragAndDropTarget, gen_viewpoint_diagram_DDiagram_DValidable, gen_viewpoint_diagram_DDiagram_DContainer, gen_viewpoint_diagram_DDiagramElement_DRepresentationElement, gen_viewpoint_diagram_DDiagramElement_DValidable, gen_viewpoint_diagram_DDiagramElement_DNavigable, gen_viewpoint_diagram_DSemanticDiagram_diagram_DDiagram, gen_viewpoint_diagram_DSemanticDiagram_DSemanticDecorator, gen_viewpoint_diagram_HideFilter_GraphicalFilter, gen_viewpoint_diagram_HideLabelFilter_GraphicalFilter, gen_viewpoint_diagram_FoldingPointFilter_GraphicalFilter, gen_viewpoint_diagram_DDiagramLink_DNavigationLink, gen_viewpoint_diagram_AbstractDNode_DDiagramElement, gen_viewpoint_diagram_FoldingFilter_GraphicalFilter, gen_viewpoint_diagram_AppliedCompositeFilters_GraphicalFilter, gen_viewpoint_diagram_AbsoluteBoundsFilter_GraphicalFilter, gen_viewpoint_diagram_DNode_diagram_AbstractDNode, gen_viewpoint_diagram_DNode_diagram_EdgeTarget, gen_viewpoint_diagram_DNode_DragAndDropTarget, gen_viewpoint_diagram_DDiagramElementContainer_diagram_AbstractDNode, gen_viewpoint_diagram_DDiagramElementContainer_diagram_EdgeTarget, gen_viewpoint_diagram_DDiagramElementContainer_DragAndDropTarget, gen_viewpoint_diagram_DDiagramElementContainer_DContainer, gen_viewpoint_diagram_DNodeContainer_DDiagramElementContainer, gen_viewpoint_diagram_DNodeList_DDiagramElementContainer, gen_viewpoint_diagram_DNodeListElement_AbstractDNode, gen_viewpoint_diagram_DEdge_diagram_DDiagramElement, gen_viewpoint_diagram_DEdge_diagram_EdgeTarget, gen_viewpoint_diagram_Dot_NodeStyle, gen_viewpoint_diagram_NodeStyle_LabelStyle, gen_viewpoint_diagram_NodeStyle_Style, gen_viewpoint_diagram_NodeStyle_diagram_BorderedStyle, gen_viewpoint_diagram_ContainerStyle_LabelStyle, gen_viewpoint_diagram_ContainerStyle_Style, gen_viewpoint_diagram_ContainerStyle_diagram_BorderedStyle, gen_viewpoint_diagram_FlatContainerStyle_ContainerStyle, gen_viewpoint_diagram_GaugeSection_Customizable, gen_viewpoint_diagram_Square_NodeStyle, gen_viewpoint_diagram_ShapeContainerStyle_ContainerStyle, gen_viewpoint_diagram_Lozenge_NodeStyle, gen_viewpoint_diagram_Ellipse_NodeStyle, gen_viewpoint_diagram_WorkspaceImage_diagram_NodeStyle, gen_viewpoint_diagram_WorkspaceImage_diagram_ContainerStyle, gen_viewpoint_diagram_CustomStyle_NodeStyle, gen_viewpoint_diagram_BundledImage_NodeStyle, gen_viewpoint_diagram_EdgeStyle_Style, gen_viewpoint_diagram_GaugeCompositeStyle_NodeStyle, gen_viewpoint_diagram_Note_NodeStyle, gen_viewpoint_diagram_BorderedStyle_Style, gen_viewpoint_diagram_CollapseFilter_GraphicalFilter, gen_viewpoint_diagram_IndirectlyCollapseFilter_CollapseFilter, gen_viewpoint_diagram_BeginLabelStyle_BasicLabelStyle, gen_viewpoint_diagram_EndLabelStyle_BasicLabelStyle, gen_viewpoint_diagram_CenterLabelStyle_BasicLabelStyle, gen_viewpoint_diagram_BracketEdgeStyle_EdgeStyle, gen_viewpoint_description_DiagramDescription_description_DragAndDropTargetDescription, gen_viewpoint_description_DiagramDescription_description_RepresentationDescription, gen_viewpoint_description_DiagramDescription_description_PasteTargetDescription, gen_viewpoint_description_DiagramImportDescription_description_RepresentationImportDescription, gen_viewpoint_description_DiagramImportDescription_description_DiagramDescription, gen_viewpoint_description_DiagramExtensionDescription_RepresentationExtensionDescription, gen_viewpoint_description_DiagramElementMapping_description_RepresentationElementMapping, gen_viewpoint_description_DiagramElementMapping_description_PasteTargetDescription, gen_viewpoint_description_AbstractNodeMapping_description_DiagramElementMapping, gen_viewpoint_description_AbstractNodeMapping_description_DocumentedElement, gen_viewpoint_description_NodeMapping_description_AbstractNodeMapping, gen_viewpoint_description_NodeMapping_description_DragAndDropTargetDescription, gen_viewpoint_description_ContainerMapping_description_AbstractNodeMapping, gen_viewpoint_description_ContainerMapping_description_DragAndDropTargetDescription, gen_viewpoint_description_NodeMappingImport_description_NodeMapping, gen_viewpoint_description_NodeMappingImport_description_AbstractMappingImport, gen_viewpoint_description_ContainerMappingImport_description_ContainerMapping, gen_viewpoint_description_ContainerMappingImport_description_AbstractMappingImport, gen_viewpoint_description_EdgeMapping_description_DiagramElementMapping, gen_viewpoint_description_EdgeMapping_description_DocumentedElement, gen_viewpoint_description_EdgeMapping_description_IEdgeMapping, gen_viewpoint_description_ConditionalNodeStyleDescription_ConditionalStyleDescription, gen_viewpoint_description_ConditionalEdgeStyleDescription_ConditionalStyleDescription, gen_viewpoint_description_EdgeMappingImport_description_DocumentedElement, gen_viewpoint_description_EdgeMappingImport_description_IEdgeMapping, gen_viewpoint_description_EdgeMappingImport_description_IdentifiedElement, gen_viewpoint_description_ConditionalContainerStyleDescription_ConditionalStyleDescription, gen_viewpoint_description_Layout_DocumentedElement, gen_viewpoint_description_OrderedTreeLayout_Layout, gen_viewpoint_description_CompositeLayout_Layout, gen_viewpoint_description_MappingBasedDecoration_DecorationDescription, gen_viewpoint_description_Layer_description_DocumentedElement, gen_viewpoint_description_Layer_description_EndUserDocumentedElement, gen_viewpoint_description_Layer_description_IdentifiedElement, gen_viewpoint_style_BorderedStyleDescription_StyleDescription, gen_viewpoint_description_AdditionalLayer_Layer, gen_viewpoint_style_NodeStyleDescription_style_StyleDescription, gen_viewpoint_style_NodeStyleDescription_style_BorderedStyleDescription, gen_viewpoint_style_NodeStyleDescription_style_LabelStyleDescription, gen_viewpoint_style_NodeStyleDescription_style_TooltipStyleDescription, gen_viewpoint_style_CustomStyleDescription_NodeStyleDescription, gen_viewpoint_style_SquareDescription_NodeStyleDescription, gen_viewpoint_style_LozengeNodeDescription_NodeStyleDescription, gen_viewpoint_style_EllipseNodeDescription_NodeStyleDescription, gen_viewpoint_style_BundledImageDescription_NodeStyleDescription, gen_viewpoint_style_NoteDescription_NodeStyleDescription, gen_viewpoint_style_RoundedCornerStyleDescription_StyleDescription, gen_viewpoint_style_DotDescription_NodeStyleDescription, gen_viewpoint_style_GaugeCompositeStyleDescription_NodeStyleDescription, gen_viewpoint_style_ContainerStyleDescription_style_RoundedCornerStyleDescription, gen_viewpoint_style_ContainerStyleDescription_style_BorderedStyleDescription, gen_viewpoint_style_ContainerStyleDescription_style_LabelStyleDescription, gen_viewpoint_style_ContainerStyleDescription_style_TooltipStyleDescription, gen_viewpoint_style_FlatContainerStyleDescription_style_ContainerStyleDescription, gen_viewpoint_style_FlatContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_viewpoint_style_ShapeContainerStyleDescription_style_ContainerStyleDescription, gen_viewpoint_style_ShapeContainerStyleDescription_style_SizeComputationContainerStyleDescription, gen_viewpoint_style_WorkspaceImageDescription_style_NodeStyleDescription, gen_viewpoint_style_WorkspaceImageDescription_style_ContainerStyleDescription, gen_viewpoint_style_EdgeStyleDescription_StyleDescription, gen_viewpoint_style_BeginLabelStyleDescription_BasicLabelStyleDescription, gen_viewpoint_style_CenterLabelStyleDescription_BasicLabelStyleDescription, gen_viewpoint_style_EndLabelStyleDescription_BasicLabelStyleDescription, gen_viewpoint_style_BracketEdgeStyleDescription_EdgeStyleDescription, gen_viewpoint_tool_ToolSection_description_DocumentedElement, gen_viewpoint_tool_ToolSection_description_IdentifiedElement, gen_viewpoint_tool_ToolGroup_ToolEntry, gen_viewpoint_tool_NodeCreationDescription_MappingBasedToolDescription, gen_viewpoint_tool_EdgeCreationDescription_MappingBasedToolDescription, gen_viewpoint_tool_ContainerCreationDescription_MappingBasedToolDescription, gen_viewpoint_tool_DeleteElementDescription_MappingBasedToolDescription, gen_viewpoint_tool_DoubleClickDescription_MappingBasedToolDescription, gen_viewpoint_tool_ReconnectEdgeDescription_MappingBasedToolDescription, gen_viewpoint_tool_RequestDescription_AbstractToolDescription, gen_viewpoint_tool_DirectEditLabel_MappingBasedToolDescription, gen_viewpoint_tool_BehaviorTool_AbstractToolDescription, gen_viewpoint_tool_SourceEdgeCreationVariable_tool_AbstractVariable, gen_viewpoint_tool_SourceEdgeCreationVariable_tool_VariableContainer, gen_viewpoint_tool_SourceEdgeViewCreationVariable_tool_AbstractVariable, gen_viewpoint_tool_SourceEdgeViewCreationVariable_tool_VariableContainer, gen_viewpoint_tool_TargetEdgeCreationVariable_tool_AbstractVariable, gen_viewpoint_tool_TargetEdgeCreationVariable_tool_VariableContainer, gen_viewpoint_tool_TargetEdgeViewCreationVariable_tool_AbstractVariable, gen_viewpoint_tool_TargetEdgeViewCreationVariable_tool_VariableContainer, gen_viewpoint_tool_ElementDoubleClickVariable_tool_AbstractVariable, gen_viewpoint_tool_ElementDoubleClickVariable_tool_VariableContainer, gen_viewpoint_tool_NodeCreationVariable_tool_AbstractVariable, gen_viewpoint_tool_NodeCreationVariable_tool_VariableContainer, gen_viewpoint_tool_CreateView_ContainerModelOperation, gen_viewpoint_tool_CreateEdgeView_CreateView, gen_viewpoint_tool_DiagramCreationDescription_RepresentationCreationDescription, gen_viewpoint_tool_DiagramNavigationDescription_RepresentationNavigationDescription, gen_viewpoint_filter_FilterDescription_description_DocumentedElement, gen_viewpoint_filter_FilterDescription_description_IdentifiedElement, gen_viewpoint_filter_MappingFilter_Filter, gen_viewpoint_tool_Navigation_ContainerModelOperation, gen_viewpoint_filter_VariableFilter_Filter, gen_viewpoint_filter_FilterVariable_SelectionDescription, gen_viewpoint_validation_ValidationSet_DocumentedElement, gen_viewpoint_filter_CompositeFilterDescription_FilterDescription, gen_viewpoint_validation_SemanticValidationRule_ValidationRule, gen_viewpoint_validation_ViewValidationRule_ValidationRule, gen_viewpoint_concern_ConcernSet_DocumentedElement, gen_viewpoint_concern_ConcernDescription_description_DocumentedElement, gen_viewpoint_concern_ConcernDescription_description_IdentifiedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)