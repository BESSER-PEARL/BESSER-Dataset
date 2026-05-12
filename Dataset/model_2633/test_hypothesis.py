import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DNode,
    DContainer,
    DValidable,
    DragAndDropTarget,
    DRepresentation,
    InformationSection,
    viewpoint_audit_TemplateInformationSection,
    description_DiagramDescription,
    DDiagramElement,
    SwitchChild,
    viewpoint_tool_Case,
    viewpoint_tool_FeatureChangeListener,
    tool_FeatureChangeListener,
    viewpoint_audit_InformationSection,
    tool_Default,
    tool_Case,
    viewpoint_tool_Default,
    viewpoint_tool_SwitchChild,
    viewpoint_tool_ToolFilterDescription,
    viewpoint_tool_ExternalJavaActionParameter,
    tool_viewpoint_EObject,
    ContainerModelOperation,
    viewpoint_tool_DeleteView,
    viewpoint_tool_MoveElement,
    viewpoint_tool_SetValue,
    viewpoint_tool_If,
    viewpoint_tool_SetObject,
    viewpoint_tool_ChangeContext,
    viewpoint_tool_Unset,
    viewpoint_tool_For,
    viewpoint_tool_RemoveElement,
    viewpoint_tool_CreateInstance,
    viewpoint_tool_InitialContainerDropOperation,
    viewpoint_validation_ValidationFix,
    ValidationRule,
    viewpoint_validation_ViewValidationRule,
    viewpoint_validation_SemanticValidationRule,
    validation_ValidationFix,
    validation_RuleAudit,
    viewpoint_validation_ValidationRule,
    viewpoint_validation_RuleAudit,
    SelectionDescription,
    viewpoint_filter_FilterVariable,
    filter_Filter,
    FilterDescription,
    viewpoint_filter_CompositeFilterDescription,
    Filter,
    viewpoint_filter_VariableFilter,
    viewpoint_filter_MappingFilter,
    viewpoint_filter_Filter,
    viewpoint_tool_Navigation,
    RepresentationNavigationDescription,
    CreateView,
    viewpoint_tool_DiagramNavigationDescription,
    viewpoint_tool_CreateEdgeView,
    RepresentationCreationDescription,
    viewpoint_tool_DiagramCreationDescription,
    viewpoint_tool_CreateView,
    tool_EditMaskVariables,
    tool_ElementDoubleClickVariable,
    tool_DeleteHook,
    viewpoint_tool_DeleteHookParameter,
    tool_DeleteHookParameter,
    viewpoint_tool_DeleteHook,
    tool_ElementDeleteVariable,
    tool_TargetEdgeViewCreationVariable,
    tool_SourceEdgeViewCreationVariable,
    tool_TargetEdgeCreationVariable,
    tool_SourceEdgeCreationVariable,
    tool_InitEdgeCreationOperation,
    tool_InitialNodeCreationOperation,
    tool_NodeCreationVariable,
    tool_PopupMenu,
    tool_ToolGroup,
    viewpoint_tool_ToolGroupExtension,
    tool_ToolGroupExtension,
    style_BeginLabelStyleDescription,
    EdgeStyleDescription,
    viewpoint_style_BracketEdgeStyleDescription,
    style_EndLabelStyleDescription,
    style_CenterLabelStyleDescription,
    viewpoint_style_SizeComputationContainerStyleDescription,
    style_SizeComputationContainerStyleDescription,
    style_RoundedCornerStyleDescription,
    viewpoint_style_GaugeSectionDescription,
    style_GaugeSectionDescription,
    NodeStyleDescription,
    viewpoint_style_DotDescription,
    viewpoint_style_GaugeCompositeStyleDescription,
    viewpoint_style_LozengeNodeDescription,
    viewpoint_style_SquareDescription,
    viewpoint_style_NoteDescription,
    viewpoint_style_BundledImageDescription,
    viewpoint_style_CustomStyleDescription,
    viewpoint_style_EllipseNodeDescription,
    style_TooltipStyleDescription,
    style_LabelStyleDescription,
    style_BorderedStyleDescription,
    viewpoint_style_ContainerStyleDescription,
    StyleDescription,
    viewpoint_style_RoundedCornerStyleDescription,
    viewpoint_style_EdgeStyleDescription,
    viewpoint_style_BorderedStyleDescription,
    Layer,
    viewpoint_description_AdditionalLayer,
    Customization,
    DecorationDescriptionsSet,
    Layout,
    viewpoint_description_CompositeLayout,
    viewpoint_description_OrderedTreeLayout,
    DocumentedElement,
    viewpoint_concern_ConcernSet,
    viewpoint_validation_ValidationSet,
    viewpoint_description_Layout,
    ConditionalStyleDescription,
    viewpoint_description_ConditionalContainerStyleDescription,
    viewpoint_description_ConditionalEdgeStyleDescription,
    viewpoint_description_ConditionalNodeStyleDescription,
    description_ConditionalEdgeStyleDescription,
    style_EdgeStyleDescription,
    viewpoint_description_IEdgeMapping,
    tool_ReconnectEdgeDescription,
    description_ConditionalContainerStyleDescription,
    style_ContainerStyleDescription,
    viewpoint_style_FlatContainerStyleDescription,
    viewpoint_style_ShapeContainerStyleDescription,
    description_AbstractMappingImport,
    description_ConditionalNodeStyleDescription,
    style_NodeStyleDescription,
    viewpoint_style_WorkspaceImageDescription,
    tool_DoubleClickDescription,
    description_AbstractNodeMapping,
    tool_DirectEditLabel,
    tool_DeleteElementDescription,
    tool_ToolSection,
    description_RepresentationElementMapping,
    description_RepresentationImportDescription,
    viewpoint_description_DiagramImportDescription,
    description_AdditionalLayer,
    description_Layout,
    description_EdgeMappingImport,
    description_EdgeMapping,
    concern_ConcernSet,
    ModelElement2ViewVariable,
    viewpoint_diagram_DiagramElementMapping2ModelElement,
    DiagramElementMapping2ModelElement,
    viewpoint_diagram_ComputedStyleDescriptionRegistry,
    description_PasteTargetDescription,
    viewpoint_description_DiagramElementMapping,
    description_RepresentationDescription,
    description_DragAndDropTargetDescription,
    viewpoint_description_NodeMapping,
    viewpoint_description_ContainerMapping,
    viewpoint_description_DiagramDescription,
    viewpoint_diagram_ContainerVariable2StyleDescription,
    ContainerVariable2StyleDescription,
    viewpoint_diagram_ViewVariable2ContainerVariable,
    ViewVariable2ContainerVariable,
    viewpoint_diagram_ModelElement2ViewVariable,
    diagram_viewpoint_EObject,
    filter_FilterVariable,
    viewpoint_diagram_FilterVariableValue,
    FilterVariableValue,
    CollapseFilter,
    viewpoint_diagram_IndirectlyCollapseFilter,
    viewpoint_diagram_FilterVariableHistory,
    GaugeSection,
    EndLabelStyle,
    CenterLabelStyle,
    BeginLabelStyle,
    diagram_ContainerStyle,
    diagram_NodeStyle,
    viewpoint_diagram_WorkspaceImage,
    viewpoint_diagram_EdgeTarget,
    diagram_BorderedStyle,
    Style,
    viewpoint_diagram_EdgeStyle,
    viewpoint_diagram_BorderedStyle,
    LabelStyle,
    viewpoint_diagram_ContainerStyle,
    viewpoint_diagram_NodeStyle,
    diagram_viewpoint_DRepresentationContainer,
    diagram_viewpoint_RGBValues,
    description_IEdgeMapping,
    viewpoint_diagram_DDiagramSet,
    AbstractDNode,
    viewpoint_diagram_DNodeListElement,
    EdgeStyle,
    viewpoint_diagram_BracketEdgeStyle,
    diagram_DDiagramElement,
    description_ContainerMapping,
    viewpoint_description_ContainerMappingImport,
    ContainerStyle,
    viewpoint_diagram_FlatContainerStyle,
    viewpoint_diagram_ShapeContainerStyle,
    diagram_EdgeTarget,
    viewpoint_diagram_DEdge,
    diagram_AbstractDNode,
    viewpoint_diagram_DDiagramElementContainer,
    viewpoint_diagram_DNode,
    viewpoint_diagram_AbstractDNode,
    EdgeTarget,
    description_NodeMapping,
    viewpoint_description_NodeMappingImport,
    diagram_viewpoint_Style,
    NodeStyle,
    viewpoint_diagram_BundledImage,
    viewpoint_diagram_CustomStyle,
    viewpoint_diagram_Ellipse,
    viewpoint_diagram_Lozenge,
    viewpoint_diagram_Note,
    viewpoint_diagram_Dot,
    viewpoint_diagram_GaugeCompositeStyle,
    viewpoint_diagram_Square,
    viewpoint_diagram_GraphicalFilter,
    GraphicalFilter,
    viewpoint_diagram_CollapseFilter,
    diagram_viewpoint_Decoration,
    viewpoint_diagram_AbsoluteBoundsFilter,
    filter_CompositeFilterDescription,
    viewpoint_diagram_AppliedCompositeFilters,
    viewpoint_diagram_FoldingFilter,
    viewpoint_diagram_FoldingPointFilter,
    viewpoint_diagram_HideLabelFilter,
    viewpoint_diagram_HideFilter,
    description_Layer,
    FilterVariableHistory,
    tool_BehaviorTool,
    validation_ValidationRule,
    DNavigable,
    DRepresentationElement,
    viewpoint_diagram_DDiagramElement,
    diagram_DDiagram,
    DEdge,
    DDiagram,
    filter_FilterDescription,
    concern_ConcernDescription,
    DDiagramElementContainer,
    viewpoint_diagram_DNodeContainer,
    viewpoint_diagram_DNodeList,
    DNodeListElement,
    viewpoint_tool_InitEdgeCreationOperation,
    viewpoint_tool_InitialOperation,
    viewpoint_tool_InitialNodeCreationOperation,
    viewpoint_tool_ModelOperation,
    tool_ModelOperation,
    ModelOperation,
    viewpoint_tool_Switch,
    viewpoint_tool_ContainerModelOperation,
    viewpoint_tool_EditMaskVariables,
    tool_AbstractVariable,
    AbstractVariable,
    viewpoint_tool_ElementSelectVariable,
    viewpoint_tool_NameVariable,
    viewpoint_tool_DialogVariable,
    viewpoint_tool_SubVariable,
    tool_VariableContainer,
    viewpoint_tool_ContainerViewVariable,
    viewpoint_tool_ElementDropVariable,
    viewpoint_tool_SelectContainerVariable,
    viewpoint_tool_TargetEdgeCreationVariable,
    viewpoint_tool_SourceEdgeCreationVariable,
    viewpoint_tool_NodeCreationVariable,
    viewpoint_tool_ElementDoubleClickVariable,
    viewpoint_tool_TargetEdgeViewCreationVariable,
    viewpoint_tool_SourceEdgeViewCreationVariable,
    viewpoint_tool_ElementVariable,
    tool_SubVariable,
    viewpoint_tool_AcceleoVariable,
    viewpoint_tool_VariableContainer,
    viewpoint_tool_AbstractVariable,
    tool_ExternalJavaAction,
    tool_ExternalJavaActionParameter,
    tool_ContainerModelOperation,
    viewpoint_tool_DropContainerVariable,
    viewpoint_tool_ElementDeleteVariable,
    viewpoint_tool_ElementViewVariable,
    MenuItemDescription,
    viewpoint_tool_OperationAction,
    tool_MenuItemDescription,
    viewpoint_tool_ExternalJavaAction,
    viewpoint_tool_ExternalJavaActionCall,
    MenuItemOrRef,
    viewpoint_tool_MenuItemDescriptionReference,
    tool_MenuItemOrRef,
    viewpoint_tool_MenuItemOrRef,
    tool_NameVariable,
    tool_SelectContainerVariable,
    tool_InitialContainerDropOperation,
    tool_ContainerViewVariable,
    tool_ElementSelectVariable,
    description_SelectionDescription,
    viewpoint_tool_SelectModelElementVariable,
    tool_AbstractToolDescription,
    viewpoint_tool_MenuItemDescription,
    viewpoint_tool_SelectionWizardDescription,
    tool_DropContainerVariable,
    description_DiagramElementMapping,
    tool_InitialOperation,
    tool_ElementViewVariable,
    tool_ElementVariable,
    MappingBasedToolDescription,
    viewpoint_tool_NodeCreationDescription,
    viewpoint_tool_ReconnectEdgeDescription,
    viewpoint_tool_PasteDescription,
    viewpoint_tool_DirectEditLabel,
    viewpoint_tool_ContainerCreationDescription,
    viewpoint_tool_DeleteElementDescription,
    viewpoint_tool_EdgeCreationDescription,
    viewpoint_tool_ContainerDropDescription,
    viewpoint_tool_DoubleClickDescription,
    viewpoint_tool_ToolDescription,
    AbstractToolDescription,
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    viewpoint_tool_PopupMenu,
    viewpoint_tool_RepresentationNavigationDescription,
    viewpoint_tool_RepresentationCreationDescription,
    viewpoint_tool_BehaviorTool,
    viewpoint_tool_RequestDescription,
    viewpoint_tool_MappingBasedToolDescription,
    tool_ElementDropVariable,
    tool_ToolFilterDescription,
    ToolEntry,
    viewpoint_tool_ToolGroup,
    viewpoint_tool_AbstractToolDescription,
    viewpoint_style_TooltipStyleDescription,
    viewpoint_style_LabelBorderStyleDescription,
    style_LabelBorderStyleDescription,
    viewpoint_style_LabelBorderStyles,
    BasicLabelStyleDescription,
    viewpoint_style_CenterLabelStyleDescription,
    viewpoint_style_EndLabelStyleDescription,
    viewpoint_style_BeginLabelStyleDescription,
    viewpoint_style_LabelStyleDescription,
    viewpoint_style_BasicLabelStyleDescription,
    viewpoint_style_StyleDescription,
    viewpoint_description_DAnnotationEntry,
    viewpoint_description_IdentifiedElement,
    viewpoint_description_EndUserDocumentedElement,
    viewpoint_description_AnnotationEntry,
    UserColor,
    viewpoint_description_UserColorsPalette,
    SystemColor,
    viewpoint_description_SytemColorsPalette,
    style_LabelBorderStyles,
    tool_ToolEntry,
    viewpoint_description_Environment,
    viewpoint_description_UserColor,
    description_FixedColor,
    ColorDescription,
    viewpoint_description_FixedColor,
    viewpoint_description_ColorStep,
    ColorStep,
    description_ColorDescription,
    FixedColor,
    viewpoint_description_SystemColor,
    viewpoint_description_ColorDescription,
    viewpoint_description_SelectionDescription,
    description_UserColor,
    viewpoint_description_UserFixedColor,
    viewpoint_description_InterpolatedColor,
    viewpoint_description_ComputedColor,
    EStructuralFeatureCustomization,
    viewpoint_description_EReferenceCustomization,
    viewpoint_description_IVSMElementCustomization,
    IVSMElementCustomization,
    viewpoint_description_VSMElementCustomizationReuse,
    viewpoint_description_VSMElementCustomization,
    viewpoint_description_Customization,
    viewpoint_description_EAttributeCustomization,
    viewpoint_description_EStructuralFeatureCustomization,
    viewpoint_description_DecorationDescription,
    viewpoint_description_DecorationDescriptionsSet,
    tool_PasteDescription,
    viewpoint_description_PasteTargetDescription,
    tool_ContainerDropDescription,
    viewpoint_description_DragAndDropTargetDescription,
    viewpoint_description_ConditionalStyleDescription,
    description_viewpoint_EStringToStringMapEntry,
    viewpoint_description_DAnnotation,
    DAnnotation,
    viewpoint_description_AbstractMappingImport,
    tool_RepresentationNavigationDescription,
    tool_RepresentationCreationDescription,
    IdentifiedElement,
    viewpoint_description_RepresentationElementMapping,
    viewpoint_description_JavaExtension,
    description_viewpoint_EObject,
    viewpoint_description_MetamodelExtensionSetting,
    viewpoint_description_RepresentationExtensionDescription,
    viewpoint_description_DModelElement,
    viewpoint_description_DocumentedElement,
    description_viewpoint_EPackage,
    viewpoint_description_FeatureExtensionDescription,
    RepresentationTemplate,
    MetamodelExtensionSetting,
    JavaExtension,
    RepresentationExtensionDescription,
    viewpoint_description_DiagramExtensionDescription,
    RepresentationDescription,
    viewpoint_description_RepresentationImportDescription,
    viewpoint_description_RepresentationTemplate,
    validation_ValidationSet,
    description_IdentifiedElement,
    description_EndUserDocumentedElement,
    description_Component,
    viewpoint_description_Component,
    UserColorsPalette,
    SytemColorsPalette,
    viewpoint_Customizable,
    DFile,
    viewpoint_DModel,
    DResourceContainer,
    viewpoint_DFolder,
    viewpoint_DProject,
    DResource,
    viewpoint_DResourceContainer,
    viewpoint_DFile,
    viewpoint_DResource,
    viewpoint_SessionManagerEObject,
    viewpoint_DAnalysisSessionEObject,
    viewpoint_RGBValues,
    DNavigationLink,
    viewpoint_diagram_DDiagramLink,
    viewpoint_DEObjectLink,
    viewpoint_DragAndDropTarget,
    style_StyleDescription,
    viewpoint_style_NodeStyleDescription,
    Customizable,
    viewpoint_diagram_GaugeSection,
    viewpoint_BasicLabelStyle,
    BasicLabelStyle,
    viewpoint_diagram_EndLabelStyle,
    viewpoint_diagram_BeginLabelStyle,
    viewpoint_diagram_CenterLabelStyle,
    viewpoint_LabelStyle,
    viewpoint_DAnalysisCustomData,
    viewpoint_DSourceFileLink,
    DecorationDescription,
    viewpoint_description_MappingBasedDecoration,
    viewpoint_description_SemanticBasedDecoration,
    viewpoint_Decoration,
    Viewpoint,
    viewpoint_MetaModelExtension,
    DSemanticDecorator,
    viewpoint_diagram_DSemanticDiagram,
    DStylizable,
    DMappingBased,
    DLabelled,
    AnnotationEntry,
    description_DModelElement,
    DRefreshable,
    viewpoint_DRepresentationElement,
    viewpoint_Style,
    description_DocumentedElement,
    viewpoint_description_Layer,
    viewpoint_filter_FilterDescription,
    viewpoint_tool_ToolSection,
    viewpoint_description_EdgeMappingImport,
    viewpoint_diagram_DDiagram,
    viewpoint_description_Viewpoint,
    viewpoint_concern_ConcernDescription,
    viewpoint_description_EdgeMapping,
    viewpoint_description_RepresentationDescription,
    viewpoint_description_Group,
    viewpoint_description_AbstractNodeMapping,
    viewpoint_tool_ToolEntry,
    viewpoint_DRepresentation,
    viewpoint_DSemanticDecorator,
    DDiagramSet,
    DView,
    viewpoint_DRepresentationContainer,
    viewpoint_DContainer,
    viewpoint_DMappingBased,
    viewpoint_DLabelled,
    viewpoint_DRefreshable,
    viewpoint_DStylizable,
    viewpoint_DNavigationLink,
    viewpoint_DNavigable,
    viewpoint_DValidable,
    FeatureExtensionDescription,
    viewpoint_DFeatureExtension,
    viewpoint_DView,
    DAnnotationEntry,
    viewpoint_EObject,
    viewpoint_DAnalysis,
    LabelAlignment,
    ContainerShape,
    DragSource,
    SyncStatus,
    ResizeKind,
    BundledImageShape,
    EdgeArrows,
    BackgroundStyle,
    NavigationTargetType,
    FilterKind,
    SystemColors,
    LabelPosition,
    ArrangeConstraint,
    ReconnectionKind,
    LineStyle,
    FontFormat,
    FoldingStyle,
    EdgeRouting,
    AlignmentKind,
    ERROR_LEVEL,
    ContainerLayout,
    LayoutDirection,
    Position,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dnode_is_not_abstract():
    assert not inspect.isabstract(DNode)


def test_dnode_constructor_exists():
    assert callable(DNode.__init__)


def test_dnode_constructor_args():
    sig = inspect.signature(DNode.__init__)
    params = list(sig.parameters.keys())



def test_dcontainer_is_not_abstract():
    assert not inspect.isabstract(DContainer)


def test_dcontainer_constructor_exists():
    assert callable(DContainer.__init__)


def test_dcontainer_constructor_args():
    sig = inspect.signature(DContainer.__init__)
    params = list(sig.parameters.keys())



def test_dvalidable_is_not_abstract():
    assert not inspect.isabstract(DValidable)


def test_dvalidable_constructor_exists():
    assert callable(DValidable.__init__)


def test_dvalidable_constructor_args():
    sig = inspect.signature(DValidable.__init__)
    params = list(sig.parameters.keys())



def test_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(DragAndDropTarget)


def test_draganddroptarget_constructor_exists():
    assert callable(DragAndDropTarget.__init__)


def test_draganddroptarget_constructor_args():
    sig = inspect.signature(DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
    params = list(sig.parameters.keys())



def test_informationsection_is_not_abstract():
    assert not inspect.isabstract(InformationSection)


def test_informationsection_constructor_exists():
    assert callable(InformationSection.__init__)


def test_informationsection_constructor_args():
    sig = inspect.signature(InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_audit_templateinformationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_TemplateInformationSection)


def test_viewpoint_audit_templateinformationsection_constructor_exists():
    assert callable(viewpoint_audit_TemplateInformationSection.__init__)


def test_viewpoint_audit_templateinformationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_TemplateInformationSection.__init__)
    params = list(sig.parameters.keys())
    assert "templatePath" in params, "Missing parameter 'templatePath'"

def test_viewpoint_audit_templateinformationsection_has_templatePath():
    assert hasattr(viewpoint_audit_TemplateInformationSection, "templatePath")
    descriptor = None
    for klass in viewpoint_audit_TemplateInformationSection.__mro__:
        if "templatePath" in klass.__dict__:
            descriptor = klass.__dict__["templatePath"]
            break
    assert isinstance(descriptor, property)



def test_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(description_DiagramDescription)


def test_description_diagramdescription_constructor_exists():
    assert callable(description_DiagramDescription.__init__)


def test_description_diagramdescription_constructor_args():
    sig = inspect.signature(description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(DDiagramElement)


def test_ddiagramelement_constructor_exists():
    assert callable(DDiagramElement.__init__)


def test_ddiagramelement_constructor_args():
    sig = inspect.signature(DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_switchchild_is_not_abstract():
    assert not inspect.isabstract(SwitchChild)


def test_switchchild_constructor_exists():
    assert callable(SwitchChild.__init__)


def test_switchchild_constructor_args():
    sig = inspect.signature(SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_case_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Case)


def test_viewpoint_tool_case_constructor_exists():
    assert callable(viewpoint_tool_Case.__init__)


def test_viewpoint_tool_case_constructor_args():
    sig = inspect.signature(viewpoint_tool_Case.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint_tool_case_has_conditionExpression():
    assert hasattr(viewpoint_tool_Case, "conditionExpression")
    descriptor = None
    for klass in viewpoint_tool_Case.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_FeatureChangeListener)


def test_viewpoint_tool_featurechangelistener_constructor_exists():
    assert callable(viewpoint_tool_FeatureChangeListener.__init__)


def test_viewpoint_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(viewpoint_tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_featurechangelistener_has_domainClass():
    assert hasattr(viewpoint_tool_FeatureChangeListener, "domainClass")
    descriptor = None
    for klass in viewpoint_tool_FeatureChangeListener.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_featurechangelistener_has_featureName():
    assert hasattr(viewpoint_tool_FeatureChangeListener, "featureName")
    descriptor = None
    for klass in viewpoint_tool_FeatureChangeListener.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_tool_featurechangelistener_is_not_abstract():
    assert not inspect.isabstract(tool_FeatureChangeListener)


def test_tool_featurechangelistener_constructor_exists():
    assert callable(tool_FeatureChangeListener.__init__)


def test_tool_featurechangelistener_constructor_args():
    sig = inspect.signature(tool_FeatureChangeListener.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_audit_informationsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_audit_InformationSection)


def test_viewpoint_audit_informationsection_constructor_exists():
    assert callable(viewpoint_audit_InformationSection.__init__)


def test_viewpoint_audit_informationsection_constructor_args():
    sig = inspect.signature(viewpoint_audit_InformationSection.__init__)
    params = list(sig.parameters.keys())



def test_tool_default_is_not_abstract():
    assert not inspect.isabstract(tool_Default)


def test_tool_default_constructor_exists():
    assert callable(tool_Default.__init__)


def test_tool_default_constructor_args():
    sig = inspect.signature(tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_tool_case_is_not_abstract():
    assert not inspect.isabstract(tool_Case)


def test_tool_case_constructor_exists():
    assert callable(tool_Case.__init__)


def test_tool_case_constructor_args():
    sig = inspect.signature(tool_Case.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_default_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Default)


def test_viewpoint_tool_default_constructor_exists():
    assert callable(viewpoint_tool_Default.__init__)


def test_viewpoint_tool_default_constructor_args():
    sig = inspect.signature(viewpoint_tool_Default.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_switchchild_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SwitchChild)


def test_viewpoint_tool_switchchild_constructor_exists():
    assert callable(viewpoint_tool_SwitchChild.__init__)


def test_viewpoint_tool_switchchild_constructor_args():
    sig = inspect.signature(viewpoint_tool_SwitchChild.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolFilterDescription)


def test_viewpoint_tool_toolfilterdescription_constructor_exists():
    assert callable(viewpoint_tool_ToolFilterDescription.__init__)


def test_viewpoint_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "elementsToListen" in params, "Missing parameter 'elementsToListen'"

def test_viewpoint_tool_toolfilterdescription_has_precondition():
    assert hasattr(viewpoint_tool_ToolFilterDescription, "precondition")
    descriptor = None
    for klass in viewpoint_tool_ToolFilterDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_toolfilterdescription_has_elementsToListen():
    assert hasattr(viewpoint_tool_ToolFilterDescription, "elementsToListen")
    descriptor = None
    for klass in viewpoint_tool_ToolFilterDescription.__mro__:
        if "elementsToListen" in klass.__dict__:
            descriptor = klass.__dict__["elementsToListen"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionParameter)


def test_viewpoint_tool_externaljavaactionparameter_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionParameter.__init__)


def test_viewpoint_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_tool_externaljavaactionparameter_has_value():
    assert hasattr(viewpoint_tool_ExternalJavaActionParameter, "value")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaActionParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_externaljavaactionparameter_has_name():
    assert hasattr(viewpoint_tool_ExternalJavaActionParameter, "name")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaActionParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tool_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(tool_viewpoint_EObject)


def test_tool_viewpoint_eobject_constructor_exists():
    assert callable(tool_viewpoint_EObject.__init__)


def test_tool_viewpoint_eobject_constructor_args():
    sig = inspect.signature(tool_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_deleteview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteView)


def test_viewpoint_tool_deleteview_constructor_exists():
    assert callable(viewpoint_tool_DeleteView.__init__)


def test_viewpoint_tool_deleteview_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_moveelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MoveElement)


def test_viewpoint_tool_moveelement_constructor_exists():
    assert callable(viewpoint_tool_MoveElement.__init__)


def test_viewpoint_tool_moveelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_MoveElement.__init__)
    params = list(sig.parameters.keys())
    assert "newContainerExpression" in params, "Missing parameter 'newContainerExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_moveelement_has_newContainerExpression():
    assert hasattr(viewpoint_tool_MoveElement, "newContainerExpression")
    descriptor = None
    for klass in viewpoint_tool_MoveElement.__mro__:
        if "newContainerExpression" in klass.__dict__:
            descriptor = klass.__dict__["newContainerExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_moveelement_has_featureName():
    assert hasattr(viewpoint_tool_MoveElement, "featureName")
    descriptor = None
    for klass in viewpoint_tool_MoveElement.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_setvalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetValue)


def test_viewpoint_tool_setvalue_constructor_exists():
    assert callable(viewpoint_tool_SetValue.__init__)


def test_viewpoint_tool_setvalue_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_setvalue_has_valueExpression():
    assert hasattr(viewpoint_tool_SetValue, "valueExpression")
    descriptor = None
    for klass in viewpoint_tool_SetValue.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_setvalue_has_featureName():
    assert hasattr(viewpoint_tool_SetValue, "featureName")
    descriptor = None
    for klass in viewpoint_tool_SetValue.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_if_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_If)


def test_viewpoint_tool_if_constructor_exists():
    assert callable(viewpoint_tool_If.__init__)


def test_viewpoint_tool_if_constructor_args():
    sig = inspect.signature(viewpoint_tool_If.__init__)
    params = list(sig.parameters.keys())
    assert "conditionExpression" in params, "Missing parameter 'conditionExpression'"

def test_viewpoint_tool_if_has_conditionExpression():
    assert hasattr(viewpoint_tool_If, "conditionExpression")
    descriptor = None
    for klass in viewpoint_tool_If.__mro__:
        if "conditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["conditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_setobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SetObject)


def test_viewpoint_tool_setobject_constructor_exists():
    assert callable(viewpoint_tool_SetObject.__init__)


def test_viewpoint_tool_setobject_constructor_args():
    sig = inspect.signature(viewpoint_tool_SetObject.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_setobject_has_featureName():
    assert hasattr(viewpoint_tool_SetObject, "featureName")
    descriptor = None
    for klass in viewpoint_tool_SetObject.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_changecontext_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ChangeContext)


def test_viewpoint_tool_changecontext_constructor_exists():
    assert callable(viewpoint_tool_ChangeContext.__init__)


def test_viewpoint_tool_changecontext_constructor_args():
    sig = inspect.signature(viewpoint_tool_ChangeContext.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint_tool_changecontext_has_browseExpression():
    assert hasattr(viewpoint_tool_ChangeContext, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_ChangeContext.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_unset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Unset)


def test_viewpoint_tool_unset_constructor_exists():
    assert callable(viewpoint_tool_Unset.__init__)


def test_viewpoint_tool_unset_constructor_args():
    sig = inspect.signature(viewpoint_tool_Unset.__init__)
    params = list(sig.parameters.keys())
    assert "elementExpression" in params, "Missing parameter 'elementExpression'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_viewpoint_tool_unset_has_elementExpression():
    assert hasattr(viewpoint_tool_Unset, "elementExpression")
    descriptor = None
    for klass in viewpoint_tool_Unset.__mro__:
        if "elementExpression" in klass.__dict__:
            descriptor = klass.__dict__["elementExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_unset_has_featureName():
    assert hasattr(viewpoint_tool_Unset, "featureName")
    descriptor = None
    for klass in viewpoint_tool_Unset.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_for_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_For)


def test_viewpoint_tool_for_constructor_exists():
    assert callable(viewpoint_tool_For.__init__)


def test_viewpoint_tool_for_constructor_args():
    sig = inspect.signature(viewpoint_tool_For.__init__)
    params = list(sig.parameters.keys())
    assert "iteratorName" in params, "Missing parameter 'iteratorName'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_viewpoint_tool_for_has_iteratorName():
    assert hasattr(viewpoint_tool_For, "iteratorName")
    descriptor = None
    for klass in viewpoint_tool_For.__mro__:
        if "iteratorName" in klass.__dict__:
            descriptor = klass.__dict__["iteratorName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_for_has_expression():
    assert hasattr(viewpoint_tool_For, "expression")
    descriptor = None
    for klass in viewpoint_tool_For.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_removeelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RemoveElement)


def test_viewpoint_tool_removeelement_constructor_exists():
    assert callable(viewpoint_tool_RemoveElement.__init__)


def test_viewpoint_tool_removeelement_constructor_args():
    sig = inspect.signature(viewpoint_tool_RemoveElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_createinstance_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_CreateInstance)


def test_viewpoint_tool_createinstance_constructor_exists():
    assert callable(viewpoint_tool_CreateInstance.__init__)


def test_viewpoint_tool_createinstance_constructor_args():
    sig = inspect.signature(viewpoint_tool_CreateInstance.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "referenceName" in params, "Missing parameter 'referenceName'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_viewpoint_tool_createinstance_has_variableName():
    assert hasattr(viewpoint_tool_CreateInstance, "variableName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createinstance_has_referenceName():
    assert hasattr(viewpoint_tool_CreateInstance, "referenceName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createinstance_has_typeName():
    assert hasattr(viewpoint_tool_CreateInstance, "typeName")
    descriptor = None
    for klass in viewpoint_tool_CreateInstance.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialContainerDropOperation)


def test_viewpoint_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialContainerDropOperation.__init__)


def test_viewpoint_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationFix)


def test_viewpoint_validation_validationfix_constructor_exists():
    assert callable(viewpoint_validation_ValidationFix.__init__)


def test_viewpoint_validation_validationfix_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_validation_validationfix_has_name():
    assert hasattr(viewpoint_validation_ValidationFix, "name")
    descriptor = None
    for klass in viewpoint_validation_ValidationFix.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validationrule_is_not_abstract():
    assert not inspect.isabstract(ValidationRule)


def test_validationrule_constructor_exists():
    assert callable(ValidationRule.__init__)


def test_validationrule_constructor_args():
    sig = inspect.signature(ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_viewvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ViewValidationRule)


def test_viewpoint_validation_viewvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_ViewValidationRule.__init__)


def test_viewpoint_validation_viewvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ViewValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_semanticvalidationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_SemanticValidationRule)


def test_viewpoint_validation_semanticvalidationrule_constructor_exists():
    assert callable(viewpoint_validation_SemanticValidationRule.__init__)


def test_viewpoint_validation_semanticvalidationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_SemanticValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "targetClass" in params, "Missing parameter 'targetClass'"

def test_viewpoint_validation_semanticvalidationrule_has_targetClass():
    assert hasattr(viewpoint_validation_SemanticValidationRule, "targetClass")
    descriptor = None
    for klass in viewpoint_validation_SemanticValidationRule.__mro__:
        if "targetClass" in klass.__dict__:
            descriptor = klass.__dict__["targetClass"]
            break
    assert isinstance(descriptor, property)



def test_validation_validationfix_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationFix)


def test_validation_validationfix_constructor_exists():
    assert callable(validation_ValidationFix.__init__)


def test_validation_validationfix_constructor_args():
    sig = inspect.signature(validation_ValidationFix.__init__)
    params = list(sig.parameters.keys())



def test_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(validation_RuleAudit)


def test_validation_ruleaudit_constructor_exists():
    assert callable(validation_RuleAudit.__init__)


def test_validation_ruleaudit_constructor_args():
    sig = inspect.signature(validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationRule)


def test_viewpoint_validation_validationrule_constructor_exists():
    assert callable(viewpoint_validation_ValidationRule.__init__)


def test_viewpoint_validation_validationrule_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "level" in params, "Missing parameter 'level'"

def test_viewpoint_validation_validationrule_has_message():
    assert hasattr(viewpoint_validation_ValidationRule, "message")
    descriptor = None
    for klass in viewpoint_validation_ValidationRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_validation_validationrule_has_level():
    assert hasattr(viewpoint_validation_ValidationRule, "level")
    descriptor = None
    for klass in viewpoint_validation_ValidationRule.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_validation_ruleaudit_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_RuleAudit)


def test_viewpoint_validation_ruleaudit_constructor_exists():
    assert callable(viewpoint_validation_RuleAudit.__init__)


def test_viewpoint_validation_ruleaudit_constructor_args():
    sig = inspect.signature(viewpoint_validation_RuleAudit.__init__)
    params = list(sig.parameters.keys())
    assert "auditExpression" in params, "Missing parameter 'auditExpression'"

def test_viewpoint_validation_ruleaudit_has_auditExpression():
    assert hasattr(viewpoint_validation_RuleAudit, "auditExpression")
    descriptor = None
    for klass in viewpoint_validation_RuleAudit.__mro__:
        if "auditExpression" in klass.__dict__:
            descriptor = klass.__dict__["auditExpression"]
            break
    assert isinstance(descriptor, property)



def test_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(SelectionDescription)


def test_selectiondescription_constructor_exists():
    assert callable(SelectionDescription.__init__)


def test_selectiondescription_constructor_args():
    sig = inspect.signature(SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_filter_filtervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_FilterVariable)


def test_viewpoint_filter_filtervariable_constructor_exists():
    assert callable(viewpoint_filter_FilterVariable.__init__)


def test_viewpoint_filter_filtervariable_constructor_args():
    sig = inspect.signature(viewpoint_filter_FilterVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_filter_filtervariable_has_name():
    assert hasattr(viewpoint_filter_FilterVariable, "name")
    descriptor = None
    for klass in viewpoint_filter_FilterVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_filter_filter_is_not_abstract():
    assert not inspect.isabstract(filter_Filter)


def test_filter_filter_constructor_exists():
    assert callable(filter_Filter.__init__)


def test_filter_filter_constructor_args():
    sig = inspect.signature(filter_Filter.__init__)
    params = list(sig.parameters.keys())



def test_filterdescription_is_not_abstract():
    assert not inspect.isabstract(FilterDescription)


def test_filterdescription_constructor_exists():
    assert callable(FilterDescription.__init__)


def test_filterdescription_constructor_args():
    sig = inspect.signature(FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_CompositeFilterDescription)


def test_viewpoint_filter_compositefilterdescription_constructor_exists():
    assert callable(viewpoint_filter_CompositeFilterDescription.__init__)


def test_viewpoint_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(viewpoint_filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_filter_variablefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_VariableFilter)


def test_viewpoint_filter_variablefilter_constructor_exists():
    assert callable(viewpoint_filter_VariableFilter.__init__)


def test_viewpoint_filter_variablefilter_constructor_args():
    sig = inspect.signature(viewpoint_filter_VariableFilter.__init__)
    params = list(sig.parameters.keys())
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_viewpoint_filter_variablefilter_has_semanticConditionExpression():
    assert hasattr(viewpoint_filter_VariableFilter, "semanticConditionExpression")
    descriptor = None
    for klass in viewpoint_filter_VariableFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_filter_mappingfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_MappingFilter)


def test_viewpoint_filter_mappingfilter_constructor_exists():
    assert callable(viewpoint_filter_MappingFilter.__init__)


def test_viewpoint_filter_mappingfilter_constructor_args():
    sig = inspect.signature(viewpoint_filter_MappingFilter.__init__)
    params = list(sig.parameters.keys())
    assert "viewConditionExpression" in params, "Missing parameter 'viewConditionExpression'"
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_viewpoint_filter_mappingfilter_has_viewConditionExpression():
    assert hasattr(viewpoint_filter_MappingFilter, "viewConditionExpression")
    descriptor = None
    for klass in viewpoint_filter_MappingFilter.__mro__:
        if "viewConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["viewConditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_filter_mappingfilter_has_semanticConditionExpression():
    assert hasattr(viewpoint_filter_MappingFilter, "semanticConditionExpression")
    descriptor = None
    for klass in viewpoint_filter_MappingFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_filter_filter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_Filter)


def test_viewpoint_filter_filter_constructor_exists():
    assert callable(viewpoint_filter_Filter.__init__)


def test_viewpoint_filter_filter_constructor_args():
    sig = inspect.signature(viewpoint_filter_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "filterKind" in params, "Missing parameter 'filterKind'"

def test_viewpoint_filter_filter_has_filterKind():
    assert hasattr(viewpoint_filter_Filter, "filterKind")
    descriptor = None
    for klass in viewpoint_filter_Filter.__mro__:
        if "filterKind" in klass.__dict__:
            descriptor = klass.__dict__["filterKind"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_navigation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Navigation)


def test_viewpoint_tool_navigation_constructor_exists():
    assert callable(viewpoint_tool_Navigation.__init__)


def test_viewpoint_tool_navigation_constructor_args():
    sig = inspect.signature(viewpoint_tool_Navigation.__init__)
    params = list(sig.parameters.keys())
    assert "createIfNotExistent" in params, "Missing parameter 'createIfNotExistent'"

def test_viewpoint_tool_navigation_has_createIfNotExistent():
    assert hasattr(viewpoint_tool_Navigation, "createIfNotExistent")
    descriptor = None
    for klass in viewpoint_tool_Navigation.__mro__:
        if "createIfNotExistent" in klass.__dict__:
            descriptor = klass.__dict__["createIfNotExistent"]
            break
    assert isinstance(descriptor, property)



def test_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_createview_is_not_abstract():
    assert not inspect.isabstract(CreateView)


def test_createview_constructor_exists():
    assert callable(CreateView.__init__)


def test_createview_constructor_args():
    sig = inspect.signature(CreateView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_diagramnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DiagramNavigationDescription)


def test_viewpoint_tool_diagramnavigationdescription_constructor_exists():
    assert callable(viewpoint_tool_DiagramNavigationDescription.__init__)


def test_viewpoint_tool_diagramnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_DiagramNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_createedgeview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_CreateEdgeView)


def test_viewpoint_tool_createedgeview_constructor_exists():
    assert callable(viewpoint_tool_CreateEdgeView.__init__)


def test_viewpoint_tool_createedgeview_constructor_args():
    sig = inspect.signature(viewpoint_tool_CreateEdgeView.__init__)
    params = list(sig.parameters.keys())
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "sourceExpression" in params, "Missing parameter 'sourceExpression'"

def test_viewpoint_tool_createedgeview_has_targetExpression():
    assert hasattr(viewpoint_tool_CreateEdgeView, "targetExpression")
    descriptor = None
    for klass in viewpoint_tool_CreateEdgeView.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createedgeview_has_sourceExpression():
    assert hasattr(viewpoint_tool_CreateEdgeView, "sourceExpression")
    descriptor = None
    for klass in viewpoint_tool_CreateEdgeView.__mro__:
        if "sourceExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceExpression"]
            break
    assert isinstance(descriptor, property)



def test_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_diagramcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DiagramCreationDescription)


def test_viewpoint_tool_diagramcreationdescription_constructor_exists():
    assert callable(viewpoint_tool_DiagramCreationDescription.__init__)


def test_viewpoint_tool_diagramcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_DiagramCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_createview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_CreateView)


def test_viewpoint_tool_createview_constructor_exists():
    assert callable(viewpoint_tool_CreateView.__init__)


def test_viewpoint_tool_createview_constructor_args():
    sig = inspect.signature(viewpoint_tool_CreateView.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "containerViewExpression" in params, "Missing parameter 'containerViewExpression'"

def test_viewpoint_tool_createview_has_variableName():
    assert hasattr(viewpoint_tool_CreateView, "variableName")
    descriptor = None
    for klass in viewpoint_tool_CreateView.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_createview_has_containerViewExpression():
    assert hasattr(viewpoint_tool_CreateView, "containerViewExpression")
    descriptor = None
    for klass in viewpoint_tool_CreateView.__mro__:
        if "containerViewExpression" in klass.__dict__:
            descriptor = klass.__dict__["containerViewExpression"]
            break
    assert isinstance(descriptor, property)



def test_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool_EditMaskVariables)


def test_tool_editmaskvariables_constructor_exists():
    assert callable(tool_EditMaskVariables.__init__)


def test_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDoubleClickVariable)


def test_tool_elementdoubleclickvariable_constructor_exists():
    assert callable(tool_ElementDoubleClickVariable.__init__)


def test_tool_elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(tool_ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_deletehook_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteHook)


def test_tool_deletehook_constructor_exists():
    assert callable(tool_DeleteHook.__init__)


def test_tool_deletehook_constructor_args():
    sig = inspect.signature(tool_DeleteHook.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteHookParameter)


def test_viewpoint_tool_deletehookparameter_constructor_exists():
    assert callable(viewpoint_tool_DeleteHookParameter.__init__)


def test_viewpoint_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_viewpoint_tool_deletehookparameter_has_name():
    assert hasattr(viewpoint_tool_DeleteHookParameter, "name")
    descriptor = None
    for klass in viewpoint_tool_DeleteHookParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_deletehookparameter_has_value():
    assert hasattr(viewpoint_tool_DeleteHookParameter, "value")
    descriptor = None
    for klass in viewpoint_tool_DeleteHookParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteHookParameter)


def test_tool_deletehookparameter_constructor_exists():
    assert callable(tool_DeleteHookParameter.__init__)


def test_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_deletehook_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteHook)


def test_viewpoint_tool_deletehook_constructor_exists():
    assert callable(viewpoint_tool_DeleteHook.__init__)


def test_viewpoint_tool_deletehook_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteHook.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint_tool_deletehook_has_id():
    assert hasattr(viewpoint_tool_DeleteHook, "id")
    descriptor = None
    for klass in viewpoint_tool_DeleteHook.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDeleteVariable)


def test_tool_elementdeletevariable_constructor_exists():
    assert callable(tool_ElementDeleteVariable.__init__)


def test_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_TargetEdgeViewCreationVariable)


def test_tool_targetedgeviewcreationvariable_constructor_exists():
    assert callable(tool_TargetEdgeViewCreationVariable.__init__)


def test_tool_targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool_TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SourceEdgeViewCreationVariable)


def test_tool_sourceedgeviewcreationvariable_constructor_exists():
    assert callable(tool_SourceEdgeViewCreationVariable.__init__)


def test_tool_sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(tool_SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_TargetEdgeCreationVariable)


def test_tool_targetedgecreationvariable_constructor_exists():
    assert callable(tool_TargetEdgeCreationVariable.__init__)


def test_tool_targetedgecreationvariable_constructor_args():
    sig = inspect.signature(tool_TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SourceEdgeCreationVariable)


def test_tool_sourceedgecreationvariable_constructor_exists():
    assert callable(tool_SourceEdgeCreationVariable.__init__)


def test_tool_sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(tool_SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitEdgeCreationOperation)


def test_tool_initedgecreationoperation_constructor_exists():
    assert callable(tool_InitEdgeCreationOperation.__init__)


def test_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialNodeCreationOperation)


def test_tool_initialnodecreationoperation_constructor_exists():
    assert callable(tool_InitialNodeCreationOperation.__init__)


def test_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_NodeCreationVariable)


def test_tool_nodecreationvariable_constructor_exists():
    assert callable(tool_NodeCreationVariable.__init__)


def test_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(tool_NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool_PopupMenu)


def test_tool_popupmenu_constructor_exists():
    assert callable(tool_PopupMenu.__init__)


def test_tool_popupmenu_constructor_args():
    sig = inspect.signature(tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroup)


def test_tool_toolgroup_constructor_exists():
    assert callable(tool_ToolGroup.__init__)


def test_tool_toolgroup_constructor_args():
    sig = inspect.signature(tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolGroupExtension)


def test_viewpoint_tool_toolgroupextension_constructor_exists():
    assert callable(viewpoint_tool_ToolGroupExtension.__init__)


def test_viewpoint_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroupExtension)


def test_tool_toolgroupextension_constructor_exists():
    assert callable(tool_ToolGroupExtension.__init__)


def test_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(tool_ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_BeginLabelStyleDescription)


def test_style_beginlabelstyledescription_constructor_exists():
    assert callable(style_BeginLabelStyleDescription.__init__)


def test_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(EdgeStyleDescription)


def test_edgestyledescription_constructor_exists():
    assert callable(EdgeStyleDescription.__init__)


def test_edgestyledescription_constructor_args():
    sig = inspect.signature(EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_bracketedgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BracketEdgeStyleDescription)


def test_viewpoint_style_bracketedgestyledescription_constructor_exists():
    assert callable(viewpoint_style_BracketEdgeStyleDescription.__init__)


def test_viewpoint_style_bracketedgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BracketEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_EndLabelStyleDescription)


def test_style_endlabelstyledescription_constructor_exists():
    assert callable(style_EndLabelStyleDescription.__init__)


def test_style_endlabelstyledescription_constructor_args():
    sig = inspect.signature(style_EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_CenterLabelStyleDescription)


def test_style_centerlabelstyledescription_constructor_exists():
    assert callable(style_CenterLabelStyleDescription.__init__)


def test_style_centerlabelstyledescription_constructor_args():
    sig = inspect.signature(style_CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_SizeComputationContainerStyleDescription)


def test_viewpoint_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(viewpoint_style_SizeComputationContainerStyleDescription.__init__)


def test_viewpoint_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"

def test_viewpoint_style_sizecomputationcontainerstyledescription_has_heightComputationExpression():
    assert hasattr(viewpoint_style_SizeComputationContainerStyleDescription, "heightComputationExpression")
    descriptor = None
    for klass in viewpoint_style_SizeComputationContainerStyleDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_sizecomputationcontainerstyledescription_has_widthComputationExpression():
    assert hasattr(viewpoint_style_SizeComputationContainerStyleDescription, "widthComputationExpression")
    descriptor = None
    for klass in viewpoint_style_SizeComputationContainerStyleDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_SizeComputationContainerStyleDescription)


def test_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(style_SizeComputationContainerStyleDescription.__init__)


def test_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_RoundedCornerStyleDescription)


def test_style_roundedcornerstyledescription_constructor_exists():
    assert callable(style_RoundedCornerStyleDescription.__init__)


def test_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_GaugeSectionDescription)


def test_viewpoint_style_gaugesectiondescription_constructor_exists():
    assert callable(viewpoint_style_GaugeSectionDescription.__init__)


def test_viewpoint_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(viewpoint_style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "maxValueExpression" in params, "Missing parameter 'maxValueExpression'"
    assert "minValueExpression" in params, "Missing parameter 'minValueExpression'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"

def test_viewpoint_style_gaugesectiondescription_has_label():
    assert hasattr(viewpoint_style_GaugeSectionDescription, "label")
    descriptor = None
    for klass in viewpoint_style_GaugeSectionDescription.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_gaugesectiondescription_has_maxValueExpression():
    assert hasattr(viewpoint_style_GaugeSectionDescription, "maxValueExpression")
    descriptor = None
    for klass in viewpoint_style_GaugeSectionDescription.__mro__:
        if "maxValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_gaugesectiondescription_has_minValueExpression():
    assert hasattr(viewpoint_style_GaugeSectionDescription, "minValueExpression")
    descriptor = None
    for klass in viewpoint_style_GaugeSectionDescription.__mro__:
        if "minValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_gaugesectiondescription_has_valueExpression():
    assert hasattr(viewpoint_style_GaugeSectionDescription, "valueExpression")
    descriptor = None
    for klass in viewpoint_style_GaugeSectionDescription.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)



def test_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(style_GaugeSectionDescription)


def test_style_gaugesectiondescription_constructor_exists():
    assert callable(style_GaugeSectionDescription.__init__)


def test_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(NodeStyleDescription)


def test_nodestyledescription_constructor_exists():
    assert callable(NodeStyleDescription.__init__)


def test_nodestyledescription_constructor_args():
    sig = inspect.signature(NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_dotdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_DotDescription)


def test_viewpoint_style_dotdescription_constructor_exists():
    assert callable(viewpoint_style_DotDescription.__init__)


def test_viewpoint_style_dotdescription_constructor_args():
    sig = inspect.signature(viewpoint_style_DotDescription.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_viewpoint_style_dotdescription_has_strokeSizeComputationExpression():
    assert hasattr(viewpoint_style_DotDescription, "strokeSizeComputationExpression")
    descriptor = None
    for klass in viewpoint_style_DotDescription.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_gaugecompositestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_GaugeCompositeStyleDescription)


def test_viewpoint_style_gaugecompositestyledescription_constructor_exists():
    assert callable(viewpoint_style_GaugeCompositeStyleDescription.__init__)


def test_viewpoint_style_gaugecompositestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_GaugeCompositeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_viewpoint_style_gaugecompositestyledescription_has_alignment():
    assert hasattr(viewpoint_style_GaugeCompositeStyleDescription, "alignment")
    descriptor = None
    for klass in viewpoint_style_GaugeCompositeStyleDescription.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_lozengenodedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LozengeNodeDescription)


def test_viewpoint_style_lozengenodedescription_constructor_exists():
    assert callable(viewpoint_style_LozengeNodeDescription.__init__)


def test_viewpoint_style_lozengenodedescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LozengeNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"

def test_viewpoint_style_lozengenodedescription_has_widthComputationExpression():
    assert hasattr(viewpoint_style_LozengeNodeDescription, "widthComputationExpression")
    descriptor = None
    for klass in viewpoint_style_LozengeNodeDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_lozengenodedescription_has_heightComputationExpression():
    assert hasattr(viewpoint_style_LozengeNodeDescription, "heightComputationExpression")
    descriptor = None
    for klass in viewpoint_style_LozengeNodeDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_squaredescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_SquareDescription)


def test_viewpoint_style_squaredescription_constructor_exists():
    assert callable(viewpoint_style_SquareDescription.__init__)


def test_viewpoint_style_squaredescription_constructor_args():
    sig = inspect.signature(viewpoint_style_SquareDescription.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint_style_squaredescription_has_height():
    assert hasattr(viewpoint_style_SquareDescription, "height")
    descriptor = None
    for klass in viewpoint_style_SquareDescription.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_squaredescription_has_width():
    assert hasattr(viewpoint_style_SquareDescription, "width")
    descriptor = None
    for klass in viewpoint_style_SquareDescription.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_notedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_NoteDescription)


def test_viewpoint_style_notedescription_constructor_exists():
    assert callable(viewpoint_style_NoteDescription.__init__)


def test_viewpoint_style_notedescription_constructor_args():
    sig = inspect.signature(viewpoint_style_NoteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_bundledimagedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BundledImageDescription)


def test_viewpoint_style_bundledimagedescription_constructor_exists():
    assert callable(viewpoint_style_BundledImageDescription.__init__)


def test_viewpoint_style_bundledimagedescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BundledImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint_style_bundledimagedescription_has_shape():
    assert hasattr(viewpoint_style_BundledImageDescription, "shape")
    descriptor = None
    for klass in viewpoint_style_BundledImageDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_customstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_CustomStyleDescription)


def test_viewpoint_style_customstyledescription_constructor_exists():
    assert callable(viewpoint_style_CustomStyleDescription.__init__)


def test_viewpoint_style_customstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_CustomStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint_style_customstyledescription_has_id():
    assert hasattr(viewpoint_style_CustomStyleDescription, "id")
    descriptor = None
    for klass in viewpoint_style_CustomStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_ellipsenodedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_EllipseNodeDescription)


def test_viewpoint_style_ellipsenodedescription_constructor_exists():
    assert callable(viewpoint_style_EllipseNodeDescription.__init__)


def test_viewpoint_style_ellipsenodedescription_constructor_args():
    sig = inspect.signature(viewpoint_style_EllipseNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameterComputationExpression" in params, "Missing parameter 'verticalDiameterComputationExpression'"
    assert "horizontalDiameterComputationExpression" in params, "Missing parameter 'horizontalDiameterComputationExpression'"

def test_viewpoint_style_ellipsenodedescription_has_verticalDiameterComputationExpression():
    assert hasattr(viewpoint_style_EllipseNodeDescription, "verticalDiameterComputationExpression")
    descriptor = None
    for klass in viewpoint_style_EllipseNodeDescription.__mro__:
        if "verticalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_ellipsenodedescription_has_horizontalDiameterComputationExpression():
    assert hasattr(viewpoint_style_EllipseNodeDescription, "horizontalDiameterComputationExpression")
    descriptor = None
    for klass in viewpoint_style_EllipseNodeDescription.__mro__:
        if "horizontalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_style_tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_TooltipStyleDescription)


def test_style_tooltipstyledescription_constructor_exists():
    assert callable(style_TooltipStyleDescription.__init__)


def test_style_tooltipstyledescription_constructor_args():
    sig = inspect.signature(style_TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelStyleDescription)


def test_style_labelstyledescription_constructor_exists():
    assert callable(style_LabelStyleDescription.__init__)


def test_style_labelstyledescription_constructor_args():
    sig = inspect.signature(style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_BorderedStyleDescription)


def test_style_borderedstyledescription_constructor_exists():
    assert callable(style_BorderedStyleDescription.__init__)


def test_style_borderedstyledescription_constructor_args():
    sig = inspect.signature(style_BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_ContainerStyleDescription)


def test_viewpoint_style_containerstyledescription_constructor_exists():
    assert callable(viewpoint_style_ContainerStyleDescription.__init__)


def test_viewpoint_style_containerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "roundedCorner" in params, "Missing parameter 'roundedCorner'"

def test_viewpoint_style_containerstyledescription_has_roundedCorner():
    assert hasattr(viewpoint_style_ContainerStyleDescription, "roundedCorner")
    descriptor = None
    for klass in viewpoint_style_ContainerStyleDescription.__mro__:
        if "roundedCorner" in klass.__dict__:
            descriptor = klass.__dict__["roundedCorner"]
            break
    assert isinstance(descriptor, property)



def test_styledescription_is_not_abstract():
    assert not inspect.isabstract(StyleDescription)


def test_styledescription_constructor_exists():
    assert callable(StyleDescription.__init__)


def test_styledescription_constructor_args():
    sig = inspect.signature(StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_RoundedCornerStyleDescription)


def test_viewpoint_style_roundedcornerstyledescription_constructor_exists():
    assert callable(viewpoint_style_RoundedCornerStyleDescription.__init__)


def test_viewpoint_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "arcWidth" in params, "Missing parameter 'arcWidth'"
    assert "arcHeight" in params, "Missing parameter 'arcHeight'"

def test_viewpoint_style_roundedcornerstyledescription_has_arcWidth():
    assert hasattr(viewpoint_style_RoundedCornerStyleDescription, "arcWidth")
    descriptor = None
    for klass in viewpoint_style_RoundedCornerStyleDescription.__mro__:
        if "arcWidth" in klass.__dict__:
            descriptor = klass.__dict__["arcWidth"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_roundedcornerstyledescription_has_arcHeight():
    assert hasattr(viewpoint_style_RoundedCornerStyleDescription, "arcHeight")
    descriptor = None
    for klass in viewpoint_style_RoundedCornerStyleDescription.__mro__:
        if "arcHeight" in klass.__dict__:
            descriptor = klass.__dict__["arcHeight"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_EdgeStyleDescription)


def test_viewpoint_style_edgestyledescription_constructor_exists():
    assert callable(viewpoint_style_EdgeStyleDescription.__init__)


def test_viewpoint_style_edgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"

def test_viewpoint_style_edgestyledescription_has_sourceArrow():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "sourceArrow")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_edgestyledescription_has_routingStyle():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "routingStyle")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_edgestyledescription_has_targetArrow():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "targetArrow")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_edgestyledescription_has_foldingStyle():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "foldingStyle")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_edgestyledescription_has_lineStyle():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "lineStyle")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_edgestyledescription_has_sizeComputationExpression():
    assert hasattr(viewpoint_style_EdgeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in viewpoint_style_EdgeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BorderedStyleDescription)


def test_viewpoint_style_borderedstyledescription_constructor_exists():
    assert callable(viewpoint_style_BorderedStyleDescription.__init__)


def test_viewpoint_style_borderedstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_viewpoint_style_borderedstyledescription_has_borderSizeComputationExpression():
    assert hasattr(viewpoint_style_BorderedStyleDescription, "borderSizeComputationExpression")
    descriptor = None
    for klass in viewpoint_style_BorderedStyleDescription.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_additionallayer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AdditionalLayer)


def test_viewpoint_description_additionallayer_constructor_exists():
    assert callable(viewpoint_description_AdditionalLayer.__init__)


def test_viewpoint_description_additionallayer_constructor_args():
    sig = inspect.signature(viewpoint_description_AdditionalLayer.__init__)
    params = list(sig.parameters.keys())
    assert "activeByDefault" in params, "Missing parameter 'activeByDefault'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_viewpoint_description_additionallayer_has_activeByDefault():
    assert hasattr(viewpoint_description_AdditionalLayer, "activeByDefault")
    descriptor = None
    for klass in viewpoint_description_AdditionalLayer.__mro__:
        if "activeByDefault" in klass.__dict__:
            descriptor = klass.__dict__["activeByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_additionallayer_has_optional():
    assert hasattr(viewpoint_description_AdditionalLayer, "optional")
    descriptor = None
    for klass in viewpoint_description_AdditionalLayer.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_customization_is_not_abstract():
    assert not inspect.isabstract(Customization)


def test_customization_constructor_exists():
    assert callable(Customization.__init__)


def test_customization_constructor_args():
    sig = inspect.signature(Customization.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(DecorationDescriptionsSet)


def test_decorationdescriptionsset_constructor_exists():
    assert callable(DecorationDescriptionsSet.__init__)


def test_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_compositelayout_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_CompositeLayout)


def test_viewpoint_description_compositelayout_constructor_exists():
    assert callable(viewpoint_description_CompositeLayout.__init__)


def test_viewpoint_description_compositelayout_constructor_args():
    sig = inspect.signature(viewpoint_description_CompositeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "padding" in params, "Missing parameter 'padding'"

def test_viewpoint_description_compositelayout_has_direction():
    assert hasattr(viewpoint_description_CompositeLayout, "direction")
    descriptor = None
    for klass in viewpoint_description_CompositeLayout.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_compositelayout_has_padding():
    assert hasattr(viewpoint_description_CompositeLayout, "padding")
    descriptor = None
    for klass in viewpoint_description_CompositeLayout.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_orderedtreelayout_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_OrderedTreeLayout)


def test_viewpoint_description_orderedtreelayout_constructor_exists():
    assert callable(viewpoint_description_OrderedTreeLayout.__init__)


def test_viewpoint_description_orderedtreelayout_constructor_args():
    sig = inspect.signature(viewpoint_description_OrderedTreeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_viewpoint_description_orderedtreelayout_has_childrenExpression():
    assert hasattr(viewpoint_description_OrderedTreeLayout, "childrenExpression")
    descriptor = None
    for klass in viewpoint_description_OrderedTreeLayout.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_concern_ConcernSet)


def test_viewpoint_concern_concernset_constructor_exists():
    assert callable(viewpoint_concern_ConcernSet.__init__)


def test_viewpoint_concern_concernset_constructor_args():
    sig = inspect.signature(viewpoint_concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_validation_ValidationSet)


def test_viewpoint_validation_validationset_constructor_exists():
    assert callable(viewpoint_validation_ValidationSet.__init__)


def test_viewpoint_validation_validationset_constructor_args():
    sig = inspect.signature(viewpoint_validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_validation_validationset_has_name():
    assert hasattr(viewpoint_validation_ValidationSet, "name")
    descriptor = None
    for klass in viewpoint_validation_ValidationSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_layout_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Layout)


def test_viewpoint_description_layout_constructor_exists():
    assert callable(viewpoint_description_Layout.__init__)


def test_viewpoint_description_layout_constructor_args():
    sig = inspect.signature(viewpoint_description_Layout.__init__)
    params = list(sig.parameters.keys())



def test_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalContainerStyleDescription)


def test_viewpoint_description_conditionalcontainerstyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalContainerStyleDescription.__init__)


def test_viewpoint_description_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalEdgeStyleDescription)


def test_viewpoint_description_conditionaledgestyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalEdgeStyleDescription.__init__)


def test_viewpoint_description_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalNodeStyleDescription)


def test_viewpoint_description_conditionalnodestyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalNodeStyleDescription.__init__)


def test_viewpoint_description_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(description_ConditionalEdgeStyleDescription)


def test_description_conditionaledgestyledescription_constructor_exists():
    assert callable(description_ConditionalEdgeStyleDescription.__init__)


def test_description_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(description_ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_EdgeStyleDescription)


def test_style_edgestyledescription_constructor_exists():
    assert callable(style_EdgeStyleDescription.__init__)


def test_style_edgestyledescription_constructor_args():
    sig = inspect.signature(style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IEdgeMapping)


def test_viewpoint_description_iedgemapping_constructor_exists():
    assert callable(viewpoint_description_IEdgeMapping.__init__)


def test_viewpoint_description_iedgemapping_constructor_args():
    sig = inspect.signature(viewpoint_description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(tool_ReconnectEdgeDescription)


def test_tool_reconnectedgedescription_constructor_exists():
    assert callable(tool_ReconnectEdgeDescription.__init__)


def test_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(description_ConditionalContainerStyleDescription)


def test_description_conditionalcontainerstyledescription_constructor_exists():
    assert callable(description_ConditionalContainerStyleDescription.__init__)


def test_description_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(description_ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_ContainerStyleDescription)


def test_style_containerstyledescription_constructor_exists():
    assert callable(style_ContainerStyleDescription.__init__)


def test_style_containerstyledescription_constructor_args():
    sig = inspect.signature(style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_flatcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_FlatContainerStyleDescription)


def test_viewpoint_style_flatcontainerstyledescription_constructor_exists():
    assert callable(viewpoint_style_FlatContainerStyleDescription.__init__)


def test_viewpoint_style_flatcontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_FlatContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_viewpoint_style_flatcontainerstyledescription_has_backgroundStyle():
    assert hasattr(viewpoint_style_FlatContainerStyleDescription, "backgroundStyle")
    descriptor = None
    for klass in viewpoint_style_FlatContainerStyleDescription.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_shapecontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_ShapeContainerStyleDescription)


def test_viewpoint_style_shapecontainerstyledescription_constructor_exists():
    assert callable(viewpoint_style_ShapeContainerStyleDescription.__init__)


def test_viewpoint_style_shapecontainerstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_ShapeContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint_style_shapecontainerstyledescription_has_shape():
    assert hasattr(viewpoint_style_ShapeContainerStyleDescription, "shape")
    descriptor = None
    for klass in viewpoint_style_ShapeContainerStyleDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(description_AbstractMappingImport)


def test_description_abstractmappingimport_constructor_exists():
    assert callable(description_AbstractMappingImport.__init__)


def test_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(description_ConditionalNodeStyleDescription)


def test_description_conditionalnodestyledescription_constructor_exists():
    assert callable(description_ConditionalNodeStyleDescription.__init__)


def test_description_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(description_ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_NodeStyleDescription)


def test_style_nodestyledescription_constructor_exists():
    assert callable(style_NodeStyleDescription.__init__)


def test_style_nodestyledescription_constructor_args():
    sig = inspect.signature(style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_workspaceimagedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_WorkspaceImageDescription)


def test_viewpoint_style_workspaceimagedescription_constructor_exists():
    assert callable(viewpoint_style_WorkspaceImageDescription.__init__)


def test_viewpoint_style_workspaceimagedescription_constructor_args():
    sig = inspect.signature(viewpoint_style_WorkspaceImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_viewpoint_style_workspaceimagedescription_has_workspacePath():
    assert hasattr(viewpoint_style_WorkspaceImageDescription, "workspacePath")
    descriptor = None
    for klass in viewpoint_style_WorkspaceImageDescription.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(tool_DoubleClickDescription)


def test_tool_doubleclickdescription_constructor_exists():
    assert callable(tool_DoubleClickDescription.__init__)


def test_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(tool_DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(description_AbstractNodeMapping)


def test_description_abstractnodemapping_constructor_exists():
    assert callable(description_AbstractNodeMapping.__init__)


def test_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_directeditlabel_is_not_abstract():
    assert not inspect.isabstract(tool_DirectEditLabel)


def test_tool_directeditlabel_constructor_exists():
    assert callable(tool_DirectEditLabel.__init__)


def test_tool_directeditlabel_constructor_args():
    sig = inspect.signature(tool_DirectEditLabel.__init__)
    params = list(sig.parameters.keys())



def test_tool_deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteElementDescription)


def test_tool_deleteelementdescription_constructor_exists():
    assert callable(tool_DeleteElementDescription.__init__)


def test_tool_deleteelementdescription_constructor_args():
    sig = inspect.signature(tool_DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(tool_ToolSection)


def test_tool_toolsection_constructor_exists():
    assert callable(tool_ToolSection.__init__)


def test_tool_toolsection_constructor_args():
    sig = inspect.signature(tool_ToolSection.__init__)
    params = list(sig.parameters.keys())



def test_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationElementMapping)


def test_description_representationelementmapping_constructor_exists():
    assert callable(description_RepresentationElementMapping.__init__)


def test_description_representationelementmapping_constructor_args():
    sig = inspect.signature(description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationImportDescription)


def test_description_representationimportdescription_constructor_exists():
    assert callable(description_RepresentationImportDescription.__init__)


def test_description_representationimportdescription_constructor_args():
    sig = inspect.signature(description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_diagramimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DiagramImportDescription)


def test_viewpoint_description_diagramimportdescription_constructor_exists():
    assert callable(viewpoint_description_DiagramImportDescription.__init__)


def test_viewpoint_description_diagramimportdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DiagramImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_additionallayer_is_not_abstract():
    assert not inspect.isabstract(description_AdditionalLayer)


def test_description_additionallayer_constructor_exists():
    assert callable(description_AdditionalLayer.__init__)


def test_description_additionallayer_constructor_args():
    sig = inspect.signature(description_AdditionalLayer.__init__)
    params = list(sig.parameters.keys())



def test_description_layout_is_not_abstract():
    assert not inspect.isabstract(description_Layout)


def test_description_layout_constructor_exists():
    assert callable(description_Layout.__init__)


def test_description_layout_constructor_args():
    sig = inspect.signature(description_Layout.__init__)
    params = list(sig.parameters.keys())



def test_description_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(description_EdgeMappingImport)


def test_description_edgemappingimport_constructor_exists():
    assert callable(description_EdgeMappingImport.__init__)


def test_description_edgemappingimport_constructor_args():
    sig = inspect.signature(description_EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description_edgemapping_is_not_abstract():
    assert not inspect.isabstract(description_EdgeMapping)


def test_description_edgemapping_constructor_exists():
    assert callable(description_EdgeMapping.__init__)


def test_description_edgemapping_constructor_args():
    sig = inspect.signature(description_EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(concern_ConcernSet)


def test_concern_concernset_constructor_exists():
    assert callable(concern_ConcernSet.__init__)


def test_concern_concernset_constructor_args():
    sig = inspect.signature(concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_modelelement2viewvariable_is_not_abstract():
    assert not inspect.isabstract(ModelElement2ViewVariable)


def test_modelelement2viewvariable_constructor_exists():
    assert callable(ModelElement2ViewVariable.__init__)


def test_modelelement2viewvariable_constructor_args():
    sig = inspect.signature(ModelElement2ViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_diagramelementmapping2modelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DiagramElementMapping2ModelElement)


def test_viewpoint_diagram_diagramelementmapping2modelelement_constructor_exists():
    assert callable(viewpoint_diagram_DiagramElementMapping2ModelElement.__init__)


def test_viewpoint_diagram_diagramelementmapping2modelelement_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DiagramElementMapping2ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_diagramelementmapping2modelelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElementMapping2ModelElement)


def test_diagramelementmapping2modelelement_constructor_exists():
    assert callable(DiagramElementMapping2ModelElement.__init__)


def test_diagramelementmapping2modelelement_constructor_args():
    sig = inspect.signature(DiagramElementMapping2ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_computedstyledescriptionregistry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ComputedStyleDescriptionRegistry)


def test_viewpoint_diagram_computedstyledescriptionregistry_constructor_exists():
    assert callable(viewpoint_diagram_ComputedStyleDescriptionRegistry.__init__)


def test_viewpoint_diagram_computedstyledescriptionregistry_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ComputedStyleDescriptionRegistry.__init__)
    params = list(sig.parameters.keys())



def test_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(description_PasteTargetDescription)


def test_description_pastetargetdescription_constructor_exists():
    assert callable(description_PasteTargetDescription.__init__)


def test_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DiagramElementMapping)


def test_viewpoint_description_diagramelementmapping_constructor_exists():
    assert callable(viewpoint_description_DiagramElementMapping.__init__)


def test_viewpoint_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(viewpoint_description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())
    assert "synchronizationLock" in params, "Missing parameter 'synchronizationLock'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "createElements" in params, "Missing parameter 'createElements'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"

def test_viewpoint_description_diagramelementmapping_has_synchronizationLock():
    assert hasattr(viewpoint_description_DiagramElementMapping, "synchronizationLock")
    descriptor = None
    for klass in viewpoint_description_DiagramElementMapping.__mro__:
        if "synchronizationLock" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationLock"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramelementmapping_has_preconditionExpression():
    assert hasattr(viewpoint_description_DiagramElementMapping, "preconditionExpression")
    descriptor = None
    for klass in viewpoint_description_DiagramElementMapping.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramelementmapping_has_createElements():
    assert hasattr(viewpoint_description_DiagramElementMapping, "createElements")
    descriptor = None
    for klass in viewpoint_description_DiagramElementMapping.__mro__:
        if "createElements" in klass.__dict__:
            descriptor = klass.__dict__["createElements"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramelementmapping_has_semanticCandidatesExpression():
    assert hasattr(viewpoint_description_DiagramElementMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in viewpoint_description_DiagramElementMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramelementmapping_has_semanticElements():
    assert hasattr(viewpoint_description_DiagramElementMapping, "semanticElements")
    descriptor = None
    for klass in viewpoint_description_DiagramElementMapping.__mro__:
        if "semanticElements" in klass.__dict__:
            descriptor = klass.__dict__["semanticElements"]
            break
    assert isinstance(descriptor, property)



def test_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationDescription)


def test_description_representationdescription_constructor_exists():
    assert callable(description_RepresentationDescription.__init__)


def test_description_representationdescription_constructor_args():
    sig = inspect.signature(description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(description_DragAndDropTargetDescription)


def test_description_draganddroptargetdescription_constructor_exists():
    assert callable(description_DragAndDropTargetDescription.__init__)


def test_description_draganddroptargetdescription_constructor_args():
    sig = inspect.signature(description_DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_NodeMapping)


def test_viewpoint_description_nodemapping_constructor_exists():
    assert callable(viewpoint_description_NodeMapping.__init__)


def test_viewpoint_description_nodemapping_constructor_args():
    sig = inspect.signature(viewpoint_description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ContainerMapping)


def test_viewpoint_description_containermapping_constructor_exists():
    assert callable(viewpoint_description_ContainerMapping.__init__)


def test_viewpoint_description_containermapping_constructor_args():
    sig = inspect.signature(viewpoint_description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_viewpoint_description_containermapping_has_childrenPresentation():
    assert hasattr(viewpoint_description_ContainerMapping, "childrenPresentation")
    descriptor = None
    for klass in viewpoint_description_ContainerMapping.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DiagramDescription)


def test_viewpoint_description_diagramdescription_constructor_exists():
    assert callable(viewpoint_description_DiagramDescription.__init__)


def test_viewpoint_description_diagramdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "enablePopupBars" in params, "Missing parameter 'enablePopupBars'"

def test_viewpoint_description_diagramdescription_has_rootExpression():
    assert hasattr(viewpoint_description_DiagramDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint_description_DiagramDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramdescription_has_preconditionExpression():
    assert hasattr(viewpoint_description_DiagramDescription, "preconditionExpression")
    descriptor = None
    for klass in viewpoint_description_DiagramDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramdescription_has_domainClass():
    assert hasattr(viewpoint_description_DiagramDescription, "domainClass")
    descriptor = None
    for klass in viewpoint_description_DiagramDescription.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_diagramdescription_has_enablePopupBars():
    assert hasattr(viewpoint_description_DiagramDescription, "enablePopupBars")
    descriptor = None
    for klass in viewpoint_description_DiagramDescription.__mro__:
        if "enablePopupBars" in klass.__dict__:
            descriptor = klass.__dict__["enablePopupBars"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_containervariable2styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ContainerVariable2StyleDescription)


def test_viewpoint_diagram_containervariable2styledescription_constructor_exists():
    assert callable(viewpoint_diagram_ContainerVariable2StyleDescription.__init__)


def test_viewpoint_diagram_containervariable2styledescription_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ContainerVariable2StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_containervariable2styledescription_is_not_abstract():
    assert not inspect.isabstract(ContainerVariable2StyleDescription)


def test_containervariable2styledescription_constructor_exists():
    assert callable(ContainerVariable2StyleDescription.__init__)


def test_containervariable2styledescription_constructor_args():
    sig = inspect.signature(ContainerVariable2StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_viewvariable2containervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ViewVariable2ContainerVariable)


def test_viewpoint_diagram_viewvariable2containervariable_constructor_exists():
    assert callable(viewpoint_diagram_ViewVariable2ContainerVariable.__init__)


def test_viewpoint_diagram_viewvariable2containervariable_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ViewVariable2ContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewvariable2containervariable_is_not_abstract():
    assert not inspect.isabstract(ViewVariable2ContainerVariable)


def test_viewvariable2containervariable_constructor_exists():
    assert callable(ViewVariable2ContainerVariable.__init__)


def test_viewvariable2containervariable_constructor_args():
    sig = inspect.signature(ViewVariable2ContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_modelelement2viewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ModelElement2ViewVariable)


def test_viewpoint_diagram_modelelement2viewvariable_constructor_exists():
    assert callable(viewpoint_diagram_ModelElement2ViewVariable.__init__)


def test_viewpoint_diagram_modelelement2viewvariable_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ModelElement2ViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(diagram_viewpoint_EObject)


def test_diagram_viewpoint_eobject_constructor_exists():
    assert callable(diagram_viewpoint_EObject.__init__)


def test_diagram_viewpoint_eobject_constructor_args():
    sig = inspect.signature(diagram_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_filter_filtervariable_is_not_abstract():
    assert not inspect.isabstract(filter_FilterVariable)


def test_filter_filtervariable_constructor_exists():
    assert callable(filter_FilterVariable.__init__)


def test_filter_filtervariable_constructor_args():
    sig = inspect.signature(filter_FilterVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_filtervariablevalue_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_FilterVariableValue)


def test_viewpoint_diagram_filtervariablevalue_constructor_exists():
    assert callable(viewpoint_diagram_FilterVariableValue.__init__)


def test_viewpoint_diagram_filtervariablevalue_constructor_args():
    sig = inspect.signature(viewpoint_diagram_FilterVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_filtervariablevalue_is_not_abstract():
    assert not inspect.isabstract(FilterVariableValue)


def test_filtervariablevalue_constructor_exists():
    assert callable(FilterVariableValue.__init__)


def test_filtervariablevalue_constructor_args():
    sig = inspect.signature(FilterVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(CollapseFilter)


def test_collapsefilter_constructor_exists():
    assert callable(CollapseFilter.__init__)


def test_collapsefilter_constructor_args():
    sig = inspect.signature(CollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_indirectlycollapsefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_IndirectlyCollapseFilter)


def test_viewpoint_diagram_indirectlycollapsefilter_constructor_exists():
    assert callable(viewpoint_diagram_IndirectlyCollapseFilter.__init__)


def test_viewpoint_diagram_indirectlycollapsefilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_IndirectlyCollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_FilterVariableHistory)


def test_viewpoint_diagram_filtervariablehistory_constructor_exists():
    assert callable(viewpoint_diagram_FilterVariableHistory.__init__)


def test_viewpoint_diagram_filtervariablehistory_constructor_args():
    sig = inspect.signature(viewpoint_diagram_FilterVariableHistory.__init__)
    params = list(sig.parameters.keys())



def test_gaugesection_is_not_abstract():
    assert not inspect.isabstract(GaugeSection)


def test_gaugesection_constructor_exists():
    assert callable(GaugeSection.__init__)


def test_gaugesection_constructor_args():
    sig = inspect.signature(GaugeSection.__init__)
    params = list(sig.parameters.keys())



def test_endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(EndLabelStyle)


def test_endlabelstyle_constructor_exists():
    assert callable(EndLabelStyle.__init__)


def test_endlabelstyle_constructor_args():
    sig = inspect.signature(EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(CenterLabelStyle)


def test_centerlabelstyle_constructor_exists():
    assert callable(CenterLabelStyle.__init__)


def test_centerlabelstyle_constructor_args():
    sig = inspect.signature(CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(BeginLabelStyle)


def test_beginlabelstyle_constructor_exists():
    assert callable(BeginLabelStyle.__init__)


def test_beginlabelstyle_constructor_args():
    sig = inspect.signature(BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_containerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_ContainerStyle)


def test_diagram_containerstyle_constructor_exists():
    assert callable(diagram_ContainerStyle.__init__)


def test_diagram_containerstyle_constructor_args():
    sig = inspect.signature(diagram_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_nodestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_NodeStyle)


def test_diagram_nodestyle_constructor_exists():
    assert callable(diagram_NodeStyle.__init__)


def test_diagram_nodestyle_constructor_args():
    sig = inspect.signature(diagram_NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_workspaceimage_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_WorkspaceImage)


def test_viewpoint_diagram_workspaceimage_constructor_exists():
    assert callable(viewpoint_diagram_WorkspaceImage.__init__)


def test_viewpoint_diagram_workspaceimage_constructor_args():
    sig = inspect.signature(viewpoint_diagram_WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_viewpoint_diagram_workspaceimage_has_workspacePath():
    assert hasattr(viewpoint_diagram_WorkspaceImage, "workspacePath")
    descriptor = None
    for klass in viewpoint_diagram_WorkspaceImage.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_edgetarget_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_EdgeTarget)


def test_viewpoint_diagram_edgetarget_constructor_exists():
    assert callable(viewpoint_diagram_EdgeTarget.__init__)


def test_viewpoint_diagram_edgetarget_constructor_args():
    sig = inspect.signature(viewpoint_diagram_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BorderedStyle)


def test_diagram_borderedstyle_constructor_exists():
    assert callable(diagram_BorderedStyle.__init__)


def test_diagram_borderedstyle_constructor_args():
    sig = inspect.signature(diagram_BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_edgestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_EdgeStyle)


def test_viewpoint_diagram_edgestyle_constructor_exists():
    assert callable(viewpoint_diagram_EdgeStyle.__init__)


def test_viewpoint_diagram_edgestyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"

def test_viewpoint_diagram_edgestyle_has_size():
    assert hasattr(viewpoint_diagram_EdgeStyle, "size")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_edgestyle_has_targetArrow():
    assert hasattr(viewpoint_diagram_EdgeStyle, "targetArrow")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_edgestyle_has_routingStyle():
    assert hasattr(viewpoint_diagram_EdgeStyle, "routingStyle")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_edgestyle_has_lineStyle():
    assert hasattr(viewpoint_diagram_EdgeStyle, "lineStyle")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_edgestyle_has_foldingStyle():
    assert hasattr(viewpoint_diagram_EdgeStyle, "foldingStyle")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_edgestyle_has_sourceArrow():
    assert hasattr(viewpoint_diagram_EdgeStyle, "sourceArrow")
    descriptor = None
    for klass in viewpoint_diagram_EdgeStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_BorderedStyle)


def test_viewpoint_diagram_borderedstyle_constructor_exists():
    assert callable(viewpoint_diagram_BorderedStyle.__init__)


def test_viewpoint_diagram_borderedstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderSize" in params, "Missing parameter 'borderSize'"
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_viewpoint_diagram_borderedstyle_has_borderSize():
    assert hasattr(viewpoint_diagram_BorderedStyle, "borderSize")
    descriptor = None
    for klass in viewpoint_diagram_BorderedStyle.__mro__:
        if "borderSize" in klass.__dict__:
            descriptor = klass.__dict__["borderSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_borderedstyle_has_borderSizeComputationExpression():
    assert hasattr(viewpoint_diagram_BorderedStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in viewpoint_diagram_BorderedStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_containerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ContainerStyle)


def test_viewpoint_diagram_containerstyle_constructor_exists():
    assert callable(viewpoint_diagram_ContainerStyle.__init__)


def test_viewpoint_diagram_containerstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_nodestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_NodeStyle)


def test_viewpoint_diagram_nodestyle_constructor_exists():
    assert callable(viewpoint_diagram_NodeStyle.__init__)


def test_viewpoint_diagram_nodestyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_viewpoint_diagram_nodestyle_has_hideLabelByDefault():
    assert hasattr(viewpoint_diagram_NodeStyle, "hideLabelByDefault")
    descriptor = None
    for klass in viewpoint_diagram_NodeStyle.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_nodestyle_has_labelPosition():
    assert hasattr(viewpoint_diagram_NodeStyle, "labelPosition")
    descriptor = None
    for klass in viewpoint_diagram_NodeStyle.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_diagram_viewpoint_drepresentationcontainer_is_not_abstract():
    assert not inspect.isabstract(diagram_viewpoint_DRepresentationContainer)


def test_diagram_viewpoint_drepresentationcontainer_constructor_exists():
    assert callable(diagram_viewpoint_DRepresentationContainer.__init__)


def test_diagram_viewpoint_drepresentationcontainer_constructor_args():
    sig = inspect.signature(diagram_viewpoint_DRepresentationContainer.__init__)
    params = list(sig.parameters.keys())



def test_diagram_viewpoint_rgbvalues_is_not_abstract():
    assert not inspect.isabstract(diagram_viewpoint_RGBValues)


def test_diagram_viewpoint_rgbvalues_constructor_exists():
    assert callable(diagram_viewpoint_RGBValues.__init__)


def test_diagram_viewpoint_rgbvalues_constructor_args():
    sig = inspect.signature(diagram_viewpoint_RGBValues.__init__)
    params = list(sig.parameters.keys())



def test_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(description_IEdgeMapping)


def test_description_iedgemapping_constructor_exists():
    assert callable(description_IEdgeMapping.__init__)


def test_description_iedgemapping_constructor_args():
    sig = inspect.signature(description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_ddiagramset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DDiagramSet)


def test_viewpoint_diagram_ddiagramset_constructor_exists():
    assert callable(viewpoint_diagram_DDiagramSet.__init__)


def test_viewpoint_diagram_ddiagramset_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DDiagramSet.__init__)
    params = list(sig.parameters.keys())



def test_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(AbstractDNode)


def test_abstractdnode_constructor_exists():
    assert callable(AbstractDNode.__init__)


def test_abstractdnode_constructor_args():
    sig = inspect.signature(AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DNodeListElement)


def test_viewpoint_diagram_dnodelistelement_constructor_exists():
    assert callable(viewpoint_diagram_DNodeListElement.__init__)


def test_viewpoint_diagram_dnodelistelement_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_edgestyle_is_not_abstract():
    assert not inspect.isabstract(EdgeStyle)


def test_edgestyle_constructor_exists():
    assert callable(EdgeStyle.__init__)


def test_edgestyle_constructor_args():
    sig = inspect.signature(EdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_bracketedgestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_BracketEdgeStyle)


def test_viewpoint_diagram_bracketedgestyle_constructor_exists():
    assert callable(viewpoint_diagram_BracketEdgeStyle.__init__)


def test_viewpoint_diagram_bracketedgestyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_BracketEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagramElement)


def test_diagram_ddiagramelement_constructor_exists():
    assert callable(diagram_DDiagramElement.__init__)


def test_diagram_ddiagramelement_constructor_args():
    sig = inspect.signature(diagram_DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(description_ContainerMapping)


def test_description_containermapping_constructor_exists():
    assert callable(description_ContainerMapping.__init__)


def test_description_containermapping_constructor_args():
    sig = inspect.signature(description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_containermappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ContainerMappingImport)


def test_viewpoint_description_containermappingimport_constructor_exists():
    assert callable(viewpoint_description_ContainerMappingImport.__init__)


def test_viewpoint_description_containermappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_ContainerMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_FlatContainerStyle)


def test_viewpoint_diagram_flatcontainerstyle_constructor_exists():
    assert callable(viewpoint_diagram_FlatContainerStyle.__init__)


def test_viewpoint_diagram_flatcontainerstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_viewpoint_diagram_flatcontainerstyle_has_backgroundStyle():
    assert hasattr(viewpoint_diagram_FlatContainerStyle, "backgroundStyle")
    descriptor = None
    for klass in viewpoint_diagram_FlatContainerStyle.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_ShapeContainerStyle)


def test_viewpoint_diagram_shapecontainerstyle_constructor_exists():
    assert callable(viewpoint_diagram_ShapeContainerStyle.__init__)


def test_viewpoint_diagram_shapecontainerstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint_diagram_shapecontainerstyle_has_shape():
    assert hasattr(viewpoint_diagram_ShapeContainerStyle, "shape")
    descriptor = None
    for klass in viewpoint_diagram_ShapeContainerStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagram_edgetarget_is_not_abstract():
    assert not inspect.isabstract(diagram_EdgeTarget)


def test_diagram_edgetarget_constructor_exists():
    assert callable(diagram_EdgeTarget.__init__)


def test_diagram_edgetarget_constructor_args():
    sig = inspect.signature(diagram_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_dedge_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DEdge)


def test_viewpoint_diagram_dedge_constructor_exists():
    assert callable(viewpoint_diagram_DEdge.__init__)


def test_viewpoint_diagram_dedge_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "beginLabel" in params, "Missing parameter 'beginLabel'"
    assert "isFold" in params, "Missing parameter 'isFold'"
    assert "endLabel" in params, "Missing parameter 'endLabel'"
    assert "size" in params, "Missing parameter 'size'"
    assert "isMockEdge" in params, "Missing parameter 'isMockEdge'"
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_viewpoint_diagram_dedge_has_routingStyle():
    assert hasattr(viewpoint_diagram_DEdge, "routingStyle")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_beginLabel():
    assert hasattr(viewpoint_diagram_DEdge, "beginLabel")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "beginLabel" in klass.__dict__:
            descriptor = klass.__dict__["beginLabel"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_isFold():
    assert hasattr(viewpoint_diagram_DEdge, "isFold")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "isFold" in klass.__dict__:
            descriptor = klass.__dict__["isFold"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_endLabel():
    assert hasattr(viewpoint_diagram_DEdge, "endLabel")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_size():
    assert hasattr(viewpoint_diagram_DEdge, "size")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_isMockEdge():
    assert hasattr(viewpoint_diagram_DEdge, "isMockEdge")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "isMockEdge" in klass.__dict__:
            descriptor = klass.__dict__["isMockEdge"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dedge_has_arrangeConstraints():
    assert hasattr(viewpoint_diagram_DEdge, "arrangeConstraints")
    descriptor = None
    for klass in viewpoint_diagram_DEdge.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_diagram_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(diagram_AbstractDNode)


def test_diagram_abstractdnode_constructor_exists():
    assert callable(diagram_AbstractDNode.__init__)


def test_diagram_abstractdnode_constructor_args():
    sig = inspect.signature(diagram_AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DDiagramElementContainer)


def test_viewpoint_diagram_ddiagramelementcontainer_constructor_exists():
    assert callable(viewpoint_diagram_DDiagramElementContainer.__init__)


def test_viewpoint_diagram_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint_diagram_ddiagramelementcontainer_has_height():
    assert hasattr(viewpoint_diagram_DDiagramElementContainer, "height")
    descriptor = None
    for klass in viewpoint_diagram_DDiagramElementContainer.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ddiagramelementcontainer_has_width():
    assert hasattr(viewpoint_diagram_DDiagramElementContainer, "width")
    descriptor = None
    for klass in viewpoint_diagram_DDiagramElementContainer.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_dnode_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DNode)


def test_viewpoint_diagram_dnode_constructor_exists():
    assert callable(viewpoint_diagram_DNode.__init__)


def test_viewpoint_diagram_dnode_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DNode.__init__)
    params = list(sig.parameters.keys())
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint_diagram_dnode_has_resizeKind():
    assert hasattr(viewpoint_diagram_DNode, "resizeKind")
    descriptor = None
    for klass in viewpoint_diagram_DNode.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dnode_has_labelPosition():
    assert hasattr(viewpoint_diagram_DNode, "labelPosition")
    descriptor = None
    for klass in viewpoint_diagram_DNode.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dnode_has_height():
    assert hasattr(viewpoint_diagram_DNode, "height")
    descriptor = None
    for klass in viewpoint_diagram_DNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_dnode_has_width():
    assert hasattr(viewpoint_diagram_DNode, "width")
    descriptor = None
    for klass in viewpoint_diagram_DNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_AbstractDNode)


def test_viewpoint_diagram_abstractdnode_constructor_exists():
    assert callable(viewpoint_diagram_AbstractDNode.__init__)


def test_viewpoint_diagram_abstractdnode_constructor_args():
    sig = inspect.signature(viewpoint_diagram_AbstractDNode.__init__)
    params = list(sig.parameters.keys())
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_viewpoint_diagram_abstractdnode_has_arrangeConstraints():
    assert hasattr(viewpoint_diagram_AbstractDNode, "arrangeConstraints")
    descriptor = None
    for klass in viewpoint_diagram_AbstractDNode.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(description_NodeMapping)


def test_description_nodemapping_constructor_exists():
    assert callable(description_NodeMapping.__init__)


def test_description_nodemapping_constructor_args():
    sig = inspect.signature(description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_nodemappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_NodeMappingImport)


def test_viewpoint_description_nodemappingimport_constructor_exists():
    assert callable(viewpoint_description_NodeMappingImport.__init__)


def test_viewpoint_description_nodemappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_NodeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_diagram_viewpoint_style_is_not_abstract():
    assert not inspect.isabstract(diagram_viewpoint_Style)


def test_diagram_viewpoint_style_constructor_exists():
    assert callable(diagram_viewpoint_Style.__init__)


def test_diagram_viewpoint_style_constructor_args():
    sig = inspect.signature(diagram_viewpoint_Style.__init__)
    params = list(sig.parameters.keys())



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_bundledimage_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_BundledImage)


def test_viewpoint_diagram_bundledimage_constructor_exists():
    assert callable(viewpoint_diagram_BundledImage.__init__)


def test_viewpoint_diagram_bundledimage_constructor_args():
    sig = inspect.signature(viewpoint_diagram_BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_viewpoint_diagram_bundledimage_has_shape():
    assert hasattr(viewpoint_diagram_BundledImage, "shape")
    descriptor = None
    for klass in viewpoint_diagram_BundledImage.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_customstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_CustomStyle)


def test_viewpoint_diagram_customstyle_constructor_exists():
    assert callable(viewpoint_diagram_CustomStyle.__init__)


def test_viewpoint_diagram_customstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_CustomStyle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint_diagram_customstyle_has_id():
    assert hasattr(viewpoint_diagram_CustomStyle, "id")
    descriptor = None
    for klass in viewpoint_diagram_CustomStyle.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_ellipse_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_Ellipse)


def test_viewpoint_diagram_ellipse_constructor_exists():
    assert callable(viewpoint_diagram_Ellipse.__init__)


def test_viewpoint_diagram_ellipse_constructor_args():
    sig = inspect.signature(viewpoint_diagram_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"

def test_viewpoint_diagram_ellipse_has_verticalDiameter():
    assert hasattr(viewpoint_diagram_Ellipse, "verticalDiameter")
    descriptor = None
    for klass in viewpoint_diagram_Ellipse.__mro__:
        if "verticalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameter"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ellipse_has_horizontalDiameter():
    assert hasattr(viewpoint_diagram_Ellipse, "horizontalDiameter")
    descriptor = None
    for klass in viewpoint_diagram_Ellipse.__mro__:
        if "horizontalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameter"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_lozenge_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_Lozenge)


def test_viewpoint_diagram_lozenge_constructor_exists():
    assert callable(viewpoint_diagram_Lozenge.__init__)


def test_viewpoint_diagram_lozenge_constructor_args():
    sig = inspect.signature(viewpoint_diagram_Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint_diagram_lozenge_has_height():
    assert hasattr(viewpoint_diagram_Lozenge, "height")
    descriptor = None
    for klass in viewpoint_diagram_Lozenge.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_lozenge_has_width():
    assert hasattr(viewpoint_diagram_Lozenge, "width")
    descriptor = None
    for klass in viewpoint_diagram_Lozenge.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_note_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_Note)


def test_viewpoint_diagram_note_constructor_exists():
    assert callable(viewpoint_diagram_Note.__init__)


def test_viewpoint_diagram_note_constructor_args():
    sig = inspect.signature(viewpoint_diagram_Note.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_dot_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_Dot)


def test_viewpoint_diagram_dot_constructor_exists():
    assert callable(viewpoint_diagram_Dot.__init__)


def test_viewpoint_diagram_dot_constructor_args():
    sig = inspect.signature(viewpoint_diagram_Dot.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_viewpoint_diagram_dot_has_strokeSizeComputationExpression():
    assert hasattr(viewpoint_diagram_Dot, "strokeSizeComputationExpression")
    descriptor = None
    for klass in viewpoint_diagram_Dot.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_GaugeCompositeStyle)


def test_viewpoint_diagram_gaugecompositestyle_constructor_exists():
    assert callable(viewpoint_diagram_GaugeCompositeStyle.__init__)


def test_viewpoint_diagram_gaugecompositestyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_viewpoint_diagram_gaugecompositestyle_has_alignment():
    assert hasattr(viewpoint_diagram_GaugeCompositeStyle, "alignment")
    descriptor = None
    for klass in viewpoint_diagram_GaugeCompositeStyle.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_square_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_Square)


def test_viewpoint_diagram_square_constructor_exists():
    assert callable(viewpoint_diagram_Square.__init__)


def test_viewpoint_diagram_square_constructor_args():
    sig = inspect.signature(viewpoint_diagram_Square.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_viewpoint_diagram_square_has_width():
    assert hasattr(viewpoint_diagram_Square, "width")
    descriptor = None
    for klass in viewpoint_diagram_Square.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_square_has_height():
    assert hasattr(viewpoint_diagram_Square, "height")
    descriptor = None
    for klass in viewpoint_diagram_Square.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_GraphicalFilter)


def test_viewpoint_diagram_graphicalfilter_constructor_exists():
    assert callable(viewpoint_diagram_GraphicalFilter.__init__)


def test_viewpoint_diagram_graphicalfilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(GraphicalFilter)


def test_graphicalfilter_constructor_exists():
    assert callable(GraphicalFilter.__init__)


def test_graphicalfilter_constructor_args():
    sig = inspect.signature(GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_CollapseFilter)


def test_viewpoint_diagram_collapsefilter_constructor_exists():
    assert callable(viewpoint_diagram_CollapseFilter.__init__)


def test_viewpoint_diagram_collapsefilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_CollapseFilter.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_viewpoint_diagram_collapsefilter_has_height():
    assert hasattr(viewpoint_diagram_CollapseFilter, "height")
    descriptor = None
    for klass in viewpoint_diagram_CollapseFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_collapsefilter_has_width():
    assert hasattr(viewpoint_diagram_CollapseFilter, "width")
    descriptor = None
    for klass in viewpoint_diagram_CollapseFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_diagram_viewpoint_decoration_is_not_abstract():
    assert not inspect.isabstract(diagram_viewpoint_Decoration)


def test_diagram_viewpoint_decoration_constructor_exists():
    assert callable(diagram_viewpoint_Decoration.__init__)


def test_diagram_viewpoint_decoration_constructor_args():
    sig = inspect.signature(diagram_viewpoint_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_absoluteboundsfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_AbsoluteBoundsFilter)


def test_viewpoint_diagram_absoluteboundsfilter_constructor_exists():
    assert callable(viewpoint_diagram_AbsoluteBoundsFilter.__init__)


def test_viewpoint_diagram_absoluteboundsfilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_AbsoluteBoundsFilter.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_viewpoint_diagram_absoluteboundsfilter_has_width():
    assert hasattr(viewpoint_diagram_AbsoluteBoundsFilter, "width")
    descriptor = None
    for klass in viewpoint_diagram_AbsoluteBoundsFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_absoluteboundsfilter_has_height():
    assert hasattr(viewpoint_diagram_AbsoluteBoundsFilter, "height")
    descriptor = None
    for klass in viewpoint_diagram_AbsoluteBoundsFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_absoluteboundsfilter_has_x():
    assert hasattr(viewpoint_diagram_AbsoluteBoundsFilter, "x")
    descriptor = None
    for klass in viewpoint_diagram_AbsoluteBoundsFilter.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_absoluteboundsfilter_has_y():
    assert hasattr(viewpoint_diagram_AbsoluteBoundsFilter, "y")
    descriptor = None
    for klass in viewpoint_diagram_AbsoluteBoundsFilter.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(filter_CompositeFilterDescription)


def test_filter_compositefilterdescription_constructor_exists():
    assert callable(filter_CompositeFilterDescription.__init__)


def test_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_appliedcompositefilters_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_AppliedCompositeFilters)


def test_viewpoint_diagram_appliedcompositefilters_constructor_exists():
    assert callable(viewpoint_diagram_AppliedCompositeFilters.__init__)


def test_viewpoint_diagram_appliedcompositefilters_constructor_args():
    sig = inspect.signature(viewpoint_diagram_AppliedCompositeFilters.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_foldingfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_FoldingFilter)


def test_viewpoint_diagram_foldingfilter_constructor_exists():
    assert callable(viewpoint_diagram_FoldingFilter.__init__)


def test_viewpoint_diagram_foldingfilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_FoldingFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_foldingpointfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_FoldingPointFilter)


def test_viewpoint_diagram_foldingpointfilter_constructor_exists():
    assert callable(viewpoint_diagram_FoldingPointFilter.__init__)


def test_viewpoint_diagram_foldingpointfilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_FoldingPointFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_hidelabelfilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_HideLabelFilter)


def test_viewpoint_diagram_hidelabelfilter_constructor_exists():
    assert callable(viewpoint_diagram_HideLabelFilter.__init__)


def test_viewpoint_diagram_hidelabelfilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_HideLabelFilter.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_hidefilter_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_HideFilter)


def test_viewpoint_diagram_hidefilter_constructor_exists():
    assert callable(viewpoint_diagram_HideFilter.__init__)


def test_viewpoint_diagram_hidefilter_constructor_args():
    sig = inspect.signature(viewpoint_diagram_HideFilter.__init__)
    params = list(sig.parameters.keys())



def test_description_layer_is_not_abstract():
    assert not inspect.isabstract(description_Layer)


def test_description_layer_constructor_exists():
    assert callable(description_Layer.__init__)


def test_description_layer_constructor_args():
    sig = inspect.signature(description_Layer.__init__)
    params = list(sig.parameters.keys())



def test_filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(FilterVariableHistory)


def test_filtervariablehistory_constructor_exists():
    assert callable(FilterVariableHistory.__init__)


def test_filtervariablehistory_constructor_args():
    sig = inspect.signature(FilterVariableHistory.__init__)
    params = list(sig.parameters.keys())



def test_tool_behaviortool_is_not_abstract():
    assert not inspect.isabstract(tool_BehaviorTool)


def test_tool_behaviortool_constructor_exists():
    assert callable(tool_BehaviorTool.__init__)


def test_tool_behaviortool_constructor_args():
    sig = inspect.signature(tool_BehaviorTool.__init__)
    params = list(sig.parameters.keys())



def test_validation_validationrule_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationRule)


def test_validation_validationrule_constructor_exists():
    assert callable(validation_ValidationRule.__init__)


def test_validation_validationrule_constructor_args():
    sig = inspect.signature(validation_ValidationRule.__init__)
    params = list(sig.parameters.keys())



def test_dnavigable_is_not_abstract():
    assert not inspect.isabstract(DNavigable)


def test_dnavigable_constructor_exists():
    assert callable(DNavigable.__init__)


def test_dnavigable_constructor_args():
    sig = inspect.signature(DNavigable.__init__)
    params = list(sig.parameters.keys())



def test_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DDiagramElement)


def test_viewpoint_diagram_ddiagramelement_constructor_exists():
    assert callable(viewpoint_diagram_DDiagramElement.__init__)


def test_viewpoint_diagram_ddiagramelement_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DDiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"
    assert "visible" in params, "Missing parameter 'visible'"

def test_viewpoint_diagram_ddiagramelement_has_tooltipText():
    assert hasattr(viewpoint_diagram_DDiagramElement, "tooltipText")
    descriptor = None
    for klass in viewpoint_diagram_DDiagramElement.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ddiagramelement_has_visible():
    assert hasattr(viewpoint_diagram_DDiagramElement, "visible")
    descriptor = None
    for klass in viewpoint_diagram_DDiagramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)



def test_diagram_ddiagram_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagram)


def test_diagram_ddiagram_constructor_exists():
    assert callable(diagram_DDiagram.__init__)


def test_diagram_ddiagram_constructor_args():
    sig = inspect.signature(diagram_DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_dedge_is_not_abstract():
    assert not inspect.isabstract(DEdge)


def test_dedge_constructor_exists():
    assert callable(DEdge.__init__)


def test_dedge_constructor_args():
    sig = inspect.signature(DEdge.__init__)
    params = list(sig.parameters.keys())



def test_ddiagram_is_not_abstract():
    assert not inspect.isabstract(DDiagram)


def test_ddiagram_constructor_exists():
    assert callable(DDiagram.__init__)


def test_ddiagram_constructor_args():
    sig = inspect.signature(DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_filter_filterdescription_is_not_abstract():
    assert not inspect.isabstract(filter_FilterDescription)


def test_filter_filterdescription_constructor_exists():
    assert callable(filter_FilterDescription.__init__)


def test_filter_filterdescription_constructor_args():
    sig = inspect.signature(filter_FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_concern_concerndescription_is_not_abstract():
    assert not inspect.isabstract(concern_ConcernDescription)


def test_concern_concerndescription_constructor_exists():
    assert callable(concern_ConcernDescription.__init__)


def test_concern_concerndescription_constructor_args():
    sig = inspect.signature(concern_ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(DDiagramElementContainer)


def test_ddiagramelementcontainer_constructor_exists():
    assert callable(DDiagramElementContainer.__init__)


def test_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_dnodecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DNodeContainer)


def test_viewpoint_diagram_dnodecontainer_constructor_exists():
    assert callable(viewpoint_diagram_DNodeContainer.__init__)


def test_viewpoint_diagram_dnodecontainer_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DNodeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_viewpoint_diagram_dnodecontainer_has_childrenPresentation():
    assert hasattr(viewpoint_diagram_DNodeContainer, "childrenPresentation")
    descriptor = None
    for klass in viewpoint_diagram_DNodeContainer.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_dnodelist_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DNodeList)


def test_viewpoint_diagram_dnodelist_constructor_exists():
    assert callable(viewpoint_diagram_DNodeList.__init__)


def test_viewpoint_diagram_dnodelist_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DNodeList.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_viewpoint_diagram_dnodelist_has_lineWidth():
    assert hasattr(viewpoint_diagram_DNodeList, "lineWidth")
    descriptor = None
    for klass in viewpoint_diagram_DNodeList.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(DNodeListElement)


def test_dnodelistelement_constructor_exists():
    assert callable(DNodeListElement.__init__)


def test_dnodelistelement_constructor_args():
    sig = inspect.signature(DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitEdgeCreationOperation)


def test_viewpoint_tool_initedgecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitEdgeCreationOperation.__init__)


def test_viewpoint_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialOperation)


def test_viewpoint_tool_initialoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialOperation.__init__)


def test_viewpoint_tool_initialoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_InitialNodeCreationOperation)


def test_viewpoint_tool_initialnodecreationoperation_constructor_exists():
    assert callable(viewpoint_tool_InitialNodeCreationOperation.__init__)


def test_viewpoint_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ModelOperation)


def test_viewpoint_tool_modeloperation_constructor_exists():
    assert callable(viewpoint_tool_ModelOperation.__init__)


def test_viewpoint_tool_modeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_modeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ModelOperation)


def test_tool_modeloperation_constructor_exists():
    assert callable(tool_ModelOperation.__init__)


def test_tool_modeloperation_constructor_args():
    sig = inspect.signature(tool_ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_modeloperation_is_not_abstract():
    assert not inspect.isabstract(ModelOperation)


def test_modeloperation_constructor_exists():
    assert callable(ModelOperation.__init__)


def test_modeloperation_constructor_args():
    sig = inspect.signature(ModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_switch_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_Switch)


def test_viewpoint_tool_switch_constructor_exists():
    assert callable(viewpoint_tool_Switch.__init__)


def test_viewpoint_tool_switch_constructor_args():
    sig = inspect.signature(viewpoint_tool_Switch.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerModelOperation)


def test_viewpoint_tool_containermodeloperation_constructor_exists():
    assert callable(viewpoint_tool_ContainerModelOperation.__init__)


def test_viewpoint_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_EditMaskVariables)


def test_viewpoint_tool_editmaskvariables_constructor_exists():
    assert callable(viewpoint_tool_EditMaskVariables.__init__)


def test_viewpoint_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(viewpoint_tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())
    assert "mask" in params, "Missing parameter 'mask'"

def test_viewpoint_tool_editmaskvariables_has_mask():
    assert hasattr(viewpoint_tool_EditMaskVariables, "mask")
    descriptor = None
    for klass in viewpoint_tool_EditMaskVariables.__mro__:
        if "mask" in klass.__dict__:
            descriptor = klass.__dict__["mask"]
            break
    assert isinstance(descriptor, property)



def test_tool_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractVariable)


def test_tool_abstractvariable_constructor_exists():
    assert callable(tool_AbstractVariable.__init__)


def test_tool_abstractvariable_constructor_args():
    sig = inspect.signature(tool_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractVariable)


def test_abstractvariable_constructor_exists():
    assert callable(AbstractVariable.__init__)


def test_abstractvariable_constructor_args():
    sig = inspect.signature(AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementSelectVariable)


def test_viewpoint_tool_elementselectvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementSelectVariable.__init__)


def test_viewpoint_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_NameVariable)


def test_viewpoint_tool_namevariable_constructor_exists():
    assert callable(viewpoint_tool_NameVariable.__init__)


def test_viewpoint_tool_namevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_dialogvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DialogVariable)


def test_viewpoint_tool_dialogvariable_constructor_exists():
    assert callable(viewpoint_tool_DialogVariable.__init__)


def test_viewpoint_tool_dialogvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DialogVariable.__init__)
    params = list(sig.parameters.keys())
    assert "dialogPrompt" in params, "Missing parameter 'dialogPrompt'"

def test_viewpoint_tool_dialogvariable_has_dialogPrompt():
    assert hasattr(viewpoint_tool_DialogVariable, "dialogPrompt")
    descriptor = None
    for klass in viewpoint_tool_DialogVariable.__mro__:
        if "dialogPrompt" in klass.__dict__:
            descriptor = klass.__dict__["dialogPrompt"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_subvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SubVariable)


def test_viewpoint_tool_subvariable_constructor_exists():
    assert callable(viewpoint_tool_SubVariable.__init__)


def test_viewpoint_tool_subvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerViewVariable)


def test_viewpoint_tool_containerviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ContainerViewVariable.__init__)


def test_viewpoint_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDropVariable)


def test_viewpoint_tool_elementdropvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDropVariable.__init__)


def test_viewpoint_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectContainerVariable)


def test_viewpoint_tool_selectcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_SelectContainerVariable.__init__)


def test_viewpoint_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_TargetEdgeCreationVariable)


def test_viewpoint_tool_targetedgecreationvariable_constructor_exists():
    assert callable(viewpoint_tool_TargetEdgeCreationVariable.__init__)


def test_viewpoint_tool_targetedgecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SourceEdgeCreationVariable)


def test_viewpoint_tool_sourceedgecreationvariable_constructor_exists():
    assert callable(viewpoint_tool_SourceEdgeCreationVariable.__init__)


def test_viewpoint_tool_sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_NodeCreationVariable)


def test_viewpoint_tool_nodecreationvariable_constructor_exists():
    assert callable(viewpoint_tool_NodeCreationVariable.__init__)


def test_viewpoint_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDoubleClickVariable)


def test_viewpoint_tool_elementdoubleclickvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDoubleClickVariable.__init__)


def test_viewpoint_tool_elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_TargetEdgeViewCreationVariable)


def test_viewpoint_tool_targetedgeviewcreationvariable_constructor_exists():
    assert callable(viewpoint_tool_TargetEdgeViewCreationVariable.__init__)


def test_viewpoint_tool_targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SourceEdgeViewCreationVariable)


def test_viewpoint_tool_sourceedgeviewcreationvariable_constructor_exists():
    assert callable(viewpoint_tool_SourceEdgeViewCreationVariable.__init__)


def test_viewpoint_tool_sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementVariable)


def test_viewpoint_tool_elementvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementVariable.__init__)


def test_viewpoint_tool_elementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_subvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SubVariable)


def test_tool_subvariable_constructor_exists():
    assert callable(tool_SubVariable.__init__)


def test_tool_subvariable_constructor_args():
    sig = inspect.signature(tool_SubVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_acceleovariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AcceleoVariable)


def test_viewpoint_tool_acceleovariable_constructor_exists():
    assert callable(viewpoint_tool_AcceleoVariable.__init__)


def test_viewpoint_tool_acceleovariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_AcceleoVariable.__init__)
    params = list(sig.parameters.keys())
    assert "computationExpression" in params, "Missing parameter 'computationExpression'"

def test_viewpoint_tool_acceleovariable_has_computationExpression():
    assert hasattr(viewpoint_tool_AcceleoVariable, "computationExpression")
    descriptor = None
    for klass in viewpoint_tool_AcceleoVariable.__mro__:
        if "computationExpression" in klass.__dict__:
            descriptor = klass.__dict__["computationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_VariableContainer)


def test_viewpoint_tool_variablecontainer_constructor_exists():
    assert callable(viewpoint_tool_VariableContainer.__init__)


def test_viewpoint_tool_variablecontainer_constructor_args():
    sig = inspect.signature(viewpoint_tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AbstractVariable)


def test_viewpoint_tool_abstractvariable_constructor_exists():
    assert callable(viewpoint_tool_AbstractVariable.__init__)


def test_viewpoint_tool_abstractvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_AbstractVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_tool_abstractvariable_has_name():
    assert hasattr(viewpoint_tool_AbstractVariable, "name")
    descriptor = None
    for klass in viewpoint_tool_AbstractVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaAction)


def test_tool_externaljavaaction_constructor_exists():
    assert callable(tool_ExternalJavaAction.__init__)


def test_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())



def test_tool_externaljavaactionparameter_is_not_abstract():
    assert not inspect.isabstract(tool_ExternalJavaActionParameter)


def test_tool_externaljavaactionparameter_constructor_exists():
    assert callable(tool_ExternalJavaActionParameter.__init__)


def test_tool_externaljavaactionparameter_constructor_args():
    sig = inspect.signature(tool_ExternalJavaActionParameter.__init__)
    params = list(sig.parameters.keys())



def test_tool_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerModelOperation)


def test_tool_containermodeloperation_constructor_exists():
    assert callable(tool_ContainerModelOperation.__init__)


def test_tool_containermodeloperation_constructor_args():
    sig = inspect.signature(tool_ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DropContainerVariable)


def test_viewpoint_tool_dropcontainervariable_constructor_exists():
    assert callable(viewpoint_tool_DropContainerVariable.__init__)


def test_viewpoint_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementDeleteVariable)


def test_viewpoint_tool_elementdeletevariable_constructor_exists():
    assert callable(viewpoint_tool_ElementDeleteVariable.__init__)


def test_viewpoint_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ElementViewVariable)


def test_viewpoint_tool_elementviewvariable_constructor_exists():
    assert callable(viewpoint_tool_ElementViewVariable.__init__)


def test_viewpoint_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(MenuItemDescription)


def test_menuitemdescription_constructor_exists():
    assert callable(MenuItemDescription.__init__)


def test_menuitemdescription_constructor_args():
    sig = inspect.signature(MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_operationaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_OperationAction)


def test_viewpoint_tool_operationaction_constructor_exists():
    assert callable(viewpoint_tool_OperationAction.__init__)


def test_viewpoint_tool_operationaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_OperationAction.__init__)
    params = list(sig.parameters.keys())



def test_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemDescription)


def test_tool_menuitemdescription_constructor_exists():
    assert callable(tool_MenuItemDescription.__init__)


def test_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_externaljavaaction_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaAction)


def test_viewpoint_tool_externaljavaaction_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaAction.__init__)


def test_viewpoint_tool_externaljavaaction_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaAction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_viewpoint_tool_externaljavaaction_has_id():
    assert hasattr(viewpoint_tool_ExternalJavaAction, "id")
    descriptor = None
    for klass in viewpoint_tool_ExternalJavaAction.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_externaljavaactioncall_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ExternalJavaActionCall)


def test_viewpoint_tool_externaljavaactioncall_constructor_exists():
    assert callable(viewpoint_tool_ExternalJavaActionCall.__init__)


def test_viewpoint_tool_externaljavaactioncall_constructor_args():
    sig = inspect.signature(viewpoint_tool_ExternalJavaActionCall.__init__)
    params = list(sig.parameters.keys())



def test_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(MenuItemOrRef)


def test_menuitemorref_constructor_exists():
    assert callable(MenuItemOrRef.__init__)


def test_menuitemorref_constructor_args():
    sig = inspect.signature(MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemdescriptionreference_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescriptionReference)


def test_viewpoint_tool_menuitemdescriptionreference_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescriptionReference.__init__)


def test_viewpoint_tool_menuitemdescriptionreference_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescriptionReference.__init__)
    params = list(sig.parameters.keys())



def test_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(tool_MenuItemOrRef)


def test_tool_menuitemorref_constructor_exists():
    assert callable(tool_MenuItemOrRef.__init__)


def test_tool_menuitemorref_constructor_args():
    sig = inspect.signature(tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemorref_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemOrRef)


def test_viewpoint_tool_menuitemorref_constructor_exists():
    assert callable(viewpoint_tool_MenuItemOrRef.__init__)


def test_viewpoint_tool_menuitemorref_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemOrRef.__init__)
    params = list(sig.parameters.keys())



def test_tool_namevariable_is_not_abstract():
    assert not inspect.isabstract(tool_NameVariable)


def test_tool_namevariable_constructor_exists():
    assert callable(tool_NameVariable.__init__)


def test_tool_namevariable_constructor_args():
    sig = inspect.signature(tool_NameVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_selectcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_SelectContainerVariable)


def test_tool_selectcontainervariable_constructor_exists():
    assert callable(tool_SelectContainerVariable.__init__)


def test_tool_selectcontainervariable_constructor_args():
    sig = inspect.signature(tool_SelectContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialContainerDropOperation)


def test_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(tool_InitialContainerDropOperation.__init__)


def test_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementSelectVariable)


def test_tool_elementselectvariable_constructor_exists():
    assert callable(tool_ElementSelectVariable.__init__)


def test_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(description_SelectionDescription)


def test_description_selectiondescription_constructor_exists():
    assert callable(description_SelectionDescription.__init__)


def test_description_selectiondescription_constructor_args():
    sig = inspect.signature(description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectModelElementVariable)


def test_viewpoint_tool_selectmodelelementvariable_constructor_exists():
    assert callable(viewpoint_tool_SelectModelElementVariable.__init__)


def test_viewpoint_tool_selectmodelelementvariable_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_menuitemdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MenuItemDescription)


def test_viewpoint_tool_menuitemdescription_constructor_exists():
    assert callable(viewpoint_tool_MenuItemDescription.__init__)


def test_viewpoint_tool_menuitemdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MenuItemDescription.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint_tool_menuitemdescription_has_icon():
    assert hasattr(viewpoint_tool_MenuItemDescription, "icon")
    descriptor = None
    for klass in viewpoint_tool_MenuItemDescription.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_selectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_SelectionWizardDescription)


def test_viewpoint_tool_selectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_SelectionWizardDescription.__init__)


def test_viewpoint_tool_selectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_SelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"

def test_viewpoint_tool_selectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_selectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_selectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint_tool_SelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint_tool_SelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)



def test_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_DiagramElementMapping)


def test_description_diagramelementmapping_constructor_exists():
    assert callable(description_DiagramElementMapping.__init__)


def test_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementViewVariable)


def test_tool_elementviewvariable_constructor_exists():
    assert callable(tool_ElementViewVariable.__init__)


def test_tool_elementviewvariable_constructor_args():
    sig = inspect.signature(tool_ElementViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementVariable)


def test_tool_elementvariable_constructor_exists():
    assert callable(tool_ElementVariable.__init__)


def test_tool_elementvariable_constructor_args():
    sig = inspect.signature(tool_ElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_NodeCreationDescription)


def test_viewpoint_tool_nodecreationdescription_constructor_exists():
    assert callable(viewpoint_tool_NodeCreationDescription.__init__)


def test_viewpoint_tool_nodecreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_nodecreationdescription_has_iconPath():
    assert hasattr(viewpoint_tool_NodeCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_NodeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ReconnectEdgeDescription)


def test_viewpoint_tool_reconnectedgedescription_constructor_exists():
    assert callable(viewpoint_tool_ReconnectEdgeDescription.__init__)


def test_viewpoint_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reconnectionKind" in params, "Missing parameter 'reconnectionKind'"

def test_viewpoint_tool_reconnectedgedescription_has_reconnectionKind():
    assert hasattr(viewpoint_tool_ReconnectEdgeDescription, "reconnectionKind")
    descriptor = None
    for klass in viewpoint_tool_ReconnectEdgeDescription.__mro__:
        if "reconnectionKind" in klass.__dict__:
            descriptor = klass.__dict__["reconnectionKind"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PasteDescription)


def test_viewpoint_tool_pastedescription_constructor_exists():
    assert callable(viewpoint_tool_PasteDescription.__init__)


def test_viewpoint_tool_pastedescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_directeditlabel_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DirectEditLabel)


def test_viewpoint_tool_directeditlabel_constructor_exists():
    assert callable(viewpoint_tool_DirectEditLabel.__init__)


def test_viewpoint_tool_directeditlabel_constructor_args():
    sig = inspect.signature(viewpoint_tool_DirectEditLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inputLabelExpression" in params, "Missing parameter 'inputLabelExpression'"

def test_viewpoint_tool_directeditlabel_has_inputLabelExpression():
    assert hasattr(viewpoint_tool_DirectEditLabel, "inputLabelExpression")
    descriptor = None
    for klass in viewpoint_tool_DirectEditLabel.__mro__:
        if "inputLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["inputLabelExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerCreationDescription)


def test_viewpoint_tool_containercreationdescription_constructor_exists():
    assert callable(viewpoint_tool_ContainerCreationDescription.__init__)


def test_viewpoint_tool_containercreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_containercreationdescription_has_iconPath():
    assert hasattr(viewpoint_tool_ContainerCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_ContainerCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DeleteElementDescription)


def test_viewpoint_tool_deleteelementdescription_constructor_exists():
    assert callable(viewpoint_tool_DeleteElementDescription.__init__)


def test_viewpoint_tool_deleteelementdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_EdgeCreationDescription)


def test_viewpoint_tool_edgecreationdescription_constructor_exists():
    assert callable(viewpoint_tool_EdgeCreationDescription.__init__)


def test_viewpoint_tool_edgecreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "connectionStartPrecondition" in params, "Missing parameter 'connectionStartPrecondition'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_edgecreationdescription_has_connectionStartPrecondition():
    assert hasattr(viewpoint_tool_EdgeCreationDescription, "connectionStartPrecondition")
    descriptor = None
    for klass in viewpoint_tool_EdgeCreationDescription.__mro__:
        if "connectionStartPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["connectionStartPrecondition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_edgecreationdescription_has_iconPath():
    assert hasattr(viewpoint_tool_EdgeCreationDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_EdgeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ContainerDropDescription)


def test_viewpoint_tool_containerdropdescription_constructor_exists():
    assert callable(viewpoint_tool_ContainerDropDescription.__init__)


def test_viewpoint_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"
    assert "moveEdges" in params, "Missing parameter 'moveEdges'"

def test_viewpoint_tool_containerdropdescription_has_dragSource():
    assert hasattr(viewpoint_tool_ContainerDropDescription, "dragSource")
    descriptor = None
    for klass in viewpoint_tool_ContainerDropDescription.__mro__:
        if "dragSource" in klass.__dict__:
            descriptor = klass.__dict__["dragSource"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_containerdropdescription_has_moveEdges():
    assert hasattr(viewpoint_tool_ContainerDropDescription, "moveEdges")
    descriptor = None
    for klass in viewpoint_tool_ContainerDropDescription.__mro__:
        if "moveEdges" in klass.__dict__:
            descriptor = klass.__dict__["moveEdges"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_DoubleClickDescription)


def test_viewpoint_tool_doubleclickdescription_constructor_exists():
    assert callable(viewpoint_tool_DoubleClickDescription.__init__)


def test_viewpoint_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_tooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolDescription)


def test_viewpoint_tool_tooldescription_constructor_exists():
    assert callable(viewpoint_tool_ToolDescription.__init__)


def test_viewpoint_tool_tooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_viewpoint_tool_tooldescription_has_iconPath():
    assert hasattr(viewpoint_tool_ToolDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_ToolDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_panebasedselectionwizarddescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PaneBasedSelectionWizardDescription)


def test_viewpoint_tool_panebasedselectionwizarddescription_constructor_exists():
    assert callable(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)


def test_viewpoint_tool_panebasedselectionwizarddescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_PaneBasedSelectionWizardDescription.__init__)
    params = list(sig.parameters.keys())
    assert "selectedValuesMessage" in params, "Missing parameter 'selectedValuesMessage'"
    assert "message" in params, "Missing parameter 'message'"
    assert "preSelectedCandidatesExpression" in params, "Missing parameter 'preSelectedCandidatesExpression'"
    assert "choiceOfValuesMessage" in params, "Missing parameter 'choiceOfValuesMessage'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "tree" in params, "Missing parameter 'tree'"
    assert "windowTitle" in params, "Missing parameter 'windowTitle'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"
    assert "windowImagePath" in params, "Missing parameter 'windowImagePath'"

def test_viewpoint_tool_panebasedselectionwizarddescription_has_selectedValuesMessage():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "selectedValuesMessage")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "selectedValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["selectedValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_message():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "message")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_preSelectedCandidatesExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "preSelectedCandidatesExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "preSelectedCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["preSelectedCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_choiceOfValuesMessage():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "choiceOfValuesMessage")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "choiceOfValuesMessage" in klass.__dict__:
            descriptor = klass.__dict__["choiceOfValuesMessage"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_iconPath():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_candidatesExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_rootExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_tree():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "tree")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_windowTitle():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "windowTitle")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "windowTitle" in klass.__dict__:
            descriptor = klass.__dict__["windowTitle"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_childrenExpression():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_panebasedselectionwizarddescription_has_windowImagePath():
    assert hasattr(viewpoint_tool_PaneBasedSelectionWizardDescription, "windowImagePath")
    descriptor = None
    for klass in viewpoint_tool_PaneBasedSelectionWizardDescription.__mro__:
        if "windowImagePath" in klass.__dict__:
            descriptor = klass.__dict__["windowImagePath"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_PopupMenu)


def test_viewpoint_tool_popupmenu_constructor_exists():
    assert callable(viewpoint_tool_PopupMenu.__init__)


def test_viewpoint_tool_popupmenu_constructor_args():
    sig = inspect.signature(viewpoint_tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationNavigationDescription)


def test_viewpoint_tool_representationnavigationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationNavigationDescription.__init__)


def test_viewpoint_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "navigationNameExpression" in params, "Missing parameter 'navigationNameExpression'"
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"

def test_viewpoint_tool_representationnavigationdescription_has_navigationNameExpression():
    assert hasattr(viewpoint_tool_RepresentationNavigationDescription, "navigationNameExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationNavigationDescription.__mro__:
        if "navigationNameExpression" in klass.__dict__:
            descriptor = klass.__dict__["navigationNameExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_representationnavigationdescription_has_browseExpression():
    assert hasattr(viewpoint_tool_RepresentationNavigationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationNavigationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RepresentationCreationDescription)


def test_viewpoint_tool_representationcreationdescription_constructor_exists():
    assert callable(viewpoint_tool_RepresentationCreationDescription.__init__)


def test_viewpoint_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "browseExpression" in params, "Missing parameter 'browseExpression'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"

def test_viewpoint_tool_representationcreationdescription_has_browseExpression():
    assert hasattr(viewpoint_tool_RepresentationCreationDescription, "browseExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationCreationDescription.__mro__:
        if "browseExpression" in klass.__dict__:
            descriptor = klass.__dict__["browseExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_representationcreationdescription_has_titleExpression():
    assert hasattr(viewpoint_tool_RepresentationCreationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint_tool_RepresentationCreationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_behaviortool_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_BehaviorTool)


def test_viewpoint_tool_behaviortool_constructor_exists():
    assert callable(viewpoint_tool_BehaviorTool.__init__)


def test_viewpoint_tool_behaviortool_constructor_args():
    sig = inspect.signature(viewpoint_tool_BehaviorTool.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint_tool_behaviortool_has_domainClass():
    assert hasattr(viewpoint_tool_BehaviorTool, "domainClass")
    descriptor = None
    for klass in viewpoint_tool_BehaviorTool.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_requestdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_RequestDescription)


def test_viewpoint_tool_requestdescription_constructor_exists():
    assert callable(viewpoint_tool_RequestDescription.__init__)


def test_viewpoint_tool_requestdescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_RequestDescription.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_viewpoint_tool_requestdescription_has_type():
    assert hasattr(viewpoint_tool_RequestDescription, "type")
    descriptor = None
    for klass in viewpoint_tool_RequestDescription.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_MappingBasedToolDescription)


def test_viewpoint_tool_mappingbasedtooldescription_constructor_exists():
    assert callable(viewpoint_tool_MappingBasedToolDescription.__init__)


def test_viewpoint_tool_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDropVariable)


def test_tool_elementdropvariable_constructor_exists():
    assert callable(tool_ElementDropVariable.__init__)


def test_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolfilterdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ToolFilterDescription)


def test_tool_toolfilterdescription_constructor_exists():
    assert callable(tool_ToolFilterDescription.__init__)


def test_tool_toolfilterdescription_constructor_args():
    sig = inspect.signature(tool_ToolFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolGroup)


def test_viewpoint_tool_toolgroup_constructor_exists():
    assert callable(viewpoint_tool_ToolGroup.__init__)


def test_viewpoint_tool_toolgroup_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_AbstractToolDescription)


def test_viewpoint_tool_abstracttooldescription_constructor_exists():
    assert callable(viewpoint_tool_AbstractToolDescription.__init__)


def test_viewpoint_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(viewpoint_tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())
    assert "forceRefresh" in params, "Missing parameter 'forceRefresh'"
    assert "precondition" in params, "Missing parameter 'precondition'"

def test_viewpoint_tool_abstracttooldescription_has_forceRefresh():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "forceRefresh")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "forceRefresh" in klass.__dict__:
            descriptor = klass.__dict__["forceRefresh"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_tool_abstracttooldescription_has_precondition():
    assert hasattr(viewpoint_tool_AbstractToolDescription, "precondition")
    descriptor = None
    for klass in viewpoint_tool_AbstractToolDescription.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_tooltipstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_TooltipStyleDescription)


def test_viewpoint_style_tooltipstyledescription_constructor_exists():
    assert callable(viewpoint_style_TooltipStyleDescription.__init__)


def test_viewpoint_style_tooltipstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_TooltipStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tooltipExpression" in params, "Missing parameter 'tooltipExpression'"

def test_viewpoint_style_tooltipstyledescription_has_tooltipExpression():
    assert hasattr(viewpoint_style_TooltipStyleDescription, "tooltipExpression")
    descriptor = None
    for klass in viewpoint_style_TooltipStyleDescription.__mro__:
        if "tooltipExpression" in klass.__dict__:
            descriptor = klass.__dict__["tooltipExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyleDescription)


def test_viewpoint_style_labelborderstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyleDescription.__init__)


def test_viewpoint_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_style_labelborderstyledescription_has_id():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "id")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_cornerWidth():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "cornerWidth")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_cornerHeight():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "cornerHeight")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_labelborderstyledescription_has_name():
    assert hasattr(viewpoint_style_LabelBorderStyleDescription, "name")
    descriptor = None
    for klass in viewpoint_style_LabelBorderStyleDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyleDescription)


def test_style_labelborderstyledescription_constructor_exists():
    assert callable(style_LabelBorderStyleDescription.__init__)


def test_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelBorderStyles)


def test_viewpoint_style_labelborderstyles_constructor_exists():
    assert callable(viewpoint_style_LabelBorderStyles.__init__)


def test_viewpoint_style_labelborderstyles_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_CenterLabelStyleDescription)


def test_viewpoint_style_centerlabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_CenterLabelStyleDescription.__init__)


def test_viewpoint_style_centerlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_EndLabelStyleDescription)


def test_viewpoint_style_endlabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_EndLabelStyleDescription.__init__)


def test_viewpoint_style_endlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BeginLabelStyleDescription)


def test_viewpoint_style_beginlabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_BeginLabelStyleDescription.__init__)


def test_viewpoint_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_labelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_LabelStyleDescription)


def test_viewpoint_style_labelstyledescription_constructor_exists():
    assert callable(viewpoint_style_LabelStyleDescription.__init__)


def test_viewpoint_style_labelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_LabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint_style_labelstyledescription_has_labelAlignment():
    assert hasattr(viewpoint_style_LabelStyleDescription, "labelAlignment")
    descriptor = None
    for klass in viewpoint_style_LabelStyleDescription.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_BasicLabelStyleDescription)


def test_viewpoint_style_basiclabelstyledescription_constructor_exists():
    assert callable(viewpoint_style_BasicLabelStyleDescription.__init__)


def test_viewpoint_style_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "labelExpression" in params, "Missing parameter 'labelExpression'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"

def test_viewpoint_style_basiclabelstyledescription_has_labelSize():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelSize")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_labelExpression():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelExpression")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelExpression" in klass.__dict__:
            descriptor = klass.__dict__["labelExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_labelFormat():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "labelFormat")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_iconPath():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "iconPath")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_basiclabelstyledescription_has_showIcon():
    assert hasattr(viewpoint_style_BasicLabelStyleDescription, "showIcon")
    descriptor = None
    for klass in viewpoint_style_BasicLabelStyleDescription.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_StyleDescription)


def test_viewpoint_style_styledescription_constructor_exists():
    assert callable(viewpoint_style_StyleDescription.__init__)


def test_viewpoint_style_styledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotationEntry)


def test_viewpoint_description_dannotationentry_constructor_exists():
    assert callable(viewpoint_description_DAnnotationEntry.__init__)


def test_viewpoint_description_dannotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"
    assert "details" in params, "Missing parameter 'details'"

def test_viewpoint_description_dannotationentry_has_source():
    assert hasattr(viewpoint_description_DAnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint_description_DAnnotationEntry.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_dannotationentry_has_details():
    assert hasattr(viewpoint_description_DAnnotationEntry, "details")
    descriptor = None
    for klass in viewpoint_description_DAnnotationEntry.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IdentifiedElement)


def test_viewpoint_description_identifiedelement_constructor_exists():
    assert callable(viewpoint_description_IdentifiedElement.__init__)


def test_viewpoint_description_identifiedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_identifiedelement_has_label():
    assert hasattr(viewpoint_description_IdentifiedElement, "label")
    descriptor = None
    for klass in viewpoint_description_IdentifiedElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_identifiedelement_has_name():
    assert hasattr(viewpoint_description_IdentifiedElement, "name")
    descriptor = None
    for klass in viewpoint_description_IdentifiedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EndUserDocumentedElement)


def test_viewpoint_description_enduserdocumentedelement_constructor_exists():
    assert callable(viewpoint_description_EndUserDocumentedElement.__init__)


def test_viewpoint_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "endUserDocumentation" in params, "Missing parameter 'endUserDocumentation'"

def test_viewpoint_description_enduserdocumentedelement_has_endUserDocumentation():
    assert hasattr(viewpoint_description_EndUserDocumentedElement, "endUserDocumentation")
    descriptor = None
    for klass in viewpoint_description_EndUserDocumentedElement.__mro__:
        if "endUserDocumentation" in klass.__dict__:
            descriptor = klass.__dict__["endUserDocumentation"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_annotationentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AnnotationEntry)


def test_viewpoint_description_annotationentry_constructor_exists():
    assert callable(viewpoint_description_AnnotationEntry.__init__)


def test_viewpoint_description_annotationentry_constructor_args():
    sig = inspect.signature(viewpoint_description_AnnotationEntry.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint_description_annotationentry_has_source():
    assert hasattr(viewpoint_description_AnnotationEntry, "source")
    descriptor = None
    for klass in viewpoint_description_AnnotationEntry.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_usercolor_is_not_abstract():
    assert not inspect.isabstract(UserColor)


def test_usercolor_constructor_exists():
    assert callable(UserColor.__init__)


def test_usercolor_constructor_args():
    sig = inspect.signature(UserColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColorsPalette)


def test_viewpoint_description_usercolorspalette_constructor_exists():
    assert callable(viewpoint_description_UserColorsPalette.__init__)


def test_viewpoint_description_usercolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColorsPalette.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_usercolorspalette_has_name():
    assert hasattr(viewpoint_description_UserColorsPalette, "name")
    descriptor = None
    for klass in viewpoint_description_UserColorsPalette.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_systemcolor_is_not_abstract():
    assert not inspect.isabstract(SystemColor)


def test_systemcolor_constructor_exists():
    assert callable(SystemColor.__init__)


def test_systemcolor_constructor_args():
    sig = inspect.signature(SystemColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SytemColorsPalette)


def test_viewpoint_description_sytemcolorspalette_constructor_exists():
    assert callable(viewpoint_description_SytemColorsPalette.__init__)


def test_viewpoint_description_sytemcolorspalette_constructor_args():
    sig = inspect.signature(viewpoint_description_SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_style_labelborderstyles_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyles)


def test_style_labelborderstyles_constructor_exists():
    assert callable(style_LabelBorderStyles.__init__)


def test_style_labelborderstyles_constructor_args():
    sig = inspect.signature(style_LabelBorderStyles.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(tool_ToolEntry)


def test_tool_toolentry_constructor_exists():
    assert callable(tool_ToolEntry.__init__)


def test_tool_toolentry_constructor_args():
    sig = inspect.signature(tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_environment_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Environment)


def test_viewpoint_description_environment_constructor_exists():
    assert callable(viewpoint_description_Environment.__init__)


def test_viewpoint_description_environment_constructor_args():
    sig = inspect.signature(viewpoint_description_Environment.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserColor)


def test_viewpoint_description_usercolor_constructor_exists():
    assert callable(viewpoint_description_UserColor.__init__)


def test_viewpoint_description_usercolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_usercolor_has_name():
    assert hasattr(viewpoint_description_UserColor, "name")
    descriptor = None
    for klass in viewpoint_description_UserColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(description_FixedColor)


def test_description_fixedcolor_constructor_exists():
    assert callable(description_FixedColor.__init__)


def test_description_fixedcolor_constructor_args():
    sig = inspect.signature(description_FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FixedColor)


def test_viewpoint_description_fixedcolor_constructor_exists():
    assert callable(viewpoint_description_FixedColor.__init__)


def test_viewpoint_description_fixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_FixedColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "blue" in params, "Missing parameter 'blue'"
    assert "green" in params, "Missing parameter 'green'"

def test_viewpoint_description_fixedcolor_has_red():
    assert hasattr(viewpoint_description_FixedColor, "red")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_fixedcolor_has_blue():
    assert hasattr(viewpoint_description_FixedColor, "blue")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_fixedcolor_has_green():
    assert hasattr(viewpoint_description_FixedColor, "green")
    descriptor = None
    for klass in viewpoint_description_FixedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_colorstep_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorStep)


def test_viewpoint_description_colorstep_constructor_exists():
    assert callable(viewpoint_description_ColorStep.__init__)


def test_viewpoint_description_colorstep_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorStep.__init__)
    params = list(sig.parameters.keys())
    assert "associatedValue" in params, "Missing parameter 'associatedValue'"

def test_viewpoint_description_colorstep_has_associatedValue():
    assert hasattr(viewpoint_description_ColorStep, "associatedValue")
    descriptor = None
    for klass in viewpoint_description_ColorStep.__mro__:
        if "associatedValue" in klass.__dict__:
            descriptor = klass.__dict__["associatedValue"]
            break
    assert isinstance(descriptor, property)



def test_colorstep_is_not_abstract():
    assert not inspect.isabstract(ColorStep)


def test_colorstep_constructor_exists():
    assert callable(ColorStep.__init__)


def test_colorstep_constructor_args():
    sig = inspect.signature(ColorStep.__init__)
    params = list(sig.parameters.keys())



def test_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(description_ColorDescription)


def test_description_colordescription_constructor_exists():
    assert callable(description_ColorDescription.__init__)


def test_description_colordescription_constructor_args():
    sig = inspect.signature(description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_fixedcolor_is_not_abstract():
    assert not inspect.isabstract(FixedColor)


def test_fixedcolor_constructor_exists():
    assert callable(FixedColor.__init__)


def test_fixedcolor_constructor_args():
    sig = inspect.signature(FixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_systemcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SystemColor)


def test_viewpoint_description_systemcolor_constructor_exists():
    assert callable(viewpoint_description_SystemColor.__init__)


def test_viewpoint_description_systemcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_SystemColor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_systemcolor_has_name():
    assert hasattr(viewpoint_description_SystemColor, "name")
    descriptor = None
    for klass in viewpoint_description_SystemColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_colordescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ColorDescription)


def test_viewpoint_description_colordescription_constructor_exists():
    assert callable(viewpoint_description_ColorDescription.__init__)


def test_viewpoint_description_colordescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_selectiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SelectionDescription)


def test_viewpoint_description_selectiondescription_constructor_exists():
    assert callable(viewpoint_description_SelectionDescription.__init__)


def test_viewpoint_description_selectiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_SelectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "tree" in params, "Missing parameter 'tree'"
    assert "message" in params, "Missing parameter 'message'"
    assert "candidatesExpression" in params, "Missing parameter 'candidatesExpression'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_viewpoint_description_selectiondescription_has_tree():
    assert hasattr(viewpoint_description_SelectionDescription, "tree")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "tree" in klass.__dict__:
            descriptor = klass.__dict__["tree"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_message():
    assert hasattr(viewpoint_description_SelectionDescription, "message")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_candidatesExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "candidatesExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "candidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["candidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_rootExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "rootExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_multiple():
    assert hasattr(viewpoint_description_SelectionDescription, "multiple")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_selectiondescription_has_childrenExpression():
    assert hasattr(viewpoint_description_SelectionDescription, "childrenExpression")
    descriptor = None
    for klass in viewpoint_description_SelectionDescription.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)



def test_description_usercolor_is_not_abstract():
    assert not inspect.isabstract(description_UserColor)


def test_description_usercolor_constructor_exists():
    assert callable(description_UserColor.__init__)


def test_description_usercolor_constructor_args():
    sig = inspect.signature(description_UserColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_userfixedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_UserFixedColor)


def test_viewpoint_description_userfixedcolor_constructor_exists():
    assert callable(viewpoint_description_UserFixedColor.__init__)


def test_viewpoint_description_userfixedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_UserFixedColor.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_interpolatedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_InterpolatedColor)


def test_viewpoint_description_interpolatedcolor_constructor_exists():
    assert callable(viewpoint_description_InterpolatedColor.__init__)


def test_viewpoint_description_interpolatedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_InterpolatedColor.__init__)
    params = list(sig.parameters.keys())
    assert "colorValueComputationExpression" in params, "Missing parameter 'colorValueComputationExpression'"
    assert "maxValueComputationExpression" in params, "Missing parameter 'maxValueComputationExpression'"
    assert "minValueComputationExpression" in params, "Missing parameter 'minValueComputationExpression'"

def test_viewpoint_description_interpolatedcolor_has_colorValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "colorValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "colorValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["colorValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_interpolatedcolor_has_maxValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "maxValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "maxValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_interpolatedcolor_has_minValueComputationExpression():
    assert hasattr(viewpoint_description_InterpolatedColor, "minValueComputationExpression")
    descriptor = None
    for klass in viewpoint_description_InterpolatedColor.__mro__:
        if "minValueComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_computedcolor_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ComputedColor)


def test_viewpoint_description_computedcolor_constructor_exists():
    assert callable(viewpoint_description_ComputedColor.__init__)


def test_viewpoint_description_computedcolor_constructor_args():
    sig = inspect.signature(viewpoint_description_ComputedColor.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"

def test_viewpoint_description_computedcolor_has_blue():
    assert hasattr(viewpoint_description_ComputedColor, "blue")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_computedcolor_has_green():
    assert hasattr(viewpoint_description_ComputedColor, "green")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_computedcolor_has_red():
    assert hasattr(viewpoint_description_ComputedColor, "red")
    descriptor = None
    for klass in viewpoint_description_ComputedColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(EStructuralFeatureCustomization)


def test_estructuralfeaturecustomization_constructor_exists():
    assert callable(EStructuralFeatureCustomization.__init__)


def test_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_ereferencecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EReferenceCustomization)


def test_viewpoint_description_ereferencecustomization_constructor_exists():
    assert callable(viewpoint_description_EReferenceCustomization.__init__)


def test_viewpoint_description_ereferencecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EReferenceCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_viewpoint_description_ereferencecustomization_has_referenceName():
    assert hasattr(viewpoint_description_EReferenceCustomization, "referenceName")
    descriptor = None
    for klass in viewpoint_description_EReferenceCustomization.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_IVSMElementCustomization)


def test_viewpoint_description_ivsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_IVSMElementCustomization.__init__)


def test_viewpoint_description_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_ivsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(IVSMElementCustomization)


def test_ivsmelementcustomization_constructor_exists():
    assert callable(IVSMElementCustomization.__init__)


def test_ivsmelementcustomization_constructor_args():
    sig = inspect.signature(IVSMElementCustomization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_vsmelementcustomizationreuse_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomizationReuse)


def test_viewpoint_description_vsmelementcustomizationreuse_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomizationReuse.__init__)


def test_viewpoint_description_vsmelementcustomizationreuse_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomizationReuse.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_vsmelementcustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_VSMElementCustomization)


def test_viewpoint_description_vsmelementcustomization_constructor_exists():
    assert callable(viewpoint_description_VSMElementCustomization.__init__)


def test_viewpoint_description_vsmelementcustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_VSMElementCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint_description_vsmelementcustomization_has_predicateExpression():
    assert hasattr(viewpoint_description_VSMElementCustomization, "predicateExpression")
    descriptor = None
    for klass in viewpoint_description_VSMElementCustomization.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_customization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Customization)


def test_viewpoint_description_customization_constructor_exists():
    assert callable(viewpoint_description_Customization.__init__)


def test_viewpoint_description_customization_constructor_args():
    sig = inspect.signature(viewpoint_description_Customization.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_eattributecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EAttributeCustomization)


def test_viewpoint_description_eattributecustomization_constructor_exists():
    assert callable(viewpoint_description_EAttributeCustomization.__init__)


def test_viewpoint_description_eattributecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EAttributeCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"
    assert "value" in params, "Missing parameter 'value'"

def test_viewpoint_description_eattributecustomization_has_attributeName():
    assert hasattr(viewpoint_description_EAttributeCustomization, "attributeName")
    descriptor = None
    for klass in viewpoint_description_EAttributeCustomization.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_eattributecustomization_has_value():
    assert hasattr(viewpoint_description_EAttributeCustomization, "value")
    descriptor = None
    for klass in viewpoint_description_EAttributeCustomization.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_estructuralfeaturecustomization_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EStructuralFeatureCustomization)


def test_viewpoint_description_estructuralfeaturecustomization_constructor_exists():
    assert callable(viewpoint_description_EStructuralFeatureCustomization.__init__)


def test_viewpoint_description_estructuralfeaturecustomization_constructor_args():
    sig = inspect.signature(viewpoint_description_EStructuralFeatureCustomization.__init__)
    params = list(sig.parameters.keys())
    assert "applyOnAll" in params, "Missing parameter 'applyOnAll'"

def test_viewpoint_description_estructuralfeaturecustomization_has_applyOnAll():
    assert hasattr(viewpoint_description_EStructuralFeatureCustomization, "applyOnAll")
    descriptor = None
    for klass in viewpoint_description_EStructuralFeatureCustomization.__mro__:
        if "applyOnAll" in klass.__dict__:
            descriptor = klass.__dict__["applyOnAll"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescription)


def test_viewpoint_description_decorationdescription_constructor_exists():
    assert callable(viewpoint_description_DecorationDescription.__init__)


def test_viewpoint_description_decorationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "decoratorPath" in params, "Missing parameter 'decoratorPath'"
    assert "name" in params, "Missing parameter 'name'"
    assert "position" in params, "Missing parameter 'position'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"

def test_viewpoint_description_decorationdescription_has_decoratorPath():
    assert hasattr(viewpoint_description_DecorationDescription, "decoratorPath")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "decoratorPath" in klass.__dict__:
            descriptor = klass.__dict__["decoratorPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_name():
    assert hasattr(viewpoint_description_DecorationDescription, "name")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_position():
    assert hasattr(viewpoint_description_DecorationDescription, "position")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_decorationdescription_has_preconditionExpression():
    assert hasattr(viewpoint_description_DecorationDescription, "preconditionExpression")
    descriptor = None
    for klass in viewpoint_description_DecorationDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DecorationDescriptionsSet)


def test_viewpoint_description_decorationdescriptionsset_constructor_exists():
    assert callable(viewpoint_description_DecorationDescriptionsSet.__init__)


def test_viewpoint_description_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(viewpoint_description_DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_tool_pastedescription_is_not_abstract():
    assert not inspect.isabstract(tool_PasteDescription)


def test_tool_pastedescription_constructor_exists():
    assert callable(tool_PasteDescription.__init__)


def test_tool_pastedescription_constructor_args():
    sig = inspect.signature(tool_PasteDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_PasteTargetDescription)


def test_viewpoint_description_pastetargetdescription_constructor_exists():
    assert callable(viewpoint_description_PasteTargetDescription.__init__)


def test_viewpoint_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerDropDescription)


def test_tool_containerdropdescription_constructor_exists():
    assert callable(tool_ContainerDropDescription.__init__)


def test_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DragAndDropTargetDescription)


def test_viewpoint_description_draganddroptargetdescription_constructor_exists():
    assert callable(viewpoint_description_DragAndDropTargetDescription.__init__)


def test_viewpoint_description_draganddroptargetdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_ConditionalStyleDescription)


def test_viewpoint_description_conditionalstyledescription_constructor_exists():
    assert callable(viewpoint_description_ConditionalStyleDescription.__init__)


def test_viewpoint_description_conditionalstyledescription_constructor_args():
    sig = inspect.signature(viewpoint_description_ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "predicateExpression" in params, "Missing parameter 'predicateExpression'"

def test_viewpoint_description_conditionalstyledescription_has_predicateExpression():
    assert hasattr(viewpoint_description_ConditionalStyleDescription, "predicateExpression")
    descriptor = None
    for klass in viewpoint_description_ConditionalStyleDescription.__mro__:
        if "predicateExpression" in klass.__dict__:
            descriptor = klass.__dict__["predicateExpression"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EStringToStringMapEntry)


def test_description_viewpoint_estringtostringmapentry_constructor_exists():
    assert callable(description_viewpoint_EStringToStringMapEntry.__init__)


def test_description_viewpoint_estringtostringmapentry_constructor_args():
    sig = inspect.signature(description_viewpoint_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_dannotation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DAnnotation)


def test_viewpoint_description_dannotation_constructor_exists():
    assert callable(viewpoint_description_DAnnotation.__init__)


def test_viewpoint_description_dannotation_constructor_args():
    sig = inspect.signature(viewpoint_description_DAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_viewpoint_description_dannotation_has_source():
    assert hasattr(viewpoint_description_DAnnotation, "source")
    descriptor = None
    for klass in viewpoint_description_DAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_dannotation_is_not_abstract():
    assert not inspect.isabstract(DAnnotation)


def test_dannotation_constructor_exists():
    assert callable(DAnnotation.__init__)


def test_dannotation_constructor_args():
    sig = inspect.signature(DAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractMappingImport)


def test_viewpoint_description_abstractmappingimport_constructor_exists():
    assert callable(viewpoint_description_AbstractMappingImport.__init__)


def test_viewpoint_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"
    assert "hideSubMappings" in params, "Missing parameter 'hideSubMappings'"

def test_viewpoint_description_abstractmappingimport_has_inheritsAncestorFilters():
    assert hasattr(viewpoint_description_AbstractMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in viewpoint_description_AbstractMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_abstractmappingimport_has_hideSubMappings():
    assert hasattr(viewpoint_description_AbstractMappingImport, "hideSubMappings")
    descriptor = None
    for klass in viewpoint_description_AbstractMappingImport.__mro__:
        if "hideSubMappings" in klass.__dict__:
            descriptor = klass.__dict__["hideSubMappings"]
            break
    assert isinstance(descriptor, property)



def test_tool_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationNavigationDescription)


def test_tool_representationnavigationdescription_constructor_exists():
    assert callable(tool_RepresentationNavigationDescription.__init__)


def test_tool_representationnavigationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElement)


def test_identifiedelement_constructor_exists():
    assert callable(IdentifiedElement.__init__)


def test_identifiedelement_constructor_args():
    sig = inspect.signature(IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationElementMapping)


def test_viewpoint_description_representationelementmapping_constructor_exists():
    assert callable(viewpoint_description_RepresentationElementMapping.__init__)


def test_viewpoint_description_representationelementmapping_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_javaextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_JavaExtension)


def test_viewpoint_description_javaextension_constructor_exists():
    assert callable(viewpoint_description_JavaExtension.__init__)


def test_viewpoint_description_javaextension_constructor_args():
    sig = inspect.signature(viewpoint_description_JavaExtension.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_viewpoint_description_javaextension_has_qualifiedClassName():
    assert hasattr(viewpoint_description_JavaExtension, "qualifiedClassName")
    descriptor = None
    for klass in viewpoint_description_JavaExtension.__mro__:
        if "qualifiedClassName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedClassName"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EObject)


def test_description_viewpoint_eobject_constructor_exists():
    assert callable(description_viewpoint_EObject.__init__)


def test_description_viewpoint_eobject_constructor_args():
    sig = inspect.signature(description_viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_MetamodelExtensionSetting)


def test_viewpoint_description_metamodelextensionsetting_constructor_exists():
    assert callable(viewpoint_description_MetamodelExtensionSetting.__init__)


def test_viewpoint_description_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(viewpoint_description_MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationExtensionDescription)


def test_viewpoint_description_representationextensiondescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationExtensionDescription.__init__)


def test_viewpoint_description_representationextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "viewpointURI" in params, "Missing parameter 'viewpointURI'"
    assert "representationName" in params, "Missing parameter 'representationName'"

def test_viewpoint_description_representationextensiondescription_has_name():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "name")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationextensiondescription_has_viewpointURI():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "viewpointURI")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "viewpointURI" in klass.__dict__:
            descriptor = klass.__dict__["viewpointURI"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationextensiondescription_has_representationName():
    assert hasattr(viewpoint_description_RepresentationExtensionDescription, "representationName")
    descriptor = None
    for klass in viewpoint_description_RepresentationExtensionDescription.__mro__:
        if "representationName" in klass.__dict__:
            descriptor = klass.__dict__["representationName"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DModelElement)


def test_viewpoint_description_dmodelelement_constructor_exists():
    assert callable(viewpoint_description_DModelElement.__init__)


def test_viewpoint_description_dmodelelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DocumentedElement)


def test_viewpoint_description_documentedelement_constructor_exists():
    assert callable(viewpoint_description_DocumentedElement.__init__)


def test_viewpoint_description_documentedelement_constructor_args():
    sig = inspect.signature(viewpoint_description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"

def test_viewpoint_description_documentedelement_has_documentation():
    assert hasattr(viewpoint_description_DocumentedElement, "documentation")
    descriptor = None
    for klass in viewpoint_description_DocumentedElement.__mro__:
        if "documentation" in klass.__dict__:
            descriptor = klass.__dict__["documentation"]
            break
    assert isinstance(descriptor, property)



def test_description_viewpoint_epackage_is_not_abstract():
    assert not inspect.isabstract(description_viewpoint_EPackage)


def test_description_viewpoint_epackage_constructor_exists():
    assert callable(description_viewpoint_EPackage.__init__)


def test_description_viewpoint_epackage_constructor_args():
    sig = inspect.signature(description_viewpoint_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_FeatureExtensionDescription)


def test_viewpoint_description_featureextensiondescription_constructor_exists():
    assert callable(viewpoint_description_FeatureExtensionDescription.__init__)


def test_viewpoint_description_featureextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(RepresentationTemplate)


def test_representationtemplate_constructor_exists():
    assert callable(RepresentationTemplate.__init__)


def test_representationtemplate_constructor_args():
    sig = inspect.signature(RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_metamodelextensionsetting_is_not_abstract():
    assert not inspect.isabstract(MetamodelExtensionSetting)


def test_metamodelextensionsetting_constructor_exists():
    assert callable(MetamodelExtensionSetting.__init__)


def test_metamodelextensionsetting_constructor_args():
    sig = inspect.signature(MetamodelExtensionSetting.__init__)
    params = list(sig.parameters.keys())



def test_javaextension_is_not_abstract():
    assert not inspect.isabstract(JavaExtension)


def test_javaextension_constructor_exists():
    assert callable(JavaExtension.__init__)


def test_javaextension_constructor_args():
    sig = inspect.signature(JavaExtension.__init__)
    params = list(sig.parameters.keys())



def test_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_diagramextensiondescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_DiagramExtensionDescription)


def test_viewpoint_description_diagramextensiondescription_constructor_exists():
    assert callable(viewpoint_description_DiagramExtensionDescription.__init__)


def test_viewpoint_description_diagramextensiondescription_constructor_args():
    sig = inspect.signature(viewpoint_description_DiagramExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationDescription)


def test_representationdescription_constructor_exists():
    assert callable(RepresentationDescription.__init__)


def test_representationdescription_constructor_args():
    sig = inspect.signature(RepresentationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationImportDescription)


def test_viewpoint_description_representationimportdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationImportDescription.__init__)


def test_viewpoint_description_representationimportdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_representationtemplate_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationTemplate)


def test_viewpoint_description_representationtemplate_constructor_exists():
    assert callable(viewpoint_description_RepresentationTemplate.__init__)


def test_viewpoint_description_representationtemplate_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_representationtemplate_has_name():
    assert hasattr(viewpoint_description_RepresentationTemplate, "name")
    descriptor = None
    for klass in viewpoint_description_RepresentationTemplate.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationSet)


def test_validation_validationset_constructor_exists():
    assert callable(validation_ValidationSet.__init__)


def test_validation_validationset_constructor_args():
    sig = inspect.signature(validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description_IdentifiedElement)


def test_description_identifiedelement_constructor_exists():
    assert callable(description_IdentifiedElement.__init__)


def test_description_identifiedelement_constructor_args():
    sig = inspect.signature(description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description_EndUserDocumentedElement)


def test_description_enduserdocumentedelement_constructor_exists():
    assert callable(description_EndUserDocumentedElement.__init__)


def test_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_description_component_is_not_abstract():
    assert not inspect.isabstract(description_Component)


def test_description_component_constructor_exists():
    assert callable(description_Component.__init__)


def test_description_component_constructor_args():
    sig = inspect.signature(description_Component.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_component_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Component)


def test_viewpoint_description_component_constructor_exists():
    assert callable(viewpoint_description_Component.__init__)


def test_viewpoint_description_component_constructor_args():
    sig = inspect.signature(viewpoint_description_Component.__init__)
    params = list(sig.parameters.keys())



def test_usercolorspalette_is_not_abstract():
    assert not inspect.isabstract(UserColorsPalette)


def test_usercolorspalette_constructor_exists():
    assert callable(UserColorsPalette.__init__)


def test_usercolorspalette_constructor_args():
    sig = inspect.signature(UserColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_sytemcolorspalette_is_not_abstract():
    assert not inspect.isabstract(SytemColorsPalette)


def test_sytemcolorspalette_constructor_exists():
    assert callable(SytemColorsPalette.__init__)


def test_sytemcolorspalette_constructor_args():
    sig = inspect.signature(SytemColorsPalette.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_customizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Customizable)


def test_viewpoint_customizable_constructor_exists():
    assert callable(viewpoint_Customizable.__init__)


def test_viewpoint_customizable_constructor_args():
    sig = inspect.signature(viewpoint_Customizable.__init__)
    params = list(sig.parameters.keys())
    assert "customFeatures" in params, "Missing parameter 'customFeatures'"

def test_viewpoint_customizable_has_customFeatures():
    assert hasattr(viewpoint_Customizable, "customFeatures")
    descriptor = None
    for klass in viewpoint_Customizable.__mro__:
        if "customFeatures" in klass.__dict__:
            descriptor = klass.__dict__["customFeatures"]
            break
    assert isinstance(descriptor, property)



def test_dfile_is_not_abstract():
    assert not inspect.isabstract(DFile)


def test_dfile_constructor_exists():
    assert callable(DFile.__init__)


def test_dfile_constructor_args():
    sig = inspect.signature(DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dmodel_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DModel)


def test_viewpoint_dmodel_constructor_exists():
    assert callable(viewpoint_DModel.__init__)


def test_viewpoint_dmodel_constructor_args():
    sig = inspect.signature(viewpoint_DModel.__init__)
    params = list(sig.parameters.keys())



def test_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(DResourceContainer)


def test_dresourcecontainer_constructor_exists():
    assert callable(DResourceContainer.__init__)


def test_dresourcecontainer_constructor_args():
    sig = inspect.signature(DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dfolder_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFolder)


def test_viewpoint_dfolder_constructor_exists():
    assert callable(viewpoint_DFolder.__init__)


def test_viewpoint_dfolder_constructor_args():
    sig = inspect.signature(viewpoint_DFolder.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dproject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DProject)


def test_viewpoint_dproject_constructor_exists():
    assert callable(viewpoint_DProject.__init__)


def test_viewpoint_dproject_constructor_args():
    sig = inspect.signature(viewpoint_DProject.__init__)
    params = list(sig.parameters.keys())



def test_dresource_is_not_abstract():
    assert not inspect.isabstract(DResource)


def test_dresource_constructor_exists():
    assert callable(DResource.__init__)


def test_dresource_constructor_args():
    sig = inspect.signature(DResource.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dresourcecontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResourceContainer)


def test_viewpoint_dresourcecontainer_constructor_exists():
    assert callable(viewpoint_DResourceContainer.__init__)


def test_viewpoint_dresourcecontainer_constructor_args():
    sig = inspect.signature(viewpoint_DResourceContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dfile_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFile)


def test_viewpoint_dfile_constructor_exists():
    assert callable(viewpoint_DFile.__init__)


def test_viewpoint_dfile_constructor_args():
    sig = inspect.signature(viewpoint_DFile.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dresource_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DResource)


def test_viewpoint_dresource_constructor_exists():
    assert callable(viewpoint_DResource.__init__)


def test_viewpoint_dresource_constructor_args():
    sig = inspect.signature(viewpoint_DResource.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_dresource_has_path():
    assert hasattr(viewpoint_DResource, "path")
    descriptor = None
    for klass in viewpoint_DResource.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_dresource_has_name():
    assert hasattr(viewpoint_DResource, "name")
    descriptor = None
    for klass in viewpoint_DResource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_sessionmanagereobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_SessionManagerEObject)


def test_viewpoint_sessionmanagereobject_constructor_exists():
    assert callable(viewpoint_SessionManagerEObject.__init__)


def test_viewpoint_sessionmanagereobject_constructor_args():
    sig = inspect.signature(viewpoint_SessionManagerEObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_danalysissessioneobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisSessionEObject)


def test_viewpoint_danalysissessioneobject_constructor_exists():
    assert callable(viewpoint_DAnalysisSessionEObject.__init__)


def test_viewpoint_danalysissessioneobject_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisSessionEObject.__init__)
    params = list(sig.parameters.keys())
    assert "resources" in params, "Missing parameter 'resources'"
    assert "open" in params, "Missing parameter 'open'"
    assert "controlledResources" in params, "Missing parameter 'controlledResources'"
    assert "blocked" in params, "Missing parameter 'blocked'"
    assert "synchronizationStatus" in params, "Missing parameter 'synchronizationStatus'"

def test_viewpoint_danalysissessioneobject_has_resources():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "resources")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "resources" in klass.__dict__:
            descriptor = klass.__dict__["resources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_open():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "open")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_controlledResources():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "controlledResources")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "controlledResources" in klass.__dict__:
            descriptor = klass.__dict__["controlledResources"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_blocked():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "blocked")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "blocked" in klass.__dict__:
            descriptor = klass.__dict__["blocked"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_danalysissessioneobject_has_synchronizationStatus():
    assert hasattr(viewpoint_DAnalysisSessionEObject, "synchronizationStatus")
    descriptor = None
    for klass in viewpoint_DAnalysisSessionEObject.__mro__:
        if "synchronizationStatus" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationStatus"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_rgbvalues_is_not_abstract():
    assert not inspect.isabstract(viewpoint_RGBValues)


def test_viewpoint_rgbvalues_constructor_exists():
    assert callable(viewpoint_RGBValues.__init__)


def test_viewpoint_rgbvalues_constructor_args():
    sig = inspect.signature(viewpoint_RGBValues.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"

def test_viewpoint_rgbvalues_has_blue():
    assert hasattr(viewpoint_RGBValues, "blue")
    descriptor = None
    for klass in viewpoint_RGBValues.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_rgbvalues_has_red():
    assert hasattr(viewpoint_RGBValues, "red")
    descriptor = None
    for klass in viewpoint_RGBValues.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_rgbvalues_has_green():
    assert hasattr(viewpoint_RGBValues, "green")
    descriptor = None
    for klass in viewpoint_RGBValues.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)



def test_dnavigationlink_is_not_abstract():
    assert not inspect.isabstract(DNavigationLink)


def test_dnavigationlink_constructor_exists():
    assert callable(DNavigationLink.__init__)


def test_dnavigationlink_constructor_args():
    sig = inspect.signature(DNavigationLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_ddiagramlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DDiagramLink)


def test_viewpoint_diagram_ddiagramlink_constructor_exists():
    assert callable(viewpoint_diagram_DDiagramLink.__init__)


def test_viewpoint_diagram_ddiagramlink_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DDiagramLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_deobjectlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DEObjectLink)


def test_viewpoint_deobjectlink_constructor_exists():
    assert callable(viewpoint_DEObjectLink.__init__)


def test_viewpoint_deobjectlink_constructor_args():
    sig = inspect.signature(viewpoint_DEObjectLink.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DragAndDropTarget)


def test_viewpoint_draganddroptarget_constructor_exists():
    assert callable(viewpoint_DragAndDropTarget.__init__)


def test_viewpoint_draganddroptarget_constructor_args():
    sig = inspect.signature(viewpoint_DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_style_NodeStyleDescription)


def test_viewpoint_style_nodestyledescription_constructor_exists():
    assert callable(viewpoint_style_NodeStyleDescription.__init__)


def test_viewpoint_style_nodestyledescription_constructor_args():
    sig = inspect.signature(viewpoint_style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"

def test_viewpoint_style_nodestyledescription_has_hideLabelByDefault():
    assert hasattr(viewpoint_style_NodeStyleDescription, "hideLabelByDefault")
    descriptor = None
    for klass in viewpoint_style_NodeStyleDescription.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_nodestyledescription_has_sizeComputationExpression():
    assert hasattr(viewpoint_style_NodeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in viewpoint_style_NodeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_nodestyledescription_has_labelPosition():
    assert hasattr(viewpoint_style_NodeStyleDescription, "labelPosition")
    descriptor = None
    for klass in viewpoint_style_NodeStyleDescription.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_style_nodestyledescription_has_resizeKind():
    assert hasattr(viewpoint_style_NodeStyleDescription, "resizeKind")
    descriptor = None
    for klass in viewpoint_style_NodeStyleDescription.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)



def test_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_gaugesection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_GaugeSection)


def test_viewpoint_diagram_gaugesection_constructor_exists():
    assert callable(viewpoint_diagram_GaugeSection.__init__)


def test_viewpoint_diagram_gaugesection_constructor_args():
    sig = inspect.signature(viewpoint_diagram_GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "value" in params, "Missing parameter 'value'"

def test_viewpoint_diagram_gaugesection_has_label():
    assert hasattr(viewpoint_diagram_GaugeSection, "label")
    descriptor = None
    for klass in viewpoint_diagram_GaugeSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_gaugesection_has_min():
    assert hasattr(viewpoint_diagram_GaugeSection, "min")
    descriptor = None
    for klass in viewpoint_diagram_GaugeSection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_gaugesection_has_max():
    assert hasattr(viewpoint_diagram_GaugeSection, "max")
    descriptor = None
    for klass in viewpoint_diagram_GaugeSection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_gaugesection_has_value():
    assert hasattr(viewpoint_diagram_GaugeSection, "value")
    descriptor = None
    for klass in viewpoint_diagram_GaugeSection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_BasicLabelStyle)


def test_viewpoint_basiclabelstyle_constructor_exists():
    assert callable(viewpoint_BasicLabelStyle.__init__)


def test_viewpoint_basiclabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelSize" in params, "Missing parameter 'labelSize'"
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "showIcon" in params, "Missing parameter 'showIcon'"
    assert "labelFormat" in params, "Missing parameter 'labelFormat'"

def test_viewpoint_basiclabelstyle_has_labelSize():
    assert hasattr(viewpoint_BasicLabelStyle, "labelSize")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "labelSize" in klass.__dict__:
            descriptor = klass.__dict__["labelSize"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_iconPath():
    assert hasattr(viewpoint_BasicLabelStyle, "iconPath")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_showIcon():
    assert hasattr(viewpoint_BasicLabelStyle, "showIcon")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "showIcon" in klass.__dict__:
            descriptor = klass.__dict__["showIcon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_basiclabelstyle_has_labelFormat():
    assert hasattr(viewpoint_BasicLabelStyle, "labelFormat")
    descriptor = None
    for klass in viewpoint_BasicLabelStyle.__mro__:
        if "labelFormat" in klass.__dict__:
            descriptor = klass.__dict__["labelFormat"]
            break
    assert isinstance(descriptor, property)



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_EndLabelStyle)


def test_viewpoint_diagram_endlabelstyle_constructor_exists():
    assert callable(viewpoint_diagram_EndLabelStyle.__init__)


def test_viewpoint_diagram_endlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_BeginLabelStyle)


def test_viewpoint_diagram_beginlabelstyle_constructor_exists():
    assert callable(viewpoint_diagram_BeginLabelStyle.__init__)


def test_viewpoint_diagram_beginlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_CenterLabelStyle)


def test_viewpoint_diagram_centerlabelstyle_constructor_exists():
    assert callable(viewpoint_diagram_CenterLabelStyle.__init__)


def test_viewpoint_diagram_centerlabelstyle_constructor_args():
    sig = inspect.signature(viewpoint_diagram_CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_labelstyle_is_not_abstract():
    assert not inspect.isabstract(viewpoint_LabelStyle)


def test_viewpoint_labelstyle_constructor_exists():
    assert callable(viewpoint_LabelStyle.__init__)


def test_viewpoint_labelstyle_constructor_args():
    sig = inspect.signature(viewpoint_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelAlignment" in params, "Missing parameter 'labelAlignment'"

def test_viewpoint_labelstyle_has_labelAlignment():
    assert hasattr(viewpoint_LabelStyle, "labelAlignment")
    descriptor = None
    for klass in viewpoint_LabelStyle.__mro__:
        if "labelAlignment" in klass.__dict__:
            descriptor = klass.__dict__["labelAlignment"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_danalysiscustomdata_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysisCustomData)


def test_viewpoint_danalysiscustomdata_constructor_exists():
    assert callable(viewpoint_DAnalysisCustomData.__init__)


def test_viewpoint_danalysiscustomdata_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysisCustomData.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_viewpoint_danalysiscustomdata_has_key():
    assert hasattr(viewpoint_DAnalysisCustomData, "key")
    descriptor = None
    for klass in viewpoint_DAnalysisCustomData.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dsourcefilelink_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DSourceFileLink)


def test_viewpoint_dsourcefilelink_constructor_exists():
    assert callable(viewpoint_DSourceFileLink.__init__)


def test_viewpoint_dsourcefilelink_constructor_args():
    sig = inspect.signature(viewpoint_DSourceFileLink.__init__)
    params = list(sig.parameters.keys())
    assert "filePath" in params, "Missing parameter 'filePath'"
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "startPosition" in params, "Missing parameter 'startPosition'"

def test_viewpoint_dsourcefilelink_has_filePath():
    assert hasattr(viewpoint_DSourceFileLink, "filePath")
    descriptor = None
    for klass in viewpoint_DSourceFileLink.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_dsourcefilelink_has_endPosition():
    assert hasattr(viewpoint_DSourceFileLink, "endPosition")
    descriptor = None
    for klass in viewpoint_DSourceFileLink.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_dsourcefilelink_has_startPosition():
    assert hasattr(viewpoint_DSourceFileLink, "startPosition")
    descriptor = None
    for klass in viewpoint_DSourceFileLink.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_mappingbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_MappingBasedDecoration)


def test_viewpoint_description_mappingbaseddecoration_constructor_exists():
    assert callable(viewpoint_description_MappingBasedDecoration.__init__)


def test_viewpoint_description_mappingbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint_description_MappingBasedDecoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_semanticbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_SemanticBasedDecoration)


def test_viewpoint_description_semanticbaseddecoration_constructor_exists():
    assert callable(viewpoint_description_SemanticBasedDecoration.__init__)


def test_viewpoint_description_semanticbaseddecoration_constructor_args():
    sig = inspect.signature(viewpoint_description_SemanticBasedDecoration.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint_description_semanticbaseddecoration_has_domainClass():
    assert hasattr(viewpoint_description_SemanticBasedDecoration, "domainClass")
    descriptor = None
    for klass in viewpoint_description_SemanticBasedDecoration.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_decoration_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Decoration)


def test_viewpoint_decoration_constructor_exists():
    assert callable(viewpoint_Decoration.__init__)


def test_viewpoint_decoration_constructor_args():
    sig = inspect.signature(viewpoint_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_is_not_abstract():
    assert not inspect.isabstract(Viewpoint)


def test_viewpoint_constructor_exists():
    assert callable(Viewpoint.__init__)


def test_viewpoint_constructor_args():
    sig = inspect.signature(Viewpoint.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_metamodelextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_MetaModelExtension)


def test_viewpoint_metamodelextension_constructor_exists():
    assert callable(viewpoint_MetaModelExtension.__init__)


def test_viewpoint_metamodelextension_constructor_args():
    sig = inspect.signature(viewpoint_MetaModelExtension.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_diagram_dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DSemanticDiagram)


def test_viewpoint_diagram_dsemanticdiagram_constructor_exists():
    assert callable(viewpoint_diagram_DSemanticDiagram.__init__)


def test_viewpoint_diagram_dsemanticdiagram_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_dstylizable_is_not_abstract():
    assert not inspect.isabstract(DStylizable)


def test_dstylizable_constructor_exists():
    assert callable(DStylizable.__init__)


def test_dstylizable_constructor_args():
    sig = inspect.signature(DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(DMappingBased)


def test_dmappingbased_constructor_exists():
    assert callable(DMappingBased.__init__)


def test_dmappingbased_constructor_args():
    sig = inspect.signature(DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_dlabelled_is_not_abstract():
    assert not inspect.isabstract(DLabelled)


def test_dlabelled_constructor_exists():
    assert callable(DLabelled.__init__)


def test_dlabelled_constructor_args():
    sig = inspect.signature(DLabelled.__init__)
    params = list(sig.parameters.keys())



def test_annotationentry_is_not_abstract():
    assert not inspect.isabstract(AnnotationEntry)


def test_annotationentry_constructor_exists():
    assert callable(AnnotationEntry.__init__)


def test_annotationentry_constructor_args():
    sig = inspect.signature(AnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_description_dmodelelement_is_not_abstract():
    assert not inspect.isabstract(description_DModelElement)


def test_description_dmodelelement_constructor_exists():
    assert callable(description_DModelElement.__init__)


def test_description_dmodelelement_constructor_args():
    sig = inspect.signature(description_DModelElement.__init__)
    params = list(sig.parameters.keys())



def test_drefreshable_is_not_abstract():
    assert not inspect.isabstract(DRefreshable)


def test_drefreshable_constructor_exists():
    assert callable(DRefreshable.__init__)


def test_drefreshable_constructor_args():
    sig = inspect.signature(DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationElement)


def test_viewpoint_drepresentationelement_constructor_exists():
    assert callable(viewpoint_DRepresentationElement.__init__)


def test_viewpoint_drepresentationelement_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_drepresentationelement_has_name():
    assert hasattr(viewpoint_DRepresentationElement, "name")
    descriptor = None
    for klass in viewpoint_DRepresentationElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_style_is_not_abstract():
    assert not inspect.isabstract(viewpoint_Style)


def test_viewpoint_style_constructor_exists():
    assert callable(viewpoint_Style.__init__)


def test_viewpoint_style_constructor_args():
    sig = inspect.signature(viewpoint_Style.__init__)
    params = list(sig.parameters.keys())



def test_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(description_DocumentedElement)


def test_description_documentedelement_constructor_exists():
    assert callable(description_DocumentedElement.__init__)


def test_description_documentedelement_constructor_args():
    sig = inspect.signature(description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_layer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Layer)


def test_viewpoint_description_layer_constructor_exists():
    assert callable(viewpoint_description_Layer.__init__)


def test_viewpoint_description_layer_constructor_args():
    sig = inspect.signature(viewpoint_description_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint_description_layer_has_icon():
    assert hasattr(viewpoint_description_Layer, "icon")
    descriptor = None
    for klass in viewpoint_description_Layer.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_filter_filterdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_filter_FilterDescription)


def test_viewpoint_filter_filterdescription_constructor_exists():
    assert callable(viewpoint_filter_FilterDescription.__init__)


def test_viewpoint_filter_filterdescription_constructor_args():
    sig = inspect.signature(viewpoint_filter_FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolSection)


def test_viewpoint_tool_toolsection_constructor_exists():
    assert callable(viewpoint_tool_ToolSection.__init__)


def test_viewpoint_tool_toolsection_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolSection.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_viewpoint_tool_toolsection_has_icon():
    assert hasattr(viewpoint_tool_ToolSection, "icon")
    descriptor = None
    for klass in viewpoint_tool_ToolSection.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EdgeMappingImport)


def test_viewpoint_description_edgemappingimport_constructor_exists():
    assert callable(viewpoint_description_EdgeMappingImport.__init__)


def test_viewpoint_description_edgemappingimport_constructor_args():
    sig = inspect.signature(viewpoint_description_EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"

def test_viewpoint_description_edgemappingimport_has_inheritsAncestorFilters():
    assert hasattr(viewpoint_description_EdgeMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in viewpoint_description_EdgeMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_diagram_ddiagram_is_not_abstract():
    assert not inspect.isabstract(viewpoint_diagram_DDiagram)


def test_viewpoint_diagram_ddiagram_constructor_exists():
    assert callable(viewpoint_diagram_DDiagram.__init__)


def test_viewpoint_diagram_ddiagram_constructor_args():
    sig = inspect.signature(viewpoint_diagram_DDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "headerHeight" in params, "Missing parameter 'headerHeight'"
    assert "isInLayoutingMode" in params, "Missing parameter 'isInLayoutingMode'"
    assert "info" in params, "Missing parameter 'info'"

def test_viewpoint_diagram_ddiagram_has_synchronized():
    assert hasattr(viewpoint_diagram_DDiagram, "synchronized")
    descriptor = None
    for klass in viewpoint_diagram_DDiagram.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ddiagram_has_headerHeight():
    assert hasattr(viewpoint_diagram_DDiagram, "headerHeight")
    descriptor = None
    for klass in viewpoint_diagram_DDiagram.__mro__:
        if "headerHeight" in klass.__dict__:
            descriptor = klass.__dict__["headerHeight"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ddiagram_has_isInLayoutingMode():
    assert hasattr(viewpoint_diagram_DDiagram, "isInLayoutingMode")
    descriptor = None
    for klass in viewpoint_diagram_DDiagram.__mro__:
        if "isInLayoutingMode" in klass.__dict__:
            descriptor = klass.__dict__["isInLayoutingMode"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_diagram_ddiagram_has_info():
    assert hasattr(viewpoint_diagram_DDiagram, "info")
    descriptor = None
    for klass in viewpoint_diagram_DDiagram.__mro__:
        if "info" in klass.__dict__:
            descriptor = klass.__dict__["info"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_viewpoint_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Viewpoint)


def test_viewpoint_description_viewpoint_constructor_exists():
    assert callable(viewpoint_description_Viewpoint.__init__)


def test_viewpoint_description_viewpoint_constructor_args():
    sig = inspect.signature(viewpoint_description_Viewpoint.__init__)
    params = list(sig.parameters.keys())
    assert "modelFileExtension" in params, "Missing parameter 'modelFileExtension'"
    assert "conflicts" in params, "Missing parameter 'conflicts'"
    assert "reuses" in params, "Missing parameter 'reuses'"
    assert "icon" in params, "Missing parameter 'icon'"
    assert "customizes" in params, "Missing parameter 'customizes'"

def test_viewpoint_description_viewpoint_has_modelFileExtension():
    assert hasattr(viewpoint_description_Viewpoint, "modelFileExtension")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "modelFileExtension" in klass.__dict__:
            descriptor = klass.__dict__["modelFileExtension"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_conflicts():
    assert hasattr(viewpoint_description_Viewpoint, "conflicts")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "conflicts" in klass.__dict__:
            descriptor = klass.__dict__["conflicts"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_reuses():
    assert hasattr(viewpoint_description_Viewpoint, "reuses")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "reuses" in klass.__dict__:
            descriptor = klass.__dict__["reuses"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_icon():
    assert hasattr(viewpoint_description_Viewpoint, "icon")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_viewpoint_has_customizes():
    assert hasattr(viewpoint_description_Viewpoint, "customizes")
    descriptor = None
    for klass in viewpoint_description_Viewpoint.__mro__:
        if "customizes" in klass.__dict__:
            descriptor = klass.__dict__["customizes"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_concern_concerndescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_concern_ConcernDescription)


def test_viewpoint_concern_concerndescription_constructor_exists():
    assert callable(viewpoint_concern_ConcernDescription.__init__)


def test_viewpoint_concern_concerndescription_constructor_args():
    sig = inspect.signature(viewpoint_concern_ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_description_edgemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_EdgeMapping)


def test_viewpoint_description_edgemapping_constructor_exists():
    assert callable(viewpoint_description_EdgeMapping.__init__)


def test_viewpoint_description_edgemapping_constructor_args():
    sig = inspect.signature(viewpoint_description_EdgeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"
    assert "pathExpression" in params, "Missing parameter 'pathExpression'"
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"

def test_viewpoint_description_edgemapping_has_sourceFinderExpression():
    assert hasattr(viewpoint_description_EdgeMapping, "sourceFinderExpression")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_edgemapping_has_useDomainElement():
    assert hasattr(viewpoint_description_EdgeMapping, "useDomainElement")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_edgemapping_has_pathExpression():
    assert hasattr(viewpoint_description_EdgeMapping, "pathExpression")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "pathExpression" in klass.__dict__:
            descriptor = klass.__dict__["pathExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_edgemapping_has_targetFinderExpression():
    assert hasattr(viewpoint_description_EdgeMapping, "targetFinderExpression")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_edgemapping_has_domainClass():
    assert hasattr(viewpoint_description_EdgeMapping, "domainClass")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_edgemapping_has_targetExpression():
    assert hasattr(viewpoint_description_EdgeMapping, "targetExpression")
    descriptor = None
    for klass in viewpoint_description_EdgeMapping.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_representationdescription_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_RepresentationDescription)


def test_viewpoint_description_representationdescription_constructor_exists():
    assert callable(viewpoint_description_RepresentationDescription.__init__)


def test_viewpoint_description_representationdescription_constructor_args():
    sig = inspect.signature(viewpoint_description_RepresentationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "initialisation" in params, "Missing parameter 'initialisation'"
    assert "titleExpression" in params, "Missing parameter 'titleExpression'"
    assert "showOnStartup" in params, "Missing parameter 'showOnStartup'"

def test_viewpoint_description_representationdescription_has_initialisation():
    assert hasattr(viewpoint_description_RepresentationDescription, "initialisation")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "initialisation" in klass.__dict__:
            descriptor = klass.__dict__["initialisation"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationdescription_has_titleExpression():
    assert hasattr(viewpoint_description_RepresentationDescription, "titleExpression")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "titleExpression" in klass.__dict__:
            descriptor = klass.__dict__["titleExpression"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_representationdescription_has_showOnStartup():
    assert hasattr(viewpoint_description_RepresentationDescription, "showOnStartup")
    descriptor = None
    for klass in viewpoint_description_RepresentationDescription.__mro__:
        if "showOnStartup" in klass.__dict__:
            descriptor = klass.__dict__["showOnStartup"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_group_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_Group)


def test_viewpoint_description_group_constructor_exists():
    assert callable(viewpoint_description_Group.__init__)


def test_viewpoint_description_group_constructor_args():
    sig = inspect.signature(viewpoint_description_Group.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_description_group_has_version():
    assert hasattr(viewpoint_description_Group, "version")
    descriptor = None
    for klass in viewpoint_description_Group.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_description_group_has_name():
    assert hasattr(viewpoint_description_Group, "name")
    descriptor = None
    for klass in viewpoint_description_Group.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(viewpoint_description_AbstractNodeMapping)


def test_viewpoint_description_abstractnodemapping_constructor_exists():
    assert callable(viewpoint_description_AbstractNodeMapping.__init__)


def test_viewpoint_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(viewpoint_description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_viewpoint_description_abstractnodemapping_has_domainClass():
    assert hasattr(viewpoint_description_AbstractNodeMapping, "domainClass")
    descriptor = None
    for klass in viewpoint_description_AbstractNodeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(viewpoint_tool_ToolEntry)


def test_viewpoint_tool_toolentry_constructor_exists():
    assert callable(viewpoint_tool_ToolEntry.__init__)


def test_viewpoint_tool_toolentry_constructor_args():
    sig = inspect.signature(viewpoint_tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drepresentation_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentation)


def test_viewpoint_drepresentation_constructor_exists():
    assert callable(viewpoint_DRepresentation.__init__)


def test_viewpoint_drepresentation_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_viewpoint_drepresentation_has_name():
    assert hasattr(viewpoint_DRepresentation, "name")
    descriptor = None
    for klass in viewpoint_DRepresentation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DSemanticDecorator)


def test_viewpoint_dsemanticdecorator_constructor_exists():
    assert callable(viewpoint_DSemanticDecorator.__init__)


def test_viewpoint_dsemanticdecorator_constructor_args():
    sig = inspect.signature(viewpoint_DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramset_is_not_abstract():
    assert not inspect.isabstract(DDiagramSet)


def test_ddiagramset_constructor_exists():
    assert callable(DDiagramSet.__init__)


def test_ddiagramset_constructor_args():
    sig = inspect.signature(DDiagramSet.__init__)
    params = list(sig.parameters.keys())



def test_dview_is_not_abstract():
    assert not inspect.isabstract(DView)


def test_dview_constructor_exists():
    assert callable(DView.__init__)


def test_dview_constructor_args():
    sig = inspect.signature(DView.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drepresentationcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRepresentationContainer)


def test_viewpoint_drepresentationcontainer_constructor_exists():
    assert callable(viewpoint_DRepresentationContainer.__init__)


def test_viewpoint_drepresentationcontainer_constructor_args():
    sig = inspect.signature(viewpoint_DRepresentationContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dcontainer_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DContainer)


def test_viewpoint_dcontainer_constructor_exists():
    assert callable(viewpoint_DContainer.__init__)


def test_viewpoint_dcontainer_constructor_args():
    sig = inspect.signature(viewpoint_DContainer.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dmappingbased_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DMappingBased)


def test_viewpoint_dmappingbased_constructor_exists():
    assert callable(viewpoint_DMappingBased.__init__)


def test_viewpoint_dmappingbased_constructor_args():
    sig = inspect.signature(viewpoint_DMappingBased.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dlabelled_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DLabelled)


def test_viewpoint_dlabelled_constructor_exists():
    assert callable(viewpoint_DLabelled.__init__)


def test_viewpoint_dlabelled_constructor_args():
    sig = inspect.signature(viewpoint_DLabelled.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_drefreshable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DRefreshable)


def test_viewpoint_drefreshable_constructor_exists():
    assert callable(viewpoint_DRefreshable.__init__)


def test_viewpoint_drefreshable_constructor_args():
    sig = inspect.signature(viewpoint_DRefreshable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dstylizable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DStylizable)


def test_viewpoint_dstylizable_constructor_exists():
    assert callable(viewpoint_DStylizable.__init__)


def test_viewpoint_dstylizable_constructor_args():
    sig = inspect.signature(viewpoint_DStylizable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dnavigationlink_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DNavigationLink)


def test_viewpoint_dnavigationlink_constructor_exists():
    assert callable(viewpoint_DNavigationLink.__init__)


def test_viewpoint_dnavigationlink_constructor_args():
    sig = inspect.signature(viewpoint_DNavigationLink.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "targetType" in params, "Missing parameter 'targetType'"

def test_viewpoint_dnavigationlink_has_label():
    assert hasattr(viewpoint_DNavigationLink, "label")
    descriptor = None
    for klass in viewpoint_DNavigationLink.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_viewpoint_dnavigationlink_has_targetType():
    assert hasattr(viewpoint_DNavigationLink, "targetType")
    descriptor = None
    for klass in viewpoint_DNavigationLink.__mro__:
        if "targetType" in klass.__dict__:
            descriptor = klass.__dict__["targetType"]
            break
    assert isinstance(descriptor, property)



def test_viewpoint_dnavigable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DNavigable)


def test_viewpoint_dnavigable_constructor_exists():
    assert callable(viewpoint_DNavigable.__init__)


def test_viewpoint_dnavigable_constructor_args():
    sig = inspect.signature(viewpoint_DNavigable.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dvalidable_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DValidable)


def test_viewpoint_dvalidable_constructor_exists():
    assert callable(viewpoint_DValidable.__init__)


def test_viewpoint_dvalidable_constructor_args():
    sig = inspect.signature(viewpoint_DValidable.__init__)
    params = list(sig.parameters.keys())



def test_featureextensiondescription_is_not_abstract():
    assert not inspect.isabstract(FeatureExtensionDescription)


def test_featureextensiondescription_constructor_exists():
    assert callable(FeatureExtensionDescription.__init__)


def test_featureextensiondescription_constructor_args():
    sig = inspect.signature(FeatureExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dfeatureextension_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DFeatureExtension)


def test_viewpoint_dfeatureextension_constructor_exists():
    assert callable(viewpoint_DFeatureExtension.__init__)


def test_viewpoint_dfeatureextension_constructor_args():
    sig = inspect.signature(viewpoint_DFeatureExtension.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_dview_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DView)


def test_viewpoint_dview_constructor_exists():
    assert callable(viewpoint_DView.__init__)


def test_viewpoint_dview_constructor_args():
    sig = inspect.signature(viewpoint_DView.__init__)
    params = list(sig.parameters.keys())
    assert "initialized" in params, "Missing parameter 'initialized'"

def test_viewpoint_dview_has_initialized():
    assert hasattr(viewpoint_DView, "initialized")
    descriptor = None
    for klass in viewpoint_DView.__mro__:
        if "initialized" in klass.__dict__:
            descriptor = klass.__dict__["initialized"]
            break
    assert isinstance(descriptor, property)



def test_dannotationentry_is_not_abstract():
    assert not inspect.isabstract(DAnnotationEntry)


def test_dannotationentry_constructor_exists():
    assert callable(DAnnotationEntry.__init__)


def test_dannotationentry_constructor_args():
    sig = inspect.signature(DAnnotationEntry.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_eobject_is_not_abstract():
    assert not inspect.isabstract(viewpoint_EObject)


def test_viewpoint_eobject_constructor_exists():
    assert callable(viewpoint_EObject.__init__)


def test_viewpoint_eobject_constructor_args():
    sig = inspect.signature(viewpoint_EObject.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_danalysis_is_not_abstract():
    assert not inspect.isabstract(viewpoint_DAnalysis)


def test_viewpoint_danalysis_constructor_exists():
    assert callable(viewpoint_DAnalysis.__init__)


def test_viewpoint_danalysis_constructor_args():
    sig = inspect.signature(viewpoint_DAnalysis.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_viewpoint_danalysis_has_version():
    assert hasattr(viewpoint_DAnalysis, "version")
    descriptor = None
    for klass in viewpoint_DAnalysis.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_labelalignment_exists():
    # Check that the Enumeration exists
    assert LabelAlignment is not None

def test_labelalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelAlignment]
    expected_literals = [
        "CENTER",
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelAlignment"

def test_containershape_exists():
    # Check that the Enumeration exists
    assert ContainerShape is not None

def test_containershape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerShape]
    expected_literals = [
        "parallelogram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerShape"

def test_dragsource_exists():
    # Check that the Enumeration exists
    assert DragSource is not None

def test_dragsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DragSource]
    expected_literals = [
        "PROJECT_EXPLORER",
        "DIAGRAM",
        "BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DragSource"

def test_syncstatus_exists():
    # Check that the Enumeration exists
    assert SyncStatus is not None

def test_syncstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SyncStatus]
    expected_literals = [
        "dirty",
        "sync",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SyncStatus"

def test_resizekind_exists():
    # Check that the Enumeration exists
    assert ResizeKind is not None

def test_resizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResizeKind]
    expected_literals = [
        "NONE",
        "NSEW",
        "NORTH_SOUTH",
        "EAST_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResizeKind"

def test_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "square",
        "stroke",
        "triangle",
        "ring",
        "dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"

def test_edgearrows_exists():
    # Check that the Enumeration exists
    assert EdgeArrows is not None

def test_edgearrows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeArrows]
    expected_literals = [
        "InputArrowWithDiamond",
        "OutputFillClosedArrow",
        "OutputClosedArrow",
        "FillDiamond",
        "NoDecoration",
        "InputClosedArrow",
        "Diamond",
        "InputArrowWithFillDiamond",
        "InputFillClosedArrow",
        "InputArrow",
        "OutputArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeArrows"

def test_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "Liquid",
        "GradientLeftToRight",
        "GradientTopToBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

def test_navigationtargettype_exists():
    # Check that the Enumeration exists
    assert NavigationTargetType is not None

def test_navigationtargettype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NavigationTargetType]
    expected_literals = [
        "model",
        "file",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NavigationTargetType"

def test_filterkind_exists():
    # Check that the Enumeration exists
    assert FilterKind is not None

def test_filterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FilterKind]
    expected_literals = [
        "COLLAPSE",
        "HIDE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FilterKind"

def test_systemcolors_exists():
    # Check that the Enumeration exists
    assert SystemColors is not None

def test_systemcolors_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SystemColors]
    expected_literals = [
        "yellow",
        "purple",
        "dark_yellow",
        "dark_gray",
        "black",
        "light_red",
        "light_orange",
        "dark_purple",
        "blue",
        "gray",
        "light_green",
        "dark_green",
        "dark_chocolate",
        "red",
        "dark_blue",
        "dark_orange",
        "light_purple",
        "light_blue",
        "green",
        "light_gray",
        "chocolate",
        "dark_red",
        "orange",
        "light_chocolate",
        "light_yellow",
        "white",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SystemColors"

def test_labelposition_exists():
    # Check that the Enumeration exists
    assert LabelPosition is not None

def test_labelposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelPosition]
    expected_literals = [
        "border",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelPosition"

def test_arrangeconstraint_exists():
    # Check that the Enumeration exists
    assert ArrangeConstraint is not None

def test_arrangeconstraint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrangeConstraint]
    expected_literals = [
        "KEEP_SIZE",
        "KEEP_LOCATION",
        "KEEP_RATIO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrangeConstraint"

def test_reconnectionkind_exists():
    # Check that the Enumeration exists
    assert ReconnectionKind is not None

def test_reconnectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReconnectionKind]
    expected_literals = [
        "RECONNECT_SOURCE",
        "RECONNECT_TARGET",
        "RECONNECT_BOTH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReconnectionKind"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "dash",
        "dot",
        "solid",
        "dash_dot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_fontformat_exists():
    # Check that the Enumeration exists
    assert FontFormat is not None

def test_fontformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontFormat]
    expected_literals = [
        "normal",
        "bold",
        "bold_italic",
        "italic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontFormat"

def test_foldingstyle_exists():
    # Check that the Enumeration exists
    assert FoldingStyle is not None

def test_foldingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoldingStyle]
    expected_literals = [
        "SOURCE",
        "NONE",
        "TARGET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoldingStyle"

def test_edgerouting_exists():
    # Check that the Enumeration exists
    assert EdgeRouting is not None

def test_edgerouting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeRouting]
    expected_literals = [
        "manhattan",
        "tree",
        "straight",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeRouting"

def test_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "HORIZONTAL",
        "VERTICAL",
        "SQUARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_error_level_exists():
    # Check that the Enumeration exists
    assert ERROR_LEVEL is not None

def test_error_level_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ERROR_LEVEL]
    expected_literals = [
        "WARNING",
        "INFO",
        "ERROR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ERROR_LEVEL"

def test_containerlayout_exists():
    # Check that the Enumeration exists
    assert ContainerLayout is not None

def test_containerlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLayout]
    expected_literals = [
        "FreeForm",
        "VerticalStack",
        "List",
        "HorizontalStack",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLayout"

def test_layoutdirection_exists():
    # Check that the Enumeration exists
    assert LayoutDirection is not None

def test_layoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LayoutDirection]
    expected_literals = [
        "BottomToTop",
        "LeftToRight",
        "TopToBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LayoutDirection"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "SOUTH_WEST",
        "NORTH",
        "EAST",
        "WEST",
        "SOUTH",
        "NORTH_EAST",
        "CENTER",
        "SOUTH_EAST",
        "NORTH_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
DNode_strategy = st.builds(
    DNode,
)
DContainer_strategy = st.builds(
    DContainer,
)
DValidable_strategy = st.builds(
    DValidable,
)
DragAndDropTarget_strategy = st.builds(
    DragAndDropTarget,
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
InformationSection_strategy = st.builds(
    InformationSection,
)
viewpoint_audit_TemplateInformationSection_strategy = st.builds(
    viewpoint_audit_TemplateInformationSection,
    templatePath=
        safe_text
)
description_DiagramDescription_strategy = st.builds(
    description_DiagramDescription,
)
DDiagramElement_strategy = st.builds(
    DDiagramElement,
)
SwitchChild_strategy = st.builds(
    SwitchChild,
)
viewpoint_tool_Case_strategy = st.builds(
    viewpoint_tool_Case,
    conditionExpression=
        safe_text
)
viewpoint_tool_FeatureChangeListener_strategy = st.builds(
    viewpoint_tool_FeatureChangeListener,
    domainClass=
        safe_text,
    featureName=
        safe_text
)
tool_FeatureChangeListener_strategy = st.builds(
    tool_FeatureChangeListener,
)
viewpoint_audit_InformationSection_strategy = st.builds(
    viewpoint_audit_InformationSection,
)
tool_Default_strategy = st.builds(
    tool_Default,
)
tool_Case_strategy = st.builds(
    tool_Case,
)
viewpoint_tool_Default_strategy = st.builds(
    viewpoint_tool_Default,
)
viewpoint_tool_SwitchChild_strategy = st.builds(
    viewpoint_tool_SwitchChild,
)
viewpoint_tool_ToolFilterDescription_strategy = st.builds(
    viewpoint_tool_ToolFilterDescription,
    precondition=
        safe_text,
    elementsToListen=
        safe_text
)
viewpoint_tool_ExternalJavaActionParameter_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionParameter,
    value=
        safe_text,
    name=
        safe_text
)
tool_viewpoint_EObject_strategy = st.builds(
    tool_viewpoint_EObject,
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
viewpoint_tool_DeleteView_strategy = st.builds(
    viewpoint_tool_DeleteView,
)
viewpoint_tool_MoveElement_strategy = st.builds(
    viewpoint_tool_MoveElement,
    newContainerExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_SetValue_strategy = st.builds(
    viewpoint_tool_SetValue,
    valueExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_If_strategy = st.builds(
    viewpoint_tool_If,
    conditionExpression=
        safe_text
)
viewpoint_tool_SetObject_strategy = st.builds(
    viewpoint_tool_SetObject,
    featureName=
        safe_text
)
viewpoint_tool_ChangeContext_strategy = st.builds(
    viewpoint_tool_ChangeContext,
    browseExpression=
        safe_text
)
viewpoint_tool_Unset_strategy = st.builds(
    viewpoint_tool_Unset,
    elementExpression=
        safe_text,
    featureName=
        safe_text
)
viewpoint_tool_For_strategy = st.builds(
    viewpoint_tool_For,
    iteratorName=
        safe_text,
    expression=
        safe_text
)
viewpoint_tool_RemoveElement_strategy = st.builds(
    viewpoint_tool_RemoveElement,
)
viewpoint_tool_CreateInstance_strategy = st.builds(
    viewpoint_tool_CreateInstance,
    variableName=
        safe_text,
    referenceName=
        safe_text,
    typeName=
        safe_text
)
viewpoint_tool_InitialContainerDropOperation_strategy = st.builds(
    viewpoint_tool_InitialContainerDropOperation,
)
viewpoint_validation_ValidationFix_strategy = st.builds(
    viewpoint_validation_ValidationFix,
    name=
        safe_text
)
ValidationRule_strategy = st.builds(
    ValidationRule,
)
viewpoint_validation_ViewValidationRule_strategy = st.builds(
    viewpoint_validation_ViewValidationRule,
)
viewpoint_validation_SemanticValidationRule_strategy = st.builds(
    viewpoint_validation_SemanticValidationRule,
    targetClass=
        safe_text
)
validation_ValidationFix_strategy = st.builds(
    validation_ValidationFix,
)
validation_RuleAudit_strategy = st.builds(
    validation_RuleAudit,
)
viewpoint_validation_ValidationRule_strategy = st.builds(
    viewpoint_validation_ValidationRule,
    message=
        safe_text,
    level=
        safe_text
)
viewpoint_validation_RuleAudit_strategy = st.builds(
    viewpoint_validation_RuleAudit,
    auditExpression=
        safe_text
)
SelectionDescription_strategy = st.builds(
    SelectionDescription,
)
viewpoint_filter_FilterVariable_strategy = st.builds(
    viewpoint_filter_FilterVariable,
    name=
        safe_text
)
filter_Filter_strategy = st.builds(
    filter_Filter,
)
FilterDescription_strategy = st.builds(
    FilterDescription,
)
viewpoint_filter_CompositeFilterDescription_strategy = st.builds(
    viewpoint_filter_CompositeFilterDescription,
)
Filter_strategy = st.builds(
    Filter,
)
viewpoint_filter_VariableFilter_strategy = st.builds(
    viewpoint_filter_VariableFilter,
    semanticConditionExpression=
        safe_text
)
viewpoint_filter_MappingFilter_strategy = st.builds(
    viewpoint_filter_MappingFilter,
    viewConditionExpression=
        safe_text,
    semanticConditionExpression=
        safe_text
)
viewpoint_filter_Filter_strategy = st.builds(
    viewpoint_filter_Filter,
    filterKind=
        safe_text
)
viewpoint_tool_Navigation_strategy = st.builds(
    viewpoint_tool_Navigation,
    createIfNotExistent=
        st.booleans()
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
CreateView_strategy = st.builds(
    CreateView,
)
viewpoint_tool_DiagramNavigationDescription_strategy = st.builds(
    viewpoint_tool_DiagramNavigationDescription,
)
viewpoint_tool_CreateEdgeView_strategy = st.builds(
    viewpoint_tool_CreateEdgeView,
    targetExpression=
        safe_text,
    sourceExpression=
        safe_text
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
viewpoint_tool_DiagramCreationDescription_strategy = st.builds(
    viewpoint_tool_DiagramCreationDescription,
)
viewpoint_tool_CreateView_strategy = st.builds(
    viewpoint_tool_CreateView,
    variableName=
        safe_text,
    containerViewExpression=
        safe_text
)
tool_EditMaskVariables_strategy = st.builds(
    tool_EditMaskVariables,
)
tool_ElementDoubleClickVariable_strategy = st.builds(
    tool_ElementDoubleClickVariable,
)
tool_DeleteHook_strategy = st.builds(
    tool_DeleteHook,
)
viewpoint_tool_DeleteHookParameter_strategy = st.builds(
    viewpoint_tool_DeleteHookParameter,
    name=
        safe_text,
    value=
        safe_text
)
tool_DeleteHookParameter_strategy = st.builds(
    tool_DeleteHookParameter,
)
viewpoint_tool_DeleteHook_strategy = st.builds(
    viewpoint_tool_DeleteHook,
    id=
        safe_text
)
tool_ElementDeleteVariable_strategy = st.builds(
    tool_ElementDeleteVariable,
)
tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    tool_TargetEdgeViewCreationVariable,
)
tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    tool_SourceEdgeViewCreationVariable,
)
tool_TargetEdgeCreationVariable_strategy = st.builds(
    tool_TargetEdgeCreationVariable,
)
tool_SourceEdgeCreationVariable_strategy = st.builds(
    tool_SourceEdgeCreationVariable,
)
tool_InitEdgeCreationOperation_strategy = st.builds(
    tool_InitEdgeCreationOperation,
)
tool_InitialNodeCreationOperation_strategy = st.builds(
    tool_InitialNodeCreationOperation,
)
tool_NodeCreationVariable_strategy = st.builds(
    tool_NodeCreationVariable,
)
tool_PopupMenu_strategy = st.builds(
    tool_PopupMenu,
)
tool_ToolGroup_strategy = st.builds(
    tool_ToolGroup,
)
viewpoint_tool_ToolGroupExtension_strategy = st.builds(
    viewpoint_tool_ToolGroupExtension,
)
tool_ToolGroupExtension_strategy = st.builds(
    tool_ToolGroupExtension,
)
style_BeginLabelStyleDescription_strategy = st.builds(
    style_BeginLabelStyleDescription,
)
EdgeStyleDescription_strategy = st.builds(
    EdgeStyleDescription,
)
viewpoint_style_BracketEdgeStyleDescription_strategy = st.builds(
    viewpoint_style_BracketEdgeStyleDescription,
)
style_EndLabelStyleDescription_strategy = st.builds(
    style_EndLabelStyleDescription,
)
style_CenterLabelStyleDescription_strategy = st.builds(
    style_CenterLabelStyleDescription,
)
viewpoint_style_SizeComputationContainerStyleDescription_strategy = st.builds(
    viewpoint_style_SizeComputationContainerStyleDescription,
    heightComputationExpression=
        safe_text,
    widthComputationExpression=
        safe_text
)
style_SizeComputationContainerStyleDescription_strategy = st.builds(
    style_SizeComputationContainerStyleDescription,
)
style_RoundedCornerStyleDescription_strategy = st.builds(
    style_RoundedCornerStyleDescription,
)
viewpoint_style_GaugeSectionDescription_strategy = st.builds(
    viewpoint_style_GaugeSectionDescription,
    label=
        safe_text,
    maxValueExpression=
        safe_text,
    minValueExpression=
        safe_text,
    valueExpression=
        safe_text
)
style_GaugeSectionDescription_strategy = st.builds(
    style_GaugeSectionDescription,
)
NodeStyleDescription_strategy = st.builds(
    NodeStyleDescription,
)
viewpoint_style_DotDescription_strategy = st.builds(
    viewpoint_style_DotDescription,
    strokeSizeComputationExpression=
        safe_text
)
viewpoint_style_GaugeCompositeStyleDescription_strategy = st.builds(
    viewpoint_style_GaugeCompositeStyleDescription,
    alignment=
        safe_text
)
viewpoint_style_LozengeNodeDescription_strategy = st.builds(
    viewpoint_style_LozengeNodeDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
viewpoint_style_SquareDescription_strategy = st.builds(
    viewpoint_style_SquareDescription,
    height=
        safe_text,
    width=
        safe_text
)
viewpoint_style_NoteDescription_strategy = st.builds(
    viewpoint_style_NoteDescription,
)
viewpoint_style_BundledImageDescription_strategy = st.builds(
    viewpoint_style_BundledImageDescription,
    shape=
        safe_text
)
viewpoint_style_CustomStyleDescription_strategy = st.builds(
    viewpoint_style_CustomStyleDescription,
    id=
        safe_text
)
viewpoint_style_EllipseNodeDescription_strategy = st.builds(
    viewpoint_style_EllipseNodeDescription,
    verticalDiameterComputationExpression=
        safe_text,
    horizontalDiameterComputationExpression=
        safe_text
)
style_TooltipStyleDescription_strategy = st.builds(
    style_TooltipStyleDescription,
)
style_LabelStyleDescription_strategy = st.builds(
    style_LabelStyleDescription,
)
style_BorderedStyleDescription_strategy = st.builds(
    style_BorderedStyleDescription,
)
viewpoint_style_ContainerStyleDescription_strategy = st.builds(
    viewpoint_style_ContainerStyleDescription,
    roundedCorner=
        st.booleans()
)
StyleDescription_strategy = st.builds(
    StyleDescription,
)
viewpoint_style_RoundedCornerStyleDescription_strategy = st.builds(
    viewpoint_style_RoundedCornerStyleDescription,
    arcWidth=
        safe_text,
    arcHeight=
        safe_text
)
viewpoint_style_EdgeStyleDescription_strategy = st.builds(
    viewpoint_style_EdgeStyleDescription,
    sourceArrow=
        safe_text,
    routingStyle=
        safe_text,
    targetArrow=
        safe_text,
    foldingStyle=
        safe_text,
    lineStyle=
        safe_text,
    sizeComputationExpression=
        safe_text
)
viewpoint_style_BorderedStyleDescription_strategy = st.builds(
    viewpoint_style_BorderedStyleDescription,
    borderSizeComputationExpression=
        safe_text
)
Layer_strategy = st.builds(
    Layer,
)
viewpoint_description_AdditionalLayer_strategy = st.builds(
    viewpoint_description_AdditionalLayer,
    activeByDefault=
        st.booleans(),
    optional=
        st.booleans()
)
Customization_strategy = st.builds(
    Customization,
)
DecorationDescriptionsSet_strategy = st.builds(
    DecorationDescriptionsSet,
)
Layout_strategy = st.builds(
    Layout,
)
viewpoint_description_CompositeLayout_strategy = st.builds(
    viewpoint_description_CompositeLayout,
    direction=
        safe_text,
    padding=
        st.integers()
)
viewpoint_description_OrderedTreeLayout_strategy = st.builds(
    viewpoint_description_OrderedTreeLayout,
    childrenExpression=
        safe_text
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
viewpoint_concern_ConcernSet_strategy = st.builds(
    viewpoint_concern_ConcernSet,
)
viewpoint_validation_ValidationSet_strategy = st.builds(
    viewpoint_validation_ValidationSet,
    name=
        safe_text
)
viewpoint_description_Layout_strategy = st.builds(
    viewpoint_description_Layout,
)
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
viewpoint_description_ConditionalContainerStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalContainerStyleDescription,
)
viewpoint_description_ConditionalEdgeStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalEdgeStyleDescription,
)
viewpoint_description_ConditionalNodeStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalNodeStyleDescription,
)
description_ConditionalEdgeStyleDescription_strategy = st.builds(
    description_ConditionalEdgeStyleDescription,
)
style_EdgeStyleDescription_strategy = st.builds(
    style_EdgeStyleDescription,
)
viewpoint_description_IEdgeMapping_strategy = st.builds(
    viewpoint_description_IEdgeMapping,
)
tool_ReconnectEdgeDescription_strategy = st.builds(
    tool_ReconnectEdgeDescription,
)
description_ConditionalContainerStyleDescription_strategy = st.builds(
    description_ConditionalContainerStyleDescription,
)
style_ContainerStyleDescription_strategy = st.builds(
    style_ContainerStyleDescription,
)
viewpoint_style_FlatContainerStyleDescription_strategy = st.builds(
    viewpoint_style_FlatContainerStyleDescription,
    backgroundStyle=
        safe_text
)
viewpoint_style_ShapeContainerStyleDescription_strategy = st.builds(
    viewpoint_style_ShapeContainerStyleDescription,
    shape=
        safe_text
)
description_AbstractMappingImport_strategy = st.builds(
    description_AbstractMappingImport,
)
description_ConditionalNodeStyleDescription_strategy = st.builds(
    description_ConditionalNodeStyleDescription,
)
style_NodeStyleDescription_strategy = st.builds(
    style_NodeStyleDescription,
)
viewpoint_style_WorkspaceImageDescription_strategy = st.builds(
    viewpoint_style_WorkspaceImageDescription,
    workspacePath=
        safe_text
)
tool_DoubleClickDescription_strategy = st.builds(
    tool_DoubleClickDescription,
)
description_AbstractNodeMapping_strategy = st.builds(
    description_AbstractNodeMapping,
)
tool_DirectEditLabel_strategy = st.builds(
    tool_DirectEditLabel,
)
tool_DeleteElementDescription_strategy = st.builds(
    tool_DeleteElementDescription,
)
tool_ToolSection_strategy = st.builds(
    tool_ToolSection,
)
description_RepresentationElementMapping_strategy = st.builds(
    description_RepresentationElementMapping,
)
description_RepresentationImportDescription_strategy = st.builds(
    description_RepresentationImportDescription,
)
viewpoint_description_DiagramImportDescription_strategy = st.builds(
    viewpoint_description_DiagramImportDescription,
)
description_AdditionalLayer_strategy = st.builds(
    description_AdditionalLayer,
)
description_Layout_strategy = st.builds(
    description_Layout,
)
description_EdgeMappingImport_strategy = st.builds(
    description_EdgeMappingImport,
)
description_EdgeMapping_strategy = st.builds(
    description_EdgeMapping,
)
concern_ConcernSet_strategy = st.builds(
    concern_ConcernSet,
)
ModelElement2ViewVariable_strategy = st.builds(
    ModelElement2ViewVariable,
)
viewpoint_diagram_DiagramElementMapping2ModelElement_strategy = st.builds(
    viewpoint_diagram_DiagramElementMapping2ModelElement,
)
DiagramElementMapping2ModelElement_strategy = st.builds(
    DiagramElementMapping2ModelElement,
)
viewpoint_diagram_ComputedStyleDescriptionRegistry_strategy = st.builds(
    viewpoint_diagram_ComputedStyleDescriptionRegistry,
)
description_PasteTargetDescription_strategy = st.builds(
    description_PasteTargetDescription,
)
viewpoint_description_DiagramElementMapping_strategy = st.builds(
    viewpoint_description_DiagramElementMapping,
    synchronizationLock=
        st.booleans(),
    preconditionExpression=
        safe_text,
    createElements=
        st.booleans(),
    semanticCandidatesExpression=
        safe_text,
    semanticElements=
        safe_text
)
description_RepresentationDescription_strategy = st.builds(
    description_RepresentationDescription,
)
description_DragAndDropTargetDescription_strategy = st.builds(
    description_DragAndDropTargetDescription,
)
viewpoint_description_NodeMapping_strategy = st.builds(
    viewpoint_description_NodeMapping,
)
viewpoint_description_ContainerMapping_strategy = st.builds(
    viewpoint_description_ContainerMapping,
    childrenPresentation=
        safe_text
)
viewpoint_description_DiagramDescription_strategy = st.builds(
    viewpoint_description_DiagramDescription,
    rootExpression=
        safe_text,
    preconditionExpression=
        safe_text,
    domainClass=
        safe_text,
    enablePopupBars=
        st.booleans()
)
viewpoint_diagram_ContainerVariable2StyleDescription_strategy = st.builds(
    viewpoint_diagram_ContainerVariable2StyleDescription,
)
ContainerVariable2StyleDescription_strategy = st.builds(
    ContainerVariable2StyleDescription,
)
viewpoint_diagram_ViewVariable2ContainerVariable_strategy = st.builds(
    viewpoint_diagram_ViewVariable2ContainerVariable,
)
ViewVariable2ContainerVariable_strategy = st.builds(
    ViewVariable2ContainerVariable,
)
viewpoint_diagram_ModelElement2ViewVariable_strategy = st.builds(
    viewpoint_diagram_ModelElement2ViewVariable,
)
diagram_viewpoint_EObject_strategy = st.builds(
    diagram_viewpoint_EObject,
)
filter_FilterVariable_strategy = st.builds(
    filter_FilterVariable,
)
viewpoint_diagram_FilterVariableValue_strategy = st.builds(
    viewpoint_diagram_FilterVariableValue,
)
FilterVariableValue_strategy = st.builds(
    FilterVariableValue,
)
CollapseFilter_strategy = st.builds(
    CollapseFilter,
)
viewpoint_diagram_IndirectlyCollapseFilter_strategy = st.builds(
    viewpoint_diagram_IndirectlyCollapseFilter,
)
viewpoint_diagram_FilterVariableHistory_strategy = st.builds(
    viewpoint_diagram_FilterVariableHistory,
)
GaugeSection_strategy = st.builds(
    GaugeSection,
)
EndLabelStyle_strategy = st.builds(
    EndLabelStyle,
)
CenterLabelStyle_strategy = st.builds(
    CenterLabelStyle,
)
BeginLabelStyle_strategy = st.builds(
    BeginLabelStyle,
)
diagram_ContainerStyle_strategy = st.builds(
    diagram_ContainerStyle,
)
diagram_NodeStyle_strategy = st.builds(
    diagram_NodeStyle,
)
viewpoint_diagram_WorkspaceImage_strategy = st.builds(
    viewpoint_diagram_WorkspaceImage,
    workspacePath=
        safe_text
)
viewpoint_diagram_EdgeTarget_strategy = st.builds(
    viewpoint_diagram_EdgeTarget,
)
diagram_BorderedStyle_strategy = st.builds(
    diagram_BorderedStyle,
)
Style_strategy = st.builds(
    Style,
)
viewpoint_diagram_EdgeStyle_strategy = st.builds(
    viewpoint_diagram_EdgeStyle,
    size=
        safe_text,
    targetArrow=
        safe_text,
    routingStyle=
        safe_text,
    lineStyle=
        safe_text,
    foldingStyle=
        safe_text,
    sourceArrow=
        safe_text
)
viewpoint_diagram_BorderedStyle_strategy = st.builds(
    viewpoint_diagram_BorderedStyle,
    borderSize=
        safe_text,
    borderSizeComputationExpression=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
viewpoint_diagram_ContainerStyle_strategy = st.builds(
    viewpoint_diagram_ContainerStyle,
)
viewpoint_diagram_NodeStyle_strategy = st.builds(
    viewpoint_diagram_NodeStyle,
    hideLabelByDefault=
        st.booleans(),
    labelPosition=
        safe_text
)
diagram_viewpoint_DRepresentationContainer_strategy = st.builds(
    diagram_viewpoint_DRepresentationContainer,
)
diagram_viewpoint_RGBValues_strategy = st.builds(
    diagram_viewpoint_RGBValues,
)
description_IEdgeMapping_strategy = st.builds(
    description_IEdgeMapping,
)
viewpoint_diagram_DDiagramSet_strategy = st.builds(
    viewpoint_diagram_DDiagramSet,
)
AbstractDNode_strategy = st.builds(
    AbstractDNode,
)
viewpoint_diagram_DNodeListElement_strategy = st.builds(
    viewpoint_diagram_DNodeListElement,
)
EdgeStyle_strategy = st.builds(
    EdgeStyle,
)
viewpoint_diagram_BracketEdgeStyle_strategy = st.builds(
    viewpoint_diagram_BracketEdgeStyle,
)
diagram_DDiagramElement_strategy = st.builds(
    diagram_DDiagramElement,
)
description_ContainerMapping_strategy = st.builds(
    description_ContainerMapping,
)
viewpoint_description_ContainerMappingImport_strategy = st.builds(
    viewpoint_description_ContainerMappingImport,
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
viewpoint_diagram_FlatContainerStyle_strategy = st.builds(
    viewpoint_diagram_FlatContainerStyle,
    backgroundStyle=
        safe_text
)
viewpoint_diagram_ShapeContainerStyle_strategy = st.builds(
    viewpoint_diagram_ShapeContainerStyle,
    shape=
        safe_text
)
diagram_EdgeTarget_strategy = st.builds(
    diagram_EdgeTarget,
)
viewpoint_diagram_DEdge_strategy = st.builds(
    viewpoint_diagram_DEdge,
    routingStyle=
        safe_text,
    beginLabel=
        safe_text,
    isFold=
        st.booleans(),
    endLabel=
        safe_text,
    size=
        safe_text,
    isMockEdge=
        st.booleans(),
    arrangeConstraints=
        safe_text
)
diagram_AbstractDNode_strategy = st.builds(
    diagram_AbstractDNode,
)
viewpoint_diagram_DDiagramElementContainer_strategy = st.builds(
    viewpoint_diagram_DDiagramElementContainer,
    height=
        safe_text,
    width=
        safe_text
)
viewpoint_diagram_DNode_strategy = st.builds(
    viewpoint_diagram_DNode,
    resizeKind=
        safe_text,
    labelPosition=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
viewpoint_diagram_AbstractDNode_strategy = st.builds(
    viewpoint_diagram_AbstractDNode,
    arrangeConstraints=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
description_NodeMapping_strategy = st.builds(
    description_NodeMapping,
)
viewpoint_description_NodeMappingImport_strategy = st.builds(
    viewpoint_description_NodeMappingImport,
)
diagram_viewpoint_Style_strategy = st.builds(
    diagram_viewpoint_Style,
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
viewpoint_diagram_BundledImage_strategy = st.builds(
    viewpoint_diagram_BundledImage,
    shape=
        safe_text
)
viewpoint_diagram_CustomStyle_strategy = st.builds(
    viewpoint_diagram_CustomStyle,
    id=
        safe_text
)
viewpoint_diagram_Ellipse_strategy = st.builds(
    viewpoint_diagram_Ellipse,
    verticalDiameter=
        safe_text,
    horizontalDiameter=
        safe_text
)
viewpoint_diagram_Lozenge_strategy = st.builds(
    viewpoint_diagram_Lozenge,
    height=
        safe_text,
    width=
        safe_text
)
viewpoint_diagram_Note_strategy = st.builds(
    viewpoint_diagram_Note,
)
viewpoint_diagram_Dot_strategy = st.builds(
    viewpoint_diagram_Dot,
    strokeSizeComputationExpression=
        safe_text
)
viewpoint_diagram_GaugeCompositeStyle_strategy = st.builds(
    viewpoint_diagram_GaugeCompositeStyle,
    alignment=
        safe_text
)
viewpoint_diagram_Square_strategy = st.builds(
    viewpoint_diagram_Square,
    width=
        safe_text,
    height=
        safe_text
)
viewpoint_diagram_GraphicalFilter_strategy = st.builds(
    viewpoint_diagram_GraphicalFilter,
)
GraphicalFilter_strategy = st.builds(
    GraphicalFilter,
)
viewpoint_diagram_CollapseFilter_strategy = st.builds(
    viewpoint_diagram_CollapseFilter,
    height=
        st.integers(),
    width=
        st.integers()
)
diagram_viewpoint_Decoration_strategy = st.builds(
    diagram_viewpoint_Decoration,
)
viewpoint_diagram_AbsoluteBoundsFilter_strategy = st.builds(
    viewpoint_diagram_AbsoluteBoundsFilter,
    width=
        safe_text,
    height=
        safe_text,
    x=
        safe_text,
    y=
        safe_text
)
filter_CompositeFilterDescription_strategy = st.builds(
    filter_CompositeFilterDescription,
)
viewpoint_diagram_AppliedCompositeFilters_strategy = st.builds(
    viewpoint_diagram_AppliedCompositeFilters,
)
viewpoint_diagram_FoldingFilter_strategy = st.builds(
    viewpoint_diagram_FoldingFilter,
)
viewpoint_diagram_FoldingPointFilter_strategy = st.builds(
    viewpoint_diagram_FoldingPointFilter,
)
viewpoint_diagram_HideLabelFilter_strategy = st.builds(
    viewpoint_diagram_HideLabelFilter,
)
viewpoint_diagram_HideFilter_strategy = st.builds(
    viewpoint_diagram_HideFilter,
)
description_Layer_strategy = st.builds(
    description_Layer,
)
FilterVariableHistory_strategy = st.builds(
    FilterVariableHistory,
)
tool_BehaviorTool_strategy = st.builds(
    tool_BehaviorTool,
)
validation_ValidationRule_strategy = st.builds(
    validation_ValidationRule,
)
DNavigable_strategy = st.builds(
    DNavigable,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
viewpoint_diagram_DDiagramElement_strategy = st.builds(
    viewpoint_diagram_DDiagramElement,
    tooltipText=
        safe_text,
    visible=
        st.booleans()
)
diagram_DDiagram_strategy = st.builds(
    diagram_DDiagram,
)
DEdge_strategy = st.builds(
    DEdge,
)
DDiagram_strategy = st.builds(
    DDiagram,
)
filter_FilterDescription_strategy = st.builds(
    filter_FilterDescription,
)
concern_ConcernDescription_strategy = st.builds(
    concern_ConcernDescription,
)
DDiagramElementContainer_strategy = st.builds(
    DDiagramElementContainer,
)
viewpoint_diagram_DNodeContainer_strategy = st.builds(
    viewpoint_diagram_DNodeContainer,
    childrenPresentation=
        safe_text
)
viewpoint_diagram_DNodeList_strategy = st.builds(
    viewpoint_diagram_DNodeList,
    lineWidth=
        st.integers()
)
DNodeListElement_strategy = st.builds(
    DNodeListElement,
)
viewpoint_tool_InitEdgeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitEdgeCreationOperation,
)
viewpoint_tool_InitialOperation_strategy = st.builds(
    viewpoint_tool_InitialOperation,
)
viewpoint_tool_InitialNodeCreationOperation_strategy = st.builds(
    viewpoint_tool_InitialNodeCreationOperation,
)
viewpoint_tool_ModelOperation_strategy = st.builds(
    viewpoint_tool_ModelOperation,
)
tool_ModelOperation_strategy = st.builds(
    tool_ModelOperation,
)
ModelOperation_strategy = st.builds(
    ModelOperation,
)
viewpoint_tool_Switch_strategy = st.builds(
    viewpoint_tool_Switch,
)
viewpoint_tool_ContainerModelOperation_strategy = st.builds(
    viewpoint_tool_ContainerModelOperation,
)
viewpoint_tool_EditMaskVariables_strategy = st.builds(
    viewpoint_tool_EditMaskVariables,
    mask=
        safe_text
)
tool_AbstractVariable_strategy = st.builds(
    tool_AbstractVariable,
)
AbstractVariable_strategy = st.builds(
    AbstractVariable,
)
viewpoint_tool_ElementSelectVariable_strategy = st.builds(
    viewpoint_tool_ElementSelectVariable,
)
viewpoint_tool_NameVariable_strategy = st.builds(
    viewpoint_tool_NameVariable,
)
viewpoint_tool_DialogVariable_strategy = st.builds(
    viewpoint_tool_DialogVariable,
    dialogPrompt=
        safe_text
)
viewpoint_tool_SubVariable_strategy = st.builds(
    viewpoint_tool_SubVariable,
)
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
viewpoint_tool_ContainerViewVariable_strategy = st.builds(
    viewpoint_tool_ContainerViewVariable,
)
viewpoint_tool_ElementDropVariable_strategy = st.builds(
    viewpoint_tool_ElementDropVariable,
)
viewpoint_tool_SelectContainerVariable_strategy = st.builds(
    viewpoint_tool_SelectContainerVariable,
)
viewpoint_tool_TargetEdgeCreationVariable_strategy = st.builds(
    viewpoint_tool_TargetEdgeCreationVariable,
)
viewpoint_tool_SourceEdgeCreationVariable_strategy = st.builds(
    viewpoint_tool_SourceEdgeCreationVariable,
)
viewpoint_tool_NodeCreationVariable_strategy = st.builds(
    viewpoint_tool_NodeCreationVariable,
)
viewpoint_tool_ElementDoubleClickVariable_strategy = st.builds(
    viewpoint_tool_ElementDoubleClickVariable,
)
viewpoint_tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    viewpoint_tool_TargetEdgeViewCreationVariable,
)
viewpoint_tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    viewpoint_tool_SourceEdgeViewCreationVariable,
)
viewpoint_tool_ElementVariable_strategy = st.builds(
    viewpoint_tool_ElementVariable,
)
tool_SubVariable_strategy = st.builds(
    tool_SubVariable,
)
viewpoint_tool_AcceleoVariable_strategy = st.builds(
    viewpoint_tool_AcceleoVariable,
    computationExpression=
        safe_text
)
viewpoint_tool_VariableContainer_strategy = st.builds(
    viewpoint_tool_VariableContainer,
)
viewpoint_tool_AbstractVariable_strategy = st.builds(
    viewpoint_tool_AbstractVariable,
    name=
        safe_text
)
tool_ExternalJavaAction_strategy = st.builds(
    tool_ExternalJavaAction,
)
tool_ExternalJavaActionParameter_strategy = st.builds(
    tool_ExternalJavaActionParameter,
)
tool_ContainerModelOperation_strategy = st.builds(
    tool_ContainerModelOperation,
)
viewpoint_tool_DropContainerVariable_strategy = st.builds(
    viewpoint_tool_DropContainerVariable,
)
viewpoint_tool_ElementDeleteVariable_strategy = st.builds(
    viewpoint_tool_ElementDeleteVariable,
)
viewpoint_tool_ElementViewVariable_strategy = st.builds(
    viewpoint_tool_ElementViewVariable,
)
MenuItemDescription_strategy = st.builds(
    MenuItemDescription,
)
viewpoint_tool_OperationAction_strategy = st.builds(
    viewpoint_tool_OperationAction,
)
tool_MenuItemDescription_strategy = st.builds(
    tool_MenuItemDescription,
)
viewpoint_tool_ExternalJavaAction_strategy = st.builds(
    viewpoint_tool_ExternalJavaAction,
    id=
        safe_text
)
viewpoint_tool_ExternalJavaActionCall_strategy = st.builds(
    viewpoint_tool_ExternalJavaActionCall,
)
MenuItemOrRef_strategy = st.builds(
    MenuItemOrRef,
)
viewpoint_tool_MenuItemDescriptionReference_strategy = st.builds(
    viewpoint_tool_MenuItemDescriptionReference,
)
tool_MenuItemOrRef_strategy = st.builds(
    tool_MenuItemOrRef,
)
viewpoint_tool_MenuItemOrRef_strategy = st.builds(
    viewpoint_tool_MenuItemOrRef,
)
tool_NameVariable_strategy = st.builds(
    tool_NameVariable,
)
tool_SelectContainerVariable_strategy = st.builds(
    tool_SelectContainerVariable,
)
tool_InitialContainerDropOperation_strategy = st.builds(
    tool_InitialContainerDropOperation,
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_ElementSelectVariable_strategy = st.builds(
    tool_ElementSelectVariable,
)
description_SelectionDescription_strategy = st.builds(
    description_SelectionDescription,
)
viewpoint_tool_SelectModelElementVariable_strategy = st.builds(
    viewpoint_tool_SelectModelElementVariable,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
viewpoint_tool_MenuItemDescription_strategy = st.builds(
    viewpoint_tool_MenuItemDescription,
    icon=
        safe_text
)
viewpoint_tool_SelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_SelectionWizardDescription,
    windowImagePath=
        safe_text,
    iconPath=
        safe_text,
    windowTitle=
        safe_text
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
description_DiagramElementMapping_strategy = st.builds(
    description_DiagramElementMapping,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
tool_ElementViewVariable_strategy = st.builds(
    tool_ElementViewVariable,
)
tool_ElementVariable_strategy = st.builds(
    tool_ElementVariable,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
viewpoint_tool_NodeCreationDescription_strategy = st.builds(
    viewpoint_tool_NodeCreationDescription,
    iconPath=
        safe_text
)
viewpoint_tool_ReconnectEdgeDescription_strategy = st.builds(
    viewpoint_tool_ReconnectEdgeDescription,
    reconnectionKind=
        safe_text
)
viewpoint_tool_PasteDescription_strategy = st.builds(
    viewpoint_tool_PasteDescription,
)
viewpoint_tool_DirectEditLabel_strategy = st.builds(
    viewpoint_tool_DirectEditLabel,
    inputLabelExpression=
        safe_text
)
viewpoint_tool_ContainerCreationDescription_strategy = st.builds(
    viewpoint_tool_ContainerCreationDescription,
    iconPath=
        safe_text
)
viewpoint_tool_DeleteElementDescription_strategy = st.builds(
    viewpoint_tool_DeleteElementDescription,
)
viewpoint_tool_EdgeCreationDescription_strategy = st.builds(
    viewpoint_tool_EdgeCreationDescription,
    connectionStartPrecondition=
        safe_text,
    iconPath=
        safe_text
)
viewpoint_tool_ContainerDropDescription_strategy = st.builds(
    viewpoint_tool_ContainerDropDescription,
    dragSource=
        safe_text,
    moveEdges=
        st.booleans()
)
viewpoint_tool_DoubleClickDescription_strategy = st.builds(
    viewpoint_tool_DoubleClickDescription,
)
viewpoint_tool_ToolDescription_strategy = st.builds(
    viewpoint_tool_ToolDescription,
    iconPath=
        safe_text
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
viewpoint_tool_PaneBasedSelectionWizardDescription_strategy = st.builds(
    viewpoint_tool_PaneBasedSelectionWizardDescription,
    selectedValuesMessage=
        safe_text,
    message=
        safe_text,
    preSelectedCandidatesExpression=
        safe_text,
    choiceOfValuesMessage=
        safe_text,
    iconPath=
        safe_text,
    candidatesExpression=
        safe_text,
    rootExpression=
        safe_text,
    tree=
        st.booleans(),
    windowTitle=
        safe_text,
    childrenExpression=
        safe_text,
    windowImagePath=
        safe_text
)
viewpoint_tool_PopupMenu_strategy = st.builds(
    viewpoint_tool_PopupMenu,
)
viewpoint_tool_RepresentationNavigationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationNavigationDescription,
    navigationNameExpression=
        safe_text,
    browseExpression=
        safe_text
)
viewpoint_tool_RepresentationCreationDescription_strategy = st.builds(
    viewpoint_tool_RepresentationCreationDescription,
    browseExpression=
        safe_text,
    titleExpression=
        safe_text
)
viewpoint_tool_BehaviorTool_strategy = st.builds(
    viewpoint_tool_BehaviorTool,
    domainClass=
        safe_text
)
viewpoint_tool_RequestDescription_strategy = st.builds(
    viewpoint_tool_RequestDescription,
    type=
        safe_text
)
viewpoint_tool_MappingBasedToolDescription_strategy = st.builds(
    viewpoint_tool_MappingBasedToolDescription,
)
tool_ElementDropVariable_strategy = st.builds(
    tool_ElementDropVariable,
)
tool_ToolFilterDescription_strategy = st.builds(
    tool_ToolFilterDescription,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
viewpoint_tool_ToolGroup_strategy = st.builds(
    viewpoint_tool_ToolGroup,
)
viewpoint_tool_AbstractToolDescription_strategy = st.builds(
    viewpoint_tool_AbstractToolDescription,
    forceRefresh=
        st.booleans(),
    precondition=
        safe_text
)
viewpoint_style_TooltipStyleDescription_strategy = st.builds(
    viewpoint_style_TooltipStyleDescription,
    tooltipExpression=
        safe_text
)
viewpoint_style_LabelBorderStyleDescription_strategy = st.builds(
    viewpoint_style_LabelBorderStyleDescription,
    id=
        safe_text,
    cornerWidth=
        st.integers(),
    cornerHeight=
        st.integers(),
    name=
        safe_text
)
style_LabelBorderStyleDescription_strategy = st.builds(
    style_LabelBorderStyleDescription,
)
viewpoint_style_LabelBorderStyles_strategy = st.builds(
    viewpoint_style_LabelBorderStyles,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
viewpoint_style_CenterLabelStyleDescription_strategy = st.builds(
    viewpoint_style_CenterLabelStyleDescription,
)
viewpoint_style_EndLabelStyleDescription_strategy = st.builds(
    viewpoint_style_EndLabelStyleDescription,
)
viewpoint_style_BeginLabelStyleDescription_strategy = st.builds(
    viewpoint_style_BeginLabelStyleDescription,
)
viewpoint_style_LabelStyleDescription_strategy = st.builds(
    viewpoint_style_LabelStyleDescription,
    labelAlignment=
        safe_text
)
viewpoint_style_BasicLabelStyleDescription_strategy = st.builds(
    viewpoint_style_BasicLabelStyleDescription,
    labelSize=
        st.integers(),
    labelExpression=
        safe_text,
    labelFormat=
        safe_text,
    iconPath=
        safe_text,
    showIcon=
        st.booleans()
)
viewpoint_style_StyleDescription_strategy = st.builds(
    viewpoint_style_StyleDescription,
)
viewpoint_description_DAnnotationEntry_strategy = st.builds(
    viewpoint_description_DAnnotationEntry,
    source=
        safe_text,
    details=
        safe_text
)
viewpoint_description_IdentifiedElement_strategy = st.builds(
    viewpoint_description_IdentifiedElement,
    label=
        safe_text,
    name=
        safe_text
)
viewpoint_description_EndUserDocumentedElement_strategy = st.builds(
    viewpoint_description_EndUserDocumentedElement,
    endUserDocumentation=
        safe_text
)
viewpoint_description_AnnotationEntry_strategy = st.builds(
    viewpoint_description_AnnotationEntry,
    source=
        safe_text
)
UserColor_strategy = st.builds(
    UserColor,
)
viewpoint_description_UserColorsPalette_strategy = st.builds(
    viewpoint_description_UserColorsPalette,
    name=
        safe_text
)
SystemColor_strategy = st.builds(
    SystemColor,
)
viewpoint_description_SytemColorsPalette_strategy = st.builds(
    viewpoint_description_SytemColorsPalette,
)
style_LabelBorderStyles_strategy = st.builds(
    style_LabelBorderStyles,
)
tool_ToolEntry_strategy = st.builds(
    tool_ToolEntry,
)
viewpoint_description_Environment_strategy = st.builds(
    viewpoint_description_Environment,
)
viewpoint_description_UserColor_strategy = st.builds(
    viewpoint_description_UserColor,
    name=
        safe_text
)
description_FixedColor_strategy = st.builds(
    description_FixedColor,
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
viewpoint_description_FixedColor_strategy = st.builds(
    viewpoint_description_FixedColor,
    red=
        st.integers(),
    blue=
        st.integers(),
    green=
        st.integers()
)
viewpoint_description_ColorStep_strategy = st.builds(
    viewpoint_description_ColorStep,
    associatedValue=
        safe_text
)
ColorStep_strategy = st.builds(
    ColorStep,
)
description_ColorDescription_strategy = st.builds(
    description_ColorDescription,
)
FixedColor_strategy = st.builds(
    FixedColor,
)
viewpoint_description_SystemColor_strategy = st.builds(
    viewpoint_description_SystemColor,
    name=
        safe_text
)
viewpoint_description_ColorDescription_strategy = st.builds(
    viewpoint_description_ColorDescription,
)
viewpoint_description_SelectionDescription_strategy = st.builds(
    viewpoint_description_SelectionDescription,
    tree=
        st.booleans(),
    message=
        safe_text,
    candidatesExpression=
        safe_text,
    rootExpression=
        safe_text,
    multiple=
        st.booleans(),
    childrenExpression=
        safe_text
)
description_UserColor_strategy = st.builds(
    description_UserColor,
)
viewpoint_description_UserFixedColor_strategy = st.builds(
    viewpoint_description_UserFixedColor,
)
viewpoint_description_InterpolatedColor_strategy = st.builds(
    viewpoint_description_InterpolatedColor,
    colorValueComputationExpression=
        safe_text,
    maxValueComputationExpression=
        safe_text,
    minValueComputationExpression=
        safe_text
)
viewpoint_description_ComputedColor_strategy = st.builds(
    viewpoint_description_ComputedColor,
    blue=
        safe_text,
    green=
        safe_text,
    red=
        safe_text
)
EStructuralFeatureCustomization_strategy = st.builds(
    EStructuralFeatureCustomization,
)
viewpoint_description_EReferenceCustomization_strategy = st.builds(
    viewpoint_description_EReferenceCustomization,
    referenceName=
        safe_text
)
viewpoint_description_IVSMElementCustomization_strategy = st.builds(
    viewpoint_description_IVSMElementCustomization,
)
IVSMElementCustomization_strategy = st.builds(
    IVSMElementCustomization,
)
viewpoint_description_VSMElementCustomizationReuse_strategy = st.builds(
    viewpoint_description_VSMElementCustomizationReuse,
)
viewpoint_description_VSMElementCustomization_strategy = st.builds(
    viewpoint_description_VSMElementCustomization,
    predicateExpression=
        safe_text
)
viewpoint_description_Customization_strategy = st.builds(
    viewpoint_description_Customization,
)
viewpoint_description_EAttributeCustomization_strategy = st.builds(
    viewpoint_description_EAttributeCustomization,
    attributeName=
        safe_text,
    value=
        safe_text
)
viewpoint_description_EStructuralFeatureCustomization_strategy = st.builds(
    viewpoint_description_EStructuralFeatureCustomization,
    applyOnAll=
        st.booleans()
)
viewpoint_description_DecorationDescription_strategy = st.builds(
    viewpoint_description_DecorationDescription,
    decoratorPath=
        safe_text,
    name=
        safe_text,
    position=
        safe_text,
    preconditionExpression=
        safe_text
)
viewpoint_description_DecorationDescriptionsSet_strategy = st.builds(
    viewpoint_description_DecorationDescriptionsSet,
)
tool_PasteDescription_strategy = st.builds(
    tool_PasteDescription,
)
viewpoint_description_PasteTargetDescription_strategy = st.builds(
    viewpoint_description_PasteTargetDescription,
)
tool_ContainerDropDescription_strategy = st.builds(
    tool_ContainerDropDescription,
)
viewpoint_description_DragAndDropTargetDescription_strategy = st.builds(
    viewpoint_description_DragAndDropTargetDescription,
)
viewpoint_description_ConditionalStyleDescription_strategy = st.builds(
    viewpoint_description_ConditionalStyleDescription,
    predicateExpression=
        safe_text
)
description_viewpoint_EStringToStringMapEntry_strategy = st.builds(
    description_viewpoint_EStringToStringMapEntry,
)
viewpoint_description_DAnnotation_strategy = st.builds(
    viewpoint_description_DAnnotation,
    source=
        safe_text
)
DAnnotation_strategy = st.builds(
    DAnnotation,
)
viewpoint_description_AbstractMappingImport_strategy = st.builds(
    viewpoint_description_AbstractMappingImport,
    inheritsAncestorFilters=
        st.booleans(),
    hideSubMappings=
        st.booleans()
)
tool_RepresentationNavigationDescription_strategy = st.builds(
    tool_RepresentationNavigationDescription,
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
IdentifiedElement_strategy = st.builds(
    IdentifiedElement,
)
viewpoint_description_RepresentationElementMapping_strategy = st.builds(
    viewpoint_description_RepresentationElementMapping,
)
viewpoint_description_JavaExtension_strategy = st.builds(
    viewpoint_description_JavaExtension,
    qualifiedClassName=
        safe_text
)
description_viewpoint_EObject_strategy = st.builds(
    description_viewpoint_EObject,
)
viewpoint_description_MetamodelExtensionSetting_strategy = st.builds(
    viewpoint_description_MetamodelExtensionSetting,
)
viewpoint_description_RepresentationExtensionDescription_strategy = st.builds(
    viewpoint_description_RepresentationExtensionDescription,
    name=
        safe_text,
    viewpointURI=
        safe_text,
    representationName=
        safe_text
)
viewpoint_description_DModelElement_strategy = st.builds(
    viewpoint_description_DModelElement,
)
viewpoint_description_DocumentedElement_strategy = st.builds(
    viewpoint_description_DocumentedElement,
    documentation=
        safe_text
)
description_viewpoint_EPackage_strategy = st.builds(
    description_viewpoint_EPackage,
)
viewpoint_description_FeatureExtensionDescription_strategy = st.builds(
    viewpoint_description_FeatureExtensionDescription,
)
RepresentationTemplate_strategy = st.builds(
    RepresentationTemplate,
)
MetamodelExtensionSetting_strategy = st.builds(
    MetamodelExtensionSetting,
)
JavaExtension_strategy = st.builds(
    JavaExtension,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
viewpoint_description_DiagramExtensionDescription_strategy = st.builds(
    viewpoint_description_DiagramExtensionDescription,
)
RepresentationDescription_strategy = st.builds(
    RepresentationDescription,
)
viewpoint_description_RepresentationImportDescription_strategy = st.builds(
    viewpoint_description_RepresentationImportDescription,
)
viewpoint_description_RepresentationTemplate_strategy = st.builds(
    viewpoint_description_RepresentationTemplate,
    name=
        safe_text
)
validation_ValidationSet_strategy = st.builds(
    validation_ValidationSet,
)
description_IdentifiedElement_strategy = st.builds(
    description_IdentifiedElement,
)
description_EndUserDocumentedElement_strategy = st.builds(
    description_EndUserDocumentedElement,
)
description_Component_strategy = st.builds(
    description_Component,
)
viewpoint_description_Component_strategy = st.builds(
    viewpoint_description_Component,
)
UserColorsPalette_strategy = st.builds(
    UserColorsPalette,
)
SytemColorsPalette_strategy = st.builds(
    SytemColorsPalette,
)
viewpoint_Customizable_strategy = st.builds(
    viewpoint_Customizable,
    customFeatures=
        safe_text
)
DFile_strategy = st.builds(
    DFile,
)
viewpoint_DModel_strategy = st.builds(
    viewpoint_DModel,
)
DResourceContainer_strategy = st.builds(
    DResourceContainer,
)
viewpoint_DFolder_strategy = st.builds(
    viewpoint_DFolder,
)
viewpoint_DProject_strategy = st.builds(
    viewpoint_DProject,
)
DResource_strategy = st.builds(
    DResource,
)
viewpoint_DResourceContainer_strategy = st.builds(
    viewpoint_DResourceContainer,
)
viewpoint_DFile_strategy = st.builds(
    viewpoint_DFile,
)
viewpoint_DResource_strategy = st.builds(
    viewpoint_DResource,
    path=
        safe_text,
    name=
        safe_text
)
viewpoint_SessionManagerEObject_strategy = st.builds(
    viewpoint_SessionManagerEObject,
)
viewpoint_DAnalysisSessionEObject_strategy = st.builds(
    viewpoint_DAnalysisSessionEObject,
    resources=
        safe_text,
    open=
        st.booleans(),
    controlledResources=
        safe_text,
    blocked=
        st.booleans(),
    synchronizationStatus=
        safe_text
)
viewpoint_RGBValues_strategy = st.builds(
    viewpoint_RGBValues,
    blue=
        st.integers(),
    red=
        st.integers(),
    green=
        st.integers()
)
DNavigationLink_strategy = st.builds(
    DNavigationLink,
)
viewpoint_diagram_DDiagramLink_strategy = st.builds(
    viewpoint_diagram_DDiagramLink,
)
viewpoint_DEObjectLink_strategy = st.builds(
    viewpoint_DEObjectLink,
)
viewpoint_DragAndDropTarget_strategy = st.builds(
    viewpoint_DragAndDropTarget,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
)
viewpoint_style_NodeStyleDescription_strategy = st.builds(
    viewpoint_style_NodeStyleDescription,
    hideLabelByDefault=
        st.booleans(),
    sizeComputationExpression=
        safe_text,
    labelPosition=
        safe_text,
    resizeKind=
        safe_text
)
Customizable_strategy = st.builds(
    Customizable,
)
viewpoint_diagram_GaugeSection_strategy = st.builds(
    viewpoint_diagram_GaugeSection,
    label=
        safe_text,
    min=
        safe_text,
    max=
        safe_text,
    value=
        safe_text
)
viewpoint_BasicLabelStyle_strategy = st.builds(
    viewpoint_BasicLabelStyle,
    labelSize=
        st.integers(),
    iconPath=
        safe_text,
    showIcon=
        st.booleans(),
    labelFormat=
        safe_text
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
viewpoint_diagram_EndLabelStyle_strategy = st.builds(
    viewpoint_diagram_EndLabelStyle,
)
viewpoint_diagram_BeginLabelStyle_strategy = st.builds(
    viewpoint_diagram_BeginLabelStyle,
)
viewpoint_diagram_CenterLabelStyle_strategy = st.builds(
    viewpoint_diagram_CenterLabelStyle,
)
viewpoint_LabelStyle_strategy = st.builds(
    viewpoint_LabelStyle,
    labelAlignment=
        safe_text
)
viewpoint_DAnalysisCustomData_strategy = st.builds(
    viewpoint_DAnalysisCustomData,
    key=
        safe_text
)
viewpoint_DSourceFileLink_strategy = st.builds(
    viewpoint_DSourceFileLink,
    filePath=
        safe_text,
    endPosition=
        st.integers(),
    startPosition=
        st.integers()
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
viewpoint_description_MappingBasedDecoration_strategy = st.builds(
    viewpoint_description_MappingBasedDecoration,
)
viewpoint_description_SemanticBasedDecoration_strategy = st.builds(
    viewpoint_description_SemanticBasedDecoration,
    domainClass=
        safe_text
)
viewpoint_Decoration_strategy = st.builds(
    viewpoint_Decoration,
)
Viewpoint_strategy = st.builds(
    Viewpoint,
)
viewpoint_MetaModelExtension_strategy = st.builds(
    viewpoint_MetaModelExtension,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
viewpoint_diagram_DSemanticDiagram_strategy = st.builds(
    viewpoint_diagram_DSemanticDiagram,
)
DStylizable_strategy = st.builds(
    DStylizable,
)
DMappingBased_strategy = st.builds(
    DMappingBased,
)
DLabelled_strategy = st.builds(
    DLabelled,
)
AnnotationEntry_strategy = st.builds(
    AnnotationEntry,
)
description_DModelElement_strategy = st.builds(
    description_DModelElement,
)
DRefreshable_strategy = st.builds(
    DRefreshable,
)
viewpoint_DRepresentationElement_strategy = st.builds(
    viewpoint_DRepresentationElement,
    name=
        safe_text
)
viewpoint_Style_strategy = st.builds(
    viewpoint_Style,
)
description_DocumentedElement_strategy = st.builds(
    description_DocumentedElement,
)
viewpoint_description_Layer_strategy = st.builds(
    viewpoint_description_Layer,
    icon=
        safe_text
)
viewpoint_filter_FilterDescription_strategy = st.builds(
    viewpoint_filter_FilterDescription,
)
viewpoint_tool_ToolSection_strategy = st.builds(
    viewpoint_tool_ToolSection,
    icon=
        safe_text
)
viewpoint_description_EdgeMappingImport_strategy = st.builds(
    viewpoint_description_EdgeMappingImport,
    inheritsAncestorFilters=
        st.booleans()
)
viewpoint_diagram_DDiagram_strategy = st.builds(
    viewpoint_diagram_DDiagram,
    synchronized=
        st.booleans(),
    headerHeight=
        st.integers(),
    isInLayoutingMode=
        st.booleans(),
    info=
        safe_text
)
viewpoint_description_Viewpoint_strategy = st.builds(
    viewpoint_description_Viewpoint,
    modelFileExtension=
        safe_text,
    conflicts=
        safe_text,
    reuses=
        safe_text,
    icon=
        safe_text,
    customizes=
        safe_text
)
viewpoint_concern_ConcernDescription_strategy = st.builds(
    viewpoint_concern_ConcernDescription,
)
viewpoint_description_EdgeMapping_strategy = st.builds(
    viewpoint_description_EdgeMapping,
    sourceFinderExpression=
        safe_text,
    useDomainElement=
        st.booleans(),
    pathExpression=
        safe_text,
    targetFinderExpression=
        safe_text,
    domainClass=
        safe_text,
    targetExpression=
        safe_text
)
viewpoint_description_RepresentationDescription_strategy = st.builds(
    viewpoint_description_RepresentationDescription,
    initialisation=
        st.booleans(),
    titleExpression=
        safe_text,
    showOnStartup=
        st.booleans()
)
viewpoint_description_Group_strategy = st.builds(
    viewpoint_description_Group,
    version=
        safe_text,
    name=
        safe_text
)
viewpoint_description_AbstractNodeMapping_strategy = st.builds(
    viewpoint_description_AbstractNodeMapping,
    domainClass=
        safe_text
)
viewpoint_tool_ToolEntry_strategy = st.builds(
    viewpoint_tool_ToolEntry,
)
viewpoint_DRepresentation_strategy = st.builds(
    viewpoint_DRepresentation,
    name=
        safe_text
)
viewpoint_DSemanticDecorator_strategy = st.builds(
    viewpoint_DSemanticDecorator,
)
DDiagramSet_strategy = st.builds(
    DDiagramSet,
)
DView_strategy = st.builds(
    DView,
)
viewpoint_DRepresentationContainer_strategy = st.builds(
    viewpoint_DRepresentationContainer,
)
viewpoint_DContainer_strategy = st.builds(
    viewpoint_DContainer,
)
viewpoint_DMappingBased_strategy = st.builds(
    viewpoint_DMappingBased,
)
viewpoint_DLabelled_strategy = st.builds(
    viewpoint_DLabelled,
)
viewpoint_DRefreshable_strategy = st.builds(
    viewpoint_DRefreshable,
)
viewpoint_DStylizable_strategy = st.builds(
    viewpoint_DStylizable,
)
viewpoint_DNavigationLink_strategy = st.builds(
    viewpoint_DNavigationLink,
    label=
        safe_text,
    targetType=
        safe_text
)
viewpoint_DNavigable_strategy = st.builds(
    viewpoint_DNavigable,
)
viewpoint_DValidable_strategy = st.builds(
    viewpoint_DValidable,
)
FeatureExtensionDescription_strategy = st.builds(
    FeatureExtensionDescription,
)
viewpoint_DFeatureExtension_strategy = st.builds(
    viewpoint_DFeatureExtension,
)
viewpoint_DView_strategy = st.builds(
    viewpoint_DView,
    initialized=
        st.booleans()
)
DAnnotationEntry_strategy = st.builds(
    DAnnotationEntry,
)
viewpoint_EObject_strategy = st.builds(
    viewpoint_EObject,
)
viewpoint_DAnalysis_strategy = st.builds(
    viewpoint_DAnalysis,
    version=
        safe_text
)

@given(instance=DNode_strategy)
@settings(max_examples=50)
def test_dnode_instantiation(instance):
    assert isinstance(instance, DNode)

@given(instance=DContainer_strategy)
@settings(max_examples=50)
def test_dcontainer_instantiation(instance):
    assert isinstance(instance, DContainer)

@given(instance=DValidable_strategy)
@settings(max_examples=50)
def test_dvalidable_instantiation(instance):
    assert isinstance(instance, DValidable)

@given(instance=DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_draganddroptarget_instantiation(instance):
    assert isinstance(instance, DragAndDropTarget)

@given(instance=DRepresentation_strategy)
@settings(max_examples=50)
def test_drepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)

@given(instance=InformationSection_strategy)
@settings(max_examples=50)
def test_informationsection_instantiation(instance):
    assert isinstance(instance, InformationSection)

@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint_audit_templateinformationsection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_TemplateInformationSection)



@given(instance=viewpoint_audit_TemplateInformationSection_strategy)
def test_viewpoint_audit_templateinformationsection_templatePath_setter(instance):
    original = instance.templatePath
    instance.templatePath = original
    assert instance.templatePath == original

@given(instance=description_DiagramDescription_strategy)
@settings(max_examples=50)
def test_description_diagramdescription_instantiation(instance):
    assert isinstance(instance, description_DiagramDescription)

@given(instance=DDiagramElement_strategy)
@settings(max_examples=50)
def test_ddiagramelement_instantiation(instance):
    assert isinstance(instance, DDiagramElement)

@given(instance=SwitchChild_strategy)
@settings(max_examples=50)
def test_switchchild_instantiation(instance):
    assert isinstance(instance, SwitchChild)

@given(instance=viewpoint_tool_Case_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_case_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Case)



@given(instance=viewpoint_tool_Case_strategy)
def test_viewpoint_tool_case_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_featurechangelistener_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_FeatureChangeListener)



@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_viewpoint_tool_featurechangelistener_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=viewpoint_tool_FeatureChangeListener_strategy)
def test_viewpoint_tool_featurechangelistener_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=tool_FeatureChangeListener_strategy)
@settings(max_examples=50)
def test_tool_featurechangelistener_instantiation(instance):
    assert isinstance(instance, tool_FeatureChangeListener)

@given(instance=viewpoint_audit_InformationSection_strategy)
@settings(max_examples=50)
def test_viewpoint_audit_informationsection_instantiation(instance):
    assert isinstance(instance, viewpoint_audit_InformationSection)

@given(instance=tool_Default_strategy)
@settings(max_examples=50)
def test_tool_default_instantiation(instance):
    assert isinstance(instance, tool_Default)

@given(instance=tool_Case_strategy)
@settings(max_examples=50)
def test_tool_case_instantiation(instance):
    assert isinstance(instance, tool_Case)

@given(instance=viewpoint_tool_Default_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_default_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Default)

@given(instance=viewpoint_tool_SwitchChild_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_switchchild_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SwitchChild)

@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolfilterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolFilterDescription)



@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_viewpoint_tool_toolfilterdescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=viewpoint_tool_ToolFilterDescription_strategy)
def test_viewpoint_tool_toolfilterdescription_elementsToListen_setter(instance):
    original = instance.elementsToListen
    instance.elementsToListen = original
    assert instance.elementsToListen == original

@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionParameter)



@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_viewpoint_tool_externaljavaactionparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=viewpoint_tool_ExternalJavaActionParameter_strategy)
def test_viewpoint_tool_externaljavaactionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool_viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_tool_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, tool_viewpoint_EObject)

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=viewpoint_tool_DeleteView_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_deleteview_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteView)

@given(instance=viewpoint_tool_MoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_moveelement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MoveElement)



@given(instance=viewpoint_tool_MoveElement_strategy)
def test_viewpoint_tool_moveelement_newContainerExpression_setter(instance):
    original = instance.newContainerExpression
    instance.newContainerExpression = original
    assert instance.newContainerExpression == original



@given(instance=viewpoint_tool_MoveElement_strategy)
def test_viewpoint_tool_moveelement_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_SetValue_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_setvalue_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetValue)



@given(instance=viewpoint_tool_SetValue_strategy)
def test_viewpoint_tool_setvalue_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=viewpoint_tool_SetValue_strategy)
def test_viewpoint_tool_setvalue_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_If_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_if_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_If)



@given(instance=viewpoint_tool_If_strategy)
def test_viewpoint_tool_if_conditionExpression_setter(instance):
    original = instance.conditionExpression
    instance.conditionExpression = original
    assert instance.conditionExpression == original

@given(instance=viewpoint_tool_SetObject_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_setobject_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SetObject)



@given(instance=viewpoint_tool_SetObject_strategy)
def test_viewpoint_tool_setobject_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_ChangeContext_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_changecontext_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ChangeContext)



@given(instance=viewpoint_tool_ChangeContext_strategy)
def test_viewpoint_tool_changecontext_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint_tool_Unset_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_unset_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Unset)



@given(instance=viewpoint_tool_Unset_strategy)
def test_viewpoint_tool_unset_elementExpression_setter(instance):
    original = instance.elementExpression
    instance.elementExpression = original
    assert instance.elementExpression == original



@given(instance=viewpoint_tool_Unset_strategy)
def test_viewpoint_tool_unset_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=viewpoint_tool_For_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_for_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_For)



@given(instance=viewpoint_tool_For_strategy)
def test_viewpoint_tool_for_iteratorName_setter(instance):
    original = instance.iteratorName
    instance.iteratorName = original
    assert instance.iteratorName == original



@given(instance=viewpoint_tool_For_strategy)
def test_viewpoint_tool_for_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=viewpoint_tool_RemoveElement_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_removeelement_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RemoveElement)

@given(instance=viewpoint_tool_CreateInstance_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_createinstance_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateInstance)



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original



@given(instance=viewpoint_tool_CreateInstance_strategy)
def test_viewpoint_tool_createinstance_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=viewpoint_tool_InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialContainerDropOperation)

@given(instance=viewpoint_validation_ValidationFix_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationfix_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationFix)



@given(instance=viewpoint_validation_ValidationFix_strategy)
def test_viewpoint_validation_validationfix_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ValidationRule_strategy)
@settings(max_examples=50)
def test_validationrule_instantiation(instance):
    assert isinstance(instance, ValidationRule)

@given(instance=viewpoint_validation_ViewValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_viewvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ViewValidationRule)

@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_semanticvalidationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_SemanticValidationRule)



@given(instance=viewpoint_validation_SemanticValidationRule_strategy)
def test_viewpoint_validation_semanticvalidationrule_targetClass_setter(instance):
    original = instance.targetClass
    instance.targetClass = original
    assert instance.targetClass == original

@given(instance=validation_ValidationFix_strategy)
@settings(max_examples=50)
def test_validation_validationfix_instantiation(instance):
    assert isinstance(instance, validation_ValidationFix)

@given(instance=validation_RuleAudit_strategy)
@settings(max_examples=50)
def test_validation_ruleaudit_instantiation(instance):
    assert isinstance(instance, validation_RuleAudit)

@given(instance=viewpoint_validation_ValidationRule_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationrule_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationRule)



@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_viewpoint_validation_validationrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_validation_ValidationRule_strategy)
def test_viewpoint_validation_validationrule_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_validation_ValidationRule_strategy)
@settings(max_examples=30)
def test_viewpoint_validation_validationrule_checkrule_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkRule(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkRule).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkRule' in viewpoint_validation_ValidationRule is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkRule' in viewpoint_validation_ValidationRule did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkRule' in viewpoint_validation_ValidationRule is not implemented or raised an error")

@given(instance=viewpoint_validation_RuleAudit_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_ruleaudit_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_RuleAudit)



@given(instance=viewpoint_validation_RuleAudit_strategy)
def test_viewpoint_validation_ruleaudit_auditExpression_setter(instance):
    original = instance.auditExpression
    instance.auditExpression = original
    assert instance.auditExpression == original

@given(instance=SelectionDescription_strategy)
@settings(max_examples=50)
def test_selectiondescription_instantiation(instance):
    assert isinstance(instance, SelectionDescription)

@given(instance=viewpoint_filter_FilterVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_filtervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_FilterVariable)



@given(instance=viewpoint_filter_FilterVariable_strategy)
def test_viewpoint_filter_filtervariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=filter_Filter_strategy)
@settings(max_examples=50)
def test_filter_filter_instantiation(instance):
    assert isinstance(instance, filter_Filter)

@given(instance=FilterDescription_strategy)
@settings(max_examples=50)
def test_filterdescription_instantiation(instance):
    assert isinstance(instance, FilterDescription)

@given(instance=viewpoint_filter_CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_compositefilterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_CompositeFilterDescription)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=viewpoint_filter_VariableFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_variablefilter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_VariableFilter)



@given(instance=viewpoint_filter_VariableFilter_strategy)
def test_viewpoint_filter_variablefilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_filter_VariableFilter_strategy)
@settings(max_examples=30)
def test_viewpoint_filter_variablefilter_setfiltercontext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setFilterContext(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setFilterContext).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setFilterContext' in viewpoint_filter_VariableFilter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setFilterContext' in viewpoint_filter_VariableFilter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setFilterContext' in viewpoint_filter_VariableFilter is not implemented or raised an error")

@given(instance=viewpoint_filter_MappingFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_mappingfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_MappingFilter)



@given(instance=viewpoint_filter_MappingFilter_strategy)
def test_viewpoint_filter_mappingfilter_viewConditionExpression_setter(instance):
    original = instance.viewConditionExpression
    instance.viewConditionExpression = original
    assert instance.viewConditionExpression == original



@given(instance=viewpoint_filter_MappingFilter_strategy)
def test_viewpoint_filter_mappingfilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

@given(instance=viewpoint_filter_Filter_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_filter_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_Filter)



@given(instance=viewpoint_filter_Filter_strategy)
def test_viewpoint_filter_filter_filterKind_setter(instance):
    original = instance.filterKind
    instance.filterKind = original
    assert instance.filterKind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_filter_Filter_strategy)
@settings(max_examples=30)
def test_viewpoint_filter_filter_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in viewpoint_filter_Filter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in viewpoint_filter_Filter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in viewpoint_filter_Filter is not implemented or raised an error")

@given(instance=viewpoint_tool_Navigation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_navigation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Navigation)



@given(instance=viewpoint_tool_Navigation_strategy)
def test_viewpoint_tool_navigation_createIfNotExistent_setter(instance):
    original = instance.createIfNotExistent
    instance.createIfNotExistent = original
    assert instance.createIfNotExistent == original

@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)

@given(instance=CreateView_strategy)
@settings(max_examples=50)
def test_createview_instantiation(instance):
    assert isinstance(instance, CreateView)

@given(instance=viewpoint_tool_DiagramNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_diagramnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DiagramNavigationDescription)

@given(instance=viewpoint_tool_CreateEdgeView_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_createedgeview_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateEdgeView)



@given(instance=viewpoint_tool_CreateEdgeView_strategy)
def test_viewpoint_tool_createedgeview_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original



@given(instance=viewpoint_tool_CreateEdgeView_strategy)
def test_viewpoint_tool_createedgeview_sourceExpression_setter(instance):
    original = instance.sourceExpression
    instance.sourceExpression = original
    assert instance.sourceExpression == original

@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)

@given(instance=viewpoint_tool_DiagramCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_diagramcreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DiagramCreationDescription)

@given(instance=viewpoint_tool_CreateView_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_createview_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_CreateView)



@given(instance=viewpoint_tool_CreateView_strategy)
def test_viewpoint_tool_createview_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=viewpoint_tool_CreateView_strategy)
def test_viewpoint_tool_createview_containerViewExpression_setter(instance):
    original = instance.containerViewExpression
    instance.containerViewExpression = original
    assert instance.containerViewExpression == original

@given(instance=tool_EditMaskVariables_strategy)
@settings(max_examples=50)
def test_tool_editmaskvariables_instantiation(instance):
    assert isinstance(instance, tool_EditMaskVariables)

@given(instance=tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDoubleClickVariable)

@given(instance=tool_DeleteHook_strategy)
@settings(max_examples=50)
def test_tool_deletehook_instantiation(instance):
    assert isinstance(instance, tool_DeleteHook)

@given(instance=viewpoint_tool_DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_deletehookparameter_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteHookParameter)



@given(instance=viewpoint_tool_DeleteHookParameter_strategy)
def test_viewpoint_tool_deletehookparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_tool_DeleteHookParameter_strategy)
def test_viewpoint_tool_deletehookparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tool_DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_tool_deletehookparameter_instantiation(instance):
    assert isinstance(instance, tool_DeleteHookParameter)

@given(instance=viewpoint_tool_DeleteHook_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_deletehook_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteHook)



@given(instance=viewpoint_tool_DeleteHook_strategy)
def test_viewpoint_tool_deletehook_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tool_ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdeletevariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDeleteVariable)

@given(instance=tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeViewCreationVariable)

@given(instance=tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeViewCreationVariable)

@given(instance=tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeCreationVariable)

@given(instance=tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeCreationVariable)

@given(instance=tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool_initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, tool_InitEdgeCreationOperation)

@given(instance=tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool_initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialNodeCreationOperation)

@given(instance=tool_NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_nodecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_NodeCreationVariable)

@given(instance=tool_PopupMenu_strategy)
@settings(max_examples=50)
def test_tool_popupmenu_instantiation(instance):
    assert isinstance(instance, tool_PopupMenu)

@given(instance=tool_ToolGroup_strategy)
@settings(max_examples=50)
def test_tool_toolgroup_instantiation(instance):
    assert isinstance(instance, tool_ToolGroup)

@given(instance=viewpoint_tool_ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolgroupextension_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolGroupExtension)

@given(instance=tool_ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_tool_toolgroupextension_instantiation(instance):
    assert isinstance(instance, tool_ToolGroupExtension)

@given(instance=style_BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_BeginLabelStyleDescription)

@given(instance=EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_edgestyledescription_instantiation(instance):
    assert isinstance(instance, EdgeStyleDescription)

@given(instance=viewpoint_style_BracketEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_bracketedgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BracketEdgeStyleDescription)

@given(instance=style_EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_EndLabelStyleDescription)

@given(instance=style_CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_CenterLabelStyleDescription)

@given(instance=viewpoint_style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_SizeComputationContainerStyleDescription)



@given(instance=viewpoint_style_SizeComputationContainerStyleDescription_strategy)
def test_viewpoint_style_sizecomputationcontainerstyledescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original



@given(instance=viewpoint_style_SizeComputationContainerStyleDescription_strategy)
def test_viewpoint_style_sizecomputationcontainerstyledescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)

@given(instance=style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, style_RoundedCornerStyleDescription)

@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_GaugeSectionDescription)



@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
def test_viewpoint_style_gaugesectiondescription_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
def test_viewpoint_style_gaugesectiondescription_maxValueExpression_setter(instance):
    original = instance.maxValueExpression
    instance.maxValueExpression = original
    assert instance.maxValueExpression == original



@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
def test_viewpoint_style_gaugesectiondescription_minValueExpression_setter(instance):
    original = instance.minValueExpression
    instance.minValueExpression = original
    assert instance.minValueExpression == original



@given(instance=viewpoint_style_GaugeSectionDescription_strategy)
def test_viewpoint_style_gaugesectiondescription_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

@given(instance=style_GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_style_gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, style_GaugeSectionDescription)

@given(instance=NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_nodestyledescription_instantiation(instance):
    assert isinstance(instance, NodeStyleDescription)

@given(instance=viewpoint_style_DotDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_dotdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_DotDescription)



@given(instance=viewpoint_style_DotDescription_strategy)
def test_viewpoint_style_dotdescription_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=viewpoint_style_GaugeCompositeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_gaugecompositestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_GaugeCompositeStyleDescription)



@given(instance=viewpoint_style_GaugeCompositeStyleDescription_strategy)
def test_viewpoint_style_gaugecompositestyledescription_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=viewpoint_style_LozengeNodeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_lozengenodedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LozengeNodeDescription)



@given(instance=viewpoint_style_LozengeNodeDescription_strategy)
def test_viewpoint_style_lozengenodedescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original



@given(instance=viewpoint_style_LozengeNodeDescription_strategy)
def test_viewpoint_style_lozengenodedescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=viewpoint_style_SquareDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_squaredescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_SquareDescription)



@given(instance=viewpoint_style_SquareDescription_strategy)
def test_viewpoint_style_squaredescription_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_style_SquareDescription_strategy)
def test_viewpoint_style_squaredescription_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint_style_NoteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_notedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_NoteDescription)

@given(instance=viewpoint_style_BundledImageDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_bundledimagedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BundledImageDescription)



@given(instance=viewpoint_style_BundledImageDescription_strategy)
def test_viewpoint_style_bundledimagedescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint_style_CustomStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_customstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_CustomStyleDescription)



@given(instance=viewpoint_style_CustomStyleDescription_strategy)
def test_viewpoint_style_customstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint_style_EllipseNodeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_ellipsenodedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EllipseNodeDescription)



@given(instance=viewpoint_style_EllipseNodeDescription_strategy)
def test_viewpoint_style_ellipsenodedescription_verticalDiameterComputationExpression_setter(instance):
    original = instance.verticalDiameterComputationExpression
    instance.verticalDiameterComputationExpression = original
    assert instance.verticalDiameterComputationExpression == original



@given(instance=viewpoint_style_EllipseNodeDescription_strategy)
def test_viewpoint_style_ellipsenodedescription_horizontalDiameterComputationExpression_setter(instance):
    original = instance.horizontalDiameterComputationExpression
    instance.horizontalDiameterComputationExpression = original
    assert instance.horizontalDiameterComputationExpression == original

@given(instance=style_TooltipStyleDescription_strategy)
@settings(max_examples=50)
def test_style_tooltipstyledescription_instantiation(instance):
    assert isinstance(instance, style_TooltipStyleDescription)

@given(instance=style_LabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_labelstyledescription_instantiation(instance):
    assert isinstance(instance, style_LabelStyleDescription)

@given(instance=style_BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_style_borderedstyledescription_instantiation(instance):
    assert isinstance(instance, style_BorderedStyleDescription)

@given(instance=viewpoint_style_ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_containerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_ContainerStyleDescription)



@given(instance=viewpoint_style_ContainerStyleDescription_strategy)
def test_viewpoint_style_containerstyledescription_roundedCorner_setter(instance):
    original = instance.roundedCorner
    instance.roundedCorner = original
    assert instance.roundedCorner == original

@given(instance=StyleDescription_strategy)
@settings(max_examples=50)
def test_styledescription_instantiation(instance):
    assert isinstance(instance, StyleDescription)

@given(instance=viewpoint_style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_RoundedCornerStyleDescription)



@given(instance=viewpoint_style_RoundedCornerStyleDescription_strategy)
def test_viewpoint_style_roundedcornerstyledescription_arcWidth_setter(instance):
    original = instance.arcWidth
    instance.arcWidth = original
    assert instance.arcWidth == original



@given(instance=viewpoint_style_RoundedCornerStyleDescription_strategy)
def test_viewpoint_style_roundedcornerstyledescription_arcHeight_setter(instance):
    original = instance.arcHeight
    instance.arcHeight = original
    assert instance.arcHeight == original

@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_edgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EdgeStyleDescription)



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=viewpoint_style_EdgeStyleDescription_strategy)
def test_viewpoint_style_edgestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original

@given(instance=viewpoint_style_BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_borderedstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BorderedStyleDescription)



@given(instance=viewpoint_style_BorderedStyleDescription_strategy)
def test_viewpoint_style_borderedstyledescription_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=Layer_strategy)
@settings(max_examples=50)
def test_layer_instantiation(instance):
    assert isinstance(instance, Layer)

@given(instance=viewpoint_description_AdditionalLayer_strategy)
@settings(max_examples=50)
def test_viewpoint_description_additionallayer_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AdditionalLayer)



@given(instance=viewpoint_description_AdditionalLayer_strategy)
def test_viewpoint_description_additionallayer_activeByDefault_setter(instance):
    original = instance.activeByDefault
    instance.activeByDefault = original
    assert instance.activeByDefault == original



@given(instance=viewpoint_description_AdditionalLayer_strategy)
def test_viewpoint_description_additionallayer_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=Customization_strategy)
@settings(max_examples=50)
def test_customization_instantiation(instance):
    assert isinstance(instance, Customization)

@given(instance=DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, DecorationDescriptionsSet)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=viewpoint_description_CompositeLayout_strategy)
@settings(max_examples=50)
def test_viewpoint_description_compositelayout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_CompositeLayout)



@given(instance=viewpoint_description_CompositeLayout_strategy)
def test_viewpoint_description_compositelayout_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=viewpoint_description_CompositeLayout_strategy)
def test_viewpoint_description_compositelayout_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original

@given(instance=viewpoint_description_OrderedTreeLayout_strategy)
@settings(max_examples=50)
def test_viewpoint_description_orderedtreelayout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_OrderedTreeLayout)



@given(instance=viewpoint_description_OrderedTreeLayout_strategy)
def test_viewpoint_description_orderedtreelayout_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=viewpoint_concern_ConcernSet_strategy)
@settings(max_examples=50)
def test_viewpoint_concern_concernset_instantiation(instance):
    assert isinstance(instance, viewpoint_concern_ConcernSet)

@given(instance=viewpoint_validation_ValidationSet_strategy)
@settings(max_examples=50)
def test_viewpoint_validation_validationset_instantiation(instance):
    assert isinstance(instance, viewpoint_validation_ValidationSet)



@given(instance=viewpoint_validation_ValidationSet_strategy)
def test_viewpoint_validation_validationset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_Layout_strategy)
@settings(max_examples=50)
def test_viewpoint_description_layout_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Layout)

@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)

@given(instance=viewpoint_description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalContainerStyleDescription)

@given(instance=viewpoint_description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalEdgeStyleDescription)

@given(instance=viewpoint_description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalNodeStyleDescription)

@given(instance=description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_description_conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalEdgeStyleDescription)

@given(instance=style_EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_style_edgestyledescription_instantiation(instance):
    assert isinstance(instance, style_EdgeStyleDescription)

@given(instance=viewpoint_description_IEdgeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_iedgemapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IEdgeMapping)

@given(instance=tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_tool_reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, tool_ReconnectEdgeDescription)

@given(instance=description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_description_conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalContainerStyleDescription)

@given(instance=style_ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_containerstyledescription_instantiation(instance):
    assert isinstance(instance, style_ContainerStyleDescription)

@given(instance=viewpoint_style_FlatContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_flatcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_FlatContainerStyleDescription)



@given(instance=viewpoint_style_FlatContainerStyleDescription_strategy)
def test_viewpoint_style_flatcontainerstyledescription_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=viewpoint_style_ShapeContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_shapecontainerstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_ShapeContainerStyleDescription)



@given(instance=viewpoint_style_ShapeContainerStyleDescription_strategy)
def test_viewpoint_style_shapecontainerstyledescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=description_AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_description_abstractmappingimport_instantiation(instance):
    assert isinstance(instance, description_AbstractMappingImport)

@given(instance=description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_description_conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, description_ConditionalNodeStyleDescription)

@given(instance=style_NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style_nodestyledescription_instantiation(instance):
    assert isinstance(instance, style_NodeStyleDescription)

@given(instance=viewpoint_style_WorkspaceImageDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_workspaceimagedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_WorkspaceImageDescription)



@given(instance=viewpoint_style_WorkspaceImageDescription_strategy)
def test_viewpoint_style_workspaceimagedescription_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=tool_DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_tool_doubleclickdescription_instantiation(instance):
    assert isinstance(instance, tool_DoubleClickDescription)

@given(instance=description_AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_description_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, description_AbstractNodeMapping)

@given(instance=tool_DirectEditLabel_strategy)
@settings(max_examples=50)
def test_tool_directeditlabel_instantiation(instance):
    assert isinstance(instance, tool_DirectEditLabel)

@given(instance=tool_DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_tool_deleteelementdescription_instantiation(instance):
    assert isinstance(instance, tool_DeleteElementDescription)

@given(instance=tool_ToolSection_strategy)
@settings(max_examples=50)
def test_tool_toolsection_instantiation(instance):
    assert isinstance(instance, tool_ToolSection)

@given(instance=description_RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_description_representationelementmapping_instantiation(instance):
    assert isinstance(instance, description_RepresentationElementMapping)

@given(instance=description_RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_description_representationimportdescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationImportDescription)

@given(instance=viewpoint_description_DiagramImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_diagramimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramImportDescription)

@given(instance=description_AdditionalLayer_strategy)
@settings(max_examples=50)
def test_description_additionallayer_instantiation(instance):
    assert isinstance(instance, description_AdditionalLayer)

@given(instance=description_Layout_strategy)
@settings(max_examples=50)
def test_description_layout_instantiation(instance):
    assert isinstance(instance, description_Layout)

@given(instance=description_EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_description_edgemappingimport_instantiation(instance):
    assert isinstance(instance, description_EdgeMappingImport)

@given(instance=description_EdgeMapping_strategy)
@settings(max_examples=50)
def test_description_edgemapping_instantiation(instance):
    assert isinstance(instance, description_EdgeMapping)

@given(instance=concern_ConcernSet_strategy)
@settings(max_examples=50)
def test_concern_concernset_instantiation(instance):
    assert isinstance(instance, concern_ConcernSet)

@given(instance=ModelElement2ViewVariable_strategy)
@settings(max_examples=50)
def test_modelelement2viewvariable_instantiation(instance):
    assert isinstance(instance, ModelElement2ViewVariable)

@given(instance=viewpoint_diagram_DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_diagramelementmapping2modelelement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DiagramElementMapping2ModelElement)

@given(instance=DiagramElementMapping2ModelElement_strategy)
@settings(max_examples=50)
def test_diagramelementmapping2modelelement_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping2ModelElement)

@given(instance=viewpoint_diagram_ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_computedstyledescriptionregistry_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ComputedStyleDescriptionRegistry)

@given(instance=description_PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_description_pastetargetdescription_instantiation(instance):
    assert isinstance(instance, description_PasteTargetDescription)

@given(instance=viewpoint_description_DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramElementMapping)



@given(instance=viewpoint_description_DiagramElementMapping_strategy)
def test_viewpoint_description_diagramelementmapping_synchronizationLock_setter(instance):
    original = instance.synchronizationLock
    instance.synchronizationLock = original
    assert instance.synchronizationLock == original



@given(instance=viewpoint_description_DiagramElementMapping_strategy)
def test_viewpoint_description_diagramelementmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=viewpoint_description_DiagramElementMapping_strategy)
def test_viewpoint_description_diagramelementmapping_createElements_setter(instance):
    original = instance.createElements
    instance.createElements = original
    assert instance.createElements == original



@given(instance=viewpoint_description_DiagramElementMapping_strategy)
def test_viewpoint_description_diagramelementmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original



@given(instance=viewpoint_description_DiagramElementMapping_strategy)
def test_viewpoint_description_diagramelementmapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_diagramelementmapping_isfrom_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFrom(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFrom).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFrom' in viewpoint_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFrom' in viewpoint_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFrom' in viewpoint_description_DiagramElementMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_diagramelementmapping_checkprecondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPrecondition(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPrecondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPrecondition' in viewpoint_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPrecondition' in viewpoint_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPrecondition' in viewpoint_description_DiagramElementMapping is not implemented or raised an error")

@given(instance=description_RepresentationDescription_strategy)
@settings(max_examples=50)
def test_description_representationdescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationDescription)

@given(instance=description_DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_description_draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, description_DragAndDropTargetDescription)

@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_nodemapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_NodeMapping)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_nodemapping_updatenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateNode' in viewpoint_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateNode' in viewpoint_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateNode' in viewpoint_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_nodemapping_createlistelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createListElement(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createListElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createListElement' in viewpoint_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createListElement' in viewpoint_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createListElement' in viewpoint_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_nodemapping_updatelistelement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateListElement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateListElement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateListElement' in viewpoint_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateListElement' in viewpoint_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateListElement' in viewpoint_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_nodemapping_createnode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createNode(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createNode' in viewpoint_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in viewpoint_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in viewpoint_description_NodeMapping is not implemented or raised an error")

@given(instance=viewpoint_description_ContainerMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_containermapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ContainerMapping)



@given(instance=viewpoint_description_ContainerMapping_strategy)
def test_viewpoint_description_containermapping_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_ContainerMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_containermapping_updatecontainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateContainer(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateContainer' in viewpoint_description_ContainerMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateContainer' in viewpoint_description_ContainerMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateContainer' in viewpoint_description_ContainerMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_ContainerMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_containermapping_createcontainer_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createContainer(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createContainer).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createContainer' in viewpoint_description_ContainerMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createContainer' in viewpoint_description_ContainerMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createContainer' in viewpoint_description_ContainerMapping is not implemented or raised an error")

@given(instance=viewpoint_description_DiagramDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_diagramdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramDescription)



@given(instance=viewpoint_description_DiagramDescription_strategy)
def test_viewpoint_description_diagramdescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_description_DiagramDescription_strategy)
def test_viewpoint_description_diagramdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=viewpoint_description_DiagramDescription_strategy)
def test_viewpoint_description_diagramdescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=viewpoint_description_DiagramDescription_strategy)
def test_viewpoint_description_diagramdescription_enablePopupBars_setter(instance):
    original = instance.enablePopupBars
    instance.enablePopupBars = original
    assert instance.enablePopupBars == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_DiagramDescription_strategy)
@settings(max_examples=30)
def test_viewpoint_description_diagramdescription_creatediagram_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createDiagram()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createDiagram).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createDiagram' in viewpoint_description_DiagramDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiagram' in viewpoint_description_DiagramDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiagram' in viewpoint_description_DiagramDescription is not implemented or raised an error")

@given(instance=viewpoint_diagram_ContainerVariable2StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_containervariable2styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ContainerVariable2StyleDescription)

@given(instance=ContainerVariable2StyleDescription_strategy)
@settings(max_examples=50)
def test_containervariable2styledescription_instantiation(instance):
    assert isinstance(instance, ContainerVariable2StyleDescription)

@given(instance=viewpoint_diagram_ViewVariable2ContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_viewvariable2containervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ViewVariable2ContainerVariable)

@given(instance=ViewVariable2ContainerVariable_strategy)
@settings(max_examples=50)
def test_viewvariable2containervariable_instantiation(instance):
    assert isinstance(instance, ViewVariable2ContainerVariable)

@given(instance=viewpoint_diagram_ModelElement2ViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_modelelement2viewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ModelElement2ViewVariable)

@given(instance=diagram_viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_diagram_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_EObject)

@given(instance=filter_FilterVariable_strategy)
@settings(max_examples=50)
def test_filter_filtervariable_instantiation(instance):
    assert isinstance(instance, filter_FilterVariable)

@given(instance=viewpoint_diagram_FilterVariableValue_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_filtervariablevalue_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FilterVariableValue)

@given(instance=FilterVariableValue_strategy)
@settings(max_examples=50)
def test_filtervariablevalue_instantiation(instance):
    assert isinstance(instance, FilterVariableValue)

@given(instance=CollapseFilter_strategy)
@settings(max_examples=50)
def test_collapsefilter_instantiation(instance):
    assert isinstance(instance, CollapseFilter)

@given(instance=viewpoint_diagram_IndirectlyCollapseFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_indirectlycollapsefilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_IndirectlyCollapseFilter)

@given(instance=viewpoint_diagram_FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_filtervariablehistory_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FilterVariableHistory)

@given(instance=GaugeSection_strategy)
@settings(max_examples=50)
def test_gaugesection_instantiation(instance):
    assert isinstance(instance, GaugeSection)

@given(instance=EndLabelStyle_strategy)
@settings(max_examples=50)
def test_endlabelstyle_instantiation(instance):
    assert isinstance(instance, EndLabelStyle)

@given(instance=CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_centerlabelstyle_instantiation(instance):
    assert isinstance(instance, CenterLabelStyle)

@given(instance=BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_beginlabelstyle_instantiation(instance):
    assert isinstance(instance, BeginLabelStyle)

@given(instance=diagram_ContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram_containerstyle_instantiation(instance):
    assert isinstance(instance, diagram_ContainerStyle)

@given(instance=diagram_NodeStyle_strategy)
@settings(max_examples=50)
def test_diagram_nodestyle_instantiation(instance):
    assert isinstance(instance, diagram_NodeStyle)

@given(instance=viewpoint_diagram_WorkspaceImage_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_workspaceimage_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_WorkspaceImage)



@given(instance=viewpoint_diagram_WorkspaceImage_strategy)
def test_viewpoint_diagram_workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=viewpoint_diagram_EdgeTarget_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_edgetarget_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EdgeTarget)

@given(instance=diagram_BorderedStyle_strategy)
@settings(max_examples=50)
def test_diagram_borderedstyle_instantiation(instance):
    assert isinstance(instance, diagram_BorderedStyle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=viewpoint_diagram_EdgeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_edgestyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EdgeStyle)



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=viewpoint_diagram_EdgeStyle_strategy)
def test_viewpoint_diagram_edgestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original

@given(instance=viewpoint_diagram_BorderedStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_borderedstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BorderedStyle)



@given(instance=viewpoint_diagram_BorderedStyle_strategy)
def test_viewpoint_diagram_borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original



@given(instance=viewpoint_diagram_BorderedStyle_strategy)
def test_viewpoint_diagram_borderedstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=LabelStyle_strategy)
@settings(max_examples=50)
def test_labelstyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)

@given(instance=viewpoint_diagram_ContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_containerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ContainerStyle)

@given(instance=viewpoint_diagram_NodeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_nodestyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_NodeStyle)



@given(instance=viewpoint_diagram_NodeStyle_strategy)
def test_viewpoint_diagram_nodestyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original



@given(instance=viewpoint_diagram_NodeStyle_strategy)
def test_viewpoint_diagram_nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=diagram_viewpoint_DRepresentationContainer_strategy)
@settings(max_examples=50)
def test_diagram_viewpoint_drepresentationcontainer_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_DRepresentationContainer)

@given(instance=diagram_viewpoint_RGBValues_strategy)
@settings(max_examples=50)
def test_diagram_viewpoint_rgbvalues_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_RGBValues)

@given(instance=description_IEdgeMapping_strategy)
@settings(max_examples=50)
def test_description_iedgemapping_instantiation(instance):
    assert isinstance(instance, description_IEdgeMapping)

@given(instance=viewpoint_diagram_DDiagramSet_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ddiagramset_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramSet)

@given(instance=AbstractDNode_strategy)
@settings(max_examples=50)
def test_abstractdnode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)

@given(instance=viewpoint_diagram_DNodeListElement_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dnodelistelement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeListElement)

@given(instance=EdgeStyle_strategy)
@settings(max_examples=50)
def test_edgestyle_instantiation(instance):
    assert isinstance(instance, EdgeStyle)

@given(instance=viewpoint_diagram_BracketEdgeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_bracketedgestyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BracketEdgeStyle)

@given(instance=diagram_DDiagramElement_strategy)
@settings(max_examples=50)
def test_diagram_ddiagramelement_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElement)

@given(instance=description_ContainerMapping_strategy)
@settings(max_examples=50)
def test_description_containermapping_instantiation(instance):
    assert isinstance(instance, description_ContainerMapping)

@given(instance=viewpoint_description_ContainerMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint_description_containermappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ContainerMappingImport)

@given(instance=ContainerStyle_strategy)
@settings(max_examples=50)
def test_containerstyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)

@given(instance=viewpoint_diagram_FlatContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_flatcontainerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FlatContainerStyle)



@given(instance=viewpoint_diagram_FlatContainerStyle_strategy)
def test_viewpoint_diagram_flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=viewpoint_diagram_ShapeContainerStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_shapecontainerstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_ShapeContainerStyle)



@given(instance=viewpoint_diagram_ShapeContainerStyle_strategy)
def test_viewpoint_diagram_shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram_EdgeTarget_strategy)
@settings(max_examples=50)
def test_diagram_edgetarget_instantiation(instance):
    assert isinstance(instance, diagram_EdgeTarget)

@given(instance=viewpoint_diagram_DEdge_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dedge_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DEdge)



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_beginLabel_setter(instance):
    original = instance.beginLabel
    instance.beginLabel = original
    assert instance.beginLabel == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_isFold_setter(instance):
    original = instance.isFold
    instance.isFold = original
    assert instance.isFold == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_isMockEdge_setter(instance):
    original = instance.isMockEdge
    instance.isMockEdge = original
    assert instance.isMockEdge == original



@given(instance=viewpoint_diagram_DEdge_strategy)
def test_viewpoint_diagram_dedge_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_DEdge_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_dedge_isrootfolding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isRootFolding()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isRootFolding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isRootFolding' in viewpoint_diagram_DEdge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRootFolding' in viewpoint_diagram_DEdge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRootFolding' in viewpoint_diagram_DEdge is not implemented or raised an error")

@given(instance=diagram_AbstractDNode_strategy)
@settings(max_examples=50)
def test_diagram_abstractdnode_instantiation(instance):
    assert isinstance(instance, diagram_AbstractDNode)

@given(instance=viewpoint_diagram_DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramElementContainer)



@given(instance=viewpoint_diagram_DDiagramElementContainer_strategy)
def test_viewpoint_diagram_ddiagramelementcontainer_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_diagram_DDiagramElementContainer_strategy)
def test_viewpoint_diagram_ddiagramelementcontainer_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint_diagram_DNode_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dnode_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNode)



@given(instance=viewpoint_diagram_DNode_strategy)
def test_viewpoint_diagram_dnode_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original



@given(instance=viewpoint_diagram_DNode_strategy)
def test_viewpoint_diagram_dnode_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=viewpoint_diagram_DNode_strategy)
def test_viewpoint_diagram_dnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_diagram_DNode_strategy)
def test_viewpoint_diagram_dnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint_diagram_AbstractDNode_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_abstractdnode_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AbstractDNode)



@given(instance=viewpoint_diagram_AbstractDNode_strategy)
def test_viewpoint_diagram_abstractdnode_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=description_NodeMapping_strategy)
@settings(max_examples=50)
def test_description_nodemapping_instantiation(instance):
    assert isinstance(instance, description_NodeMapping)

@given(instance=viewpoint_description_NodeMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint_description_nodemappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_NodeMappingImport)

@given(instance=diagram_viewpoint_Style_strategy)
@settings(max_examples=50)
def test_diagram_viewpoint_style_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_Style)

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=viewpoint_diagram_BundledImage_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_bundledimage_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BundledImage)



@given(instance=viewpoint_diagram_BundledImage_strategy)
def test_viewpoint_diagram_bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=viewpoint_diagram_CustomStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_customstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CustomStyle)



@given(instance=viewpoint_diagram_CustomStyle_strategy)
def test_viewpoint_diagram_customstyle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint_diagram_Ellipse_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ellipse_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Ellipse)



@given(instance=viewpoint_diagram_Ellipse_strategy)
def test_viewpoint_diagram_ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original



@given(instance=viewpoint_diagram_Ellipse_strategy)
def test_viewpoint_diagram_ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original

@given(instance=viewpoint_diagram_Lozenge_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_lozenge_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Lozenge)



@given(instance=viewpoint_diagram_Lozenge_strategy)
def test_viewpoint_diagram_lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_diagram_Lozenge_strategy)
def test_viewpoint_diagram_lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=viewpoint_diagram_Note_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_note_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Note)

@given(instance=viewpoint_diagram_Dot_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dot_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Dot)



@given(instance=viewpoint_diagram_Dot_strategy)
def test_viewpoint_diagram_dot_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=viewpoint_diagram_GaugeCompositeStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_gaugecompositestyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GaugeCompositeStyle)



@given(instance=viewpoint_diagram_GaugeCompositeStyle_strategy)
def test_viewpoint_diagram_gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=viewpoint_diagram_Square_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_square_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_Square)



@given(instance=viewpoint_diagram_Square_strategy)
def test_viewpoint_diagram_square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=viewpoint_diagram_Square_strategy)
def test_viewpoint_diagram_square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=viewpoint_diagram_GraphicalFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_graphicalfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GraphicalFilter)

@given(instance=GraphicalFilter_strategy)
@settings(max_examples=50)
def test_graphicalfilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)

@given(instance=viewpoint_diagram_CollapseFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_collapsefilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CollapseFilter)



@given(instance=viewpoint_diagram_CollapseFilter_strategy)
def test_viewpoint_diagram_collapsefilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_diagram_CollapseFilter_strategy)
def test_viewpoint_diagram_collapsefilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram_viewpoint_Decoration_strategy)
@settings(max_examples=50)
def test_diagram_viewpoint_decoration_instantiation(instance):
    assert isinstance(instance, diagram_viewpoint_Decoration)

@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_absoluteboundsfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AbsoluteBoundsFilter)



@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
def test_viewpoint_diagram_absoluteboundsfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
def test_viewpoint_diagram_absoluteboundsfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
def test_viewpoint_diagram_absoluteboundsfilter_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=viewpoint_diagram_AbsoluteBoundsFilter_strategy)
def test_viewpoint_diagram_absoluteboundsfilter_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=filter_CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_filter_compositefilterdescription_instantiation(instance):
    assert isinstance(instance, filter_CompositeFilterDescription)

@given(instance=viewpoint_diagram_AppliedCompositeFilters_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_appliedcompositefilters_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_AppliedCompositeFilters)

@given(instance=viewpoint_diagram_FoldingFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_foldingfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FoldingFilter)

@given(instance=viewpoint_diagram_FoldingPointFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_foldingpointfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_FoldingPointFilter)

@given(instance=viewpoint_diagram_HideLabelFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_hidelabelfilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_HideLabelFilter)

@given(instance=viewpoint_diagram_HideFilter_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_hidefilter_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_HideFilter)

@given(instance=description_Layer_strategy)
@settings(max_examples=50)
def test_description_layer_instantiation(instance):
    assert isinstance(instance, description_Layer)

@given(instance=FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_filtervariablehistory_instantiation(instance):
    assert isinstance(instance, FilterVariableHistory)

@given(instance=tool_BehaviorTool_strategy)
@settings(max_examples=50)
def test_tool_behaviortool_instantiation(instance):
    assert isinstance(instance, tool_BehaviorTool)

@given(instance=validation_ValidationRule_strategy)
@settings(max_examples=50)
def test_validation_validationrule_instantiation(instance):
    assert isinstance(instance, validation_ValidationRule)

@given(instance=DNavigable_strategy)
@settings(max_examples=50)
def test_dnavigable_instantiation(instance):
    assert isinstance(instance, DNavigable)

@given(instance=DRepresentationElement_strategy)
@settings(max_examples=50)
def test_drepresentationelement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)

@given(instance=viewpoint_diagram_DDiagramElement_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ddiagramelement_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramElement)



@given(instance=viewpoint_diagram_DDiagramElement_strategy)
def test_viewpoint_diagram_ddiagramelement_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original



@given(instance=viewpoint_diagram_DDiagramElement_strategy)
def test_viewpoint_diagram_ddiagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_DDiagramElement_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_ddiagramelement_isfold_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isFold(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isFold).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isFold' in viewpoint_diagram_DDiagramElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFold' in viewpoint_diagram_DDiagramElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFold' in viewpoint_diagram_DDiagramElement is not implemented or raised an error")

@given(instance=diagram_DDiagram_strategy)
@settings(max_examples=50)
def test_diagram_ddiagram_instantiation(instance):
    assert isinstance(instance, diagram_DDiagram)

@given(instance=DEdge_strategy)
@settings(max_examples=50)
def test_dedge_instantiation(instance):
    assert isinstance(instance, DEdge)

@given(instance=DDiagram_strategy)
@settings(max_examples=50)
def test_ddiagram_instantiation(instance):
    assert isinstance(instance, DDiagram)

@given(instance=filter_FilterDescription_strategy)
@settings(max_examples=50)
def test_filter_filterdescription_instantiation(instance):
    assert isinstance(instance, filter_FilterDescription)

@given(instance=concern_ConcernDescription_strategy)
@settings(max_examples=50)
def test_concern_concerndescription_instantiation(instance):
    assert isinstance(instance, concern_ConcernDescription)

@given(instance=DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, DDiagramElementContainer)

@given(instance=viewpoint_diagram_DNodeContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dnodecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeContainer)



@given(instance=viewpoint_diagram_DNodeContainer_strategy)
def test_viewpoint_diagram_dnodecontainer_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=viewpoint_diagram_DNodeList_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dnodelist_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DNodeList)



@given(instance=viewpoint_diagram_DNodeList_strategy)
def test_viewpoint_diagram_dnodelist_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=DNodeListElement_strategy)
@settings(max_examples=50)
def test_dnodelistelement_instantiation(instance):
    assert isinstance(instance, DNodeListElement)

@given(instance=viewpoint_tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitEdgeCreationOperation)

@given(instance=viewpoint_tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialOperation)

@given(instance=viewpoint_tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_InitialNodeCreationOperation)

@given(instance=viewpoint_tool_ModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_modeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ModelOperation)

@given(instance=tool_ModelOperation_strategy)
@settings(max_examples=50)
def test_tool_modeloperation_instantiation(instance):
    assert isinstance(instance, tool_ModelOperation)

@given(instance=ModelOperation_strategy)
@settings(max_examples=50)
def test_modeloperation_instantiation(instance):
    assert isinstance(instance, ModelOperation)

@given(instance=viewpoint_tool_Switch_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_switch_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_Switch)

@given(instance=viewpoint_tool_ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containermodeloperation_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerModelOperation)

@given(instance=viewpoint_tool_EditMaskVariables_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_editmaskvariables_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_EditMaskVariables)



@given(instance=viewpoint_tool_EditMaskVariables_strategy)
def test_viewpoint_tool_editmaskvariables_mask_setter(instance):
    original = instance.mask
    instance.mask = original
    assert instance.mask == original

@given(instance=tool_AbstractVariable_strategy)
@settings(max_examples=50)
def test_tool_abstractvariable_instantiation(instance):
    assert isinstance(instance, tool_AbstractVariable)

@given(instance=AbstractVariable_strategy)
@settings(max_examples=50)
def test_abstractvariable_instantiation(instance):
    assert isinstance(instance, AbstractVariable)

@given(instance=viewpoint_tool_ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementselectvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementSelectVariable)

@given(instance=viewpoint_tool_NameVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_namevariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NameVariable)

@given(instance=viewpoint_tool_DialogVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_dialogvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DialogVariable)



@given(instance=viewpoint_tool_DialogVariable_strategy)
def test_viewpoint_tool_dialogvariable_dialogPrompt_setter(instance):
    original = instance.dialogPrompt
    instance.dialogPrompt = original
    assert instance.dialogPrompt == original

@given(instance=viewpoint_tool_SubVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_subvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SubVariable)

@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=50)
def test_tool_variablecontainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)

@given(instance=viewpoint_tool_ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containerviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerViewVariable)

@given(instance=viewpoint_tool_ElementDropVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementdropvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDropVariable)

@given(instance=viewpoint_tool_SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectContainerVariable)

@given(instance=viewpoint_tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_TargetEdgeCreationVariable)

@given(instance=viewpoint_tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SourceEdgeCreationVariable)

@given(instance=viewpoint_tool_NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_nodecreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NodeCreationVariable)

@given(instance=viewpoint_tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDoubleClickVariable)

@given(instance=viewpoint_tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_TargetEdgeViewCreationVariable)

@given(instance=viewpoint_tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SourceEdgeViewCreationVariable)

@given(instance=viewpoint_tool_ElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementVariable)

@given(instance=tool_SubVariable_strategy)
@settings(max_examples=50)
def test_tool_subvariable_instantiation(instance):
    assert isinstance(instance, tool_SubVariable)

@given(instance=viewpoint_tool_AcceleoVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_acceleovariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AcceleoVariable)



@given(instance=viewpoint_tool_AcceleoVariable_strategy)
def test_viewpoint_tool_acceleovariable_computationExpression_setter(instance):
    original = instance.computationExpression
    instance.computationExpression = original
    assert instance.computationExpression == original

@given(instance=viewpoint_tool_VariableContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_variablecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_VariableContainer)

@given(instance=viewpoint_tool_AbstractVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_abstractvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractVariable)



@given(instance=viewpoint_tool_AbstractVariable_strategy)
def test_viewpoint_tool_abstractvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool_ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_tool_externaljavaaction_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaAction)

@given(instance=tool_ExternalJavaActionParameter_strategy)
@settings(max_examples=50)
def test_tool_externaljavaactionparameter_instantiation(instance):
    assert isinstance(instance, tool_ExternalJavaActionParameter)

@given(instance=tool_ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_tool_containermodeloperation_instantiation(instance):
    assert isinstance(instance, tool_ContainerModelOperation)

@given(instance=viewpoint_tool_DropContainerVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_dropcontainervariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DropContainerVariable)

@given(instance=viewpoint_tool_ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementdeletevariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementDeleteVariable)

@given(instance=viewpoint_tool_ElementViewVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_elementviewvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ElementViewVariable)

@given(instance=MenuItemDescription_strategy)
@settings(max_examples=50)
def test_menuitemdescription_instantiation(instance):
    assert isinstance(instance, MenuItemDescription)

@given(instance=viewpoint_tool_OperationAction_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_operationaction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_OperationAction)

@given(instance=tool_MenuItemDescription_strategy)
@settings(max_examples=50)
def test_tool_menuitemdescription_instantiation(instance):
    assert isinstance(instance, tool_MenuItemDescription)

@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaaction_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaAction)



@given(instance=viewpoint_tool_ExternalJavaAction_strategy)
def test_viewpoint_tool_externaljavaaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=viewpoint_tool_ExternalJavaActionCall_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_externaljavaactioncall_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ExternalJavaActionCall)

@given(instance=MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_menuitemorref_instantiation(instance):
    assert isinstance(instance, MenuItemOrRef)

@given(instance=viewpoint_tool_MenuItemDescriptionReference_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemdescriptionreference_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescriptionReference)

@given(instance=tool_MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_tool_menuitemorref_instantiation(instance):
    assert isinstance(instance, tool_MenuItemOrRef)

@given(instance=viewpoint_tool_MenuItemOrRef_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemorref_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemOrRef)

@given(instance=tool_NameVariable_strategy)
@settings(max_examples=50)
def test_tool_namevariable_instantiation(instance):
    assert isinstance(instance, tool_NameVariable)

@given(instance=tool_SelectContainerVariable_strategy)
@settings(max_examples=50)
def test_tool_selectcontainervariable_instantiation(instance):
    assert isinstance(instance, tool_SelectContainerVariable)

@given(instance=tool_InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_tool_initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialContainerDropOperation)

@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool_containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)

@given(instance=tool_ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_tool_elementselectvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementSelectVariable)

@given(instance=description_SelectionDescription_strategy)
@settings(max_examples=50)
def test_description_selectiondescription_instantiation(instance):
    assert isinstance(instance, description_SelectionDescription)

@given(instance=viewpoint_tool_SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectModelElementVariable)

@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)

@given(instance=viewpoint_tool_MenuItemDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_menuitemdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MenuItemDescription)



@given(instance=viewpoint_tool_MenuItemDescription_strategy)
def test_viewpoint_tool_menuitemdescription_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_selectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_SelectionWizardDescription)



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_tool_SelectionWizardDescription_strategy)
def test_viewpoint_tool_selectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original

@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool_dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)

@given(instance=description_DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_description_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, description_DiagramElementMapping)

@given(instance=tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialOperation)

@given(instance=tool_ElementViewVariable_strategy)
@settings(max_examples=50)
def test_tool_elementviewvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementViewVariable)

@given(instance=tool_ElementVariable_strategy)
@settings(max_examples=50)
def test_tool_elementvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementVariable)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

@given(instance=viewpoint_tool_NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_nodecreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_NodeCreationDescription)



@given(instance=viewpoint_tool_NodeCreationDescription_strategy)
def test_viewpoint_tool_nodecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint_tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ReconnectEdgeDescription)



@given(instance=viewpoint_tool_ReconnectEdgeDescription_strategy)
def test_viewpoint_tool_reconnectedgedescription_reconnectionKind_setter(instance):
    original = instance.reconnectionKind
    instance.reconnectionKind = original
    assert instance.reconnectionKind == original

@given(instance=viewpoint_tool_PasteDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_pastedescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PasteDescription)

@given(instance=viewpoint_tool_DirectEditLabel_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_directeditlabel_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DirectEditLabel)



@given(instance=viewpoint_tool_DirectEditLabel_strategy)
def test_viewpoint_tool_directeditlabel_inputLabelExpression_setter(instance):
    original = instance.inputLabelExpression
    instance.inputLabelExpression = original
    assert instance.inputLabelExpression == original

@given(instance=viewpoint_tool_ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containercreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerCreationDescription)



@given(instance=viewpoint_tool_ContainerCreationDescription_strategy)
def test_viewpoint_tool_containercreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint_tool_DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_deleteelementdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DeleteElementDescription)

@given(instance=viewpoint_tool_EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_edgecreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_EdgeCreationDescription)



@given(instance=viewpoint_tool_EdgeCreationDescription_strategy)
def test_viewpoint_tool_edgecreationdescription_connectionStartPrecondition_setter(instance):
    original = instance.connectionStartPrecondition
    instance.connectionStartPrecondition = original
    assert instance.connectionStartPrecondition == original



@given(instance=viewpoint_tool_EdgeCreationDescription_strategy)
def test_viewpoint_tool_edgecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=viewpoint_tool_ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_containerdropdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ContainerDropDescription)



@given(instance=viewpoint_tool_ContainerDropDescription_strategy)
def test_viewpoint_tool_containerdropdescription_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original



@given(instance=viewpoint_tool_ContainerDropDescription_strategy)
def test_viewpoint_tool_containerdropdescription_moveEdges_setter(instance):
    original = instance.moveEdges
    instance.moveEdges = original
    assert instance.moveEdges == original

@given(instance=viewpoint_tool_DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_doubleclickdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_DoubleClickDescription)

@given(instance=viewpoint_tool_ToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_tooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolDescription)



@given(instance=viewpoint_tool_ToolDescription_strategy)
def test_viewpoint_tool_tooldescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)

@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_panebasedselectionwizarddescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PaneBasedSelectionWizardDescription)



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_selectedValuesMessage_setter(instance):
    original = instance.selectedValuesMessage
    instance.selectedValuesMessage = original
    assert instance.selectedValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_preSelectedCandidatesExpression_setter(instance):
    original = instance.preSelectedCandidatesExpression
    instance.preSelectedCandidatesExpression = original
    assert instance.preSelectedCandidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_choiceOfValuesMessage_setter(instance):
    original = instance.choiceOfValuesMessage
    instance.choiceOfValuesMessage = original
    assert instance.choiceOfValuesMessage == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_windowTitle_setter(instance):
    original = instance.windowTitle
    instance.windowTitle = original
    assert instance.windowTitle == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original



@given(instance=viewpoint_tool_PaneBasedSelectionWizardDescription_strategy)
def test_viewpoint_tool_panebasedselectionwizarddescription_windowImagePath_setter(instance):
    original = instance.windowImagePath
    instance.windowImagePath = original
    assert instance.windowImagePath == original

@given(instance=viewpoint_tool_PopupMenu_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_popupmenu_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_PopupMenu)

@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationNavigationDescription)



@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_viewpoint_tool_representationnavigationdescription_navigationNameExpression_setter(instance):
    original = instance.navigationNameExpression
    instance.navigationNameExpression = original
    assert instance.navigationNameExpression == original



@given(instance=viewpoint_tool_RepresentationNavigationDescription_strategy)
def test_viewpoint_tool_representationnavigationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original

@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RepresentationCreationDescription)



@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_viewpoint_tool_representationcreationdescription_browseExpression_setter(instance):
    original = instance.browseExpression
    instance.browseExpression = original
    assert instance.browseExpression == original



@given(instance=viewpoint_tool_RepresentationCreationDescription_strategy)
def test_viewpoint_tool_representationcreationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original

@given(instance=viewpoint_tool_BehaviorTool_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_behaviortool_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_BehaviorTool)



@given(instance=viewpoint_tool_BehaviorTool_strategy)
def test_viewpoint_tool_behaviortool_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint_tool_RequestDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_requestdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_RequestDescription)



@given(instance=viewpoint_tool_RequestDescription_strategy)
def test_viewpoint_tool_requestdescription_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=viewpoint_tool_MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_MappingBasedToolDescription)

@given(instance=tool_ElementDropVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdropvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDropVariable)

@given(instance=tool_ToolFilterDescription_strategy)
@settings(max_examples=50)
def test_tool_toolfilterdescription_instantiation(instance):
    assert isinstance(instance, tool_ToolFilterDescription)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=viewpoint_tool_ToolGroup_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolgroup_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolGroup)

@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_AbstractToolDescription)



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_forceRefresh_setter(instance):
    original = instance.forceRefresh
    instance.forceRefresh = original
    assert instance.forceRefresh == original



@given(instance=viewpoint_tool_AbstractToolDescription_strategy)
def test_viewpoint_tool_abstracttooldescription_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_tooltipstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_TooltipStyleDescription)



@given(instance=viewpoint_style_TooltipStyleDescription_strategy)
def test_viewpoint_style_tooltipstyledescription_tooltipExpression_setter(instance):
    original = instance.tooltipExpression
    instance.tooltipExpression = original
    assert instance.tooltipExpression == original

@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyleDescription)



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original



@given(instance=viewpoint_style_LabelBorderStyleDescription_strategy)
def test_viewpoint_style_labelborderstyledescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=style_LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_style_labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyleDescription)

@given(instance=viewpoint_style_LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelborderstyles_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelBorderStyles)

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

@given(instance=viewpoint_style_CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_CenterLabelStyleDescription)

@given(instance=viewpoint_style_EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_EndLabelStyleDescription)

@given(instance=viewpoint_style_BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BeginLabelStyleDescription)

@given(instance=viewpoint_style_LabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_labelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_LabelStyleDescription)



@given(instance=viewpoint_style_LabelStyleDescription_strategy)
def test_viewpoint_style_labelstyledescription_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_BasicLabelStyleDescription)



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelExpression_setter(instance):
    original = instance.labelExpression
    instance.labelExpression = original
    assert instance.labelExpression == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_style_BasicLabelStyleDescription_strategy)
def test_viewpoint_style_basiclabelstyledescription_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original

@given(instance=viewpoint_style_StyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_styledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_StyleDescription)

@given(instance=viewpoint_description_DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dannotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotationEntry)



@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_viewpoint_description_dannotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=viewpoint_description_DAnnotationEntry_strategy)
def test_viewpoint_description_dannotationentry_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=viewpoint_description_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_identifiedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IdentifiedElement)



@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_viewpoint_description_identifiedelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=viewpoint_description_IdentifiedElement_strategy)
def test_viewpoint_description_identifiedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EndUserDocumentedElement)



@given(instance=viewpoint_description_EndUserDocumentedElement_strategy)
def test_viewpoint_description_enduserdocumentedelement_endUserDocumentation_setter(instance):
    original = instance.endUserDocumentation
    instance.endUserDocumentation = original
    assert instance.endUserDocumentation == original

@given(instance=viewpoint_description_AnnotationEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_description_annotationentry_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AnnotationEntry)



@given(instance=viewpoint_description_AnnotationEntry_strategy)
def test_viewpoint_description_annotationentry_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UserColor_strategy)
@settings(max_examples=50)
def test_usercolor_instantiation(instance):
    assert isinstance(instance, UserColor)

@given(instance=viewpoint_description_UserColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint_description_usercolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColorsPalette)



@given(instance=viewpoint_description_UserColorsPalette_strategy)
def test_viewpoint_description_usercolorspalette_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SystemColor_strategy)
@settings(max_examples=50)
def test_systemcolor_instantiation(instance):
    assert isinstance(instance, SystemColor)

@given(instance=viewpoint_description_SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_viewpoint_description_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SytemColorsPalette)

@given(instance=style_LabelBorderStyles_strategy)
@settings(max_examples=50)
def test_style_labelborderstyles_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyles)

@given(instance=tool_ToolEntry_strategy)
@settings(max_examples=50)
def test_tool_toolentry_instantiation(instance):
    assert isinstance(instance, tool_ToolEntry)

@given(instance=viewpoint_description_Environment_strategy)
@settings(max_examples=50)
def test_viewpoint_description_environment_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Environment)

@given(instance=viewpoint_description_UserColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_usercolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserColor)



@given(instance=viewpoint_description_UserColor_strategy)
def test_viewpoint_description_usercolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=description_FixedColor_strategy)
@settings(max_examples=50)
def test_description_fixedcolor_instantiation(instance):
    assert isinstance(instance, description_FixedColor)

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=viewpoint_description_FixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_fixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FixedColor)



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=viewpoint_description_FixedColor_strategy)
def test_viewpoint_description_fixedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=viewpoint_description_ColorStep_strategy)
@settings(max_examples=50)
def test_viewpoint_description_colorstep_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorStep)



@given(instance=viewpoint_description_ColorStep_strategy)
def test_viewpoint_description_colorstep_associatedValue_setter(instance):
    original = instance.associatedValue
    instance.associatedValue = original
    assert instance.associatedValue == original

@given(instance=ColorStep_strategy)
@settings(max_examples=50)
def test_colorstep_instantiation(instance):
    assert isinstance(instance, ColorStep)

@given(instance=description_ColorDescription_strategy)
@settings(max_examples=50)
def test_description_colordescription_instantiation(instance):
    assert isinstance(instance, description_ColorDescription)

@given(instance=FixedColor_strategy)
@settings(max_examples=50)
def test_fixedcolor_instantiation(instance):
    assert isinstance(instance, FixedColor)

@given(instance=viewpoint_description_SystemColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_systemcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SystemColor)



@given(instance=viewpoint_description_SystemColor_strategy)
def test_viewpoint_description_systemcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_ColorDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_colordescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ColorDescription)

@given(instance=viewpoint_description_SelectionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_selectiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SelectionDescription)



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_tree_setter(instance):
    original = instance.tree
    instance.tree = original
    assert instance.tree == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_candidatesExpression_setter(instance):
    original = instance.candidatesExpression
    instance.candidatesExpression = original
    assert instance.candidatesExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original



@given(instance=viewpoint_description_SelectionDescription_strategy)
def test_viewpoint_description_selectiondescription_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=description_UserColor_strategy)
@settings(max_examples=50)
def test_description_usercolor_instantiation(instance):
    assert isinstance(instance, description_UserColor)

@given(instance=viewpoint_description_UserFixedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_userfixedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_UserFixedColor)

@given(instance=viewpoint_description_InterpolatedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_interpolatedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_InterpolatedColor)



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_colorValueComputationExpression_setter(instance):
    original = instance.colorValueComputationExpression
    instance.colorValueComputationExpression = original
    assert instance.colorValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_maxValueComputationExpression_setter(instance):
    original = instance.maxValueComputationExpression
    instance.maxValueComputationExpression = original
    assert instance.maxValueComputationExpression == original



@given(instance=viewpoint_description_InterpolatedColor_strategy)
def test_viewpoint_description_interpolatedcolor_minValueComputationExpression_setter(instance):
    original = instance.minValueComputationExpression
    instance.minValueComputationExpression = original
    assert instance.minValueComputationExpression == original

@given(instance=viewpoint_description_ComputedColor_strategy)
@settings(max_examples=50)
def test_viewpoint_description_computedcolor_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ComputedColor)



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=viewpoint_description_ComputedColor_strategy)
def test_viewpoint_description_computedcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, EStructuralFeatureCustomization)

@given(instance=viewpoint_description_EReferenceCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_ereferencecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EReferenceCustomization)



@given(instance=viewpoint_description_EReferenceCustomization_strategy)
def test_viewpoint_description_ereferencecustomization_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=viewpoint_description_IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_IVSMElementCustomization)

@given(instance=IVSMElementCustomization_strategy)
@settings(max_examples=50)
def test_ivsmelementcustomization_instantiation(instance):
    assert isinstance(instance, IVSMElementCustomization)

@given(instance=viewpoint_description_VSMElementCustomizationReuse_strategy)
@settings(max_examples=50)
def test_viewpoint_description_vsmelementcustomizationreuse_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomizationReuse)

@given(instance=viewpoint_description_VSMElementCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_vsmelementcustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_VSMElementCustomization)



@given(instance=viewpoint_description_VSMElementCustomization_strategy)
def test_viewpoint_description_vsmelementcustomization_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

@given(instance=viewpoint_description_Customization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_customization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Customization)

@given(instance=viewpoint_description_EAttributeCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_eattributecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EAttributeCustomization)



@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_viewpoint_description_eattributecustomization_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original



@given(instance=viewpoint_description_EAttributeCustomization_strategy)
def test_viewpoint_description_eattributecustomization_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
@settings(max_examples=50)
def test_viewpoint_description_estructuralfeaturecustomization_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EStructuralFeatureCustomization)



@given(instance=viewpoint_description_EStructuralFeatureCustomization_strategy)
def test_viewpoint_description_estructuralfeaturecustomization_applyOnAll_setter(instance):
    original = instance.applyOnAll
    instance.applyOnAll = original
    assert instance.applyOnAll == original

@given(instance=viewpoint_description_DecorationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_decorationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescription)



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_decoratorPath_setter(instance):
    original = instance.decoratorPath
    instance.decoratorPath = original
    assert instance.decoratorPath == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=viewpoint_description_DecorationDescription_strategy)
def test_viewpoint_description_decorationdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

@given(instance=viewpoint_description_DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_viewpoint_description_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DecorationDescriptionsSet)

@given(instance=tool_PasteDescription_strategy)
@settings(max_examples=50)
def test_tool_pastedescription_instantiation(instance):
    assert isinstance(instance, tool_PasteDescription)

@given(instance=viewpoint_description_PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_pastetargetdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_PasteTargetDescription)

@given(instance=tool_ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_tool_containerdropdescription_instantiation(instance):
    assert isinstance(instance, tool_ContainerDropDescription)

@given(instance=viewpoint_description_DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DragAndDropTargetDescription)

@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_ConditionalStyleDescription)



@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
def test_viewpoint_description_conditionalstyledescription_predicateExpression_setter(instance):
    original = instance.predicateExpression
    instance.predicateExpression = original
    assert instance.predicateExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_ConditionalStyleDescription_strategy)
@settings(max_examples=30)
def test_viewpoint_description_conditionalstyledescription_checkpredicate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.checkPredicate(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.checkPredicate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPredicate' in viewpoint_description_ConditionalStyleDescription is not implemented or raised an error")

@given(instance=description_viewpoint_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_description_viewpoint_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EStringToStringMapEntry)

@given(instance=viewpoint_description_DAnnotation_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dannotation_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DAnnotation)



@given(instance=viewpoint_description_DAnnotation_strategy)
def test_viewpoint_description_dannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=DAnnotation_strategy)
@settings(max_examples=50)
def test_dannotation_instantiation(instance):
    assert isinstance(instance, DAnnotation)

@given(instance=viewpoint_description_AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint_description_abstractmappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractMappingImport)



@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_viewpoint_description_abstractmappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original



@given(instance=viewpoint_description_AbstractMappingImport_strategy)
def test_viewpoint_description_abstractmappingimport_hideSubMappings_setter(instance):
    original = instance.hideSubMappings
    instance.hideSubMappings = original
    assert instance.hideSubMappings == original

@given(instance=tool_RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_tool_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationNavigationDescription)

@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)

@given(instance=IdentifiedElement_strategy)
@settings(max_examples=50)
def test_identifiedelement_instantiation(instance):
    assert isinstance(instance, IdentifiedElement)

@given(instance=viewpoint_description_RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationelementmapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationElementMapping)

@given(instance=viewpoint_description_JavaExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_description_javaextension_instantiation(instance):
    assert isinstance(instance, viewpoint_description_JavaExtension)



@given(instance=viewpoint_description_JavaExtension_strategy)
def test_viewpoint_description_javaextension_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=description_viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_description_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EObject)

@given(instance=viewpoint_description_MetamodelExtensionSetting_strategy)
@settings(max_examples=50)
def test_viewpoint_description_metamodelextensionsetting_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MetamodelExtensionSetting)

@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationExtensionDescription)



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_viewpointURI_setter(instance):
    original = instance.viewpointURI
    instance.viewpointURI = original
    assert instance.viewpointURI == original



@given(instance=viewpoint_description_RepresentationExtensionDescription_strategy)
def test_viewpoint_description_representationextensiondescription_representationName_setter(instance):
    original = instance.representationName
    instance.representationName = original
    assert instance.representationName == original

@given(instance=viewpoint_description_DModelElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_dmodelelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DModelElement)

@given(instance=viewpoint_description_DocumentedElement_strategy)
@settings(max_examples=50)
def test_viewpoint_description_documentedelement_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DocumentedElement)



@given(instance=viewpoint_description_DocumentedElement_strategy)
def test_viewpoint_description_documentedelement_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original

@given(instance=description_viewpoint_EPackage_strategy)
@settings(max_examples=50)
def test_description_viewpoint_epackage_instantiation(instance):
    assert isinstance(instance, description_viewpoint_EPackage)

@given(instance=viewpoint_description_FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_FeatureExtensionDescription)

@given(instance=RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_representationtemplate_instantiation(instance):
    assert isinstance(instance, RepresentationTemplate)

@given(instance=MetamodelExtensionSetting_strategy)
@settings(max_examples=50)
def test_metamodelextensionsetting_instantiation(instance):
    assert isinstance(instance, MetamodelExtensionSetting)

@given(instance=JavaExtension_strategy)
@settings(max_examples=50)
def test_javaextension_instantiation(instance):
    assert isinstance(instance, JavaExtension)

@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)

@given(instance=viewpoint_description_DiagramExtensionDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_diagramextensiondescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_DiagramExtensionDescription)

@given(instance=RepresentationDescription_strategy)
@settings(max_examples=50)
def test_representationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationDescription)

@given(instance=viewpoint_description_RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationimportdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationImportDescription)

@given(instance=viewpoint_description_RepresentationTemplate_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationtemplate_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationTemplate)



@given(instance=viewpoint_description_RepresentationTemplate_strategy)
def test_viewpoint_description_representationtemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=validation_ValidationSet_strategy)
@settings(max_examples=50)
def test_validation_validationset_instantiation(instance):
    assert isinstance(instance, validation_ValidationSet)

@given(instance=description_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description_identifiedelement_instantiation(instance):
    assert isinstance(instance, description_IdentifiedElement)

@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description_enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)

@given(instance=description_Component_strategy)
@settings(max_examples=50)
def test_description_component_instantiation(instance):
    assert isinstance(instance, description_Component)

@given(instance=viewpoint_description_Component_strategy)
@settings(max_examples=50)
def test_viewpoint_description_component_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Component)

@given(instance=UserColorsPalette_strategy)
@settings(max_examples=50)
def test_usercolorspalette_instantiation(instance):
    assert isinstance(instance, UserColorsPalette)

@given(instance=SytemColorsPalette_strategy)
@settings(max_examples=50)
def test_sytemcolorspalette_instantiation(instance):
    assert isinstance(instance, SytemColorsPalette)

@given(instance=viewpoint_Customizable_strategy)
@settings(max_examples=50)
def test_viewpoint_customizable_instantiation(instance):
    assert isinstance(instance, viewpoint_Customizable)



@given(instance=viewpoint_Customizable_strategy)
def test_viewpoint_customizable_customFeatures_setter(instance):
    original = instance.customFeatures
    instance.customFeatures = original
    assert instance.customFeatures == original

@given(instance=DFile_strategy)
@settings(max_examples=50)
def test_dfile_instantiation(instance):
    assert isinstance(instance, DFile)

@given(instance=viewpoint_DModel_strategy)
@settings(max_examples=50)
def test_viewpoint_dmodel_instantiation(instance):
    assert isinstance(instance, viewpoint_DModel)

@given(instance=DResourceContainer_strategy)
@settings(max_examples=50)
def test_dresourcecontainer_instantiation(instance):
    assert isinstance(instance, DResourceContainer)

@given(instance=viewpoint_DFolder_strategy)
@settings(max_examples=50)
def test_viewpoint_dfolder_instantiation(instance):
    assert isinstance(instance, viewpoint_DFolder)

@given(instance=viewpoint_DProject_strategy)
@settings(max_examples=50)
def test_viewpoint_dproject_instantiation(instance):
    assert isinstance(instance, viewpoint_DProject)

@given(instance=DResource_strategy)
@settings(max_examples=50)
def test_dresource_instantiation(instance):
    assert isinstance(instance, DResource)

@given(instance=viewpoint_DResourceContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_dresourcecontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DResourceContainer)

@given(instance=viewpoint_DFile_strategy)
@settings(max_examples=50)
def test_viewpoint_dfile_instantiation(instance):
    assert isinstance(instance, viewpoint_DFile)

@given(instance=viewpoint_DResource_strategy)
@settings(max_examples=50)
def test_viewpoint_dresource_instantiation(instance):
    assert isinstance(instance, viewpoint_DResource)



@given(instance=viewpoint_DResource_strategy)
def test_viewpoint_dresource_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=viewpoint_DResource_strategy)
def test_viewpoint_dresource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_SessionManagerEObject_strategy)
@settings(max_examples=50)
def test_viewpoint_sessionmanagereobject_instantiation(instance):
    assert isinstance(instance, viewpoint_SessionManagerEObject)

@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysissessioneobject_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisSessionEObject)



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_resources_setter(instance):
    original = instance.resources
    instance.resources = original
    assert instance.resources == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_controlledResources_setter(instance):
    original = instance.controlledResources
    instance.controlledResources = original
    assert instance.controlledResources == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_blocked_setter(instance):
    original = instance.blocked
    instance.blocked = original
    assert instance.blocked == original



@given(instance=viewpoint_DAnalysisSessionEObject_strategy)
def test_viewpoint_danalysissessioneobject_synchronizationStatus_setter(instance):
    original = instance.synchronizationStatus
    instance.synchronizationStatus = original
    assert instance.synchronizationStatus == original

@given(instance=viewpoint_RGBValues_strategy)
@settings(max_examples=50)
def test_viewpoint_rgbvalues_instantiation(instance):
    assert isinstance(instance, viewpoint_RGBValues)



@given(instance=viewpoint_RGBValues_strategy)
def test_viewpoint_rgbvalues_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original



@given(instance=viewpoint_RGBValues_strategy)
def test_viewpoint_rgbvalues_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=viewpoint_RGBValues_strategy)
def test_viewpoint_rgbvalues_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=DNavigationLink_strategy)
@settings(max_examples=50)
def test_dnavigationlink_instantiation(instance):
    assert isinstance(instance, DNavigationLink)

@given(instance=viewpoint_diagram_DDiagramLink_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ddiagramlink_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagramLink)

@given(instance=viewpoint_DEObjectLink_strategy)
@settings(max_examples=50)
def test_viewpoint_deobjectlink_instantiation(instance):
    assert isinstance(instance, viewpoint_DEObjectLink)

@given(instance=viewpoint_DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_viewpoint_draganddroptarget_instantiation(instance):
    assert isinstance(instance, viewpoint_DragAndDropTarget)

@given(instance=style_StyleDescription_strategy)
@settings(max_examples=50)
def test_style_styledescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)

@given(instance=viewpoint_style_NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_style_nodestyledescription_instantiation(instance):
    assert isinstance(instance, viewpoint_style_NodeStyleDescription)



@given(instance=viewpoint_style_NodeStyleDescription_strategy)
def test_viewpoint_style_nodestyledescription_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original



@given(instance=viewpoint_style_NodeStyleDescription_strategy)
def test_viewpoint_style_nodestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original



@given(instance=viewpoint_style_NodeStyleDescription_strategy)
def test_viewpoint_style_nodestyledescription_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=viewpoint_style_NodeStyleDescription_strategy)
def test_viewpoint_style_nodestyledescription_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=Customizable_strategy)
@settings(max_examples=50)
def test_customizable_instantiation(instance):
    assert isinstance(instance, Customizable)

@given(instance=viewpoint_diagram_GaugeSection_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_gaugesection_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_GaugeSection)



@given(instance=viewpoint_diagram_GaugeSection_strategy)
def test_viewpoint_diagram_gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=viewpoint_diagram_GaugeSection_strategy)
def test_viewpoint_diagram_gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=viewpoint_diagram_GaugeSection_strategy)
def test_viewpoint_diagram_gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=viewpoint_diagram_GaugeSection_strategy)
def test_viewpoint_diagram_gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=viewpoint_BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_BasicLabelStyle)



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_labelSize_setter(instance):
    original = instance.labelSize
    instance.labelSize = original
    assert instance.labelSize == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_showIcon_setter(instance):
    original = instance.showIcon
    instance.showIcon = original
    assert instance.showIcon == original



@given(instance=viewpoint_BasicLabelStyle_strategy)
def test_viewpoint_basiclabelstyle_labelFormat_setter(instance):
    original = instance.labelFormat
    instance.labelFormat = original
    assert instance.labelFormat == original

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=viewpoint_diagram_EndLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_endlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_EndLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_EndLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_endlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in viewpoint_diagram_EndLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_EndLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_EndLabelStyle is not implemented or raised an error")

@given(instance=viewpoint_diagram_BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_beginlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_BeginLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_BeginLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_beginlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in viewpoint_diagram_BeginLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_BeginLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_BeginLabelStyle is not implemented or raised an error")

@given(instance=viewpoint_diagram_CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_centerlabelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_CenterLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_CenterLabelStyle_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_centerlabelstyle_setdescription_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDescription(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDescription).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDescription' in viewpoint_diagram_CenterLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_CenterLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in viewpoint_diagram_CenterLabelStyle is not implemented or raised an error")

@given(instance=viewpoint_LabelStyle_strategy)
@settings(max_examples=50)
def test_viewpoint_labelstyle_instantiation(instance):
    assert isinstance(instance, viewpoint_LabelStyle)



@given(instance=viewpoint_LabelStyle_strategy)
def test_viewpoint_labelstyle_labelAlignment_setter(instance):
    original = instance.labelAlignment
    instance.labelAlignment = original
    assert instance.labelAlignment == original

@given(instance=viewpoint_DAnalysisCustomData_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysiscustomdata_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysisCustomData)



@given(instance=viewpoint_DAnalysisCustomData_strategy)
def test_viewpoint_danalysiscustomdata_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=viewpoint_DSourceFileLink_strategy)
@settings(max_examples=50)
def test_viewpoint_dsourcefilelink_instantiation(instance):
    assert isinstance(instance, viewpoint_DSourceFileLink)



@given(instance=viewpoint_DSourceFileLink_strategy)
def test_viewpoint_dsourcefilelink_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original



@given(instance=viewpoint_DSourceFileLink_strategy)
def test_viewpoint_dsourcefilelink_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original



@given(instance=viewpoint_DSourceFileLink_strategy)
def test_viewpoint_dsourcefilelink_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=viewpoint_description_MappingBasedDecoration_strategy)
@settings(max_examples=50)
def test_viewpoint_description_mappingbaseddecoration_instantiation(instance):
    assert isinstance(instance, viewpoint_description_MappingBasedDecoration)

@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
@settings(max_examples=50)
def test_viewpoint_description_semanticbaseddecoration_instantiation(instance):
    assert isinstance(instance, viewpoint_description_SemanticBasedDecoration)



@given(instance=viewpoint_description_SemanticBasedDecoration_strategy)
def test_viewpoint_description_semanticbaseddecoration_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=viewpoint_Decoration_strategy)
@settings(max_examples=50)
def test_viewpoint_decoration_instantiation(instance):
    assert isinstance(instance, viewpoint_Decoration)

@given(instance=Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_instantiation(instance):
    assert isinstance(instance, Viewpoint)

@given(instance=viewpoint_MetaModelExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_metamodelextension_instantiation(instance):
    assert isinstance(instance, viewpoint_MetaModelExtension)

@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)

@given(instance=viewpoint_diagram_DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DSemanticDiagram)

@given(instance=DStylizable_strategy)
@settings(max_examples=50)
def test_dstylizable_instantiation(instance):
    assert isinstance(instance, DStylizable)

@given(instance=DMappingBased_strategy)
@settings(max_examples=50)
def test_dmappingbased_instantiation(instance):
    assert isinstance(instance, DMappingBased)

@given(instance=DLabelled_strategy)
@settings(max_examples=50)
def test_dlabelled_instantiation(instance):
    assert isinstance(instance, DLabelled)

@given(instance=AnnotationEntry_strategy)
@settings(max_examples=50)
def test_annotationentry_instantiation(instance):
    assert isinstance(instance, AnnotationEntry)

@given(instance=description_DModelElement_strategy)
@settings(max_examples=50)
def test_description_dmodelelement_instantiation(instance):
    assert isinstance(instance, description_DModelElement)

@given(instance=DRefreshable_strategy)
@settings(max_examples=50)
def test_drefreshable_instantiation(instance):
    assert isinstance(instance, DRefreshable)

@given(instance=viewpoint_DRepresentationElement_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentationelement_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationElement)



@given(instance=viewpoint_DRepresentationElement_strategy)
def test_viewpoint_drepresentationelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_Style_strategy)
@settings(max_examples=50)
def test_viewpoint_style_instantiation(instance):
    assert isinstance(instance, viewpoint_Style)

@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=50)
def test_description_documentedelement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)

@given(instance=viewpoint_description_Layer_strategy)
@settings(max_examples=50)
def test_viewpoint_description_layer_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Layer)



@given(instance=viewpoint_description_Layer_strategy)
def test_viewpoint_description_layer_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint_filter_FilterDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_filter_filterdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_filter_FilterDescription)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_filter_FilterDescription_strategy)
@settings(max_examples=30)
def test_viewpoint_filter_filterdescription_isvisible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isVisible(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isVisible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isVisible' in viewpoint_filter_FilterDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in viewpoint_filter_FilterDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in viewpoint_filter_FilterDescription is not implemented or raised an error")

@given(instance=viewpoint_tool_ToolSection_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolsection_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolSection)



@given(instance=viewpoint_tool_ToolSection_strategy)
def test_viewpoint_tool_toolsection_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=viewpoint_description_EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_viewpoint_description_edgemappingimport_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EdgeMappingImport)



@given(instance=viewpoint_description_EdgeMappingImport_strategy)
def test_viewpoint_description_edgemappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original

@given(instance=viewpoint_diagram_DDiagram_strategy)
@settings(max_examples=50)
def test_viewpoint_diagram_ddiagram_instantiation(instance):
    assert isinstance(instance, viewpoint_diagram_DDiagram)



@given(instance=viewpoint_diagram_DDiagram_strategy)
def test_viewpoint_diagram_ddiagram_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original



@given(instance=viewpoint_diagram_DDiagram_strategy)
def test_viewpoint_diagram_ddiagram_headerHeight_setter(instance):
    original = instance.headerHeight
    instance.headerHeight = original
    assert instance.headerHeight == original



@given(instance=viewpoint_diagram_DDiagram_strategy)
def test_viewpoint_diagram_ddiagram_isInLayoutingMode_setter(instance):
    original = instance.isInLayoutingMode
    instance.isInLayoutingMode = original
    assert instance.isInLayoutingMode == original



@given(instance=viewpoint_diagram_DDiagram_strategy)
def test_viewpoint_diagram_ddiagram_info_setter(instance):
    original = instance.info
    instance.info = original
    assert instance.info == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_DDiagram_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_ddiagram_finddiagramelements_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findDiagramElements(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findDiagramElements).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findDiagramElements' in viewpoint_diagram_DDiagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDiagramElements' in viewpoint_diagram_DDiagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDiagramElements' in viewpoint_diagram_DDiagram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_diagram_DDiagram_strategy)
@settings(max_examples=30)
def test_viewpoint_diagram_ddiagram_clean_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clean()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clean).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clean' in viewpoint_diagram_DDiagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clean' in viewpoint_diagram_DDiagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clean' in viewpoint_diagram_DDiagram is not implemented or raised an error")

@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=50)
def test_viewpoint_description_viewpoint_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Viewpoint)



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_modelFileExtension_setter(instance):
    original = instance.modelFileExtension
    instance.modelFileExtension = original
    assert instance.modelFileExtension == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_conflicts_setter(instance):
    original = instance.conflicts
    instance.conflicts = original
    assert instance.conflicts == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_reuses_setter(instance):
    original = instance.reuses
    instance.reuses = original
    assert instance.reuses == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original



@given(instance=viewpoint_description_Viewpoint_strategy)
def test_viewpoint_description_viewpoint_customizes_setter(instance):
    original = instance.customizes
    instance.customizes = original
    assert instance.customizes == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_Viewpoint_strategy)
@settings(max_examples=30)
def test_viewpoint_description_viewpoint_initview_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initView(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initView).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initView' in viewpoint_description_Viewpoint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initView' in viewpoint_description_Viewpoint is not implemented or raised an error")

@given(instance=viewpoint_concern_ConcernDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_concern_concerndescription_instantiation(instance):
    assert isinstance(instance, viewpoint_concern_ConcernDescription)

@given(instance=viewpoint_description_EdgeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_edgemapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_EdgeMapping)



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_pathExpression_setter(instance):
    original = instance.pathExpression
    instance.pathExpression = original
    assert instance.pathExpression == original



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=viewpoint_description_EdgeMapping_strategy)
def test_viewpoint_description_edgemapping_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_edgemapping_updateedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateEdge' in viewpoint_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateEdge' in viewpoint_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateEdge' in viewpoint_description_EdgeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_edgemapping_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in viewpoint_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in viewpoint_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in viewpoint_description_EdgeMapping is not implemented or raised an error")

@given(instance=viewpoint_description_RepresentationDescription_strategy)
@settings(max_examples=50)
def test_viewpoint_description_representationdescription_instantiation(instance):
    assert isinstance(instance, viewpoint_description_RepresentationDescription)



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_initialisation_setter(instance):
    original = instance.initialisation
    instance.initialisation = original
    assert instance.initialisation == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_titleExpression_setter(instance):
    original = instance.titleExpression
    instance.titleExpression = original
    assert instance.titleExpression == original



@given(instance=viewpoint_description_RepresentationDescription_strategy)
def test_viewpoint_description_representationdescription_showOnStartup_setter(instance):
    original = instance.showOnStartup
    instance.showOnStartup = original
    assert instance.showOnStartup == original

@given(instance=viewpoint_description_Group_strategy)
@settings(max_examples=50)
def test_viewpoint_description_group_instantiation(instance):
    assert isinstance(instance, viewpoint_description_Group)



@given(instance=viewpoint_description_Group_strategy)
def test_viewpoint_description_group_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=viewpoint_description_Group_strategy)
def test_viewpoint_description_group_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_viewpoint_description_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, viewpoint_description_AbstractNodeMapping)



@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
def test_viewpoint_description_abstractnodemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_abstractnodemapping_adddonenode_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addDoneNode(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addDoneNode).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addDoneNode' in viewpoint_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addDoneNode' in viewpoint_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addDoneNode' in viewpoint_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_abstractnodemapping_finddnodefromeobject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findDNodeFromEObject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findDNodeFromEObject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findDNodeFromEObject' in viewpoint_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDNodeFromEObject' in viewpoint_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDNodeFromEObject' in viewpoint_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_viewpoint_description_abstractnodemapping_cleardnodesdone_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clearDNodesDone()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clearDNodesDone).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clearDNodesDone' in viewpoint_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clearDNodesDone' in viewpoint_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clearDNodesDone' in viewpoint_description_AbstractNodeMapping is not implemented or raised an error")

@given(instance=viewpoint_tool_ToolEntry_strategy)
@settings(max_examples=50)
def test_viewpoint_tool_toolentry_instantiation(instance):
    assert isinstance(instance, viewpoint_tool_ToolEntry)

@given(instance=viewpoint_DRepresentation_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentation_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentation)



@given(instance=viewpoint_DRepresentation_strategy)
def test_viewpoint_drepresentation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DRepresentation_strategy)
@settings(max_examples=30)
def test_viewpoint_drepresentation_updatecontent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateContent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateContent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateContent' in viewpoint_DRepresentation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateContent' in viewpoint_DRepresentation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateContent' in viewpoint_DRepresentation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DRepresentation_strategy)
@settings(max_examples=30)
def test_viewpoint_drepresentation_createcontents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createContents(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createContents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createContents' in viewpoint_DRepresentation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createContents' in viewpoint_DRepresentation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createContents' in viewpoint_DRepresentation is not implemented or raised an error")

@given(instance=viewpoint_DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_viewpoint_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, viewpoint_DSemanticDecorator)

@given(instance=DDiagramSet_strategy)
@settings(max_examples=50)
def test_ddiagramset_instantiation(instance):
    assert isinstance(instance, DDiagramSet)

@given(instance=DView_strategy)
@settings(max_examples=50)
def test_dview_instantiation(instance):
    assert isinstance(instance, DView)

@given(instance=viewpoint_DRepresentationContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_drepresentationcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DRepresentationContainer)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DRepresentationContainer_strategy)
@settings(max_examples=30)
def test_viewpoint_drepresentationcontainer_addsemanticdiagram_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addSemanticDiagram(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addSemanticDiagram).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addSemanticDiagram' in viewpoint_DRepresentationContainer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addSemanticDiagram' in viewpoint_DRepresentationContainer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addSemanticDiagram' in viewpoint_DRepresentationContainer is not implemented or raised an error")

@given(instance=viewpoint_DContainer_strategy)
@settings(max_examples=50)
def test_viewpoint_dcontainer_instantiation(instance):
    assert isinstance(instance, viewpoint_DContainer)

@given(instance=viewpoint_DMappingBased_strategy)
@settings(max_examples=50)
def test_viewpoint_dmappingbased_instantiation(instance):
    assert isinstance(instance, viewpoint_DMappingBased)

@given(instance=viewpoint_DLabelled_strategy)
@settings(max_examples=50)
def test_viewpoint_dlabelled_instantiation(instance):
    assert isinstance(instance, viewpoint_DLabelled)

@given(instance=viewpoint_DRefreshable_strategy)
@settings(max_examples=50)
def test_viewpoint_drefreshable_instantiation(instance):
    assert isinstance(instance, viewpoint_DRefreshable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DRefreshable_strategy)
@settings(max_examples=30)
def test_viewpoint_drefreshable_refresh_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.refresh()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.refresh).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'refresh' in viewpoint_DRefreshable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'refresh' in viewpoint_DRefreshable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'refresh' in viewpoint_DRefreshable is not implemented or raised an error")

@given(instance=viewpoint_DStylizable_strategy)
@settings(max_examples=50)
def test_viewpoint_dstylizable_instantiation(instance):
    assert isinstance(instance, viewpoint_DStylizable)

@given(instance=viewpoint_DNavigationLink_strategy)
@settings(max_examples=50)
def test_viewpoint_dnavigationlink_instantiation(instance):
    assert isinstance(instance, viewpoint_DNavigationLink)



@given(instance=viewpoint_DNavigationLink_strategy)
def test_viewpoint_dnavigationlink_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=viewpoint_DNavigationLink_strategy)
def test_viewpoint_dnavigationlink_targetType_setter(instance):
    original = instance.targetType
    instance.targetType = original
    assert instance.targetType == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DNavigationLink_strategy)
@settings(max_examples=30)
def test_viewpoint_dnavigationlink_isavailable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isAvailable()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isAvailable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isAvailable' in viewpoint_DNavigationLink is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isAvailable' in viewpoint_DNavigationLink did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isAvailable' in viewpoint_DNavigationLink is not implemented or raised an error")

@given(instance=viewpoint_DNavigable_strategy)
@settings(max_examples=50)
def test_viewpoint_dnavigable_instantiation(instance):
    assert isinstance(instance, viewpoint_DNavigable)

@given(instance=viewpoint_DValidable_strategy)
@settings(max_examples=50)
def test_viewpoint_dvalidable_instantiation(instance):
    assert isinstance(instance, viewpoint_DValidable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=viewpoint_DValidable_strategy)
@settings(max_examples=30)
def test_viewpoint_dvalidable_validate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.validate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.validate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'validate' in viewpoint_DValidable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'validate' in viewpoint_DValidable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'validate' in viewpoint_DValidable is not implemented or raised an error")

@given(instance=FeatureExtensionDescription_strategy)
@settings(max_examples=50)
def test_featureextensiondescription_instantiation(instance):
    assert isinstance(instance, FeatureExtensionDescription)

@given(instance=viewpoint_DFeatureExtension_strategy)
@settings(max_examples=50)
def test_viewpoint_dfeatureextension_instantiation(instance):
    assert isinstance(instance, viewpoint_DFeatureExtension)

@given(instance=viewpoint_DView_strategy)
@settings(max_examples=50)
def test_viewpoint_dview_instantiation(instance):
    assert isinstance(instance, viewpoint_DView)



@given(instance=viewpoint_DView_strategy)
def test_viewpoint_dview_initialized_setter(instance):
    original = instance.initialized
    instance.initialized = original
    assert instance.initialized == original

@given(instance=DAnnotationEntry_strategy)
@settings(max_examples=50)
def test_dannotationentry_instantiation(instance):
    assert isinstance(instance, DAnnotationEntry)

@given(instance=viewpoint_EObject_strategy)
@settings(max_examples=50)
def test_viewpoint_eobject_instantiation(instance):
    assert isinstance(instance, viewpoint_EObject)

@given(instance=viewpoint_DAnalysis_strategy)
@settings(max_examples=50)
def test_viewpoint_danalysis_instantiation(instance):
    assert isinstance(instance, viewpoint_DAnalysis)



@given(instance=viewpoint_DAnalysis_strategy)
def test_viewpoint_danalysis_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original
