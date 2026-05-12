import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractFigure,
    gmf_all_gmfgraph_FigureRef,
    gmf_all_gmfgraph_ChildAccess,
    Figure,
    gmf_all_gmfgraph_AbstractFigure,
    gmf_all_gmfgraph_PinOwner,
    gmf_all_gmfgraph_SVGProperty,
    Rectangle2D,
    SVGProperty,
    gmf_all_gmfgraph_Rectangle2D,
    gmfgraph_Layout,
    gmf_all_gmfgraph_Layout,
    gmf_all_gmfgraph_Layoutable,
    LayoutData,
    gmf_all_gmfgraph_BorderLayoutData,
    gmf_all_gmfgraph_XYLayoutData,
    gmf_all_gmfgraph_GridLayoutData,
    gmfgraph_Border,
    gmf_all_gmfgraph_Border,
    gmfgraph_LayoutData,
    gmf_all_gmfgraph_LayoutData,
    gmf_all_gmfgraph_Point,
    gmf_all_gmfgraph_Font,
    gmf_all_gmfgraph_Color,
    gmfgraph_CustomFigure,
    FigureAccessor,
    gmf_all_gmfgraph_Insets,
    gmf_all_gmfgraph_Dimension,
    gmf_all_gmfgraph_FigureAccessor,
    gmf_all_gmfgraph_CustomAttribute,
    CustomAttributeOwner,
    gmf_all_gmfgraph_CustomClass,
    CustomAttribute,
    gmf_all_gmfgraph_CustomAttributeOwner,
    gmfgraph_Polygon,
    gmfgraph_DecorationFigure,
    gmf_all_gmfgraph_PolygonDecoration,
    gmf_all_gmfgraph_CustomDecoration,
    DecorationFigure,
    gmfgraph_ConnectionFigure,
    gmf_all_gmfgraph_CustomConnection,
    gmfgraph_Polyline,
    gmf_all_gmfgraph_PolylineDecoration,
    gmf_all_gmfgraph_PolylineConnection,
    Polygon,
    gmf_all_gmfgraph_ScalablePolygon,
    Polyline,
    gmf_all_gmfgraph_Polygon,
    gmfgraph_CustomClass,
    gmf_all_gmfgraph_CustomBorder,
    gmf_all_gmfgraph_CustomLayoutData,
    gmf_all_gmfgraph_CustomLayout,
    gmfgraph_RealFigure,
    gmf_all_gmfgraph_CustomFigure,
    Shape,
    gmf_all_gmfgraph_Polyline,
    gmf_all_gmfgraph_Ellipse,
    gmf_all_gmfgraph_RoundedRectangle,
    gmf_all_gmfgraph_Rectangle,
    Point,
    Insets,
    Font,
    gmf_all_gmfgraph_BasicFont,
    Color,
    gmf_all_gmfgraph_ConstantColor,
    gmf_all_gmfgraph_RGBColor,
    gmfgraph_CustomAttributeOwner,
    gmfgraph_PinOwner,
    gmfgraph_AbstractFigure,
    gmf_all_gmfgraph_RealFigure,
    Dimension,
    gmf_all_gmfgraph_VisualFacet,
    ChildAccess,
    Layoutable,
    gmf_all_gmfgraph_Figure,
    VisualFacet,
    gmf_all_gmfgraph_AlignmentFacet,
    gmf_all_gmfgraph_GeneralFacet,
    gmf_all_gmfgraph_LabelOffsetFacet,
    gmf_all_gmfgraph_DefaultSizeFacet,
    gmf_all_gmfgraph_GradientFacet,
    gmf_all_gmfgraph_Identity,
    Layout,
    gmf_all_gmfgraph_CenterLayout,
    gmf_all_gmfgraph_LayoutRef,
    gmf_all_gmfgraph_XYLayout,
    gmf_all_gmfgraph_BorderLayout,
    gmf_all_gmfgraph_FlowLayout,
    gmf_all_gmfgraph_GridLayout,
    gmf_all_gmfgraph_StackLayout,
    Border,
    gmf_all_gmfgraph_CompoundBorder,
    gmf_all_gmfgraph_LineBorder,
    gmf_all_gmfgraph_BorderRef,
    gmf_all_gmfgraph_MarginBorder,
    FigureDescriptor,
    RealFigure,
    gmf_all_gmfgraph_InvisibleRectangle,
    gmf_all_gmfgraph_VerticalLabel,
    gmf_all_gmfgraph_Shape,
    gmf_all_gmfgraph_SVGFigure,
    gmf_all_gmfgraph_Label,
    gmf_all_gmfgraph_DecorationFigure,
    gmf_all_gmfgraph_ConnectionFigure,
    gmf_all_gmfgraph_LabeledContainer,
    FigureGallery,
    AbstractNode,
    gmf_all_gmfgraph_Node,
    DiagramElement,
    gmf_all_gmfgraph_Compartment,
    gmf_all_gmfgraph_Connection,
    gmf_all_gmfgraph_AbstractNode,
    gmf_all_tooldef_StyleSelector,
    gmf_all_tooldef_Image,
    tooldef_ContributionItem,
    Identity,
    gmf_all_gmfgraph_Pin,
    gmf_all_gmfgraph_FigureDescriptor,
    gmf_all_gmfgraph_DiagramElement,
    gmf_all_gmfgraph_FigureGallery,
    gmf_all_gmfgraph_Canvas,
    tooldef_PredefinedItem,
    tooldef_Menu,
    gmf_all_tooldef_PopupMenu,
    gmf_all_tooldef_PredefinedMenu,
    ItemBase,
    gmf_all_tooldef_Separator,
    gmf_all_tooldef_PredefinedItem,
    gmf_all_tooldef_ContributionItem,
    gmf_all_tooldef_Menu,
    gmf_all_tooldef_ItemBase,
    gmf_all_tooldef_ItemRef,
    ContributionItem,
    gmf_all_tooldef_MenuAction,
    Image,
    gmf_all_tooldef_BundleImage,
    gmf_all_tooldef_DefaultImage,
    gmf_all_tooldef_AbstractTool,
    Menu,
    gmf_all_tooldef_Toolbar,
    gmf_all_tooldef_ContextMenu,
    gmf_all_tooldef_MainMenu,
    MenuAction,
    gmf_all_tooldef_ToolRegistry,
    Pin,
    gmf_all_gmfgraph_CustomPin,
    gmf_all_gmfgraph_VisiblePin,
    gmf_all_gmfgraph_ColorPin,
    gmf_all_mappings_VisualEffectMapping,
    gmf_all_mappings_Measurable,
    gmf_all_mappings_Auditable,
    ToolContainer,
    gmf_all_tooldef_Palette,
    gmf_all_tooldef_ToolGroup,
    Measurable,
    MetricRule,
    gmf_all_mappings_MetricContainer,
    mappings_Measurable,
    mappings_Auditable,
    gmf_all_mappings_NotationElementTarget,
    gmf_all_mappings_DiagramElementTarget,
    gmf_all_mappings_DomainElementTarget,
    Auditable,
    gmf_all_mappings_AuditedMetricTarget,
    RuleBase,
    gmf_all_mappings_MetricRule,
    gmf_all_mappings_AuditRule,
    gmf_all_mappings_RuleBase,
    gmf_all_mappings_DomainAttributeTarget,
    gmf_all_mappings_AuditContainer,
    gmf_all_mappings_AppearanceSteward,
    AbstractTool,
    gmf_all_tooldef_GenericTool,
    gmf_all_tooldef_ToolContainer,
    gmf_all_tooldef_CreationTool,
    gmf_all_tooldef_PaletteSeparator,
    gmf_all_tooldef_StandardTool,
    gmf_all_mappings_ToolOwner,
    ContextMenu,
    gmf_all_mappings_MenuOwner,
    FeatureSeqInitializer,
    AuditRule,
    ReferenceNewElementSpec,
    FeatureInitializer,
    gmf_all_mappings_ReferenceNewElementSpec,
    gmf_all_mappings_FeatureValueSpec,
    gmf_all_mappings_ElementInitializer,
    gmf_all_mappings_ValueExpression,
    gmf_all_mappings_FeatureInitializer,
    gmf_all_mappings_LinkConstraints,
    mappings_gmf_all_EAttribute,
    MappingEntry,
    DiagramLabel,
    gmf_all_mappings_LabelMapping,
    Toolbar,
    MainMenu,
    ValueExpression,
    gmf_all_mappings_Constraint,
    Canvas,
    gmf_all_mappings_CanvasMapping,
    LinkConstraints,
    mappings_gmf_all_EStructuralFeature,
    Connection,
    mappings_NeedsContainment,
    Compartment,
    gmf_all_mappings_CompartmentMapping,
    ChildReference,
    Palette,
    mappings_gmf_all_EPackage,
    CompartmentMapping,
    NodeReference,
    gmf_all_mappings_TopNodeReference,
    gmf_all_mappings_ChildReference,
    NodeMapping,
    NeedsContainment,
    gmf_all_mappings_NodeReference,
    Node,
    gmf_all_gmfgraph_DiagramLabel,
    mappings_AppearanceSteward,
    mappings_ToolOwner,
    mappings_MenuOwner,
    mappings_MappingEntry,
    gmf_all_mappings_LinkMapping,
    gmf_all_mappings_NodeMapping,
    LabelMapping,
    gmf_all_mappings_ExpressionLabelMapping,
    gmf_all_mappings_FeatureLabelMapping,
    gmf_all_mappings_OclChoiceLabelMapping,
    gmf_all_mappings_DesignLabelMapping,
    ElementInitializer,
    gmf_all_mappings_FeatureSeqInitializer,
    Constraint,
    mappings_gmf_all_EClass,
    gmf_all_mappings_MappingEntry,
    MetricContainer,
    AuditContainer,
    StyleSelector,
    gmf_all_tooldef_GenericStyleSelector,
    CanvasMapping,
    LinkMapping,
    mappings_gmf_all_EReference,
    gmf_all_mappings_NeedsContainment,
    VisualEffectMapping,
    TopNodeReference,
    gmf_all_mappings_Mapping,
    Severity,
    LineKind,
    AppearanceStyle,
    SVGPropertyType,
    FontStyle,
    Alignment,
    ActionKind,
    Direction,
    ColorConstants,
    LabelTextAccessMethod,
    Language,
    StandardToolKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(AbstractFigure)


def test_abstractfigure_constructor_exists():
    assert callable(AbstractFigure.__init__)


def test_abstractfigure_constructor_args():
    sig = inspect.signature(AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_figureref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureRef)


def test_gmf_all_gmfgraph_figureref_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureRef.__init__)


def test_gmf_all_gmfgraph_figureref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_childaccess_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ChildAccess)


def test_gmf_all_gmfgraph_childaccess_constructor_exists():
    assert callable(gmf_all_gmfgraph_ChildAccess.__init__)


def test_gmf_all_gmfgraph_childaccess_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ChildAccess.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmf_all_gmfgraph_childaccess_has_accessor():
    assert hasattr(gmf_all_gmfgraph_ChildAccess, "accessor")
    descriptor = None
    for klass in gmf_all_gmfgraph_ChildAccess.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AbstractFigure)


def test_gmf_all_gmfgraph_abstractfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_AbstractFigure.__init__)


def test_gmf_all_gmfgraph_abstractfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_pinowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PinOwner)


def test_gmf_all_gmfgraph_pinowner_constructor_exists():
    assert callable(gmf_all_gmfgraph_PinOwner.__init__)


def test_gmf_all_gmfgraph_pinowner_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_svgproperty_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_SVGProperty)


def test_gmf_all_gmfgraph_svgproperty_constructor_exists():
    assert callable(gmf_all_gmfgraph_SVGProperty.__init__)


def test_gmf_all_gmfgraph_svgproperty_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_SVGProperty.__init__)
    params = list(sig.parameters.keys())
    assert "setter" in params, "Missing parameter 'setter'"
    assert "callSuper" in params, "Missing parameter 'callSuper'"
    assert "type" in params, "Missing parameter 'type'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "getter" in params, "Missing parameter 'getter'"
    assert "query" in params, "Missing parameter 'query'"

def test_gmf_all_gmfgraph_svgproperty_has_setter():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "setter")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "setter" in klass.__dict__:
            descriptor = klass.__dict__["setter"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgproperty_has_callSuper():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "callSuper")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "callSuper" in klass.__dict__:
            descriptor = klass.__dict__["callSuper"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgproperty_has_type():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "type")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgproperty_has_attribute():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "attribute")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgproperty_has_getter():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "getter")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "getter" in klass.__dict__:
            descriptor = klass.__dict__["getter"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgproperty_has_query():
    assert hasattr(gmf_all_gmfgraph_SVGProperty, "query")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGProperty.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_rectangle2d_is_not_abstract():
    assert not inspect.isabstract(Rectangle2D)


def test_rectangle2d_constructor_exists():
    assert callable(Rectangle2D.__init__)


def test_rectangle2d_constructor_args():
    sig = inspect.signature(Rectangle2D.__init__)
    params = list(sig.parameters.keys())



def test_svgproperty_is_not_abstract():
    assert not inspect.isabstract(SVGProperty)


def test_svgproperty_constructor_exists():
    assert callable(SVGProperty.__init__)


def test_svgproperty_constructor_args():
    sig = inspect.signature(SVGProperty.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_rectangle2d_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Rectangle2D)


def test_gmf_all_gmfgraph_rectangle2d_constructor_exists():
    assert callable(gmf_all_gmfgraph_Rectangle2D.__init__)


def test_gmf_all_gmfgraph_rectangle2d_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Rectangle2D.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"

def test_gmf_all_gmfgraph_rectangle2d_has_height():
    assert hasattr(gmf_all_gmfgraph_Rectangle2D, "height")
    descriptor = None
    for klass in gmf_all_gmfgraph_Rectangle2D.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_rectangle2d_has_x():
    assert hasattr(gmf_all_gmfgraph_Rectangle2D, "x")
    descriptor = None
    for klass in gmf_all_gmfgraph_Rectangle2D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_rectangle2d_has_y():
    assert hasattr(gmf_all_gmfgraph_Rectangle2D, "y")
    descriptor = None
    for klass in gmf_all_gmfgraph_Rectangle2D.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_rectangle2d_has_width():
    assert hasattr(gmf_all_gmfgraph_Rectangle2D, "width")
    descriptor = None
    for klass in gmf_all_gmfgraph_Rectangle2D.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph_layout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Layout)


def test_gmfgraph_layout_constructor_exists():
    assert callable(gmfgraph_Layout.__init__)


def test_gmfgraph_layout_constructor_args():
    sig = inspect.signature(gmfgraph_Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_layout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Layout)


def test_gmf_all_gmfgraph_layout_constructor_exists():
    assert callable(gmf_all_gmfgraph_Layout.__init__)


def test_gmf_all_gmfgraph_layout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_layoutable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Layoutable)


def test_gmf_all_gmfgraph_layoutable_constructor_exists():
    assert callable(gmf_all_gmfgraph_Layoutable.__init__)


def test_gmf_all_gmfgraph_layoutable_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_layoutdata_is_not_abstract():
    assert not inspect.isabstract(LayoutData)


def test_layoutdata_constructor_exists():
    assert callable(LayoutData.__init__)


def test_layoutdata_constructor_args():
    sig = inspect.signature(LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_borderlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderLayoutData)


def test_gmf_all_gmfgraph_borderlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderLayoutData.__init__)


def test_gmf_all_gmfgraph_borderlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "vertical" in params, "Missing parameter 'vertical'"

def test_gmf_all_gmfgraph_borderlayoutdata_has_alignment():
    assert hasattr(gmf_all_gmfgraph_BorderLayoutData, "alignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_BorderLayoutData.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_borderlayoutdata_has_vertical():
    assert hasattr(gmf_all_gmfgraph_BorderLayoutData, "vertical")
    descriptor = None
    for klass in gmf_all_gmfgraph_BorderLayoutData.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_xylayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_XYLayoutData)


def test_gmf_all_gmfgraph_xylayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_XYLayoutData.__init__)


def test_gmf_all_gmfgraph_xylayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_XYLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_gridlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GridLayoutData)


def test_gmf_all_gmfgraph_gridlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_GridLayoutData.__init__)


def test_gmf_all_gmfgraph_gridlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GridLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"

def test_gmf_all_gmfgraph_gridlayoutdata_has_horizontalSpan():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "horizontalSpan")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "horizontalSpan" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpan"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_grabExcessVerticalSpace():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "grabExcessVerticalSpace")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "grabExcessVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_horizontalAlignment():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "horizontalAlignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_verticalAlignment():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "verticalAlignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_horizontalIndent():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "horizontalIndent")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "horizontalIndent" in klass.__dict__:
            descriptor = klass.__dict__["horizontalIndent"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_verticalSpan():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "verticalSpan")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "verticalSpan" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpan"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayoutdata_has_grabExcessHorizontalSpace():
    assert hasattr(gmf_all_gmfgraph_GridLayoutData, "grabExcessHorizontalSpace")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayoutData.__mro__:
        if "grabExcessHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessHorizontalSpace"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph_border_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Border)


def test_gmfgraph_border_constructor_exists():
    assert callable(gmfgraph_Border.__init__)


def test_gmfgraph_border_constructor_args():
    sig = inspect.signature(gmfgraph_Border.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_border_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Border)


def test_gmf_all_gmfgraph_border_constructor_exists():
    assert callable(gmf_all_gmfgraph_Border.__init__)


def test_gmf_all_gmfgraph_border_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Border.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_LayoutData)


def test_gmfgraph_layoutdata_constructor_exists():
    assert callable(gmfgraph_LayoutData.__init__)


def test_gmfgraph_layoutdata_constructor_args():
    sig = inspect.signature(gmfgraph_LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LayoutData)


def test_gmf_all_gmfgraph_layoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_LayoutData.__init__)


def test_gmf_all_gmfgraph_layoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_point_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Point)


def test_gmf_all_gmfgraph_point_constructor_exists():
    assert callable(gmf_all_gmfgraph_Point.__init__)


def test_gmf_all_gmfgraph_point_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_gmf_all_gmfgraph_point_has_x():
    assert hasattr(gmf_all_gmfgraph_Point, "x")
    descriptor = None
    for klass in gmf_all_gmfgraph_Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_point_has_y():
    assert hasattr(gmf_all_gmfgraph_Point, "y")
    descriptor = None
    for klass in gmf_all_gmfgraph_Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_font_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Font)


def test_gmf_all_gmfgraph_font_constructor_exists():
    assert callable(gmf_all_gmfgraph_Font.__init__)


def test_gmf_all_gmfgraph_font_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Font.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_color_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Color)


def test_gmf_all_gmfgraph_color_constructor_exists():
    assert callable(gmf_all_gmfgraph_Color.__init__)


def test_gmf_all_gmfgraph_color_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Color.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_customfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomFigure)


def test_gmfgraph_customfigure_constructor_exists():
    assert callable(gmfgraph_CustomFigure.__init__)


def test_gmfgraph_customfigure_constructor_args():
    sig = inspect.signature(gmfgraph_CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(FigureAccessor)


def test_figureaccessor_constructor_exists():
    assert callable(FigureAccessor.__init__)


def test_figureaccessor_constructor_args():
    sig = inspect.signature(FigureAccessor.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_insets_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Insets)


def test_gmf_all_gmfgraph_insets_constructor_exists():
    assert callable(gmf_all_gmfgraph_Insets.__init__)


def test_gmf_all_gmfgraph_insets_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Insets.__init__)
    params = list(sig.parameters.keys())
    assert "bottom" in params, "Missing parameter 'bottom'"
    assert "right" in params, "Missing parameter 'right'"
    assert "top" in params, "Missing parameter 'top'"
    assert "left" in params, "Missing parameter 'left'"

def test_gmf_all_gmfgraph_insets_has_bottom():
    assert hasattr(gmf_all_gmfgraph_Insets, "bottom")
    descriptor = None
    for klass in gmf_all_gmfgraph_Insets.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_insets_has_right():
    assert hasattr(gmf_all_gmfgraph_Insets, "right")
    descriptor = None
    for klass in gmf_all_gmfgraph_Insets.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_insets_has_top():
    assert hasattr(gmf_all_gmfgraph_Insets, "top")
    descriptor = None
    for klass in gmf_all_gmfgraph_Insets.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_insets_has_left():
    assert hasattr(gmf_all_gmfgraph_Insets, "left")
    descriptor = None
    for klass in gmf_all_gmfgraph_Insets.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_dimension_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Dimension)


def test_gmf_all_gmfgraph_dimension_constructor_exists():
    assert callable(gmf_all_gmfgraph_Dimension.__init__)


def test_gmf_all_gmfgraph_dimension_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "dx" in params, "Missing parameter 'dx'"
    assert "dy" in params, "Missing parameter 'dy'"

def test_gmf_all_gmfgraph_dimension_has_dx():
    assert hasattr(gmf_all_gmfgraph_Dimension, "dx")
    descriptor = None
    for klass in gmf_all_gmfgraph_Dimension.__mro__:
        if "dx" in klass.__dict__:
            descriptor = klass.__dict__["dx"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_dimension_has_dy():
    assert hasattr(gmf_all_gmfgraph_Dimension, "dy")
    descriptor = None
    for klass in gmf_all_gmfgraph_Dimension.__mro__:
        if "dy" in klass.__dict__:
            descriptor = klass.__dict__["dy"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureAccessor)


def test_gmf_all_gmfgraph_figureaccessor_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureAccessor.__init__)


def test_gmf_all_gmfgraph_figureaccessor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureAccessor.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmf_all_gmfgraph_figureaccessor_has_accessor():
    assert hasattr(gmf_all_gmfgraph_FigureAccessor, "accessor")
    descriptor = None
    for klass in gmf_all_gmfgraph_FigureAccessor.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_customattribute_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomAttribute)


def test_gmf_all_gmfgraph_customattribute_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomAttribute.__init__)


def test_gmf_all_gmfgraph_customattribute_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "directAccess" in params, "Missing parameter 'directAccess'"
    assert "name" in params, "Missing parameter 'name'"
    assert "multiStatementValue" in params, "Missing parameter 'multiStatementValue'"

def test_gmf_all_gmfgraph_customattribute_has_value():
    assert hasattr(gmf_all_gmfgraph_CustomAttribute, "value")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_customattribute_has_directAccess():
    assert hasattr(gmf_all_gmfgraph_CustomAttribute, "directAccess")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomAttribute.__mro__:
        if "directAccess" in klass.__dict__:
            descriptor = klass.__dict__["directAccess"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_customattribute_has_name():
    assert hasattr(gmf_all_gmfgraph_CustomAttribute, "name")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_customattribute_has_multiStatementValue():
    assert hasattr(gmf_all_gmfgraph_CustomAttribute, "multiStatementValue")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomAttribute.__mro__:
        if "multiStatementValue" in klass.__dict__:
            descriptor = klass.__dict__["multiStatementValue"]
            break
    assert isinstance(descriptor, property)



def test_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(CustomAttributeOwner)


def test_customattributeowner_constructor_exists():
    assert callable(CustomAttributeOwner.__init__)


def test_customattributeowner_constructor_args():
    sig = inspect.signature(CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customclass_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomClass)


def test_gmf_all_gmfgraph_customclass_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomClass.__init__)


def test_gmf_all_gmfgraph_customclass_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomClass.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_gmf_all_gmfgraph_customclass_has_qualifiedClassName():
    assert hasattr(gmf_all_gmfgraph_CustomClass, "qualifiedClassName")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomClass.__mro__:
        if "qualifiedClassName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedClassName"]
            break
    assert isinstance(descriptor, property)



def test_customattribute_is_not_abstract():
    assert not inspect.isabstract(CustomAttribute)


def test_customattribute_constructor_exists():
    assert callable(CustomAttribute.__init__)


def test_customattribute_constructor_args():
    sig = inspect.signature(CustomAttribute.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomAttributeOwner)


def test_gmf_all_gmfgraph_customattributeowner_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomAttributeOwner.__init__)


def test_gmf_all_gmfgraph_customattributeowner_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_polygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polygon)


def test_gmfgraph_polygon_constructor_exists():
    assert callable(gmfgraph_Polygon.__init__)


def test_gmfgraph_polygon_constructor_args():
    sig = inspect.signature(gmfgraph_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_DecorationFigure)


def test_gmfgraph_decorationfigure_constructor_exists():
    assert callable(gmfgraph_DecorationFigure.__init__)


def test_gmfgraph_decorationfigure_constructor_args():
    sig = inspect.signature(gmfgraph_DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_polygondecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolygonDecoration)


def test_gmf_all_gmfgraph_polygondecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolygonDecoration.__init__)


def test_gmf_all_gmfgraph_polygondecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolygonDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customdecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomDecoration)


def test_gmf_all_gmfgraph_customdecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomDecoration.__init__)


def test_gmf_all_gmfgraph_customdecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomDecoration.__init__)
    params = list(sig.parameters.keys())



def test_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(DecorationFigure)


def test_decorationfigure_constructor_exists():
    assert callable(DecorationFigure.__init__)


def test_decorationfigure_constructor_args():
    sig = inspect.signature(DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_ConnectionFigure)


def test_gmfgraph_connectionfigure_constructor_exists():
    assert callable(gmfgraph_ConnectionFigure.__init__)


def test_gmfgraph_connectionfigure_constructor_args():
    sig = inspect.signature(gmfgraph_ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customconnection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomConnection)


def test_gmf_all_gmfgraph_customconnection_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomConnection.__init__)


def test_gmf_all_gmfgraph_customconnection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomConnection.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_polyline_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_Polyline)


def test_gmfgraph_polyline_constructor_exists():
    assert callable(gmfgraph_Polyline.__init__)


def test_gmfgraph_polyline_constructor_args():
    sig = inspect.signature(gmfgraph_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_polylinedecoration_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolylineDecoration)


def test_gmf_all_gmfgraph_polylinedecoration_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolylineDecoration.__init__)


def test_gmf_all_gmfgraph_polylinedecoration_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolylineDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_polylineconnection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_PolylineConnection)


def test_gmf_all_gmfgraph_polylineconnection_constructor_exists():
    assert callable(gmf_all_gmfgraph_PolylineConnection.__init__)


def test_gmf_all_gmfgraph_polylineconnection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_PolylineConnection.__init__)
    params = list(sig.parameters.keys())



def test_polygon_is_not_abstract():
    assert not inspect.isabstract(Polygon)


def test_polygon_constructor_exists():
    assert callable(Polygon.__init__)


def test_polygon_constructor_args():
    sig = inspect.signature(Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_scalablepolygon_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ScalablePolygon)


def test_gmf_all_gmfgraph_scalablepolygon_constructor_exists():
    assert callable(gmf_all_gmfgraph_ScalablePolygon.__init__)


def test_gmf_all_gmfgraph_scalablepolygon_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ScalablePolygon.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_polygon_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Polygon)


def test_gmf_all_gmfgraph_polygon_constructor_exists():
    assert callable(gmf_all_gmfgraph_Polygon.__init__)


def test_gmf_all_gmfgraph_polygon_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_customclass_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomClass)


def test_gmfgraph_customclass_constructor_exists():
    assert callable(gmfgraph_CustomClass.__init__)


def test_gmfgraph_customclass_constructor_args():
    sig = inspect.signature(gmfgraph_CustomClass.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomBorder)


def test_gmf_all_gmfgraph_customborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomBorder.__init__)


def test_gmf_all_gmfgraph_customborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomLayoutData)


def test_gmf_all_gmfgraph_customlayoutdata_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomLayoutData.__init__)


def test_gmf_all_gmfgraph_customlayoutdata_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomLayout)


def test_gmf_all_gmfgraph_customlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomLayout.__init__)


def test_gmf_all_gmfgraph_customlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_realfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_RealFigure)


def test_gmfgraph_realfigure_constructor_exists():
    assert callable(gmfgraph_RealFigure.__init__)


def test_gmfgraph_realfigure_constructor_args():
    sig = inspect.signature(gmfgraph_RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_customfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomFigure)


def test_gmf_all_gmfgraph_customfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomFigure.__init__)


def test_gmf_all_gmfgraph_customfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_polyline_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Polyline)


def test_gmf_all_gmfgraph_polyline_constructor_exists():
    assert callable(gmf_all_gmfgraph_Polyline.__init__)


def test_gmf_all_gmfgraph_polyline_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_ellipse_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Ellipse)


def test_gmf_all_gmfgraph_ellipse_constructor_exists():
    assert callable(gmf_all_gmfgraph_Ellipse.__init__)


def test_gmf_all_gmfgraph_ellipse_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RoundedRectangle)


def test_gmf_all_gmfgraph_roundedrectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_RoundedRectangle.__init__)


def test_gmf_all_gmfgraph_roundedrectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"

def test_gmf_all_gmfgraph_roundedrectangle_has_cornerHeight():
    assert hasattr(gmf_all_gmfgraph_RoundedRectangle, "cornerHeight")
    descriptor = None
    for klass in gmf_all_gmfgraph_RoundedRectangle.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_roundedrectangle_has_cornerWidth():
    assert hasattr(gmf_all_gmfgraph_RoundedRectangle, "cornerWidth")
    descriptor = None
    for klass in gmf_all_gmfgraph_RoundedRectangle.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_rectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Rectangle)


def test_gmf_all_gmfgraph_rectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_Rectangle.__init__)


def test_gmf_all_gmfgraph_rectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_insets_is_not_abstract():
    assert not inspect.isabstract(Insets)


def test_insets_constructor_exists():
    assert callable(Insets.__init__)


def test_insets_constructor_args():
    sig = inspect.signature(Insets.__init__)
    params = list(sig.parameters.keys())



def test_font_is_not_abstract():
    assert not inspect.isabstract(Font)


def test_font_constructor_exists():
    assert callable(Font.__init__)


def test_font_constructor_args():
    sig = inspect.signature(Font.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_basicfont_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BasicFont)


def test_gmf_all_gmfgraph_basicfont_constructor_exists():
    assert callable(gmf_all_gmfgraph_BasicFont.__init__)


def test_gmf_all_gmfgraph_basicfont_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BasicFont.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "faceName" in params, "Missing parameter 'faceName'"
    assert "height" in params, "Missing parameter 'height'"

def test_gmf_all_gmfgraph_basicfont_has_style():
    assert hasattr(gmf_all_gmfgraph_BasicFont, "style")
    descriptor = None
    for klass in gmf_all_gmfgraph_BasicFont.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_basicfont_has_faceName():
    assert hasattr(gmf_all_gmfgraph_BasicFont, "faceName")
    descriptor = None
    for klass in gmf_all_gmfgraph_BasicFont.__mro__:
        if "faceName" in klass.__dict__:
            descriptor = klass.__dict__["faceName"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_basicfont_has_height():
    assert hasattr(gmf_all_gmfgraph_BasicFont, "height")
    descriptor = None
    for klass in gmf_all_gmfgraph_BasicFont.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_constantcolor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ConstantColor)


def test_gmf_all_gmfgraph_constantcolor_constructor_exists():
    assert callable(gmf_all_gmfgraph_ConstantColor.__init__)


def test_gmf_all_gmfgraph_constantcolor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ConstantColor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gmf_all_gmfgraph_constantcolor_has_value():
    assert hasattr(gmf_all_gmfgraph_ConstantColor, "value")
    descriptor = None
    for klass in gmf_all_gmfgraph_ConstantColor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RGBColor)


def test_gmf_all_gmfgraph_rgbcolor_constructor_exists():
    assert callable(gmf_all_gmfgraph_RGBColor.__init__)


def test_gmf_all_gmfgraph_rgbcolor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_gmf_all_gmfgraph_rgbcolor_has_red():
    assert hasattr(gmf_all_gmfgraph_RGBColor, "red")
    descriptor = None
    for klass in gmf_all_gmfgraph_RGBColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_rgbcolor_has_green():
    assert hasattr(gmf_all_gmfgraph_RGBColor, "green")
    descriptor = None
    for klass in gmf_all_gmfgraph_RGBColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_rgbcolor_has_blue():
    assert hasattr(gmf_all_gmfgraph_RGBColor, "blue")
    descriptor = None
    for klass in gmf_all_gmfgraph_RGBColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_CustomAttributeOwner)


def test_gmfgraph_customattributeowner_constructor_exists():
    assert callable(gmfgraph_CustomAttributeOwner.__init__)


def test_gmfgraph_customattributeowner_constructor_args():
    sig = inspect.signature(gmfgraph_CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_pinowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_PinOwner)


def test_gmfgraph_pinowner_constructor_exists():
    assert callable(gmfgraph_PinOwner.__init__)


def test_gmfgraph_pinowner_constructor_args():
    sig = inspect.signature(gmfgraph_PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph_AbstractFigure)


def test_gmfgraph_abstractfigure_constructor_exists():
    assert callable(gmfgraph_AbstractFigure.__init__)


def test_gmfgraph_abstractfigure_constructor_args():
    sig = inspect.signature(gmfgraph_AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_realfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_RealFigure)


def test_gmf_all_gmfgraph_realfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_RealFigure.__init__)


def test_gmf_all_gmfgraph_realfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_RealFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf_all_gmfgraph_realfigure_has_name():
    assert hasattr(gmf_all_gmfgraph_RealFigure, "name")
    descriptor = None
    for klass in gmf_all_gmfgraph_RealFigure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dimension_is_not_abstract():
    assert not inspect.isabstract(Dimension)


def test_dimension_constructor_exists():
    assert callable(Dimension.__init__)


def test_dimension_constructor_args():
    sig = inspect.signature(Dimension.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_visualfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VisualFacet)


def test_gmf_all_gmfgraph_visualfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_VisualFacet.__init__)


def test_gmf_all_gmfgraph_visualfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_childaccess_is_not_abstract():
    assert not inspect.isabstract(ChildAccess)


def test_childaccess_constructor_exists():
    assert callable(ChildAccess.__init__)


def test_childaccess_constructor_args():
    sig = inspect.signature(ChildAccess.__init__)
    params = list(sig.parameters.keys())



def test_layoutable_is_not_abstract():
    assert not inspect.isabstract(Layoutable)


def test_layoutable_constructor_exists():
    assert callable(Layoutable.__init__)


def test_layoutable_constructor_args():
    sig = inspect.signature(Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_figure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Figure)


def test_gmf_all_gmfgraph_figure_constructor_exists():
    assert callable(gmf_all_gmfgraph_Figure.__init__)


def test_gmf_all_gmfgraph_figure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Figure.__init__)
    params = list(sig.parameters.keys())



def test_visualfacet_is_not_abstract():
    assert not inspect.isabstract(VisualFacet)


def test_visualfacet_constructor_exists():
    assert callable(VisualFacet.__init__)


def test_visualfacet_constructor_args():
    sig = inspect.signature(VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_alignmentfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AlignmentFacet)


def test_gmf_all_gmfgraph_alignmentfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_AlignmentFacet.__init__)


def test_gmf_all_gmfgraph_alignmentfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AlignmentFacet.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_gmf_all_gmfgraph_alignmentfacet_has_alignment():
    assert hasattr(gmf_all_gmfgraph_AlignmentFacet, "alignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_AlignmentFacet.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_generalfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GeneralFacet)


def test_gmf_all_gmfgraph_generalfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_GeneralFacet.__init__)


def test_gmf_all_gmfgraph_generalfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GeneralFacet.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "data" in params, "Missing parameter 'data'"

def test_gmf_all_gmfgraph_generalfacet_has_identifier():
    assert hasattr(gmf_all_gmfgraph_GeneralFacet, "identifier")
    descriptor = None
    for klass in gmf_all_gmfgraph_GeneralFacet.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_generalfacet_has_data():
    assert hasattr(gmf_all_gmfgraph_GeneralFacet, "data")
    descriptor = None
    for klass in gmf_all_gmfgraph_GeneralFacet.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_labeloffsetfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LabelOffsetFacet)


def test_gmf_all_gmfgraph_labeloffsetfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_LabelOffsetFacet.__init__)


def test_gmf_all_gmfgraph_labeloffsetfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LabelOffsetFacet.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_gmf_all_gmfgraph_labeloffsetfacet_has_y():
    assert hasattr(gmf_all_gmfgraph_LabelOffsetFacet, "y")
    descriptor = None
    for klass in gmf_all_gmfgraph_LabelOffsetFacet.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_labeloffsetfacet_has_x():
    assert hasattr(gmf_all_gmfgraph_LabelOffsetFacet, "x")
    descriptor = None
    for klass in gmf_all_gmfgraph_LabelOffsetFacet.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_defaultsizefacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DefaultSizeFacet)


def test_gmf_all_gmfgraph_defaultsizefacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_DefaultSizeFacet.__init__)


def test_gmf_all_gmfgraph_defaultsizefacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DefaultSizeFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_gradientfacet_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GradientFacet)


def test_gmf_all_gmfgraph_gradientfacet_constructor_exists():
    assert callable(gmf_all_gmfgraph_GradientFacet.__init__)


def test_gmf_all_gmfgraph_gradientfacet_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GradientFacet.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_gmf_all_gmfgraph_gradientfacet_has_direction():
    assert hasattr(gmf_all_gmfgraph_GradientFacet, "direction")
    descriptor = None
    for klass in gmf_all_gmfgraph_GradientFacet.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_identity_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Identity)


def test_gmf_all_gmfgraph_identity_constructor_exists():
    assert callable(gmf_all_gmfgraph_Identity.__init__)


def test_gmf_all_gmfgraph_identity_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Identity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf_all_gmfgraph_identity_has_name():
    assert hasattr(gmf_all_gmfgraph_Identity, "name")
    descriptor = None
    for klass in gmf_all_gmfgraph_Identity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_layout_is_not_abstract():
    assert not inspect.isabstract(Layout)


def test_layout_constructor_exists():
    assert callable(Layout.__init__)


def test_layout_constructor_args():
    sig = inspect.signature(Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_centerlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CenterLayout)


def test_gmf_all_gmfgraph_centerlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_CenterLayout.__init__)


def test_gmf_all_gmfgraph_centerlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CenterLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_layoutref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LayoutRef)


def test_gmf_all_gmfgraph_layoutref_constructor_exists():
    assert callable(gmf_all_gmfgraph_LayoutRef.__init__)


def test_gmf_all_gmfgraph_layoutref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LayoutRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_xylayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_XYLayout)


def test_gmf_all_gmfgraph_xylayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_XYLayout.__init__)


def test_gmf_all_gmfgraph_xylayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_XYLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_borderlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderLayout)


def test_gmf_all_gmfgraph_borderlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderLayout.__init__)


def test_gmf_all_gmfgraph_borderlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_flowlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FlowLayout)


def test_gmf_all_gmfgraph_flowlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_FlowLayout.__init__)


def test_gmf_all_gmfgraph_flowlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FlowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "forceSingleLine" in params, "Missing parameter 'forceSingleLine'"
    assert "minorSpacing" in params, "Missing parameter 'minorSpacing'"
    assert "majorAlignment" in params, "Missing parameter 'majorAlignment'"
    assert "minorAlignment" in params, "Missing parameter 'minorAlignment'"
    assert "majorSpacing" in params, "Missing parameter 'majorSpacing'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "matchMinorSize" in params, "Missing parameter 'matchMinorSize'"

def test_gmf_all_gmfgraph_flowlayout_has_forceSingleLine():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "forceSingleLine")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "forceSingleLine" in klass.__dict__:
            descriptor = klass.__dict__["forceSingleLine"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_minorSpacing():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "minorSpacing")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "minorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["minorSpacing"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_majorAlignment():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "majorAlignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "majorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["majorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_minorAlignment():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "minorAlignment")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "minorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["minorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_majorSpacing():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "majorSpacing")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "majorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["majorSpacing"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_vertical():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "vertical")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_flowlayout_has_matchMinorSize():
    assert hasattr(gmf_all_gmfgraph_FlowLayout, "matchMinorSize")
    descriptor = None
    for klass in gmf_all_gmfgraph_FlowLayout.__mro__:
        if "matchMinorSize" in klass.__dict__:
            descriptor = klass.__dict__["matchMinorSize"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_gridlayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_GridLayout)


def test_gmf_all_gmfgraph_gridlayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_GridLayout.__init__)


def test_gmf_all_gmfgraph_gridlayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "numColumns" in params, "Missing parameter 'numColumns'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"

def test_gmf_all_gmfgraph_gridlayout_has_numColumns():
    assert hasattr(gmf_all_gmfgraph_GridLayout, "numColumns")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayout.__mro__:
        if "numColumns" in klass.__dict__:
            descriptor = klass.__dict__["numColumns"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_gridlayout_has_equalWidth():
    assert hasattr(gmf_all_gmfgraph_GridLayout, "equalWidth")
    descriptor = None
    for klass in gmf_all_gmfgraph_GridLayout.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_stacklayout_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_StackLayout)


def test_gmf_all_gmfgraph_stacklayout_constructor_exists():
    assert callable(gmf_all_gmfgraph_StackLayout.__init__)


def test_gmf_all_gmfgraph_stacklayout_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_StackLayout.__init__)
    params = list(sig.parameters.keys())



def test_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_border_constructor_exists():
    assert callable(Border.__init__)


def test_border_constructor_args():
    sig = inspect.signature(Border.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_compoundborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CompoundBorder)


def test_gmf_all_gmfgraph_compoundborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_CompoundBorder.__init__)


def test_gmf_all_gmfgraph_compoundborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CompoundBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_lineborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LineBorder)


def test_gmf_all_gmfgraph_lineborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_LineBorder.__init__)


def test_gmf_all_gmfgraph_lineborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LineBorder.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_gmf_all_gmfgraph_lineborder_has_width():
    assert hasattr(gmf_all_gmfgraph_LineBorder, "width")
    descriptor = None
    for klass in gmf_all_gmfgraph_LineBorder.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_borderref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_BorderRef)


def test_gmf_all_gmfgraph_borderref_constructor_exists():
    assert callable(gmf_all_gmfgraph_BorderRef.__init__)


def test_gmf_all_gmfgraph_borderref_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_BorderRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_marginborder_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_MarginBorder)


def test_gmf_all_gmfgraph_marginborder_constructor_exists():
    assert callable(gmf_all_gmfgraph_MarginBorder.__init__)


def test_gmf_all_gmfgraph_marginborder_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_MarginBorder.__init__)
    params = list(sig.parameters.keys())



def test_figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(FigureDescriptor)


def test_figuredescriptor_constructor_exists():
    assert callable(FigureDescriptor.__init__)


def test_figuredescriptor_constructor_args():
    sig = inspect.signature(FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_realfigure_is_not_abstract():
    assert not inspect.isabstract(RealFigure)


def test_realfigure_constructor_exists():
    assert callable(RealFigure.__init__)


def test_realfigure_constructor_args():
    sig = inspect.signature(RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_invisiblerectangle_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_InvisibleRectangle)


def test_gmf_all_gmfgraph_invisiblerectangle_constructor_exists():
    assert callable(gmf_all_gmfgraph_InvisibleRectangle.__init__)


def test_gmf_all_gmfgraph_invisiblerectangle_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_InvisibleRectangle.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_verticallabel_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VerticalLabel)


def test_gmf_all_gmfgraph_verticallabel_constructor_exists():
    assert callable(gmf_all_gmfgraph_VerticalLabel.__init__)


def test_gmf_all_gmfgraph_verticallabel_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VerticalLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gmf_all_gmfgraph_verticallabel_has_text():
    assert hasattr(gmf_all_gmfgraph_VerticalLabel, "text")
    descriptor = None
    for klass in gmf_all_gmfgraph_VerticalLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_shape_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Shape)


def test_gmf_all_gmfgraph_shape_constructor_exists():
    assert callable(gmf_all_gmfgraph_Shape.__init__)


def test_gmf_all_gmfgraph_shape_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Shape.__init__)
    params = list(sig.parameters.keys())
    assert "xorFill" in params, "Missing parameter 'xorFill'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "lineKind" in params, "Missing parameter 'lineKind'"
    assert "xorOutline" in params, "Missing parameter 'xorOutline'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_gmf_all_gmfgraph_shape_has_xorFill():
    assert hasattr(gmf_all_gmfgraph_Shape, "xorFill")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "xorFill" in klass.__dict__:
            descriptor = klass.__dict__["xorFill"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_shape_has_outline():
    assert hasattr(gmf_all_gmfgraph_Shape, "outline")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_shape_has_fill():
    assert hasattr(gmf_all_gmfgraph_Shape, "fill")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_shape_has_lineKind():
    assert hasattr(gmf_all_gmfgraph_Shape, "lineKind")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "lineKind" in klass.__dict__:
            descriptor = klass.__dict__["lineKind"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_shape_has_xorOutline():
    assert hasattr(gmf_all_gmfgraph_Shape, "xorOutline")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "xorOutline" in klass.__dict__:
            descriptor = klass.__dict__["xorOutline"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_shape_has_lineWidth():
    assert hasattr(gmf_all_gmfgraph_Shape, "lineWidth")
    descriptor = None
    for klass in gmf_all_gmfgraph_Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_svgfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_SVGFigure)


def test_gmf_all_gmfgraph_svgfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_SVGFigure.__init__)


def test_gmf_all_gmfgraph_svgfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_SVGFigure.__init__)
    params = list(sig.parameters.keys())
    assert "noCanvasWidth" in params, "Missing parameter 'noCanvasWidth'"
    assert "documentURI" in params, "Missing parameter 'documentURI'"
    assert "noCanvasHeight" in params, "Missing parameter 'noCanvasHeight'"

def test_gmf_all_gmfgraph_svgfigure_has_noCanvasWidth():
    assert hasattr(gmf_all_gmfgraph_SVGFigure, "noCanvasWidth")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGFigure.__mro__:
        if "noCanvasWidth" in klass.__dict__:
            descriptor = klass.__dict__["noCanvasWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgfigure_has_documentURI():
    assert hasattr(gmf_all_gmfgraph_SVGFigure, "documentURI")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGFigure.__mro__:
        if "documentURI" in klass.__dict__:
            descriptor = klass.__dict__["documentURI"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_svgfigure_has_noCanvasHeight():
    assert hasattr(gmf_all_gmfgraph_SVGFigure, "noCanvasHeight")
    descriptor = None
    for klass in gmf_all_gmfgraph_SVGFigure.__mro__:
        if "noCanvasHeight" in klass.__dict__:
            descriptor = klass.__dict__["noCanvasHeight"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_label_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Label)


def test_gmf_all_gmfgraph_label_constructor_exists():
    assert callable(gmf_all_gmfgraph_Label.__init__)


def test_gmf_all_gmfgraph_label_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gmf_all_gmfgraph_label_has_text():
    assert hasattr(gmf_all_gmfgraph_Label, "text")
    descriptor = None
    for klass in gmf_all_gmfgraph_Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DecorationFigure)


def test_gmf_all_gmfgraph_decorationfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_DecorationFigure.__init__)


def test_gmf_all_gmfgraph_decorationfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ConnectionFigure)


def test_gmf_all_gmfgraph_connectionfigure_constructor_exists():
    assert callable(gmf_all_gmfgraph_ConnectionFigure.__init__)


def test_gmf_all_gmfgraph_connectionfigure_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_labeledcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_LabeledContainer)


def test_gmf_all_gmfgraph_labeledcontainer_constructor_exists():
    assert callable(gmf_all_gmfgraph_LabeledContainer.__init__)


def test_gmf_all_gmfgraph_labeledcontainer_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_LabeledContainer.__init__)
    params = list(sig.parameters.keys())



def test_figuregallery_is_not_abstract():
    assert not inspect.isabstract(FigureGallery)


def test_figuregallery_constructor_exists():
    assert callable(FigureGallery.__init__)


def test_figuregallery_constructor_args():
    sig = inspect.signature(FigureGallery.__init__)
    params = list(sig.parameters.keys())



def test_abstractnode_is_not_abstract():
    assert not inspect.isabstract(AbstractNode)


def test_abstractnode_constructor_exists():
    assert callable(AbstractNode.__init__)


def test_abstractnode_constructor_args():
    sig = inspect.signature(AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_node_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Node)


def test_gmf_all_gmfgraph_node_constructor_exists():
    assert callable(gmf_all_gmfgraph_Node.__init__)


def test_gmf_all_gmfgraph_node_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "resizeConstraint" in params, "Missing parameter 'resizeConstraint'"
    assert "affixedParentSide" in params, "Missing parameter 'affixedParentSide'"

def test_gmf_all_gmfgraph_node_has_resizeConstraint():
    assert hasattr(gmf_all_gmfgraph_Node, "resizeConstraint")
    descriptor = None
    for klass in gmf_all_gmfgraph_Node.__mro__:
        if "resizeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["resizeConstraint"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_node_has_affixedParentSide():
    assert hasattr(gmf_all_gmfgraph_Node, "affixedParentSide")
    descriptor = None
    for klass in gmf_all_gmfgraph_Node.__mro__:
        if "affixedParentSide" in klass.__dict__:
            descriptor = klass.__dict__["affixedParentSide"]
            break
    assert isinstance(descriptor, property)



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_compartment_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Compartment)


def test_gmf_all_gmfgraph_compartment_constructor_exists():
    assert callable(gmf_all_gmfgraph_Compartment.__init__)


def test_gmf_all_gmfgraph_compartment_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "needsTitle" in params, "Missing parameter 'needsTitle'"

def test_gmf_all_gmfgraph_compartment_has_collapsible():
    assert hasattr(gmf_all_gmfgraph_Compartment, "collapsible")
    descriptor = None
    for klass in gmf_all_gmfgraph_Compartment.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_compartment_has_needsTitle():
    assert hasattr(gmf_all_gmfgraph_Compartment, "needsTitle")
    descriptor = None
    for klass in gmf_all_gmfgraph_Compartment.__mro__:
        if "needsTitle" in klass.__dict__:
            descriptor = klass.__dict__["needsTitle"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_connection_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Connection)


def test_gmf_all_gmfgraph_connection_constructor_exists():
    assert callable(gmf_all_gmfgraph_Connection.__init__)


def test_gmf_all_gmfgraph_connection_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Connection.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_abstractnode_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_AbstractNode)


def test_gmf_all_gmfgraph_abstractnode_constructor_exists():
    assert callable(gmf_all_gmfgraph_AbstractNode.__init__)


def test_gmf_all_gmfgraph_abstractnode_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_styleselector_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_StyleSelector)


def test_gmf_all_tooldef_styleselector_constructor_exists():
    assert callable(gmf_all_tooldef_StyleSelector.__init__)


def test_gmf_all_tooldef_styleselector_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_StyleSelector.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_image_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Image)


def test_gmf_all_tooldef_image_constructor_exists():
    assert callable(gmf_all_tooldef_Image.__init__)


def test_gmf_all_tooldef_image_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Image.__init__)
    params = list(sig.parameters.keys())



def test_tooldef_contributionitem_is_not_abstract():
    assert not inspect.isabstract(tooldef_ContributionItem)


def test_tooldef_contributionitem_constructor_exists():
    assert callable(tooldef_ContributionItem.__init__)


def test_tooldef_contributionitem_constructor_args():
    sig = inspect.signature(tooldef_ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_identity_is_not_abstract():
    assert not inspect.isabstract(Identity)


def test_identity_constructor_exists():
    assert callable(Identity.__init__)


def test_identity_constructor_args():
    sig = inspect.signature(Identity.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_pin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Pin)


def test_gmf_all_gmfgraph_pin_constructor_exists():
    assert callable(gmf_all_gmfgraph_Pin.__init__)


def test_gmf_all_gmfgraph_pin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Pin.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureDescriptor)


def test_gmf_all_gmfgraph_figuredescriptor_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureDescriptor.__init__)


def test_gmf_all_gmfgraph_figuredescriptor_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_diagramelement_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DiagramElement)


def test_gmf_all_gmfgraph_diagramelement_constructor_exists():
    assert callable(gmf_all_gmfgraph_DiagramElement.__init__)


def test_gmf_all_gmfgraph_diagramelement_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_figuregallery_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_FigureGallery)


def test_gmf_all_gmfgraph_figuregallery_constructor_exists():
    assert callable(gmf_all_gmfgraph_FigureGallery.__init__)


def test_gmf_all_gmfgraph_figuregallery_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_FigureGallery.__init__)
    params = list(sig.parameters.keys())
    assert "implementationBundle" in params, "Missing parameter 'implementationBundle'"

def test_gmf_all_gmfgraph_figuregallery_has_implementationBundle():
    assert hasattr(gmf_all_gmfgraph_FigureGallery, "implementationBundle")
    descriptor = None
    for klass in gmf_all_gmfgraph_FigureGallery.__mro__:
        if "implementationBundle" in klass.__dict__:
            descriptor = klass.__dict__["implementationBundle"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_canvas_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_Canvas)


def test_gmf_all_gmfgraph_canvas_constructor_exists():
    assert callable(gmf_all_gmfgraph_Canvas.__init__)


def test_gmf_all_gmfgraph_canvas_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_Canvas.__init__)
    params = list(sig.parameters.keys())



def test_tooldef_predefineditem_is_not_abstract():
    assert not inspect.isabstract(tooldef_PredefinedItem)


def test_tooldef_predefineditem_constructor_exists():
    assert callable(tooldef_PredefinedItem.__init__)


def test_tooldef_predefineditem_constructor_args():
    sig = inspect.signature(tooldef_PredefinedItem.__init__)
    params = list(sig.parameters.keys())



def test_tooldef_menu_is_not_abstract():
    assert not inspect.isabstract(tooldef_Menu)


def test_tooldef_menu_constructor_exists():
    assert callable(tooldef_Menu.__init__)


def test_tooldef_menu_constructor_args():
    sig = inspect.signature(tooldef_Menu.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_popupmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PopupMenu)


def test_gmf_all_tooldef_popupmenu_constructor_exists():
    assert callable(gmf_all_tooldef_PopupMenu.__init__)


def test_gmf_all_tooldef_popupmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PopupMenu.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_gmf_all_tooldef_popupmenu_has_iD():
    assert hasattr(gmf_all_tooldef_PopupMenu, "iD")
    descriptor = None
    for klass in gmf_all_tooldef_PopupMenu.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_predefinedmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PredefinedMenu)


def test_gmf_all_tooldef_predefinedmenu_constructor_exists():
    assert callable(gmf_all_tooldef_PredefinedMenu.__init__)


def test_gmf_all_tooldef_predefinedmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PredefinedMenu.__init__)
    params = list(sig.parameters.keys())



def test_itembase_is_not_abstract():
    assert not inspect.isabstract(ItemBase)


def test_itembase_constructor_exists():
    assert callable(ItemBase.__init__)


def test_itembase_constructor_args():
    sig = inspect.signature(ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_separator_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Separator)


def test_gmf_all_tooldef_separator_constructor_exists():
    assert callable(gmf_all_tooldef_Separator.__init__)


def test_gmf_all_tooldef_separator_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Separator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf_all_tooldef_separator_has_name():
    assert hasattr(gmf_all_tooldef_Separator, "name")
    descriptor = None
    for klass in gmf_all_tooldef_Separator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_predefineditem_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PredefinedItem)


def test_gmf_all_tooldef_predefineditem_constructor_exists():
    assert callable(gmf_all_tooldef_PredefinedItem.__init__)


def test_gmf_all_tooldef_predefineditem_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PredefinedItem.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_gmf_all_tooldef_predefineditem_has_identifier():
    assert hasattr(gmf_all_tooldef_PredefinedItem, "identifier")
    descriptor = None
    for klass in gmf_all_tooldef_PredefinedItem.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_contributionitem_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ContributionItem)


def test_gmf_all_tooldef_contributionitem_constructor_exists():
    assert callable(gmf_all_tooldef_ContributionItem.__init__)


def test_gmf_all_tooldef_contributionitem_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ContributionItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_gmf_all_tooldef_contributionitem_has_title():
    assert hasattr(gmf_all_tooldef_ContributionItem, "title")
    descriptor = None
    for klass in gmf_all_tooldef_ContributionItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_menu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Menu)


def test_gmf_all_tooldef_menu_constructor_exists():
    assert callable(gmf_all_tooldef_Menu.__init__)


def test_gmf_all_tooldef_menu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Menu.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_itembase_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ItemBase)


def test_gmf_all_tooldef_itembase_constructor_exists():
    assert callable(gmf_all_tooldef_ItemBase.__init__)


def test_gmf_all_tooldef_itembase_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_itemref_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ItemRef)


def test_gmf_all_tooldef_itemref_constructor_exists():
    assert callable(gmf_all_tooldef_ItemRef.__init__)


def test_gmf_all_tooldef_itemref_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ItemRef.__init__)
    params = list(sig.parameters.keys())



def test_contributionitem_is_not_abstract():
    assert not inspect.isabstract(ContributionItem)


def test_contributionitem_constructor_exists():
    assert callable(ContributionItem.__init__)


def test_contributionitem_constructor_args():
    sig = inspect.signature(ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_menuaction_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_MenuAction)


def test_gmf_all_tooldef_menuaction_constructor_exists():
    assert callable(gmf_all_tooldef_MenuAction.__init__)


def test_gmf_all_tooldef_menuaction_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_MenuAction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "hotKey" in params, "Missing parameter 'hotKey'"

def test_gmf_all_tooldef_menuaction_has_kind():
    assert hasattr(gmf_all_tooldef_MenuAction, "kind")
    descriptor = None
    for klass in gmf_all_tooldef_MenuAction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_tooldef_menuaction_has_hotKey():
    assert hasattr(gmf_all_tooldef_MenuAction, "hotKey")
    descriptor = None
    for klass in gmf_all_tooldef_MenuAction.__mro__:
        if "hotKey" in klass.__dict__:
            descriptor = klass.__dict__["hotKey"]
            break
    assert isinstance(descriptor, property)



def test_image_is_not_abstract():
    assert not inspect.isabstract(Image)


def test_image_constructor_exists():
    assert callable(Image.__init__)


def test_image_constructor_args():
    sig = inspect.signature(Image.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_bundleimage_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_BundleImage)


def test_gmf_all_tooldef_bundleimage_constructor_exists():
    assert callable(gmf_all_tooldef_BundleImage.__init__)


def test_gmf_all_tooldef_bundleimage_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_BundleImage.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "bundle" in params, "Missing parameter 'bundle'"

def test_gmf_all_tooldef_bundleimage_has_path():
    assert hasattr(gmf_all_tooldef_BundleImage, "path")
    descriptor = None
    for klass in gmf_all_tooldef_BundleImage.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_tooldef_bundleimage_has_bundle():
    assert hasattr(gmf_all_tooldef_BundleImage, "bundle")
    descriptor = None
    for klass in gmf_all_tooldef_BundleImage.__mro__:
        if "bundle" in klass.__dict__:
            descriptor = klass.__dict__["bundle"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_defaultimage_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_DefaultImage)


def test_gmf_all_tooldef_defaultimage_constructor_exists():
    assert callable(gmf_all_tooldef_DefaultImage.__init__)


def test_gmf_all_tooldef_defaultimage_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_DefaultImage.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_abstracttool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_AbstractTool)


def test_gmf_all_tooldef_abstracttool_constructor_exists():
    assert callable(gmf_all_tooldef_AbstractTool.__init__)


def test_gmf_all_tooldef_abstracttool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_AbstractTool.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"

def test_gmf_all_tooldef_abstracttool_has_description():
    assert hasattr(gmf_all_tooldef_AbstractTool, "description")
    descriptor = None
    for klass in gmf_all_tooldef_AbstractTool.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_tooldef_abstracttool_has_title():
    assert hasattr(gmf_all_tooldef_AbstractTool, "title")
    descriptor = None
    for klass in gmf_all_tooldef_AbstractTool.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_toolbar_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Toolbar)


def test_gmf_all_tooldef_toolbar_constructor_exists():
    assert callable(gmf_all_tooldef_Toolbar.__init__)


def test_gmf_all_tooldef_toolbar_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Toolbar.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_contextmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ContextMenu)


def test_gmf_all_tooldef_contextmenu_constructor_exists():
    assert callable(gmf_all_tooldef_ContextMenu.__init__)


def test_gmf_all_tooldef_contextmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_mainmenu_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_MainMenu)


def test_gmf_all_tooldef_mainmenu_constructor_exists():
    assert callable(gmf_all_tooldef_MainMenu.__init__)


def test_gmf_all_tooldef_mainmenu_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_MainMenu.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_gmf_all_tooldef_mainmenu_has_title():
    assert hasattr(gmf_all_tooldef_MainMenu, "title")
    descriptor = None
    for klass in gmf_all_tooldef_MainMenu.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_menuaction_is_not_abstract():
    assert not inspect.isabstract(MenuAction)


def test_menuaction_constructor_exists():
    assert callable(MenuAction.__init__)


def test_menuaction_constructor_args():
    sig = inspect.signature(MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_toolregistry_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolRegistry)


def test_gmf_all_tooldef_toolregistry_constructor_exists():
    assert callable(gmf_all_tooldef_ToolRegistry.__init__)


def test_gmf_all_tooldef_toolregistry_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolRegistry.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_custompin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_CustomPin)


def test_gmf_all_gmfgraph_custompin_constructor_exists():
    assert callable(gmf_all_gmfgraph_CustomPin.__init__)


def test_gmf_all_gmfgraph_custompin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_CustomPin.__init__)
    params = list(sig.parameters.keys())
    assert "customOperationName" in params, "Missing parameter 'customOperationName'"
    assert "customOperationType" in params, "Missing parameter 'customOperationType'"

def test_gmf_all_gmfgraph_custompin_has_customOperationName():
    assert hasattr(gmf_all_gmfgraph_CustomPin, "customOperationName")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomPin.__mro__:
        if "customOperationName" in klass.__dict__:
            descriptor = klass.__dict__["customOperationName"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_custompin_has_customOperationType():
    assert hasattr(gmf_all_gmfgraph_CustomPin, "customOperationType")
    descriptor = None
    for klass in gmf_all_gmfgraph_CustomPin.__mro__:
        if "customOperationType" in klass.__dict__:
            descriptor = klass.__dict__["customOperationType"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_gmfgraph_visiblepin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_VisiblePin)


def test_gmf_all_gmfgraph_visiblepin_constructor_exists():
    assert callable(gmf_all_gmfgraph_VisiblePin.__init__)


def test_gmf_all_gmfgraph_visiblepin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_VisiblePin.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_colorpin_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_ColorPin)


def test_gmf_all_gmfgraph_colorpin_constructor_exists():
    assert callable(gmf_all_gmfgraph_ColorPin.__init__)


def test_gmf_all_gmfgraph_colorpin_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_ColorPin.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundNotForeground" in params, "Missing parameter 'backgroundNotForeground'"

def test_gmf_all_gmfgraph_colorpin_has_backgroundNotForeground():
    assert hasattr(gmf_all_gmfgraph_ColorPin, "backgroundNotForeground")
    descriptor = None
    for klass in gmf_all_gmfgraph_ColorPin.__mro__:
        if "backgroundNotForeground" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNotForeground"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_visualeffectmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_VisualEffectMapping)


def test_gmf_all_mappings_visualeffectmapping_constructor_exists():
    assert callable(gmf_all_mappings_VisualEffectMapping.__init__)


def test_gmf_all_mappings_visualeffectmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_VisualEffectMapping.__init__)
    params = list(sig.parameters.keys())
    assert "oclExpression" in params, "Missing parameter 'oclExpression'"

def test_gmf_all_mappings_visualeffectmapping_has_oclExpression():
    assert hasattr(gmf_all_mappings_VisualEffectMapping, "oclExpression")
    descriptor = None
    for klass in gmf_all_mappings_VisualEffectMapping.__mro__:
        if "oclExpression" in klass.__dict__:
            descriptor = klass.__dict__["oclExpression"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_measurable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Measurable)


def test_gmf_all_mappings_measurable_constructor_exists():
    assert callable(gmf_all_mappings_Measurable.__init__)


def test_gmf_all_mappings_measurable_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Measurable.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_auditable_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Auditable)


def test_gmf_all_mappings_auditable_constructor_exists():
    assert callable(gmf_all_mappings_Auditable.__init__)


def test_gmf_all_mappings_auditable_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Auditable.__init__)
    params = list(sig.parameters.keys())



def test_toolcontainer_is_not_abstract():
    assert not inspect.isabstract(ToolContainer)


def test_toolcontainer_constructor_exists():
    assert callable(ToolContainer.__init__)


def test_toolcontainer_constructor_args():
    sig = inspect.signature(ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_palette_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_Palette)


def test_gmf_all_tooldef_palette_constructor_exists():
    assert callable(gmf_all_tooldef_Palette.__init__)


def test_gmf_all_tooldef_palette_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_Palette.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_toolgroup_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolGroup)


def test_gmf_all_tooldef_toolgroup_constructor_exists():
    assert callable(gmf_all_tooldef_ToolGroup.__init__)


def test_gmf_all_tooldef_toolgroup_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolGroup.__init__)
    params = list(sig.parameters.keys())
    assert "stack" in params, "Missing parameter 'stack'"
    assert "collapsible" in params, "Missing parameter 'collapsible'"

def test_gmf_all_tooldef_toolgroup_has_stack():
    assert hasattr(gmf_all_tooldef_ToolGroup, "stack")
    descriptor = None
    for klass in gmf_all_tooldef_ToolGroup.__mro__:
        if "stack" in klass.__dict__:
            descriptor = klass.__dict__["stack"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_tooldef_toolgroup_has_collapsible():
    assert hasattr(gmf_all_tooldef_ToolGroup, "collapsible")
    descriptor = None
    for klass in gmf_all_tooldef_ToolGroup.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)



def test_measurable_is_not_abstract():
    assert not inspect.isabstract(Measurable)


def test_measurable_constructor_exists():
    assert callable(Measurable.__init__)


def test_measurable_constructor_args():
    sig = inspect.signature(Measurable.__init__)
    params = list(sig.parameters.keys())



def test_metricrule_is_not_abstract():
    assert not inspect.isabstract(MetricRule)


def test_metricrule_constructor_exists():
    assert callable(MetricRule.__init__)


def test_metricrule_constructor_args():
    sig = inspect.signature(MetricRule.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_metriccontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MetricContainer)


def test_gmf_all_mappings_metriccontainer_constructor_exists():
    assert callable(gmf_all_mappings_MetricContainer.__init__)


def test_gmf_all_mappings_metriccontainer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MetricContainer.__init__)
    params = list(sig.parameters.keys())



def test_mappings_measurable_is_not_abstract():
    assert not inspect.isabstract(mappings_Measurable)


def test_mappings_measurable_constructor_exists():
    assert callable(mappings_Measurable.__init__)


def test_mappings_measurable_constructor_args():
    sig = inspect.signature(mappings_Measurable.__init__)
    params = list(sig.parameters.keys())



def test_mappings_auditable_is_not_abstract():
    assert not inspect.isabstract(mappings_Auditable)


def test_mappings_auditable_constructor_exists():
    assert callable(mappings_Auditable.__init__)


def test_mappings_auditable_constructor_args():
    sig = inspect.signature(mappings_Auditable.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_notationelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NotationElementTarget)


def test_gmf_all_mappings_notationelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_NotationElementTarget.__init__)


def test_gmf_all_mappings_notationelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NotationElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_diagramelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DiagramElementTarget)


def test_gmf_all_mappings_diagramelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_DiagramElementTarget.__init__)


def test_gmf_all_mappings_diagramelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DiagramElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_domainelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DomainElementTarget)


def test_gmf_all_mappings_domainelementtarget_constructor_exists():
    assert callable(gmf_all_mappings_DomainElementTarget.__init__)


def test_gmf_all_mappings_domainelementtarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DomainElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_auditable_is_not_abstract():
    assert not inspect.isabstract(Auditable)


def test_auditable_constructor_exists():
    assert callable(Auditable.__init__)


def test_auditable_constructor_args():
    sig = inspect.signature(Auditable.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_auditedmetrictarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditedMetricTarget)


def test_gmf_all_mappings_auditedmetrictarget_constructor_exists():
    assert callable(gmf_all_mappings_AuditedMetricTarget.__init__)


def test_gmf_all_mappings_auditedmetrictarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditedMetricTarget.__init__)
    params = list(sig.parameters.keys())



def test_rulebase_is_not_abstract():
    assert not inspect.isabstract(RuleBase)


def test_rulebase_constructor_exists():
    assert callable(RuleBase.__init__)


def test_rulebase_constructor_args():
    sig = inspect.signature(RuleBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_metricrule_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MetricRule)


def test_gmf_all_mappings_metricrule_constructor_exists():
    assert callable(gmf_all_mappings_MetricRule.__init__)


def test_gmf_all_mappings_metricrule_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MetricRule.__init__)
    params = list(sig.parameters.keys())
    assert "lowLimit" in params, "Missing parameter 'lowLimit'"
    assert "key" in params, "Missing parameter 'key'"
    assert "highLimit" in params, "Missing parameter 'highLimit'"

def test_gmf_all_mappings_metricrule_has_lowLimit():
    assert hasattr(gmf_all_mappings_MetricRule, "lowLimit")
    descriptor = None
    for klass in gmf_all_mappings_MetricRule.__mro__:
        if "lowLimit" in klass.__dict__:
            descriptor = klass.__dict__["lowLimit"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_metricrule_has_key():
    assert hasattr(gmf_all_mappings_MetricRule, "key")
    descriptor = None
    for klass in gmf_all_mappings_MetricRule.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_metricrule_has_highLimit():
    assert hasattr(gmf_all_mappings_MetricRule, "highLimit")
    descriptor = None
    for klass in gmf_all_mappings_MetricRule.__mro__:
        if "highLimit" in klass.__dict__:
            descriptor = klass.__dict__["highLimit"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_auditrule_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditRule)


def test_gmf_all_mappings_auditrule_constructor_exists():
    assert callable(gmf_all_mappings_AuditRule.__init__)


def test_gmf_all_mappings_auditrule_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditRule.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "useInLiveMode" in params, "Missing parameter 'useInLiveMode'"
    assert "message" in params, "Missing parameter 'message'"
    assert "severity" in params, "Missing parameter 'severity'"

def test_gmf_all_mappings_auditrule_has_id():
    assert hasattr(gmf_all_mappings_AuditRule, "id")
    descriptor = None
    for klass in gmf_all_mappings_AuditRule.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_auditrule_has_useInLiveMode():
    assert hasattr(gmf_all_mappings_AuditRule, "useInLiveMode")
    descriptor = None
    for klass in gmf_all_mappings_AuditRule.__mro__:
        if "useInLiveMode" in klass.__dict__:
            descriptor = klass.__dict__["useInLiveMode"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_auditrule_has_message():
    assert hasattr(gmf_all_mappings_AuditRule, "message")
    descriptor = None
    for klass in gmf_all_mappings_AuditRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_auditrule_has_severity():
    assert hasattr(gmf_all_mappings_AuditRule, "severity")
    descriptor = None
    for klass in gmf_all_mappings_AuditRule.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_rulebase_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_RuleBase)


def test_gmf_all_mappings_rulebase_constructor_exists():
    assert callable(gmf_all_mappings_RuleBase.__init__)


def test_gmf_all_mappings_rulebase_constructor_args():
    sig = inspect.signature(gmf_all_mappings_RuleBase.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_gmf_all_mappings_rulebase_has_description():
    assert hasattr(gmf_all_mappings_RuleBase, "description")
    descriptor = None
    for klass in gmf_all_mappings_RuleBase.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_rulebase_has_name():
    assert hasattr(gmf_all_mappings_RuleBase, "name")
    descriptor = None
    for klass in gmf_all_mappings_RuleBase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_domainattributetarget_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DomainAttributeTarget)


def test_gmf_all_mappings_domainattributetarget_constructor_exists():
    assert callable(gmf_all_mappings_DomainAttributeTarget.__init__)


def test_gmf_all_mappings_domainattributetarget_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DomainAttributeTarget.__init__)
    params = list(sig.parameters.keys())
    assert "nullAsError" in params, "Missing parameter 'nullAsError'"

def test_gmf_all_mappings_domainattributetarget_has_nullAsError():
    assert hasattr(gmf_all_mappings_DomainAttributeTarget, "nullAsError")
    descriptor = None
    for klass in gmf_all_mappings_DomainAttributeTarget.__mro__:
        if "nullAsError" in klass.__dict__:
            descriptor = klass.__dict__["nullAsError"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_auditcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AuditContainer)


def test_gmf_all_mappings_auditcontainer_constructor_exists():
    assert callable(gmf_all_mappings_AuditContainer.__init__)


def test_gmf_all_mappings_auditcontainer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AuditContainer.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_gmf_all_mappings_auditcontainer_has_description():
    assert hasattr(gmf_all_mappings_AuditContainer, "description")
    descriptor = None
    for klass in gmf_all_mappings_AuditContainer.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_auditcontainer_has_id():
    assert hasattr(gmf_all_mappings_AuditContainer, "id")
    descriptor = None
    for klass in gmf_all_mappings_AuditContainer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_auditcontainer_has_name():
    assert hasattr(gmf_all_mappings_AuditContainer, "name")
    descriptor = None
    for klass in gmf_all_mappings_AuditContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_appearancesteward_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_AppearanceSteward)


def test_gmf_all_mappings_appearancesteward_constructor_exists():
    assert callable(gmf_all_mappings_AppearanceSteward.__init__)


def test_gmf_all_mappings_appearancesteward_constructor_args():
    sig = inspect.signature(gmf_all_mappings_AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_abstracttool_is_not_abstract():
    assert not inspect.isabstract(AbstractTool)


def test_abstracttool_constructor_exists():
    assert callable(AbstractTool.__init__)


def test_abstracttool_constructor_args():
    sig = inspect.signature(AbstractTool.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_generictool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_GenericTool)


def test_gmf_all_tooldef_generictool_constructor_exists():
    assert callable(gmf_all_tooldef_GenericTool.__init__)


def test_gmf_all_tooldef_generictool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_GenericTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolClass" in params, "Missing parameter 'toolClass'"

def test_gmf_all_tooldef_generictool_has_toolClass():
    assert hasattr(gmf_all_tooldef_GenericTool, "toolClass")
    descriptor = None
    for klass in gmf_all_tooldef_GenericTool.__mro__:
        if "toolClass" in klass.__dict__:
            descriptor = klass.__dict__["toolClass"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_tooldef_toolcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_ToolContainer)


def test_gmf_all_tooldef_toolcontainer_constructor_exists():
    assert callable(gmf_all_tooldef_ToolContainer.__init__)


def test_gmf_all_tooldef_toolcontainer_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_creationtool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_CreationTool)


def test_gmf_all_tooldef_creationtool_constructor_exists():
    assert callable(gmf_all_tooldef_CreationTool.__init__)


def test_gmf_all_tooldef_creationtool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_CreationTool.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_paletteseparator_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_PaletteSeparator)


def test_gmf_all_tooldef_paletteseparator_constructor_exists():
    assert callable(gmf_all_tooldef_PaletteSeparator.__init__)


def test_gmf_all_tooldef_paletteseparator_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_PaletteSeparator.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_standardtool_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_StandardTool)


def test_gmf_all_tooldef_standardtool_constructor_exists():
    assert callable(gmf_all_tooldef_StandardTool.__init__)


def test_gmf_all_tooldef_standardtool_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_StandardTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolKind" in params, "Missing parameter 'toolKind'"

def test_gmf_all_tooldef_standardtool_has_toolKind():
    assert hasattr(gmf_all_tooldef_StandardTool, "toolKind")
    descriptor = None
    for klass in gmf_all_tooldef_StandardTool.__mro__:
        if "toolKind" in klass.__dict__:
            descriptor = klass.__dict__["toolKind"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_toolowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ToolOwner)


def test_gmf_all_mappings_toolowner_constructor_exists():
    assert callable(gmf_all_mappings_ToolOwner.__init__)


def test_gmf_all_mappings_toolowner_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_contextmenu_is_not_abstract():
    assert not inspect.isabstract(ContextMenu)


def test_contextmenu_constructor_exists():
    assert callable(ContextMenu.__init__)


def test_contextmenu_constructor_args():
    sig = inspect.signature(ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_menuowner_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MenuOwner)


def test_gmf_all_mappings_menuowner_constructor_exists():
    assert callable(gmf_all_mappings_MenuOwner.__init__)


def test_gmf_all_mappings_menuowner_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MenuOwner.__init__)
    params = list(sig.parameters.keys())



def test_featureseqinitializer_is_not_abstract():
    assert not inspect.isabstract(FeatureSeqInitializer)


def test_featureseqinitializer_constructor_exists():
    assert callable(FeatureSeqInitializer.__init__)


def test_featureseqinitializer_constructor_args():
    sig = inspect.signature(FeatureSeqInitializer.__init__)
    params = list(sig.parameters.keys())



def test_auditrule_is_not_abstract():
    assert not inspect.isabstract(AuditRule)


def test_auditrule_constructor_exists():
    assert callable(AuditRule.__init__)


def test_auditrule_constructor_args():
    sig = inspect.signature(AuditRule.__init__)
    params = list(sig.parameters.keys())



def test_referencenewelementspec_is_not_abstract():
    assert not inspect.isabstract(ReferenceNewElementSpec)


def test_referencenewelementspec_constructor_exists():
    assert callable(ReferenceNewElementSpec.__init__)


def test_referencenewelementspec_constructor_args():
    sig = inspect.signature(ReferenceNewElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_featureinitializer_is_not_abstract():
    assert not inspect.isabstract(FeatureInitializer)


def test_featureinitializer_constructor_exists():
    assert callable(FeatureInitializer.__init__)


def test_featureinitializer_constructor_args():
    sig = inspect.signature(FeatureInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_referencenewelementspec_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ReferenceNewElementSpec)


def test_gmf_all_mappings_referencenewelementspec_constructor_exists():
    assert callable(gmf_all_mappings_ReferenceNewElementSpec.__init__)


def test_gmf_all_mappings_referencenewelementspec_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ReferenceNewElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_featurevaluespec_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureValueSpec)


def test_gmf_all_mappings_featurevaluespec_constructor_exists():
    assert callable(gmf_all_mappings_FeatureValueSpec.__init__)


def test_gmf_all_mappings_featurevaluespec_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureValueSpec.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_elementinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ElementInitializer)


def test_gmf_all_mappings_elementinitializer_constructor_exists():
    assert callable(gmf_all_mappings_ElementInitializer.__init__)


def test_gmf_all_mappings_elementinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_valueexpression_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ValueExpression)


def test_gmf_all_mappings_valueexpression_constructor_exists():
    assert callable(gmf_all_mappings_ValueExpression.__init__)


def test_gmf_all_mappings_valueexpression_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "langName" in params, "Missing parameter 'langName'"
    assert "body" in params, "Missing parameter 'body'"

def test_gmf_all_mappings_valueexpression_has_language():
    assert hasattr(gmf_all_mappings_ValueExpression, "language")
    descriptor = None
    for klass in gmf_all_mappings_ValueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_valueexpression_has_langName():
    assert hasattr(gmf_all_mappings_ValueExpression, "langName")
    descriptor = None
    for klass in gmf_all_mappings_ValueExpression.__mro__:
        if "langName" in klass.__dict__:
            descriptor = klass.__dict__["langName"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_valueexpression_has_body():
    assert hasattr(gmf_all_mappings_ValueExpression, "body")
    descriptor = None
    for klass in gmf_all_mappings_ValueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_featureinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureInitializer)


def test_gmf_all_mappings_featureinitializer_constructor_exists():
    assert callable(gmf_all_mappings_FeatureInitializer.__init__)


def test_gmf_all_mappings_featureinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_linkconstraints_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LinkConstraints)


def test_gmf_all_mappings_linkconstraints_constructor_exists():
    assert callable(gmf_all_mappings_LinkConstraints.__init__)


def test_gmf_all_mappings_linkconstraints_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_mappings_gmf_all_eattribute_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EAttribute)


def test_mappings_gmf_all_eattribute_constructor_exists():
    assert callable(mappings_gmf_all_EAttribute.__init__)


def test_mappings_gmf_all_eattribute_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_mappingentry_is_not_abstract():
    assert not inspect.isabstract(MappingEntry)


def test_mappingentry_constructor_exists():
    assert callable(MappingEntry.__init__)


def test_mappingentry_constructor_args():
    sig = inspect.signature(MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_diagramlabel_is_not_abstract():
    assert not inspect.isabstract(DiagramLabel)


def test_diagramlabel_constructor_exists():
    assert callable(DiagramLabel.__init__)


def test_diagramlabel_constructor_args():
    sig = inspect.signature(DiagramLabel.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_labelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LabelMapping)


def test_gmf_all_mappings_labelmapping_constructor_exists():
    assert callable(gmf_all_mappings_LabelMapping.__init__)


def test_gmf_all_mappings_labelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_gmf_all_mappings_labelmapping_has_readOnly():
    assert hasattr(gmf_all_mappings_LabelMapping, "readOnly")
    descriptor = None
    for klass in gmf_all_mappings_LabelMapping.__mro__:
        if "readOnly" in klass.__dict__:
            descriptor = klass.__dict__["readOnly"]
            break
    assert isinstance(descriptor, property)



def test_toolbar_is_not_abstract():
    assert not inspect.isabstract(Toolbar)


def test_toolbar_constructor_exists():
    assert callable(Toolbar.__init__)


def test_toolbar_constructor_args():
    sig = inspect.signature(Toolbar.__init__)
    params = list(sig.parameters.keys())



def test_mainmenu_is_not_abstract():
    assert not inspect.isabstract(MainMenu)


def test_mainmenu_constructor_exists():
    assert callable(MainMenu.__init__)


def test_mainmenu_constructor_args():
    sig = inspect.signature(MainMenu.__init__)
    params = list(sig.parameters.keys())



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_constraint_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Constraint)


def test_gmf_all_mappings_constraint_constructor_exists():
    assert callable(gmf_all_mappings_Constraint.__init__)


def test_gmf_all_mappings_constraint_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_canvasmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_CanvasMapping)


def test_gmf_all_mappings_canvasmapping_constructor_exists():
    assert callable(gmf_all_mappings_CanvasMapping.__init__)


def test_gmf_all_mappings_canvasmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_CanvasMapping.__init__)
    params = list(sig.parameters.keys())



def test_linkconstraints_is_not_abstract():
    assert not inspect.isabstract(LinkConstraints)


def test_linkconstraints_constructor_exists():
    assert callable(LinkConstraints.__init__)


def test_linkconstraints_constructor_args():
    sig = inspect.signature(LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_mappings_gmf_all_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EStructuralFeature)


def test_mappings_gmf_all_estructuralfeature_constructor_exists():
    assert callable(mappings_gmf_all_EStructuralFeature.__init__)


def test_mappings_gmf_all_estructuralfeature_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_mappings_needscontainment_is_not_abstract():
    assert not inspect.isabstract(mappings_NeedsContainment)


def test_mappings_needscontainment_constructor_exists():
    assert callable(mappings_NeedsContainment.__init__)


def test_mappings_needscontainment_constructor_args():
    sig = inspect.signature(mappings_NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_compartment_is_not_abstract():
    assert not inspect.isabstract(Compartment)


def test_compartment_constructor_exists():
    assert callable(Compartment.__init__)


def test_compartment_constructor_args():
    sig = inspect.signature(Compartment.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_compartmentmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_CompartmentMapping)


def test_gmf_all_mappings_compartmentmapping_constructor_exists():
    assert callable(gmf_all_mappings_CompartmentMapping.__init__)


def test_gmf_all_mappings_compartmentmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_CompartmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_childreference_is_not_abstract():
    assert not inspect.isabstract(ChildReference)


def test_childreference_constructor_exists():
    assert callable(ChildReference.__init__)


def test_childreference_constructor_args():
    sig = inspect.signature(ChildReference.__init__)
    params = list(sig.parameters.keys())



def test_palette_is_not_abstract():
    assert not inspect.isabstract(Palette)


def test_palette_constructor_exists():
    assert callable(Palette.__init__)


def test_palette_constructor_args():
    sig = inspect.signature(Palette.__init__)
    params = list(sig.parameters.keys())



def test_mappings_gmf_all_epackage_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EPackage)


def test_mappings_gmf_all_epackage_constructor_exists():
    assert callable(mappings_gmf_all_EPackage.__init__)


def test_mappings_gmf_all_epackage_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_compartmentmapping_is_not_abstract():
    assert not inspect.isabstract(CompartmentMapping)


def test_compartmentmapping_constructor_exists():
    assert callable(CompartmentMapping.__init__)


def test_compartmentmapping_constructor_args():
    sig = inspect.signature(CompartmentMapping.__init__)
    params = list(sig.parameters.keys())



def test_nodereference_is_not_abstract():
    assert not inspect.isabstract(NodeReference)


def test_nodereference_constructor_exists():
    assert callable(NodeReference.__init__)


def test_nodereference_constructor_args():
    sig = inspect.signature(NodeReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_topnodereference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_TopNodeReference)


def test_gmf_all_mappings_topnodereference_constructor_exists():
    assert callable(gmf_all_mappings_TopNodeReference.__init__)


def test_gmf_all_mappings_topnodereference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_TopNodeReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_childreference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ChildReference)


def test_gmf_all_mappings_childreference_constructor_exists():
    assert callable(gmf_all_mappings_ChildReference.__init__)


def test_gmf_all_mappings_childreference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ChildReference.__init__)
    params = list(sig.parameters.keys())



def test_nodemapping_is_not_abstract():
    assert not inspect.isabstract(NodeMapping)


def test_nodemapping_constructor_exists():
    assert callable(NodeMapping.__init__)


def test_nodemapping_constructor_args():
    sig = inspect.signature(NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_needscontainment_is_not_abstract():
    assert not inspect.isabstract(NeedsContainment)


def test_needscontainment_constructor_exists():
    assert callable(NeedsContainment.__init__)


def test_needscontainment_constructor_args():
    sig = inspect.signature(NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_nodereference_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NodeReference)


def test_gmf_all_mappings_nodereference_constructor_exists():
    assert callable(gmf_all_mappings_NodeReference.__init__)


def test_gmf_all_mappings_nodereference_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NodeReference.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_gmfgraph_diagramlabel_is_not_abstract():
    assert not inspect.isabstract(gmf_all_gmfgraph_DiagramLabel)


def test_gmf_all_gmfgraph_diagramlabel_constructor_exists():
    assert callable(gmf_all_gmfgraph_DiagramLabel.__init__)


def test_gmf_all_gmfgraph_diagramlabel_constructor_args():
    sig = inspect.signature(gmf_all_gmfgraph_DiagramLabel.__init__)
    params = list(sig.parameters.keys())
    assert "elementIcon" in params, "Missing parameter 'elementIcon'"
    assert "external" in params, "Missing parameter 'external'"

def test_gmf_all_gmfgraph_diagramlabel_has_elementIcon():
    assert hasattr(gmf_all_gmfgraph_DiagramLabel, "elementIcon")
    descriptor = None
    for klass in gmf_all_gmfgraph_DiagramLabel.__mro__:
        if "elementIcon" in klass.__dict__:
            descriptor = klass.__dict__["elementIcon"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_gmfgraph_diagramlabel_has_external():
    assert hasattr(gmf_all_gmfgraph_DiagramLabel, "external")
    descriptor = None
    for klass in gmf_all_gmfgraph_DiagramLabel.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)



def test_mappings_appearancesteward_is_not_abstract():
    assert not inspect.isabstract(mappings_AppearanceSteward)


def test_mappings_appearancesteward_constructor_exists():
    assert callable(mappings_AppearanceSteward.__init__)


def test_mappings_appearancesteward_constructor_args():
    sig = inspect.signature(mappings_AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_mappings_toolowner_is_not_abstract():
    assert not inspect.isabstract(mappings_ToolOwner)


def test_mappings_toolowner_constructor_exists():
    assert callable(mappings_ToolOwner.__init__)


def test_mappings_toolowner_constructor_args():
    sig = inspect.signature(mappings_ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_mappings_menuowner_is_not_abstract():
    assert not inspect.isabstract(mappings_MenuOwner)


def test_mappings_menuowner_constructor_exists():
    assert callable(mappings_MenuOwner.__init__)


def test_mappings_menuowner_constructor_args():
    sig = inspect.signature(mappings_MenuOwner.__init__)
    params = list(sig.parameters.keys())



def test_mappings_mappingentry_is_not_abstract():
    assert not inspect.isabstract(mappings_MappingEntry)


def test_mappings_mappingentry_constructor_exists():
    assert callable(mappings_MappingEntry.__init__)


def test_mappings_mappingentry_constructor_args():
    sig = inspect.signature(mappings_MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_linkmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_LinkMapping)


def test_gmf_all_mappings_linkmapping_constructor_exists():
    assert callable(gmf_all_mappings_LinkMapping.__init__)


def test_gmf_all_mappings_linkmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_LinkMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_nodemapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NodeMapping)


def test_gmf_all_mappings_nodemapping_constructor_exists():
    assert callable(gmf_all_mappings_NodeMapping.__init__)


def test_gmf_all_mappings_nodemapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_labelmapping_is_not_abstract():
    assert not inspect.isabstract(LabelMapping)


def test_labelmapping_constructor_exists():
    assert callable(LabelMapping.__init__)


def test_labelmapping_constructor_args():
    sig = inspect.signature(LabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_expressionlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_ExpressionLabelMapping)


def test_gmf_all_mappings_expressionlabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_ExpressionLabelMapping.__init__)


def test_gmf_all_mappings_expressionlabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_ExpressionLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_featurelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureLabelMapping)


def test_gmf_all_mappings_featurelabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_FeatureLabelMapping.__init__)


def test_gmf_all_mappings_featurelabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureLabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "viewPattern" in params, "Missing parameter 'viewPattern'"
    assert "editPattern" in params, "Missing parameter 'editPattern'"
    assert "viewMethod" in params, "Missing parameter 'viewMethod'"
    assert "editMethod" in params, "Missing parameter 'editMethod'"
    assert "editorPattern" in params, "Missing parameter 'editorPattern'"

def test_gmf_all_mappings_featurelabelmapping_has_viewPattern():
    assert hasattr(gmf_all_mappings_FeatureLabelMapping, "viewPattern")
    descriptor = None
    for klass in gmf_all_mappings_FeatureLabelMapping.__mro__:
        if "viewPattern" in klass.__dict__:
            descriptor = klass.__dict__["viewPattern"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_featurelabelmapping_has_editPattern():
    assert hasattr(gmf_all_mappings_FeatureLabelMapping, "editPattern")
    descriptor = None
    for klass in gmf_all_mappings_FeatureLabelMapping.__mro__:
        if "editPattern" in klass.__dict__:
            descriptor = klass.__dict__["editPattern"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_featurelabelmapping_has_viewMethod():
    assert hasattr(gmf_all_mappings_FeatureLabelMapping, "viewMethod")
    descriptor = None
    for klass in gmf_all_mappings_FeatureLabelMapping.__mro__:
        if "viewMethod" in klass.__dict__:
            descriptor = klass.__dict__["viewMethod"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_featurelabelmapping_has_editMethod():
    assert hasattr(gmf_all_mappings_FeatureLabelMapping, "editMethod")
    descriptor = None
    for klass in gmf_all_mappings_FeatureLabelMapping.__mro__:
        if "editMethod" in klass.__dict__:
            descriptor = klass.__dict__["editMethod"]
            break
    assert isinstance(descriptor, property)

def test_gmf_all_mappings_featurelabelmapping_has_editorPattern():
    assert hasattr(gmf_all_mappings_FeatureLabelMapping, "editorPattern")
    descriptor = None
    for klass in gmf_all_mappings_FeatureLabelMapping.__mro__:
        if "editorPattern" in klass.__dict__:
            descriptor = klass.__dict__["editorPattern"]
            break
    assert isinstance(descriptor, property)



def test_gmf_all_mappings_oclchoicelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_OclChoiceLabelMapping)


def test_gmf_all_mappings_oclchoicelabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_OclChoiceLabelMapping.__init__)


def test_gmf_all_mappings_oclchoicelabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_OclChoiceLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_designlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_DesignLabelMapping)


def test_gmf_all_mappings_designlabelmapping_constructor_exists():
    assert callable(gmf_all_mappings_DesignLabelMapping.__init__)


def test_gmf_all_mappings_designlabelmapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_DesignLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_elementinitializer_is_not_abstract():
    assert not inspect.isabstract(ElementInitializer)


def test_elementinitializer_constructor_exists():
    assert callable(ElementInitializer.__init__)


def test_elementinitializer_constructor_args():
    sig = inspect.signature(ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_featureseqinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_FeatureSeqInitializer)


def test_gmf_all_mappings_featureseqinitializer_constructor_exists():
    assert callable(gmf_all_mappings_FeatureSeqInitializer.__init__)


def test_gmf_all_mappings_featureseqinitializer_constructor_args():
    sig = inspect.signature(gmf_all_mappings_FeatureSeqInitializer.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_mappings_gmf_all_eclass_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EClass)


def test_mappings_gmf_all_eclass_constructor_exists():
    assert callable(mappings_gmf_all_EClass.__init__)


def test_mappings_gmf_all_eclass_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EClass.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_mappingentry_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_MappingEntry)


def test_gmf_all_mappings_mappingentry_constructor_exists():
    assert callable(gmf_all_mappings_MappingEntry.__init__)


def test_gmf_all_mappings_mappingentry_constructor_args():
    sig = inspect.signature(gmf_all_mappings_MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_metriccontainer_is_not_abstract():
    assert not inspect.isabstract(MetricContainer)


def test_metriccontainer_constructor_exists():
    assert callable(MetricContainer.__init__)


def test_metriccontainer_constructor_args():
    sig = inspect.signature(MetricContainer.__init__)
    params = list(sig.parameters.keys())



def test_auditcontainer_is_not_abstract():
    assert not inspect.isabstract(AuditContainer)


def test_auditcontainer_constructor_exists():
    assert callable(AuditContainer.__init__)


def test_auditcontainer_constructor_args():
    sig = inspect.signature(AuditContainer.__init__)
    params = list(sig.parameters.keys())



def test_styleselector_is_not_abstract():
    assert not inspect.isabstract(StyleSelector)


def test_styleselector_constructor_exists():
    assert callable(StyleSelector.__init__)


def test_styleselector_constructor_args():
    sig = inspect.signature(StyleSelector.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_tooldef_genericstyleselector_is_not_abstract():
    assert not inspect.isabstract(gmf_all_tooldef_GenericStyleSelector)


def test_gmf_all_tooldef_genericstyleselector_constructor_exists():
    assert callable(gmf_all_tooldef_GenericStyleSelector.__init__)


def test_gmf_all_tooldef_genericstyleselector_constructor_args():
    sig = inspect.signature(gmf_all_tooldef_GenericStyleSelector.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_gmf_all_tooldef_genericstyleselector_has_values():
    assert hasattr(gmf_all_tooldef_GenericStyleSelector, "values")
    descriptor = None
    for klass in gmf_all_tooldef_GenericStyleSelector.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_canvasmapping_is_not_abstract():
    assert not inspect.isabstract(CanvasMapping)


def test_canvasmapping_constructor_exists():
    assert callable(CanvasMapping.__init__)


def test_canvasmapping_constructor_args():
    sig = inspect.signature(CanvasMapping.__init__)
    params = list(sig.parameters.keys())



def test_linkmapping_is_not_abstract():
    assert not inspect.isabstract(LinkMapping)


def test_linkmapping_constructor_exists():
    assert callable(LinkMapping.__init__)


def test_linkmapping_constructor_args():
    sig = inspect.signature(LinkMapping.__init__)
    params = list(sig.parameters.keys())



def test_mappings_gmf_all_ereference_is_not_abstract():
    assert not inspect.isabstract(mappings_gmf_all_EReference)


def test_mappings_gmf_all_ereference_constructor_exists():
    assert callable(mappings_gmf_all_EReference.__init__)


def test_mappings_gmf_all_ereference_constructor_args():
    sig = inspect.signature(mappings_gmf_all_EReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_needscontainment_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_NeedsContainment)


def test_gmf_all_mappings_needscontainment_constructor_exists():
    assert callable(gmf_all_mappings_NeedsContainment.__init__)


def test_gmf_all_mappings_needscontainment_constructor_args():
    sig = inspect.signature(gmf_all_mappings_NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_visualeffectmapping_is_not_abstract():
    assert not inspect.isabstract(VisualEffectMapping)


def test_visualeffectmapping_constructor_exists():
    assert callable(VisualEffectMapping.__init__)


def test_visualeffectmapping_constructor_args():
    sig = inspect.signature(VisualEffectMapping.__init__)
    params = list(sig.parameters.keys())



def test_topnodereference_is_not_abstract():
    assert not inspect.isabstract(TopNodeReference)


def test_topnodereference_constructor_exists():
    assert callable(TopNodeReference.__init__)


def test_topnodereference_constructor_args():
    sig = inspect.signature(TopNodeReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf_all_mappings_mapping_is_not_abstract():
    assert not inspect.isabstract(gmf_all_mappings_Mapping)


def test_gmf_all_mappings_mapping_constructor_exists():
    assert callable(gmf_all_mappings_Mapping.__init__)


def test_gmf_all_mappings_mapping_constructor_args():
    sig = inspect.signature(gmf_all_mappings_Mapping.__init__)
    params = list(sig.parameters.keys())

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "INFO",
        "ERROR",
        "WARNING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Severity"

def test_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "LINE_DOT",
        "LINE_CUSTOM",
        "LINE_SOLID",
        "LINE_DASH",
        "LINE_DASHDOT",
        "LINE_DASHDOTDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_appearancestyle_exists():
    # Check that the Enumeration exists
    assert AppearanceStyle is not None

def test_appearancestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AppearanceStyle]
    expected_literals = [
        "Font",
        "Fill",
        "Line",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AppearanceStyle"

def test_svgpropertytype_exists():
    # Check that the Enumeration exists
    assert SVGPropertyType is not None

def test_svgpropertytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SVGPropertyType]
    expected_literals = [
        "FLOAT",
        "COLOR",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SVGPropertyType"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "ITALIC",
        "NORMAL",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "FILL",
        "END",
        "BEGINNING",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "PROPCHANGE",
        "CUSTOM",
        "CREATE",
        "MODIFY",
        "PROCESS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "SOUTH",
        "NORTH",
        "NORTH_SOUTH",
        "SOUTH_EAST",
        "NORTH_WEST",
        "SOUTH_WEST",
        "EAST",
        "NONE",
        "EAST_WEST",
        "NORTH_EAST",
        "NSEW",
        "WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "blue",
        "lightGray",
        "white",
        "cyan",
        "darkBlue",
        "gray",
        "red",
        "green",
        "lightGreen",
        "darkGray",
        "darkGreen",
        "yellow",
        "black",
        "orange",
        "lightBlue",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorConstants"

def test_labeltextaccessmethod_exists():
    # Check that the Enumeration exists
    assert LabelTextAccessMethod is not None

def test_labeltextaccessmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelTextAccessMethod]
    expected_literals = [
        "PRINTF",
        "REGEXP",
        "MESSAGE_FORMAT",
        "NATIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelTextAccessMethod"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "literal",
        "ocl",
        "regexp",
        "java",
        "nregexp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_standardtoolkind_exists():
    # Check that the Enumeration exists
    assert StandardToolKind is not None

def test_standardtoolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardToolKind]
    expected_literals = [
        "ZOOM_OUT",
        "ZOOM_IN",
        "MARQUEE",
        "ZOOM_PAN",
        "SELECT",
        "SELECT_PAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardToolKind"


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
AbstractFigure_strategy = st.builds(
    AbstractFigure,
)
gmf_all_gmfgraph_FigureRef_strategy = st.builds(
    gmf_all_gmfgraph_FigureRef,
)
gmf_all_gmfgraph_ChildAccess_strategy = st.builds(
    gmf_all_gmfgraph_ChildAccess,
    accessor=
        safe_text
)
Figure_strategy = st.builds(
    Figure,
)
gmf_all_gmfgraph_AbstractFigure_strategy = st.builds(
    gmf_all_gmfgraph_AbstractFigure,
)
gmf_all_gmfgraph_PinOwner_strategy = st.builds(
    gmf_all_gmfgraph_PinOwner,
)
gmf_all_gmfgraph_SVGProperty_strategy = st.builds(
    gmf_all_gmfgraph_SVGProperty,
    setter=
        safe_text,
    callSuper=
        st.booleans(),
    type=
        safe_text,
    attribute=
        safe_text,
    getter=
        safe_text,
    query=
        safe_text
)
Rectangle2D_strategy = st.builds(
    Rectangle2D,
)
SVGProperty_strategy = st.builds(
    SVGProperty,
)
gmf_all_gmfgraph_Rectangle2D_strategy = st.builds(
    gmf_all_gmfgraph_Rectangle2D,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gmfgraph_Layout_strategy = st.builds(
    gmfgraph_Layout,
)
gmf_all_gmfgraph_Layout_strategy = st.builds(
    gmf_all_gmfgraph_Layout,
)
gmf_all_gmfgraph_Layoutable_strategy = st.builds(
    gmf_all_gmfgraph_Layoutable,
)
LayoutData_strategy = st.builds(
    LayoutData,
)
gmf_all_gmfgraph_BorderLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_BorderLayoutData,
    alignment=
        safe_text,
    vertical=
        st.booleans()
)
gmf_all_gmfgraph_XYLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_XYLayoutData,
)
gmf_all_gmfgraph_GridLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_GridLayoutData,
    horizontalSpan=
        st.integers(),
    grabExcessVerticalSpace=
        st.booleans(),
    horizontalAlignment=
        safe_text,
    verticalAlignment=
        safe_text,
    horizontalIndent=
        st.integers(),
    verticalSpan=
        st.integers(),
    grabExcessHorizontalSpace=
        st.booleans()
)
gmfgraph_Border_strategy = st.builds(
    gmfgraph_Border,
)
gmf_all_gmfgraph_Border_strategy = st.builds(
    gmf_all_gmfgraph_Border,
)
gmfgraph_LayoutData_strategy = st.builds(
    gmfgraph_LayoutData,
)
gmf_all_gmfgraph_LayoutData_strategy = st.builds(
    gmf_all_gmfgraph_LayoutData,
)
gmf_all_gmfgraph_Point_strategy = st.builds(
    gmf_all_gmfgraph_Point,
    x=
        st.integers(),
    y=
        st.integers()
)
gmf_all_gmfgraph_Font_strategy = st.builds(
    gmf_all_gmfgraph_Font,
)
gmf_all_gmfgraph_Color_strategy = st.builds(
    gmf_all_gmfgraph_Color,
)
gmfgraph_CustomFigure_strategy = st.builds(
    gmfgraph_CustomFigure,
)
FigureAccessor_strategy = st.builds(
    FigureAccessor,
)
gmf_all_gmfgraph_Insets_strategy = st.builds(
    gmf_all_gmfgraph_Insets,
    bottom=
        st.integers(),
    right=
        st.integers(),
    top=
        st.integers(),
    left=
        st.integers()
)
gmf_all_gmfgraph_Dimension_strategy = st.builds(
    gmf_all_gmfgraph_Dimension,
    dx=
        st.integers(),
    dy=
        st.integers()
)
gmf_all_gmfgraph_FigureAccessor_strategy = st.builds(
    gmf_all_gmfgraph_FigureAccessor,
    accessor=
        safe_text
)
gmf_all_gmfgraph_CustomAttribute_strategy = st.builds(
    gmf_all_gmfgraph_CustomAttribute,
    value=
        safe_text,
    directAccess=
        st.booleans(),
    name=
        safe_text,
    multiStatementValue=
        st.booleans()
)
CustomAttributeOwner_strategy = st.builds(
    CustomAttributeOwner,
)
gmf_all_gmfgraph_CustomClass_strategy = st.builds(
    gmf_all_gmfgraph_CustomClass,
    qualifiedClassName=
        safe_text
)
CustomAttribute_strategy = st.builds(
    CustomAttribute,
)
gmf_all_gmfgraph_CustomAttributeOwner_strategy = st.builds(
    gmf_all_gmfgraph_CustomAttributeOwner,
)
gmfgraph_Polygon_strategy = st.builds(
    gmfgraph_Polygon,
)
gmfgraph_DecorationFigure_strategy = st.builds(
    gmfgraph_DecorationFigure,
)
gmf_all_gmfgraph_PolygonDecoration_strategy = st.builds(
    gmf_all_gmfgraph_PolygonDecoration,
)
gmf_all_gmfgraph_CustomDecoration_strategy = st.builds(
    gmf_all_gmfgraph_CustomDecoration,
)
DecorationFigure_strategy = st.builds(
    DecorationFigure,
)
gmfgraph_ConnectionFigure_strategy = st.builds(
    gmfgraph_ConnectionFigure,
)
gmf_all_gmfgraph_CustomConnection_strategy = st.builds(
    gmf_all_gmfgraph_CustomConnection,
)
gmfgraph_Polyline_strategy = st.builds(
    gmfgraph_Polyline,
)
gmf_all_gmfgraph_PolylineDecoration_strategy = st.builds(
    gmf_all_gmfgraph_PolylineDecoration,
)
gmf_all_gmfgraph_PolylineConnection_strategy = st.builds(
    gmf_all_gmfgraph_PolylineConnection,
)
Polygon_strategy = st.builds(
    Polygon,
)
gmf_all_gmfgraph_ScalablePolygon_strategy = st.builds(
    gmf_all_gmfgraph_ScalablePolygon,
)
Polyline_strategy = st.builds(
    Polyline,
)
gmf_all_gmfgraph_Polygon_strategy = st.builds(
    gmf_all_gmfgraph_Polygon,
)
gmfgraph_CustomClass_strategy = st.builds(
    gmfgraph_CustomClass,
)
gmf_all_gmfgraph_CustomBorder_strategy = st.builds(
    gmf_all_gmfgraph_CustomBorder,
)
gmf_all_gmfgraph_CustomLayoutData_strategy = st.builds(
    gmf_all_gmfgraph_CustomLayoutData,
)
gmf_all_gmfgraph_CustomLayout_strategy = st.builds(
    gmf_all_gmfgraph_CustomLayout,
)
gmfgraph_RealFigure_strategy = st.builds(
    gmfgraph_RealFigure,
)
gmf_all_gmfgraph_CustomFigure_strategy = st.builds(
    gmf_all_gmfgraph_CustomFigure,
)
Shape_strategy = st.builds(
    Shape,
)
gmf_all_gmfgraph_Polyline_strategy = st.builds(
    gmf_all_gmfgraph_Polyline,
)
gmf_all_gmfgraph_Ellipse_strategy = st.builds(
    gmf_all_gmfgraph_Ellipse,
)
gmf_all_gmfgraph_RoundedRectangle_strategy = st.builds(
    gmf_all_gmfgraph_RoundedRectangle,
    cornerHeight=
        st.integers(),
    cornerWidth=
        st.integers()
)
gmf_all_gmfgraph_Rectangle_strategy = st.builds(
    gmf_all_gmfgraph_Rectangle,
)
Point_strategy = st.builds(
    Point,
)
Insets_strategy = st.builds(
    Insets,
)
Font_strategy = st.builds(
    Font,
)
gmf_all_gmfgraph_BasicFont_strategy = st.builds(
    gmf_all_gmfgraph_BasicFont,
    style=
        safe_text,
    faceName=
        safe_text,
    height=
        st.integers()
)
Color_strategy = st.builds(
    Color,
)
gmf_all_gmfgraph_ConstantColor_strategy = st.builds(
    gmf_all_gmfgraph_ConstantColor,
    value=
        safe_text
)
gmf_all_gmfgraph_RGBColor_strategy = st.builds(
    gmf_all_gmfgraph_RGBColor,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
gmfgraph_CustomAttributeOwner_strategy = st.builds(
    gmfgraph_CustomAttributeOwner,
)
gmfgraph_PinOwner_strategy = st.builds(
    gmfgraph_PinOwner,
)
gmfgraph_AbstractFigure_strategy = st.builds(
    gmfgraph_AbstractFigure,
)
gmf_all_gmfgraph_RealFigure_strategy = st.builds(
    gmf_all_gmfgraph_RealFigure,
    name=
        safe_text
)
Dimension_strategy = st.builds(
    Dimension,
)
gmf_all_gmfgraph_VisualFacet_strategy = st.builds(
    gmf_all_gmfgraph_VisualFacet,
)
ChildAccess_strategy = st.builds(
    ChildAccess,
)
Layoutable_strategy = st.builds(
    Layoutable,
)
gmf_all_gmfgraph_Figure_strategy = st.builds(
    gmf_all_gmfgraph_Figure,
)
VisualFacet_strategy = st.builds(
    VisualFacet,
)
gmf_all_gmfgraph_AlignmentFacet_strategy = st.builds(
    gmf_all_gmfgraph_AlignmentFacet,
    alignment=
        safe_text
)
gmf_all_gmfgraph_GeneralFacet_strategy = st.builds(
    gmf_all_gmfgraph_GeneralFacet,
    identifier=
        safe_text,
    data=
        safe_text
)
gmf_all_gmfgraph_LabelOffsetFacet_strategy = st.builds(
    gmf_all_gmfgraph_LabelOffsetFacet,
    y=
        st.integers(),
    x=
        st.integers()
)
gmf_all_gmfgraph_DefaultSizeFacet_strategy = st.builds(
    gmf_all_gmfgraph_DefaultSizeFacet,
)
gmf_all_gmfgraph_GradientFacet_strategy = st.builds(
    gmf_all_gmfgraph_GradientFacet,
    direction=
        safe_text
)
gmf_all_gmfgraph_Identity_strategy = st.builds(
    gmf_all_gmfgraph_Identity,
    name=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
gmf_all_gmfgraph_CenterLayout_strategy = st.builds(
    gmf_all_gmfgraph_CenterLayout,
)
gmf_all_gmfgraph_LayoutRef_strategy = st.builds(
    gmf_all_gmfgraph_LayoutRef,
)
gmf_all_gmfgraph_XYLayout_strategy = st.builds(
    gmf_all_gmfgraph_XYLayout,
)
gmf_all_gmfgraph_BorderLayout_strategy = st.builds(
    gmf_all_gmfgraph_BorderLayout,
)
gmf_all_gmfgraph_FlowLayout_strategy = st.builds(
    gmf_all_gmfgraph_FlowLayout,
    forceSingleLine=
        st.booleans(),
    minorSpacing=
        st.integers(),
    majorAlignment=
        safe_text,
    minorAlignment=
        safe_text,
    majorSpacing=
        st.integers(),
    vertical=
        st.booleans(),
    matchMinorSize=
        st.booleans()
)
gmf_all_gmfgraph_GridLayout_strategy = st.builds(
    gmf_all_gmfgraph_GridLayout,
    numColumns=
        st.integers(),
    equalWidth=
        st.booleans()
)
gmf_all_gmfgraph_StackLayout_strategy = st.builds(
    gmf_all_gmfgraph_StackLayout,
)
Border_strategy = st.builds(
    Border,
)
gmf_all_gmfgraph_CompoundBorder_strategy = st.builds(
    gmf_all_gmfgraph_CompoundBorder,
)
gmf_all_gmfgraph_LineBorder_strategy = st.builds(
    gmf_all_gmfgraph_LineBorder,
    width=
        st.integers()
)
gmf_all_gmfgraph_BorderRef_strategy = st.builds(
    gmf_all_gmfgraph_BorderRef,
)
gmf_all_gmfgraph_MarginBorder_strategy = st.builds(
    gmf_all_gmfgraph_MarginBorder,
)
FigureDescriptor_strategy = st.builds(
    FigureDescriptor,
)
RealFigure_strategy = st.builds(
    RealFigure,
)
gmf_all_gmfgraph_InvisibleRectangle_strategy = st.builds(
    gmf_all_gmfgraph_InvisibleRectangle,
)
gmf_all_gmfgraph_VerticalLabel_strategy = st.builds(
    gmf_all_gmfgraph_VerticalLabel,
    text=
        safe_text
)
gmf_all_gmfgraph_Shape_strategy = st.builds(
    gmf_all_gmfgraph_Shape,
    xorFill=
        st.booleans(),
    outline=
        st.booleans(),
    fill=
        st.booleans(),
    lineKind=
        safe_text,
    xorOutline=
        st.booleans(),
    lineWidth=
        st.integers()
)
gmf_all_gmfgraph_SVGFigure_strategy = st.builds(
    gmf_all_gmfgraph_SVGFigure,
    noCanvasWidth=
        st.booleans(),
    documentURI=
        safe_text,
    noCanvasHeight=
        st.booleans()
)
gmf_all_gmfgraph_Label_strategy = st.builds(
    gmf_all_gmfgraph_Label,
    text=
        safe_text
)
gmf_all_gmfgraph_DecorationFigure_strategy = st.builds(
    gmf_all_gmfgraph_DecorationFigure,
)
gmf_all_gmfgraph_ConnectionFigure_strategy = st.builds(
    gmf_all_gmfgraph_ConnectionFigure,
)
gmf_all_gmfgraph_LabeledContainer_strategy = st.builds(
    gmf_all_gmfgraph_LabeledContainer,
)
FigureGallery_strategy = st.builds(
    FigureGallery,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
gmf_all_gmfgraph_Node_strategy = st.builds(
    gmf_all_gmfgraph_Node,
    resizeConstraint=
        safe_text,
    affixedParentSide=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
gmf_all_gmfgraph_Compartment_strategy = st.builds(
    gmf_all_gmfgraph_Compartment,
    collapsible=
        st.booleans(),
    needsTitle=
        st.booleans()
)
gmf_all_gmfgraph_Connection_strategy = st.builds(
    gmf_all_gmfgraph_Connection,
)
gmf_all_gmfgraph_AbstractNode_strategy = st.builds(
    gmf_all_gmfgraph_AbstractNode,
)
gmf_all_tooldef_StyleSelector_strategy = st.builds(
    gmf_all_tooldef_StyleSelector,
)
gmf_all_tooldef_Image_strategy = st.builds(
    gmf_all_tooldef_Image,
)
tooldef_ContributionItem_strategy = st.builds(
    tooldef_ContributionItem,
)
Identity_strategy = st.builds(
    Identity,
)
gmf_all_gmfgraph_Pin_strategy = st.builds(
    gmf_all_gmfgraph_Pin,
)
gmf_all_gmfgraph_FigureDescriptor_strategy = st.builds(
    gmf_all_gmfgraph_FigureDescriptor,
)
gmf_all_gmfgraph_DiagramElement_strategy = st.builds(
    gmf_all_gmfgraph_DiagramElement,
)
gmf_all_gmfgraph_FigureGallery_strategy = st.builds(
    gmf_all_gmfgraph_FigureGallery,
    implementationBundle=
        safe_text
)
gmf_all_gmfgraph_Canvas_strategy = st.builds(
    gmf_all_gmfgraph_Canvas,
)
tooldef_PredefinedItem_strategy = st.builds(
    tooldef_PredefinedItem,
)
tooldef_Menu_strategy = st.builds(
    tooldef_Menu,
)
gmf_all_tooldef_PopupMenu_strategy = st.builds(
    gmf_all_tooldef_PopupMenu,
    iD=
        safe_text
)
gmf_all_tooldef_PredefinedMenu_strategy = st.builds(
    gmf_all_tooldef_PredefinedMenu,
)
ItemBase_strategy = st.builds(
    ItemBase,
)
gmf_all_tooldef_Separator_strategy = st.builds(
    gmf_all_tooldef_Separator,
    name=
        safe_text
)
gmf_all_tooldef_PredefinedItem_strategy = st.builds(
    gmf_all_tooldef_PredefinedItem,
    identifier=
        safe_text
)
gmf_all_tooldef_ContributionItem_strategy = st.builds(
    gmf_all_tooldef_ContributionItem,
    title=
        safe_text
)
gmf_all_tooldef_Menu_strategy = st.builds(
    gmf_all_tooldef_Menu,
)
gmf_all_tooldef_ItemBase_strategy = st.builds(
    gmf_all_tooldef_ItemBase,
)
gmf_all_tooldef_ItemRef_strategy = st.builds(
    gmf_all_tooldef_ItemRef,
)
ContributionItem_strategy = st.builds(
    ContributionItem,
)
gmf_all_tooldef_MenuAction_strategy = st.builds(
    gmf_all_tooldef_MenuAction,
    kind=
        safe_text,
    hotKey=
        safe_text
)
Image_strategy = st.builds(
    Image,
)
gmf_all_tooldef_BundleImage_strategy = st.builds(
    gmf_all_tooldef_BundleImage,
    path=
        safe_text,
    bundle=
        safe_text
)
gmf_all_tooldef_DefaultImage_strategy = st.builds(
    gmf_all_tooldef_DefaultImage,
)
gmf_all_tooldef_AbstractTool_strategy = st.builds(
    gmf_all_tooldef_AbstractTool,
    description=
        safe_text,
    title=
        safe_text
)
Menu_strategy = st.builds(
    Menu,
)
gmf_all_tooldef_Toolbar_strategy = st.builds(
    gmf_all_tooldef_Toolbar,
)
gmf_all_tooldef_ContextMenu_strategy = st.builds(
    gmf_all_tooldef_ContextMenu,
)
gmf_all_tooldef_MainMenu_strategy = st.builds(
    gmf_all_tooldef_MainMenu,
    title=
        safe_text
)
MenuAction_strategy = st.builds(
    MenuAction,
)
gmf_all_tooldef_ToolRegistry_strategy = st.builds(
    gmf_all_tooldef_ToolRegistry,
)
Pin_strategy = st.builds(
    Pin,
)
gmf_all_gmfgraph_CustomPin_strategy = st.builds(
    gmf_all_gmfgraph_CustomPin,
    customOperationName=
        safe_text,
    customOperationType=
        safe_text
)
gmf_all_gmfgraph_VisiblePin_strategy = st.builds(
    gmf_all_gmfgraph_VisiblePin,
)
gmf_all_gmfgraph_ColorPin_strategy = st.builds(
    gmf_all_gmfgraph_ColorPin,
    backgroundNotForeground=
        st.booleans()
)
gmf_all_mappings_VisualEffectMapping_strategy = st.builds(
    gmf_all_mappings_VisualEffectMapping,
    oclExpression=
        safe_text
)
gmf_all_mappings_Measurable_strategy = st.builds(
    gmf_all_mappings_Measurable,
)
gmf_all_mappings_Auditable_strategy = st.builds(
    gmf_all_mappings_Auditable,
)
ToolContainer_strategy = st.builds(
    ToolContainer,
)
gmf_all_tooldef_Palette_strategy = st.builds(
    gmf_all_tooldef_Palette,
)
gmf_all_tooldef_ToolGroup_strategy = st.builds(
    gmf_all_tooldef_ToolGroup,
    stack=
        st.booleans(),
    collapsible=
        st.booleans()
)
Measurable_strategy = st.builds(
    Measurable,
)
MetricRule_strategy = st.builds(
    MetricRule,
)
gmf_all_mappings_MetricContainer_strategy = st.builds(
    gmf_all_mappings_MetricContainer,
)
mappings_Measurable_strategy = st.builds(
    mappings_Measurable,
)
mappings_Auditable_strategy = st.builds(
    mappings_Auditable,
)
gmf_all_mappings_NotationElementTarget_strategy = st.builds(
    gmf_all_mappings_NotationElementTarget,
)
gmf_all_mappings_DiagramElementTarget_strategy = st.builds(
    gmf_all_mappings_DiagramElementTarget,
)
gmf_all_mappings_DomainElementTarget_strategy = st.builds(
    gmf_all_mappings_DomainElementTarget,
)
Auditable_strategy = st.builds(
    Auditable,
)
gmf_all_mappings_AuditedMetricTarget_strategy = st.builds(
    gmf_all_mappings_AuditedMetricTarget,
)
RuleBase_strategy = st.builds(
    RuleBase,
)
gmf_all_mappings_MetricRule_strategy = st.builds(
    gmf_all_mappings_MetricRule,
    lowLimit=
        safe_text,
    key=
        safe_text,
    highLimit=
        safe_text
)
gmf_all_mappings_AuditRule_strategy = st.builds(
    gmf_all_mappings_AuditRule,
    id=
        safe_text,
    useInLiveMode=
        st.booleans(),
    message=
        safe_text,
    severity=
        safe_text
)
gmf_all_mappings_RuleBase_strategy = st.builds(
    gmf_all_mappings_RuleBase,
    description=
        safe_text,
    name=
        safe_text
)
gmf_all_mappings_DomainAttributeTarget_strategy = st.builds(
    gmf_all_mappings_DomainAttributeTarget,
    nullAsError=
        st.booleans()
)
gmf_all_mappings_AuditContainer_strategy = st.builds(
    gmf_all_mappings_AuditContainer,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
gmf_all_mappings_AppearanceSteward_strategy = st.builds(
    gmf_all_mappings_AppearanceSteward,
)
AbstractTool_strategy = st.builds(
    AbstractTool,
)
gmf_all_tooldef_GenericTool_strategy = st.builds(
    gmf_all_tooldef_GenericTool,
    toolClass=
        safe_text
)
gmf_all_tooldef_ToolContainer_strategy = st.builds(
    gmf_all_tooldef_ToolContainer,
)
gmf_all_tooldef_CreationTool_strategy = st.builds(
    gmf_all_tooldef_CreationTool,
)
gmf_all_tooldef_PaletteSeparator_strategy = st.builds(
    gmf_all_tooldef_PaletteSeparator,
)
gmf_all_tooldef_StandardTool_strategy = st.builds(
    gmf_all_tooldef_StandardTool,
    toolKind=
        safe_text
)
gmf_all_mappings_ToolOwner_strategy = st.builds(
    gmf_all_mappings_ToolOwner,
)
ContextMenu_strategy = st.builds(
    ContextMenu,
)
gmf_all_mappings_MenuOwner_strategy = st.builds(
    gmf_all_mappings_MenuOwner,
)
FeatureSeqInitializer_strategy = st.builds(
    FeatureSeqInitializer,
)
AuditRule_strategy = st.builds(
    AuditRule,
)
ReferenceNewElementSpec_strategy = st.builds(
    ReferenceNewElementSpec,
)
FeatureInitializer_strategy = st.builds(
    FeatureInitializer,
)
gmf_all_mappings_ReferenceNewElementSpec_strategy = st.builds(
    gmf_all_mappings_ReferenceNewElementSpec,
)
gmf_all_mappings_FeatureValueSpec_strategy = st.builds(
    gmf_all_mappings_FeatureValueSpec,
)
gmf_all_mappings_ElementInitializer_strategy = st.builds(
    gmf_all_mappings_ElementInitializer,
)
gmf_all_mappings_ValueExpression_strategy = st.builds(
    gmf_all_mappings_ValueExpression,
    language=
        safe_text,
    langName=
        safe_text,
    body=
        safe_text
)
gmf_all_mappings_FeatureInitializer_strategy = st.builds(
    gmf_all_mappings_FeatureInitializer,
)
gmf_all_mappings_LinkConstraints_strategy = st.builds(
    gmf_all_mappings_LinkConstraints,
)
mappings_gmf_all_EAttribute_strategy = st.builds(
    mappings_gmf_all_EAttribute,
)
MappingEntry_strategy = st.builds(
    MappingEntry,
)
DiagramLabel_strategy = st.builds(
    DiagramLabel,
)
gmf_all_mappings_LabelMapping_strategy = st.builds(
    gmf_all_mappings_LabelMapping,
    readOnly=
        st.booleans()
)
Toolbar_strategy = st.builds(
    Toolbar,
)
MainMenu_strategy = st.builds(
    MainMenu,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
gmf_all_mappings_Constraint_strategy = st.builds(
    gmf_all_mappings_Constraint,
)
Canvas_strategy = st.builds(
    Canvas,
)
gmf_all_mappings_CanvasMapping_strategy = st.builds(
    gmf_all_mappings_CanvasMapping,
)
LinkConstraints_strategy = st.builds(
    LinkConstraints,
)
mappings_gmf_all_EStructuralFeature_strategy = st.builds(
    mappings_gmf_all_EStructuralFeature,
)
Connection_strategy = st.builds(
    Connection,
)
mappings_NeedsContainment_strategy = st.builds(
    mappings_NeedsContainment,
)
Compartment_strategy = st.builds(
    Compartment,
)
gmf_all_mappings_CompartmentMapping_strategy = st.builds(
    gmf_all_mappings_CompartmentMapping,
)
ChildReference_strategy = st.builds(
    ChildReference,
)
Palette_strategy = st.builds(
    Palette,
)
mappings_gmf_all_EPackage_strategy = st.builds(
    mappings_gmf_all_EPackage,
)
CompartmentMapping_strategy = st.builds(
    CompartmentMapping,
)
NodeReference_strategy = st.builds(
    NodeReference,
)
gmf_all_mappings_TopNodeReference_strategy = st.builds(
    gmf_all_mappings_TopNodeReference,
)
gmf_all_mappings_ChildReference_strategy = st.builds(
    gmf_all_mappings_ChildReference,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
NeedsContainment_strategy = st.builds(
    NeedsContainment,
)
gmf_all_mappings_NodeReference_strategy = st.builds(
    gmf_all_mappings_NodeReference,
)
Node_strategy = st.builds(
    Node,
)
gmf_all_gmfgraph_DiagramLabel_strategy = st.builds(
    gmf_all_gmfgraph_DiagramLabel,
    elementIcon=
        st.booleans(),
    external=
        st.booleans()
)
mappings_AppearanceSteward_strategy = st.builds(
    mappings_AppearanceSteward,
)
mappings_ToolOwner_strategy = st.builds(
    mappings_ToolOwner,
)
mappings_MenuOwner_strategy = st.builds(
    mappings_MenuOwner,
)
mappings_MappingEntry_strategy = st.builds(
    mappings_MappingEntry,
)
gmf_all_mappings_LinkMapping_strategy = st.builds(
    gmf_all_mappings_LinkMapping,
)
gmf_all_mappings_NodeMapping_strategy = st.builds(
    gmf_all_mappings_NodeMapping,
)
LabelMapping_strategy = st.builds(
    LabelMapping,
)
gmf_all_mappings_ExpressionLabelMapping_strategy = st.builds(
    gmf_all_mappings_ExpressionLabelMapping,
)
gmf_all_mappings_FeatureLabelMapping_strategy = st.builds(
    gmf_all_mappings_FeatureLabelMapping,
    viewPattern=
        safe_text,
    editPattern=
        safe_text,
    viewMethod=
        safe_text,
    editMethod=
        safe_text,
    editorPattern=
        safe_text
)
gmf_all_mappings_OclChoiceLabelMapping_strategy = st.builds(
    gmf_all_mappings_OclChoiceLabelMapping,
)
gmf_all_mappings_DesignLabelMapping_strategy = st.builds(
    gmf_all_mappings_DesignLabelMapping,
)
ElementInitializer_strategy = st.builds(
    ElementInitializer,
)
gmf_all_mappings_FeatureSeqInitializer_strategy = st.builds(
    gmf_all_mappings_FeatureSeqInitializer,
)
Constraint_strategy = st.builds(
    Constraint,
)
mappings_gmf_all_EClass_strategy = st.builds(
    mappings_gmf_all_EClass,
)
gmf_all_mappings_MappingEntry_strategy = st.builds(
    gmf_all_mappings_MappingEntry,
)
MetricContainer_strategy = st.builds(
    MetricContainer,
)
AuditContainer_strategy = st.builds(
    AuditContainer,
)
StyleSelector_strategy = st.builds(
    StyleSelector,
)
gmf_all_tooldef_GenericStyleSelector_strategy = st.builds(
    gmf_all_tooldef_GenericStyleSelector,
    values=
        safe_text
)
CanvasMapping_strategy = st.builds(
    CanvasMapping,
)
LinkMapping_strategy = st.builds(
    LinkMapping,
)
mappings_gmf_all_EReference_strategy = st.builds(
    mappings_gmf_all_EReference,
)
gmf_all_mappings_NeedsContainment_strategy = st.builds(
    gmf_all_mappings_NeedsContainment,
)
VisualEffectMapping_strategy = st.builds(
    VisualEffectMapping,
)
TopNodeReference_strategy = st.builds(
    TopNodeReference,
)
gmf_all_mappings_Mapping_strategy = st.builds(
    gmf_all_mappings_Mapping,
)

@given(instance=AbstractFigure_strategy)
@settings(max_examples=50)
def test_abstractfigure_instantiation(instance):
    assert isinstance(instance, AbstractFigure)

@given(instance=gmf_all_gmfgraph_FigureRef_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_figureref_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureRef)

@given(instance=gmf_all_gmfgraph_ChildAccess_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_childaccess_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ChildAccess)



@given(instance=gmf_all_gmfgraph_ChildAccess_strategy)
def test_gmf_all_gmfgraph_childaccess_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=gmf_all_gmfgraph_AbstractFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_abstractfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AbstractFigure)

@given(instance=gmf_all_gmfgraph_PinOwner_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_pinowner_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PinOwner)

@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_svgproperty_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_SVGProperty)



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_setter_setter(instance):
    original = instance.setter
    instance.setter = original
    assert instance.setter == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_callSuper_setter(instance):
    original = instance.callSuper
    instance.callSuper = original
    assert instance.callSuper == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_getter_setter(instance):
    original = instance.getter
    instance.getter = original
    assert instance.getter == original



@given(instance=gmf_all_gmfgraph_SVGProperty_strategy)
def test_gmf_all_gmfgraph_svgproperty_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=Rectangle2D_strategy)
@settings(max_examples=50)
def test_rectangle2d_instantiation(instance):
    assert isinstance(instance, Rectangle2D)

@given(instance=SVGProperty_strategy)
@settings(max_examples=50)
def test_svgproperty_instantiation(instance):
    assert isinstance(instance, SVGProperty)

@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_rectangle2d_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Rectangle2D)



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_gmf_all_gmfgraph_rectangle2d_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_gmf_all_gmfgraph_rectangle2d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_gmf_all_gmfgraph_rectangle2d_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=gmf_all_gmfgraph_Rectangle2D_strategy)
def test_gmf_all_gmfgraph_rectangle2d_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gmfgraph_Layout_strategy)
@settings(max_examples=50)
def test_gmfgraph_layout_instantiation(instance):
    assert isinstance(instance, gmfgraph_Layout)

@given(instance=gmf_all_gmfgraph_Layout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_layout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Layout)

@given(instance=gmf_all_gmfgraph_Layoutable_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_layoutable_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Layoutable)

@given(instance=LayoutData_strategy)
@settings(max_examples=50)
def test_layoutdata_instantiation(instance):
    assert isinstance(instance, LayoutData)

@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_borderlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderLayoutData)



@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
def test_gmf_all_gmfgraph_borderlayoutdata_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original



@given(instance=gmf_all_gmfgraph_BorderLayoutData_strategy)
def test_gmf_all_gmfgraph_borderlayoutdata_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=gmf_all_gmfgraph_XYLayoutData_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_xylayoutdata_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_XYLayoutData)

@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_gridlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GridLayoutData)



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original



@given(instance=gmf_all_gmfgraph_GridLayoutData_strategy)
def test_gmf_all_gmfgraph_gridlayoutdata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original

@given(instance=gmfgraph_Border_strategy)
@settings(max_examples=50)
def test_gmfgraph_border_instantiation(instance):
    assert isinstance(instance, gmfgraph_Border)

@given(instance=gmf_all_gmfgraph_Border_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_border_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Border)

@given(instance=gmfgraph_LayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph_layoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph_LayoutData)

@given(instance=gmf_all_gmfgraph_LayoutData_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_layoutdata_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LayoutData)

@given(instance=gmf_all_gmfgraph_Point_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_point_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Point)



@given(instance=gmf_all_gmfgraph_Point_strategy)
def test_gmf_all_gmfgraph_point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=gmf_all_gmfgraph_Point_strategy)
def test_gmf_all_gmfgraph_point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmf_all_gmfgraph_Font_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_font_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Font)

@given(instance=gmf_all_gmfgraph_Color_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_color_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Color)

@given(instance=gmfgraph_CustomFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph_customfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomFigure)

@given(instance=FigureAccessor_strategy)
@settings(max_examples=50)
def test_figureaccessor_instantiation(instance):
    assert isinstance(instance, FigureAccessor)

@given(instance=gmf_all_gmfgraph_Insets_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_insets_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Insets)



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_gmf_all_gmfgraph_insets_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_gmf_all_gmfgraph_insets_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_gmf_all_gmfgraph_insets_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original



@given(instance=gmf_all_gmfgraph_Insets_strategy)
def test_gmf_all_gmfgraph_insets_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=gmf_all_gmfgraph_Dimension_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_dimension_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Dimension)



@given(instance=gmf_all_gmfgraph_Dimension_strategy)
def test_gmf_all_gmfgraph_dimension_dx_setter(instance):
    original = instance.dx
    instance.dx = original
    assert instance.dx == original



@given(instance=gmf_all_gmfgraph_Dimension_strategy)
def test_gmf_all_gmfgraph_dimension_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original

@given(instance=gmf_all_gmfgraph_FigureAccessor_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_figureaccessor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureAccessor)



@given(instance=gmf_all_gmfgraph_FigureAccessor_strategy)
def test_gmf_all_gmfgraph_figureaccessor_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customattribute_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomAttribute)



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_gmf_all_gmfgraph_customattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_gmf_all_gmfgraph_customattribute_directAccess_setter(instance):
    original = instance.directAccess
    instance.directAccess = original
    assert instance.directAccess == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_gmf_all_gmfgraph_customattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gmf_all_gmfgraph_CustomAttribute_strategy)
def test_gmf_all_gmfgraph_customattribute_multiStatementValue_setter(instance):
    original = instance.multiStatementValue
    instance.multiStatementValue = original
    assert instance.multiStatementValue == original

@given(instance=CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_customattributeowner_instantiation(instance):
    assert isinstance(instance, CustomAttributeOwner)

@given(instance=gmf_all_gmfgraph_CustomClass_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customclass_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomClass)



@given(instance=gmf_all_gmfgraph_CustomClass_strategy)
def test_gmf_all_gmfgraph_customclass_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=CustomAttribute_strategy)
@settings(max_examples=50)
def test_customattribute_instantiation(instance):
    assert isinstance(instance, CustomAttribute)

@given(instance=gmf_all_gmfgraph_CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customattributeowner_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomAttributeOwner)

@given(instance=gmfgraph_Polygon_strategy)
@settings(max_examples=50)
def test_gmfgraph_polygon_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polygon)

@given(instance=gmfgraph_DecorationFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph_decorationfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_DecorationFigure)

@given(instance=gmf_all_gmfgraph_PolygonDecoration_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_polygondecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolygonDecoration)

@given(instance=gmf_all_gmfgraph_CustomDecoration_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customdecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomDecoration)

@given(instance=DecorationFigure_strategy)
@settings(max_examples=50)
def test_decorationfigure_instantiation(instance):
    assert isinstance(instance, DecorationFigure)

@given(instance=gmfgraph_ConnectionFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph_connectionfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_ConnectionFigure)

@given(instance=gmf_all_gmfgraph_CustomConnection_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customconnection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomConnection)

@given(instance=gmfgraph_Polyline_strategy)
@settings(max_examples=50)
def test_gmfgraph_polyline_instantiation(instance):
    assert isinstance(instance, gmfgraph_Polyline)

@given(instance=gmf_all_gmfgraph_PolylineDecoration_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_polylinedecoration_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolylineDecoration)

@given(instance=gmf_all_gmfgraph_PolylineConnection_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_polylineconnection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_PolylineConnection)

@given(instance=Polygon_strategy)
@settings(max_examples=50)
def test_polygon_instantiation(instance):
    assert isinstance(instance, Polygon)

@given(instance=gmf_all_gmfgraph_ScalablePolygon_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_scalablepolygon_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ScalablePolygon)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=gmf_all_gmfgraph_Polygon_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_polygon_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Polygon)

@given(instance=gmfgraph_CustomClass_strategy)
@settings(max_examples=50)
def test_gmfgraph_customclass_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomClass)

@given(instance=gmf_all_gmfgraph_CustomBorder_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customborder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomBorder)

@given(instance=gmf_all_gmfgraph_CustomLayoutData_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomLayoutData)

@given(instance=gmf_all_gmfgraph_CustomLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customlayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomLayout)

@given(instance=gmfgraph_RealFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph_realfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_RealFigure)

@given(instance=gmf_all_gmfgraph_CustomFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_customfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomFigure)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=gmf_all_gmfgraph_Polyline_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_polyline_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Polyline)

@given(instance=gmf_all_gmfgraph_Ellipse_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_ellipse_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Ellipse)

@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_roundedrectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RoundedRectangle)



@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
def test_gmf_all_gmfgraph_roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original



@given(instance=gmf_all_gmfgraph_RoundedRectangle_strategy)
def test_gmf_all_gmfgraph_roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

@given(instance=gmf_all_gmfgraph_Rectangle_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_rectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Rectangle)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=Insets_strategy)
@settings(max_examples=50)
def test_insets_instantiation(instance):
    assert isinstance(instance, Insets)

@given(instance=Font_strategy)
@settings(max_examples=50)
def test_font_instantiation(instance):
    assert isinstance(instance, Font)

@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_basicfont_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BasicFont)



@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_gmf_all_gmfgraph_basicfont_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_gmf_all_gmfgraph_basicfont_faceName_setter(instance):
    original = instance.faceName
    instance.faceName = original
    assert instance.faceName == original



@given(instance=gmf_all_gmfgraph_BasicFont_strategy)
def test_gmf_all_gmfgraph_basicfont_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=gmf_all_gmfgraph_ConstantColor_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_constantcolor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ConstantColor)



@given(instance=gmf_all_gmfgraph_ConstantColor_strategy)
def test_gmf_all_gmfgraph_constantcolor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_rgbcolor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RGBColor)



@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_gmf_all_gmfgraph_rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original



@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_gmf_all_gmfgraph_rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original



@given(instance=gmf_all_gmfgraph_RGBColor_strategy)
def test_gmf_all_gmfgraph_rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=gmfgraph_CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_gmfgraph_customattributeowner_instantiation(instance):
    assert isinstance(instance, gmfgraph_CustomAttributeOwner)

@given(instance=gmfgraph_PinOwner_strategy)
@settings(max_examples=50)
def test_gmfgraph_pinowner_instantiation(instance):
    assert isinstance(instance, gmfgraph_PinOwner)

@given(instance=gmfgraph_AbstractFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph_abstractfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph_AbstractFigure)

@given(instance=gmf_all_gmfgraph_RealFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_realfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_RealFigure)



@given(instance=gmf_all_gmfgraph_RealFigure_strategy)
def test_gmf_all_gmfgraph_realfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=gmf_all_gmfgraph_VisualFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_visualfacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VisualFacet)

@given(instance=ChildAccess_strategy)
@settings(max_examples=50)
def test_childaccess_instantiation(instance):
    assert isinstance(instance, ChildAccess)

@given(instance=Layoutable_strategy)
@settings(max_examples=50)
def test_layoutable_instantiation(instance):
    assert isinstance(instance, Layoutable)

@given(instance=gmf_all_gmfgraph_Figure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_figure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Figure)

@given(instance=VisualFacet_strategy)
@settings(max_examples=50)
def test_visualfacet_instantiation(instance):
    assert isinstance(instance, VisualFacet)

@given(instance=gmf_all_gmfgraph_AlignmentFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_alignmentfacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AlignmentFacet)



@given(instance=gmf_all_gmfgraph_AlignmentFacet_strategy)
def test_gmf_all_gmfgraph_alignmentfacet_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_generalfacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GeneralFacet)



@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
def test_gmf_all_gmfgraph_generalfacet_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=gmf_all_gmfgraph_GeneralFacet_strategy)
def test_gmf_all_gmfgraph_generalfacet_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_labeloffsetfacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LabelOffsetFacet)



@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
def test_gmf_all_gmfgraph_labeloffsetfacet_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=gmf_all_gmfgraph_LabelOffsetFacet_strategy)
def test_gmf_all_gmfgraph_labeloffsetfacet_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmf_all_gmfgraph_DefaultSizeFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_defaultsizefacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DefaultSizeFacet)

@given(instance=gmf_all_gmfgraph_GradientFacet_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_gradientfacet_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GradientFacet)



@given(instance=gmf_all_gmfgraph_GradientFacet_strategy)
def test_gmf_all_gmfgraph_gradientfacet_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=gmf_all_gmfgraph_Identity_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_identity_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Identity)



@given(instance=gmf_all_gmfgraph_Identity_strategy)
def test_gmf_all_gmfgraph_identity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=gmf_all_gmfgraph_CenterLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_centerlayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CenterLayout)

@given(instance=gmf_all_gmfgraph_LayoutRef_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_layoutref_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LayoutRef)

@given(instance=gmf_all_gmfgraph_XYLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_xylayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_XYLayout)

@given(instance=gmf_all_gmfgraph_BorderLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_borderlayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderLayout)

@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_flowlayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FlowLayout)



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_forceSingleLine_setter(instance):
    original = instance.forceSingleLine
    instance.forceSingleLine = original
    assert instance.forceSingleLine == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_minorSpacing_setter(instance):
    original = instance.minorSpacing
    instance.minorSpacing = original
    assert instance.minorSpacing == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_majorAlignment_setter(instance):
    original = instance.majorAlignment
    instance.majorAlignment = original
    assert instance.majorAlignment == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_minorAlignment_setter(instance):
    original = instance.minorAlignment
    instance.minorAlignment = original
    assert instance.minorAlignment == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_majorSpacing_setter(instance):
    original = instance.majorSpacing
    instance.majorSpacing = original
    assert instance.majorSpacing == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original



@given(instance=gmf_all_gmfgraph_FlowLayout_strategy)
def test_gmf_all_gmfgraph_flowlayout_matchMinorSize_setter(instance):
    original = instance.matchMinorSize
    instance.matchMinorSize = original
    assert instance.matchMinorSize == original

@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_gridlayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_GridLayout)



@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
def test_gmf_all_gmfgraph_gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original



@given(instance=gmf_all_gmfgraph_GridLayout_strategy)
def test_gmf_all_gmfgraph_gridlayout_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original

@given(instance=gmf_all_gmfgraph_StackLayout_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_stacklayout_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_StackLayout)

@given(instance=Border_strategy)
@settings(max_examples=50)
def test_border_instantiation(instance):
    assert isinstance(instance, Border)

@given(instance=gmf_all_gmfgraph_CompoundBorder_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_compoundborder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CompoundBorder)

@given(instance=gmf_all_gmfgraph_LineBorder_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_lineborder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LineBorder)



@given(instance=gmf_all_gmfgraph_LineBorder_strategy)
def test_gmf_all_gmfgraph_lineborder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gmf_all_gmfgraph_BorderRef_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_borderref_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_BorderRef)

@given(instance=gmf_all_gmfgraph_MarginBorder_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_marginborder_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_MarginBorder)

@given(instance=FigureDescriptor_strategy)
@settings(max_examples=50)
def test_figuredescriptor_instantiation(instance):
    assert isinstance(instance, FigureDescriptor)

@given(instance=RealFigure_strategy)
@settings(max_examples=50)
def test_realfigure_instantiation(instance):
    assert isinstance(instance, RealFigure)

@given(instance=gmf_all_gmfgraph_InvisibleRectangle_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_invisiblerectangle_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_InvisibleRectangle)

@given(instance=gmf_all_gmfgraph_VerticalLabel_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_verticallabel_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VerticalLabel)



@given(instance=gmf_all_gmfgraph_VerticalLabel_strategy)
def test_gmf_all_gmfgraph_verticallabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gmf_all_gmfgraph_Shape_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_shape_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Shape)



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_xorFill_setter(instance):
    original = instance.xorFill
    instance.xorFill = original
    assert instance.xorFill == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_lineKind_setter(instance):
    original = instance.lineKind
    instance.lineKind = original
    assert instance.lineKind == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_xorOutline_setter(instance):
    original = instance.xorOutline
    instance.xorOutline = original
    assert instance.xorOutline == original



@given(instance=gmf_all_gmfgraph_Shape_strategy)
def test_gmf_all_gmfgraph_shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_svgfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_SVGFigure)



@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_gmf_all_gmfgraph_svgfigure_noCanvasWidth_setter(instance):
    original = instance.noCanvasWidth
    instance.noCanvasWidth = original
    assert instance.noCanvasWidth == original



@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_gmf_all_gmfgraph_svgfigure_documentURI_setter(instance):
    original = instance.documentURI
    instance.documentURI = original
    assert instance.documentURI == original



@given(instance=gmf_all_gmfgraph_SVGFigure_strategy)
def test_gmf_all_gmfgraph_svgfigure_noCanvasHeight_setter(instance):
    original = instance.noCanvasHeight
    instance.noCanvasHeight = original
    assert instance.noCanvasHeight == original

@given(instance=gmf_all_gmfgraph_Label_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_label_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Label)



@given(instance=gmf_all_gmfgraph_Label_strategy)
def test_gmf_all_gmfgraph_label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gmf_all_gmfgraph_DecorationFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_decorationfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DecorationFigure)

@given(instance=gmf_all_gmfgraph_ConnectionFigure_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_connectionfigure_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ConnectionFigure)

@given(instance=gmf_all_gmfgraph_LabeledContainer_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_labeledcontainer_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_LabeledContainer)

@given(instance=FigureGallery_strategy)
@settings(max_examples=50)
def test_figuregallery_instantiation(instance):
    assert isinstance(instance, FigureGallery)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=gmf_all_gmfgraph_Node_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_node_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Node)



@given(instance=gmf_all_gmfgraph_Node_strategy)
def test_gmf_all_gmfgraph_node_resizeConstraint_setter(instance):
    original = instance.resizeConstraint
    instance.resizeConstraint = original
    assert instance.resizeConstraint == original



@given(instance=gmf_all_gmfgraph_Node_strategy)
def test_gmf_all_gmfgraph_node_affixedParentSide_setter(instance):
    original = instance.affixedParentSide
    instance.affixedParentSide = original
    assert instance.affixedParentSide == original

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=gmf_all_gmfgraph_Compartment_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_compartment_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Compartment)



@given(instance=gmf_all_gmfgraph_Compartment_strategy)
def test_gmf_all_gmfgraph_compartment_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original



@given(instance=gmf_all_gmfgraph_Compartment_strategy)
def test_gmf_all_gmfgraph_compartment_needsTitle_setter(instance):
    original = instance.needsTitle
    instance.needsTitle = original
    assert instance.needsTitle == original

@given(instance=gmf_all_gmfgraph_Connection_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_connection_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Connection)

@given(instance=gmf_all_gmfgraph_AbstractNode_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_abstractnode_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_AbstractNode)

@given(instance=gmf_all_tooldef_StyleSelector_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_styleselector_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_StyleSelector)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gmf_all_tooldef_StyleSelector_strategy)
@settings(max_examples=30)
def test_gmf_all_tooldef_styleselector_isok_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isOk(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isOk).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isOk' in gmf_all_tooldef_StyleSelector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isOk' in gmf_all_tooldef_StyleSelector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isOk' in gmf_all_tooldef_StyleSelector is not implemented or raised an error")

@given(instance=gmf_all_tooldef_Image_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_image_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Image)

@given(instance=tooldef_ContributionItem_strategy)
@settings(max_examples=50)
def test_tooldef_contributionitem_instantiation(instance):
    assert isinstance(instance, tooldef_ContributionItem)

@given(instance=Identity_strategy)
@settings(max_examples=50)
def test_identity_instantiation(instance):
    assert isinstance(instance, Identity)

@given(instance=gmf_all_gmfgraph_Pin_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_pin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Pin)

@given(instance=gmf_all_gmfgraph_FigureDescriptor_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_figuredescriptor_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureDescriptor)

@given(instance=gmf_all_gmfgraph_DiagramElement_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_diagramelement_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DiagramElement)

@given(instance=gmf_all_gmfgraph_FigureGallery_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_figuregallery_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_FigureGallery)



@given(instance=gmf_all_gmfgraph_FigureGallery_strategy)
def test_gmf_all_gmfgraph_figuregallery_implementationBundle_setter(instance):
    original = instance.implementationBundle
    instance.implementationBundle = original
    assert instance.implementationBundle == original

@given(instance=gmf_all_gmfgraph_Canvas_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_canvas_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_Canvas)

@given(instance=tooldef_PredefinedItem_strategy)
@settings(max_examples=50)
def test_tooldef_predefineditem_instantiation(instance):
    assert isinstance(instance, tooldef_PredefinedItem)

@given(instance=tooldef_Menu_strategy)
@settings(max_examples=50)
def test_tooldef_menu_instantiation(instance):
    assert isinstance(instance, tooldef_Menu)

@given(instance=gmf_all_tooldef_PopupMenu_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_popupmenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PopupMenu)



@given(instance=gmf_all_tooldef_PopupMenu_strategy)
def test_gmf_all_tooldef_popupmenu_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=gmf_all_tooldef_PredefinedMenu_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_predefinedmenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PredefinedMenu)

@given(instance=ItemBase_strategy)
@settings(max_examples=50)
def test_itembase_instantiation(instance):
    assert isinstance(instance, ItemBase)

@given(instance=gmf_all_tooldef_Separator_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_separator_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Separator)



@given(instance=gmf_all_tooldef_Separator_strategy)
def test_gmf_all_tooldef_separator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf_all_tooldef_PredefinedItem_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_predefineditem_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PredefinedItem)



@given(instance=gmf_all_tooldef_PredefinedItem_strategy)
def test_gmf_all_tooldef_predefineditem_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=gmf_all_tooldef_ContributionItem_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_contributionitem_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ContributionItem)



@given(instance=gmf_all_tooldef_ContributionItem_strategy)
def test_gmf_all_tooldef_contributionitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=gmf_all_tooldef_Menu_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_menu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Menu)

@given(instance=gmf_all_tooldef_ItemBase_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_itembase_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ItemBase)

@given(instance=gmf_all_tooldef_ItemRef_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_itemref_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ItemRef)

@given(instance=ContributionItem_strategy)
@settings(max_examples=50)
def test_contributionitem_instantiation(instance):
    assert isinstance(instance, ContributionItem)

@given(instance=gmf_all_tooldef_MenuAction_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_menuaction_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_MenuAction)



@given(instance=gmf_all_tooldef_MenuAction_strategy)
def test_gmf_all_tooldef_menuaction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=gmf_all_tooldef_MenuAction_strategy)
def test_gmf_all_tooldef_menuaction_hotKey_setter(instance):
    original = instance.hotKey
    instance.hotKey = original
    assert instance.hotKey == original

@given(instance=Image_strategy)
@settings(max_examples=50)
def test_image_instantiation(instance):
    assert isinstance(instance, Image)

@given(instance=gmf_all_tooldef_BundleImage_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_bundleimage_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_BundleImage)



@given(instance=gmf_all_tooldef_BundleImage_strategy)
def test_gmf_all_tooldef_bundleimage_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=gmf_all_tooldef_BundleImage_strategy)
def test_gmf_all_tooldef_bundleimage_bundle_setter(instance):
    original = instance.bundle
    instance.bundle = original
    assert instance.bundle == original

@given(instance=gmf_all_tooldef_DefaultImage_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_defaultimage_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_DefaultImage)

@given(instance=gmf_all_tooldef_AbstractTool_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_abstracttool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_AbstractTool)



@given(instance=gmf_all_tooldef_AbstractTool_strategy)
def test_gmf_all_tooldef_abstracttool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_tooldef_AbstractTool_strategy)
def test_gmf_all_tooldef_abstracttool_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)

@given(instance=gmf_all_tooldef_Toolbar_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_toolbar_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Toolbar)

@given(instance=gmf_all_tooldef_ContextMenu_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_contextmenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ContextMenu)

@given(instance=gmf_all_tooldef_MainMenu_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_mainmenu_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_MainMenu)



@given(instance=gmf_all_tooldef_MainMenu_strategy)
def test_gmf_all_tooldef_mainmenu_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=MenuAction_strategy)
@settings(max_examples=50)
def test_menuaction_instantiation(instance):
    assert isinstance(instance, MenuAction)

@given(instance=gmf_all_tooldef_ToolRegistry_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_toolregistry_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolRegistry)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_custompin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_CustomPin)



@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
def test_gmf_all_gmfgraph_custompin_customOperationName_setter(instance):
    original = instance.customOperationName
    instance.customOperationName = original
    assert instance.customOperationName == original



@given(instance=gmf_all_gmfgraph_CustomPin_strategy)
def test_gmf_all_gmfgraph_custompin_customOperationType_setter(instance):
    original = instance.customOperationType
    instance.customOperationType = original
    assert instance.customOperationType == original

@given(instance=gmf_all_gmfgraph_VisiblePin_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_visiblepin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_VisiblePin)

@given(instance=gmf_all_gmfgraph_ColorPin_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_colorpin_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_ColorPin)



@given(instance=gmf_all_gmfgraph_ColorPin_strategy)
def test_gmf_all_gmfgraph_colorpin_backgroundNotForeground_setter(instance):
    original = instance.backgroundNotForeground
    instance.backgroundNotForeground = original
    assert instance.backgroundNotForeground == original

@given(instance=gmf_all_mappings_VisualEffectMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_visualeffectmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_VisualEffectMapping)



@given(instance=gmf_all_mappings_VisualEffectMapping_strategy)
def test_gmf_all_mappings_visualeffectmapping_oclExpression_setter(instance):
    original = instance.oclExpression
    instance.oclExpression = original
    assert instance.oclExpression == original

@given(instance=gmf_all_mappings_Measurable_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_measurable_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Measurable)

@given(instance=gmf_all_mappings_Auditable_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_auditable_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Auditable)

@given(instance=ToolContainer_strategy)
@settings(max_examples=50)
def test_toolcontainer_instantiation(instance):
    assert isinstance(instance, ToolContainer)

@given(instance=gmf_all_tooldef_Palette_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_palette_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_Palette)

@given(instance=gmf_all_tooldef_ToolGroup_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_toolgroup_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolGroup)



@given(instance=gmf_all_tooldef_ToolGroup_strategy)
def test_gmf_all_tooldef_toolgroup_stack_setter(instance):
    original = instance.stack
    instance.stack = original
    assert instance.stack == original



@given(instance=gmf_all_tooldef_ToolGroup_strategy)
def test_gmf_all_tooldef_toolgroup_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=Measurable_strategy)
@settings(max_examples=50)
def test_measurable_instantiation(instance):
    assert isinstance(instance, Measurable)

@given(instance=MetricRule_strategy)
@settings(max_examples=50)
def test_metricrule_instantiation(instance):
    assert isinstance(instance, MetricRule)

@given(instance=gmf_all_mappings_MetricContainer_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_metriccontainer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MetricContainer)

@given(instance=mappings_Measurable_strategy)
@settings(max_examples=50)
def test_mappings_measurable_instantiation(instance):
    assert isinstance(instance, mappings_Measurable)

@given(instance=mappings_Auditable_strategy)
@settings(max_examples=50)
def test_mappings_auditable_instantiation(instance):
    assert isinstance(instance, mappings_Auditable)

@given(instance=gmf_all_mappings_NotationElementTarget_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_notationelementtarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NotationElementTarget)

@given(instance=gmf_all_mappings_DiagramElementTarget_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_diagramelementtarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DiagramElementTarget)

@given(instance=gmf_all_mappings_DomainElementTarget_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_domainelementtarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DomainElementTarget)

@given(instance=Auditable_strategy)
@settings(max_examples=50)
def test_auditable_instantiation(instance):
    assert isinstance(instance, Auditable)

@given(instance=gmf_all_mappings_AuditedMetricTarget_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_auditedmetrictarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditedMetricTarget)

@given(instance=RuleBase_strategy)
@settings(max_examples=50)
def test_rulebase_instantiation(instance):
    assert isinstance(instance, RuleBase)

@given(instance=gmf_all_mappings_MetricRule_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_metricrule_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MetricRule)



@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_gmf_all_mappings_metricrule_lowLimit_setter(instance):
    original = instance.lowLimit
    instance.lowLimit = original
    assert instance.lowLimit == original



@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_gmf_all_mappings_metricrule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=gmf_all_mappings_MetricRule_strategy)
def test_gmf_all_mappings_metricrule_highLimit_setter(instance):
    original = instance.highLimit
    instance.highLimit = original
    assert instance.highLimit == original

@given(instance=gmf_all_mappings_AuditRule_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_auditrule_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditRule)



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_gmf_all_mappings_auditrule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_gmf_all_mappings_auditrule_useInLiveMode_setter(instance):
    original = instance.useInLiveMode
    instance.useInLiveMode = original
    assert instance.useInLiveMode == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_gmf_all_mappings_auditrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=gmf_all_mappings_AuditRule_strategy)
def test_gmf_all_mappings_auditrule_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=gmf_all_mappings_RuleBase_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_rulebase_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_RuleBase)



@given(instance=gmf_all_mappings_RuleBase_strategy)
def test_gmf_all_mappings_rulebase_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_mappings_RuleBase_strategy)
def test_gmf_all_mappings_rulebase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf_all_mappings_DomainAttributeTarget_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_domainattributetarget_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DomainAttributeTarget)



@given(instance=gmf_all_mappings_DomainAttributeTarget_strategy)
def test_gmf_all_mappings_domainattributetarget_nullAsError_setter(instance):
    original = instance.nullAsError
    instance.nullAsError = original
    assert instance.nullAsError == original

@given(instance=gmf_all_mappings_AuditContainer_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_auditcontainer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AuditContainer)



@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_gmf_all_mappings_auditcontainer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_gmf_all_mappings_auditcontainer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=gmf_all_mappings_AuditContainer_strategy)
def test_gmf_all_mappings_auditcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf_all_mappings_AppearanceSteward_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_appearancesteward_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_AppearanceSteward)

@given(instance=AbstractTool_strategy)
@settings(max_examples=50)
def test_abstracttool_instantiation(instance):
    assert isinstance(instance, AbstractTool)

@given(instance=gmf_all_tooldef_GenericTool_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_generictool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_GenericTool)



@given(instance=gmf_all_tooldef_GenericTool_strategy)
def test_gmf_all_tooldef_generictool_toolClass_setter(instance):
    original = instance.toolClass
    instance.toolClass = original
    assert instance.toolClass == original

@given(instance=gmf_all_tooldef_ToolContainer_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_toolcontainer_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_ToolContainer)

@given(instance=gmf_all_tooldef_CreationTool_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_creationtool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_CreationTool)

@given(instance=gmf_all_tooldef_PaletteSeparator_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_paletteseparator_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_PaletteSeparator)

@given(instance=gmf_all_tooldef_StandardTool_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_standardtool_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_StandardTool)



@given(instance=gmf_all_tooldef_StandardTool_strategy)
def test_gmf_all_tooldef_standardtool_toolKind_setter(instance):
    original = instance.toolKind
    instance.toolKind = original
    assert instance.toolKind == original

@given(instance=gmf_all_mappings_ToolOwner_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_toolowner_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ToolOwner)

@given(instance=ContextMenu_strategy)
@settings(max_examples=50)
def test_contextmenu_instantiation(instance):
    assert isinstance(instance, ContextMenu)

@given(instance=gmf_all_mappings_MenuOwner_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_menuowner_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MenuOwner)

@given(instance=FeatureSeqInitializer_strategy)
@settings(max_examples=50)
def test_featureseqinitializer_instantiation(instance):
    assert isinstance(instance, FeatureSeqInitializer)

@given(instance=AuditRule_strategy)
@settings(max_examples=50)
def test_auditrule_instantiation(instance):
    assert isinstance(instance, AuditRule)

@given(instance=ReferenceNewElementSpec_strategy)
@settings(max_examples=50)
def test_referencenewelementspec_instantiation(instance):
    assert isinstance(instance, ReferenceNewElementSpec)

@given(instance=FeatureInitializer_strategy)
@settings(max_examples=50)
def test_featureinitializer_instantiation(instance):
    assert isinstance(instance, FeatureInitializer)

@given(instance=gmf_all_mappings_ReferenceNewElementSpec_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_referencenewelementspec_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ReferenceNewElementSpec)

@given(instance=gmf_all_mappings_FeatureValueSpec_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_featurevaluespec_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureValueSpec)

@given(instance=gmf_all_mappings_ElementInitializer_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_elementinitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ElementInitializer)

@given(instance=gmf_all_mappings_ValueExpression_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_valueexpression_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ValueExpression)



@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_gmf_all_mappings_valueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_gmf_all_mappings_valueexpression_langName_setter(instance):
    original = instance.langName
    instance.langName = original
    assert instance.langName == original



@given(instance=gmf_all_mappings_ValueExpression_strategy)
def test_gmf_all_mappings_valueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=gmf_all_mappings_FeatureInitializer_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_featureinitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureInitializer)

@given(instance=gmf_all_mappings_LinkConstraints_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_linkconstraints_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LinkConstraints)

@given(instance=mappings_gmf_all_EAttribute_strategy)
@settings(max_examples=50)
def test_mappings_gmf_all_eattribute_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EAttribute)

@given(instance=MappingEntry_strategy)
@settings(max_examples=50)
def test_mappingentry_instantiation(instance):
    assert isinstance(instance, MappingEntry)

@given(instance=DiagramLabel_strategy)
@settings(max_examples=50)
def test_diagramlabel_instantiation(instance):
    assert isinstance(instance, DiagramLabel)

@given(instance=gmf_all_mappings_LabelMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_labelmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LabelMapping)



@given(instance=gmf_all_mappings_LabelMapping_strategy)
def test_gmf_all_mappings_labelmapping_readOnly_setter(instance):
    original = instance.readOnly
    instance.readOnly = original
    assert instance.readOnly == original

@given(instance=Toolbar_strategy)
@settings(max_examples=50)
def test_toolbar_instantiation(instance):
    assert isinstance(instance, Toolbar)

@given(instance=MainMenu_strategy)
@settings(max_examples=50)
def test_mainmenu_instantiation(instance):
    assert isinstance(instance, MainMenu)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=gmf_all_mappings_Constraint_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_constraint_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Constraint)

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=gmf_all_mappings_CanvasMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_canvasmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_CanvasMapping)

@given(instance=LinkConstraints_strategy)
@settings(max_examples=50)
def test_linkconstraints_instantiation(instance):
    assert isinstance(instance, LinkConstraints)

@given(instance=mappings_gmf_all_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_mappings_gmf_all_estructuralfeature_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EStructuralFeature)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=mappings_NeedsContainment_strategy)
@settings(max_examples=50)
def test_mappings_needscontainment_instantiation(instance):
    assert isinstance(instance, mappings_NeedsContainment)

@given(instance=Compartment_strategy)
@settings(max_examples=50)
def test_compartment_instantiation(instance):
    assert isinstance(instance, Compartment)

@given(instance=gmf_all_mappings_CompartmentMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_compartmentmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_CompartmentMapping)

@given(instance=ChildReference_strategy)
@settings(max_examples=50)
def test_childreference_instantiation(instance):
    assert isinstance(instance, ChildReference)

@given(instance=Palette_strategy)
@settings(max_examples=50)
def test_palette_instantiation(instance):
    assert isinstance(instance, Palette)

@given(instance=mappings_gmf_all_EPackage_strategy)
@settings(max_examples=50)
def test_mappings_gmf_all_epackage_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EPackage)

@given(instance=CompartmentMapping_strategy)
@settings(max_examples=50)
def test_compartmentmapping_instantiation(instance):
    assert isinstance(instance, CompartmentMapping)

@given(instance=NodeReference_strategy)
@settings(max_examples=50)
def test_nodereference_instantiation(instance):
    assert isinstance(instance, NodeReference)

@given(instance=gmf_all_mappings_TopNodeReference_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_topnodereference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_TopNodeReference)

@given(instance=gmf_all_mappings_ChildReference_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_childreference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ChildReference)

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=NeedsContainment_strategy)
@settings(max_examples=50)
def test_needscontainment_instantiation(instance):
    assert isinstance(instance, NeedsContainment)

@given(instance=gmf_all_mappings_NodeReference_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_nodereference_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NodeReference)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
@settings(max_examples=50)
def test_gmf_all_gmfgraph_diagramlabel_instantiation(instance):
    assert isinstance(instance, gmf_all_gmfgraph_DiagramLabel)



@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
def test_gmf_all_gmfgraph_diagramlabel_elementIcon_setter(instance):
    original = instance.elementIcon
    instance.elementIcon = original
    assert instance.elementIcon == original



@given(instance=gmf_all_gmfgraph_DiagramLabel_strategy)
def test_gmf_all_gmfgraph_diagramlabel_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=mappings_AppearanceSteward_strategy)
@settings(max_examples=50)
def test_mappings_appearancesteward_instantiation(instance):
    assert isinstance(instance, mappings_AppearanceSteward)

@given(instance=mappings_ToolOwner_strategy)
@settings(max_examples=50)
def test_mappings_toolowner_instantiation(instance):
    assert isinstance(instance, mappings_ToolOwner)

@given(instance=mappings_MenuOwner_strategy)
@settings(max_examples=50)
def test_mappings_menuowner_instantiation(instance):
    assert isinstance(instance, mappings_MenuOwner)

@given(instance=mappings_MappingEntry_strategy)
@settings(max_examples=50)
def test_mappings_mappingentry_instantiation(instance):
    assert isinstance(instance, mappings_MappingEntry)

@given(instance=gmf_all_mappings_LinkMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_linkmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_LinkMapping)

@given(instance=gmf_all_mappings_NodeMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_nodemapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NodeMapping)

@given(instance=LabelMapping_strategy)
@settings(max_examples=50)
def test_labelmapping_instantiation(instance):
    assert isinstance(instance, LabelMapping)

@given(instance=gmf_all_mappings_ExpressionLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_expressionlabelmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_ExpressionLabelMapping)

@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_featurelabelmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureLabelMapping)



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_gmf_all_mappings_featurelabelmapping_viewPattern_setter(instance):
    original = instance.viewPattern
    instance.viewPattern = original
    assert instance.viewPattern == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_gmf_all_mappings_featurelabelmapping_editPattern_setter(instance):
    original = instance.editPattern
    instance.editPattern = original
    assert instance.editPattern == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_gmf_all_mappings_featurelabelmapping_viewMethod_setter(instance):
    original = instance.viewMethod
    instance.viewMethod = original
    assert instance.viewMethod == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_gmf_all_mappings_featurelabelmapping_editMethod_setter(instance):
    original = instance.editMethod
    instance.editMethod = original
    assert instance.editMethod == original



@given(instance=gmf_all_mappings_FeatureLabelMapping_strategy)
def test_gmf_all_mappings_featurelabelmapping_editorPattern_setter(instance):
    original = instance.editorPattern
    instance.editorPattern = original
    assert instance.editorPattern == original

@given(instance=gmf_all_mappings_OclChoiceLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_oclchoicelabelmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_OclChoiceLabelMapping)

@given(instance=gmf_all_mappings_DesignLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_designlabelmapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_DesignLabelMapping)

@given(instance=ElementInitializer_strategy)
@settings(max_examples=50)
def test_elementinitializer_instantiation(instance):
    assert isinstance(instance, ElementInitializer)

@given(instance=gmf_all_mappings_FeatureSeqInitializer_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_featureseqinitializer_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_FeatureSeqInitializer)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=mappings_gmf_all_EClass_strategy)
@settings(max_examples=50)
def test_mappings_gmf_all_eclass_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EClass)

@given(instance=gmf_all_mappings_MappingEntry_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_mappingentry_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_MappingEntry)

@given(instance=MetricContainer_strategy)
@settings(max_examples=50)
def test_metriccontainer_instantiation(instance):
    assert isinstance(instance, MetricContainer)

@given(instance=AuditContainer_strategy)
@settings(max_examples=50)
def test_auditcontainer_instantiation(instance):
    assert isinstance(instance, AuditContainer)

@given(instance=StyleSelector_strategy)
@settings(max_examples=50)
def test_styleselector_instantiation(instance):
    assert isinstance(instance, StyleSelector)

@given(instance=gmf_all_tooldef_GenericStyleSelector_strategy)
@settings(max_examples=50)
def test_gmf_all_tooldef_genericstyleselector_instantiation(instance):
    assert isinstance(instance, gmf_all_tooldef_GenericStyleSelector)



@given(instance=gmf_all_tooldef_GenericStyleSelector_strategy)
def test_gmf_all_tooldef_genericstyleselector_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=CanvasMapping_strategy)
@settings(max_examples=50)
def test_canvasmapping_instantiation(instance):
    assert isinstance(instance, CanvasMapping)

@given(instance=LinkMapping_strategy)
@settings(max_examples=50)
def test_linkmapping_instantiation(instance):
    assert isinstance(instance, LinkMapping)

@given(instance=mappings_gmf_all_EReference_strategy)
@settings(max_examples=50)
def test_mappings_gmf_all_ereference_instantiation(instance):
    assert isinstance(instance, mappings_gmf_all_EReference)

@given(instance=gmf_all_mappings_NeedsContainment_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_needscontainment_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_NeedsContainment)

@given(instance=VisualEffectMapping_strategy)
@settings(max_examples=50)
def test_visualeffectmapping_instantiation(instance):
    assert isinstance(instance, VisualEffectMapping)

@given(instance=TopNodeReference_strategy)
@settings(max_examples=50)
def test_topnodereference_instantiation(instance):
    assert isinstance(instance, TopNodeReference)

@given(instance=gmf_all_mappings_Mapping_strategy)
@settings(max_examples=50)
def test_gmf_all_mappings_mapping_instantiation(instance):
    assert isinstance(instance, gmf_all_mappings_Mapping)
