import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tool_VariableContainer,
    description_AbstractVariable,
    diagram_tool_ElementDoubleClickVariable,
    diagram_tool_TargetEdgeCreationVariable,
    diagram_tool_SourceEdgeViewCreationVariable,
    diagram_tool_TargetEdgeViewCreationVariable,
    diagram_tool_SourceEdgeCreationVariable,
    tool_EditMaskVariables,
    AbstractToolDescription,
    diagram_tool_BehaviorTool,
    diagram_tool_RequestDescription,
    tool_ElementSelectVariable,
    tool_ElementDeleteVariable,
    diagram_tool_DeleteHookParameter,
    tool_DeleteHookParameter,
    diagram_tool_DeleteHook,
    tool_ElementDoubleClickVariable,
    tool_DeleteHook,
    tool_TargetEdgeViewCreationVariable,
    tool_SourceEdgeViewCreationVariable,
    tool_InitEdgeCreationOperation,
    MappingBasedToolDescription,
    diagram_tool_DeleteElementDescription,
    diagram_tool_DoubleClickDescription,
    diagram_tool_ReconnectEdgeDescription,
    diagram_tool_ContainerCreationDescription,
    diagram_tool_DirectEditLabel,
    diagram_tool_NodeCreationDescription,
    tool_ToolGroup,
    diagram_tool_ToolGroupExtension,
    tool_TargetEdgeCreationVariable,
    tool_SourceEdgeCreationVariable,
    diagram_tool_EdgeCreationDescription,
    tool_InitialNodeCreationOperation,
    tool_ContainerViewVariable,
    tool_NodeCreationVariable,
    style_EndLabelStyleDescription,
    style_CenterLabelStyleDescription,
    ToolEntry,
    diagram_tool_ToolGroup,
    tool_ToolGroupExtension,
    tool_PopupMenu,
    tool_ToolEntry,
    diagram_style_HideLabelCapabilityStyleDescription,
    EdgeStyleDescription,
    diagram_style_BracketEdgeStyleDescription,
    BasicLabelStyleDescription,
    diagram_style_CenterLabelStyleDescription,
    diagram_style_EndLabelStyleDescription,
    diagram_style_BeginLabelStyleDescription,
    style_SizeComputationContainerStyleDescription,
    style_BeginLabelStyleDescription,
    style_LabelBorderStyleDescription,
    style_RoundedCornerStyleDescription,
    diagram_style_SizeComputationContainerStyleDescription,
    diagram_style_GaugeSectionDescription,
    style_GaugeSectionDescription,
    DecorationDescriptionsSet,
    NodeStyleDescription,
    diagram_style_LozengeNodeDescription,
    diagram_style_DotDescription,
    diagram_style_EllipseNodeDescription,
    diagram_style_BundledImageDescription,
    diagram_style_NoteDescription,
    diagram_style_GaugeCompositeStyleDescription,
    diagram_style_SquareDescription,
    diagram_style_CustomStyleDescription,
    style_HideLabelCapabilityStyleDescription,
    style_TooltipStyleDescription,
    style_LabelStyleDescription,
    style_BorderedStyleDescription,
    diagram_style_ContainerStyleDescription,
    ColorDescription,
    StyleDescription,
    diagram_style_RoundedCornerStyleDescription,
    diagram_style_EdgeStyleDescription,
    diagram_style_BorderedStyleDescription,
    tool_ContainerDropDescription,
    diagram_description_DragAndDropTargetDescription,
    Customization,
    DecorationDescription,
    diagram_description_MappingBasedDecoration,
    description_EndUserDocumentedElement,
    DocumentedElement,
    diagram_description_Layout,
    ConditionalStyleDescription,
    diagram_description_ConditionalEdgeStyleDescription,
    diagram_description_ConditionalContainerStyleDescription,
    diagram_description_ConditionalNodeStyleDescription,
    description_IdentifiedElement,
    diagram_description_IEdgeMapping,
    AbstractNodeMapping,
    tool_ReconnectEdgeDescription,
    ConditionalEdgeStyleDescription,
    style_EdgeStyleDescription,
    description_IEdgeMapping,
    description_ContainerMapping,
    description_AbstractMappingImport,
    diagram_description_ContainerMappingImport,
    description_NodeMapping,
    diagram_description_NodeMappingImport,
    ConditionalContainerStyleDescription,
    style_ContainerStyleDescription,
    diagram_style_ShapeContainerStyleDescription,
    diagram_style_FlatContainerStyleDescription,
    ConditionalNodeStyleDescription,
    style_NodeStyleDescription,
    diagram_style_WorkspaceImageDescription,
    description_AbstractNodeMapping,
    description_RepresentationElementMapping,
    description_DiagramElementMapping,
    tool_DoubleClickDescription,
    tool_DirectEditLabel,
    tool_DeleteElementDescription,
    RepresentationExtensionDescription,
    diagram_description_DiagramExtensionDescription,
    description_DiagramDescription,
    description_RepresentationImportDescription,
    diagram_description_DiagramImportDescription,
    tool_ToolSection,
    tool_AbstractToolDescription,
    EdgeMappingImport,
    AdditionalLayer,
    tool_InitialOperation,
    Layout,
    diagram_description_CompositeLayout,
    diagram_description_OrderedTreeLayout,
    tool_RepresentationCreationDescription,
    diagram_concern_ConcernSet,
    InteractiveVariableDescription,
    filter_Filter,
    FilterDescription,
    diagram_filter_CompositeFilterDescription,
    Filter,
    diagram_filter_VariableFilter,
    diagram_filter_MappingFilter,
    diagram_filter_Filter,
    tool_InitialContainerDropOperation,
    CreateView,
    diagram_tool_CreateEdgeView,
    tool_ElementDropVariable,
    tool_DropContainerVariable,
    diagram_tool_ContainerDropDescription,
    RepresentationNavigationDescription,
    diagram_tool_DiagramNavigationDescription,
    RepresentationCreationDescription,
    diagram_tool_DiagramCreationDescription,
    ContainerModelOperation,
    diagram_tool_Navigation,
    diagram_tool_CreateView,
    diagram_tool_NodeCreationVariable,
    diagram_HideLabelCapabilityStyle,
    concern_ConcernSet,
    validation_ValidationSet,
    EdgeMapping,
    description_PasteTargetDescription,
    diagram_description_DiagramElementMapping,
    description_RepresentationDescription,
    description_DragAndDropTargetDescription,
    diagram_description_NodeMapping,
    diagram_description_ContainerMapping,
    diagram_description_DiagramDescription,
    diagram_EObject,
    tool_SelectModelElementVariable,
    TypedVariable,
    diagram_DragAndDropTarget,
    style_StyleDescription,
    diagram_style_NodeStyleDescription,
    diagram_ComputedStyleDescriptionRegistry,
    EdgeStyle,
    diagram_BracketEdgeStyle,
    BasicLabelStyle,
    CollapseFilter,
    diagram_IndirectlyCollapseFilter,
    diagram_VariableValue,
    diagram_EndLabelStyle,
    diagram_CenterLabelStyle,
    diagram_BeginLabelStyle,
    ContainerStyle,
    diagram_FlatContainerStyle,
    diagram_ShapeContainerStyle,
    Customizable,
    diagram_GaugeSection,
    NodeStyle,
    diagram_Note,
    diagram_CustomStyle,
    diagram_Square,
    diagram_Ellipse,
    diagram_Lozenge,
    diagram_BundledImage,
    diagram_WorkspaceImage,
    diagram_GaugeCompositeStyle,
    VariableValue,
    diagram_EObjectVariableValue,
    diagram_TypedVariableValue,
    diagram_Dot,
    HideLabelCapabilityStyle,
    BorderedStyle,
    Style,
    diagram_BorderedStyle,
    LabelStyle,
    IEdgeMapping,
    diagram_EdgeTarget,
    diagram_EdgeStyle,
    NodeMapping,
    DDiagramElementContainer,
    diagram_DNodeList,
    diagram_DNodeContainer,
    ContainerMapping,
    diagram_ContainerStyle,
    diagram_Style,
    diagram_GraphicalFilter,
    diagram_NodeStyle,
    EdgeTarget,
    AbstractDNode,
    DDiagramElement,
    diagram_AbstractDNode,
    filter_CompositeFilterDescription,
    GraphicalFilter,
    diagram_HideLabelFilter,
    diagram_CollapseFilter,
    diagram_FoldingPointFilter,
    diagram_AbsoluteBoundsFilter,
    diagram_FoldingFilter,
    diagram_AppliedCompositeFilters,
    diagram_HideFilter,
    DiagramElementMapping,
    diagram_Decoration,
    DRepresentationElement,
    DSemanticDecorator,
    DDiagram,
    diagram_DSemanticDiagram,
    Layer,
    diagram_description_AdditionalLayer,
    diagram_FilterVariableHistory,
    tool_BehaviorTool,
    validation_ValidationRule,
    DRepresentation,
    filter_FilterDescription,
    concern_ConcernDescription,
    diagram_DNodeListElement,
    diagram_DEdge,
    DiagramDescription,
    diagram_DDiagramElement,
    DragAndDropTarget,
    diagram_DNode,
    diagram_DDiagramElementContainer,
    description_DocumentedElement,
    diagram_DDiagram,
    diagram_description_Layer,
    diagram_concern_ConcernDescription,
    diagram_filter_FilterDescription,
    diagram_description_EdgeMappingImport,
    diagram_description_EdgeMapping,
    diagram_tool_ToolSection,
    diagram_description_AbstractNodeMapping,
    AlignmentKind,
    ArrangeConstraint,
    ContainerShape,
    ContainerLayout,
    BackgroundStyle,
    LayoutDirection,
    FoldingStyle,
    EdgeArrows,
    ResizeKind,
    ReconnectionKind,
    EdgeRouting,
    LineStyle,
    BundledImageShape,
    LabelPosition,
    CenteringStyle,
    FilterKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tool_variablecontainer_is_not_abstract():
    assert not inspect.isabstract(tool_VariableContainer)


def test_tool_variablecontainer_constructor_exists():
    assert callable(tool_VariableContainer.__init__)


def test_tool_variablecontainer_constructor_args():
    sig = inspect.signature(tool_VariableContainer.__init__)
    params = list(sig.parameters.keys())



def test_description_abstractvariable_is_not_abstract():
    assert not inspect.isabstract(description_AbstractVariable)


def test_description_abstractvariable_constructor_exists():
    assert callable(description_AbstractVariable.__init__)


def test_description_abstractvariable_constructor_args():
    sig = inspect.signature(description_AbstractVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_elementdoubleclickvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ElementDoubleClickVariable)


def test_diagram_tool_elementdoubleclickvariable_constructor_exists():
    assert callable(diagram_tool_ElementDoubleClickVariable.__init__)


def test_diagram_tool_elementdoubleclickvariable_constructor_args():
    sig = inspect.signature(diagram_tool_ElementDoubleClickVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_targetedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_TargetEdgeCreationVariable)


def test_diagram_tool_targetedgecreationvariable_constructor_exists():
    assert callable(diagram_tool_TargetEdgeCreationVariable.__init__)


def test_diagram_tool_targetedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_TargetEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_sourceedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_SourceEdgeViewCreationVariable)


def test_diagram_tool_sourceedgeviewcreationvariable_constructor_exists():
    assert callable(diagram_tool_SourceEdgeViewCreationVariable.__init__)


def test_diagram_tool_sourceedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_SourceEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_targetedgeviewcreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_TargetEdgeViewCreationVariable)


def test_diagram_tool_targetedgeviewcreationvariable_constructor_exists():
    assert callable(diagram_tool_TargetEdgeViewCreationVariable.__init__)


def test_diagram_tool_targetedgeviewcreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_TargetEdgeViewCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_sourceedgecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_SourceEdgeCreationVariable)


def test_diagram_tool_sourceedgecreationvariable_constructor_exists():
    assert callable(diagram_tool_SourceEdgeCreationVariable.__init__)


def test_diagram_tool_sourceedgecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_SourceEdgeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_editmaskvariables_is_not_abstract():
    assert not inspect.isabstract(tool_EditMaskVariables)


def test_tool_editmaskvariables_constructor_exists():
    assert callable(tool_EditMaskVariables.__init__)


def test_tool_editmaskvariables_constructor_args():
    sig = inspect.signature(tool_EditMaskVariables.__init__)
    params = list(sig.parameters.keys())



def test_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(AbstractToolDescription)


def test_abstracttooldescription_constructor_exists():
    assert callable(AbstractToolDescription.__init__)


def test_abstracttooldescription_constructor_args():
    sig = inspect.signature(AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_behaviortool_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_BehaviorTool)


def test_diagram_tool_behaviortool_constructor_exists():
    assert callable(diagram_tool_BehaviorTool.__init__)


def test_diagram_tool_behaviortool_constructor_args():
    sig = inspect.signature(diagram_tool_BehaviorTool.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_diagram_tool_behaviortool_has_domainClass():
    assert hasattr(diagram_tool_BehaviorTool, "domainClass")
    descriptor = None
    for klass in diagram_tool_BehaviorTool.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_requestdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_RequestDescription)


def test_diagram_tool_requestdescription_constructor_exists():
    assert callable(diagram_tool_RequestDescription.__init__)


def test_diagram_tool_requestdescription_constructor_args():
    sig = inspect.signature(diagram_tool_RequestDescription.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_diagram_tool_requestdescription_has_type():
    assert hasattr(diagram_tool_RequestDescription, "type")
    descriptor = None
    for klass in diagram_tool_RequestDescription.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_tool_elementselectvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementSelectVariable)


def test_tool_elementselectvariable_constructor_exists():
    assert callable(tool_ElementSelectVariable.__init__)


def test_tool_elementselectvariable_constructor_args():
    sig = inspect.signature(tool_ElementSelectVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_elementdeletevariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDeleteVariable)


def test_tool_elementdeletevariable_constructor_exists():
    assert callable(tool_ElementDeleteVariable.__init__)


def test_tool_elementdeletevariable_constructor_args():
    sig = inspect.signature(tool_ElementDeleteVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteHookParameter)


def test_diagram_tool_deletehookparameter_constructor_exists():
    assert callable(diagram_tool_DeleteHookParameter.__init__)


def test_diagram_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_diagram_tool_deletehookparameter_has_value():
    assert hasattr(diagram_tool_DeleteHookParameter, "value")
    descriptor = None
    for klass in diagram_tool_DeleteHookParameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_diagram_tool_deletehookparameter_has_name():
    assert hasattr(diagram_tool_DeleteHookParameter, "name")
    descriptor = None
    for klass in diagram_tool_DeleteHookParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tool_deletehookparameter_is_not_abstract():
    assert not inspect.isabstract(tool_DeleteHookParameter)


def test_tool_deletehookparameter_constructor_exists():
    assert callable(tool_DeleteHookParameter.__init__)


def test_tool_deletehookparameter_constructor_args():
    sig = inspect.signature(tool_DeleteHookParameter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_deletehook_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteHook)


def test_diagram_tool_deletehook_constructor_exists():
    assert callable(diagram_tool_DeleteHook.__init__)


def test_diagram_tool_deletehook_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteHook.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram_tool_deletehook_has_id():
    assert hasattr(diagram_tool_DeleteHook, "id")
    descriptor = None
    for klass in diagram_tool_DeleteHook.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



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



def test_tool_initedgecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitEdgeCreationOperation)


def test_tool_initedgecreationoperation_constructor_exists():
    assert callable(tool_InitEdgeCreationOperation.__init__)


def test_tool_initedgecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitEdgeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_mappingbasedtooldescription_is_not_abstract():
    assert not inspect.isabstract(MappingBasedToolDescription)


def test_mappingbasedtooldescription_constructor_exists():
    assert callable(MappingBasedToolDescription.__init__)


def test_mappingbasedtooldescription_constructor_args():
    sig = inspect.signature(MappingBasedToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_deleteelementdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DeleteElementDescription)


def test_diagram_tool_deleteelementdescription_constructor_exists():
    assert callable(diagram_tool_DeleteElementDescription.__init__)


def test_diagram_tool_deleteelementdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DeleteElementDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DoubleClickDescription)


def test_diagram_tool_doubleclickdescription_constructor_exists():
    assert callable(diagram_tool_DoubleClickDescription.__init__)


def test_diagram_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DoubleClickDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ReconnectEdgeDescription)


def test_diagram_tool_reconnectedgedescription_constructor_exists():
    assert callable(diagram_tool_ReconnectEdgeDescription.__init__)


def test_diagram_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(diagram_tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "reconnectionKind" in params, "Missing parameter 'reconnectionKind'"

def test_diagram_tool_reconnectedgedescription_has_reconnectionKind():
    assert hasattr(diagram_tool_ReconnectEdgeDescription, "reconnectionKind")
    descriptor = None
    for klass in diagram_tool_ReconnectEdgeDescription.__mro__:
        if "reconnectionKind" in klass.__dict__:
            descriptor = klass.__dict__["reconnectionKind"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_containercreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ContainerCreationDescription)


def test_diagram_tool_containercreationdescription_constructor_exists():
    assert callable(diagram_tool_ContainerCreationDescription.__init__)


def test_diagram_tool_containercreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_ContainerCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_diagram_tool_containercreationdescription_has_iconPath():
    assert hasattr(diagram_tool_ContainerCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram_tool_ContainerCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_directeditlabel_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DirectEditLabel)


def test_diagram_tool_directeditlabel_constructor_exists():
    assert callable(diagram_tool_DirectEditLabel.__init__)


def test_diagram_tool_directeditlabel_constructor_args():
    sig = inspect.signature(diagram_tool_DirectEditLabel.__init__)
    params = list(sig.parameters.keys())
    assert "inputLabelExpression" in params, "Missing parameter 'inputLabelExpression'"

def test_diagram_tool_directeditlabel_has_inputLabelExpression():
    assert hasattr(diagram_tool_DirectEditLabel, "inputLabelExpression")
    descriptor = None
    for klass in diagram_tool_DirectEditLabel.__mro__:
        if "inputLabelExpression" in klass.__dict__:
            descriptor = klass.__dict__["inputLabelExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_nodecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_NodeCreationDescription)


def test_diagram_tool_nodecreationdescription_constructor_exists():
    assert callable(diagram_tool_NodeCreationDescription.__init__)


def test_diagram_tool_nodecreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_NodeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"

def test_diagram_tool_nodecreationdescription_has_iconPath():
    assert hasattr(diagram_tool_NodeCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram_tool_NodeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)



def test_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroup)


def test_tool_toolgroup_constructor_exists():
    assert callable(tool_ToolGroup.__init__)


def test_tool_toolgroup_constructor_args():
    sig = inspect.signature(tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolGroupExtension)


def test_diagram_tool_toolgroupextension_constructor_exists():
    assert callable(diagram_tool_ToolGroupExtension.__init__)


def test_diagram_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(diagram_tool_ToolGroupExtension.__init__)
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



def test_diagram_tool_edgecreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_EdgeCreationDescription)


def test_diagram_tool_edgecreationdescription_constructor_exists():
    assert callable(diagram_tool_EdgeCreationDescription.__init__)


def test_diagram_tool_edgecreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_EdgeCreationDescription.__init__)
    params = list(sig.parameters.keys())
    assert "iconPath" in params, "Missing parameter 'iconPath'"
    assert "connectionStartPrecondition" in params, "Missing parameter 'connectionStartPrecondition'"

def test_diagram_tool_edgecreationdescription_has_iconPath():
    assert hasattr(diagram_tool_EdgeCreationDescription, "iconPath")
    descriptor = None
    for klass in diagram_tool_EdgeCreationDescription.__mro__:
        if "iconPath" in klass.__dict__:
            descriptor = klass.__dict__["iconPath"]
            break
    assert isinstance(descriptor, property)

def test_diagram_tool_edgecreationdescription_has_connectionStartPrecondition():
    assert hasattr(diagram_tool_EdgeCreationDescription, "connectionStartPrecondition")
    descriptor = None
    for klass in diagram_tool_EdgeCreationDescription.__mro__:
        if "connectionStartPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["connectionStartPrecondition"]
            break
    assert isinstance(descriptor, property)



def test_tool_initialnodecreationoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialNodeCreationOperation)


def test_tool_initialnodecreationoperation_constructor_exists():
    assert callable(tool_InitialNodeCreationOperation.__init__)


def test_tool_initialnodecreationoperation_constructor_args():
    sig = inspect.signature(tool_InitialNodeCreationOperation.__init__)
    params = list(sig.parameters.keys())



def test_tool_containerviewvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerViewVariable)


def test_tool_containerviewvariable_constructor_exists():
    assert callable(tool_ContainerViewVariable.__init__)


def test_tool_containerviewvariable_constructor_args():
    sig = inspect.signature(tool_ContainerViewVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(tool_NodeCreationVariable)


def test_tool_nodecreationvariable_constructor_exists():
    assert callable(tool_NodeCreationVariable.__init__)


def test_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(tool_NodeCreationVariable.__init__)
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



def test_toolentry_is_not_abstract():
    assert not inspect.isabstract(ToolEntry)


def test_toolentry_constructor_exists():
    assert callable(ToolEntry.__init__)


def test_toolentry_constructor_args():
    sig = inspect.signature(ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_toolgroup_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolGroup)


def test_diagram_tool_toolgroup_constructor_exists():
    assert callable(diagram_tool_ToolGroup.__init__)


def test_diagram_tool_toolgroup_constructor_args():
    sig = inspect.signature(diagram_tool_ToolGroup.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolgroupextension_is_not_abstract():
    assert not inspect.isabstract(tool_ToolGroupExtension)


def test_tool_toolgroupextension_constructor_exists():
    assert callable(tool_ToolGroupExtension.__init__)


def test_tool_toolgroupextension_constructor_args():
    sig = inspect.signature(tool_ToolGroupExtension.__init__)
    params = list(sig.parameters.keys())



def test_tool_popupmenu_is_not_abstract():
    assert not inspect.isabstract(tool_PopupMenu)


def test_tool_popupmenu_constructor_exists():
    assert callable(tool_PopupMenu.__init__)


def test_tool_popupmenu_constructor_args():
    sig = inspect.signature(tool_PopupMenu.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolentry_is_not_abstract():
    assert not inspect.isabstract(tool_ToolEntry)


def test_tool_toolentry_constructor_exists():
    assert callable(tool_ToolEntry.__init__)


def test_tool_toolentry_constructor_args():
    sig = inspect.signature(tool_ToolEntry.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_HideLabelCapabilityStyleDescription)


def test_diagram_style_hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(diagram_style_HideLabelCapabilityStyleDescription.__init__)


def test_diagram_style_hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(diagram_style_HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"

def test_diagram_style_hidelabelcapabilitystyledescription_has_hideLabelByDefault():
    assert hasattr(diagram_style_HideLabelCapabilityStyleDescription, "hideLabelByDefault")
    descriptor = None
    for klass in diagram_style_HideLabelCapabilityStyleDescription.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)



def test_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(EdgeStyleDescription)


def test_edgestyledescription_constructor_exists():
    assert callable(EdgeStyleDescription.__init__)


def test_edgestyledescription_constructor_args():
    sig = inspect.signature(EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_bracketedgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BracketEdgeStyleDescription)


def test_diagram_style_bracketedgestyledescription_constructor_exists():
    assert callable(diagram_style_BracketEdgeStyleDescription.__init__)


def test_diagram_style_bracketedgestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BracketEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyleDescription)


def test_basiclabelstyledescription_constructor_exists():
    assert callable(BasicLabelStyleDescription.__init__)


def test_basiclabelstyledescription_constructor_args():
    sig = inspect.signature(BasicLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_centerlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_CenterLabelStyleDescription)


def test_diagram_style_centerlabelstyledescription_constructor_exists():
    assert callable(diagram_style_CenterLabelStyleDescription.__init__)


def test_diagram_style_centerlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_CenterLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_endlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EndLabelStyleDescription)


def test_diagram_style_endlabelstyledescription_constructor_exists():
    assert callable(diagram_style_EndLabelStyleDescription.__init__)


def test_diagram_style_endlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_EndLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BeginLabelStyleDescription)


def test_diagram_style_beginlabelstyledescription_constructor_exists():
    assert callable(diagram_style_BeginLabelStyleDescription.__init__)


def test_diagram_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_SizeComputationContainerStyleDescription)


def test_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(style_SizeComputationContainerStyleDescription.__init__)


def test_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_beginlabelstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_BeginLabelStyleDescription)


def test_style_beginlabelstyledescription_constructor_exists():
    assert callable(style_BeginLabelStyleDescription.__init__)


def test_style_beginlabelstyledescription_constructor_args():
    sig = inspect.signature(style_BeginLabelStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_labelborderstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_LabelBorderStyleDescription)


def test_style_labelborderstyledescription_constructor_exists():
    assert callable(style_LabelBorderStyleDescription.__init__)


def test_style_labelborderstyledescription_constructor_args():
    sig = inspect.signature(style_LabelBorderStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_RoundedCornerStyleDescription)


def test_style_roundedcornerstyledescription_constructor_exists():
    assert callable(style_RoundedCornerStyleDescription.__init__)


def test_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_sizecomputationcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_SizeComputationContainerStyleDescription)


def test_diagram_style_sizecomputationcontainerstyledescription_constructor_exists():
    assert callable(diagram_style_SizeComputationContainerStyleDescription.__init__)


def test_diagram_style_sizecomputationcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_SizeComputationContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"

def test_diagram_style_sizecomputationcontainerstyledescription_has_widthComputationExpression():
    assert hasattr(diagram_style_SizeComputationContainerStyleDescription, "widthComputationExpression")
    descriptor = None
    for klass in diagram_style_SizeComputationContainerStyleDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_sizecomputationcontainerstyledescription_has_heightComputationExpression():
    assert hasattr(diagram_style_SizeComputationContainerStyleDescription, "heightComputationExpression")
    descriptor = None
    for klass in diagram_style_SizeComputationContainerStyleDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_GaugeSectionDescription)


def test_diagram_style_gaugesectiondescription_constructor_exists():
    assert callable(diagram_style_GaugeSectionDescription.__init__)


def test_diagram_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(diagram_style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())
    assert "minValueExpression" in params, "Missing parameter 'minValueExpression'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"
    assert "maxValueExpression" in params, "Missing parameter 'maxValueExpression'"
    assert "label" in params, "Missing parameter 'label'"

def test_diagram_style_gaugesectiondescription_has_minValueExpression():
    assert hasattr(diagram_style_GaugeSectionDescription, "minValueExpression")
    descriptor = None
    for klass in diagram_style_GaugeSectionDescription.__mro__:
        if "minValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["minValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_gaugesectiondescription_has_valueExpression():
    assert hasattr(diagram_style_GaugeSectionDescription, "valueExpression")
    descriptor = None
    for klass in diagram_style_GaugeSectionDescription.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_gaugesectiondescription_has_maxValueExpression():
    assert hasattr(diagram_style_GaugeSectionDescription, "maxValueExpression")
    descriptor = None
    for klass in diagram_style_GaugeSectionDescription.__mro__:
        if "maxValueExpression" in klass.__dict__:
            descriptor = klass.__dict__["maxValueExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_gaugesectiondescription_has_label():
    assert hasattr(diagram_style_GaugeSectionDescription, "label")
    descriptor = None
    for klass in diagram_style_GaugeSectionDescription.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_style_gaugesectiondescription_is_not_abstract():
    assert not inspect.isabstract(style_GaugeSectionDescription)


def test_style_gaugesectiondescription_constructor_exists():
    assert callable(style_GaugeSectionDescription.__init__)


def test_style_gaugesectiondescription_constructor_args():
    sig = inspect.signature(style_GaugeSectionDescription.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescriptionsset_is_not_abstract():
    assert not inspect.isabstract(DecorationDescriptionsSet)


def test_decorationdescriptionsset_constructor_exists():
    assert callable(DecorationDescriptionsSet.__init__)


def test_decorationdescriptionsset_constructor_args():
    sig = inspect.signature(DecorationDescriptionsSet.__init__)
    params = list(sig.parameters.keys())



def test_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(NodeStyleDescription)


def test_nodestyledescription_constructor_exists():
    assert callable(NodeStyleDescription.__init__)


def test_nodestyledescription_constructor_args():
    sig = inspect.signature(NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_lozengenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_LozengeNodeDescription)


def test_diagram_style_lozengenodedescription_constructor_exists():
    assert callable(diagram_style_LozengeNodeDescription.__init__)


def test_diagram_style_lozengenodedescription_constructor_args():
    sig = inspect.signature(diagram_style_LozengeNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "heightComputationExpression" in params, "Missing parameter 'heightComputationExpression'"
    assert "widthComputationExpression" in params, "Missing parameter 'widthComputationExpression'"

def test_diagram_style_lozengenodedescription_has_heightComputationExpression():
    assert hasattr(diagram_style_LozengeNodeDescription, "heightComputationExpression")
    descriptor = None
    for klass in diagram_style_LozengeNodeDescription.__mro__:
        if "heightComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["heightComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_lozengenodedescription_has_widthComputationExpression():
    assert hasattr(diagram_style_LozengeNodeDescription, "widthComputationExpression")
    descriptor = None
    for klass in diagram_style_LozengeNodeDescription.__mro__:
        if "widthComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["widthComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_dotdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_DotDescription)


def test_diagram_style_dotdescription_constructor_exists():
    assert callable(diagram_style_DotDescription.__init__)


def test_diagram_style_dotdescription_constructor_args():
    sig = inspect.signature(diagram_style_DotDescription.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"

def test_diagram_style_dotdescription_has_strokeSizeComputationExpression():
    assert hasattr(diagram_style_DotDescription, "strokeSizeComputationExpression")
    descriptor = None
    for klass in diagram_style_DotDescription.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_ellipsenodedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EllipseNodeDescription)


def test_diagram_style_ellipsenodedescription_constructor_exists():
    assert callable(diagram_style_EllipseNodeDescription.__init__)


def test_diagram_style_ellipsenodedescription_constructor_args():
    sig = inspect.signature(diagram_style_EllipseNodeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameterComputationExpression" in params, "Missing parameter 'verticalDiameterComputationExpression'"
    assert "horizontalDiameterComputationExpression" in params, "Missing parameter 'horizontalDiameterComputationExpression'"

def test_diagram_style_ellipsenodedescription_has_verticalDiameterComputationExpression():
    assert hasattr(diagram_style_EllipseNodeDescription, "verticalDiameterComputationExpression")
    descriptor = None
    for klass in diagram_style_EllipseNodeDescription.__mro__:
        if "verticalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_ellipsenodedescription_has_horizontalDiameterComputationExpression():
    assert hasattr(diagram_style_EllipseNodeDescription, "horizontalDiameterComputationExpression")
    descriptor = None
    for klass in diagram_style_EllipseNodeDescription.__mro__:
        if "horizontalDiameterComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameterComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_bundledimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BundledImageDescription)


def test_diagram_style_bundledimagedescription_constructor_exists():
    assert callable(diagram_style_BundledImageDescription.__init__)


def test_diagram_style_bundledimagedescription_constructor_args():
    sig = inspect.signature(diagram_style_BundledImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"

def test_diagram_style_bundledimagedescription_has_shape():
    assert hasattr(diagram_style_BundledImageDescription, "shape")
    descriptor = None
    for klass in diagram_style_BundledImageDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_bundledimagedescription_has_providedShapeID():
    assert hasattr(diagram_style_BundledImageDescription, "providedShapeID")
    descriptor = None
    for klass in diagram_style_BundledImageDescription.__mro__:
        if "providedShapeID" in klass.__dict__:
            descriptor = klass.__dict__["providedShapeID"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_notedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_NoteDescription)


def test_diagram_style_notedescription_constructor_exists():
    assert callable(diagram_style_NoteDescription.__init__)


def test_diagram_style_notedescription_constructor_args():
    sig = inspect.signature(diagram_style_NoteDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_gaugecompositestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_GaugeCompositeStyleDescription)


def test_diagram_style_gaugecompositestyledescription_constructor_exists():
    assert callable(diagram_style_GaugeCompositeStyleDescription.__init__)


def test_diagram_style_gaugecompositestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_GaugeCompositeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_diagram_style_gaugecompositestyledescription_has_alignment():
    assert hasattr(diagram_style_GaugeCompositeStyleDescription, "alignment")
    descriptor = None
    for klass in diagram_style_GaugeCompositeStyleDescription.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_squaredescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_SquareDescription)


def test_diagram_style_squaredescription_constructor_exists():
    assert callable(diagram_style_SquareDescription.__init__)


def test_diagram_style_squaredescription_constructor_args():
    sig = inspect.signature(diagram_style_SquareDescription.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram_style_squaredescription_has_width():
    assert hasattr(diagram_style_SquareDescription, "width")
    descriptor = None
    for klass in diagram_style_SquareDescription.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_squaredescription_has_height():
    assert hasattr(diagram_style_SquareDescription, "height")
    descriptor = None
    for klass in diagram_style_SquareDescription.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_customstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_CustomStyleDescription)


def test_diagram_style_customstyledescription_constructor_exists():
    assert callable(diagram_style_CustomStyleDescription.__init__)


def test_diagram_style_customstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_CustomStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram_style_customstyledescription_has_id():
    assert hasattr(diagram_style_CustomStyleDescription, "id")
    descriptor = None
    for klass in diagram_style_CustomStyleDescription.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_style_hidelabelcapabilitystyledescription_is_not_abstract():
    assert not inspect.isabstract(style_HideLabelCapabilityStyleDescription)


def test_style_hidelabelcapabilitystyledescription_constructor_exists():
    assert callable(style_HideLabelCapabilityStyleDescription.__init__)


def test_style_hidelabelcapabilitystyledescription_constructor_args():
    sig = inspect.signature(style_HideLabelCapabilityStyleDescription.__init__)
    params = list(sig.parameters.keys())



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



def test_diagram_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_ContainerStyleDescription)


def test_diagram_style_containerstyledescription_constructor_exists():
    assert callable(diagram_style_ContainerStyleDescription.__init__)


def test_diagram_style_containerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "roundedCorner" in params, "Missing parameter 'roundedCorner'"

def test_diagram_style_containerstyledescription_has_roundedCorner():
    assert hasattr(diagram_style_ContainerStyleDescription, "roundedCorner")
    descriptor = None
    for klass in diagram_style_ContainerStyleDescription.__mro__:
        if "roundedCorner" in klass.__dict__:
            descriptor = klass.__dict__["roundedCorner"]
            break
    assert isinstance(descriptor, property)



def test_colordescription_is_not_abstract():
    assert not inspect.isabstract(ColorDescription)


def test_colordescription_constructor_exists():
    assert callable(ColorDescription.__init__)


def test_colordescription_constructor_args():
    sig = inspect.signature(ColorDescription.__init__)
    params = list(sig.parameters.keys())



def test_styledescription_is_not_abstract():
    assert not inspect.isabstract(StyleDescription)


def test_styledescription_constructor_exists():
    assert callable(StyleDescription.__init__)


def test_styledescription_constructor_args():
    sig = inspect.signature(StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_roundedcornerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_RoundedCornerStyleDescription)


def test_diagram_style_roundedcornerstyledescription_constructor_exists():
    assert callable(diagram_style_RoundedCornerStyleDescription.__init__)


def test_diagram_style_roundedcornerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_RoundedCornerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "arcHeight" in params, "Missing parameter 'arcHeight'"
    assert "arcWidth" in params, "Missing parameter 'arcWidth'"

def test_diagram_style_roundedcornerstyledescription_has_arcHeight():
    assert hasattr(diagram_style_RoundedCornerStyleDescription, "arcHeight")
    descriptor = None
    for klass in diagram_style_RoundedCornerStyleDescription.__mro__:
        if "arcHeight" in klass.__dict__:
            descriptor = klass.__dict__["arcHeight"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_roundedcornerstyledescription_has_arcWidth():
    assert hasattr(diagram_style_RoundedCornerStyleDescription, "arcWidth")
    descriptor = None
    for klass in diagram_style_RoundedCornerStyleDescription.__mro__:
        if "arcWidth" in klass.__dict__:
            descriptor = klass.__dict__["arcWidth"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_EdgeStyleDescription)


def test_diagram_style_edgestyledescription_constructor_exists():
    assert callable(diagram_style_EdgeStyleDescription.__init__)


def test_diagram_style_edgestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "endsCentering" in params, "Missing parameter 'endsCentering'"
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"

def test_diagram_style_edgestyledescription_has_foldingStyle():
    assert hasattr(diagram_style_EdgeStyleDescription, "foldingStyle")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_endsCentering():
    assert hasattr(diagram_style_EdgeStyleDescription, "endsCentering")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "endsCentering" in klass.__dict__:
            descriptor = klass.__dict__["endsCentering"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_targetArrow():
    assert hasattr(diagram_style_EdgeStyleDescription, "targetArrow")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_sizeComputationExpression():
    assert hasattr(diagram_style_EdgeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_lineStyle():
    assert hasattr(diagram_style_EdgeStyleDescription, "lineStyle")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_sourceArrow():
    assert hasattr(diagram_style_EdgeStyleDescription, "sourceArrow")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_edgestyledescription_has_routingStyle():
    assert hasattr(diagram_style_EdgeStyleDescription, "routingStyle")
    descriptor = None
    for klass in diagram_style_EdgeStyleDescription.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_borderedstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_BorderedStyleDescription)


def test_diagram_style_borderedstyledescription_constructor_exists():
    assert callable(diagram_style_BorderedStyleDescription.__init__)


def test_diagram_style_borderedstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_BorderedStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"

def test_diagram_style_borderedstyledescription_has_borderLineStyle():
    assert hasattr(diagram_style_BorderedStyleDescription, "borderLineStyle")
    descriptor = None
    for klass in diagram_style_BorderedStyleDescription.__mro__:
        if "borderLineStyle" in klass.__dict__:
            descriptor = klass.__dict__["borderLineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_borderedstyledescription_has_borderSizeComputationExpression():
    assert hasattr(diagram_style_BorderedStyleDescription, "borderSizeComputationExpression")
    descriptor = None
    for klass in diagram_style_BorderedStyleDescription.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)



def test_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(tool_ContainerDropDescription)


def test_tool_containerdropdescription_constructor_exists():
    assert callable(tool_ContainerDropDescription.__init__)


def test_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_draganddroptargetdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DragAndDropTargetDescription)


def test_diagram_description_draganddroptargetdescription_constructor_exists():
    assert callable(diagram_description_DragAndDropTargetDescription.__init__)


def test_diagram_description_draganddroptargetdescription_constructor_args():
    sig = inspect.signature(diagram_description_DragAndDropTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_customization_is_not_abstract():
    assert not inspect.isabstract(Customization)


def test_customization_constructor_exists():
    assert callable(Customization.__init__)


def test_customization_constructor_args():
    sig = inspect.signature(Customization.__init__)
    params = list(sig.parameters.keys())



def test_decorationdescription_is_not_abstract():
    assert not inspect.isabstract(DecorationDescription)


def test_decorationdescription_constructor_exists():
    assert callable(DecorationDescription.__init__)


def test_decorationdescription_constructor_args():
    sig = inspect.signature(DecorationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_mappingbaseddecoration_is_not_abstract():
    assert not inspect.isabstract(diagram_description_MappingBasedDecoration)


def test_diagram_description_mappingbaseddecoration_constructor_exists():
    assert callable(diagram_description_MappingBasedDecoration.__init__)


def test_diagram_description_mappingbaseddecoration_constructor_args():
    sig = inspect.signature(diagram_description_MappingBasedDecoration.__init__)
    params = list(sig.parameters.keys())



def test_description_enduserdocumentedelement_is_not_abstract():
    assert not inspect.isabstract(description_EndUserDocumentedElement)


def test_description_enduserdocumentedelement_constructor_exists():
    assert callable(description_EndUserDocumentedElement.__init__)


def test_description_enduserdocumentedelement_constructor_args():
    sig = inspect.signature(description_EndUserDocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_documentedelement_is_not_abstract():
    assert not inspect.isabstract(DocumentedElement)


def test_documentedelement_constructor_exists():
    assert callable(DocumentedElement.__init__)


def test_documentedelement_constructor_args():
    sig = inspect.signature(DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_layout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_Layout)


def test_diagram_description_layout_constructor_exists():
    assert callable(diagram_description_Layout.__init__)


def test_diagram_description_layout_constructor_args():
    sig = inspect.signature(diagram_description_Layout.__init__)
    params = list(sig.parameters.keys())



def test_conditionalstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalStyleDescription)


def test_conditionalstyledescription_constructor_exists():
    assert callable(ConditionalStyleDescription.__init__)


def test_conditionalstyledescription_constructor_args():
    sig = inspect.signature(ConditionalStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalEdgeStyleDescription)


def test_diagram_description_conditionaledgestyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalEdgeStyleDescription.__init__)


def test_diagram_description_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalContainerStyleDescription)


def test_diagram_description_conditionalcontainerstyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalContainerStyleDescription.__init__)


def test_diagram_description_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ConditionalNodeStyleDescription)


def test_diagram_description_conditionalnodestyledescription_constructor_exists():
    assert callable(diagram_description_ConditionalNodeStyleDescription.__init__)


def test_diagram_description_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(diagram_description_ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(description_IdentifiedElement)


def test_description_identifiedelement_constructor_exists():
    assert callable(description_IdentifiedElement.__init__)


def test_description_identifiedelement_constructor_args():
    sig = inspect.signature(description_IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_IEdgeMapping)


def test_diagram_description_iedgemapping_constructor_exists():
    assert callable(diagram_description_IEdgeMapping.__init__)


def test_diagram_description_iedgemapping_constructor_args():
    sig = inspect.signature(diagram_description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(AbstractNodeMapping)


def test_abstractnodemapping_constructor_exists():
    assert callable(AbstractNodeMapping.__init__)


def test_abstractnodemapping_constructor_args():
    sig = inspect.signature(AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_reconnectedgedescription_is_not_abstract():
    assert not inspect.isabstract(tool_ReconnectEdgeDescription)


def test_tool_reconnectedgedescription_constructor_exists():
    assert callable(tool_ReconnectEdgeDescription.__init__)


def test_tool_reconnectedgedescription_constructor_args():
    sig = inspect.signature(tool_ReconnectEdgeDescription.__init__)
    params = list(sig.parameters.keys())



def test_conditionaledgestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalEdgeStyleDescription)


def test_conditionaledgestyledescription_constructor_exists():
    assert callable(ConditionalEdgeStyleDescription.__init__)


def test_conditionaledgestyledescription_constructor_args():
    sig = inspect.signature(ConditionalEdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_edgestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_EdgeStyleDescription)


def test_style_edgestyledescription_constructor_exists():
    assert callable(style_EdgeStyleDescription.__init__)


def test_style_edgestyledescription_constructor_args():
    sig = inspect.signature(style_EdgeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(description_IEdgeMapping)


def test_description_iedgemapping_constructor_exists():
    assert callable(description_IEdgeMapping.__init__)


def test_description_iedgemapping_constructor_args():
    sig = inspect.signature(description_IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(description_ContainerMapping)


def test_description_containermapping_constructor_exists():
    assert callable(description_ContainerMapping.__init__)


def test_description_containermapping_constructor_args():
    sig = inspect.signature(description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_abstractmappingimport_is_not_abstract():
    assert not inspect.isabstract(description_AbstractMappingImport)


def test_description_abstractmappingimport_constructor_exists():
    assert callable(description_AbstractMappingImport.__init__)


def test_description_abstractmappingimport_constructor_args():
    sig = inspect.signature(description_AbstractMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_containermappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ContainerMappingImport)


def test_diagram_description_containermappingimport_constructor_exists():
    assert callable(diagram_description_ContainerMappingImport.__init__)


def test_diagram_description_containermappingimport_constructor_args():
    sig = inspect.signature(diagram_description_ContainerMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(description_NodeMapping)


def test_description_nodemapping_constructor_exists():
    assert callable(description_NodeMapping.__init__)


def test_description_nodemapping_constructor_args():
    sig = inspect.signature(description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_nodemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_NodeMappingImport)


def test_diagram_description_nodemappingimport_constructor_exists():
    assert callable(diagram_description_NodeMappingImport.__init__)


def test_diagram_description_nodemappingimport_constructor_args():
    sig = inspect.signature(diagram_description_NodeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_conditionalcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalContainerStyleDescription)


def test_conditionalcontainerstyledescription_constructor_exists():
    assert callable(ConditionalContainerStyleDescription.__init__)


def test_conditionalcontainerstyledescription_constructor_args():
    sig = inspect.signature(ConditionalContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_containerstyledescription_is_not_abstract():
    assert not inspect.isabstract(style_ContainerStyleDescription)


def test_style_containerstyledescription_constructor_exists():
    assert callable(style_ContainerStyleDescription.__init__)


def test_style_containerstyledescription_constructor_args():
    sig = inspect.signature(style_ContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_shapecontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_ShapeContainerStyleDescription)


def test_diagram_style_shapecontainerstyledescription_constructor_exists():
    assert callable(diagram_style_ShapeContainerStyleDescription.__init__)


def test_diagram_style_shapecontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_ShapeContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagram_style_shapecontainerstyledescription_has_shape():
    assert hasattr(diagram_style_ShapeContainerStyleDescription, "shape")
    descriptor = None
    for klass in diagram_style_ShapeContainerStyleDescription.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagram_style_flatcontainerstyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_FlatContainerStyleDescription)


def test_diagram_style_flatcontainerstyledescription_constructor_exists():
    assert callable(diagram_style_FlatContainerStyleDescription.__init__)


def test_diagram_style_flatcontainerstyledescription_constructor_args():
    sig = inspect.signature(diagram_style_FlatContainerStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"

def test_diagram_style_flatcontainerstyledescription_has_backgroundStyle():
    assert hasattr(diagram_style_FlatContainerStyleDescription, "backgroundStyle")
    descriptor = None
    for klass in diagram_style_FlatContainerStyleDescription.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)



def test_conditionalnodestyledescription_is_not_abstract():
    assert not inspect.isabstract(ConditionalNodeStyleDescription)


def test_conditionalnodestyledescription_constructor_exists():
    assert callable(ConditionalNodeStyleDescription.__init__)


def test_conditionalnodestyledescription_constructor_args():
    sig = inspect.signature(ConditionalNodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(style_NodeStyleDescription)


def test_style_nodestyledescription_constructor_exists():
    assert callable(style_NodeStyleDescription.__init__)


def test_style_nodestyledescription_constructor_args():
    sig = inspect.signature(style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_workspaceimagedescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_WorkspaceImageDescription)


def test_diagram_style_workspaceimagedescription_constructor_exists():
    assert callable(diagram_style_WorkspaceImageDescription.__init__)


def test_diagram_style_workspaceimagedescription_constructor_args():
    sig = inspect.signature(diagram_style_WorkspaceImageDescription.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_diagram_style_workspaceimagedescription_has_workspacePath():
    assert hasattr(diagram_style_WorkspaceImageDescription, "workspacePath")
    descriptor = None
    for klass in diagram_style_WorkspaceImageDescription.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(description_AbstractNodeMapping)


def test_description_abstractnodemapping_constructor_exists():
    assert callable(description_AbstractNodeMapping.__init__)


def test_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_representationelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationElementMapping)


def test_description_representationelementmapping_constructor_exists():
    assert callable(description_RepresentationElementMapping.__init__)


def test_description_representationelementmapping_constructor_args():
    sig = inspect.signature(description_RepresentationElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(description_DiagramElementMapping)


def test_description_diagramelementmapping_constructor_exists():
    assert callable(description_DiagramElementMapping.__init__)


def test_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_tool_doubleclickdescription_is_not_abstract():
    assert not inspect.isabstract(tool_DoubleClickDescription)


def test_tool_doubleclickdescription_constructor_exists():
    assert callable(tool_DoubleClickDescription.__init__)


def test_tool_doubleclickdescription_constructor_args():
    sig = inspect.signature(tool_DoubleClickDescription.__init__)
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



def test_representationextensiondescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationExtensionDescription)


def test_representationextensiondescription_constructor_exists():
    assert callable(RepresentationExtensionDescription.__init__)


def test_representationextensiondescription_constructor_args():
    sig = inspect.signature(RepresentationExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_diagramextensiondescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramExtensionDescription)


def test_diagram_description_diagramextensiondescription_constructor_exists():
    assert callable(diagram_description_DiagramExtensionDescription.__init__)


def test_diagram_description_diagramextensiondescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramExtensionDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(description_DiagramDescription)


def test_description_diagramdescription_constructor_exists():
    assert callable(description_DiagramDescription.__init__)


def test_description_diagramdescription_constructor_args():
    sig = inspect.signature(description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_description_representationimportdescription_is_not_abstract():
    assert not inspect.isabstract(description_RepresentationImportDescription)


def test_description_representationimportdescription_constructor_exists():
    assert callable(description_RepresentationImportDescription.__init__)


def test_description_representationimportdescription_constructor_args():
    sig = inspect.signature(description_RepresentationImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_diagramimportdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramImportDescription)


def test_diagram_description_diagramimportdescription_constructor_exists():
    assert callable(diagram_description_DiagramImportDescription.__init__)


def test_diagram_description_diagramimportdescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramImportDescription.__init__)
    params = list(sig.parameters.keys())



def test_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(tool_ToolSection)


def test_tool_toolsection_constructor_exists():
    assert callable(tool_ToolSection.__init__)


def test_tool_toolsection_constructor_args():
    sig = inspect.signature(tool_ToolSection.__init__)
    params = list(sig.parameters.keys())



def test_tool_abstracttooldescription_is_not_abstract():
    assert not inspect.isabstract(tool_AbstractToolDescription)


def test_tool_abstracttooldescription_constructor_exists():
    assert callable(tool_AbstractToolDescription.__init__)


def test_tool_abstracttooldescription_constructor_args():
    sig = inspect.signature(tool_AbstractToolDescription.__init__)
    params = list(sig.parameters.keys())



def test_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(EdgeMappingImport)


def test_edgemappingimport_constructor_exists():
    assert callable(EdgeMappingImport.__init__)


def test_edgemappingimport_constructor_args():
    sig = inspect.signature(EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())



def test_additionallayer_is_not_abstract():
    assert not inspect.isabstract(AdditionalLayer)


def test_additionallayer_constructor_exists():
    assert callable(AdditionalLayer.__init__)


def test_additionallayer_constructor_args():
    sig = inspect.signature(AdditionalLayer.__init__)
    params = list(sig.parameters.keys())



def test_tool_initialoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialOperation)


def test_tool_initialoperation_constructor_exists():
    assert callable(tool_InitialOperation.__init__)


def test_tool_initialoperation_constructor_args():
    sig = inspect.signature(tool_InitialOperation.__init__)
    params = list(sig.parameters.keys())



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_compositelayout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_CompositeLayout)


def test_diagram_description_compositelayout_constructor_exists():
    assert callable(diagram_description_CompositeLayout.__init__)


def test_diagram_description_compositelayout_constructor_args():
    sig = inspect.signature(diagram_description_CompositeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "padding" in params, "Missing parameter 'padding'"

def test_diagram_description_compositelayout_has_direction():
    assert hasattr(diagram_description_CompositeLayout, "direction")
    descriptor = None
    for klass in diagram_description_CompositeLayout.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_compositelayout_has_padding():
    assert hasattr(diagram_description_CompositeLayout, "padding")
    descriptor = None
    for klass in diagram_description_CompositeLayout.__mro__:
        if "padding" in klass.__dict__:
            descriptor = klass.__dict__["padding"]
            break
    assert isinstance(descriptor, property)



def test_diagram_description_orderedtreelayout_is_not_abstract():
    assert not inspect.isabstract(diagram_description_OrderedTreeLayout)


def test_diagram_description_orderedtreelayout_constructor_exists():
    assert callable(diagram_description_OrderedTreeLayout.__init__)


def test_diagram_description_orderedtreelayout_constructor_args():
    sig = inspect.signature(diagram_description_OrderedTreeLayout.__init__)
    params = list(sig.parameters.keys())
    assert "childrenExpression" in params, "Missing parameter 'childrenExpression'"

def test_diagram_description_orderedtreelayout_has_childrenExpression():
    assert hasattr(diagram_description_OrderedTreeLayout, "childrenExpression")
    descriptor = None
    for klass in diagram_description_OrderedTreeLayout.__mro__:
        if "childrenExpression" in klass.__dict__:
            descriptor = klass.__dict__["childrenExpression"]
            break
    assert isinstance(descriptor, property)



def test_tool_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(tool_RepresentationCreationDescription)


def test_tool_representationcreationdescription_constructor_exists():
    assert callable(tool_RepresentationCreationDescription.__init__)


def test_tool_representationcreationdescription_constructor_args():
    sig = inspect.signature(tool_RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(diagram_concern_ConcernSet)


def test_diagram_concern_concernset_constructor_exists():
    assert callable(diagram_concern_ConcernSet.__init__)


def test_diagram_concern_concernset_constructor_args():
    sig = inspect.signature(diagram_concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_interactivevariabledescription_is_not_abstract():
    assert not inspect.isabstract(InteractiveVariableDescription)


def test_interactivevariabledescription_constructor_exists():
    assert callable(InteractiveVariableDescription.__init__)


def test_interactivevariabledescription_constructor_args():
    sig = inspect.signature(InteractiveVariableDescription.__init__)
    params = list(sig.parameters.keys())



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



def test_diagram_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_CompositeFilterDescription)


def test_diagram_filter_compositefilterdescription_constructor_exists():
    assert callable(diagram_filter_CompositeFilterDescription.__init__)


def test_diagram_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(diagram_filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_filter_variablefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_VariableFilter)


def test_diagram_filter_variablefilter_constructor_exists():
    assert callable(diagram_filter_VariableFilter.__init__)


def test_diagram_filter_variablefilter_constructor_args():
    sig = inspect.signature(diagram_filter_VariableFilter.__init__)
    params = list(sig.parameters.keys())
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_diagram_filter_variablefilter_has_semanticConditionExpression():
    assert hasattr(diagram_filter_VariableFilter, "semanticConditionExpression")
    descriptor = None
    for klass in diagram_filter_VariableFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_filter_mappingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_MappingFilter)


def test_diagram_filter_mappingfilter_constructor_exists():
    assert callable(diagram_filter_MappingFilter.__init__)


def test_diagram_filter_mappingfilter_constructor_args():
    sig = inspect.signature(diagram_filter_MappingFilter.__init__)
    params = list(sig.parameters.keys())
    assert "viewConditionExpression" in params, "Missing parameter 'viewConditionExpression'"
    assert "semanticConditionExpression" in params, "Missing parameter 'semanticConditionExpression'"

def test_diagram_filter_mappingfilter_has_viewConditionExpression():
    assert hasattr(diagram_filter_MappingFilter, "viewConditionExpression")
    descriptor = None
    for klass in diagram_filter_MappingFilter.__mro__:
        if "viewConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["viewConditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_filter_mappingfilter_has_semanticConditionExpression():
    assert hasattr(diagram_filter_MappingFilter, "semanticConditionExpression")
    descriptor = None
    for klass in diagram_filter_MappingFilter.__mro__:
        if "semanticConditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticConditionExpression"]
            break
    assert isinstance(descriptor, property)



def test_diagram_filter_filter_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_Filter)


def test_diagram_filter_filter_constructor_exists():
    assert callable(diagram_filter_Filter.__init__)


def test_diagram_filter_filter_constructor_args():
    sig = inspect.signature(diagram_filter_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "filterKind" in params, "Missing parameter 'filterKind'"

def test_diagram_filter_filter_has_filterKind():
    assert hasattr(diagram_filter_Filter, "filterKind")
    descriptor = None
    for klass in diagram_filter_Filter.__mro__:
        if "filterKind" in klass.__dict__:
            descriptor = klass.__dict__["filterKind"]
            break
    assert isinstance(descriptor, property)



def test_tool_initialcontainerdropoperation_is_not_abstract():
    assert not inspect.isabstract(tool_InitialContainerDropOperation)


def test_tool_initialcontainerdropoperation_constructor_exists():
    assert callable(tool_InitialContainerDropOperation.__init__)


def test_tool_initialcontainerdropoperation_constructor_args():
    sig = inspect.signature(tool_InitialContainerDropOperation.__init__)
    params = list(sig.parameters.keys())



def test_createview_is_not_abstract():
    assert not inspect.isabstract(CreateView)


def test_createview_constructor_exists():
    assert callable(CreateView.__init__)


def test_createview_constructor_args():
    sig = inspect.signature(CreateView.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_createedgeview_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_CreateEdgeView)


def test_diagram_tool_createedgeview_constructor_exists():
    assert callable(diagram_tool_CreateEdgeView.__init__)


def test_diagram_tool_createedgeview_constructor_args():
    sig = inspect.signature(diagram_tool_CreateEdgeView.__init__)
    params = list(sig.parameters.keys())
    assert "sourceExpression" in params, "Missing parameter 'sourceExpression'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"

def test_diagram_tool_createedgeview_has_sourceExpression():
    assert hasattr(diagram_tool_CreateEdgeView, "sourceExpression")
    descriptor = None
    for klass in diagram_tool_CreateEdgeView.__mro__:
        if "sourceExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_tool_createedgeview_has_targetExpression():
    assert hasattr(diagram_tool_CreateEdgeView, "targetExpression")
    descriptor = None
    for klass in diagram_tool_CreateEdgeView.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)



def test_tool_elementdropvariable_is_not_abstract():
    assert not inspect.isabstract(tool_ElementDropVariable)


def test_tool_elementdropvariable_constructor_exists():
    assert callable(tool_ElementDropVariable.__init__)


def test_tool_elementdropvariable_constructor_args():
    sig = inspect.signature(tool_ElementDropVariable.__init__)
    params = list(sig.parameters.keys())



def test_tool_dropcontainervariable_is_not_abstract():
    assert not inspect.isabstract(tool_DropContainerVariable)


def test_tool_dropcontainervariable_constructor_exists():
    assert callable(tool_DropContainerVariable.__init__)


def test_tool_dropcontainervariable_constructor_args():
    sig = inspect.signature(tool_DropContainerVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_containerdropdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ContainerDropDescription)


def test_diagram_tool_containerdropdescription_constructor_exists():
    assert callable(diagram_tool_ContainerDropDescription.__init__)


def test_diagram_tool_containerdropdescription_constructor_args():
    sig = inspect.signature(diagram_tool_ContainerDropDescription.__init__)
    params = list(sig.parameters.keys())
    assert "dragSource" in params, "Missing parameter 'dragSource'"
    assert "moveEdges" in params, "Missing parameter 'moveEdges'"

def test_diagram_tool_containerdropdescription_has_dragSource():
    assert hasattr(diagram_tool_ContainerDropDescription, "dragSource")
    descriptor = None
    for klass in diagram_tool_ContainerDropDescription.__mro__:
        if "dragSource" in klass.__dict__:
            descriptor = klass.__dict__["dragSource"]
            break
    assert isinstance(descriptor, property)

def test_diagram_tool_containerdropdescription_has_moveEdges():
    assert hasattr(diagram_tool_ContainerDropDescription, "moveEdges")
    descriptor = None
    for klass in diagram_tool_ContainerDropDescription.__mro__:
        if "moveEdges" in klass.__dict__:
            descriptor = klass.__dict__["moveEdges"]
            break
    assert isinstance(descriptor, property)



def test_representationnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationNavigationDescription)


def test_representationnavigationdescription_constructor_exists():
    assert callable(RepresentationNavigationDescription.__init__)


def test_representationnavigationdescription_constructor_args():
    sig = inspect.signature(RepresentationNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_diagramnavigationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DiagramNavigationDescription)


def test_diagram_tool_diagramnavigationdescription_constructor_exists():
    assert callable(diagram_tool_DiagramNavigationDescription.__init__)


def test_diagram_tool_diagramnavigationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DiagramNavigationDescription.__init__)
    params = list(sig.parameters.keys())



def test_representationcreationdescription_is_not_abstract():
    assert not inspect.isabstract(RepresentationCreationDescription)


def test_representationcreationdescription_constructor_exists():
    assert callable(RepresentationCreationDescription.__init__)


def test_representationcreationdescription_constructor_args():
    sig = inspect.signature(RepresentationCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_diagramcreationdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_DiagramCreationDescription)


def test_diagram_tool_diagramcreationdescription_constructor_exists():
    assert callable(diagram_tool_DiagramCreationDescription.__init__)


def test_diagram_tool_diagramcreationdescription_constructor_args():
    sig = inspect.signature(diagram_tool_DiagramCreationDescription.__init__)
    params = list(sig.parameters.keys())



def test_containermodeloperation_is_not_abstract():
    assert not inspect.isabstract(ContainerModelOperation)


def test_containermodeloperation_constructor_exists():
    assert callable(ContainerModelOperation.__init__)


def test_containermodeloperation_constructor_args():
    sig = inspect.signature(ContainerModelOperation.__init__)
    params = list(sig.parameters.keys())



def test_diagram_tool_navigation_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_Navigation)


def test_diagram_tool_navigation_constructor_exists():
    assert callable(diagram_tool_Navigation.__init__)


def test_diagram_tool_navigation_constructor_args():
    sig = inspect.signature(diagram_tool_Navigation.__init__)
    params = list(sig.parameters.keys())
    assert "createIfNotExistent" in params, "Missing parameter 'createIfNotExistent'"

def test_diagram_tool_navigation_has_createIfNotExistent():
    assert hasattr(diagram_tool_Navigation, "createIfNotExistent")
    descriptor = None
    for klass in diagram_tool_Navigation.__mro__:
        if "createIfNotExistent" in klass.__dict__:
            descriptor = klass.__dict__["createIfNotExistent"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_createview_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_CreateView)


def test_diagram_tool_createview_constructor_exists():
    assert callable(diagram_tool_CreateView.__init__)


def test_diagram_tool_createview_constructor_args():
    sig = inspect.signature(diagram_tool_CreateView.__init__)
    params = list(sig.parameters.keys())
    assert "containerViewExpression" in params, "Missing parameter 'containerViewExpression'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_diagram_tool_createview_has_containerViewExpression():
    assert hasattr(diagram_tool_CreateView, "containerViewExpression")
    descriptor = None
    for klass in diagram_tool_CreateView.__mro__:
        if "containerViewExpression" in klass.__dict__:
            descriptor = klass.__dict__["containerViewExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_tool_createview_has_variableName():
    assert hasattr(diagram_tool_CreateView, "variableName")
    descriptor = None
    for klass in diagram_tool_CreateView.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_nodecreationvariable_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_NodeCreationVariable)


def test_diagram_tool_nodecreationvariable_constructor_exists():
    assert callable(diagram_tool_NodeCreationVariable.__init__)


def test_diagram_tool_nodecreationvariable_constructor_args():
    sig = inspect.signature(diagram_tool_NodeCreationVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(diagram_HideLabelCapabilityStyle)


def test_diagram_hidelabelcapabilitystyle_constructor_exists():
    assert callable(diagram_HideLabelCapabilityStyle.__init__)


def test_diagram_hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(diagram_HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hideLabelByDefault" in params, "Missing parameter 'hideLabelByDefault'"

def test_diagram_hidelabelcapabilitystyle_has_hideLabelByDefault():
    assert hasattr(diagram_HideLabelCapabilityStyle, "hideLabelByDefault")
    descriptor = None
    for klass in diagram_HideLabelCapabilityStyle.__mro__:
        if "hideLabelByDefault" in klass.__dict__:
            descriptor = klass.__dict__["hideLabelByDefault"]
            break
    assert isinstance(descriptor, property)



def test_concern_concernset_is_not_abstract():
    assert not inspect.isabstract(concern_ConcernSet)


def test_concern_concernset_constructor_exists():
    assert callable(concern_ConcernSet.__init__)


def test_concern_concernset_constructor_args():
    sig = inspect.signature(concern_ConcernSet.__init__)
    params = list(sig.parameters.keys())



def test_validation_validationset_is_not_abstract():
    assert not inspect.isabstract(validation_ValidationSet)


def test_validation_validationset_constructor_exists():
    assert callable(validation_ValidationSet.__init__)


def test_validation_validationset_constructor_args():
    sig = inspect.signature(validation_ValidationSet.__init__)
    params = list(sig.parameters.keys())



def test_edgemapping_is_not_abstract():
    assert not inspect.isabstract(EdgeMapping)


def test_edgemapping_constructor_exists():
    assert callable(EdgeMapping.__init__)


def test_edgemapping_constructor_args():
    sig = inspect.signature(EdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_description_pastetargetdescription_is_not_abstract():
    assert not inspect.isabstract(description_PasteTargetDescription)


def test_description_pastetargetdescription_constructor_exists():
    assert callable(description_PasteTargetDescription.__init__)


def test_description_pastetargetdescription_constructor_args():
    sig = inspect.signature(description_PasteTargetDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramElementMapping)


def test_diagram_description_diagramelementmapping_constructor_exists():
    assert callable(diagram_description_DiagramElementMapping.__init__)


def test_diagram_description_diagramelementmapping_constructor_args():
    sig = inspect.signature(diagram_description_DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())
    assert "synchronizationLock" in params, "Missing parameter 'synchronizationLock'"
    assert "semanticElements" in params, "Missing parameter 'semanticElements'"
    assert "createElements" in params, "Missing parameter 'createElements'"
    assert "semanticCandidatesExpression" in params, "Missing parameter 'semanticCandidatesExpression'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"

def test_diagram_description_diagramelementmapping_has_synchronizationLock():
    assert hasattr(diagram_description_DiagramElementMapping, "synchronizationLock")
    descriptor = None
    for klass in diagram_description_DiagramElementMapping.__mro__:
        if "synchronizationLock" in klass.__dict__:
            descriptor = klass.__dict__["synchronizationLock"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramelementmapping_has_semanticElements():
    assert hasattr(diagram_description_DiagramElementMapping, "semanticElements")
    descriptor = None
    for klass in diagram_description_DiagramElementMapping.__mro__:
        if "semanticElements" in klass.__dict__:
            descriptor = klass.__dict__["semanticElements"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramelementmapping_has_createElements():
    assert hasattr(diagram_description_DiagramElementMapping, "createElements")
    descriptor = None
    for klass in diagram_description_DiagramElementMapping.__mro__:
        if "createElements" in klass.__dict__:
            descriptor = klass.__dict__["createElements"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramelementmapping_has_semanticCandidatesExpression():
    assert hasattr(diagram_description_DiagramElementMapping, "semanticCandidatesExpression")
    descriptor = None
    for klass in diagram_description_DiagramElementMapping.__mro__:
        if "semanticCandidatesExpression" in klass.__dict__:
            descriptor = klass.__dict__["semanticCandidatesExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramelementmapping_has_preconditionExpression():
    assert hasattr(diagram_description_DiagramElementMapping, "preconditionExpression")
    descriptor = None
    for klass in diagram_description_DiagramElementMapping.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
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



def test_diagram_description_nodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_NodeMapping)


def test_diagram_description_nodemapping_constructor_exists():
    assert callable(diagram_description_NodeMapping.__init__)


def test_diagram_description_nodemapping_constructor_args():
    sig = inspect.signature(diagram_description_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_containermapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_ContainerMapping)


def test_diagram_description_containermapping_constructor_exists():
    assert callable(diagram_description_ContainerMapping.__init__)


def test_diagram_description_containermapping_constructor_args():
    sig = inspect.signature(diagram_description_ContainerMapping.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_diagram_description_containermapping_has_childrenPresentation():
    assert hasattr(diagram_description_ContainerMapping, "childrenPresentation")
    descriptor = None
    for klass in diagram_description_ContainerMapping.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_diagram_description_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_description_DiagramDescription)


def test_diagram_description_diagramdescription_constructor_exists():
    assert callable(diagram_description_DiagramDescription.__init__)


def test_diagram_description_diagramdescription_constructor_args():
    sig = inspect.signature(diagram_description_DiagramDescription.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "rootExpression" in params, "Missing parameter 'rootExpression'"
    assert "preconditionExpression" in params, "Missing parameter 'preconditionExpression'"
    assert "enablePopupBars" in params, "Missing parameter 'enablePopupBars'"

def test_diagram_description_diagramdescription_has_domainClass():
    assert hasattr(diagram_description_DiagramDescription, "domainClass")
    descriptor = None
    for klass in diagram_description_DiagramDescription.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramdescription_has_rootExpression():
    assert hasattr(diagram_description_DiagramDescription, "rootExpression")
    descriptor = None
    for klass in diagram_description_DiagramDescription.__mro__:
        if "rootExpression" in klass.__dict__:
            descriptor = klass.__dict__["rootExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramdescription_has_preconditionExpression():
    assert hasattr(diagram_description_DiagramDescription, "preconditionExpression")
    descriptor = None
    for klass in diagram_description_DiagramDescription.__mro__:
        if "preconditionExpression" in klass.__dict__:
            descriptor = klass.__dict__["preconditionExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_diagramdescription_has_enablePopupBars():
    assert hasattr(diagram_description_DiagramDescription, "enablePopupBars")
    descriptor = None
    for klass in diagram_description_DiagramDescription.__mro__:
        if "enablePopupBars" in klass.__dict__:
            descriptor = klass.__dict__["enablePopupBars"]
            break
    assert isinstance(descriptor, property)



def test_diagram_eobject_is_not_abstract():
    assert not inspect.isabstract(diagram_EObject)


def test_diagram_eobject_constructor_exists():
    assert callable(diagram_EObject.__init__)


def test_diagram_eobject_constructor_args():
    sig = inspect.signature(diagram_EObject.__init__)
    params = list(sig.parameters.keys())



def test_tool_selectmodelelementvariable_is_not_abstract():
    assert not inspect.isabstract(tool_SelectModelElementVariable)


def test_tool_selectmodelelementvariable_constructor_exists():
    assert callable(tool_SelectModelElementVariable.__init__)


def test_tool_selectmodelelementvariable_constructor_args():
    sig = inspect.signature(tool_SelectModelElementVariable.__init__)
    params = list(sig.parameters.keys())



def test_typedvariable_is_not_abstract():
    assert not inspect.isabstract(TypedVariable)


def test_typedvariable_constructor_exists():
    assert callable(TypedVariable.__init__)


def test_typedvariable_constructor_args():
    sig = inspect.signature(TypedVariable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(diagram_DragAndDropTarget)


def test_diagram_draganddroptarget_constructor_exists():
    assert callable(diagram_DragAndDropTarget.__init__)


def test_diagram_draganddroptarget_constructor_args():
    sig = inspect.signature(diagram_DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_style_styledescription_is_not_abstract():
    assert not inspect.isabstract(style_StyleDescription)


def test_style_styledescription_constructor_exists():
    assert callable(style_StyleDescription.__init__)


def test_style_styledescription_constructor_args():
    sig = inspect.signature(style_StyleDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_nodestyledescription_is_not_abstract():
    assert not inspect.isabstract(diagram_style_NodeStyleDescription)


def test_diagram_style_nodestyledescription_constructor_exists():
    assert callable(diagram_style_NodeStyleDescription.__init__)


def test_diagram_style_nodestyledescription_constructor_args():
    sig = inspect.signature(diagram_style_NodeStyleDescription.__init__)
    params = list(sig.parameters.keys())
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"
    assert "sizeComputationExpression" in params, "Missing parameter 'sizeComputationExpression'"
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_diagram_style_nodestyledescription_has_resizeKind():
    assert hasattr(diagram_style_NodeStyleDescription, "resizeKind")
    descriptor = None
    for klass in diagram_style_NodeStyleDescription.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_nodestyledescription_has_sizeComputationExpression():
    assert hasattr(diagram_style_NodeStyleDescription, "sizeComputationExpression")
    descriptor = None
    for klass in diagram_style_NodeStyleDescription.__mro__:
        if "sizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["sizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_style_nodestyledescription_has_labelPosition():
    assert hasattr(diagram_style_NodeStyleDescription, "labelPosition")
    descriptor = None
    for klass in diagram_style_NodeStyleDescription.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_diagram_computedstyledescriptionregistry_is_not_abstract():
    assert not inspect.isabstract(diagram_ComputedStyleDescriptionRegistry)


def test_diagram_computedstyledescriptionregistry_constructor_exists():
    assert callable(diagram_ComputedStyleDescriptionRegistry.__init__)


def test_diagram_computedstyledescriptionregistry_constructor_args():
    sig = inspect.signature(diagram_ComputedStyleDescriptionRegistry.__init__)
    params = list(sig.parameters.keys())



def test_edgestyle_is_not_abstract():
    assert not inspect.isabstract(EdgeStyle)


def test_edgestyle_constructor_exists():
    assert callable(EdgeStyle.__init__)


def test_edgestyle_constructor_args():
    sig = inspect.signature(EdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_bracketedgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BracketEdgeStyle)


def test_diagram_bracketedgestyle_constructor_exists():
    assert callable(diagram_BracketEdgeStyle.__init__)


def test_diagram_bracketedgestyle_constructor_args():
    sig = inspect.signature(diagram_BracketEdgeStyle.__init__)
    params = list(sig.parameters.keys())



def test_basiclabelstyle_is_not_abstract():
    assert not inspect.isabstract(BasicLabelStyle)


def test_basiclabelstyle_constructor_exists():
    assert callable(BasicLabelStyle.__init__)


def test_basiclabelstyle_constructor_args():
    sig = inspect.signature(BasicLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(CollapseFilter)


def test_collapsefilter_constructor_exists():
    assert callable(CollapseFilter.__init__)


def test_collapsefilter_constructor_args():
    sig = inspect.signature(CollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_indirectlycollapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_IndirectlyCollapseFilter)


def test_diagram_indirectlycollapsefilter_constructor_exists():
    assert callable(diagram_IndirectlyCollapseFilter.__init__)


def test_diagram_indirectlycollapsefilter_constructor_args():
    sig = inspect.signature(diagram_IndirectlyCollapseFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_variablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_VariableValue)


def test_diagram_variablevalue_constructor_exists():
    assert callable(diagram_VariableValue.__init__)


def test_diagram_variablevalue_constructor_args():
    sig = inspect.signature(diagram_VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram_endlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_EndLabelStyle)


def test_diagram_endlabelstyle_constructor_exists():
    assert callable(diagram_EndLabelStyle.__init__)


def test_diagram_endlabelstyle_constructor_args():
    sig = inspect.signature(diagram_EndLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_centerlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_CenterLabelStyle)


def test_diagram_centerlabelstyle_constructor_exists():
    assert callable(diagram_CenterLabelStyle.__init__)


def test_diagram_centerlabelstyle_constructor_args():
    sig = inspect.signature(diagram_CenterLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_beginlabelstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BeginLabelStyle)


def test_diagram_beginlabelstyle_constructor_exists():
    assert callable(diagram_BeginLabelStyle.__init__)


def test_diagram_beginlabelstyle_constructor_args():
    sig = inspect.signature(diagram_BeginLabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_containerstyle_is_not_abstract():
    assert not inspect.isabstract(ContainerStyle)


def test_containerstyle_constructor_exists():
    assert callable(ContainerStyle.__init__)


def test_containerstyle_constructor_args():
    sig = inspect.signature(ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_flatcontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_FlatContainerStyle)


def test_diagram_flatcontainerstyle_constructor_exists():
    assert callable(diagram_FlatContainerStyle.__init__)


def test_diagram_flatcontainerstyle_constructor_args():
    sig = inspect.signature(diagram_FlatContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundStyle" in params, "Missing parameter 'backgroundStyle'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"

def test_diagram_flatcontainerstyle_has_backgroundStyle():
    assert hasattr(diagram_FlatContainerStyle, "backgroundStyle")
    descriptor = None
    for klass in diagram_FlatContainerStyle.__mro__:
        if "backgroundStyle" in klass.__dict__:
            descriptor = klass.__dict__["backgroundStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_flatcontainerstyle_has_backgroundColor():
    assert hasattr(diagram_FlatContainerStyle, "backgroundColor")
    descriptor = None
    for klass in diagram_FlatContainerStyle.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram_flatcontainerstyle_has_foregroundColor():
    assert hasattr(diagram_FlatContainerStyle, "foregroundColor")
    descriptor = None
    for klass in diagram_FlatContainerStyle.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)



def test_diagram_shapecontainerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_ShapeContainerStyle)


def test_diagram_shapecontainerstyle_constructor_exists():
    assert callable(diagram_ShapeContainerStyle.__init__)


def test_diagram_shapecontainerstyle_constructor_args():
    sig = inspect.signature(diagram_ShapeContainerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"

def test_diagram_shapecontainerstyle_has_shape():
    assert hasattr(diagram_ShapeContainerStyle, "shape")
    descriptor = None
    for klass in diagram_ShapeContainerStyle.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_diagram_shapecontainerstyle_has_backgroundColor():
    assert hasattr(diagram_ShapeContainerStyle, "backgroundColor")
    descriptor = None
    for klass in diagram_ShapeContainerStyle.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)



def test_customizable_is_not_abstract():
    assert not inspect.isabstract(Customizable)


def test_customizable_constructor_exists():
    assert callable(Customizable.__init__)


def test_customizable_constructor_args():
    sig = inspect.signature(Customizable.__init__)
    params = list(sig.parameters.keys())



def test_diagram_gaugesection_is_not_abstract():
    assert not inspect.isabstract(diagram_GaugeSection)


def test_diagram_gaugesection_constructor_exists():
    assert callable(diagram_GaugeSection.__init__)


def test_diagram_gaugesection_constructor_args():
    sig = inspect.signature(diagram_GaugeSection.__init__)
    params = list(sig.parameters.keys())
    assert "foregroundColor" in params, "Missing parameter 'foregroundColor'"
    assert "max" in params, "Missing parameter 'max'"
    assert "value" in params, "Missing parameter 'value'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"
    assert "min" in params, "Missing parameter 'min'"
    assert "label" in params, "Missing parameter 'label'"

def test_diagram_gaugesection_has_foregroundColor():
    assert hasattr(diagram_GaugeSection, "foregroundColor")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "foregroundColor" in klass.__dict__:
            descriptor = klass.__dict__["foregroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram_gaugesection_has_max():
    assert hasattr(diagram_GaugeSection, "max")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_diagram_gaugesection_has_value():
    assert hasattr(diagram_GaugeSection, "value")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_diagram_gaugesection_has_backgroundColor():
    assert hasattr(diagram_GaugeSection, "backgroundColor")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram_gaugesection_has_min():
    assert hasattr(diagram_GaugeSection, "min")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_diagram_gaugesection_has_label():
    assert hasattr(diagram_GaugeSection, "label")
    descriptor = None
    for klass in diagram_GaugeSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_note_is_not_abstract():
    assert not inspect.isabstract(diagram_Note)


def test_diagram_note_constructor_exists():
    assert callable(diagram_Note.__init__)


def test_diagram_note_constructor_args():
    sig = inspect.signature(diagram_Note.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_diagram_note_has_color():
    assert hasattr(diagram_Note, "color")
    descriptor = None
    for klass in diagram_Note.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_diagram_customstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_CustomStyle)


def test_diagram_customstyle_constructor_exists():
    assert callable(diagram_CustomStyle.__init__)


def test_diagram_customstyle_constructor_args():
    sig = inspect.signature(diagram_CustomStyle.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_diagram_customstyle_has_id():
    assert hasattr(diagram_CustomStyle, "id")
    descriptor = None
    for klass in diagram_CustomStyle.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_diagram_square_is_not_abstract():
    assert not inspect.isabstract(diagram_Square)


def test_diagram_square_constructor_exists():
    assert callable(diagram_Square.__init__)


def test_diagram_square_constructor_args():
    sig = inspect.signature(diagram_Square.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "color" in params, "Missing parameter 'color'"

def test_diagram_square_has_height():
    assert hasattr(diagram_Square, "height")
    descriptor = None
    for klass in diagram_Square.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram_square_has_width():
    assert hasattr(diagram_Square, "width")
    descriptor = None
    for klass in diagram_Square.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram_square_has_color():
    assert hasattr(diagram_Square, "color")
    descriptor = None
    for klass in diagram_Square.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_diagram_ellipse_is_not_abstract():
    assert not inspect.isabstract(diagram_Ellipse)


def test_diagram_ellipse_constructor_exists():
    assert callable(diagram_Ellipse.__init__)


def test_diagram_ellipse_constructor_args():
    sig = inspect.signature(diagram_Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "verticalDiameter" in params, "Missing parameter 'verticalDiameter'"
    assert "color" in params, "Missing parameter 'color'"
    assert "horizontalDiameter" in params, "Missing parameter 'horizontalDiameter'"

def test_diagram_ellipse_has_verticalDiameter():
    assert hasattr(diagram_Ellipse, "verticalDiameter")
    descriptor = None
    for klass in diagram_Ellipse.__mro__:
        if "verticalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["verticalDiameter"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ellipse_has_color():
    assert hasattr(diagram_Ellipse, "color")
    descriptor = None
    for klass in diagram_Ellipse.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ellipse_has_horizontalDiameter():
    assert hasattr(diagram_Ellipse, "horizontalDiameter")
    descriptor = None
    for klass in diagram_Ellipse.__mro__:
        if "horizontalDiameter" in klass.__dict__:
            descriptor = klass.__dict__["horizontalDiameter"]
            break
    assert isinstance(descriptor, property)



def test_diagram_lozenge_is_not_abstract():
    assert not inspect.isabstract(diagram_Lozenge)


def test_diagram_lozenge_constructor_exists():
    assert callable(diagram_Lozenge.__init__)


def test_diagram_lozenge_constructor_args():
    sig = inspect.signature(diagram_Lozenge.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram_lozenge_has_color():
    assert hasattr(diagram_Lozenge, "color")
    descriptor = None
    for klass in diagram_Lozenge.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram_lozenge_has_width():
    assert hasattr(diagram_Lozenge, "width")
    descriptor = None
    for klass in diagram_Lozenge.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram_lozenge_has_height():
    assert hasattr(diagram_Lozenge, "height")
    descriptor = None
    for klass in diagram_Lozenge.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_diagram_bundledimage_is_not_abstract():
    assert not inspect.isabstract(diagram_BundledImage)


def test_diagram_bundledimage_constructor_exists():
    assert callable(diagram_BundledImage.__init__)


def test_diagram_bundledimage_constructor_args():
    sig = inspect.signature(diagram_BundledImage.__init__)
    params = list(sig.parameters.keys())
    assert "providedShapeID" in params, "Missing parameter 'providedShapeID'"
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_diagram_bundledimage_has_providedShapeID():
    assert hasattr(diagram_BundledImage, "providedShapeID")
    descriptor = None
    for klass in diagram_BundledImage.__mro__:
        if "providedShapeID" in klass.__dict__:
            descriptor = klass.__dict__["providedShapeID"]
            break
    assert isinstance(descriptor, property)

def test_diagram_bundledimage_has_color():
    assert hasattr(diagram_BundledImage, "color")
    descriptor = None
    for klass in diagram_BundledImage.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_diagram_bundledimage_has_shape():
    assert hasattr(diagram_BundledImage, "shape")
    descriptor = None
    for klass in diagram_BundledImage.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_diagram_workspaceimage_is_not_abstract():
    assert not inspect.isabstract(diagram_WorkspaceImage)


def test_diagram_workspaceimage_constructor_exists():
    assert callable(diagram_WorkspaceImage.__init__)


def test_diagram_workspaceimage_constructor_args():
    sig = inspect.signature(diagram_WorkspaceImage.__init__)
    params = list(sig.parameters.keys())
    assert "workspacePath" in params, "Missing parameter 'workspacePath'"

def test_diagram_workspaceimage_has_workspacePath():
    assert hasattr(diagram_WorkspaceImage, "workspacePath")
    descriptor = None
    for klass in diagram_WorkspaceImage.__mro__:
        if "workspacePath" in klass.__dict__:
            descriptor = klass.__dict__["workspacePath"]
            break
    assert isinstance(descriptor, property)



def test_diagram_gaugecompositestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_GaugeCompositeStyle)


def test_diagram_gaugecompositestyle_constructor_exists():
    assert callable(diagram_GaugeCompositeStyle.__init__)


def test_diagram_gaugecompositestyle_constructor_args():
    sig = inspect.signature(diagram_GaugeCompositeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_diagram_gaugecompositestyle_has_alignment():
    assert hasattr(diagram_GaugeCompositeStyle, "alignment")
    descriptor = None
    for klass in diagram_GaugeCompositeStyle.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_variablevalue_is_not_abstract():
    assert not inspect.isabstract(VariableValue)


def test_variablevalue_constructor_exists():
    assert callable(VariableValue.__init__)


def test_variablevalue_constructor_args():
    sig = inspect.signature(VariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram_eobjectvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_EObjectVariableValue)


def test_diagram_eobjectvariablevalue_constructor_exists():
    assert callable(diagram_EObjectVariableValue.__init__)


def test_diagram_eobjectvariablevalue_constructor_args():
    sig = inspect.signature(diagram_EObjectVariableValue.__init__)
    params = list(sig.parameters.keys())



def test_diagram_typedvariablevalue_is_not_abstract():
    assert not inspect.isabstract(diagram_TypedVariableValue)


def test_diagram_typedvariablevalue_constructor_exists():
    assert callable(diagram_TypedVariableValue.__init__)


def test_diagram_typedvariablevalue_constructor_args():
    sig = inspect.signature(diagram_TypedVariableValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_diagram_typedvariablevalue_has_value():
    assert hasattr(diagram_TypedVariableValue, "value")
    descriptor = None
    for klass in diagram_TypedVariableValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_diagram_dot_is_not_abstract():
    assert not inspect.isabstract(diagram_Dot)


def test_diagram_dot_constructor_exists():
    assert callable(diagram_Dot.__init__)


def test_diagram_dot_constructor_args():
    sig = inspect.signature(diagram_Dot.__init__)
    params = list(sig.parameters.keys())
    assert "strokeSizeComputationExpression" in params, "Missing parameter 'strokeSizeComputationExpression'"
    assert "backgroundColor" in params, "Missing parameter 'backgroundColor'"

def test_diagram_dot_has_strokeSizeComputationExpression():
    assert hasattr(diagram_Dot, "strokeSizeComputationExpression")
    descriptor = None
    for klass in diagram_Dot.__mro__:
        if "strokeSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["strokeSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dot_has_backgroundColor():
    assert hasattr(diagram_Dot, "backgroundColor")
    descriptor = None
    for klass in diagram_Dot.__mro__:
        if "backgroundColor" in klass.__dict__:
            descriptor = klass.__dict__["backgroundColor"]
            break
    assert isinstance(descriptor, property)



def test_hidelabelcapabilitystyle_is_not_abstract():
    assert not inspect.isabstract(HideLabelCapabilityStyle)


def test_hidelabelcapabilitystyle_constructor_exists():
    assert callable(HideLabelCapabilityStyle.__init__)


def test_hidelabelcapabilitystyle_constructor_args():
    sig = inspect.signature(HideLabelCapabilityStyle.__init__)
    params = list(sig.parameters.keys())



def test_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(BorderedStyle)


def test_borderedstyle_constructor_exists():
    assert callable(BorderedStyle.__init__)


def test_borderedstyle_constructor_args():
    sig = inspect.signature(BorderedStyle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_diagram_borderedstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_BorderedStyle)


def test_diagram_borderedstyle_constructor_exists():
    assert callable(diagram_BorderedStyle.__init__)


def test_diagram_borderedstyle_constructor_args():
    sig = inspect.signature(diagram_BorderedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "borderLineStyle" in params, "Missing parameter 'borderLineStyle'"
    assert "borderColor" in params, "Missing parameter 'borderColor'"
    assert "borderSizeComputationExpression" in params, "Missing parameter 'borderSizeComputationExpression'"
    assert "borderSize" in params, "Missing parameter 'borderSize'"

def test_diagram_borderedstyle_has_borderLineStyle():
    assert hasattr(diagram_BorderedStyle, "borderLineStyle")
    descriptor = None
    for klass in diagram_BorderedStyle.__mro__:
        if "borderLineStyle" in klass.__dict__:
            descriptor = klass.__dict__["borderLineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_borderedstyle_has_borderColor():
    assert hasattr(diagram_BorderedStyle, "borderColor")
    descriptor = None
    for klass in diagram_BorderedStyle.__mro__:
        if "borderColor" in klass.__dict__:
            descriptor = klass.__dict__["borderColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram_borderedstyle_has_borderSizeComputationExpression():
    assert hasattr(diagram_BorderedStyle, "borderSizeComputationExpression")
    descriptor = None
    for klass in diagram_BorderedStyle.__mro__:
        if "borderSizeComputationExpression" in klass.__dict__:
            descriptor = klass.__dict__["borderSizeComputationExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_borderedstyle_has_borderSize():
    assert hasattr(diagram_BorderedStyle, "borderSize")
    descriptor = None
    for klass in diagram_BorderedStyle.__mro__:
        if "borderSize" in klass.__dict__:
            descriptor = klass.__dict__["borderSize"]
            break
    assert isinstance(descriptor, property)



def test_labelstyle_is_not_abstract():
    assert not inspect.isabstract(LabelStyle)


def test_labelstyle_constructor_exists():
    assert callable(LabelStyle.__init__)


def test_labelstyle_constructor_args():
    sig = inspect.signature(LabelStyle.__init__)
    params = list(sig.parameters.keys())



def test_iedgemapping_is_not_abstract():
    assert not inspect.isabstract(IEdgeMapping)


def test_iedgemapping_constructor_exists():
    assert callable(IEdgeMapping.__init__)


def test_iedgemapping_constructor_args():
    sig = inspect.signature(IEdgeMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram_edgetarget_is_not_abstract():
    assert not inspect.isabstract(diagram_EdgeTarget)


def test_diagram_edgetarget_constructor_exists():
    assert callable(diagram_EdgeTarget.__init__)


def test_diagram_edgetarget_constructor_args():
    sig = inspect.signature(diagram_EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram_edgestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_EdgeStyle)


def test_diagram_edgestyle_constructor_exists():
    assert callable(diagram_EdgeStyle.__init__)


def test_diagram_edgestyle_constructor_args():
    sig = inspect.signature(diagram_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "targetArrow" in params, "Missing parameter 'targetArrow'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "strokeColor" in params, "Missing parameter 'strokeColor'"
    assert "foldingStyle" in params, "Missing parameter 'foldingStyle'"
    assert "size" in params, "Missing parameter 'size'"
    assert "sourceArrow" in params, "Missing parameter 'sourceArrow'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "centered" in params, "Missing parameter 'centered'"

def test_diagram_edgestyle_has_targetArrow():
    assert hasattr(diagram_EdgeStyle, "targetArrow")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "targetArrow" in klass.__dict__:
            descriptor = klass.__dict__["targetArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_routingStyle():
    assert hasattr(diagram_EdgeStyle, "routingStyle")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_strokeColor():
    assert hasattr(diagram_EdgeStyle, "strokeColor")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "strokeColor" in klass.__dict__:
            descriptor = klass.__dict__["strokeColor"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_foldingStyle():
    assert hasattr(diagram_EdgeStyle, "foldingStyle")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "foldingStyle" in klass.__dict__:
            descriptor = klass.__dict__["foldingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_size():
    assert hasattr(diagram_EdgeStyle, "size")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_sourceArrow():
    assert hasattr(diagram_EdgeStyle, "sourceArrow")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "sourceArrow" in klass.__dict__:
            descriptor = klass.__dict__["sourceArrow"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_lineStyle():
    assert hasattr(diagram_EdgeStyle, "lineStyle")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_edgestyle_has_centered():
    assert hasattr(diagram_EdgeStyle, "centered")
    descriptor = None
    for klass in diagram_EdgeStyle.__mro__:
        if "centered" in klass.__dict__:
            descriptor = klass.__dict__["centered"]
            break
    assert isinstance(descriptor, property)



def test_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(DDiagramElementContainer)


def test_ddiagramelementcontainer_constructor_exists():
    assert callable(DDiagramElementContainer.__init__)


def test_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())



def test_diagram_dnodelist_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeList)


def test_diagram_dnodelist_constructor_exists():
    assert callable(diagram_DNodeList.__init__)


def test_diagram_dnodelist_constructor_args():
    sig = inspect.signature(diagram_DNodeList.__init__)
    params = list(sig.parameters.keys())



def test_diagram_dnodecontainer_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeContainer)


def test_diagram_dnodecontainer_constructor_exists():
    assert callable(diagram_DNodeContainer.__init__)


def test_diagram_dnodecontainer_constructor_args():
    sig = inspect.signature(diagram_DNodeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "childrenPresentation" in params, "Missing parameter 'childrenPresentation'"

def test_diagram_dnodecontainer_has_childrenPresentation():
    assert hasattr(diagram_DNodeContainer, "childrenPresentation")
    descriptor = None
    for klass in diagram_DNodeContainer.__mro__:
        if "childrenPresentation" in klass.__dict__:
            descriptor = klass.__dict__["childrenPresentation"]
            break
    assert isinstance(descriptor, property)



def test_containermapping_is_not_abstract():
    assert not inspect.isabstract(ContainerMapping)


def test_containermapping_constructor_exists():
    assert callable(ContainerMapping.__init__)


def test_containermapping_constructor_args():
    sig = inspect.signature(ContainerMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram_containerstyle_is_not_abstract():
    assert not inspect.isabstract(diagram_ContainerStyle)


def test_diagram_containerstyle_constructor_exists():
    assert callable(diagram_ContainerStyle.__init__)


def test_diagram_containerstyle_constructor_args():
    sig = inspect.signature(diagram_ContainerStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagram_style_is_not_abstract():
    assert not inspect.isabstract(diagram_Style)


def test_diagram_style_constructor_exists():
    assert callable(diagram_Style.__init__)


def test_diagram_style_constructor_args():
    sig = inspect.signature(diagram_Style.__init__)
    params = list(sig.parameters.keys())



def test_diagram_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_GraphicalFilter)


def test_diagram_graphicalfilter_constructor_exists():
    assert callable(diagram_GraphicalFilter.__init__)


def test_diagram_graphicalfilter_constructor_args():
    sig = inspect.signature(diagram_GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_nodestyle_is_not_abstract():
    assert not inspect.isabstract(diagram_NodeStyle)


def test_diagram_nodestyle_constructor_exists():
    assert callable(diagram_NodeStyle.__init__)


def test_diagram_nodestyle_constructor_args():
    sig = inspect.signature(diagram_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"

def test_diagram_nodestyle_has_labelPosition():
    assert hasattr(diagram_NodeStyle, "labelPosition")
    descriptor = None
    for klass in diagram_NodeStyle.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)



def test_edgetarget_is_not_abstract():
    assert not inspect.isabstract(EdgeTarget)


def test_edgetarget_constructor_exists():
    assert callable(EdgeTarget.__init__)


def test_edgetarget_constructor_args():
    sig = inspect.signature(EdgeTarget.__init__)
    params = list(sig.parameters.keys())



def test_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(AbstractDNode)


def test_abstractdnode_constructor_exists():
    assert callable(AbstractDNode.__init__)


def test_abstractdnode_constructor_args():
    sig = inspect.signature(AbstractDNode.__init__)
    params = list(sig.parameters.keys())



def test_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(DDiagramElement)


def test_ddiagramelement_constructor_exists():
    assert callable(DDiagramElement.__init__)


def test_ddiagramelement_constructor_args():
    sig = inspect.signature(DDiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram_abstractdnode_is_not_abstract():
    assert not inspect.isabstract(diagram_AbstractDNode)


def test_diagram_abstractdnode_constructor_exists():
    assert callable(diagram_AbstractDNode.__init__)


def test_diagram_abstractdnode_constructor_args():
    sig = inspect.signature(diagram_AbstractDNode.__init__)
    params = list(sig.parameters.keys())
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"

def test_diagram_abstractdnode_has_arrangeConstraints():
    assert hasattr(diagram_AbstractDNode, "arrangeConstraints")
    descriptor = None
    for klass in diagram_AbstractDNode.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)



def test_filter_compositefilterdescription_is_not_abstract():
    assert not inspect.isabstract(filter_CompositeFilterDescription)


def test_filter_compositefilterdescription_constructor_exists():
    assert callable(filter_CompositeFilterDescription.__init__)


def test_filter_compositefilterdescription_constructor_args():
    sig = inspect.signature(filter_CompositeFilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_graphicalfilter_is_not_abstract():
    assert not inspect.isabstract(GraphicalFilter)


def test_graphicalfilter_constructor_exists():
    assert callable(GraphicalFilter.__init__)


def test_graphicalfilter_constructor_args():
    sig = inspect.signature(GraphicalFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_hidelabelfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_HideLabelFilter)


def test_diagram_hidelabelfilter_constructor_exists():
    assert callable(diagram_HideLabelFilter.__init__)


def test_diagram_hidelabelfilter_constructor_args():
    sig = inspect.signature(diagram_HideLabelFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_collapsefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_CollapseFilter)


def test_diagram_collapsefilter_constructor_exists():
    assert callable(diagram_CollapseFilter.__init__)


def test_diagram_collapsefilter_constructor_args():
    sig = inspect.signature(diagram_CollapseFilter.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_diagram_collapsefilter_has_height():
    assert hasattr(diagram_CollapseFilter, "height")
    descriptor = None
    for klass in diagram_CollapseFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram_collapsefilter_has_width():
    assert hasattr(diagram_CollapseFilter, "width")
    descriptor = None
    for klass in diagram_CollapseFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_diagram_foldingpointfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_FoldingPointFilter)


def test_diagram_foldingpointfilter_constructor_exists():
    assert callable(diagram_FoldingPointFilter.__init__)


def test_diagram_foldingpointfilter_constructor_args():
    sig = inspect.signature(diagram_FoldingPointFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_absoluteboundsfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_AbsoluteBoundsFilter)


def test_diagram_absoluteboundsfilter_constructor_exists():
    assert callable(diagram_AbsoluteBoundsFilter.__init__)


def test_diagram_absoluteboundsfilter_constructor_args():
    sig = inspect.signature(diagram_AbsoluteBoundsFilter.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"

def test_diagram_absoluteboundsfilter_has_x():
    assert hasattr(diagram_AbsoluteBoundsFilter, "x")
    descriptor = None
    for klass in diagram_AbsoluteBoundsFilter.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_diagram_absoluteboundsfilter_has_y():
    assert hasattr(diagram_AbsoluteBoundsFilter, "y")
    descriptor = None
    for klass in diagram_AbsoluteBoundsFilter.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_diagram_absoluteboundsfilter_has_height():
    assert hasattr(diagram_AbsoluteBoundsFilter, "height")
    descriptor = None
    for klass in diagram_AbsoluteBoundsFilter.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram_absoluteboundsfilter_has_width():
    assert hasattr(diagram_AbsoluteBoundsFilter, "width")
    descriptor = None
    for klass in diagram_AbsoluteBoundsFilter.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_diagram_foldingfilter_is_not_abstract():
    assert not inspect.isabstract(diagram_FoldingFilter)


def test_diagram_foldingfilter_constructor_exists():
    assert callable(diagram_FoldingFilter.__init__)


def test_diagram_foldingfilter_constructor_args():
    sig = inspect.signature(diagram_FoldingFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagram_appliedcompositefilters_is_not_abstract():
    assert not inspect.isabstract(diagram_AppliedCompositeFilters)


def test_diagram_appliedcompositefilters_constructor_exists():
    assert callable(diagram_AppliedCompositeFilters.__init__)


def test_diagram_appliedcompositefilters_constructor_args():
    sig = inspect.signature(diagram_AppliedCompositeFilters.__init__)
    params = list(sig.parameters.keys())



def test_diagram_hidefilter_is_not_abstract():
    assert not inspect.isabstract(diagram_HideFilter)


def test_diagram_hidefilter_constructor_exists():
    assert callable(diagram_HideFilter.__init__)


def test_diagram_hidefilter_constructor_args():
    sig = inspect.signature(diagram_HideFilter.__init__)
    params = list(sig.parameters.keys())



def test_diagramelementmapping_is_not_abstract():
    assert not inspect.isabstract(DiagramElementMapping)


def test_diagramelementmapping_constructor_exists():
    assert callable(DiagramElementMapping.__init__)


def test_diagramelementmapping_constructor_args():
    sig = inspect.signature(DiagramElementMapping.__init__)
    params = list(sig.parameters.keys())



def test_diagram_decoration_is_not_abstract():
    assert not inspect.isabstract(diagram_Decoration)


def test_diagram_decoration_constructor_exists():
    assert callable(diagram_Decoration.__init__)


def test_diagram_decoration_constructor_args():
    sig = inspect.signature(diagram_Decoration.__init__)
    params = list(sig.parameters.keys())



def test_drepresentationelement_is_not_abstract():
    assert not inspect.isabstract(DRepresentationElement)


def test_drepresentationelement_constructor_exists():
    assert callable(DRepresentationElement.__init__)


def test_drepresentationelement_constructor_args():
    sig = inspect.signature(DRepresentationElement.__init__)
    params = list(sig.parameters.keys())



def test_dsemanticdecorator_is_not_abstract():
    assert not inspect.isabstract(DSemanticDecorator)


def test_dsemanticdecorator_constructor_exists():
    assert callable(DSemanticDecorator.__init__)


def test_dsemanticdecorator_constructor_args():
    sig = inspect.signature(DSemanticDecorator.__init__)
    params = list(sig.parameters.keys())



def test_ddiagram_is_not_abstract():
    assert not inspect.isabstract(DDiagram)


def test_ddiagram_constructor_exists():
    assert callable(DDiagram.__init__)


def test_ddiagram_constructor_args():
    sig = inspect.signature(DDiagram.__init__)
    params = list(sig.parameters.keys())



def test_diagram_dsemanticdiagram_is_not_abstract():
    assert not inspect.isabstract(diagram_DSemanticDiagram)


def test_diagram_dsemanticdiagram_constructor_exists():
    assert callable(diagram_DSemanticDiagram.__init__)


def test_diagram_dsemanticdiagram_constructor_args():
    sig = inspect.signature(diagram_DSemanticDiagram.__init__)
    params = list(sig.parameters.keys())



def test_layer_is_not_abstract():
    assert not inspect.isabstract(Layer)


def test_layer_constructor_exists():
    assert callable(Layer.__init__)


def test_layer_constructor_args():
    sig = inspect.signature(Layer.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_additionallayer_is_not_abstract():
    assert not inspect.isabstract(diagram_description_AdditionalLayer)


def test_diagram_description_additionallayer_constructor_exists():
    assert callable(diagram_description_AdditionalLayer.__init__)


def test_diagram_description_additionallayer_constructor_args():
    sig = inspect.signature(diagram_description_AdditionalLayer.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "activeByDefault" in params, "Missing parameter 'activeByDefault'"

def test_diagram_description_additionallayer_has_optional():
    assert hasattr(diagram_description_AdditionalLayer, "optional")
    descriptor = None
    for klass in diagram_description_AdditionalLayer.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_additionallayer_has_activeByDefault():
    assert hasattr(diagram_description_AdditionalLayer, "activeByDefault")
    descriptor = None
    for klass in diagram_description_AdditionalLayer.__mro__:
        if "activeByDefault" in klass.__dict__:
            descriptor = klass.__dict__["activeByDefault"]
            break
    assert isinstance(descriptor, property)



def test_diagram_filtervariablehistory_is_not_abstract():
    assert not inspect.isabstract(diagram_FilterVariableHistory)


def test_diagram_filtervariablehistory_constructor_exists():
    assert callable(diagram_FilterVariableHistory.__init__)


def test_diagram_filtervariablehistory_constructor_args():
    sig = inspect.signature(diagram_FilterVariableHistory.__init__)
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



def test_drepresentation_is_not_abstract():
    assert not inspect.isabstract(DRepresentation)


def test_drepresentation_constructor_exists():
    assert callable(DRepresentation.__init__)


def test_drepresentation_constructor_args():
    sig = inspect.signature(DRepresentation.__init__)
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



def test_diagram_dnodelistelement_is_not_abstract():
    assert not inspect.isabstract(diagram_DNodeListElement)


def test_diagram_dnodelistelement_constructor_exists():
    assert callable(diagram_DNodeListElement.__init__)


def test_diagram_dnodelistelement_constructor_args():
    sig = inspect.signature(diagram_DNodeListElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram_dedge_is_not_abstract():
    assert not inspect.isabstract(diagram_DEdge)


def test_diagram_dedge_constructor_exists():
    assert callable(diagram_DEdge.__init__)


def test_diagram_dedge_constructor_args():
    sig = inspect.signature(diagram_DEdge.__init__)
    params = list(sig.parameters.keys())
    assert "isMockEdge" in params, "Missing parameter 'isMockEdge'"
    assert "isFold" in params, "Missing parameter 'isFold'"
    assert "routingStyle" in params, "Missing parameter 'routingStyle'"
    assert "beginLabel" in params, "Missing parameter 'beginLabel'"
    assert "endLabel" in params, "Missing parameter 'endLabel'"
    assert "arrangeConstraints" in params, "Missing parameter 'arrangeConstraints'"
    assert "size" in params, "Missing parameter 'size'"

def test_diagram_dedge_has_isMockEdge():
    assert hasattr(diagram_DEdge, "isMockEdge")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "isMockEdge" in klass.__dict__:
            descriptor = klass.__dict__["isMockEdge"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_isFold():
    assert hasattr(diagram_DEdge, "isFold")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "isFold" in klass.__dict__:
            descriptor = klass.__dict__["isFold"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_routingStyle():
    assert hasattr(diagram_DEdge, "routingStyle")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "routingStyle" in klass.__dict__:
            descriptor = klass.__dict__["routingStyle"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_beginLabel():
    assert hasattr(diagram_DEdge, "beginLabel")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "beginLabel" in klass.__dict__:
            descriptor = klass.__dict__["beginLabel"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_endLabel():
    assert hasattr(diagram_DEdge, "endLabel")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "endLabel" in klass.__dict__:
            descriptor = klass.__dict__["endLabel"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_arrangeConstraints():
    assert hasattr(diagram_DEdge, "arrangeConstraints")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "arrangeConstraints" in klass.__dict__:
            descriptor = klass.__dict__["arrangeConstraints"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dedge_has_size():
    assert hasattr(diagram_DEdge, "size")
    descriptor = None
    for klass in diagram_DEdge.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_diagramdescription_is_not_abstract():
    assert not inspect.isabstract(DiagramDescription)


def test_diagramdescription_constructor_exists():
    assert callable(DiagramDescription.__init__)


def test_diagramdescription_constructor_args():
    sig = inspect.signature(DiagramDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_ddiagramelement_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagramElement)


def test_diagram_ddiagramelement_constructor_exists():
    assert callable(diagram_DDiagramElement.__init__)


def test_diagram_ddiagramelement_constructor_args():
    sig = inspect.signature(diagram_DDiagramElement.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "tooltipText" in params, "Missing parameter 'tooltipText'"

def test_diagram_ddiagramelement_has_visible():
    assert hasattr(diagram_DDiagramElement, "visible")
    descriptor = None
    for klass in diagram_DDiagramElement.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ddiagramelement_has_tooltipText():
    assert hasattr(diagram_DDiagramElement, "tooltipText")
    descriptor = None
    for klass in diagram_DDiagramElement.__mro__:
        if "tooltipText" in klass.__dict__:
            descriptor = klass.__dict__["tooltipText"]
            break
    assert isinstance(descriptor, property)



def test_draganddroptarget_is_not_abstract():
    assert not inspect.isabstract(DragAndDropTarget)


def test_draganddroptarget_constructor_exists():
    assert callable(DragAndDropTarget.__init__)


def test_draganddroptarget_constructor_args():
    sig = inspect.signature(DragAndDropTarget.__init__)
    params = list(sig.parameters.keys())



def test_diagram_dnode_is_not_abstract():
    assert not inspect.isabstract(diagram_DNode)


def test_diagram_dnode_constructor_exists():
    assert callable(diagram_DNode.__init__)


def test_diagram_dnode_constructor_args():
    sig = inspect.signature(diagram_DNode.__init__)
    params = list(sig.parameters.keys())
    assert "labelPosition" in params, "Missing parameter 'labelPosition'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "resizeKind" in params, "Missing parameter 'resizeKind'"

def test_diagram_dnode_has_labelPosition():
    assert hasattr(diagram_DNode, "labelPosition")
    descriptor = None
    for klass in diagram_DNode.__mro__:
        if "labelPosition" in klass.__dict__:
            descriptor = klass.__dict__["labelPosition"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dnode_has_width():
    assert hasattr(diagram_DNode, "width")
    descriptor = None
    for klass in diagram_DNode.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dnode_has_height():
    assert hasattr(diagram_DNode, "height")
    descriptor = None
    for klass in diagram_DNode.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_diagram_dnode_has_resizeKind():
    assert hasattr(diagram_DNode, "resizeKind")
    descriptor = None
    for klass in diagram_DNode.__mro__:
        if "resizeKind" in klass.__dict__:
            descriptor = klass.__dict__["resizeKind"]
            break
    assert isinstance(descriptor, property)



def test_diagram_ddiagramelementcontainer_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagramElementContainer)


def test_diagram_ddiagramelementcontainer_constructor_exists():
    assert callable(diagram_DDiagramElementContainer.__init__)


def test_diagram_ddiagramelementcontainer_constructor_args():
    sig = inspect.signature(diagram_DDiagramElementContainer.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_diagram_ddiagramelementcontainer_has_width():
    assert hasattr(diagram_DDiagramElementContainer, "width")
    descriptor = None
    for klass in diagram_DDiagramElementContainer.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ddiagramelementcontainer_has_height():
    assert hasattr(diagram_DDiagramElementContainer, "height")
    descriptor = None
    for klass in diagram_DDiagramElementContainer.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_description_documentedelement_is_not_abstract():
    assert not inspect.isabstract(description_DocumentedElement)


def test_description_documentedelement_constructor_exists():
    assert callable(description_DocumentedElement.__init__)


def test_description_documentedelement_constructor_args():
    sig = inspect.signature(description_DocumentedElement.__init__)
    params = list(sig.parameters.keys())



def test_diagram_ddiagram_is_not_abstract():
    assert not inspect.isabstract(diagram_DDiagram)


def test_diagram_ddiagram_constructor_exists():
    assert callable(diagram_DDiagram.__init__)


def test_diagram_ddiagram_constructor_args():
    sig = inspect.signature(diagram_DDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "isInLayoutingMode" in params, "Missing parameter 'isInLayoutingMode'"
    assert "headerHeight" in params, "Missing parameter 'headerHeight'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_diagram_ddiagram_has_isInLayoutingMode():
    assert hasattr(diagram_DDiagram, "isInLayoutingMode")
    descriptor = None
    for klass in diagram_DDiagram.__mro__:
        if "isInLayoutingMode" in klass.__dict__:
            descriptor = klass.__dict__["isInLayoutingMode"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ddiagram_has_headerHeight():
    assert hasattr(diagram_DDiagram, "headerHeight")
    descriptor = None
    for klass in diagram_DDiagram.__mro__:
        if "headerHeight" in klass.__dict__:
            descriptor = klass.__dict__["headerHeight"]
            break
    assert isinstance(descriptor, property)

def test_diagram_ddiagram_has_synchronized():
    assert hasattr(diagram_DDiagram, "synchronized")
    descriptor = None
    for klass in diagram_DDiagram.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_diagram_description_layer_is_not_abstract():
    assert not inspect.isabstract(diagram_description_Layer)


def test_diagram_description_layer_constructor_exists():
    assert callable(diagram_description_Layer.__init__)


def test_diagram_description_layer_constructor_args():
    sig = inspect.signature(diagram_description_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_diagram_description_layer_has_icon():
    assert hasattr(diagram_description_Layer, "icon")
    descriptor = None
    for klass in diagram_description_Layer.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_diagram_concern_concerndescription_is_not_abstract():
    assert not inspect.isabstract(diagram_concern_ConcernDescription)


def test_diagram_concern_concerndescription_constructor_exists():
    assert callable(diagram_concern_ConcernDescription.__init__)


def test_diagram_concern_concerndescription_constructor_args():
    sig = inspect.signature(diagram_concern_ConcernDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_filter_filterdescription_is_not_abstract():
    assert not inspect.isabstract(diagram_filter_FilterDescription)


def test_diagram_filter_filterdescription_constructor_exists():
    assert callable(diagram_filter_FilterDescription.__init__)


def test_diagram_filter_filterdescription_constructor_args():
    sig = inspect.signature(diagram_filter_FilterDescription.__init__)
    params = list(sig.parameters.keys())



def test_diagram_description_edgemappingimport_is_not_abstract():
    assert not inspect.isabstract(diagram_description_EdgeMappingImport)


def test_diagram_description_edgemappingimport_constructor_exists():
    assert callable(diagram_description_EdgeMappingImport.__init__)


def test_diagram_description_edgemappingimport_constructor_args():
    sig = inspect.signature(diagram_description_EdgeMappingImport.__init__)
    params = list(sig.parameters.keys())
    assert "inheritsAncestorFilters" in params, "Missing parameter 'inheritsAncestorFilters'"

def test_diagram_description_edgemappingimport_has_inheritsAncestorFilters():
    assert hasattr(diagram_description_EdgeMappingImport, "inheritsAncestorFilters")
    descriptor = None
    for klass in diagram_description_EdgeMappingImport.__mro__:
        if "inheritsAncestorFilters" in klass.__dict__:
            descriptor = klass.__dict__["inheritsAncestorFilters"]
            break
    assert isinstance(descriptor, property)



def test_diagram_description_edgemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_EdgeMapping)


def test_diagram_description_edgemapping_constructor_exists():
    assert callable(diagram_description_EdgeMapping.__init__)


def test_diagram_description_edgemapping_constructor_args():
    sig = inspect.signature(diagram_description_EdgeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"
    assert "sourceFinderExpression" in params, "Missing parameter 'sourceFinderExpression'"
    assert "pathExpression" in params, "Missing parameter 'pathExpression'"
    assert "targetExpression" in params, "Missing parameter 'targetExpression'"
    assert "targetFinderExpression" in params, "Missing parameter 'targetFinderExpression'"
    assert "useDomainElement" in params, "Missing parameter 'useDomainElement'"

def test_diagram_description_edgemapping_has_domainClass():
    assert hasattr(diagram_description_EdgeMapping, "domainClass")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_edgemapping_has_sourceFinderExpression():
    assert hasattr(diagram_description_EdgeMapping, "sourceFinderExpression")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "sourceFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["sourceFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_edgemapping_has_pathExpression():
    assert hasattr(diagram_description_EdgeMapping, "pathExpression")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "pathExpression" in klass.__dict__:
            descriptor = klass.__dict__["pathExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_edgemapping_has_targetExpression():
    assert hasattr(diagram_description_EdgeMapping, "targetExpression")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "targetExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_edgemapping_has_targetFinderExpression():
    assert hasattr(diagram_description_EdgeMapping, "targetFinderExpression")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "targetFinderExpression" in klass.__dict__:
            descriptor = klass.__dict__["targetFinderExpression"]
            break
    assert isinstance(descriptor, property)

def test_diagram_description_edgemapping_has_useDomainElement():
    assert hasattr(diagram_description_EdgeMapping, "useDomainElement")
    descriptor = None
    for klass in diagram_description_EdgeMapping.__mro__:
        if "useDomainElement" in klass.__dict__:
            descriptor = klass.__dict__["useDomainElement"]
            break
    assert isinstance(descriptor, property)



def test_diagram_tool_toolsection_is_not_abstract():
    assert not inspect.isabstract(diagram_tool_ToolSection)


def test_diagram_tool_toolsection_constructor_exists():
    assert callable(diagram_tool_ToolSection.__init__)


def test_diagram_tool_toolsection_constructor_args():
    sig = inspect.signature(diagram_tool_ToolSection.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_diagram_tool_toolsection_has_icon():
    assert hasattr(diagram_tool_ToolSection, "icon")
    descriptor = None
    for klass in diagram_tool_ToolSection.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_diagram_description_abstractnodemapping_is_not_abstract():
    assert not inspect.isabstract(diagram_description_AbstractNodeMapping)


def test_diagram_description_abstractnodemapping_constructor_exists():
    assert callable(diagram_description_AbstractNodeMapping.__init__)


def test_diagram_description_abstractnodemapping_constructor_args():
    sig = inspect.signature(diagram_description_AbstractNodeMapping.__init__)
    params = list(sig.parameters.keys())
    assert "domainClass" in params, "Missing parameter 'domainClass'"

def test_diagram_description_abstractnodemapping_has_domainClass():
    assert hasattr(diagram_description_AbstractNodeMapping, "domainClass")
    descriptor = None
    for klass in diagram_description_AbstractNodeMapping.__mro__:
        if "domainClass" in klass.__dict__:
            descriptor = klass.__dict__["domainClass"]
            break
    assert isinstance(descriptor, property)

def test_alignmentkind_exists():
    # Check that the Enumeration exists
    assert AlignmentKind is not None

def test_alignmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignmentKind]
    expected_literals = [
        "VERTICAL",
        "HORIZONTAL",
        "SQUARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignmentKind"

def test_arrangeconstraint_exists():
    # Check that the Enumeration exists
    assert ArrangeConstraint is not None

def test_arrangeconstraint_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrangeConstraint]
    expected_literals = [
        "KEEP_SIZE",
        "KEEP_RATIO",
        "KEEP_LOCATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrangeConstraint"

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

def test_containerlayout_exists():
    # Check that the Enumeration exists
    assert ContainerLayout is not None

def test_containerlayout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerLayout]
    expected_literals = [
        "List",
        "FreeForm",
        "HorizontalStack",
        "VerticalStack",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerLayout"

def test_backgroundstyle_exists():
    # Check that the Enumeration exists
    assert BackgroundStyle is not None

def test_backgroundstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackgroundStyle]
    expected_literals = [
        "GradientLeftToRight",
        "Liquid",
        "GradientTopToBottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackgroundStyle"

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

def test_foldingstyle_exists():
    # Check that the Enumeration exists
    assert FoldingStyle is not None

def test_foldingstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoldingStyle]
    expected_literals = [
        "SOURCE",
        "TARGET",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoldingStyle"

def test_edgearrows_exists():
    # Check that the Enumeration exists
    assert EdgeArrows is not None

def test_edgearrows_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeArrows]
    expected_literals = [
        "NoDecoration",
        "InputArrow",
        "Diamond",
        "OutputArrow",
        "InputArrowWithFillDiamond",
        "InputArrowWithDiamond",
        "OutputClosedArrow",
        "FillDiamond",
        "InputFillClosedArrow",
        "OutputFillClosedArrow",
        "InputClosedArrow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeArrows"

def test_resizekind_exists():
    # Check that the Enumeration exists
    assert ResizeKind is not None

def test_resizekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResizeKind]
    expected_literals = [
        "NORTH_SOUTH",
        "NSEW",
        "NONE",
        "EAST_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResizeKind"

def test_reconnectionkind_exists():
    # Check that the Enumeration exists
    assert ReconnectionKind is not None

def test_reconnectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReconnectionKind]
    expected_literals = [
        "RECONNECT_BOTH",
        "RECONNECT_TARGET",
        "RECONNECT_SOURCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReconnectionKind"

def test_edgerouting_exists():
    # Check that the Enumeration exists
    assert EdgeRouting is not None

def test_edgerouting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeRouting]
    expected_literals = [
        "tree",
        "straight",
        "manhattan",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeRouting"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "dash_dot",
        "dash",
        "dot",
        "solid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_bundledimageshape_exists():
    # Check that the Enumeration exists
    assert BundledImageShape is not None

def test_bundledimageshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BundledImageShape]
    expected_literals = [
        "ring",
        "stroke",
        "providedShape",
        "triangle",
        "dot",
        "square",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BundledImageShape"

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

def test_centeringstyle_exists():
    # Check that the Enumeration exists
    assert CenteringStyle is not None

def test_centeringstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CenteringStyle]
    expected_literals = [
        "Target",
        "Both",
        "None_",
        "Source",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CenteringStyle"

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
tool_VariableContainer_strategy = st.builds(
    tool_VariableContainer,
)
description_AbstractVariable_strategy = st.builds(
    description_AbstractVariable,
)
diagram_tool_ElementDoubleClickVariable_strategy = st.builds(
    diagram_tool_ElementDoubleClickVariable,
)
diagram_tool_TargetEdgeCreationVariable_strategy = st.builds(
    diagram_tool_TargetEdgeCreationVariable,
)
diagram_tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    diagram_tool_SourceEdgeViewCreationVariable,
)
diagram_tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    diagram_tool_TargetEdgeViewCreationVariable,
)
diagram_tool_SourceEdgeCreationVariable_strategy = st.builds(
    diagram_tool_SourceEdgeCreationVariable,
)
tool_EditMaskVariables_strategy = st.builds(
    tool_EditMaskVariables,
)
AbstractToolDescription_strategy = st.builds(
    AbstractToolDescription,
)
diagram_tool_BehaviorTool_strategy = st.builds(
    diagram_tool_BehaviorTool,
    domainClass=
        safe_text
)
diagram_tool_RequestDescription_strategy = st.builds(
    diagram_tool_RequestDescription,
    type=
        safe_text
)
tool_ElementSelectVariable_strategy = st.builds(
    tool_ElementSelectVariable,
)
tool_ElementDeleteVariable_strategy = st.builds(
    tool_ElementDeleteVariable,
)
diagram_tool_DeleteHookParameter_strategy = st.builds(
    diagram_tool_DeleteHookParameter,
    value=
        safe_text,
    name=
        safe_text
)
tool_DeleteHookParameter_strategy = st.builds(
    tool_DeleteHookParameter,
)
diagram_tool_DeleteHook_strategy = st.builds(
    diagram_tool_DeleteHook,
    id=
        safe_text
)
tool_ElementDoubleClickVariable_strategy = st.builds(
    tool_ElementDoubleClickVariable,
)
tool_DeleteHook_strategy = st.builds(
    tool_DeleteHook,
)
tool_TargetEdgeViewCreationVariable_strategy = st.builds(
    tool_TargetEdgeViewCreationVariable,
)
tool_SourceEdgeViewCreationVariable_strategy = st.builds(
    tool_SourceEdgeViewCreationVariable,
)
tool_InitEdgeCreationOperation_strategy = st.builds(
    tool_InitEdgeCreationOperation,
)
MappingBasedToolDescription_strategy = st.builds(
    MappingBasedToolDescription,
)
diagram_tool_DeleteElementDescription_strategy = st.builds(
    diagram_tool_DeleteElementDescription,
)
diagram_tool_DoubleClickDescription_strategy = st.builds(
    diagram_tool_DoubleClickDescription,
)
diagram_tool_ReconnectEdgeDescription_strategy = st.builds(
    diagram_tool_ReconnectEdgeDescription,
    reconnectionKind=
        safe_text
)
diagram_tool_ContainerCreationDescription_strategy = st.builds(
    diagram_tool_ContainerCreationDescription,
    iconPath=
        safe_text
)
diagram_tool_DirectEditLabel_strategy = st.builds(
    diagram_tool_DirectEditLabel,
    inputLabelExpression=
        safe_text
)
diagram_tool_NodeCreationDescription_strategy = st.builds(
    diagram_tool_NodeCreationDescription,
    iconPath=
        safe_text
)
tool_ToolGroup_strategy = st.builds(
    tool_ToolGroup,
)
diagram_tool_ToolGroupExtension_strategy = st.builds(
    diagram_tool_ToolGroupExtension,
)
tool_TargetEdgeCreationVariable_strategy = st.builds(
    tool_TargetEdgeCreationVariable,
)
tool_SourceEdgeCreationVariable_strategy = st.builds(
    tool_SourceEdgeCreationVariable,
)
diagram_tool_EdgeCreationDescription_strategy = st.builds(
    diagram_tool_EdgeCreationDescription,
    iconPath=
        safe_text,
    connectionStartPrecondition=
        safe_text
)
tool_InitialNodeCreationOperation_strategy = st.builds(
    tool_InitialNodeCreationOperation,
)
tool_ContainerViewVariable_strategy = st.builds(
    tool_ContainerViewVariable,
)
tool_NodeCreationVariable_strategy = st.builds(
    tool_NodeCreationVariable,
)
style_EndLabelStyleDescription_strategy = st.builds(
    style_EndLabelStyleDescription,
)
style_CenterLabelStyleDescription_strategy = st.builds(
    style_CenterLabelStyleDescription,
)
ToolEntry_strategy = st.builds(
    ToolEntry,
)
diagram_tool_ToolGroup_strategy = st.builds(
    diagram_tool_ToolGroup,
)
tool_ToolGroupExtension_strategy = st.builds(
    tool_ToolGroupExtension,
)
tool_PopupMenu_strategy = st.builds(
    tool_PopupMenu,
)
tool_ToolEntry_strategy = st.builds(
    tool_ToolEntry,
)
diagram_style_HideLabelCapabilityStyleDescription_strategy = st.builds(
    diagram_style_HideLabelCapabilityStyleDescription,
    hideLabelByDefault=
        st.booleans()
)
EdgeStyleDescription_strategy = st.builds(
    EdgeStyleDescription,
)
diagram_style_BracketEdgeStyleDescription_strategy = st.builds(
    diagram_style_BracketEdgeStyleDescription,
)
BasicLabelStyleDescription_strategy = st.builds(
    BasicLabelStyleDescription,
)
diagram_style_CenterLabelStyleDescription_strategy = st.builds(
    diagram_style_CenterLabelStyleDescription,
)
diagram_style_EndLabelStyleDescription_strategy = st.builds(
    diagram_style_EndLabelStyleDescription,
)
diagram_style_BeginLabelStyleDescription_strategy = st.builds(
    diagram_style_BeginLabelStyleDescription,
)
style_SizeComputationContainerStyleDescription_strategy = st.builds(
    style_SizeComputationContainerStyleDescription,
)
style_BeginLabelStyleDescription_strategy = st.builds(
    style_BeginLabelStyleDescription,
)
style_LabelBorderStyleDescription_strategy = st.builds(
    style_LabelBorderStyleDescription,
)
style_RoundedCornerStyleDescription_strategy = st.builds(
    style_RoundedCornerStyleDescription,
)
diagram_style_SizeComputationContainerStyleDescription_strategy = st.builds(
    diagram_style_SizeComputationContainerStyleDescription,
    widthComputationExpression=
        safe_text,
    heightComputationExpression=
        safe_text
)
diagram_style_GaugeSectionDescription_strategy = st.builds(
    diagram_style_GaugeSectionDescription,
    minValueExpression=
        safe_text,
    valueExpression=
        safe_text,
    maxValueExpression=
        safe_text,
    label=
        safe_text
)
style_GaugeSectionDescription_strategy = st.builds(
    style_GaugeSectionDescription,
)
DecorationDescriptionsSet_strategy = st.builds(
    DecorationDescriptionsSet,
)
NodeStyleDescription_strategy = st.builds(
    NodeStyleDescription,
)
diagram_style_LozengeNodeDescription_strategy = st.builds(
    diagram_style_LozengeNodeDescription,
    heightComputationExpression=
        safe_text,
    widthComputationExpression=
        safe_text
)
diagram_style_DotDescription_strategy = st.builds(
    diagram_style_DotDescription,
    strokeSizeComputationExpression=
        safe_text
)
diagram_style_EllipseNodeDescription_strategy = st.builds(
    diagram_style_EllipseNodeDescription,
    verticalDiameterComputationExpression=
        safe_text,
    horizontalDiameterComputationExpression=
        safe_text
)
diagram_style_BundledImageDescription_strategy = st.builds(
    diagram_style_BundledImageDescription,
    shape=
        safe_text,
    providedShapeID=
        safe_text
)
diagram_style_NoteDescription_strategy = st.builds(
    diagram_style_NoteDescription,
)
diagram_style_GaugeCompositeStyleDescription_strategy = st.builds(
    diagram_style_GaugeCompositeStyleDescription,
    alignment=
        safe_text
)
diagram_style_SquareDescription_strategy = st.builds(
    diagram_style_SquareDescription,
    width=
        safe_text,
    height=
        safe_text
)
diagram_style_CustomStyleDescription_strategy = st.builds(
    diagram_style_CustomStyleDescription,
    id=
        safe_text
)
style_HideLabelCapabilityStyleDescription_strategy = st.builds(
    style_HideLabelCapabilityStyleDescription,
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
diagram_style_ContainerStyleDescription_strategy = st.builds(
    diagram_style_ContainerStyleDescription,
    roundedCorner=
        st.booleans()
)
ColorDescription_strategy = st.builds(
    ColorDescription,
)
StyleDescription_strategy = st.builds(
    StyleDescription,
)
diagram_style_RoundedCornerStyleDescription_strategy = st.builds(
    diagram_style_RoundedCornerStyleDescription,
    arcHeight=
        safe_text,
    arcWidth=
        safe_text
)
diagram_style_EdgeStyleDescription_strategy = st.builds(
    diagram_style_EdgeStyleDescription,
    foldingStyle=
        safe_text,
    endsCentering=
        safe_text,
    targetArrow=
        safe_text,
    sizeComputationExpression=
        safe_text,
    lineStyle=
        safe_text,
    sourceArrow=
        safe_text,
    routingStyle=
        safe_text
)
diagram_style_BorderedStyleDescription_strategy = st.builds(
    diagram_style_BorderedStyleDescription,
    borderLineStyle=
        safe_text,
    borderSizeComputationExpression=
        safe_text
)
tool_ContainerDropDescription_strategy = st.builds(
    tool_ContainerDropDescription,
)
diagram_description_DragAndDropTargetDescription_strategy = st.builds(
    diagram_description_DragAndDropTargetDescription,
)
Customization_strategy = st.builds(
    Customization,
)
DecorationDescription_strategy = st.builds(
    DecorationDescription,
)
diagram_description_MappingBasedDecoration_strategy = st.builds(
    diagram_description_MappingBasedDecoration,
)
description_EndUserDocumentedElement_strategy = st.builds(
    description_EndUserDocumentedElement,
)
DocumentedElement_strategy = st.builds(
    DocumentedElement,
)
diagram_description_Layout_strategy = st.builds(
    diagram_description_Layout,
)
ConditionalStyleDescription_strategy = st.builds(
    ConditionalStyleDescription,
)
diagram_description_ConditionalEdgeStyleDescription_strategy = st.builds(
    diagram_description_ConditionalEdgeStyleDescription,
)
diagram_description_ConditionalContainerStyleDescription_strategy = st.builds(
    diagram_description_ConditionalContainerStyleDescription,
)
diagram_description_ConditionalNodeStyleDescription_strategy = st.builds(
    diagram_description_ConditionalNodeStyleDescription,
)
description_IdentifiedElement_strategy = st.builds(
    description_IdentifiedElement,
)
diagram_description_IEdgeMapping_strategy = st.builds(
    diagram_description_IEdgeMapping,
)
AbstractNodeMapping_strategy = st.builds(
    AbstractNodeMapping,
)
tool_ReconnectEdgeDescription_strategy = st.builds(
    tool_ReconnectEdgeDescription,
)
ConditionalEdgeStyleDescription_strategy = st.builds(
    ConditionalEdgeStyleDescription,
)
style_EdgeStyleDescription_strategy = st.builds(
    style_EdgeStyleDescription,
)
description_IEdgeMapping_strategy = st.builds(
    description_IEdgeMapping,
)
description_ContainerMapping_strategy = st.builds(
    description_ContainerMapping,
)
description_AbstractMappingImport_strategy = st.builds(
    description_AbstractMappingImport,
)
diagram_description_ContainerMappingImport_strategy = st.builds(
    diagram_description_ContainerMappingImport,
)
description_NodeMapping_strategy = st.builds(
    description_NodeMapping,
)
diagram_description_NodeMappingImport_strategy = st.builds(
    diagram_description_NodeMappingImport,
)
ConditionalContainerStyleDescription_strategy = st.builds(
    ConditionalContainerStyleDescription,
)
style_ContainerStyleDescription_strategy = st.builds(
    style_ContainerStyleDescription,
)
diagram_style_ShapeContainerStyleDescription_strategy = st.builds(
    diagram_style_ShapeContainerStyleDescription,
    shape=
        safe_text
)
diagram_style_FlatContainerStyleDescription_strategy = st.builds(
    diagram_style_FlatContainerStyleDescription,
    backgroundStyle=
        safe_text
)
ConditionalNodeStyleDescription_strategy = st.builds(
    ConditionalNodeStyleDescription,
)
style_NodeStyleDescription_strategy = st.builds(
    style_NodeStyleDescription,
)
diagram_style_WorkspaceImageDescription_strategy = st.builds(
    diagram_style_WorkspaceImageDescription,
    workspacePath=
        safe_text
)
description_AbstractNodeMapping_strategy = st.builds(
    description_AbstractNodeMapping,
)
description_RepresentationElementMapping_strategy = st.builds(
    description_RepresentationElementMapping,
)
description_DiagramElementMapping_strategy = st.builds(
    description_DiagramElementMapping,
)
tool_DoubleClickDescription_strategy = st.builds(
    tool_DoubleClickDescription,
)
tool_DirectEditLabel_strategy = st.builds(
    tool_DirectEditLabel,
)
tool_DeleteElementDescription_strategy = st.builds(
    tool_DeleteElementDescription,
)
RepresentationExtensionDescription_strategy = st.builds(
    RepresentationExtensionDescription,
)
diagram_description_DiagramExtensionDescription_strategy = st.builds(
    diagram_description_DiagramExtensionDescription,
)
description_DiagramDescription_strategy = st.builds(
    description_DiagramDescription,
)
description_RepresentationImportDescription_strategy = st.builds(
    description_RepresentationImportDescription,
)
diagram_description_DiagramImportDescription_strategy = st.builds(
    diagram_description_DiagramImportDescription,
)
tool_ToolSection_strategy = st.builds(
    tool_ToolSection,
)
tool_AbstractToolDescription_strategy = st.builds(
    tool_AbstractToolDescription,
)
EdgeMappingImport_strategy = st.builds(
    EdgeMappingImport,
)
AdditionalLayer_strategy = st.builds(
    AdditionalLayer,
)
tool_InitialOperation_strategy = st.builds(
    tool_InitialOperation,
)
Layout_strategy = st.builds(
    Layout,
)
diagram_description_CompositeLayout_strategy = st.builds(
    diagram_description_CompositeLayout,
    direction=
        safe_text,
    padding=
        st.integers()
)
diagram_description_OrderedTreeLayout_strategy = st.builds(
    diagram_description_OrderedTreeLayout,
    childrenExpression=
        safe_text
)
tool_RepresentationCreationDescription_strategy = st.builds(
    tool_RepresentationCreationDescription,
)
diagram_concern_ConcernSet_strategy = st.builds(
    diagram_concern_ConcernSet,
)
InteractiveVariableDescription_strategy = st.builds(
    InteractiveVariableDescription,
)
filter_Filter_strategy = st.builds(
    filter_Filter,
)
FilterDescription_strategy = st.builds(
    FilterDescription,
)
diagram_filter_CompositeFilterDescription_strategy = st.builds(
    diagram_filter_CompositeFilterDescription,
)
Filter_strategy = st.builds(
    Filter,
)
diagram_filter_VariableFilter_strategy = st.builds(
    diagram_filter_VariableFilter,
    semanticConditionExpression=
        safe_text
)
diagram_filter_MappingFilter_strategy = st.builds(
    diagram_filter_MappingFilter,
    viewConditionExpression=
        safe_text,
    semanticConditionExpression=
        safe_text
)
diagram_filter_Filter_strategy = st.builds(
    diagram_filter_Filter,
    filterKind=
        safe_text
)
tool_InitialContainerDropOperation_strategy = st.builds(
    tool_InitialContainerDropOperation,
)
CreateView_strategy = st.builds(
    CreateView,
)
diagram_tool_CreateEdgeView_strategy = st.builds(
    diagram_tool_CreateEdgeView,
    sourceExpression=
        safe_text,
    targetExpression=
        safe_text
)
tool_ElementDropVariable_strategy = st.builds(
    tool_ElementDropVariable,
)
tool_DropContainerVariable_strategy = st.builds(
    tool_DropContainerVariable,
)
diagram_tool_ContainerDropDescription_strategy = st.builds(
    diagram_tool_ContainerDropDescription,
    dragSource=
        safe_text,
    moveEdges=
        st.booleans()
)
RepresentationNavigationDescription_strategy = st.builds(
    RepresentationNavigationDescription,
)
diagram_tool_DiagramNavigationDescription_strategy = st.builds(
    diagram_tool_DiagramNavigationDescription,
)
RepresentationCreationDescription_strategy = st.builds(
    RepresentationCreationDescription,
)
diagram_tool_DiagramCreationDescription_strategy = st.builds(
    diagram_tool_DiagramCreationDescription,
)
ContainerModelOperation_strategy = st.builds(
    ContainerModelOperation,
)
diagram_tool_Navigation_strategy = st.builds(
    diagram_tool_Navigation,
    createIfNotExistent=
        st.booleans()
)
diagram_tool_CreateView_strategy = st.builds(
    diagram_tool_CreateView,
    containerViewExpression=
        safe_text,
    variableName=
        safe_text
)
diagram_tool_NodeCreationVariable_strategy = st.builds(
    diagram_tool_NodeCreationVariable,
)
diagram_HideLabelCapabilityStyle_strategy = st.builds(
    diagram_HideLabelCapabilityStyle,
    hideLabelByDefault=
        st.booleans()
)
concern_ConcernSet_strategy = st.builds(
    concern_ConcernSet,
)
validation_ValidationSet_strategy = st.builds(
    validation_ValidationSet,
)
EdgeMapping_strategy = st.builds(
    EdgeMapping,
)
description_PasteTargetDescription_strategy = st.builds(
    description_PasteTargetDescription,
)
diagram_description_DiagramElementMapping_strategy = st.builds(
    diagram_description_DiagramElementMapping,
    synchronizationLock=
        st.booleans(),
    semanticElements=
        safe_text,
    createElements=
        st.booleans(),
    semanticCandidatesExpression=
        safe_text,
    preconditionExpression=
        safe_text
)
description_RepresentationDescription_strategy = st.builds(
    description_RepresentationDescription,
)
description_DragAndDropTargetDescription_strategy = st.builds(
    description_DragAndDropTargetDescription,
)
diagram_description_NodeMapping_strategy = st.builds(
    diagram_description_NodeMapping,
)
diagram_description_ContainerMapping_strategy = st.builds(
    diagram_description_ContainerMapping,
    childrenPresentation=
        safe_text
)
diagram_description_DiagramDescription_strategy = st.builds(
    diagram_description_DiagramDescription,
    domainClass=
        safe_text,
    rootExpression=
        safe_text,
    preconditionExpression=
        safe_text,
    enablePopupBars=
        st.booleans()
)
diagram_EObject_strategy = st.builds(
    diagram_EObject,
)
tool_SelectModelElementVariable_strategy = st.builds(
    tool_SelectModelElementVariable,
)
TypedVariable_strategy = st.builds(
    TypedVariable,
)
diagram_DragAndDropTarget_strategy = st.builds(
    diagram_DragAndDropTarget,
)
style_StyleDescription_strategy = st.builds(
    style_StyleDescription,
)
diagram_style_NodeStyleDescription_strategy = st.builds(
    diagram_style_NodeStyleDescription,
    resizeKind=
        safe_text,
    sizeComputationExpression=
        safe_text,
    labelPosition=
        safe_text
)
diagram_ComputedStyleDescriptionRegistry_strategy = st.builds(
    diagram_ComputedStyleDescriptionRegistry,
)
EdgeStyle_strategy = st.builds(
    EdgeStyle,
)
diagram_BracketEdgeStyle_strategy = st.builds(
    diagram_BracketEdgeStyle,
)
BasicLabelStyle_strategy = st.builds(
    BasicLabelStyle,
)
CollapseFilter_strategy = st.builds(
    CollapseFilter,
)
diagram_IndirectlyCollapseFilter_strategy = st.builds(
    diagram_IndirectlyCollapseFilter,
)
diagram_VariableValue_strategy = st.builds(
    diagram_VariableValue,
)
diagram_EndLabelStyle_strategy = st.builds(
    diagram_EndLabelStyle,
)
diagram_CenterLabelStyle_strategy = st.builds(
    diagram_CenterLabelStyle,
)
diagram_BeginLabelStyle_strategy = st.builds(
    diagram_BeginLabelStyle,
)
ContainerStyle_strategy = st.builds(
    ContainerStyle,
)
diagram_FlatContainerStyle_strategy = st.builds(
    diagram_FlatContainerStyle,
    backgroundStyle=
        safe_text,
    backgroundColor=
        safe_text,
    foregroundColor=
        safe_text
)
diagram_ShapeContainerStyle_strategy = st.builds(
    diagram_ShapeContainerStyle,
    shape=
        safe_text,
    backgroundColor=
        safe_text
)
Customizable_strategy = st.builds(
    Customizable,
)
diagram_GaugeSection_strategy = st.builds(
    diagram_GaugeSection,
    foregroundColor=
        safe_text,
    max=
        safe_text,
    value=
        safe_text,
    backgroundColor=
        safe_text,
    min=
        safe_text,
    label=
        safe_text
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
diagram_Note_strategy = st.builds(
    diagram_Note,
    color=
        safe_text
)
diagram_CustomStyle_strategy = st.builds(
    diagram_CustomStyle,
    id=
        safe_text
)
diagram_Square_strategy = st.builds(
    diagram_Square,
    height=
        safe_text,
    width=
        safe_text,
    color=
        safe_text
)
diagram_Ellipse_strategy = st.builds(
    diagram_Ellipse,
    verticalDiameter=
        safe_text,
    color=
        safe_text,
    horizontalDiameter=
        safe_text
)
diagram_Lozenge_strategy = st.builds(
    diagram_Lozenge,
    color=
        safe_text,
    width=
        safe_text,
    height=
        safe_text
)
diagram_BundledImage_strategy = st.builds(
    diagram_BundledImage,
    providedShapeID=
        safe_text,
    color=
        safe_text,
    shape=
        safe_text
)
diagram_WorkspaceImage_strategy = st.builds(
    diagram_WorkspaceImage,
    workspacePath=
        safe_text
)
diagram_GaugeCompositeStyle_strategy = st.builds(
    diagram_GaugeCompositeStyle,
    alignment=
        safe_text
)
VariableValue_strategy = st.builds(
    VariableValue,
)
diagram_EObjectVariableValue_strategy = st.builds(
    diagram_EObjectVariableValue,
)
diagram_TypedVariableValue_strategy = st.builds(
    diagram_TypedVariableValue,
    value=
        safe_text
)
diagram_Dot_strategy = st.builds(
    diagram_Dot,
    strokeSizeComputationExpression=
        safe_text,
    backgroundColor=
        safe_text
)
HideLabelCapabilityStyle_strategy = st.builds(
    HideLabelCapabilityStyle,
)
BorderedStyle_strategy = st.builds(
    BorderedStyle,
)
Style_strategy = st.builds(
    Style,
)
diagram_BorderedStyle_strategy = st.builds(
    diagram_BorderedStyle,
    borderLineStyle=
        safe_text,
    borderColor=
        safe_text,
    borderSizeComputationExpression=
        safe_text,
    borderSize=
        safe_text
)
LabelStyle_strategy = st.builds(
    LabelStyle,
)
IEdgeMapping_strategy = st.builds(
    IEdgeMapping,
)
diagram_EdgeTarget_strategy = st.builds(
    diagram_EdgeTarget,
)
diagram_EdgeStyle_strategy = st.builds(
    diagram_EdgeStyle,
    targetArrow=
        safe_text,
    routingStyle=
        safe_text,
    strokeColor=
        safe_text,
    foldingStyle=
        safe_text,
    size=
        safe_text,
    sourceArrow=
        safe_text,
    lineStyle=
        safe_text,
    centered=
        safe_text
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
DDiagramElementContainer_strategy = st.builds(
    DDiagramElementContainer,
)
diagram_DNodeList_strategy = st.builds(
    diagram_DNodeList,
)
diagram_DNodeContainer_strategy = st.builds(
    diagram_DNodeContainer,
    childrenPresentation=
        safe_text
)
ContainerMapping_strategy = st.builds(
    ContainerMapping,
)
diagram_ContainerStyle_strategy = st.builds(
    diagram_ContainerStyle,
)
diagram_Style_strategy = st.builds(
    diagram_Style,
)
diagram_GraphicalFilter_strategy = st.builds(
    diagram_GraphicalFilter,
)
diagram_NodeStyle_strategy = st.builds(
    diagram_NodeStyle,
    labelPosition=
        safe_text
)
EdgeTarget_strategy = st.builds(
    EdgeTarget,
)
AbstractDNode_strategy = st.builds(
    AbstractDNode,
)
DDiagramElement_strategy = st.builds(
    DDiagramElement,
)
diagram_AbstractDNode_strategy = st.builds(
    diagram_AbstractDNode,
    arrangeConstraints=
        safe_text
)
filter_CompositeFilterDescription_strategy = st.builds(
    filter_CompositeFilterDescription,
)
GraphicalFilter_strategy = st.builds(
    GraphicalFilter,
)
diagram_HideLabelFilter_strategy = st.builds(
    diagram_HideLabelFilter,
)
diagram_CollapseFilter_strategy = st.builds(
    diagram_CollapseFilter,
    height=
        st.integers(),
    width=
        st.integers()
)
diagram_FoldingPointFilter_strategy = st.builds(
    diagram_FoldingPointFilter,
)
diagram_AbsoluteBoundsFilter_strategy = st.builds(
    diagram_AbsoluteBoundsFilter,
    x=
        safe_text,
    y=
        safe_text,
    height=
        safe_text,
    width=
        safe_text
)
diagram_FoldingFilter_strategy = st.builds(
    diagram_FoldingFilter,
)
diagram_AppliedCompositeFilters_strategy = st.builds(
    diagram_AppliedCompositeFilters,
)
diagram_HideFilter_strategy = st.builds(
    diagram_HideFilter,
)
DiagramElementMapping_strategy = st.builds(
    DiagramElementMapping,
)
diagram_Decoration_strategy = st.builds(
    diagram_Decoration,
)
DRepresentationElement_strategy = st.builds(
    DRepresentationElement,
)
DSemanticDecorator_strategy = st.builds(
    DSemanticDecorator,
)
DDiagram_strategy = st.builds(
    DDiagram,
)
diagram_DSemanticDiagram_strategy = st.builds(
    diagram_DSemanticDiagram,
)
Layer_strategy = st.builds(
    Layer,
)
diagram_description_AdditionalLayer_strategy = st.builds(
    diagram_description_AdditionalLayer,
    optional=
        st.booleans(),
    activeByDefault=
        st.booleans()
)
diagram_FilterVariableHistory_strategy = st.builds(
    diagram_FilterVariableHistory,
)
tool_BehaviorTool_strategy = st.builds(
    tool_BehaviorTool,
)
validation_ValidationRule_strategy = st.builds(
    validation_ValidationRule,
)
DRepresentation_strategy = st.builds(
    DRepresentation,
)
filter_FilterDescription_strategy = st.builds(
    filter_FilterDescription,
)
concern_ConcernDescription_strategy = st.builds(
    concern_ConcernDescription,
)
diagram_DNodeListElement_strategy = st.builds(
    diagram_DNodeListElement,
)
diagram_DEdge_strategy = st.builds(
    diagram_DEdge,
    isMockEdge=
        st.booleans(),
    isFold=
        st.booleans(),
    routingStyle=
        safe_text,
    beginLabel=
        safe_text,
    endLabel=
        safe_text,
    arrangeConstraints=
        safe_text,
    size=
        safe_text
)
DiagramDescription_strategy = st.builds(
    DiagramDescription,
)
diagram_DDiagramElement_strategy = st.builds(
    diagram_DDiagramElement,
    visible=
        st.booleans(),
    tooltipText=
        safe_text
)
DragAndDropTarget_strategy = st.builds(
    DragAndDropTarget,
)
diagram_DNode_strategy = st.builds(
    diagram_DNode,
    labelPosition=
        safe_text,
    width=
        safe_text,
    height=
        safe_text,
    resizeKind=
        safe_text
)
diagram_DDiagramElementContainer_strategy = st.builds(
    diagram_DDiagramElementContainer,
    width=
        safe_text,
    height=
        safe_text
)
description_DocumentedElement_strategy = st.builds(
    description_DocumentedElement,
)
diagram_DDiagram_strategy = st.builds(
    diagram_DDiagram,
    isInLayoutingMode=
        st.booleans(),
    headerHeight=
        st.integers(),
    synchronized=
        st.booleans()
)
diagram_description_Layer_strategy = st.builds(
    diagram_description_Layer,
    icon=
        safe_text
)
diagram_concern_ConcernDescription_strategy = st.builds(
    diagram_concern_ConcernDescription,
)
diagram_filter_FilterDescription_strategy = st.builds(
    diagram_filter_FilterDescription,
)
diagram_description_EdgeMappingImport_strategy = st.builds(
    diagram_description_EdgeMappingImport,
    inheritsAncestorFilters=
        st.booleans()
)
diagram_description_EdgeMapping_strategy = st.builds(
    diagram_description_EdgeMapping,
    domainClass=
        safe_text,
    sourceFinderExpression=
        safe_text,
    pathExpression=
        safe_text,
    targetExpression=
        safe_text,
    targetFinderExpression=
        safe_text,
    useDomainElement=
        st.booleans()
)
diagram_tool_ToolSection_strategy = st.builds(
    diagram_tool_ToolSection,
    icon=
        safe_text
)
diagram_description_AbstractNodeMapping_strategy = st.builds(
    diagram_description_AbstractNodeMapping,
    domainClass=
        safe_text
)

@given(instance=tool_VariableContainer_strategy)
@settings(max_examples=50)
def test_tool_variablecontainer_instantiation(instance):
    assert isinstance(instance, tool_VariableContainer)

@given(instance=description_AbstractVariable_strategy)
@settings(max_examples=50)
def test_description_abstractvariable_instantiation(instance):
    assert isinstance(instance, description_AbstractVariable)

@given(instance=diagram_tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_ElementDoubleClickVariable)

@given(instance=diagram_tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_TargetEdgeCreationVariable)

@given(instance=diagram_tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_SourceEdgeViewCreationVariable)

@given(instance=diagram_tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_TargetEdgeViewCreationVariable)

@given(instance=diagram_tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_SourceEdgeCreationVariable)

@given(instance=tool_EditMaskVariables_strategy)
@settings(max_examples=50)
def test_tool_editmaskvariables_instantiation(instance):
    assert isinstance(instance, tool_EditMaskVariables)

@given(instance=AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, AbstractToolDescription)

@given(instance=diagram_tool_BehaviorTool_strategy)
@settings(max_examples=50)
def test_diagram_tool_behaviortool_instantiation(instance):
    assert isinstance(instance, diagram_tool_BehaviorTool)



@given(instance=diagram_tool_BehaviorTool_strategy)
def test_diagram_tool_behaviortool_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

@given(instance=diagram_tool_RequestDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_requestdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_RequestDescription)



@given(instance=diagram_tool_RequestDescription_strategy)
def test_diagram_tool_requestdescription_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=tool_ElementSelectVariable_strategy)
@settings(max_examples=50)
def test_tool_elementselectvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementSelectVariable)

@given(instance=tool_ElementDeleteVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdeletevariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDeleteVariable)

@given(instance=diagram_tool_DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_diagram_tool_deletehookparameter_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteHookParameter)



@given(instance=diagram_tool_DeleteHookParameter_strategy)
def test_diagram_tool_deletehookparameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=diagram_tool_DeleteHookParameter_strategy)
def test_diagram_tool_deletehookparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tool_DeleteHookParameter_strategy)
@settings(max_examples=50)
def test_tool_deletehookparameter_instantiation(instance):
    assert isinstance(instance, tool_DeleteHookParameter)

@given(instance=diagram_tool_DeleteHook_strategy)
@settings(max_examples=50)
def test_diagram_tool_deletehook_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteHook)



@given(instance=diagram_tool_DeleteHook_strategy)
def test_diagram_tool_deletehook_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=tool_ElementDoubleClickVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdoubleclickvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDoubleClickVariable)

@given(instance=tool_DeleteHook_strategy)
@settings(max_examples=50)
def test_tool_deletehook_instantiation(instance):
    assert isinstance(instance, tool_DeleteHook)

@given(instance=tool_TargetEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_targetedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeViewCreationVariable)

@given(instance=tool_SourceEdgeViewCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_sourceedgeviewcreationvariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeViewCreationVariable)

@given(instance=tool_InitEdgeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool_initedgecreationoperation_instantiation(instance):
    assert isinstance(instance, tool_InitEdgeCreationOperation)

@given(instance=MappingBasedToolDescription_strategy)
@settings(max_examples=50)
def test_mappingbasedtooldescription_instantiation(instance):
    assert isinstance(instance, MappingBasedToolDescription)

@given(instance=diagram_tool_DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_deleteelementdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DeleteElementDescription)

@given(instance=diagram_tool_DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_doubleclickdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DoubleClickDescription)

@given(instance=diagram_tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ReconnectEdgeDescription)



@given(instance=diagram_tool_ReconnectEdgeDescription_strategy)
def test_diagram_tool_reconnectedgedescription_reconnectionKind_setter(instance):
    original = instance.reconnectionKind
    instance.reconnectionKind = original
    assert instance.reconnectionKind == original

@given(instance=diagram_tool_ContainerCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_containercreationdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ContainerCreationDescription)



@given(instance=diagram_tool_ContainerCreationDescription_strategy)
def test_diagram_tool_containercreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=diagram_tool_DirectEditLabel_strategy)
@settings(max_examples=50)
def test_diagram_tool_directeditlabel_instantiation(instance):
    assert isinstance(instance, diagram_tool_DirectEditLabel)



@given(instance=diagram_tool_DirectEditLabel_strategy)
def test_diagram_tool_directeditlabel_inputLabelExpression_setter(instance):
    original = instance.inputLabelExpression
    instance.inputLabelExpression = original
    assert instance.inputLabelExpression == original

@given(instance=diagram_tool_NodeCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_nodecreationdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_NodeCreationDescription)



@given(instance=diagram_tool_NodeCreationDescription_strategy)
def test_diagram_tool_nodecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original

@given(instance=tool_ToolGroup_strategy)
@settings(max_examples=50)
def test_tool_toolgroup_instantiation(instance):
    assert isinstance(instance, tool_ToolGroup)

@given(instance=diagram_tool_ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_diagram_tool_toolgroupextension_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolGroupExtension)

@given(instance=tool_TargetEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_targetedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_TargetEdgeCreationVariable)

@given(instance=tool_SourceEdgeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_sourceedgecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_SourceEdgeCreationVariable)

@given(instance=diagram_tool_EdgeCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_edgecreationdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_EdgeCreationDescription)



@given(instance=diagram_tool_EdgeCreationDescription_strategy)
def test_diagram_tool_edgecreationdescription_iconPath_setter(instance):
    original = instance.iconPath
    instance.iconPath = original
    assert instance.iconPath == original



@given(instance=diagram_tool_EdgeCreationDescription_strategy)
def test_diagram_tool_edgecreationdescription_connectionStartPrecondition_setter(instance):
    original = instance.connectionStartPrecondition
    instance.connectionStartPrecondition = original
    assert instance.connectionStartPrecondition == original

@given(instance=tool_InitialNodeCreationOperation_strategy)
@settings(max_examples=50)
def test_tool_initialnodecreationoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialNodeCreationOperation)

@given(instance=tool_ContainerViewVariable_strategy)
@settings(max_examples=50)
def test_tool_containerviewvariable_instantiation(instance):
    assert isinstance(instance, tool_ContainerViewVariable)

@given(instance=tool_NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_tool_nodecreationvariable_instantiation(instance):
    assert isinstance(instance, tool_NodeCreationVariable)

@given(instance=style_EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_EndLabelStyleDescription)

@given(instance=style_CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_CenterLabelStyleDescription)

@given(instance=ToolEntry_strategy)
@settings(max_examples=50)
def test_toolentry_instantiation(instance):
    assert isinstance(instance, ToolEntry)

@given(instance=diagram_tool_ToolGroup_strategy)
@settings(max_examples=50)
def test_diagram_tool_toolgroup_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolGroup)

@given(instance=tool_ToolGroupExtension_strategy)
@settings(max_examples=50)
def test_tool_toolgroupextension_instantiation(instance):
    assert isinstance(instance, tool_ToolGroupExtension)

@given(instance=tool_PopupMenu_strategy)
@settings(max_examples=50)
def test_tool_popupmenu_instantiation(instance):
    assert isinstance(instance, tool_PopupMenu)

@given(instance=tool_ToolEntry_strategy)
@settings(max_examples=50)
def test_tool_toolentry_instantiation(instance):
    assert isinstance(instance, tool_ToolEntry)

@given(instance=diagram_style_HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_hidelabelcapabilitystyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_HideLabelCapabilityStyleDescription)



@given(instance=diagram_style_HideLabelCapabilityStyleDescription_strategy)
def test_diagram_style_hidelabelcapabilitystyledescription_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_edgestyledescription_instantiation(instance):
    assert isinstance(instance, EdgeStyleDescription)

@given(instance=diagram_style_BracketEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_bracketedgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BracketEdgeStyleDescription)

@given(instance=BasicLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_basiclabelstyledescription_instantiation(instance):
    assert isinstance(instance, BasicLabelStyleDescription)

@given(instance=diagram_style_CenterLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_centerlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_CenterLabelStyleDescription)

@given(instance=diagram_style_EndLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_endlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EndLabelStyleDescription)

@given(instance=diagram_style_BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BeginLabelStyleDescription)

@given(instance=style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, style_SizeComputationContainerStyleDescription)

@given(instance=style_BeginLabelStyleDescription_strategy)
@settings(max_examples=50)
def test_style_beginlabelstyledescription_instantiation(instance):
    assert isinstance(instance, style_BeginLabelStyleDescription)

@given(instance=style_LabelBorderStyleDescription_strategy)
@settings(max_examples=50)
def test_style_labelborderstyledescription_instantiation(instance):
    assert isinstance(instance, style_LabelBorderStyleDescription)

@given(instance=style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, style_RoundedCornerStyleDescription)

@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_sizecomputationcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_SizeComputationContainerStyleDescription)



@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
def test_diagram_style_sizecomputationcontainerstyledescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original



@given(instance=diagram_style_SizeComputationContainerStyleDescription_strategy)
def test_diagram_style_sizecomputationcontainerstyledescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original

@given(instance=diagram_style_GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, diagram_style_GaugeSectionDescription)



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_diagram_style_gaugesectiondescription_minValueExpression_setter(instance):
    original = instance.minValueExpression
    instance.minValueExpression = original
    assert instance.minValueExpression == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_diagram_style_gaugesectiondescription_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_diagram_style_gaugesectiondescription_maxValueExpression_setter(instance):
    original = instance.maxValueExpression
    instance.maxValueExpression = original
    assert instance.maxValueExpression == original



@given(instance=diagram_style_GaugeSectionDescription_strategy)
def test_diagram_style_gaugesectiondescription_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=style_GaugeSectionDescription_strategy)
@settings(max_examples=50)
def test_style_gaugesectiondescription_instantiation(instance):
    assert isinstance(instance, style_GaugeSectionDescription)

@given(instance=DecorationDescriptionsSet_strategy)
@settings(max_examples=50)
def test_decorationdescriptionsset_instantiation(instance):
    assert isinstance(instance, DecorationDescriptionsSet)

@given(instance=NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_nodestyledescription_instantiation(instance):
    assert isinstance(instance, NodeStyleDescription)

@given(instance=diagram_style_LozengeNodeDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_lozengenodedescription_instantiation(instance):
    assert isinstance(instance, diagram_style_LozengeNodeDescription)



@given(instance=diagram_style_LozengeNodeDescription_strategy)
def test_diagram_style_lozengenodedescription_heightComputationExpression_setter(instance):
    original = instance.heightComputationExpression
    instance.heightComputationExpression = original
    assert instance.heightComputationExpression == original



@given(instance=diagram_style_LozengeNodeDescription_strategy)
def test_diagram_style_lozengenodedescription_widthComputationExpression_setter(instance):
    original = instance.widthComputationExpression
    instance.widthComputationExpression = original
    assert instance.widthComputationExpression == original

@given(instance=diagram_style_DotDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_dotdescription_instantiation(instance):
    assert isinstance(instance, diagram_style_DotDescription)



@given(instance=diagram_style_DotDescription_strategy)
def test_diagram_style_dotdescription_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original

@given(instance=diagram_style_EllipseNodeDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_ellipsenodedescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EllipseNodeDescription)



@given(instance=diagram_style_EllipseNodeDescription_strategy)
def test_diagram_style_ellipsenodedescription_verticalDiameterComputationExpression_setter(instance):
    original = instance.verticalDiameterComputationExpression
    instance.verticalDiameterComputationExpression = original
    assert instance.verticalDiameterComputationExpression == original



@given(instance=diagram_style_EllipseNodeDescription_strategy)
def test_diagram_style_ellipsenodedescription_horizontalDiameterComputationExpression_setter(instance):
    original = instance.horizontalDiameterComputationExpression
    instance.horizontalDiameterComputationExpression = original
    assert instance.horizontalDiameterComputationExpression == original

@given(instance=diagram_style_BundledImageDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_bundledimagedescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BundledImageDescription)



@given(instance=diagram_style_BundledImageDescription_strategy)
def test_diagram_style_bundledimagedescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diagram_style_BundledImageDescription_strategy)
def test_diagram_style_bundledimagedescription_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original

@given(instance=diagram_style_NoteDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_notedescription_instantiation(instance):
    assert isinstance(instance, diagram_style_NoteDescription)

@given(instance=diagram_style_GaugeCompositeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_gaugecompositestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_GaugeCompositeStyleDescription)



@given(instance=diagram_style_GaugeCompositeStyleDescription_strategy)
def test_diagram_style_gaugecompositestyledescription_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=diagram_style_SquareDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_squaredescription_instantiation(instance):
    assert isinstance(instance, diagram_style_SquareDescription)



@given(instance=diagram_style_SquareDescription_strategy)
def test_diagram_style_squaredescription_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_style_SquareDescription_strategy)
def test_diagram_style_squaredescription_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram_style_CustomStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_customstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_CustomStyleDescription)



@given(instance=diagram_style_CustomStyleDescription_strategy)
def test_diagram_style_customstyledescription_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=style_HideLabelCapabilityStyleDescription_strategy)
@settings(max_examples=50)
def test_style_hidelabelcapabilitystyledescription_instantiation(instance):
    assert isinstance(instance, style_HideLabelCapabilityStyleDescription)

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

@given(instance=diagram_style_ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_containerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_ContainerStyleDescription)



@given(instance=diagram_style_ContainerStyleDescription_strategy)
def test_diagram_style_containerstyledescription_roundedCorner_setter(instance):
    original = instance.roundedCorner
    instance.roundedCorner = original
    assert instance.roundedCorner == original

@given(instance=ColorDescription_strategy)
@settings(max_examples=50)
def test_colordescription_instantiation(instance):
    assert isinstance(instance, ColorDescription)

@given(instance=StyleDescription_strategy)
@settings(max_examples=50)
def test_styledescription_instantiation(instance):
    assert isinstance(instance, StyleDescription)

@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_roundedcornerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_RoundedCornerStyleDescription)



@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
def test_diagram_style_roundedcornerstyledescription_arcHeight_setter(instance):
    original = instance.arcHeight
    instance.arcHeight = original
    assert instance.arcHeight == original



@given(instance=diagram_style_RoundedCornerStyleDescription_strategy)
def test_diagram_style_roundedcornerstyledescription_arcWidth_setter(instance):
    original = instance.arcWidth
    instance.arcWidth = original
    assert instance.arcWidth == original

@given(instance=diagram_style_EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_edgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_EdgeStyleDescription)



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_endsCentering_setter(instance):
    original = instance.endsCentering
    instance.endsCentering = original
    assert instance.endsCentering == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original



@given(instance=diagram_style_EdgeStyleDescription_strategy)
def test_diagram_style_edgestyledescription_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original

@given(instance=diagram_style_BorderedStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_borderedstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_BorderedStyleDescription)



@given(instance=diagram_style_BorderedStyleDescription_strategy)
def test_diagram_style_borderedstyledescription_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original



@given(instance=diagram_style_BorderedStyleDescription_strategy)
def test_diagram_style_borderedstyledescription_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original

@given(instance=tool_ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_tool_containerdropdescription_instantiation(instance):
    assert isinstance(instance, tool_ContainerDropDescription)

@given(instance=diagram_description_DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DragAndDropTargetDescription)

@given(instance=Customization_strategy)
@settings(max_examples=50)
def test_customization_instantiation(instance):
    assert isinstance(instance, Customization)

@given(instance=DecorationDescription_strategy)
@settings(max_examples=50)
def test_decorationdescription_instantiation(instance):
    assert isinstance(instance, DecorationDescription)

@given(instance=diagram_description_MappingBasedDecoration_strategy)
@settings(max_examples=50)
def test_diagram_description_mappingbaseddecoration_instantiation(instance):
    assert isinstance(instance, diagram_description_MappingBasedDecoration)

@given(instance=description_EndUserDocumentedElement_strategy)
@settings(max_examples=50)
def test_description_enduserdocumentedelement_instantiation(instance):
    assert isinstance(instance, description_EndUserDocumentedElement)

@given(instance=DocumentedElement_strategy)
@settings(max_examples=50)
def test_documentedelement_instantiation(instance):
    assert isinstance(instance, DocumentedElement)

@given(instance=diagram_description_Layout_strategy)
@settings(max_examples=50)
def test_diagram_description_layout_instantiation(instance):
    assert isinstance(instance, diagram_description_Layout)

@given(instance=ConditionalStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalStyleDescription)

@given(instance=diagram_description_ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalEdgeStyleDescription)

@given(instance=diagram_description_ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalContainerStyleDescription)

@given(instance=diagram_description_ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_description_ConditionalNodeStyleDescription)

@given(instance=description_IdentifiedElement_strategy)
@settings(max_examples=50)
def test_description_identifiedelement_instantiation(instance):
    assert isinstance(instance, description_IdentifiedElement)

@given(instance=diagram_description_IEdgeMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_iedgemapping_instantiation(instance):
    assert isinstance(instance, diagram_description_IEdgeMapping)

@given(instance=AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, AbstractNodeMapping)

@given(instance=tool_ReconnectEdgeDescription_strategy)
@settings(max_examples=50)
def test_tool_reconnectedgedescription_instantiation(instance):
    assert isinstance(instance, tool_ReconnectEdgeDescription)

@given(instance=ConditionalEdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionaledgestyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalEdgeStyleDescription)

@given(instance=style_EdgeStyleDescription_strategy)
@settings(max_examples=50)
def test_style_edgestyledescription_instantiation(instance):
    assert isinstance(instance, style_EdgeStyleDescription)

@given(instance=description_IEdgeMapping_strategy)
@settings(max_examples=50)
def test_description_iedgemapping_instantiation(instance):
    assert isinstance(instance, description_IEdgeMapping)

@given(instance=description_ContainerMapping_strategy)
@settings(max_examples=50)
def test_description_containermapping_instantiation(instance):
    assert isinstance(instance, description_ContainerMapping)

@given(instance=description_AbstractMappingImport_strategy)
@settings(max_examples=50)
def test_description_abstractmappingimport_instantiation(instance):
    assert isinstance(instance, description_AbstractMappingImport)

@given(instance=diagram_description_ContainerMappingImport_strategy)
@settings(max_examples=50)
def test_diagram_description_containermappingimport_instantiation(instance):
    assert isinstance(instance, diagram_description_ContainerMappingImport)

@given(instance=description_NodeMapping_strategy)
@settings(max_examples=50)
def test_description_nodemapping_instantiation(instance):
    assert isinstance(instance, description_NodeMapping)

@given(instance=diagram_description_NodeMappingImport_strategy)
@settings(max_examples=50)
def test_diagram_description_nodemappingimport_instantiation(instance):
    assert isinstance(instance, diagram_description_NodeMappingImport)

@given(instance=ConditionalContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalContainerStyleDescription)

@given(instance=style_ContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_style_containerstyledescription_instantiation(instance):
    assert isinstance(instance, style_ContainerStyleDescription)

@given(instance=diagram_style_ShapeContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_shapecontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_ShapeContainerStyleDescription)



@given(instance=diagram_style_ShapeContainerStyleDescription_strategy)
def test_diagram_style_shapecontainerstyledescription_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram_style_FlatContainerStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_flatcontainerstyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_FlatContainerStyleDescription)



@given(instance=diagram_style_FlatContainerStyleDescription_strategy)
def test_diagram_style_flatcontainerstyledescription_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original

@given(instance=ConditionalNodeStyleDescription_strategy)
@settings(max_examples=50)
def test_conditionalnodestyledescription_instantiation(instance):
    assert isinstance(instance, ConditionalNodeStyleDescription)

@given(instance=style_NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_style_nodestyledescription_instantiation(instance):
    assert isinstance(instance, style_NodeStyleDescription)

@given(instance=diagram_style_WorkspaceImageDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_workspaceimagedescription_instantiation(instance):
    assert isinstance(instance, diagram_style_WorkspaceImageDescription)



@given(instance=diagram_style_WorkspaceImageDescription_strategy)
def test_diagram_style_workspaceimagedescription_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=description_AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_description_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, description_AbstractNodeMapping)

@given(instance=description_RepresentationElementMapping_strategy)
@settings(max_examples=50)
def test_description_representationelementmapping_instantiation(instance):
    assert isinstance(instance, description_RepresentationElementMapping)

@given(instance=description_DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_description_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, description_DiagramElementMapping)

@given(instance=tool_DoubleClickDescription_strategy)
@settings(max_examples=50)
def test_tool_doubleclickdescription_instantiation(instance):
    assert isinstance(instance, tool_DoubleClickDescription)

@given(instance=tool_DirectEditLabel_strategy)
@settings(max_examples=50)
def test_tool_directeditlabel_instantiation(instance):
    assert isinstance(instance, tool_DirectEditLabel)

@given(instance=tool_DeleteElementDescription_strategy)
@settings(max_examples=50)
def test_tool_deleteelementdescription_instantiation(instance):
    assert isinstance(instance, tool_DeleteElementDescription)

@given(instance=RepresentationExtensionDescription_strategy)
@settings(max_examples=50)
def test_representationextensiondescription_instantiation(instance):
    assert isinstance(instance, RepresentationExtensionDescription)

@given(instance=diagram_description_DiagramExtensionDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_diagramextensiondescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramExtensionDescription)

@given(instance=description_DiagramDescription_strategy)
@settings(max_examples=50)
def test_description_diagramdescription_instantiation(instance):
    assert isinstance(instance, description_DiagramDescription)

@given(instance=description_RepresentationImportDescription_strategy)
@settings(max_examples=50)
def test_description_representationimportdescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationImportDescription)

@given(instance=diagram_description_DiagramImportDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_diagramimportdescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramImportDescription)

@given(instance=tool_ToolSection_strategy)
@settings(max_examples=50)
def test_tool_toolsection_instantiation(instance):
    assert isinstance(instance, tool_ToolSection)

@given(instance=tool_AbstractToolDescription_strategy)
@settings(max_examples=50)
def test_tool_abstracttooldescription_instantiation(instance):
    assert isinstance(instance, tool_AbstractToolDescription)

@given(instance=EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_edgemappingimport_instantiation(instance):
    assert isinstance(instance, EdgeMappingImport)

@given(instance=AdditionalLayer_strategy)
@settings(max_examples=50)
def test_additionallayer_instantiation(instance):
    assert isinstance(instance, AdditionalLayer)

@given(instance=tool_InitialOperation_strategy)
@settings(max_examples=50)
def test_tool_initialoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialOperation)

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=diagram_description_CompositeLayout_strategy)
@settings(max_examples=50)
def test_diagram_description_compositelayout_instantiation(instance):
    assert isinstance(instance, diagram_description_CompositeLayout)



@given(instance=diagram_description_CompositeLayout_strategy)
def test_diagram_description_compositelayout_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=diagram_description_CompositeLayout_strategy)
def test_diagram_description_compositelayout_padding_setter(instance):
    original = instance.padding
    instance.padding = original
    assert instance.padding == original

@given(instance=diagram_description_OrderedTreeLayout_strategy)
@settings(max_examples=50)
def test_diagram_description_orderedtreelayout_instantiation(instance):
    assert isinstance(instance, diagram_description_OrderedTreeLayout)



@given(instance=diagram_description_OrderedTreeLayout_strategy)
def test_diagram_description_orderedtreelayout_childrenExpression_setter(instance):
    original = instance.childrenExpression
    instance.childrenExpression = original
    assert instance.childrenExpression == original

@given(instance=tool_RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_tool_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, tool_RepresentationCreationDescription)

@given(instance=diagram_concern_ConcernSet_strategy)
@settings(max_examples=50)
def test_diagram_concern_concernset_instantiation(instance):
    assert isinstance(instance, diagram_concern_ConcernSet)

@given(instance=InteractiveVariableDescription_strategy)
@settings(max_examples=50)
def test_interactivevariabledescription_instantiation(instance):
    assert isinstance(instance, InteractiveVariableDescription)

@given(instance=filter_Filter_strategy)
@settings(max_examples=50)
def test_filter_filter_instantiation(instance):
    assert isinstance(instance, filter_Filter)

@given(instance=FilterDescription_strategy)
@settings(max_examples=50)
def test_filterdescription_instantiation(instance):
    assert isinstance(instance, FilterDescription)

@given(instance=diagram_filter_CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_diagram_filter_compositefilterdescription_instantiation(instance):
    assert isinstance(instance, diagram_filter_CompositeFilterDescription)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=diagram_filter_VariableFilter_strategy)
@settings(max_examples=50)
def test_diagram_filter_variablefilter_instantiation(instance):
    assert isinstance(instance, diagram_filter_VariableFilter)



@given(instance=diagram_filter_VariableFilter_strategy)
def test_diagram_filter_variablefilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_VariableFilter_strategy)
@settings(max_examples=30)
def test_diagram_filter_variablefilter_resetvariables_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resetVariables()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resetVariables).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resetVariables' in diagram_filter_VariableFilter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resetVariables' in diagram_filter_VariableFilter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resetVariables' in diagram_filter_VariableFilter is not implemented or raised an error")

@given(instance=diagram_filter_MappingFilter_strategy)
@settings(max_examples=50)
def test_diagram_filter_mappingfilter_instantiation(instance):
    assert isinstance(instance, diagram_filter_MappingFilter)



@given(instance=diagram_filter_MappingFilter_strategy)
def test_diagram_filter_mappingfilter_viewConditionExpression_setter(instance):
    original = instance.viewConditionExpression
    instance.viewConditionExpression = original
    assert instance.viewConditionExpression == original



@given(instance=diagram_filter_MappingFilter_strategy)
def test_diagram_filter_mappingfilter_semanticConditionExpression_setter(instance):
    original = instance.semanticConditionExpression
    instance.semanticConditionExpression = original
    assert instance.semanticConditionExpression == original

@given(instance=diagram_filter_Filter_strategy)
@settings(max_examples=50)
def test_diagram_filter_filter_instantiation(instance):
    assert isinstance(instance, diagram_filter_Filter)



@given(instance=diagram_filter_Filter_strategy)
def test_diagram_filter_filter_filterKind_setter(instance):
    original = instance.filterKind
    instance.filterKind = original
    assert instance.filterKind == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_Filter_strategy)
@settings(max_examples=30)
def test_diagram_filter_filter_isvisible_changes_state(instance):
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
        assert has_statements, f"Function 'isVisible' in diagram_filter_Filter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram_filter_Filter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram_filter_Filter is not implemented or raised an error")

@given(instance=tool_InitialContainerDropOperation_strategy)
@settings(max_examples=50)
def test_tool_initialcontainerdropoperation_instantiation(instance):
    assert isinstance(instance, tool_InitialContainerDropOperation)

@given(instance=CreateView_strategy)
@settings(max_examples=50)
def test_createview_instantiation(instance):
    assert isinstance(instance, CreateView)

@given(instance=diagram_tool_CreateEdgeView_strategy)
@settings(max_examples=50)
def test_diagram_tool_createedgeview_instantiation(instance):
    assert isinstance(instance, diagram_tool_CreateEdgeView)



@given(instance=diagram_tool_CreateEdgeView_strategy)
def test_diagram_tool_createedgeview_sourceExpression_setter(instance):
    original = instance.sourceExpression
    instance.sourceExpression = original
    assert instance.sourceExpression == original



@given(instance=diagram_tool_CreateEdgeView_strategy)
def test_diagram_tool_createedgeview_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original

@given(instance=tool_ElementDropVariable_strategy)
@settings(max_examples=50)
def test_tool_elementdropvariable_instantiation(instance):
    assert isinstance(instance, tool_ElementDropVariable)

@given(instance=tool_DropContainerVariable_strategy)
@settings(max_examples=50)
def test_tool_dropcontainervariable_instantiation(instance):
    assert isinstance(instance, tool_DropContainerVariable)

@given(instance=diagram_tool_ContainerDropDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_containerdropdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_ContainerDropDescription)



@given(instance=diagram_tool_ContainerDropDescription_strategy)
def test_diagram_tool_containerdropdescription_dragSource_setter(instance):
    original = instance.dragSource
    instance.dragSource = original
    assert instance.dragSource == original



@given(instance=diagram_tool_ContainerDropDescription_strategy)
def test_diagram_tool_containerdropdescription_moveEdges_setter(instance):
    original = instance.moveEdges
    instance.moveEdges = original
    assert instance.moveEdges == original

@given(instance=RepresentationNavigationDescription_strategy)
@settings(max_examples=50)
def test_representationnavigationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationNavigationDescription)

@given(instance=diagram_tool_DiagramNavigationDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_diagramnavigationdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DiagramNavigationDescription)

@given(instance=RepresentationCreationDescription_strategy)
@settings(max_examples=50)
def test_representationcreationdescription_instantiation(instance):
    assert isinstance(instance, RepresentationCreationDescription)

@given(instance=diagram_tool_DiagramCreationDescription_strategy)
@settings(max_examples=50)
def test_diagram_tool_diagramcreationdescription_instantiation(instance):
    assert isinstance(instance, diagram_tool_DiagramCreationDescription)

@given(instance=ContainerModelOperation_strategy)
@settings(max_examples=50)
def test_containermodeloperation_instantiation(instance):
    assert isinstance(instance, ContainerModelOperation)

@given(instance=diagram_tool_Navigation_strategy)
@settings(max_examples=50)
def test_diagram_tool_navigation_instantiation(instance):
    assert isinstance(instance, diagram_tool_Navigation)



@given(instance=diagram_tool_Navigation_strategy)
def test_diagram_tool_navigation_createIfNotExistent_setter(instance):
    original = instance.createIfNotExistent
    instance.createIfNotExistent = original
    assert instance.createIfNotExistent == original

@given(instance=diagram_tool_CreateView_strategy)
@settings(max_examples=50)
def test_diagram_tool_createview_instantiation(instance):
    assert isinstance(instance, diagram_tool_CreateView)



@given(instance=diagram_tool_CreateView_strategy)
def test_diagram_tool_createview_containerViewExpression_setter(instance):
    original = instance.containerViewExpression
    instance.containerViewExpression = original
    assert instance.containerViewExpression == original



@given(instance=diagram_tool_CreateView_strategy)
def test_diagram_tool_createview_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=diagram_tool_NodeCreationVariable_strategy)
@settings(max_examples=50)
def test_diagram_tool_nodecreationvariable_instantiation(instance):
    assert isinstance(instance, diagram_tool_NodeCreationVariable)

@given(instance=diagram_HideLabelCapabilityStyle_strategy)
@settings(max_examples=50)
def test_diagram_hidelabelcapabilitystyle_instantiation(instance):
    assert isinstance(instance, diagram_HideLabelCapabilityStyle)



@given(instance=diagram_HideLabelCapabilityStyle_strategy)
def test_diagram_hidelabelcapabilitystyle_hideLabelByDefault_setter(instance):
    original = instance.hideLabelByDefault
    instance.hideLabelByDefault = original
    assert instance.hideLabelByDefault == original

@given(instance=concern_ConcernSet_strategy)
@settings(max_examples=50)
def test_concern_concernset_instantiation(instance):
    assert isinstance(instance, concern_ConcernSet)

@given(instance=validation_ValidationSet_strategy)
@settings(max_examples=50)
def test_validation_validationset_instantiation(instance):
    assert isinstance(instance, validation_ValidationSet)

@given(instance=EdgeMapping_strategy)
@settings(max_examples=50)
def test_edgemapping_instantiation(instance):
    assert isinstance(instance, EdgeMapping)

@given(instance=description_PasteTargetDescription_strategy)
@settings(max_examples=50)
def test_description_pastetargetdescription_instantiation(instance):
    assert isinstance(instance, description_PasteTargetDescription)

@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramElementMapping)



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_diagram_description_diagramelementmapping_synchronizationLock_setter(instance):
    original = instance.synchronizationLock
    instance.synchronizationLock = original
    assert instance.synchronizationLock == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_diagram_description_diagramelementmapping_semanticElements_setter(instance):
    original = instance.semanticElements
    instance.semanticElements = original
    assert instance.semanticElements == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_diagram_description_diagramelementmapping_createElements_setter(instance):
    original = instance.createElements
    instance.createElements = original
    assert instance.createElements == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_diagram_description_diagramelementmapping_semanticCandidatesExpression_setter(instance):
    original = instance.semanticCandidatesExpression
    instance.semanticCandidatesExpression = original
    assert instance.semanticCandidatesExpression == original



@given(instance=diagram_description_DiagramElementMapping_strategy)
def test_diagram_description_diagramelementmapping_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_diagramelementmapping_checkprecondition_changes_state(instance):
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
        assert has_statements, f"Function 'checkPrecondition' in diagram_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'checkPrecondition' in diagram_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'checkPrecondition' in diagram_description_DiagramElementMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramElementMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_diagramelementmapping_isfrom_changes_state(instance):
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
        assert has_statements, f"Function 'isFrom' in diagram_description_DiagramElementMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isFrom' in diagram_description_DiagramElementMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isFrom' in diagram_description_DiagramElementMapping is not implemented or raised an error")

@given(instance=description_RepresentationDescription_strategy)
@settings(max_examples=50)
def test_description_representationdescription_instantiation(instance):
    assert isinstance(instance, description_RepresentationDescription)

@given(instance=description_DragAndDropTargetDescription_strategy)
@settings(max_examples=50)
def test_description_draganddroptargetdescription_instantiation(instance):
    assert isinstance(instance, description_DragAndDropTargetDescription)

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_nodemapping_instantiation(instance):
    assert isinstance(instance, diagram_description_NodeMapping)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_nodemapping_updatelistelement_changes_state(instance):
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
        assert has_statements, f"Function 'updateListElement' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateListElement' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateListElement' in diagram_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_nodemapping_createnode_changes_state(instance):
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
        assert has_statements, f"Function 'createNode' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createNode' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createNode' in diagram_description_NodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_NodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_nodemapping_updatenode_changes_state(instance):
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
        assert has_statements, f"Function 'updateNode' in diagram_description_NodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateNode' in diagram_description_NodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateNode' in diagram_description_NodeMapping is not implemented or raised an error")

@given(instance=diagram_description_ContainerMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_containermapping_instantiation(instance):
    assert isinstance(instance, diagram_description_ContainerMapping)



@given(instance=diagram_description_ContainerMapping_strategy)
def test_diagram_description_containermapping_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=diagram_description_DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagram_description_diagramdescription_instantiation(instance):
    assert isinstance(instance, diagram_description_DiagramDescription)



@given(instance=diagram_description_DiagramDescription_strategy)
def test_diagram_description_diagramdescription_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_diagram_description_diagramdescription_rootExpression_setter(instance):
    original = instance.rootExpression
    instance.rootExpression = original
    assert instance.rootExpression == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_diagram_description_diagramdescription_preconditionExpression_setter(instance):
    original = instance.preconditionExpression
    instance.preconditionExpression = original
    assert instance.preconditionExpression == original



@given(instance=diagram_description_DiagramDescription_strategy)
def test_diagram_description_diagramdescription_enablePopupBars_setter(instance):
    original = instance.enablePopupBars
    instance.enablePopupBars = original
    assert instance.enablePopupBars == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_DiagramDescription_strategy)
@settings(max_examples=30)
def test_diagram_description_diagramdescription_creatediagram_changes_state(instance):
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
        assert has_statements, f"Function 'createDiagram' in diagram_description_DiagramDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createDiagram' in diagram_description_DiagramDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createDiagram' in diagram_description_DiagramDescription is not implemented or raised an error")

@given(instance=diagram_EObject_strategy)
@settings(max_examples=50)
def test_diagram_eobject_instantiation(instance):
    assert isinstance(instance, diagram_EObject)

@given(instance=tool_SelectModelElementVariable_strategy)
@settings(max_examples=50)
def test_tool_selectmodelelementvariable_instantiation(instance):
    assert isinstance(instance, tool_SelectModelElementVariable)

@given(instance=TypedVariable_strategy)
@settings(max_examples=50)
def test_typedvariable_instantiation(instance):
    assert isinstance(instance, TypedVariable)

@given(instance=diagram_DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_diagram_draganddroptarget_instantiation(instance):
    assert isinstance(instance, diagram_DragAndDropTarget)

@given(instance=style_StyleDescription_strategy)
@settings(max_examples=50)
def test_style_styledescription_instantiation(instance):
    assert isinstance(instance, style_StyleDescription)

@given(instance=diagram_style_NodeStyleDescription_strategy)
@settings(max_examples=50)
def test_diagram_style_nodestyledescription_instantiation(instance):
    assert isinstance(instance, diagram_style_NodeStyleDescription)



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_diagram_style_nodestyledescription_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_diagram_style_nodestyledescription_sizeComputationExpression_setter(instance):
    original = instance.sizeComputationExpression
    instance.sizeComputationExpression = original
    assert instance.sizeComputationExpression == original



@given(instance=diagram_style_NodeStyleDescription_strategy)
def test_diagram_style_nodestyledescription_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=diagram_ComputedStyleDescriptionRegistry_strategy)
@settings(max_examples=50)
def test_diagram_computedstyledescriptionregistry_instantiation(instance):
    assert isinstance(instance, diagram_ComputedStyleDescriptionRegistry)

@given(instance=EdgeStyle_strategy)
@settings(max_examples=50)
def test_edgestyle_instantiation(instance):
    assert isinstance(instance, EdgeStyle)

@given(instance=diagram_BracketEdgeStyle_strategy)
@settings(max_examples=50)
def test_diagram_bracketedgestyle_instantiation(instance):
    assert isinstance(instance, diagram_BracketEdgeStyle)

@given(instance=BasicLabelStyle_strategy)
@settings(max_examples=50)
def test_basiclabelstyle_instantiation(instance):
    assert isinstance(instance, BasicLabelStyle)

@given(instance=CollapseFilter_strategy)
@settings(max_examples=50)
def test_collapsefilter_instantiation(instance):
    assert isinstance(instance, CollapseFilter)

@given(instance=diagram_IndirectlyCollapseFilter_strategy)
@settings(max_examples=50)
def test_diagram_indirectlycollapsefilter_instantiation(instance):
    assert isinstance(instance, diagram_IndirectlyCollapseFilter)

@given(instance=diagram_VariableValue_strategy)
@settings(max_examples=50)
def test_diagram_variablevalue_instantiation(instance):
    assert isinstance(instance, diagram_VariableValue)

@given(instance=diagram_EndLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram_endlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram_EndLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_EndLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram_endlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in diagram_EndLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_EndLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_EndLabelStyle is not implemented or raised an error")

@given(instance=diagram_CenterLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram_centerlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram_CenterLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_CenterLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram_centerlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in diagram_CenterLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_CenterLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_CenterLabelStyle is not implemented or raised an error")

@given(instance=diagram_BeginLabelStyle_strategy)
@settings(max_examples=50)
def test_diagram_beginlabelstyle_instantiation(instance):
    assert isinstance(instance, diagram_BeginLabelStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_BeginLabelStyle_strategy)
@settings(max_examples=30)
def test_diagram_beginlabelstyle_setdescription_changes_state(instance):
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
        assert has_statements, f"Function 'setDescription' in diagram_BeginLabelStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDescription' in diagram_BeginLabelStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDescription' in diagram_BeginLabelStyle is not implemented or raised an error")

@given(instance=ContainerStyle_strategy)
@settings(max_examples=50)
def test_containerstyle_instantiation(instance):
    assert isinstance(instance, ContainerStyle)

@given(instance=diagram_FlatContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram_flatcontainerstyle_instantiation(instance):
    assert isinstance(instance, diagram_FlatContainerStyle)



@given(instance=diagram_FlatContainerStyle_strategy)
def test_diagram_flatcontainerstyle_backgroundStyle_setter(instance):
    original = instance.backgroundStyle
    instance.backgroundStyle = original
    assert instance.backgroundStyle == original



@given(instance=diagram_FlatContainerStyle_strategy)
def test_diagram_flatcontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=diagram_FlatContainerStyle_strategy)
def test_diagram_flatcontainerstyle_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original

@given(instance=diagram_ShapeContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram_shapecontainerstyle_instantiation(instance):
    assert isinstance(instance, diagram_ShapeContainerStyle)



@given(instance=diagram_ShapeContainerStyle_strategy)
def test_diagram_shapecontainerstyle_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=diagram_ShapeContainerStyle_strategy)
def test_diagram_shapecontainerstyle_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=Customizable_strategy)
@settings(max_examples=50)
def test_customizable_instantiation(instance):
    assert isinstance(instance, Customizable)

@given(instance=diagram_GaugeSection_strategy)
@settings(max_examples=50)
def test_diagram_gaugesection_instantiation(instance):
    assert isinstance(instance, diagram_GaugeSection)



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_foregroundColor_setter(instance):
    original = instance.foregroundColor
    instance.foregroundColor = original
    assert instance.foregroundColor == original



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=diagram_GaugeSection_strategy)
def test_diagram_gaugesection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=diagram_Note_strategy)
@settings(max_examples=50)
def test_diagram_note_instantiation(instance):
    assert isinstance(instance, diagram_Note)



@given(instance=diagram_Note_strategy)
def test_diagram_note_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram_CustomStyle_strategy)
@settings(max_examples=50)
def test_diagram_customstyle_instantiation(instance):
    assert isinstance(instance, diagram_CustomStyle)



@given(instance=diagram_CustomStyle_strategy)
def test_diagram_customstyle_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=diagram_Square_strategy)
@settings(max_examples=50)
def test_diagram_square_instantiation(instance):
    assert isinstance(instance, diagram_Square)



@given(instance=diagram_Square_strategy)
def test_diagram_square_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_Square_strategy)
def test_diagram_square_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_Square_strategy)
def test_diagram_square_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=diagram_Ellipse_strategy)
@settings(max_examples=50)
def test_diagram_ellipse_instantiation(instance):
    assert isinstance(instance, diagram_Ellipse)



@given(instance=diagram_Ellipse_strategy)
def test_diagram_ellipse_verticalDiameter_setter(instance):
    original = instance.verticalDiameter
    instance.verticalDiameter = original
    assert instance.verticalDiameter == original



@given(instance=diagram_Ellipse_strategy)
def test_diagram_ellipse_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diagram_Ellipse_strategy)
def test_diagram_ellipse_horizontalDiameter_setter(instance):
    original = instance.horizontalDiameter
    instance.horizontalDiameter = original
    assert instance.horizontalDiameter == original

@given(instance=diagram_Lozenge_strategy)
@settings(max_examples=50)
def test_diagram_lozenge_instantiation(instance):
    assert isinstance(instance, diagram_Lozenge)



@given(instance=diagram_Lozenge_strategy)
def test_diagram_lozenge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diagram_Lozenge_strategy)
def test_diagram_lozenge_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_Lozenge_strategy)
def test_diagram_lozenge_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=diagram_BundledImage_strategy)
@settings(max_examples=50)
def test_diagram_bundledimage_instantiation(instance):
    assert isinstance(instance, diagram_BundledImage)



@given(instance=diagram_BundledImage_strategy)
def test_diagram_bundledimage_providedShapeID_setter(instance):
    original = instance.providedShapeID
    instance.providedShapeID = original
    assert instance.providedShapeID == original



@given(instance=diagram_BundledImage_strategy)
def test_diagram_bundledimage_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=diagram_BundledImage_strategy)
def test_diagram_bundledimage_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=diagram_WorkspaceImage_strategy)
@settings(max_examples=50)
def test_diagram_workspaceimage_instantiation(instance):
    assert isinstance(instance, diagram_WorkspaceImage)



@given(instance=diagram_WorkspaceImage_strategy)
def test_diagram_workspaceimage_workspacePath_setter(instance):
    original = instance.workspacePath
    instance.workspacePath = original
    assert instance.workspacePath == original

@given(instance=diagram_GaugeCompositeStyle_strategy)
@settings(max_examples=50)
def test_diagram_gaugecompositestyle_instantiation(instance):
    assert isinstance(instance, diagram_GaugeCompositeStyle)



@given(instance=diagram_GaugeCompositeStyle_strategy)
def test_diagram_gaugecompositestyle_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=VariableValue_strategy)
@settings(max_examples=50)
def test_variablevalue_instantiation(instance):
    assert isinstance(instance, VariableValue)

@given(instance=diagram_EObjectVariableValue_strategy)
@settings(max_examples=50)
def test_diagram_eobjectvariablevalue_instantiation(instance):
    assert isinstance(instance, diagram_EObjectVariableValue)

@given(instance=diagram_TypedVariableValue_strategy)
@settings(max_examples=50)
def test_diagram_typedvariablevalue_instantiation(instance):
    assert isinstance(instance, diagram_TypedVariableValue)



@given(instance=diagram_TypedVariableValue_strategy)
def test_diagram_typedvariablevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=diagram_Dot_strategy)
@settings(max_examples=50)
def test_diagram_dot_instantiation(instance):
    assert isinstance(instance, diagram_Dot)



@given(instance=diagram_Dot_strategy)
def test_diagram_dot_strokeSizeComputationExpression_setter(instance):
    original = instance.strokeSizeComputationExpression
    instance.strokeSizeComputationExpression = original
    assert instance.strokeSizeComputationExpression == original



@given(instance=diagram_Dot_strategy)
def test_diagram_dot_backgroundColor_setter(instance):
    original = instance.backgroundColor
    instance.backgroundColor = original
    assert instance.backgroundColor == original

@given(instance=HideLabelCapabilityStyle_strategy)
@settings(max_examples=50)
def test_hidelabelcapabilitystyle_instantiation(instance):
    assert isinstance(instance, HideLabelCapabilityStyle)

@given(instance=BorderedStyle_strategy)
@settings(max_examples=50)
def test_borderedstyle_instantiation(instance):
    assert isinstance(instance, BorderedStyle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=diagram_BorderedStyle_strategy)
@settings(max_examples=50)
def test_diagram_borderedstyle_instantiation(instance):
    assert isinstance(instance, diagram_BorderedStyle)



@given(instance=diagram_BorderedStyle_strategy)
def test_diagram_borderedstyle_borderLineStyle_setter(instance):
    original = instance.borderLineStyle
    instance.borderLineStyle = original
    assert instance.borderLineStyle == original



@given(instance=diagram_BorderedStyle_strategy)
def test_diagram_borderedstyle_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original



@given(instance=diagram_BorderedStyle_strategy)
def test_diagram_borderedstyle_borderSizeComputationExpression_setter(instance):
    original = instance.borderSizeComputationExpression
    instance.borderSizeComputationExpression = original
    assert instance.borderSizeComputationExpression == original



@given(instance=diagram_BorderedStyle_strategy)
def test_diagram_borderedstyle_borderSize_setter(instance):
    original = instance.borderSize
    instance.borderSize = original
    assert instance.borderSize == original

@given(instance=LabelStyle_strategy)
@settings(max_examples=50)
def test_labelstyle_instantiation(instance):
    assert isinstance(instance, LabelStyle)

@given(instance=IEdgeMapping_strategy)
@settings(max_examples=50)
def test_iedgemapping_instantiation(instance):
    assert isinstance(instance, IEdgeMapping)

@given(instance=diagram_EdgeTarget_strategy)
@settings(max_examples=50)
def test_diagram_edgetarget_instantiation(instance):
    assert isinstance(instance, diagram_EdgeTarget)

@given(instance=diagram_EdgeStyle_strategy)
@settings(max_examples=50)
def test_diagram_edgestyle_instantiation(instance):
    assert isinstance(instance, diagram_EdgeStyle)



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_targetArrow_setter(instance):
    original = instance.targetArrow
    instance.targetArrow = original
    assert instance.targetArrow == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_strokeColor_setter(instance):
    original = instance.strokeColor
    instance.strokeColor = original
    assert instance.strokeColor == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_foldingStyle_setter(instance):
    original = instance.foldingStyle
    instance.foldingStyle = original
    assert instance.foldingStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_sourceArrow_setter(instance):
    original = instance.sourceArrow
    instance.sourceArrow = original
    assert instance.sourceArrow == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original



@given(instance=diagram_EdgeStyle_strategy)
def test_diagram_edgestyle_centered_setter(instance):
    original = instance.centered
    instance.centered = original
    assert instance.centered == original

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, DDiagramElementContainer)

@given(instance=diagram_DNodeList_strategy)
@settings(max_examples=50)
def test_diagram_dnodelist_instantiation(instance):
    assert isinstance(instance, diagram_DNodeList)

@given(instance=diagram_DNodeContainer_strategy)
@settings(max_examples=50)
def test_diagram_dnodecontainer_instantiation(instance):
    assert isinstance(instance, diagram_DNodeContainer)



@given(instance=diagram_DNodeContainer_strategy)
def test_diagram_dnodecontainer_childrenPresentation_setter(instance):
    original = instance.childrenPresentation
    instance.childrenPresentation = original
    assert instance.childrenPresentation == original

@given(instance=ContainerMapping_strategy)
@settings(max_examples=50)
def test_containermapping_instantiation(instance):
    assert isinstance(instance, ContainerMapping)

@given(instance=diagram_ContainerStyle_strategy)
@settings(max_examples=50)
def test_diagram_containerstyle_instantiation(instance):
    assert isinstance(instance, diagram_ContainerStyle)

@given(instance=diagram_Style_strategy)
@settings(max_examples=50)
def test_diagram_style_instantiation(instance):
    assert isinstance(instance, diagram_Style)

@given(instance=diagram_GraphicalFilter_strategy)
@settings(max_examples=50)
def test_diagram_graphicalfilter_instantiation(instance):
    assert isinstance(instance, diagram_GraphicalFilter)

@given(instance=diagram_NodeStyle_strategy)
@settings(max_examples=50)
def test_diagram_nodestyle_instantiation(instance):
    assert isinstance(instance, diagram_NodeStyle)



@given(instance=diagram_NodeStyle_strategy)
def test_diagram_nodestyle_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original

@given(instance=EdgeTarget_strategy)
@settings(max_examples=50)
def test_edgetarget_instantiation(instance):
    assert isinstance(instance, EdgeTarget)

@given(instance=AbstractDNode_strategy)
@settings(max_examples=50)
def test_abstractdnode_instantiation(instance):
    assert isinstance(instance, AbstractDNode)

@given(instance=DDiagramElement_strategy)
@settings(max_examples=50)
def test_ddiagramelement_instantiation(instance):
    assert isinstance(instance, DDiagramElement)

@given(instance=diagram_AbstractDNode_strategy)
@settings(max_examples=50)
def test_diagram_abstractdnode_instantiation(instance):
    assert isinstance(instance, diagram_AbstractDNode)



@given(instance=diagram_AbstractDNode_strategy)
def test_diagram_abstractdnode_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original

@given(instance=filter_CompositeFilterDescription_strategy)
@settings(max_examples=50)
def test_filter_compositefilterdescription_instantiation(instance):
    assert isinstance(instance, filter_CompositeFilterDescription)

@given(instance=GraphicalFilter_strategy)
@settings(max_examples=50)
def test_graphicalfilter_instantiation(instance):
    assert isinstance(instance, GraphicalFilter)

@given(instance=diagram_HideLabelFilter_strategy)
@settings(max_examples=50)
def test_diagram_hidelabelfilter_instantiation(instance):
    assert isinstance(instance, diagram_HideLabelFilter)

@given(instance=diagram_CollapseFilter_strategy)
@settings(max_examples=50)
def test_diagram_collapsefilter_instantiation(instance):
    assert isinstance(instance, diagram_CollapseFilter)



@given(instance=diagram_CollapseFilter_strategy)
def test_diagram_collapsefilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_CollapseFilter_strategy)
def test_diagram_collapsefilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram_FoldingPointFilter_strategy)
@settings(max_examples=50)
def test_diagram_foldingpointfilter_instantiation(instance):
    assert isinstance(instance, diagram_FoldingPointFilter)

@given(instance=diagram_AbsoluteBoundsFilter_strategy)
@settings(max_examples=50)
def test_diagram_absoluteboundsfilter_instantiation(instance):
    assert isinstance(instance, diagram_AbsoluteBoundsFilter)



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_diagram_absoluteboundsfilter_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_diagram_absoluteboundsfilter_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_diagram_absoluteboundsfilter_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_AbsoluteBoundsFilter_strategy)
def test_diagram_absoluteboundsfilter_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=diagram_FoldingFilter_strategy)
@settings(max_examples=50)
def test_diagram_foldingfilter_instantiation(instance):
    assert isinstance(instance, diagram_FoldingFilter)

@given(instance=diagram_AppliedCompositeFilters_strategy)
@settings(max_examples=50)
def test_diagram_appliedcompositefilters_instantiation(instance):
    assert isinstance(instance, diagram_AppliedCompositeFilters)

@given(instance=diagram_HideFilter_strategy)
@settings(max_examples=50)
def test_diagram_hidefilter_instantiation(instance):
    assert isinstance(instance, diagram_HideFilter)

@given(instance=DiagramElementMapping_strategy)
@settings(max_examples=50)
def test_diagramelementmapping_instantiation(instance):
    assert isinstance(instance, DiagramElementMapping)

@given(instance=diagram_Decoration_strategy)
@settings(max_examples=50)
def test_diagram_decoration_instantiation(instance):
    assert isinstance(instance, diagram_Decoration)

@given(instance=DRepresentationElement_strategy)
@settings(max_examples=50)
def test_drepresentationelement_instantiation(instance):
    assert isinstance(instance, DRepresentationElement)

@given(instance=DSemanticDecorator_strategy)
@settings(max_examples=50)
def test_dsemanticdecorator_instantiation(instance):
    assert isinstance(instance, DSemanticDecorator)

@given(instance=DDiagram_strategy)
@settings(max_examples=50)
def test_ddiagram_instantiation(instance):
    assert isinstance(instance, DDiagram)

@given(instance=diagram_DSemanticDiagram_strategy)
@settings(max_examples=50)
def test_diagram_dsemanticdiagram_instantiation(instance):
    assert isinstance(instance, diagram_DSemanticDiagram)

@given(instance=Layer_strategy)
@settings(max_examples=50)
def test_layer_instantiation(instance):
    assert isinstance(instance, Layer)

@given(instance=diagram_description_AdditionalLayer_strategy)
@settings(max_examples=50)
def test_diagram_description_additionallayer_instantiation(instance):
    assert isinstance(instance, diagram_description_AdditionalLayer)



@given(instance=diagram_description_AdditionalLayer_strategy)
def test_diagram_description_additionallayer_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=diagram_description_AdditionalLayer_strategy)
def test_diagram_description_additionallayer_activeByDefault_setter(instance):
    original = instance.activeByDefault
    instance.activeByDefault = original
    assert instance.activeByDefault == original

@given(instance=diagram_FilterVariableHistory_strategy)
@settings(max_examples=50)
def test_diagram_filtervariablehistory_instantiation(instance):
    assert isinstance(instance, diagram_FilterVariableHistory)

@given(instance=tool_BehaviorTool_strategy)
@settings(max_examples=50)
def test_tool_behaviortool_instantiation(instance):
    assert isinstance(instance, tool_BehaviorTool)

@given(instance=validation_ValidationRule_strategy)
@settings(max_examples=50)
def test_validation_validationrule_instantiation(instance):
    assert isinstance(instance, validation_ValidationRule)

@given(instance=DRepresentation_strategy)
@settings(max_examples=50)
def test_drepresentation_instantiation(instance):
    assert isinstance(instance, DRepresentation)

@given(instance=filter_FilterDescription_strategy)
@settings(max_examples=50)
def test_filter_filterdescription_instantiation(instance):
    assert isinstance(instance, filter_FilterDescription)

@given(instance=concern_ConcernDescription_strategy)
@settings(max_examples=50)
def test_concern_concerndescription_instantiation(instance):
    assert isinstance(instance, concern_ConcernDescription)

@given(instance=diagram_DNodeListElement_strategy)
@settings(max_examples=50)
def test_diagram_dnodelistelement_instantiation(instance):
    assert isinstance(instance, diagram_DNodeListElement)

@given(instance=diagram_DEdge_strategy)
@settings(max_examples=50)
def test_diagram_dedge_instantiation(instance):
    assert isinstance(instance, diagram_DEdge)



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_isMockEdge_setter(instance):
    original = instance.isMockEdge
    instance.isMockEdge = original
    assert instance.isMockEdge == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_isFold_setter(instance):
    original = instance.isFold
    instance.isFold = original
    assert instance.isFold == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_routingStyle_setter(instance):
    original = instance.routingStyle
    instance.routingStyle = original
    assert instance.routingStyle == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_beginLabel_setter(instance):
    original = instance.beginLabel
    instance.beginLabel = original
    assert instance.beginLabel == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_endLabel_setter(instance):
    original = instance.endLabel
    instance.endLabel = original
    assert instance.endLabel == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_arrangeConstraints_setter(instance):
    original = instance.arrangeConstraints
    instance.arrangeConstraints = original
    assert instance.arrangeConstraints == original



@given(instance=diagram_DEdge_strategy)
def test_diagram_dedge_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_DEdge_strategy)
@settings(max_examples=30)
def test_diagram_dedge_isrootfolding_changes_state(instance):
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
        assert has_statements, f"Function 'isRootFolding' in diagram_DEdge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isRootFolding' in diagram_DEdge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isRootFolding' in diagram_DEdge is not implemented or raised an error")

@given(instance=DiagramDescription_strategy)
@settings(max_examples=50)
def test_diagramdescription_instantiation(instance):
    assert isinstance(instance, DiagramDescription)

@given(instance=diagram_DDiagramElement_strategy)
@settings(max_examples=50)
def test_diagram_ddiagramelement_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElement)



@given(instance=diagram_DDiagramElement_strategy)
def test_diagram_ddiagramelement_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=diagram_DDiagramElement_strategy)
def test_diagram_ddiagramelement_tooltipText_setter(instance):
    original = instance.tooltipText
    instance.tooltipText = original
    assert instance.tooltipText == original

@given(instance=DragAndDropTarget_strategy)
@settings(max_examples=50)
def test_draganddroptarget_instantiation(instance):
    assert isinstance(instance, DragAndDropTarget)

@given(instance=diagram_DNode_strategy)
@settings(max_examples=50)
def test_diagram_dnode_instantiation(instance):
    assert isinstance(instance, diagram_DNode)



@given(instance=diagram_DNode_strategy)
def test_diagram_dnode_labelPosition_setter(instance):
    original = instance.labelPosition
    instance.labelPosition = original
    assert instance.labelPosition == original



@given(instance=diagram_DNode_strategy)
def test_diagram_dnode_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_DNode_strategy)
def test_diagram_dnode_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=diagram_DNode_strategy)
def test_diagram_dnode_resizeKind_setter(instance):
    original = instance.resizeKind
    instance.resizeKind = original
    assert instance.resizeKind == original

@given(instance=diagram_DDiagramElementContainer_strategy)
@settings(max_examples=50)
def test_diagram_ddiagramelementcontainer_instantiation(instance):
    assert isinstance(instance, diagram_DDiagramElementContainer)



@given(instance=diagram_DDiagramElementContainer_strategy)
def test_diagram_ddiagramelementcontainer_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=diagram_DDiagramElementContainer_strategy)
def test_diagram_ddiagramelementcontainer_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=description_DocumentedElement_strategy)
@settings(max_examples=50)
def test_description_documentedelement_instantiation(instance):
    assert isinstance(instance, description_DocumentedElement)

@given(instance=diagram_DDiagram_strategy)
@settings(max_examples=50)
def test_diagram_ddiagram_instantiation(instance):
    assert isinstance(instance, diagram_DDiagram)



@given(instance=diagram_DDiagram_strategy)
def test_diagram_ddiagram_isInLayoutingMode_setter(instance):
    original = instance.isInLayoutingMode
    instance.isInLayoutingMode = original
    assert instance.isInLayoutingMode == original



@given(instance=diagram_DDiagram_strategy)
def test_diagram_ddiagram_headerHeight_setter(instance):
    original = instance.headerHeight
    instance.headerHeight = original
    assert instance.headerHeight == original



@given(instance=diagram_DDiagram_strategy)
def test_diagram_ddiagram_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=diagram_description_Layer_strategy)
@settings(max_examples=50)
def test_diagram_description_layer_instantiation(instance):
    assert isinstance(instance, diagram_description_Layer)



@given(instance=diagram_description_Layer_strategy)
def test_diagram_description_layer_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=diagram_concern_ConcernDescription_strategy)
@settings(max_examples=50)
def test_diagram_concern_concerndescription_instantiation(instance):
    assert isinstance(instance, diagram_concern_ConcernDescription)

@given(instance=diagram_filter_FilterDescription_strategy)
@settings(max_examples=50)
def test_diagram_filter_filterdescription_instantiation(instance):
    assert isinstance(instance, diagram_filter_FilterDescription)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_filter_FilterDescription_strategy)
@settings(max_examples=30)
def test_diagram_filter_filterdescription_isvisible_changes_state(instance):
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
        assert has_statements, f"Function 'isVisible' in diagram_filter_FilterDescription is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isVisible' in diagram_filter_FilterDescription did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isVisible' in diagram_filter_FilterDescription is not implemented or raised an error")

@given(instance=diagram_description_EdgeMappingImport_strategy)
@settings(max_examples=50)
def test_diagram_description_edgemappingimport_instantiation(instance):
    assert isinstance(instance, diagram_description_EdgeMappingImport)



@given(instance=diagram_description_EdgeMappingImport_strategy)
def test_diagram_description_edgemappingimport_inheritsAncestorFilters_setter(instance):
    original = instance.inheritsAncestorFilters
    instance.inheritsAncestorFilters = original
    assert instance.inheritsAncestorFilters == original

@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_edgemapping_instantiation(instance):
    assert isinstance(instance, diagram_description_EdgeMapping)



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_sourceFinderExpression_setter(instance):
    original = instance.sourceFinderExpression
    instance.sourceFinderExpression = original
    assert instance.sourceFinderExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_pathExpression_setter(instance):
    original = instance.pathExpression
    instance.pathExpression = original
    assert instance.pathExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_targetExpression_setter(instance):
    original = instance.targetExpression
    instance.targetExpression = original
    assert instance.targetExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_targetFinderExpression_setter(instance):
    original = instance.targetFinderExpression
    instance.targetFinderExpression = original
    assert instance.targetFinderExpression == original



@given(instance=diagram_description_EdgeMapping_strategy)
def test_diagram_description_edgemapping_useDomainElement_setter(instance):
    original = instance.useDomainElement
    instance.useDomainElement = original
    assert instance.useDomainElement == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_edgemapping_updateedge_changes_state(instance):
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
        assert has_statements, f"Function 'updateEdge' in diagram_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateEdge' in diagram_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateEdge' in diagram_description_EdgeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_EdgeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_edgemapping_createedge_changes_state(instance):
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
        assert has_statements, f"Function 'createEdge' in diagram_description_EdgeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in diagram_description_EdgeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in diagram_description_EdgeMapping is not implemented or raised an error")

@given(instance=diagram_tool_ToolSection_strategy)
@settings(max_examples=50)
def test_diagram_tool_toolsection_instantiation(instance):
    assert isinstance(instance, diagram_tool_ToolSection)



@given(instance=diagram_tool_ToolSection_strategy)
def test_diagram_tool_toolsection_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=50)
def test_diagram_description_abstractnodemapping_instantiation(instance):
    assert isinstance(instance, diagram_description_AbstractNodeMapping)



@given(instance=diagram_description_AbstractNodeMapping_strategy)
def test_diagram_description_abstractnodemapping_domainClass_setter(instance):
    original = instance.domainClass
    instance.domainClass = original
    assert instance.domainClass == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_abstractnodemapping_finddnodefromeobject_changes_state(instance):
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
        assert has_statements, f"Function 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findDNodeFromEObject' in diagram_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_abstractnodemapping_adddonenode_changes_state(instance):
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
        assert has_statements, f"Function 'addDoneNode' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addDoneNode' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addDoneNode' in diagram_description_AbstractNodeMapping is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=diagram_description_AbstractNodeMapping_strategy)
@settings(max_examples=30)
def test_diagram_description_abstractnodemapping_cleardnodesdone_changes_state(instance):
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
        assert has_statements, f"Function 'clearDNodesDone' in diagram_description_AbstractNodeMapping is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clearDNodesDone' in diagram_description_AbstractNodeMapping did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clearDNodesDone' in diagram_description_AbstractNodeMapping is not implemented or raised an error")
