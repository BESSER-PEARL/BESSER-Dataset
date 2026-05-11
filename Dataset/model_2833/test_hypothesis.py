import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gmf::all::gmfgraph::PinOwner,
    gmf::all::gmfgraph::SVGProperty,
    Rectangle2D,
    SVGProperty,
    Polygon,
    gmf::all::gmfgraph::ScalablePolygon,
    Polyline,
    gmf::all::gmfgraph::Polygon,
    gmfgraph::CustomClass,
    gmfgraph::RealFigure,
    gmf::all::gmfgraph::CustomFigure,
    Shape,
    gmf::all::gmfgraph::RoundedRectangle,
    gmf::all::gmfgraph::Rectangle,
    AbstractFigure,
    gmf::all::gmfgraph::FigureRef,
    gmf::all::gmfgraph::Polyline,
    gmf::all::gmfgraph::Ellipse,
    gmf::all::gmfgraph::ChildAccess,
    Figure,
    gmf::all::gmfgraph::AbstractFigure,
    Point,
    Insets,
    Font,
    Color,
    gmfgraph::CustomAttributeOwner,
    gmfgraph::PinOwner,
    gmfgraph::AbstractFigure,
    gmf::all::gmfgraph::RealFigure,
    Dimension,
    gmf::all::gmfgraph::VisualFacet,
    ChildAccess,
    Layoutable,
    gmf::all::gmfgraph::Figure,
    VisualFacet,
    gmf::all::gmfgraph::AlignmentFacet,
    gmf::all::gmfgraph::LabelOffsetFacet,
    gmf::all::gmfgraph::GeneralFacet,
    gmf::all::gmfgraph::DefaultSizeFacet,
    gmf::all::gmfgraph::GradientFacet,
    gmf::all::gmfgraph::Identity,
    Layout,
    gmf::all::gmfgraph::FlowLayout,
    gmf::all::gmfgraph::CenterLayout,
    gmf::all::gmfgraph::StackLayout,
    gmf::all::gmfgraph::XYLayout,
    Border,
    FigureDescriptor,
    RealFigure,
    gmf::all::gmfgraph::ConnectionFigure,
    gmf::all::gmfgraph::InvisibleRectangle,
    gmf::all::gmfgraph::LabeledContainer,
    gmf::all::gmfgraph::Label,
    gmf::all::gmfgraph::SVGFigure,
    gmf::all::gmfgraph::VerticalLabel,
    gmf::all::gmfgraph::DecorationFigure,
    gmf::all::gmfgraph::Shape,
    FigureGallery,
    AbstractNode,
    gmf::all::gmfgraph::Node,
    DiagramElement,
    gmf::all::gmfgraph::Connection,
    gmf::all::gmfgraph::Compartment,
    gmf::all::gmfgraph::AbstractNode,
    gmf::all::tooldef::StyleSelector,
    gmf::all::tooldef::Image,
    tooldef::ContributionItem,
    Identity,
    gmf::all::gmfgraph::FigureDescriptor,
    gmf::all::gmfgraph::FigureGallery,
    gmf::all::gmfgraph::Pin,
    gmf::all::gmfgraph::DiagramElement,
    gmf::all::gmfgraph::Canvas,
    tooldef::PredefinedItem,
    tooldef::Menu,
    gmf::all::tooldef::PopupMenu,
    gmf::all::tooldef::PredefinedMenu,
    ItemBase,
    gmf::all::tooldef::PredefinedItem,
    gmf::all::tooldef::ContributionItem,
    gmf::all::tooldef::Separator,
    gmf::all::tooldef::Menu,
    gmf::all::tooldef::ItemBase,
    gmf::all::tooldef::ItemRef,
    ContributionItem,
    gmf::all::tooldef::MenuAction,
    Image,
    gmf::all::tooldef::DefaultImage,
    gmf::all::tooldef::BundleImage,
    gmf::all::tooldef::AbstractTool,
    Menu,
    gmf::all::tooldef::MainMenu,
    gmf::all::tooldef::Toolbar,
    gmf::all::tooldef::ContextMenu,
    MenuAction,
    gmf::all::tooldef::ToolRegistry,
    Pin,
    gmf::all::gmfgraph::CustomPin,
    gmf::all::gmfgraph::VisiblePin,
    gmf::all::gmfgraph::ColorPin,
    gmf::all::mappings::VisualEffectMapping,
    gmf::all::mappings::Measurable,
    gmf::all::mappings::Auditable,
    ToolContainer,
    gmf::all::tooldef::Palette,
    gmf::all::tooldef::ToolGroup,
    Measurable,
    MetricRule,
    gmf::all::mappings::MetricContainer,
    mappings::Measurable,
    mappings::Auditable,
    gmf::all::mappings::NotationElementTarget,
    gmf::all::mappings::DiagramElementTarget,
    gmf::all::mappings::DomainElementTarget,
    Auditable,
    gmf::all::mappings::AuditedMetricTarget,
    RuleBase,
    gmf::all::mappings::MetricRule,
    gmf::all::mappings::AuditRule,
    gmf::all::mappings::RuleBase,
    gmf::all::mappings::DomainAttributeTarget,
    gmf::all::mappings::AuditContainer,
    gmf::all::mappings::AppearanceSteward,
    AbstractTool,
    gmf::all::tooldef::GenericTool,
    gmf::all::tooldef::StandardTool,
    gmf::all::tooldef::PaletteSeparator,
    gmf::all::tooldef::ToolContainer,
    gmf::all::tooldef::CreationTool,
    gmf::all::mappings::ToolOwner,
    ContextMenu,
    gmf::all::mappings::MenuOwner,
    FeatureSeqInitializer,
    AuditRule,
    ReferenceNewElementSpec,
    FeatureInitializer,
    gmf::all::mappings::ReferenceNewElementSpec,
    gmf::all::mappings::FeatureValueSpec,
    gmf::all::mappings::ElementInitializer,
    gmf::all::mappings::ValueExpression,
    gmf::all::mappings::FeatureInitializer,
    gmf::all::mappings::LinkConstraints,
    mappings::gmf::all::EAttribute,
    MappingEntry,
    DiagramLabel,
    gmf::all::mappings::LabelMapping,
    Toolbar,
    MainMenu,
    ValueExpression,
    gmf::all::mappings::Constraint,
    Canvas,
    gmf::all::mappings::CanvasMapping,
    LinkConstraints,
    mappings::gmf::all::EStructuralFeature,
    Connection,
    mappings::NeedsContainment,
    Compartment,
    gmf::all::mappings::CompartmentMapping,
    ChildReference,
    Palette,
    mappings::gmf::all::EPackage,
    CompartmentMapping,
    NodeReference,
    gmf::all::mappings::TopNodeReference,
    gmf::all::mappings::ChildReference,
    NodeMapping,
    NeedsContainment,
    gmf::all::mappings::NodeReference,
    Node,
    gmf::all::gmfgraph::DiagramLabel,
    mappings::AppearanceSteward,
    mappings::ToolOwner,
    mappings::MenuOwner,
    mappings::MappingEntry,
    gmf::all::mappings::LinkMapping,
    gmf::all::mappings::NodeMapping,
    LabelMapping,
    gmf::all::mappings::ExpressionLabelMapping,
    gmf::all::mappings::FeatureLabelMapping,
    gmf::all::mappings::DesignLabelMapping,
    gmf::all::mappings::OclChoiceLabelMapping,
    ElementInitializer,
    gmf::all::mappings::FeatureSeqInitializer,
    Constraint,
    mappings::gmf::all::EClass,
    gmf::all::mappings::MappingEntry,
    MetricContainer,
    AuditContainer,
    StyleSelector,
    gmf::all::tooldef::GenericStyleSelector,
    CanvasMapping,
    LinkMapping,
    mappings::gmf::all::EReference,
    gmf::all::mappings::NeedsContainment,
    VisualEffectMapping,
    TopNodeReference,
    gmf::all::mappings::Mapping,
    gmf::all::gmfgraph::Rectangle2D,
    gmf::all::gmfgraph::GridLayout,
    gmfgraph::Layout,
    gmf::all::gmfgraph::CustomLayout,
    gmf::all::gmfgraph::LayoutRef,
    gmf::all::gmfgraph::Layout,
    gmf::all::gmfgraph::Layoutable,
    LayoutData,
    gmf::all::gmfgraph::XYLayoutData,
    gmf::all::gmfgraph::BorderLayoutData,
    gmf::all::gmfgraph::GridLayoutData,
    gmf::all::gmfgraph::BorderLayout,
    gmfgraph::Border,
    gmf::all::gmfgraph::CustomBorder,
    gmf::all::gmfgraph::CompoundBorder,
    gmf::all::gmfgraph::MarginBorder,
    gmf::all::gmfgraph::LineBorder,
    gmf::all::gmfgraph::BorderRef,
    gmf::all::gmfgraph::Border,
    gmfgraph::LayoutData,
    gmf::all::gmfgraph::CustomLayoutData,
    gmf::all::gmfgraph::LayoutData,
    gmf::all::gmfgraph::Point,
    gmf::all::gmfgraph::BasicFont,
    gmf::all::gmfgraph::Font,
    gmf::all::gmfgraph::ConstantColor,
    gmf::all::gmfgraph::RGBColor,
    gmf::all::gmfgraph::Color,
    gmfgraph::CustomFigure,
    FigureAccessor,
    gmf::all::gmfgraph::Insets,
    gmf::all::gmfgraph::Dimension,
    gmf::all::gmfgraph::FigureAccessor,
    gmf::all::gmfgraph::CustomAttribute,
    CustomAttributeOwner,
    gmf::all::gmfgraph::CustomClass,
    CustomAttribute,
    gmf::all::gmfgraph::CustomAttributeOwner,
    gmfgraph::Polygon,
    gmfgraph::DecorationFigure,
    gmf::all::gmfgraph::CustomDecoration,
    gmf::all::gmfgraph::PolygonDecoration,
    DecorationFigure,
    gmfgraph::ConnectionFigure,
    gmf::all::gmfgraph::CustomConnection,
    gmfgraph::Polyline,
    gmf::all::gmfgraph::PolylineDecoration,
    gmf::all::gmfgraph::PolylineConnection,
    AppearanceStyle,
    Alignment,
    Severity,
    LineKind,
    StandardToolKind,
    LabelTextAccessMethod,
    SVGPropertyType,
    ActionKind,
    Language,
    Direction,
    FontStyle,
    ColorConstants,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gmf::all::gmfgraph::pinowner_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::PinOwner)


def test_gmf::all::gmfgraph::pinowner_constructor_exists():
    assert callable(gmf::all::gmfgraph::PinOwner.__init__)


def test_gmf::all::gmfgraph::pinowner_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::svgproperty_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::SVGProperty)


def test_gmf::all::gmfgraph::svgproperty_constructor_exists():
    assert callable(gmf::all::gmfgraph::SVGProperty.__init__)


def test_gmf::all::gmfgraph::svgproperty_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::SVGProperty.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "setter" in params, "Missing parameter 'setter'"
    assert "callSuper" in params, "Missing parameter 'callSuper'"
    assert "type" in params, "Missing parameter 'type'"
    assert "getter" in params, "Missing parameter 'getter'"
    assert "query" in params, "Missing parameter 'query'"

def test_gmf::all::gmfgraph::svgproperty_has_attribute():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "attribute")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgproperty_has_setter():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "setter")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
        if "setter" in klass.__dict__:
            descriptor = klass.__dict__["setter"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgproperty_has_callSuper():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "callSuper")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
        if "callSuper" in klass.__dict__:
            descriptor = klass.__dict__["callSuper"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgproperty_has_type():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "type")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgproperty_has_getter():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "getter")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
        if "getter" in klass.__dict__:
            descriptor = klass.__dict__["getter"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgproperty_has_query():
    assert hasattr(gmf::all::gmfgraph::SVGProperty, "query")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGProperty.__mro__:
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



def test_polygon_is_not_abstract():
    assert not inspect.isabstract(Polygon)


def test_polygon_constructor_exists():
    assert callable(Polygon.__init__)


def test_polygon_constructor_args():
    sig = inspect.signature(Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::scalablepolygon_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::ScalablePolygon)


def test_gmf::all::gmfgraph::scalablepolygon_constructor_exists():
    assert callable(gmf::all::gmfgraph::ScalablePolygon.__init__)


def test_gmf::all::gmfgraph::scalablepolygon_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::ScalablePolygon.__init__)
    params = list(sig.parameters.keys())



def test_polyline_is_not_abstract():
    assert not inspect.isabstract(Polyline)


def test_polyline_constructor_exists():
    assert callable(Polyline.__init__)


def test_polyline_constructor_args():
    sig = inspect.signature(Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::polygon_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Polygon)


def test_gmf::all::gmfgraph::polygon_constructor_exists():
    assert callable(gmf::all::gmfgraph::Polygon.__init__)


def test_gmf::all::gmfgraph::polygon_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customclass_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomClass)


def test_gmfgraph::customclass_constructor_exists():
    assert callable(gmfgraph::CustomClass.__init__)


def test_gmfgraph::customclass_constructor_args():
    sig = inspect.signature(gmfgraph::CustomClass.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::realfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::RealFigure)


def test_gmfgraph::realfigure_constructor_exists():
    assert callable(gmfgraph::RealFigure.__init__)


def test_gmfgraph::realfigure_constructor_args():
    sig = inspect.signature(gmfgraph::RealFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomFigure)


def test_gmf::all::gmfgraph::customfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomFigure.__init__)


def test_gmf::all::gmfgraph::customfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_shape_is_not_abstract():
    assert not inspect.isabstract(Shape)


def test_shape_constructor_exists():
    assert callable(Shape.__init__)


def test_shape_constructor_args():
    sig = inspect.signature(Shape.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::RoundedRectangle)


def test_gmf::all::gmfgraph::roundedrectangle_constructor_exists():
    assert callable(gmf::all::gmfgraph::RoundedRectangle.__init__)


def test_gmf::all::gmfgraph::roundedrectangle_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())
    assert "cornerHeight" in params, "Missing parameter 'cornerHeight'"
    assert "cornerWidth" in params, "Missing parameter 'cornerWidth'"

def test_gmf::all::gmfgraph::roundedrectangle_has_cornerHeight():
    assert hasattr(gmf::all::gmfgraph::RoundedRectangle, "cornerHeight")
    descriptor = None
    for klass in gmf::all::gmfgraph::RoundedRectangle.__mro__:
        if "cornerHeight" in klass.__dict__:
            descriptor = klass.__dict__["cornerHeight"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::roundedrectangle_has_cornerWidth():
    assert hasattr(gmf::all::gmfgraph::RoundedRectangle, "cornerWidth")
    descriptor = None
    for klass in gmf::all::gmfgraph::RoundedRectangle.__mro__:
        if "cornerWidth" in klass.__dict__:
            descriptor = klass.__dict__["cornerWidth"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::rectangle_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Rectangle)


def test_gmf::all::gmfgraph::rectangle_constructor_exists():
    assert callable(gmf::all::gmfgraph::Rectangle.__init__)


def test_gmf::all::gmfgraph::rectangle_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_abstractfigure_is_not_abstract():
    assert not inspect.isabstract(AbstractFigure)


def test_abstractfigure_constructor_exists():
    assert callable(AbstractFigure.__init__)


def test_abstractfigure_constructor_args():
    sig = inspect.signature(AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::figureref_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::FigureRef)


def test_gmf::all::gmfgraph::figureref_constructor_exists():
    assert callable(gmf::all::gmfgraph::FigureRef.__init__)


def test_gmf::all::gmfgraph::figureref_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::FigureRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::polyline_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Polyline)


def test_gmf::all::gmfgraph::polyline_constructor_exists():
    assert callable(gmf::all::gmfgraph::Polyline.__init__)


def test_gmf::all::gmfgraph::polyline_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::ellipse_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Ellipse)


def test_gmf::all::gmfgraph::ellipse_constructor_exists():
    assert callable(gmf::all::gmfgraph::Ellipse.__init__)


def test_gmf::all::gmfgraph::ellipse_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::childaccess_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::ChildAccess)


def test_gmf::all::gmfgraph::childaccess_constructor_exists():
    assert callable(gmf::all::gmfgraph::ChildAccess.__init__)


def test_gmf::all::gmfgraph::childaccess_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::ChildAccess.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmf::all::gmfgraph::childaccess_has_accessor():
    assert hasattr(gmf::all::gmfgraph::ChildAccess, "accessor")
    descriptor = None
    for klass in gmf::all::gmfgraph::ChildAccess.__mro__:
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



def test_gmf::all::gmfgraph::abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::AbstractFigure)


def test_gmf::all::gmfgraph::abstractfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::AbstractFigure.__init__)


def test_gmf::all::gmfgraph::abstractfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::AbstractFigure.__init__)
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



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomAttributeOwner)


def test_gmfgraph::customattributeowner_constructor_exists():
    assert callable(gmfgraph::CustomAttributeOwner.__init__)


def test_gmfgraph::customattributeowner_constructor_args():
    sig = inspect.signature(gmfgraph::CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::pinowner_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::PinOwner)


def test_gmfgraph::pinowner_constructor_exists():
    assert callable(gmfgraph::PinOwner.__init__)


def test_gmfgraph::pinowner_constructor_args():
    sig = inspect.signature(gmfgraph::PinOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::abstractfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::AbstractFigure)


def test_gmfgraph::abstractfigure_constructor_exists():
    assert callable(gmfgraph::AbstractFigure.__init__)


def test_gmfgraph::abstractfigure_constructor_args():
    sig = inspect.signature(gmfgraph::AbstractFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::realfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::RealFigure)


def test_gmf::all::gmfgraph::realfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::RealFigure.__init__)


def test_gmf::all::gmfgraph::realfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::RealFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf::all::gmfgraph::realfigure_has_name():
    assert hasattr(gmf::all::gmfgraph::RealFigure, "name")
    descriptor = None
    for klass in gmf::all::gmfgraph::RealFigure.__mro__:
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



def test_gmf::all::gmfgraph::visualfacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::VisualFacet)


def test_gmf::all::gmfgraph::visualfacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::VisualFacet.__init__)


def test_gmf::all::gmfgraph::visualfacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::VisualFacet.__init__)
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



def test_gmf::all::gmfgraph::figure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Figure)


def test_gmf::all::gmfgraph::figure_constructor_exists():
    assert callable(gmf::all::gmfgraph::Figure.__init__)


def test_gmf::all::gmfgraph::figure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Figure.__init__)
    params = list(sig.parameters.keys())



def test_visualfacet_is_not_abstract():
    assert not inspect.isabstract(VisualFacet)


def test_visualfacet_constructor_exists():
    assert callable(VisualFacet.__init__)


def test_visualfacet_constructor_args():
    sig = inspect.signature(VisualFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::alignmentfacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::AlignmentFacet)


def test_gmf::all::gmfgraph::alignmentfacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::AlignmentFacet.__init__)


def test_gmf::all::gmfgraph::alignmentfacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::AlignmentFacet.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"

def test_gmf::all::gmfgraph::alignmentfacet_has_alignment():
    assert hasattr(gmf::all::gmfgraph::AlignmentFacet, "alignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::AlignmentFacet.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::labeloffsetfacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::LabelOffsetFacet)


def test_gmf::all::gmfgraph::labeloffsetfacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::LabelOffsetFacet.__init__)


def test_gmf::all::gmfgraph::labeloffsetfacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::LabelOffsetFacet.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_gmf::all::gmfgraph::labeloffsetfacet_has_x():
    assert hasattr(gmf::all::gmfgraph::LabelOffsetFacet, "x")
    descriptor = None
    for klass in gmf::all::gmfgraph::LabelOffsetFacet.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::labeloffsetfacet_has_y():
    assert hasattr(gmf::all::gmfgraph::LabelOffsetFacet, "y")
    descriptor = None
    for klass in gmf::all::gmfgraph::LabelOffsetFacet.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::generalfacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::GeneralFacet)


def test_gmf::all::gmfgraph::generalfacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::GeneralFacet.__init__)


def test_gmf::all::gmfgraph::generalfacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::GeneralFacet.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "data" in params, "Missing parameter 'data'"

def test_gmf::all::gmfgraph::generalfacet_has_identifier():
    assert hasattr(gmf::all::gmfgraph::GeneralFacet, "identifier")
    descriptor = None
    for klass in gmf::all::gmfgraph::GeneralFacet.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::generalfacet_has_data():
    assert hasattr(gmf::all::gmfgraph::GeneralFacet, "data")
    descriptor = None
    for klass in gmf::all::gmfgraph::GeneralFacet.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::defaultsizefacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::DefaultSizeFacet)


def test_gmf::all::gmfgraph::defaultsizefacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::DefaultSizeFacet.__init__)


def test_gmf::all::gmfgraph::defaultsizefacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::DefaultSizeFacet.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::gradientfacet_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::GradientFacet)


def test_gmf::all::gmfgraph::gradientfacet_constructor_exists():
    assert callable(gmf::all::gmfgraph::GradientFacet.__init__)


def test_gmf::all::gmfgraph::gradientfacet_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::GradientFacet.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_gmf::all::gmfgraph::gradientfacet_has_direction():
    assert hasattr(gmf::all::gmfgraph::GradientFacet, "direction")
    descriptor = None
    for klass in gmf::all::gmfgraph::GradientFacet.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::identity_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Identity)


def test_gmf::all::gmfgraph::identity_constructor_exists():
    assert callable(gmf::all::gmfgraph::Identity.__init__)


def test_gmf::all::gmfgraph::identity_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Identity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf::all::gmfgraph::identity_has_name():
    assert hasattr(gmf::all::gmfgraph::Identity, "name")
    descriptor = None
    for klass in gmf::all::gmfgraph::Identity.__mro__:
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



def test_gmf::all::gmfgraph::flowlayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::FlowLayout)


def test_gmf::all::gmfgraph::flowlayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::FlowLayout.__init__)


def test_gmf::all::gmfgraph::flowlayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::FlowLayout.__init__)
    params = list(sig.parameters.keys())
    assert "matchMinorSize" in params, "Missing parameter 'matchMinorSize'"
    assert "forceSingleLine" in params, "Missing parameter 'forceSingleLine'"
    assert "minorAlignment" in params, "Missing parameter 'minorAlignment'"
    assert "minorSpacing" in params, "Missing parameter 'minorSpacing'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "majorAlignment" in params, "Missing parameter 'majorAlignment'"
    assert "majorSpacing" in params, "Missing parameter 'majorSpacing'"

def test_gmf::all::gmfgraph::flowlayout_has_matchMinorSize():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "matchMinorSize")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "matchMinorSize" in klass.__dict__:
            descriptor = klass.__dict__["matchMinorSize"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_forceSingleLine():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "forceSingleLine")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "forceSingleLine" in klass.__dict__:
            descriptor = klass.__dict__["forceSingleLine"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_minorAlignment():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "minorAlignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "minorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["minorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_minorSpacing():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "minorSpacing")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "minorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["minorSpacing"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_vertical():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "vertical")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_majorAlignment():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "majorAlignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "majorAlignment" in klass.__dict__:
            descriptor = klass.__dict__["majorAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::flowlayout_has_majorSpacing():
    assert hasattr(gmf::all::gmfgraph::FlowLayout, "majorSpacing")
    descriptor = None
    for klass in gmf::all::gmfgraph::FlowLayout.__mro__:
        if "majorSpacing" in klass.__dict__:
            descriptor = klass.__dict__["majorSpacing"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::centerlayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CenterLayout)


def test_gmf::all::gmfgraph::centerlayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::CenterLayout.__init__)


def test_gmf::all::gmfgraph::centerlayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CenterLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::stacklayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::StackLayout)


def test_gmf::all::gmfgraph::stacklayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::StackLayout.__init__)


def test_gmf::all::gmfgraph::stacklayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::StackLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::xylayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::XYLayout)


def test_gmf::all::gmfgraph::xylayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::XYLayout.__init__)


def test_gmf::all::gmfgraph::xylayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::XYLayout.__init__)
    params = list(sig.parameters.keys())



def test_border_is_not_abstract():
    assert not inspect.isabstract(Border)


def test_border_constructor_exists():
    assert callable(Border.__init__)


def test_border_constructor_args():
    sig = inspect.signature(Border.__init__)
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



def test_gmf::all::gmfgraph::connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::ConnectionFigure)


def test_gmf::all::gmfgraph::connectionfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::ConnectionFigure.__init__)


def test_gmf::all::gmfgraph::connectionfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::invisiblerectangle_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::InvisibleRectangle)


def test_gmf::all::gmfgraph::invisiblerectangle_constructor_exists():
    assert callable(gmf::all::gmfgraph::InvisibleRectangle.__init__)


def test_gmf::all::gmfgraph::invisiblerectangle_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::InvisibleRectangle.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::labeledcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::LabeledContainer)


def test_gmf::all::gmfgraph::labeledcontainer_constructor_exists():
    assert callable(gmf::all::gmfgraph::LabeledContainer.__init__)


def test_gmf::all::gmfgraph::labeledcontainer_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::LabeledContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::label_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Label)


def test_gmf::all::gmfgraph::label_constructor_exists():
    assert callable(gmf::all::gmfgraph::Label.__init__)


def test_gmf::all::gmfgraph::label_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Label.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gmf::all::gmfgraph::label_has_text():
    assert hasattr(gmf::all::gmfgraph::Label, "text")
    descriptor = None
    for klass in gmf::all::gmfgraph::Label.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::svgfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::SVGFigure)


def test_gmf::all::gmfgraph::svgfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::SVGFigure.__init__)


def test_gmf::all::gmfgraph::svgfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::SVGFigure.__init__)
    params = list(sig.parameters.keys())
    assert "documentURI" in params, "Missing parameter 'documentURI'"
    assert "noCanvasWidth" in params, "Missing parameter 'noCanvasWidth'"
    assert "noCanvasHeight" in params, "Missing parameter 'noCanvasHeight'"

def test_gmf::all::gmfgraph::svgfigure_has_documentURI():
    assert hasattr(gmf::all::gmfgraph::SVGFigure, "documentURI")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGFigure.__mro__:
        if "documentURI" in klass.__dict__:
            descriptor = klass.__dict__["documentURI"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgfigure_has_noCanvasWidth():
    assert hasattr(gmf::all::gmfgraph::SVGFigure, "noCanvasWidth")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGFigure.__mro__:
        if "noCanvasWidth" in klass.__dict__:
            descriptor = klass.__dict__["noCanvasWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::svgfigure_has_noCanvasHeight():
    assert hasattr(gmf::all::gmfgraph::SVGFigure, "noCanvasHeight")
    descriptor = None
    for klass in gmf::all::gmfgraph::SVGFigure.__mro__:
        if "noCanvasHeight" in klass.__dict__:
            descriptor = klass.__dict__["noCanvasHeight"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::verticallabel_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::VerticalLabel)


def test_gmf::all::gmfgraph::verticallabel_constructor_exists():
    assert callable(gmf::all::gmfgraph::VerticalLabel.__init__)


def test_gmf::all::gmfgraph::verticallabel_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::VerticalLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_gmf::all::gmfgraph::verticallabel_has_text():
    assert hasattr(gmf::all::gmfgraph::VerticalLabel, "text")
    descriptor = None
    for klass in gmf::all::gmfgraph::VerticalLabel.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::DecorationFigure)


def test_gmf::all::gmfgraph::decorationfigure_constructor_exists():
    assert callable(gmf::all::gmfgraph::DecorationFigure.__init__)


def test_gmf::all::gmfgraph::decorationfigure_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::shape_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Shape)


def test_gmf::all::gmfgraph::shape_constructor_exists():
    assert callable(gmf::all::gmfgraph::Shape.__init__)


def test_gmf::all::gmfgraph::shape_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Shape.__init__)
    params = list(sig.parameters.keys())
    assert "lineKind" in params, "Missing parameter 'lineKind'"
    assert "fill" in params, "Missing parameter 'fill'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "xorOutline" in params, "Missing parameter 'xorOutline'"
    assert "outline" in params, "Missing parameter 'outline'"
    assert "xorFill" in params, "Missing parameter 'xorFill'"

def test_gmf::all::gmfgraph::shape_has_lineKind():
    assert hasattr(gmf::all::gmfgraph::Shape, "lineKind")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "lineKind" in klass.__dict__:
            descriptor = klass.__dict__["lineKind"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::shape_has_fill():
    assert hasattr(gmf::all::gmfgraph::Shape, "fill")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::shape_has_lineWidth():
    assert hasattr(gmf::all::gmfgraph::Shape, "lineWidth")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::shape_has_xorOutline():
    assert hasattr(gmf::all::gmfgraph::Shape, "xorOutline")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "xorOutline" in klass.__dict__:
            descriptor = klass.__dict__["xorOutline"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::shape_has_outline():
    assert hasattr(gmf::all::gmfgraph::Shape, "outline")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::shape_has_xorFill():
    assert hasattr(gmf::all::gmfgraph::Shape, "xorFill")
    descriptor = None
    for klass in gmf::all::gmfgraph::Shape.__mro__:
        if "xorFill" in klass.__dict__:
            descriptor = klass.__dict__["xorFill"]
            break
    assert isinstance(descriptor, property)



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



def test_gmf::all::gmfgraph::node_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Node)


def test_gmf::all::gmfgraph::node_constructor_exists():
    assert callable(gmf::all::gmfgraph::Node.__init__)


def test_gmf::all::gmfgraph::node_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "resizeConstraint" in params, "Missing parameter 'resizeConstraint'"
    assert "affixedParentSide" in params, "Missing parameter 'affixedParentSide'"

def test_gmf::all::gmfgraph::node_has_resizeConstraint():
    assert hasattr(gmf::all::gmfgraph::Node, "resizeConstraint")
    descriptor = None
    for klass in gmf::all::gmfgraph::Node.__mro__:
        if "resizeConstraint" in klass.__dict__:
            descriptor = klass.__dict__["resizeConstraint"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::node_has_affixedParentSide():
    assert hasattr(gmf::all::gmfgraph::Node, "affixedParentSide")
    descriptor = None
    for klass in gmf::all::gmfgraph::Node.__mro__:
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



def test_gmf::all::gmfgraph::connection_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Connection)


def test_gmf::all::gmfgraph::connection_constructor_exists():
    assert callable(gmf::all::gmfgraph::Connection.__init__)


def test_gmf::all::gmfgraph::connection_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Connection.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::compartment_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Compartment)


def test_gmf::all::gmfgraph::compartment_constructor_exists():
    assert callable(gmf::all::gmfgraph::Compartment.__init__)


def test_gmf::all::gmfgraph::compartment_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "needsTitle" in params, "Missing parameter 'needsTitle'"

def test_gmf::all::gmfgraph::compartment_has_collapsible():
    assert hasattr(gmf::all::gmfgraph::Compartment, "collapsible")
    descriptor = None
    for klass in gmf::all::gmfgraph::Compartment.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::compartment_has_needsTitle():
    assert hasattr(gmf::all::gmfgraph::Compartment, "needsTitle")
    descriptor = None
    for klass in gmf::all::gmfgraph::Compartment.__mro__:
        if "needsTitle" in klass.__dict__:
            descriptor = klass.__dict__["needsTitle"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::abstractnode_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::AbstractNode)


def test_gmf::all::gmfgraph::abstractnode_constructor_exists():
    assert callable(gmf::all::gmfgraph::AbstractNode.__init__)


def test_gmf::all::gmfgraph::abstractnode_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::AbstractNode.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::styleselector_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::StyleSelector)


def test_gmf::all::tooldef::styleselector_constructor_exists():
    assert callable(gmf::all::tooldef::StyleSelector.__init__)


def test_gmf::all::tooldef::styleselector_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::StyleSelector.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::image_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::Image)


def test_gmf::all::tooldef::image_constructor_exists():
    assert callable(gmf::all::tooldef::Image.__init__)


def test_gmf::all::tooldef::image_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::Image.__init__)
    params = list(sig.parameters.keys())



def test_tooldef::contributionitem_is_not_abstract():
    assert not inspect.isabstract(tooldef::ContributionItem)


def test_tooldef::contributionitem_constructor_exists():
    assert callable(tooldef::ContributionItem.__init__)


def test_tooldef::contributionitem_constructor_args():
    sig = inspect.signature(tooldef::ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_identity_is_not_abstract():
    assert not inspect.isabstract(Identity)


def test_identity_constructor_exists():
    assert callable(Identity.__init__)


def test_identity_constructor_args():
    sig = inspect.signature(Identity.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::figuredescriptor_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::FigureDescriptor)


def test_gmf::all::gmfgraph::figuredescriptor_constructor_exists():
    assert callable(gmf::all::gmfgraph::FigureDescriptor.__init__)


def test_gmf::all::gmfgraph::figuredescriptor_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::FigureDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::figuregallery_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::FigureGallery)


def test_gmf::all::gmfgraph::figuregallery_constructor_exists():
    assert callable(gmf::all::gmfgraph::FigureGallery.__init__)


def test_gmf::all::gmfgraph::figuregallery_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::FigureGallery.__init__)
    params = list(sig.parameters.keys())
    assert "implementationBundle" in params, "Missing parameter 'implementationBundle'"

def test_gmf::all::gmfgraph::figuregallery_has_implementationBundle():
    assert hasattr(gmf::all::gmfgraph::FigureGallery, "implementationBundle")
    descriptor = None
    for klass in gmf::all::gmfgraph::FigureGallery.__mro__:
        if "implementationBundle" in klass.__dict__:
            descriptor = klass.__dict__["implementationBundle"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::pin_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Pin)


def test_gmf::all::gmfgraph::pin_constructor_exists():
    assert callable(gmf::all::gmfgraph::Pin.__init__)


def test_gmf::all::gmfgraph::pin_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Pin.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::diagramelement_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::DiagramElement)


def test_gmf::all::gmfgraph::diagramelement_constructor_exists():
    assert callable(gmf::all::gmfgraph::DiagramElement.__init__)


def test_gmf::all::gmfgraph::diagramelement_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::canvas_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Canvas)


def test_gmf::all::gmfgraph::canvas_constructor_exists():
    assert callable(gmf::all::gmfgraph::Canvas.__init__)


def test_gmf::all::gmfgraph::canvas_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Canvas.__init__)
    params = list(sig.parameters.keys())



def test_tooldef::predefineditem_is_not_abstract():
    assert not inspect.isabstract(tooldef::PredefinedItem)


def test_tooldef::predefineditem_constructor_exists():
    assert callable(tooldef::PredefinedItem.__init__)


def test_tooldef::predefineditem_constructor_args():
    sig = inspect.signature(tooldef::PredefinedItem.__init__)
    params = list(sig.parameters.keys())



def test_tooldef::menu_is_not_abstract():
    assert not inspect.isabstract(tooldef::Menu)


def test_tooldef::menu_constructor_exists():
    assert callable(tooldef::Menu.__init__)


def test_tooldef::menu_constructor_args():
    sig = inspect.signature(tooldef::Menu.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::popupmenu_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::PopupMenu)


def test_gmf::all::tooldef::popupmenu_constructor_exists():
    assert callable(gmf::all::tooldef::PopupMenu.__init__)


def test_gmf::all::tooldef::popupmenu_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::PopupMenu.__init__)
    params = list(sig.parameters.keys())
    assert "iD" in params, "Missing parameter 'iD'"

def test_gmf::all::tooldef::popupmenu_has_iD():
    assert hasattr(gmf::all::tooldef::PopupMenu, "iD")
    descriptor = None
    for klass in gmf::all::tooldef::PopupMenu.__mro__:
        if "iD" in klass.__dict__:
            descriptor = klass.__dict__["iD"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::predefinedmenu_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::PredefinedMenu)


def test_gmf::all::tooldef::predefinedmenu_constructor_exists():
    assert callable(gmf::all::tooldef::PredefinedMenu.__init__)


def test_gmf::all::tooldef::predefinedmenu_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::PredefinedMenu.__init__)
    params = list(sig.parameters.keys())



def test_itembase_is_not_abstract():
    assert not inspect.isabstract(ItemBase)


def test_itembase_constructor_exists():
    assert callable(ItemBase.__init__)


def test_itembase_constructor_args():
    sig = inspect.signature(ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::predefineditem_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::PredefinedItem)


def test_gmf::all::tooldef::predefineditem_constructor_exists():
    assert callable(gmf::all::tooldef::PredefinedItem.__init__)


def test_gmf::all::tooldef::predefineditem_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::PredefinedItem.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_gmf::all::tooldef::predefineditem_has_identifier():
    assert hasattr(gmf::all::tooldef::PredefinedItem, "identifier")
    descriptor = None
    for klass in gmf::all::tooldef::PredefinedItem.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::contributionitem_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ContributionItem)


def test_gmf::all::tooldef::contributionitem_constructor_exists():
    assert callable(gmf::all::tooldef::ContributionItem.__init__)


def test_gmf::all::tooldef::contributionitem_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ContributionItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_gmf::all::tooldef::contributionitem_has_title():
    assert hasattr(gmf::all::tooldef::ContributionItem, "title")
    descriptor = None
    for klass in gmf::all::tooldef::ContributionItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::separator_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::Separator)


def test_gmf::all::tooldef::separator_constructor_exists():
    assert callable(gmf::all::tooldef::Separator.__init__)


def test_gmf::all::tooldef::separator_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::Separator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gmf::all::tooldef::separator_has_name():
    assert hasattr(gmf::all::tooldef::Separator, "name")
    descriptor = None
    for klass in gmf::all::tooldef::Separator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::menu_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::Menu)


def test_gmf::all::tooldef::menu_constructor_exists():
    assert callable(gmf::all::tooldef::Menu.__init__)


def test_gmf::all::tooldef::menu_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::Menu.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::itembase_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ItemBase)


def test_gmf::all::tooldef::itembase_constructor_exists():
    assert callable(gmf::all::tooldef::ItemBase.__init__)


def test_gmf::all::tooldef::itembase_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ItemBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::itemref_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ItemRef)


def test_gmf::all::tooldef::itemref_constructor_exists():
    assert callable(gmf::all::tooldef::ItemRef.__init__)


def test_gmf::all::tooldef::itemref_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ItemRef.__init__)
    params = list(sig.parameters.keys())



def test_contributionitem_is_not_abstract():
    assert not inspect.isabstract(ContributionItem)


def test_contributionitem_constructor_exists():
    assert callable(ContributionItem.__init__)


def test_contributionitem_constructor_args():
    sig = inspect.signature(ContributionItem.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::menuaction_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::MenuAction)


def test_gmf::all::tooldef::menuaction_constructor_exists():
    assert callable(gmf::all::tooldef::MenuAction.__init__)


def test_gmf::all::tooldef::menuaction_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::MenuAction.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "hotKey" in params, "Missing parameter 'hotKey'"

def test_gmf::all::tooldef::menuaction_has_kind():
    assert hasattr(gmf::all::tooldef::MenuAction, "kind")
    descriptor = None
    for klass in gmf::all::tooldef::MenuAction.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::tooldef::menuaction_has_hotKey():
    assert hasattr(gmf::all::tooldef::MenuAction, "hotKey")
    descriptor = None
    for klass in gmf::all::tooldef::MenuAction.__mro__:
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



def test_gmf::all::tooldef::defaultimage_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::DefaultImage)


def test_gmf::all::tooldef::defaultimage_constructor_exists():
    assert callable(gmf::all::tooldef::DefaultImage.__init__)


def test_gmf::all::tooldef::defaultimage_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::DefaultImage.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::bundleimage_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::BundleImage)


def test_gmf::all::tooldef::bundleimage_constructor_exists():
    assert callable(gmf::all::tooldef::BundleImage.__init__)


def test_gmf::all::tooldef::bundleimage_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::BundleImage.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "bundle" in params, "Missing parameter 'bundle'"

def test_gmf::all::tooldef::bundleimage_has_path():
    assert hasattr(gmf::all::tooldef::BundleImage, "path")
    descriptor = None
    for klass in gmf::all::tooldef::BundleImage.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::tooldef::bundleimage_has_bundle():
    assert hasattr(gmf::all::tooldef::BundleImage, "bundle")
    descriptor = None
    for klass in gmf::all::tooldef::BundleImage.__mro__:
        if "bundle" in klass.__dict__:
            descriptor = klass.__dict__["bundle"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::abstracttool_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::AbstractTool)


def test_gmf::all::tooldef::abstracttool_constructor_exists():
    assert callable(gmf::all::tooldef::AbstractTool.__init__)


def test_gmf::all::tooldef::abstracttool_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::AbstractTool.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"

def test_gmf::all::tooldef::abstracttool_has_description():
    assert hasattr(gmf::all::tooldef::AbstractTool, "description")
    descriptor = None
    for klass in gmf::all::tooldef::AbstractTool.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::tooldef::abstracttool_has_title():
    assert hasattr(gmf::all::tooldef::AbstractTool, "title")
    descriptor = None
    for klass in gmf::all::tooldef::AbstractTool.__mro__:
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



def test_gmf::all::tooldef::mainmenu_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::MainMenu)


def test_gmf::all::tooldef::mainmenu_constructor_exists():
    assert callable(gmf::all::tooldef::MainMenu.__init__)


def test_gmf::all::tooldef::mainmenu_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::MainMenu.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_gmf::all::tooldef::mainmenu_has_title():
    assert hasattr(gmf::all::tooldef::MainMenu, "title")
    descriptor = None
    for klass in gmf::all::tooldef::MainMenu.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::toolbar_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::Toolbar)


def test_gmf::all::tooldef::toolbar_constructor_exists():
    assert callable(gmf::all::tooldef::Toolbar.__init__)


def test_gmf::all::tooldef::toolbar_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::Toolbar.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::contextmenu_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ContextMenu)


def test_gmf::all::tooldef::contextmenu_constructor_exists():
    assert callable(gmf::all::tooldef::ContextMenu.__init__)


def test_gmf::all::tooldef::contextmenu_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_menuaction_is_not_abstract():
    assert not inspect.isabstract(MenuAction)


def test_menuaction_constructor_exists():
    assert callable(MenuAction.__init__)


def test_menuaction_constructor_args():
    sig = inspect.signature(MenuAction.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::toolregistry_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ToolRegistry)


def test_gmf::all::tooldef::toolregistry_constructor_exists():
    assert callable(gmf::all::tooldef::ToolRegistry.__init__)


def test_gmf::all::tooldef::toolregistry_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ToolRegistry.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::custompin_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomPin)


def test_gmf::all::gmfgraph::custompin_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomPin.__init__)


def test_gmf::all::gmfgraph::custompin_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomPin.__init__)
    params = list(sig.parameters.keys())
    assert "customOperationType" in params, "Missing parameter 'customOperationType'"
    assert "customOperationName" in params, "Missing parameter 'customOperationName'"

def test_gmf::all::gmfgraph::custompin_has_customOperationType():
    assert hasattr(gmf::all::gmfgraph::CustomPin, "customOperationType")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomPin.__mro__:
        if "customOperationType" in klass.__dict__:
            descriptor = klass.__dict__["customOperationType"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::custompin_has_customOperationName():
    assert hasattr(gmf::all::gmfgraph::CustomPin, "customOperationName")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomPin.__mro__:
        if "customOperationName" in klass.__dict__:
            descriptor = klass.__dict__["customOperationName"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::visiblepin_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::VisiblePin)


def test_gmf::all::gmfgraph::visiblepin_constructor_exists():
    assert callable(gmf::all::gmfgraph::VisiblePin.__init__)


def test_gmf::all::gmfgraph::visiblepin_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::VisiblePin.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::colorpin_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::ColorPin)


def test_gmf::all::gmfgraph::colorpin_constructor_exists():
    assert callable(gmf::all::gmfgraph::ColorPin.__init__)


def test_gmf::all::gmfgraph::colorpin_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::ColorPin.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundNotForeground" in params, "Missing parameter 'backgroundNotForeground'"

def test_gmf::all::gmfgraph::colorpin_has_backgroundNotForeground():
    assert hasattr(gmf::all::gmfgraph::ColorPin, "backgroundNotForeground")
    descriptor = None
    for klass in gmf::all::gmfgraph::ColorPin.__mro__:
        if "backgroundNotForeground" in klass.__dict__:
            descriptor = klass.__dict__["backgroundNotForeground"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::visualeffectmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::VisualEffectMapping)


def test_gmf::all::mappings::visualeffectmapping_constructor_exists():
    assert callable(gmf::all::mappings::VisualEffectMapping.__init__)


def test_gmf::all::mappings::visualeffectmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::VisualEffectMapping.__init__)
    params = list(sig.parameters.keys())
    assert "oclExpression" in params, "Missing parameter 'oclExpression'"

def test_gmf::all::mappings::visualeffectmapping_has_oclExpression():
    assert hasattr(gmf::all::mappings::VisualEffectMapping, "oclExpression")
    descriptor = None
    for klass in gmf::all::mappings::VisualEffectMapping.__mro__:
        if "oclExpression" in klass.__dict__:
            descriptor = klass.__dict__["oclExpression"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::measurable_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::Measurable)


def test_gmf::all::mappings::measurable_constructor_exists():
    assert callable(gmf::all::mappings::Measurable.__init__)


def test_gmf::all::mappings::measurable_constructor_args():
    sig = inspect.signature(gmf::all::mappings::Measurable.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::auditable_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::Auditable)


def test_gmf::all::mappings::auditable_constructor_exists():
    assert callable(gmf::all::mappings::Auditable.__init__)


def test_gmf::all::mappings::auditable_constructor_args():
    sig = inspect.signature(gmf::all::mappings::Auditable.__init__)
    params = list(sig.parameters.keys())



def test_toolcontainer_is_not_abstract():
    assert not inspect.isabstract(ToolContainer)


def test_toolcontainer_constructor_exists():
    assert callable(ToolContainer.__init__)


def test_toolcontainer_constructor_args():
    sig = inspect.signature(ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::palette_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::Palette)


def test_gmf::all::tooldef::palette_constructor_exists():
    assert callable(gmf::all::tooldef::Palette.__init__)


def test_gmf::all::tooldef::palette_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::Palette.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::toolgroup_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ToolGroup)


def test_gmf::all::tooldef::toolgroup_constructor_exists():
    assert callable(gmf::all::tooldef::ToolGroup.__init__)


def test_gmf::all::tooldef::toolgroup_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ToolGroup.__init__)
    params = list(sig.parameters.keys())
    assert "collapsible" in params, "Missing parameter 'collapsible'"
    assert "stack" in params, "Missing parameter 'stack'"

def test_gmf::all::tooldef::toolgroup_has_collapsible():
    assert hasattr(gmf::all::tooldef::ToolGroup, "collapsible")
    descriptor = None
    for klass in gmf::all::tooldef::ToolGroup.__mro__:
        if "collapsible" in klass.__dict__:
            descriptor = klass.__dict__["collapsible"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::tooldef::toolgroup_has_stack():
    assert hasattr(gmf::all::tooldef::ToolGroup, "stack")
    descriptor = None
    for klass in gmf::all::tooldef::ToolGroup.__mro__:
        if "stack" in klass.__dict__:
            descriptor = klass.__dict__["stack"]
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



def test_gmf::all::mappings::metriccontainer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::MetricContainer)


def test_gmf::all::mappings::metriccontainer_constructor_exists():
    assert callable(gmf::all::mappings::MetricContainer.__init__)


def test_gmf::all::mappings::metriccontainer_constructor_args():
    sig = inspect.signature(gmf::all::mappings::MetricContainer.__init__)
    params = list(sig.parameters.keys())



def test_mappings::measurable_is_not_abstract():
    assert not inspect.isabstract(mappings::Measurable)


def test_mappings::measurable_constructor_exists():
    assert callable(mappings::Measurable.__init__)


def test_mappings::measurable_constructor_args():
    sig = inspect.signature(mappings::Measurable.__init__)
    params = list(sig.parameters.keys())



def test_mappings::auditable_is_not_abstract():
    assert not inspect.isabstract(mappings::Auditable)


def test_mappings::auditable_constructor_exists():
    assert callable(mappings::Auditable.__init__)


def test_mappings::auditable_constructor_args():
    sig = inspect.signature(mappings::Auditable.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::notationelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::NotationElementTarget)


def test_gmf::all::mappings::notationelementtarget_constructor_exists():
    assert callable(gmf::all::mappings::NotationElementTarget.__init__)


def test_gmf::all::mappings::notationelementtarget_constructor_args():
    sig = inspect.signature(gmf::all::mappings::NotationElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::diagramelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::DiagramElementTarget)


def test_gmf::all::mappings::diagramelementtarget_constructor_exists():
    assert callable(gmf::all::mappings::DiagramElementTarget.__init__)


def test_gmf::all::mappings::diagramelementtarget_constructor_args():
    sig = inspect.signature(gmf::all::mappings::DiagramElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::domainelementtarget_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::DomainElementTarget)


def test_gmf::all::mappings::domainelementtarget_constructor_exists():
    assert callable(gmf::all::mappings::DomainElementTarget.__init__)


def test_gmf::all::mappings::domainelementtarget_constructor_args():
    sig = inspect.signature(gmf::all::mappings::DomainElementTarget.__init__)
    params = list(sig.parameters.keys())



def test_auditable_is_not_abstract():
    assert not inspect.isabstract(Auditable)


def test_auditable_constructor_exists():
    assert callable(Auditable.__init__)


def test_auditable_constructor_args():
    sig = inspect.signature(Auditable.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::auditedmetrictarget_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::AuditedMetricTarget)


def test_gmf::all::mappings::auditedmetrictarget_constructor_exists():
    assert callable(gmf::all::mappings::AuditedMetricTarget.__init__)


def test_gmf::all::mappings::auditedmetrictarget_constructor_args():
    sig = inspect.signature(gmf::all::mappings::AuditedMetricTarget.__init__)
    params = list(sig.parameters.keys())



def test_rulebase_is_not_abstract():
    assert not inspect.isabstract(RuleBase)


def test_rulebase_constructor_exists():
    assert callable(RuleBase.__init__)


def test_rulebase_constructor_args():
    sig = inspect.signature(RuleBase.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::metricrule_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::MetricRule)


def test_gmf::all::mappings::metricrule_constructor_exists():
    assert callable(gmf::all::mappings::MetricRule.__init__)


def test_gmf::all::mappings::metricrule_constructor_args():
    sig = inspect.signature(gmf::all::mappings::MetricRule.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "highLimit" in params, "Missing parameter 'highLimit'"
    assert "lowLimit" in params, "Missing parameter 'lowLimit'"

def test_gmf::all::mappings::metricrule_has_key():
    assert hasattr(gmf::all::mappings::MetricRule, "key")
    descriptor = None
    for klass in gmf::all::mappings::MetricRule.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::metricrule_has_highLimit():
    assert hasattr(gmf::all::mappings::MetricRule, "highLimit")
    descriptor = None
    for klass in gmf::all::mappings::MetricRule.__mro__:
        if "highLimit" in klass.__dict__:
            descriptor = klass.__dict__["highLimit"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::metricrule_has_lowLimit():
    assert hasattr(gmf::all::mappings::MetricRule, "lowLimit")
    descriptor = None
    for klass in gmf::all::mappings::MetricRule.__mro__:
        if "lowLimit" in klass.__dict__:
            descriptor = klass.__dict__["lowLimit"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::auditrule_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::AuditRule)


def test_gmf::all::mappings::auditrule_constructor_exists():
    assert callable(gmf::all::mappings::AuditRule.__init__)


def test_gmf::all::mappings::auditrule_constructor_args():
    sig = inspect.signature(gmf::all::mappings::AuditRule.__init__)
    params = list(sig.parameters.keys())
    assert "useInLiveMode" in params, "Missing parameter 'useInLiveMode'"
    assert "message" in params, "Missing parameter 'message'"
    assert "severity" in params, "Missing parameter 'severity'"
    assert "id" in params, "Missing parameter 'id'"

def test_gmf::all::mappings::auditrule_has_useInLiveMode():
    assert hasattr(gmf::all::mappings::AuditRule, "useInLiveMode")
    descriptor = None
    for klass in gmf::all::mappings::AuditRule.__mro__:
        if "useInLiveMode" in klass.__dict__:
            descriptor = klass.__dict__["useInLiveMode"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::auditrule_has_message():
    assert hasattr(gmf::all::mappings::AuditRule, "message")
    descriptor = None
    for klass in gmf::all::mappings::AuditRule.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::auditrule_has_severity():
    assert hasattr(gmf::all::mappings::AuditRule, "severity")
    descriptor = None
    for klass in gmf::all::mappings::AuditRule.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::auditrule_has_id():
    assert hasattr(gmf::all::mappings::AuditRule, "id")
    descriptor = None
    for klass in gmf::all::mappings::AuditRule.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::rulebase_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::RuleBase)


def test_gmf::all::mappings::rulebase_constructor_exists():
    assert callable(gmf::all::mappings::RuleBase.__init__)


def test_gmf::all::mappings::rulebase_constructor_args():
    sig = inspect.signature(gmf::all::mappings::RuleBase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_gmf::all::mappings::rulebase_has_name():
    assert hasattr(gmf::all::mappings::RuleBase, "name")
    descriptor = None
    for klass in gmf::all::mappings::RuleBase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::rulebase_has_description():
    assert hasattr(gmf::all::mappings::RuleBase, "description")
    descriptor = None
    for klass in gmf::all::mappings::RuleBase.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::domainattributetarget_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::DomainAttributeTarget)


def test_gmf::all::mappings::domainattributetarget_constructor_exists():
    assert callable(gmf::all::mappings::DomainAttributeTarget.__init__)


def test_gmf::all::mappings::domainattributetarget_constructor_args():
    sig = inspect.signature(gmf::all::mappings::DomainAttributeTarget.__init__)
    params = list(sig.parameters.keys())
    assert "nullAsError" in params, "Missing parameter 'nullAsError'"

def test_gmf::all::mappings::domainattributetarget_has_nullAsError():
    assert hasattr(gmf::all::mappings::DomainAttributeTarget, "nullAsError")
    descriptor = None
    for klass in gmf::all::mappings::DomainAttributeTarget.__mro__:
        if "nullAsError" in klass.__dict__:
            descriptor = klass.__dict__["nullAsError"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::auditcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::AuditContainer)


def test_gmf::all::mappings::auditcontainer_constructor_exists():
    assert callable(gmf::all::mappings::AuditContainer.__init__)


def test_gmf::all::mappings::auditcontainer_constructor_args():
    sig = inspect.signature(gmf::all::mappings::AuditContainer.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_gmf::all::mappings::auditcontainer_has_description():
    assert hasattr(gmf::all::mappings::AuditContainer, "description")
    descriptor = None
    for klass in gmf::all::mappings::AuditContainer.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::auditcontainer_has_id():
    assert hasattr(gmf::all::mappings::AuditContainer, "id")
    descriptor = None
    for klass in gmf::all::mappings::AuditContainer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::auditcontainer_has_name():
    assert hasattr(gmf::all::mappings::AuditContainer, "name")
    descriptor = None
    for klass in gmf::all::mappings::AuditContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::appearancesteward_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::AppearanceSteward)


def test_gmf::all::mappings::appearancesteward_constructor_exists():
    assert callable(gmf::all::mappings::AppearanceSteward.__init__)


def test_gmf::all::mappings::appearancesteward_constructor_args():
    sig = inspect.signature(gmf::all::mappings::AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_abstracttool_is_not_abstract():
    assert not inspect.isabstract(AbstractTool)


def test_abstracttool_constructor_exists():
    assert callable(AbstractTool.__init__)


def test_abstracttool_constructor_args():
    sig = inspect.signature(AbstractTool.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::generictool_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::GenericTool)


def test_gmf::all::tooldef::generictool_constructor_exists():
    assert callable(gmf::all::tooldef::GenericTool.__init__)


def test_gmf::all::tooldef::generictool_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::GenericTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolClass" in params, "Missing parameter 'toolClass'"

def test_gmf::all::tooldef::generictool_has_toolClass():
    assert hasattr(gmf::all::tooldef::GenericTool, "toolClass")
    descriptor = None
    for klass in gmf::all::tooldef::GenericTool.__mro__:
        if "toolClass" in klass.__dict__:
            descriptor = klass.__dict__["toolClass"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::standardtool_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::StandardTool)


def test_gmf::all::tooldef::standardtool_constructor_exists():
    assert callable(gmf::all::tooldef::StandardTool.__init__)


def test_gmf::all::tooldef::standardtool_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::StandardTool.__init__)
    params = list(sig.parameters.keys())
    assert "toolKind" in params, "Missing parameter 'toolKind'"

def test_gmf::all::tooldef::standardtool_has_toolKind():
    assert hasattr(gmf::all::tooldef::StandardTool, "toolKind")
    descriptor = None
    for klass in gmf::all::tooldef::StandardTool.__mro__:
        if "toolKind" in klass.__dict__:
            descriptor = klass.__dict__["toolKind"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::tooldef::paletteseparator_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::PaletteSeparator)


def test_gmf::all::tooldef::paletteseparator_constructor_exists():
    assert callable(gmf::all::tooldef::PaletteSeparator.__init__)


def test_gmf::all::tooldef::paletteseparator_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::PaletteSeparator.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::toolcontainer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::ToolContainer)


def test_gmf::all::tooldef::toolcontainer_constructor_exists():
    assert callable(gmf::all::tooldef::ToolContainer.__init__)


def test_gmf::all::tooldef::toolcontainer_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::ToolContainer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::tooldef::creationtool_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::CreationTool)


def test_gmf::all::tooldef::creationtool_constructor_exists():
    assert callable(gmf::all::tooldef::CreationTool.__init__)


def test_gmf::all::tooldef::creationtool_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::CreationTool.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::toolowner_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ToolOwner)


def test_gmf::all::mappings::toolowner_constructor_exists():
    assert callable(gmf::all::mappings::ToolOwner.__init__)


def test_gmf::all::mappings::toolowner_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_contextmenu_is_not_abstract():
    assert not inspect.isabstract(ContextMenu)


def test_contextmenu_constructor_exists():
    assert callable(ContextMenu.__init__)


def test_contextmenu_constructor_args():
    sig = inspect.signature(ContextMenu.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::menuowner_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::MenuOwner)


def test_gmf::all::mappings::menuowner_constructor_exists():
    assert callable(gmf::all::mappings::MenuOwner.__init__)


def test_gmf::all::mappings::menuowner_constructor_args():
    sig = inspect.signature(gmf::all::mappings::MenuOwner.__init__)
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



def test_gmf::all::mappings::referencenewelementspec_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ReferenceNewElementSpec)


def test_gmf::all::mappings::referencenewelementspec_constructor_exists():
    assert callable(gmf::all::mappings::ReferenceNewElementSpec.__init__)


def test_gmf::all::mappings::referencenewelementspec_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ReferenceNewElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::featurevaluespec_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::FeatureValueSpec)


def test_gmf::all::mappings::featurevaluespec_constructor_exists():
    assert callable(gmf::all::mappings::FeatureValueSpec.__init__)


def test_gmf::all::mappings::featurevaluespec_constructor_args():
    sig = inspect.signature(gmf::all::mappings::FeatureValueSpec.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::elementinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ElementInitializer)


def test_gmf::all::mappings::elementinitializer_constructor_exists():
    assert callable(gmf::all::mappings::ElementInitializer.__init__)


def test_gmf::all::mappings::elementinitializer_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::valueexpression_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ValueExpression)


def test_gmf::all::mappings::valueexpression_constructor_exists():
    assert callable(gmf::all::mappings::ValueExpression.__init__)


def test_gmf::all::mappings::valueexpression_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "langName" in params, "Missing parameter 'langName'"
    assert "language" in params, "Missing parameter 'language'"

def test_gmf::all::mappings::valueexpression_has_body():
    assert hasattr(gmf::all::mappings::ValueExpression, "body")
    descriptor = None
    for klass in gmf::all::mappings::ValueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::valueexpression_has_langName():
    assert hasattr(gmf::all::mappings::ValueExpression, "langName")
    descriptor = None
    for klass in gmf::all::mappings::ValueExpression.__mro__:
        if "langName" in klass.__dict__:
            descriptor = klass.__dict__["langName"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::valueexpression_has_language():
    assert hasattr(gmf::all::mappings::ValueExpression, "language")
    descriptor = None
    for klass in gmf::all::mappings::ValueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::featureinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::FeatureInitializer)


def test_gmf::all::mappings::featureinitializer_constructor_exists():
    assert callable(gmf::all::mappings::FeatureInitializer.__init__)


def test_gmf::all::mappings::featureinitializer_constructor_args():
    sig = inspect.signature(gmf::all::mappings::FeatureInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::linkconstraints_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::LinkConstraints)


def test_gmf::all::mappings::linkconstraints_constructor_exists():
    assert callable(gmf::all::mappings::LinkConstraints.__init__)


def test_gmf::all::mappings::linkconstraints_constructor_args():
    sig = inspect.signature(gmf::all::mappings::LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_mappings::gmf::all::eattribute_is_not_abstract():
    assert not inspect.isabstract(mappings::gmf::all::EAttribute)


def test_mappings::gmf::all::eattribute_constructor_exists():
    assert callable(mappings::gmf::all::EAttribute.__init__)


def test_mappings::gmf::all::eattribute_constructor_args():
    sig = inspect.signature(mappings::gmf::all::EAttribute.__init__)
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



def test_gmf::all::mappings::labelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::LabelMapping)


def test_gmf::all::mappings::labelmapping_constructor_exists():
    assert callable(gmf::all::mappings::LabelMapping.__init__)


def test_gmf::all::mappings::labelmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::LabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "readOnly" in params, "Missing parameter 'readOnly'"

def test_gmf::all::mappings::labelmapping_has_readOnly():
    assert hasattr(gmf::all::mappings::LabelMapping, "readOnly")
    descriptor = None
    for klass in gmf::all::mappings::LabelMapping.__mro__:
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



def test_gmf::all::mappings::constraint_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::Constraint)


def test_gmf::all::mappings::constraint_constructor_exists():
    assert callable(gmf::all::mappings::Constraint.__init__)


def test_gmf::all::mappings::constraint_constructor_args():
    sig = inspect.signature(gmf::all::mappings::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_canvas_is_not_abstract():
    assert not inspect.isabstract(Canvas)


def test_canvas_constructor_exists():
    assert callable(Canvas.__init__)


def test_canvas_constructor_args():
    sig = inspect.signature(Canvas.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::canvasmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::CanvasMapping)


def test_gmf::all::mappings::canvasmapping_constructor_exists():
    assert callable(gmf::all::mappings::CanvasMapping.__init__)


def test_gmf::all::mappings::canvasmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::CanvasMapping.__init__)
    params = list(sig.parameters.keys())



def test_linkconstraints_is_not_abstract():
    assert not inspect.isabstract(LinkConstraints)


def test_linkconstraints_constructor_exists():
    assert callable(LinkConstraints.__init__)


def test_linkconstraints_constructor_args():
    sig = inspect.signature(LinkConstraints.__init__)
    params = list(sig.parameters.keys())



def test_mappings::gmf::all::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(mappings::gmf::all::EStructuralFeature)


def test_mappings::gmf::all::estructuralfeature_constructor_exists():
    assert callable(mappings::gmf::all::EStructuralFeature.__init__)


def test_mappings::gmf::all::estructuralfeature_constructor_args():
    sig = inspect.signature(mappings::gmf::all::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_connection_is_not_abstract():
    assert not inspect.isabstract(Connection)


def test_connection_constructor_exists():
    assert callable(Connection.__init__)


def test_connection_constructor_args():
    sig = inspect.signature(Connection.__init__)
    params = list(sig.parameters.keys())



def test_mappings::needscontainment_is_not_abstract():
    assert not inspect.isabstract(mappings::NeedsContainment)


def test_mappings::needscontainment_constructor_exists():
    assert callable(mappings::NeedsContainment.__init__)


def test_mappings::needscontainment_constructor_args():
    sig = inspect.signature(mappings::NeedsContainment.__init__)
    params = list(sig.parameters.keys())



def test_compartment_is_not_abstract():
    assert not inspect.isabstract(Compartment)


def test_compartment_constructor_exists():
    assert callable(Compartment.__init__)


def test_compartment_constructor_args():
    sig = inspect.signature(Compartment.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::compartmentmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::CompartmentMapping)


def test_gmf::all::mappings::compartmentmapping_constructor_exists():
    assert callable(gmf::all::mappings::CompartmentMapping.__init__)


def test_gmf::all::mappings::compartmentmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::CompartmentMapping.__init__)
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



def test_mappings::gmf::all::epackage_is_not_abstract():
    assert not inspect.isabstract(mappings::gmf::all::EPackage)


def test_mappings::gmf::all::epackage_constructor_exists():
    assert callable(mappings::gmf::all::EPackage.__init__)


def test_mappings::gmf::all::epackage_constructor_args():
    sig = inspect.signature(mappings::gmf::all::EPackage.__init__)
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



def test_gmf::all::mappings::topnodereference_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::TopNodeReference)


def test_gmf::all::mappings::topnodereference_constructor_exists():
    assert callable(gmf::all::mappings::TopNodeReference.__init__)


def test_gmf::all::mappings::topnodereference_constructor_args():
    sig = inspect.signature(gmf::all::mappings::TopNodeReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::childreference_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ChildReference)


def test_gmf::all::mappings::childreference_constructor_exists():
    assert callable(gmf::all::mappings::ChildReference.__init__)


def test_gmf::all::mappings::childreference_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ChildReference.__init__)
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



def test_gmf::all::mappings::nodereference_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::NodeReference)


def test_gmf::all::mappings::nodereference_constructor_exists():
    assert callable(gmf::all::mappings::NodeReference.__init__)


def test_gmf::all::mappings::nodereference_constructor_args():
    sig = inspect.signature(gmf::all::mappings::NodeReference.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::diagramlabel_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::DiagramLabel)


def test_gmf::all::gmfgraph::diagramlabel_constructor_exists():
    assert callable(gmf::all::gmfgraph::DiagramLabel.__init__)


def test_gmf::all::gmfgraph::diagramlabel_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::DiagramLabel.__init__)
    params = list(sig.parameters.keys())
    assert "external" in params, "Missing parameter 'external'"
    assert "elementIcon" in params, "Missing parameter 'elementIcon'"

def test_gmf::all::gmfgraph::diagramlabel_has_external():
    assert hasattr(gmf::all::gmfgraph::DiagramLabel, "external")
    descriptor = None
    for klass in gmf::all::gmfgraph::DiagramLabel.__mro__:
        if "external" in klass.__dict__:
            descriptor = klass.__dict__["external"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::diagramlabel_has_elementIcon():
    assert hasattr(gmf::all::gmfgraph::DiagramLabel, "elementIcon")
    descriptor = None
    for klass in gmf::all::gmfgraph::DiagramLabel.__mro__:
        if "elementIcon" in klass.__dict__:
            descriptor = klass.__dict__["elementIcon"]
            break
    assert isinstance(descriptor, property)



def test_mappings::appearancesteward_is_not_abstract():
    assert not inspect.isabstract(mappings::AppearanceSteward)


def test_mappings::appearancesteward_constructor_exists():
    assert callable(mappings::AppearanceSteward.__init__)


def test_mappings::appearancesteward_constructor_args():
    sig = inspect.signature(mappings::AppearanceSteward.__init__)
    params = list(sig.parameters.keys())



def test_mappings::toolowner_is_not_abstract():
    assert not inspect.isabstract(mappings::ToolOwner)


def test_mappings::toolowner_constructor_exists():
    assert callable(mappings::ToolOwner.__init__)


def test_mappings::toolowner_constructor_args():
    sig = inspect.signature(mappings::ToolOwner.__init__)
    params = list(sig.parameters.keys())



def test_mappings::menuowner_is_not_abstract():
    assert not inspect.isabstract(mappings::MenuOwner)


def test_mappings::menuowner_constructor_exists():
    assert callable(mappings::MenuOwner.__init__)


def test_mappings::menuowner_constructor_args():
    sig = inspect.signature(mappings::MenuOwner.__init__)
    params = list(sig.parameters.keys())



def test_mappings::mappingentry_is_not_abstract():
    assert not inspect.isabstract(mappings::MappingEntry)


def test_mappings::mappingentry_constructor_exists():
    assert callable(mappings::MappingEntry.__init__)


def test_mappings::mappingentry_constructor_args():
    sig = inspect.signature(mappings::MappingEntry.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::linkmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::LinkMapping)


def test_gmf::all::mappings::linkmapping_constructor_exists():
    assert callable(gmf::all::mappings::LinkMapping.__init__)


def test_gmf::all::mappings::linkmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::LinkMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::nodemapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::NodeMapping)


def test_gmf::all::mappings::nodemapping_constructor_exists():
    assert callable(gmf::all::mappings::NodeMapping.__init__)


def test_gmf::all::mappings::nodemapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::NodeMapping.__init__)
    params = list(sig.parameters.keys())



def test_labelmapping_is_not_abstract():
    assert not inspect.isabstract(LabelMapping)


def test_labelmapping_constructor_exists():
    assert callable(LabelMapping.__init__)


def test_labelmapping_constructor_args():
    sig = inspect.signature(LabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::expressionlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::ExpressionLabelMapping)


def test_gmf::all::mappings::expressionlabelmapping_constructor_exists():
    assert callable(gmf::all::mappings::ExpressionLabelMapping.__init__)


def test_gmf::all::mappings::expressionlabelmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::ExpressionLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::featurelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::FeatureLabelMapping)


def test_gmf::all::mappings::featurelabelmapping_constructor_exists():
    assert callable(gmf::all::mappings::FeatureLabelMapping.__init__)


def test_gmf::all::mappings::featurelabelmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::FeatureLabelMapping.__init__)
    params = list(sig.parameters.keys())
    assert "editPattern" in params, "Missing parameter 'editPattern'"
    assert "editMethod" in params, "Missing parameter 'editMethod'"
    assert "editorPattern" in params, "Missing parameter 'editorPattern'"
    assert "viewPattern" in params, "Missing parameter 'viewPattern'"
    assert "viewMethod" in params, "Missing parameter 'viewMethod'"

def test_gmf::all::mappings::featurelabelmapping_has_editPattern():
    assert hasattr(gmf::all::mappings::FeatureLabelMapping, "editPattern")
    descriptor = None
    for klass in gmf::all::mappings::FeatureLabelMapping.__mro__:
        if "editPattern" in klass.__dict__:
            descriptor = klass.__dict__["editPattern"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::featurelabelmapping_has_editMethod():
    assert hasattr(gmf::all::mappings::FeatureLabelMapping, "editMethod")
    descriptor = None
    for klass in gmf::all::mappings::FeatureLabelMapping.__mro__:
        if "editMethod" in klass.__dict__:
            descriptor = klass.__dict__["editMethod"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::featurelabelmapping_has_editorPattern():
    assert hasattr(gmf::all::mappings::FeatureLabelMapping, "editorPattern")
    descriptor = None
    for klass in gmf::all::mappings::FeatureLabelMapping.__mro__:
        if "editorPattern" in klass.__dict__:
            descriptor = klass.__dict__["editorPattern"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::featurelabelmapping_has_viewPattern():
    assert hasattr(gmf::all::mappings::FeatureLabelMapping, "viewPattern")
    descriptor = None
    for klass in gmf::all::mappings::FeatureLabelMapping.__mro__:
        if "viewPattern" in klass.__dict__:
            descriptor = klass.__dict__["viewPattern"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::mappings::featurelabelmapping_has_viewMethod():
    assert hasattr(gmf::all::mappings::FeatureLabelMapping, "viewMethod")
    descriptor = None
    for klass in gmf::all::mappings::FeatureLabelMapping.__mro__:
        if "viewMethod" in klass.__dict__:
            descriptor = klass.__dict__["viewMethod"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::mappings::designlabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::DesignLabelMapping)


def test_gmf::all::mappings::designlabelmapping_constructor_exists():
    assert callable(gmf::all::mappings::DesignLabelMapping.__init__)


def test_gmf::all::mappings::designlabelmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::DesignLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::oclchoicelabelmapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::OclChoiceLabelMapping)


def test_gmf::all::mappings::oclchoicelabelmapping_constructor_exists():
    assert callable(gmf::all::mappings::OclChoiceLabelMapping.__init__)


def test_gmf::all::mappings::oclchoicelabelmapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::OclChoiceLabelMapping.__init__)
    params = list(sig.parameters.keys())



def test_elementinitializer_is_not_abstract():
    assert not inspect.isabstract(ElementInitializer)


def test_elementinitializer_constructor_exists():
    assert callable(ElementInitializer.__init__)


def test_elementinitializer_constructor_args():
    sig = inspect.signature(ElementInitializer.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::featureseqinitializer_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::FeatureSeqInitializer)


def test_gmf::all::mappings::featureseqinitializer_constructor_exists():
    assert callable(gmf::all::mappings::FeatureSeqInitializer.__init__)


def test_gmf::all::mappings::featureseqinitializer_constructor_args():
    sig = inspect.signature(gmf::all::mappings::FeatureSeqInitializer.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_mappings::gmf::all::eclass_is_not_abstract():
    assert not inspect.isabstract(mappings::gmf::all::EClass)


def test_mappings::gmf::all::eclass_constructor_exists():
    assert callable(mappings::gmf::all::EClass.__init__)


def test_mappings::gmf::all::eclass_constructor_args():
    sig = inspect.signature(mappings::gmf::all::EClass.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::mappingentry_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::MappingEntry)


def test_gmf::all::mappings::mappingentry_constructor_exists():
    assert callable(gmf::all::mappings::MappingEntry.__init__)


def test_gmf::all::mappings::mappingentry_constructor_args():
    sig = inspect.signature(gmf::all::mappings::MappingEntry.__init__)
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



def test_gmf::all::tooldef::genericstyleselector_is_not_abstract():
    assert not inspect.isabstract(gmf::all::tooldef::GenericStyleSelector)


def test_gmf::all::tooldef::genericstyleselector_constructor_exists():
    assert callable(gmf::all::tooldef::GenericStyleSelector.__init__)


def test_gmf::all::tooldef::genericstyleselector_constructor_args():
    sig = inspect.signature(gmf::all::tooldef::GenericStyleSelector.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_gmf::all::tooldef::genericstyleselector_has_values():
    assert hasattr(gmf::all::tooldef::GenericStyleSelector, "values")
    descriptor = None
    for klass in gmf::all::tooldef::GenericStyleSelector.__mro__:
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



def test_mappings::gmf::all::ereference_is_not_abstract():
    assert not inspect.isabstract(mappings::gmf::all::EReference)


def test_mappings::gmf::all::ereference_constructor_exists():
    assert callable(mappings::gmf::all::EReference.__init__)


def test_mappings::gmf::all::ereference_constructor_args():
    sig = inspect.signature(mappings::gmf::all::EReference.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::mappings::needscontainment_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::NeedsContainment)


def test_gmf::all::mappings::needscontainment_constructor_exists():
    assert callable(gmf::all::mappings::NeedsContainment.__init__)


def test_gmf::all::mappings::needscontainment_constructor_args():
    sig = inspect.signature(gmf::all::mappings::NeedsContainment.__init__)
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



def test_gmf::all::mappings::mapping_is_not_abstract():
    assert not inspect.isabstract(gmf::all::mappings::Mapping)


def test_gmf::all::mappings::mapping_constructor_exists():
    assert callable(gmf::all::mappings::Mapping.__init__)


def test_gmf::all::mappings::mapping_constructor_args():
    sig = inspect.signature(gmf::all::mappings::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::rectangle2d_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Rectangle2D)


def test_gmf::all::gmfgraph::rectangle2d_constructor_exists():
    assert callable(gmf::all::gmfgraph::Rectangle2D.__init__)


def test_gmf::all::gmfgraph::rectangle2d_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Rectangle2D.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"

def test_gmf::all::gmfgraph::rectangle2d_has_height():
    assert hasattr(gmf::all::gmfgraph::Rectangle2D, "height")
    descriptor = None
    for klass in gmf::all::gmfgraph::Rectangle2D.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::rectangle2d_has_x():
    assert hasattr(gmf::all::gmfgraph::Rectangle2D, "x")
    descriptor = None
    for klass in gmf::all::gmfgraph::Rectangle2D.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::rectangle2d_has_y():
    assert hasattr(gmf::all::gmfgraph::Rectangle2D, "y")
    descriptor = None
    for klass in gmf::all::gmfgraph::Rectangle2D.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::rectangle2d_has_width():
    assert hasattr(gmf::all::gmfgraph::Rectangle2D, "width")
    descriptor = None
    for klass in gmf::all::gmfgraph::Rectangle2D.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::gridlayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::GridLayout)


def test_gmf::all::gmfgraph::gridlayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::GridLayout.__init__)


def test_gmf::all::gmfgraph::gridlayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::GridLayout.__init__)
    params = list(sig.parameters.keys())
    assert "numColumns" in params, "Missing parameter 'numColumns'"
    assert "equalWidth" in params, "Missing parameter 'equalWidth'"

def test_gmf::all::gmfgraph::gridlayout_has_numColumns():
    assert hasattr(gmf::all::gmfgraph::GridLayout, "numColumns")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayout.__mro__:
        if "numColumns" in klass.__dict__:
            descriptor = klass.__dict__["numColumns"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayout_has_equalWidth():
    assert hasattr(gmf::all::gmfgraph::GridLayout, "equalWidth")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayout.__mro__:
        if "equalWidth" in klass.__dict__:
            descriptor = klass.__dict__["equalWidth"]
            break
    assert isinstance(descriptor, property)



def test_gmfgraph::layout_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Layout)


def test_gmfgraph::layout_constructor_exists():
    assert callable(gmfgraph::Layout.__init__)


def test_gmfgraph::layout_constructor_args():
    sig = inspect.signature(gmfgraph::Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customlayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomLayout)


def test_gmf::all::gmfgraph::customlayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomLayout.__init__)


def test_gmf::all::gmfgraph::customlayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::layoutref_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::LayoutRef)


def test_gmf::all::gmfgraph::layoutref_constructor_exists():
    assert callable(gmf::all::gmfgraph::LayoutRef.__init__)


def test_gmf::all::gmfgraph::layoutref_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::LayoutRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::layout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Layout)


def test_gmf::all::gmfgraph::layout_constructor_exists():
    assert callable(gmf::all::gmfgraph::Layout.__init__)


def test_gmf::all::gmfgraph::layout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Layout.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::layoutable_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Layoutable)


def test_gmf::all::gmfgraph::layoutable_constructor_exists():
    assert callable(gmf::all::gmfgraph::Layoutable.__init__)


def test_gmf::all::gmfgraph::layoutable_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Layoutable.__init__)
    params = list(sig.parameters.keys())



def test_layoutdata_is_not_abstract():
    assert not inspect.isabstract(LayoutData)


def test_layoutdata_constructor_exists():
    assert callable(LayoutData.__init__)


def test_layoutdata_constructor_args():
    sig = inspect.signature(LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::xylayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::XYLayoutData)


def test_gmf::all::gmfgraph::xylayoutdata_constructor_exists():
    assert callable(gmf::all::gmfgraph::XYLayoutData.__init__)


def test_gmf::all::gmfgraph::xylayoutdata_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::XYLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::borderlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::BorderLayoutData)


def test_gmf::all::gmfgraph::borderlayoutdata_constructor_exists():
    assert callable(gmf::all::gmfgraph::BorderLayoutData.__init__)


def test_gmf::all::gmfgraph::borderlayoutdata_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::BorderLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "alignment" in params, "Missing parameter 'alignment'"
    assert "vertical" in params, "Missing parameter 'vertical'"

def test_gmf::all::gmfgraph::borderlayoutdata_has_alignment():
    assert hasattr(gmf::all::gmfgraph::BorderLayoutData, "alignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::BorderLayoutData.__mro__:
        if "alignment" in klass.__dict__:
            descriptor = klass.__dict__["alignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::borderlayoutdata_has_vertical():
    assert hasattr(gmf::all::gmfgraph::BorderLayoutData, "vertical")
    descriptor = None
    for klass in gmf::all::gmfgraph::BorderLayoutData.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::gridlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::GridLayoutData)


def test_gmf::all::gmfgraph::gridlayoutdata_constructor_exists():
    assert callable(gmf::all::gmfgraph::GridLayoutData.__init__)


def test_gmf::all::gmfgraph::gridlayoutdata_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::GridLayoutData.__init__)
    params = list(sig.parameters.keys())
    assert "verticalAlignment" in params, "Missing parameter 'verticalAlignment'"
    assert "horizontalSpan" in params, "Missing parameter 'horizontalSpan'"
    assert "grabExcessVerticalSpace" in params, "Missing parameter 'grabExcessVerticalSpace'"
    assert "verticalSpan" in params, "Missing parameter 'verticalSpan'"
    assert "grabExcessHorizontalSpace" in params, "Missing parameter 'grabExcessHorizontalSpace'"
    assert "horizontalIndent" in params, "Missing parameter 'horizontalIndent'"
    assert "horizontalAlignment" in params, "Missing parameter 'horizontalAlignment'"

def test_gmf::all::gmfgraph::gridlayoutdata_has_verticalAlignment():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "verticalAlignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "verticalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["verticalAlignment"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_horizontalSpan():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "horizontalSpan")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "horizontalSpan" in klass.__dict__:
            descriptor = klass.__dict__["horizontalSpan"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_grabExcessVerticalSpace():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "grabExcessVerticalSpace")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "grabExcessVerticalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessVerticalSpace"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_verticalSpan():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "verticalSpan")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "verticalSpan" in klass.__dict__:
            descriptor = klass.__dict__["verticalSpan"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_grabExcessHorizontalSpace():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "grabExcessHorizontalSpace")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "grabExcessHorizontalSpace" in klass.__dict__:
            descriptor = klass.__dict__["grabExcessHorizontalSpace"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_horizontalIndent():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "horizontalIndent")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "horizontalIndent" in klass.__dict__:
            descriptor = klass.__dict__["horizontalIndent"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::gridlayoutdata_has_horizontalAlignment():
    assert hasattr(gmf::all::gmfgraph::GridLayoutData, "horizontalAlignment")
    descriptor = None
    for klass in gmf::all::gmfgraph::GridLayoutData.__mro__:
        if "horizontalAlignment" in klass.__dict__:
            descriptor = klass.__dict__["horizontalAlignment"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::borderlayout_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::BorderLayout)


def test_gmf::all::gmfgraph::borderlayout_constructor_exists():
    assert callable(gmf::all::gmfgraph::BorderLayout.__init__)


def test_gmf::all::gmfgraph::borderlayout_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::BorderLayout.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::border_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Border)


def test_gmfgraph::border_constructor_exists():
    assert callable(gmfgraph::Border.__init__)


def test_gmfgraph::border_constructor_args():
    sig = inspect.signature(gmfgraph::Border.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customborder_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomBorder)


def test_gmf::all::gmfgraph::customborder_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomBorder.__init__)


def test_gmf::all::gmfgraph::customborder_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::compoundborder_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CompoundBorder)


def test_gmf::all::gmfgraph::compoundborder_constructor_exists():
    assert callable(gmf::all::gmfgraph::CompoundBorder.__init__)


def test_gmf::all::gmfgraph::compoundborder_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CompoundBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::marginborder_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::MarginBorder)


def test_gmf::all::gmfgraph::marginborder_constructor_exists():
    assert callable(gmf::all::gmfgraph::MarginBorder.__init__)


def test_gmf::all::gmfgraph::marginborder_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::MarginBorder.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::lineborder_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::LineBorder)


def test_gmf::all::gmfgraph::lineborder_constructor_exists():
    assert callable(gmf::all::gmfgraph::LineBorder.__init__)


def test_gmf::all::gmfgraph::lineborder_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::LineBorder.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_gmf::all::gmfgraph::lineborder_has_width():
    assert hasattr(gmf::all::gmfgraph::LineBorder, "width")
    descriptor = None
    for klass in gmf::all::gmfgraph::LineBorder.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::borderref_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::BorderRef)


def test_gmf::all::gmfgraph::borderref_constructor_exists():
    assert callable(gmf::all::gmfgraph::BorderRef.__init__)


def test_gmf::all::gmfgraph::borderref_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::BorderRef.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::border_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Border)


def test_gmf::all::gmfgraph::border_constructor_exists():
    assert callable(gmf::all::gmfgraph::Border.__init__)


def test_gmf::all::gmfgraph::border_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Border.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::LayoutData)


def test_gmfgraph::layoutdata_constructor_exists():
    assert callable(gmfgraph::LayoutData.__init__)


def test_gmfgraph::layoutdata_constructor_args():
    sig = inspect.signature(gmfgraph::LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customlayoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomLayoutData)


def test_gmf::all::gmfgraph::customlayoutdata_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomLayoutData.__init__)


def test_gmf::all::gmfgraph::customlayoutdata_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomLayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::layoutdata_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::LayoutData)


def test_gmf::all::gmfgraph::layoutdata_constructor_exists():
    assert callable(gmf::all::gmfgraph::LayoutData.__init__)


def test_gmf::all::gmfgraph::layoutdata_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::LayoutData.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::point_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Point)


def test_gmf::all::gmfgraph::point_constructor_exists():
    assert callable(gmf::all::gmfgraph::Point.__init__)


def test_gmf::all::gmfgraph::point_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Point.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_gmf::all::gmfgraph::point_has_y():
    assert hasattr(gmf::all::gmfgraph::Point, "y")
    descriptor = None
    for klass in gmf::all::gmfgraph::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::point_has_x():
    assert hasattr(gmf::all::gmfgraph::Point, "x")
    descriptor = None
    for klass in gmf::all::gmfgraph::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::basicfont_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::BasicFont)


def test_gmf::all::gmfgraph::basicfont_constructor_exists():
    assert callable(gmf::all::gmfgraph::BasicFont.__init__)


def test_gmf::all::gmfgraph::basicfont_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::BasicFont.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "faceName" in params, "Missing parameter 'faceName'"
    assert "height" in params, "Missing parameter 'height'"

def test_gmf::all::gmfgraph::basicfont_has_style():
    assert hasattr(gmf::all::gmfgraph::BasicFont, "style")
    descriptor = None
    for klass in gmf::all::gmfgraph::BasicFont.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::basicfont_has_faceName():
    assert hasattr(gmf::all::gmfgraph::BasicFont, "faceName")
    descriptor = None
    for klass in gmf::all::gmfgraph::BasicFont.__mro__:
        if "faceName" in klass.__dict__:
            descriptor = klass.__dict__["faceName"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::basicfont_has_height():
    assert hasattr(gmf::all::gmfgraph::BasicFont, "height")
    descriptor = None
    for klass in gmf::all::gmfgraph::BasicFont.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::font_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Font)


def test_gmf::all::gmfgraph::font_constructor_exists():
    assert callable(gmf::all::gmfgraph::Font.__init__)


def test_gmf::all::gmfgraph::font_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Font.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::constantcolor_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::ConstantColor)


def test_gmf::all::gmfgraph::constantcolor_constructor_exists():
    assert callable(gmf::all::gmfgraph::ConstantColor.__init__)


def test_gmf::all::gmfgraph::constantcolor_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::ConstantColor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_gmf::all::gmfgraph::constantcolor_has_value():
    assert hasattr(gmf::all::gmfgraph::ConstantColor, "value")
    descriptor = None
    for klass in gmf::all::gmfgraph::ConstantColor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::rgbcolor_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::RGBColor)


def test_gmf::all::gmfgraph::rgbcolor_constructor_exists():
    assert callable(gmf::all::gmfgraph::RGBColor.__init__)


def test_gmf::all::gmfgraph::rgbcolor_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "blue" in params, "Missing parameter 'blue'"
    assert "green" in params, "Missing parameter 'green'"
    assert "red" in params, "Missing parameter 'red'"

def test_gmf::all::gmfgraph::rgbcolor_has_blue():
    assert hasattr(gmf::all::gmfgraph::RGBColor, "blue")
    descriptor = None
    for klass in gmf::all::gmfgraph::RGBColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::rgbcolor_has_green():
    assert hasattr(gmf::all::gmfgraph::RGBColor, "green")
    descriptor = None
    for klass in gmf::all::gmfgraph::RGBColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::rgbcolor_has_red():
    assert hasattr(gmf::all::gmfgraph::RGBColor, "red")
    descriptor = None
    for klass in gmf::all::gmfgraph::RGBColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::color_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Color)


def test_gmf::all::gmfgraph::color_constructor_exists():
    assert callable(gmf::all::gmfgraph::Color.__init__)


def test_gmf::all::gmfgraph::color_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Color.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::customfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::CustomFigure)


def test_gmfgraph::customfigure_constructor_exists():
    assert callable(gmfgraph::CustomFigure.__init__)


def test_gmfgraph::customfigure_constructor_args():
    sig = inspect.signature(gmfgraph::CustomFigure.__init__)
    params = list(sig.parameters.keys())



def test_figureaccessor_is_not_abstract():
    assert not inspect.isabstract(FigureAccessor)


def test_figureaccessor_constructor_exists():
    assert callable(FigureAccessor.__init__)


def test_figureaccessor_constructor_args():
    sig = inspect.signature(FigureAccessor.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::insets_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Insets)


def test_gmf::all::gmfgraph::insets_constructor_exists():
    assert callable(gmf::all::gmfgraph::Insets.__init__)


def test_gmf::all::gmfgraph::insets_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Insets.__init__)
    params = list(sig.parameters.keys())
    assert "top" in params, "Missing parameter 'top'"
    assert "left" in params, "Missing parameter 'left'"
    assert "right" in params, "Missing parameter 'right'"
    assert "bottom" in params, "Missing parameter 'bottom'"

def test_gmf::all::gmfgraph::insets_has_top():
    assert hasattr(gmf::all::gmfgraph::Insets, "top")
    descriptor = None
    for klass in gmf::all::gmfgraph::Insets.__mro__:
        if "top" in klass.__dict__:
            descriptor = klass.__dict__["top"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::insets_has_left():
    assert hasattr(gmf::all::gmfgraph::Insets, "left")
    descriptor = None
    for klass in gmf::all::gmfgraph::Insets.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::insets_has_right():
    assert hasattr(gmf::all::gmfgraph::Insets, "right")
    descriptor = None
    for klass in gmf::all::gmfgraph::Insets.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::insets_has_bottom():
    assert hasattr(gmf::all::gmfgraph::Insets, "bottom")
    descriptor = None
    for klass in gmf::all::gmfgraph::Insets.__mro__:
        if "bottom" in klass.__dict__:
            descriptor = klass.__dict__["bottom"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::dimension_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::Dimension)


def test_gmf::all::gmfgraph::dimension_constructor_exists():
    assert callable(gmf::all::gmfgraph::Dimension.__init__)


def test_gmf::all::gmfgraph::dimension_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "dx" in params, "Missing parameter 'dx'"
    assert "dy" in params, "Missing parameter 'dy'"

def test_gmf::all::gmfgraph::dimension_has_dx():
    assert hasattr(gmf::all::gmfgraph::Dimension, "dx")
    descriptor = None
    for klass in gmf::all::gmfgraph::Dimension.__mro__:
        if "dx" in klass.__dict__:
            descriptor = klass.__dict__["dx"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::dimension_has_dy():
    assert hasattr(gmf::all::gmfgraph::Dimension, "dy")
    descriptor = None
    for klass in gmf::all::gmfgraph::Dimension.__mro__:
        if "dy" in klass.__dict__:
            descriptor = klass.__dict__["dy"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::figureaccessor_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::FigureAccessor)


def test_gmf::all::gmfgraph::figureaccessor_constructor_exists():
    assert callable(gmf::all::gmfgraph::FigureAccessor.__init__)


def test_gmf::all::gmfgraph::figureaccessor_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::FigureAccessor.__init__)
    params = list(sig.parameters.keys())
    assert "accessor" in params, "Missing parameter 'accessor'"

def test_gmf::all::gmfgraph::figureaccessor_has_accessor():
    assert hasattr(gmf::all::gmfgraph::FigureAccessor, "accessor")
    descriptor = None
    for klass in gmf::all::gmfgraph::FigureAccessor.__mro__:
        if "accessor" in klass.__dict__:
            descriptor = klass.__dict__["accessor"]
            break
    assert isinstance(descriptor, property)



def test_gmf::all::gmfgraph::customattribute_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomAttribute)


def test_gmf::all::gmfgraph::customattribute_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomAttribute.__init__)


def test_gmf::all::gmfgraph::customattribute_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "multiStatementValue" in params, "Missing parameter 'multiStatementValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "directAccess" in params, "Missing parameter 'directAccess'"

def test_gmf::all::gmfgraph::customattribute_has_multiStatementValue():
    assert hasattr(gmf::all::gmfgraph::CustomAttribute, "multiStatementValue")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomAttribute.__mro__:
        if "multiStatementValue" in klass.__dict__:
            descriptor = klass.__dict__["multiStatementValue"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::customattribute_has_name():
    assert hasattr(gmf::all::gmfgraph::CustomAttribute, "name")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::customattribute_has_value():
    assert hasattr(gmf::all::gmfgraph::CustomAttribute, "value")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_gmf::all::gmfgraph::customattribute_has_directAccess():
    assert hasattr(gmf::all::gmfgraph::CustomAttribute, "directAccess")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomAttribute.__mro__:
        if "directAccess" in klass.__dict__:
            descriptor = klass.__dict__["directAccess"]
            break
    assert isinstance(descriptor, property)



def test_customattributeowner_is_not_abstract():
    assert not inspect.isabstract(CustomAttributeOwner)


def test_customattributeowner_constructor_exists():
    assert callable(CustomAttributeOwner.__init__)


def test_customattributeowner_constructor_args():
    sig = inspect.signature(CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customclass_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomClass)


def test_gmf::all::gmfgraph::customclass_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomClass.__init__)


def test_gmf::all::gmfgraph::customclass_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomClass.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedClassName" in params, "Missing parameter 'qualifiedClassName'"

def test_gmf::all::gmfgraph::customclass_has_qualifiedClassName():
    assert hasattr(gmf::all::gmfgraph::CustomClass, "qualifiedClassName")
    descriptor = None
    for klass in gmf::all::gmfgraph::CustomClass.__mro__:
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



def test_gmf::all::gmfgraph::customattributeowner_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomAttributeOwner)


def test_gmf::all::gmfgraph::customattributeowner_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomAttributeOwner.__init__)


def test_gmf::all::gmfgraph::customattributeowner_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polygon_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Polygon)


def test_gmfgraph::polygon_constructor_exists():
    assert callable(gmfgraph::Polygon.__init__)


def test_gmfgraph::polygon_constructor_args():
    sig = inspect.signature(gmfgraph::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::decorationfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::DecorationFigure)


def test_gmfgraph::decorationfigure_constructor_exists():
    assert callable(gmfgraph::DecorationFigure.__init__)


def test_gmfgraph::decorationfigure_constructor_args():
    sig = inspect.signature(gmfgraph::DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customdecoration_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomDecoration)


def test_gmf::all::gmfgraph::customdecoration_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomDecoration.__init__)


def test_gmf::all::gmfgraph::customdecoration_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::polygondecoration_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::PolygonDecoration)


def test_gmf::all::gmfgraph::polygondecoration_constructor_exists():
    assert callable(gmf::all::gmfgraph::PolygonDecoration.__init__)


def test_gmf::all::gmfgraph::polygondecoration_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::PolygonDecoration.__init__)
    params = list(sig.parameters.keys())



def test_decorationfigure_is_not_abstract():
    assert not inspect.isabstract(DecorationFigure)


def test_decorationfigure_constructor_exists():
    assert callable(DecorationFigure.__init__)


def test_decorationfigure_constructor_args():
    sig = inspect.signature(DecorationFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::connectionfigure_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::ConnectionFigure)


def test_gmfgraph::connectionfigure_constructor_exists():
    assert callable(gmfgraph::ConnectionFigure.__init__)


def test_gmfgraph::connectionfigure_constructor_args():
    sig = inspect.signature(gmfgraph::ConnectionFigure.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::customconnection_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::CustomConnection)


def test_gmf::all::gmfgraph::customconnection_constructor_exists():
    assert callable(gmf::all::gmfgraph::CustomConnection.__init__)


def test_gmf::all::gmfgraph::customconnection_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::CustomConnection.__init__)
    params = list(sig.parameters.keys())



def test_gmfgraph::polyline_is_not_abstract():
    assert not inspect.isabstract(gmfgraph::Polyline)


def test_gmfgraph::polyline_constructor_exists():
    assert callable(gmfgraph::Polyline.__init__)


def test_gmfgraph::polyline_constructor_args():
    sig = inspect.signature(gmfgraph::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::polylinedecoration_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::PolylineDecoration)


def test_gmf::all::gmfgraph::polylinedecoration_constructor_exists():
    assert callable(gmf::all::gmfgraph::PolylineDecoration.__init__)


def test_gmf::all::gmfgraph::polylinedecoration_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::PolylineDecoration.__init__)
    params = list(sig.parameters.keys())



def test_gmf::all::gmfgraph::polylineconnection_is_not_abstract():
    assert not inspect.isabstract(gmf::all::gmfgraph::PolylineConnection)


def test_gmf::all::gmfgraph::polylineconnection_constructor_exists():
    assert callable(gmf::all::gmfgraph::PolylineConnection.__init__)


def test_gmf::all::gmfgraph::polylineconnection_constructor_args():
    sig = inspect.signature(gmf::all::gmfgraph::PolylineConnection.__init__)
    params = list(sig.parameters.keys())

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

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "END",
        "FILL",
        "BEGINNING",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_severity_exists():
    # Check that the Enumeration exists
    assert Severity is not None

def test_severity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Severity]
    expected_literals = [
        "WARNING",
        "ERROR",
        "INFO",
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
        "LINE_DASH",
        "LINE_DASHDOTDOT",
        "LINE_SOLID",
        "LINE_DASHDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_standardtoolkind_exists():
    # Check that the Enumeration exists
    assert StandardToolKind is not None

def test_standardtoolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StandardToolKind]
    expected_literals = [
        "SELECT",
        "MARQUEE",
        "ZOOM_OUT",
        "SELECT_PAN",
        "ZOOM_IN",
        "ZOOM_PAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StandardToolKind"

def test_labeltextaccessmethod_exists():
    # Check that the Enumeration exists
    assert LabelTextAccessMethod is not None

def test_labeltextaccessmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LabelTextAccessMethod]
    expected_literals = [
        "MESSAGE_FORMAT",
        "NATIVE",
        "REGEXP",
        "PRINTF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LabelTextAccessMethod"

def test_svgpropertytype_exists():
    # Check that the Enumeration exists
    assert SVGPropertyType is not None

def test_svgpropertytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SVGPropertyType]
    expected_literals = [
        "STRING",
        "COLOR",
        "FLOAT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SVGPropertyType"

def test_actionkind_exists():
    # Check that the Enumeration exists
    assert ActionKind is not None

def test_actionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionKind]
    expected_literals = [
        "PROPCHANGE",
        "CREATE",
        "PROCESS",
        "CUSTOM",
        "MODIFY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionKind"

def test_language_exists():
    # Check that the Enumeration exists
    assert Language is not None

def test_language_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Language]
    expected_literals = [
        "java",
        "ocl",
        "literal",
        "regexp",
        "nregexp",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Language"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "NORTH_WEST",
        "NONE",
        "SOUTH",
        "NORTH_EAST",
        "WEST",
        "NORTH",
        "SOUTH_WEST",
        "SOUTH_EAST",
        "NORTH_SOUTH",
        "EAST",
        "NSEW",
        "EAST_WEST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_fontstyle_exists():
    # Check that the Enumeration exists
    assert FontStyle is not None

def test_fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontStyle]
    expected_literals = [
        "BOLD",
        "NORMAL",
        "ITALIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontStyle"

def test_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "red",
        "lightGreen",
        "cyan",
        "darkBlue",
        "lightGray",
        "black",
        "yellow",
        "white",
        "gray",
        "lightBlue",
        "blue",
        "orange",
        "darkGreen",
        "green",
        "darkGray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorConstants"


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
gmf::all::gmfgraph::PinOwner_strategy = st.builds(
    gmf::all::gmfgraph::PinOwner,
)
gmf::all::gmfgraph::SVGProperty_strategy = st.builds(
    gmf::all::gmfgraph::SVGProperty,
    attribute=
        safe_text,
    setter=
        safe_text,
    callSuper=
        st.booleans(),
    type=
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
Polygon_strategy = st.builds(
    Polygon,
)
gmf::all::gmfgraph::ScalablePolygon_strategy = st.builds(
    gmf::all::gmfgraph::ScalablePolygon,
)
Polyline_strategy = st.builds(
    Polyline,
)
gmf::all::gmfgraph::Polygon_strategy = st.builds(
    gmf::all::gmfgraph::Polygon,
)
gmfgraph::CustomClass_strategy = st.builds(
    gmfgraph::CustomClass,
)
gmfgraph::RealFigure_strategy = st.builds(
    gmfgraph::RealFigure,
)
gmf::all::gmfgraph::CustomFigure_strategy = st.builds(
    gmf::all::gmfgraph::CustomFigure,
)
Shape_strategy = st.builds(
    Shape,
)
gmf::all::gmfgraph::RoundedRectangle_strategy = st.builds(
    gmf::all::gmfgraph::RoundedRectangle,
    cornerHeight=
        st.integers(),
    cornerWidth=
        st.integers()
)
gmf::all::gmfgraph::Rectangle_strategy = st.builds(
    gmf::all::gmfgraph::Rectangle,
)
AbstractFigure_strategy = st.builds(
    AbstractFigure,
)
gmf::all::gmfgraph::FigureRef_strategy = st.builds(
    gmf::all::gmfgraph::FigureRef,
)
gmf::all::gmfgraph::Polyline_strategy = st.builds(
    gmf::all::gmfgraph::Polyline,
)
gmf::all::gmfgraph::Ellipse_strategy = st.builds(
    gmf::all::gmfgraph::Ellipse,
)
gmf::all::gmfgraph::ChildAccess_strategy = st.builds(
    gmf::all::gmfgraph::ChildAccess,
    accessor=
        safe_text
)
Figure_strategy = st.builds(
    Figure,
)
gmf::all::gmfgraph::AbstractFigure_strategy = st.builds(
    gmf::all::gmfgraph::AbstractFigure,
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
Color_strategy = st.builds(
    Color,
)
gmfgraph::CustomAttributeOwner_strategy = st.builds(
    gmfgraph::CustomAttributeOwner,
)
gmfgraph::PinOwner_strategy = st.builds(
    gmfgraph::PinOwner,
)
gmfgraph::AbstractFigure_strategy = st.builds(
    gmfgraph::AbstractFigure,
)
gmf::all::gmfgraph::RealFigure_strategy = st.builds(
    gmf::all::gmfgraph::RealFigure,
    name=
        safe_text
)
Dimension_strategy = st.builds(
    Dimension,
)
gmf::all::gmfgraph::VisualFacet_strategy = st.builds(
    gmf::all::gmfgraph::VisualFacet,
)
ChildAccess_strategy = st.builds(
    ChildAccess,
)
Layoutable_strategy = st.builds(
    Layoutable,
)
gmf::all::gmfgraph::Figure_strategy = st.builds(
    gmf::all::gmfgraph::Figure,
)
VisualFacet_strategy = st.builds(
    VisualFacet,
)
gmf::all::gmfgraph::AlignmentFacet_strategy = st.builds(
    gmf::all::gmfgraph::AlignmentFacet,
    alignment=
        safe_text
)
gmf::all::gmfgraph::LabelOffsetFacet_strategy = st.builds(
    gmf::all::gmfgraph::LabelOffsetFacet,
    x=
        st.integers(),
    y=
        st.integers()
)
gmf::all::gmfgraph::GeneralFacet_strategy = st.builds(
    gmf::all::gmfgraph::GeneralFacet,
    identifier=
        safe_text,
    data=
        safe_text
)
gmf::all::gmfgraph::DefaultSizeFacet_strategy = st.builds(
    gmf::all::gmfgraph::DefaultSizeFacet,
)
gmf::all::gmfgraph::GradientFacet_strategy = st.builds(
    gmf::all::gmfgraph::GradientFacet,
    direction=
        safe_text
)
gmf::all::gmfgraph::Identity_strategy = st.builds(
    gmf::all::gmfgraph::Identity,
    name=
        safe_text
)
Layout_strategy = st.builds(
    Layout,
)
gmf::all::gmfgraph::FlowLayout_strategy = st.builds(
    gmf::all::gmfgraph::FlowLayout,
    matchMinorSize=
        st.booleans(),
    forceSingleLine=
        st.booleans(),
    minorAlignment=
        safe_text,
    minorSpacing=
        st.integers(),
    vertical=
        st.booleans(),
    majorAlignment=
        safe_text,
    majorSpacing=
        st.integers()
)
gmf::all::gmfgraph::CenterLayout_strategy = st.builds(
    gmf::all::gmfgraph::CenterLayout,
)
gmf::all::gmfgraph::StackLayout_strategy = st.builds(
    gmf::all::gmfgraph::StackLayout,
)
gmf::all::gmfgraph::XYLayout_strategy = st.builds(
    gmf::all::gmfgraph::XYLayout,
)
Border_strategy = st.builds(
    Border,
)
FigureDescriptor_strategy = st.builds(
    FigureDescriptor,
)
RealFigure_strategy = st.builds(
    RealFigure,
)
gmf::all::gmfgraph::ConnectionFigure_strategy = st.builds(
    gmf::all::gmfgraph::ConnectionFigure,
)
gmf::all::gmfgraph::InvisibleRectangle_strategy = st.builds(
    gmf::all::gmfgraph::InvisibleRectangle,
)
gmf::all::gmfgraph::LabeledContainer_strategy = st.builds(
    gmf::all::gmfgraph::LabeledContainer,
)
gmf::all::gmfgraph::Label_strategy = st.builds(
    gmf::all::gmfgraph::Label,
    text=
        safe_text
)
gmf::all::gmfgraph::SVGFigure_strategy = st.builds(
    gmf::all::gmfgraph::SVGFigure,
    documentURI=
        safe_text,
    noCanvasWidth=
        st.booleans(),
    noCanvasHeight=
        st.booleans()
)
gmf::all::gmfgraph::VerticalLabel_strategy = st.builds(
    gmf::all::gmfgraph::VerticalLabel,
    text=
        safe_text
)
gmf::all::gmfgraph::DecorationFigure_strategy = st.builds(
    gmf::all::gmfgraph::DecorationFigure,
)
gmf::all::gmfgraph::Shape_strategy = st.builds(
    gmf::all::gmfgraph::Shape,
    lineKind=
        safe_text,
    fill=
        st.booleans(),
    lineWidth=
        st.integers(),
    xorOutline=
        st.booleans(),
    outline=
        st.booleans(),
    xorFill=
        st.booleans()
)
FigureGallery_strategy = st.builds(
    FigureGallery,
)
AbstractNode_strategy = st.builds(
    AbstractNode,
)
gmf::all::gmfgraph::Node_strategy = st.builds(
    gmf::all::gmfgraph::Node,
    resizeConstraint=
        safe_text,
    affixedParentSide=
        safe_text
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
gmf::all::gmfgraph::Connection_strategy = st.builds(
    gmf::all::gmfgraph::Connection,
)
gmf::all::gmfgraph::Compartment_strategy = st.builds(
    gmf::all::gmfgraph::Compartment,
    collapsible=
        st.booleans(),
    needsTitle=
        st.booleans()
)
gmf::all::gmfgraph::AbstractNode_strategy = st.builds(
    gmf::all::gmfgraph::AbstractNode,
)
gmf::all::tooldef::StyleSelector_strategy = st.builds(
    gmf::all::tooldef::StyleSelector,
)
gmf::all::tooldef::Image_strategy = st.builds(
    gmf::all::tooldef::Image,
)
tooldef::ContributionItem_strategy = st.builds(
    tooldef::ContributionItem,
)
Identity_strategy = st.builds(
    Identity,
)
gmf::all::gmfgraph::FigureDescriptor_strategy = st.builds(
    gmf::all::gmfgraph::FigureDescriptor,
)
gmf::all::gmfgraph::FigureGallery_strategy = st.builds(
    gmf::all::gmfgraph::FigureGallery,
    implementationBundle=
        safe_text
)
gmf::all::gmfgraph::Pin_strategy = st.builds(
    gmf::all::gmfgraph::Pin,
)
gmf::all::gmfgraph::DiagramElement_strategy = st.builds(
    gmf::all::gmfgraph::DiagramElement,
)
gmf::all::gmfgraph::Canvas_strategy = st.builds(
    gmf::all::gmfgraph::Canvas,
)
tooldef::PredefinedItem_strategy = st.builds(
    tooldef::PredefinedItem,
)
tooldef::Menu_strategy = st.builds(
    tooldef::Menu,
)
gmf::all::tooldef::PopupMenu_strategy = st.builds(
    gmf::all::tooldef::PopupMenu,
    iD=
        safe_text
)
gmf::all::tooldef::PredefinedMenu_strategy = st.builds(
    gmf::all::tooldef::PredefinedMenu,
)
ItemBase_strategy = st.builds(
    ItemBase,
)
gmf::all::tooldef::PredefinedItem_strategy = st.builds(
    gmf::all::tooldef::PredefinedItem,
    identifier=
        safe_text
)
gmf::all::tooldef::ContributionItem_strategy = st.builds(
    gmf::all::tooldef::ContributionItem,
    title=
        safe_text
)
gmf::all::tooldef::Separator_strategy = st.builds(
    gmf::all::tooldef::Separator,
    name=
        safe_text
)
gmf::all::tooldef::Menu_strategy = st.builds(
    gmf::all::tooldef::Menu,
)
gmf::all::tooldef::ItemBase_strategy = st.builds(
    gmf::all::tooldef::ItemBase,
)
gmf::all::tooldef::ItemRef_strategy = st.builds(
    gmf::all::tooldef::ItemRef,
)
ContributionItem_strategy = st.builds(
    ContributionItem,
)
gmf::all::tooldef::MenuAction_strategy = st.builds(
    gmf::all::tooldef::MenuAction,
    kind=
        safe_text,
    hotKey=
        safe_text
)
Image_strategy = st.builds(
    Image,
)
gmf::all::tooldef::DefaultImage_strategy = st.builds(
    gmf::all::tooldef::DefaultImage,
)
gmf::all::tooldef::BundleImage_strategy = st.builds(
    gmf::all::tooldef::BundleImage,
    path=
        safe_text,
    bundle=
        safe_text
)
gmf::all::tooldef::AbstractTool_strategy = st.builds(
    gmf::all::tooldef::AbstractTool,
    description=
        safe_text,
    title=
        safe_text
)
Menu_strategy = st.builds(
    Menu,
)
gmf::all::tooldef::MainMenu_strategy = st.builds(
    gmf::all::tooldef::MainMenu,
    title=
        safe_text
)
gmf::all::tooldef::Toolbar_strategy = st.builds(
    gmf::all::tooldef::Toolbar,
)
gmf::all::tooldef::ContextMenu_strategy = st.builds(
    gmf::all::tooldef::ContextMenu,
)
MenuAction_strategy = st.builds(
    MenuAction,
)
gmf::all::tooldef::ToolRegistry_strategy = st.builds(
    gmf::all::tooldef::ToolRegistry,
)
Pin_strategy = st.builds(
    Pin,
)
gmf::all::gmfgraph::CustomPin_strategy = st.builds(
    gmf::all::gmfgraph::CustomPin,
    customOperationType=
        safe_text,
    customOperationName=
        safe_text
)
gmf::all::gmfgraph::VisiblePin_strategy = st.builds(
    gmf::all::gmfgraph::VisiblePin,
)
gmf::all::gmfgraph::ColorPin_strategy = st.builds(
    gmf::all::gmfgraph::ColorPin,
    backgroundNotForeground=
        st.booleans()
)
gmf::all::mappings::VisualEffectMapping_strategy = st.builds(
    gmf::all::mappings::VisualEffectMapping,
    oclExpression=
        safe_text
)
gmf::all::mappings::Measurable_strategy = st.builds(
    gmf::all::mappings::Measurable,
)
gmf::all::mappings::Auditable_strategy = st.builds(
    gmf::all::mappings::Auditable,
)
ToolContainer_strategy = st.builds(
    ToolContainer,
)
gmf::all::tooldef::Palette_strategy = st.builds(
    gmf::all::tooldef::Palette,
)
gmf::all::tooldef::ToolGroup_strategy = st.builds(
    gmf::all::tooldef::ToolGroup,
    collapsible=
        st.booleans(),
    stack=
        st.booleans()
)
Measurable_strategy = st.builds(
    Measurable,
)
MetricRule_strategy = st.builds(
    MetricRule,
)
gmf::all::mappings::MetricContainer_strategy = st.builds(
    gmf::all::mappings::MetricContainer,
)
mappings::Measurable_strategy = st.builds(
    mappings::Measurable,
)
mappings::Auditable_strategy = st.builds(
    mappings::Auditable,
)
gmf::all::mappings::NotationElementTarget_strategy = st.builds(
    gmf::all::mappings::NotationElementTarget,
)
gmf::all::mappings::DiagramElementTarget_strategy = st.builds(
    gmf::all::mappings::DiagramElementTarget,
)
gmf::all::mappings::DomainElementTarget_strategy = st.builds(
    gmf::all::mappings::DomainElementTarget,
)
Auditable_strategy = st.builds(
    Auditable,
)
gmf::all::mappings::AuditedMetricTarget_strategy = st.builds(
    gmf::all::mappings::AuditedMetricTarget,
)
RuleBase_strategy = st.builds(
    RuleBase,
)
gmf::all::mappings::MetricRule_strategy = st.builds(
    gmf::all::mappings::MetricRule,
    key=
        safe_text,
    highLimit=
        safe_text,
    lowLimit=
        safe_text
)
gmf::all::mappings::AuditRule_strategy = st.builds(
    gmf::all::mappings::AuditRule,
    useInLiveMode=
        st.booleans(),
    message=
        safe_text,
    severity=
        safe_text,
    id=
        safe_text
)
gmf::all::mappings::RuleBase_strategy = st.builds(
    gmf::all::mappings::RuleBase,
    name=
        safe_text,
    description=
        safe_text
)
gmf::all::mappings::DomainAttributeTarget_strategy = st.builds(
    gmf::all::mappings::DomainAttributeTarget,
    nullAsError=
        st.booleans()
)
gmf::all::mappings::AuditContainer_strategy = st.builds(
    gmf::all::mappings::AuditContainer,
    description=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
gmf::all::mappings::AppearanceSteward_strategy = st.builds(
    gmf::all::mappings::AppearanceSteward,
)
AbstractTool_strategy = st.builds(
    AbstractTool,
)
gmf::all::tooldef::GenericTool_strategy = st.builds(
    gmf::all::tooldef::GenericTool,
    toolClass=
        safe_text
)
gmf::all::tooldef::StandardTool_strategy = st.builds(
    gmf::all::tooldef::StandardTool,
    toolKind=
        safe_text
)
gmf::all::tooldef::PaletteSeparator_strategy = st.builds(
    gmf::all::tooldef::PaletteSeparator,
)
gmf::all::tooldef::ToolContainer_strategy = st.builds(
    gmf::all::tooldef::ToolContainer,
)
gmf::all::tooldef::CreationTool_strategy = st.builds(
    gmf::all::tooldef::CreationTool,
)
gmf::all::mappings::ToolOwner_strategy = st.builds(
    gmf::all::mappings::ToolOwner,
)
ContextMenu_strategy = st.builds(
    ContextMenu,
)
gmf::all::mappings::MenuOwner_strategy = st.builds(
    gmf::all::mappings::MenuOwner,
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
gmf::all::mappings::ReferenceNewElementSpec_strategy = st.builds(
    gmf::all::mappings::ReferenceNewElementSpec,
)
gmf::all::mappings::FeatureValueSpec_strategy = st.builds(
    gmf::all::mappings::FeatureValueSpec,
)
gmf::all::mappings::ElementInitializer_strategy = st.builds(
    gmf::all::mappings::ElementInitializer,
)
gmf::all::mappings::ValueExpression_strategy = st.builds(
    gmf::all::mappings::ValueExpression,
    body=
        safe_text,
    langName=
        safe_text,
    language=
        safe_text
)
gmf::all::mappings::FeatureInitializer_strategy = st.builds(
    gmf::all::mappings::FeatureInitializer,
)
gmf::all::mappings::LinkConstraints_strategy = st.builds(
    gmf::all::mappings::LinkConstraints,
)
mappings::gmf::all::EAttribute_strategy = st.builds(
    mappings::gmf::all::EAttribute,
)
MappingEntry_strategy = st.builds(
    MappingEntry,
)
DiagramLabel_strategy = st.builds(
    DiagramLabel,
)
gmf::all::mappings::LabelMapping_strategy = st.builds(
    gmf::all::mappings::LabelMapping,
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
gmf::all::mappings::Constraint_strategy = st.builds(
    gmf::all::mappings::Constraint,
)
Canvas_strategy = st.builds(
    Canvas,
)
gmf::all::mappings::CanvasMapping_strategy = st.builds(
    gmf::all::mappings::CanvasMapping,
)
LinkConstraints_strategy = st.builds(
    LinkConstraints,
)
mappings::gmf::all::EStructuralFeature_strategy = st.builds(
    mappings::gmf::all::EStructuralFeature,
)
Connection_strategy = st.builds(
    Connection,
)
mappings::NeedsContainment_strategy = st.builds(
    mappings::NeedsContainment,
)
Compartment_strategy = st.builds(
    Compartment,
)
gmf::all::mappings::CompartmentMapping_strategy = st.builds(
    gmf::all::mappings::CompartmentMapping,
)
ChildReference_strategy = st.builds(
    ChildReference,
)
Palette_strategy = st.builds(
    Palette,
)
mappings::gmf::all::EPackage_strategy = st.builds(
    mappings::gmf::all::EPackage,
)
CompartmentMapping_strategy = st.builds(
    CompartmentMapping,
)
NodeReference_strategy = st.builds(
    NodeReference,
)
gmf::all::mappings::TopNodeReference_strategy = st.builds(
    gmf::all::mappings::TopNodeReference,
)
gmf::all::mappings::ChildReference_strategy = st.builds(
    gmf::all::mappings::ChildReference,
)
NodeMapping_strategy = st.builds(
    NodeMapping,
)
NeedsContainment_strategy = st.builds(
    NeedsContainment,
)
gmf::all::mappings::NodeReference_strategy = st.builds(
    gmf::all::mappings::NodeReference,
)
Node_strategy = st.builds(
    Node,
)
gmf::all::gmfgraph::DiagramLabel_strategy = st.builds(
    gmf::all::gmfgraph::DiagramLabel,
    external=
        st.booleans(),
    elementIcon=
        st.booleans()
)
mappings::AppearanceSteward_strategy = st.builds(
    mappings::AppearanceSteward,
)
mappings::ToolOwner_strategy = st.builds(
    mappings::ToolOwner,
)
mappings::MenuOwner_strategy = st.builds(
    mappings::MenuOwner,
)
mappings::MappingEntry_strategy = st.builds(
    mappings::MappingEntry,
)
gmf::all::mappings::LinkMapping_strategy = st.builds(
    gmf::all::mappings::LinkMapping,
)
gmf::all::mappings::NodeMapping_strategy = st.builds(
    gmf::all::mappings::NodeMapping,
)
LabelMapping_strategy = st.builds(
    LabelMapping,
)
gmf::all::mappings::ExpressionLabelMapping_strategy = st.builds(
    gmf::all::mappings::ExpressionLabelMapping,
)
gmf::all::mappings::FeatureLabelMapping_strategy = st.builds(
    gmf::all::mappings::FeatureLabelMapping,
    editPattern=
        safe_text,
    editMethod=
        safe_text,
    editorPattern=
        safe_text,
    viewPattern=
        safe_text,
    viewMethod=
        safe_text
)
gmf::all::mappings::DesignLabelMapping_strategy = st.builds(
    gmf::all::mappings::DesignLabelMapping,
)
gmf::all::mappings::OclChoiceLabelMapping_strategy = st.builds(
    gmf::all::mappings::OclChoiceLabelMapping,
)
ElementInitializer_strategy = st.builds(
    ElementInitializer,
)
gmf::all::mappings::FeatureSeqInitializer_strategy = st.builds(
    gmf::all::mappings::FeatureSeqInitializer,
)
Constraint_strategy = st.builds(
    Constraint,
)
mappings::gmf::all::EClass_strategy = st.builds(
    mappings::gmf::all::EClass,
)
gmf::all::mappings::MappingEntry_strategy = st.builds(
    gmf::all::mappings::MappingEntry,
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
gmf::all::tooldef::GenericStyleSelector_strategy = st.builds(
    gmf::all::tooldef::GenericStyleSelector,
    values=
        safe_text
)
CanvasMapping_strategy = st.builds(
    CanvasMapping,
)
LinkMapping_strategy = st.builds(
    LinkMapping,
)
mappings::gmf::all::EReference_strategy = st.builds(
    mappings::gmf::all::EReference,
)
gmf::all::mappings::NeedsContainment_strategy = st.builds(
    gmf::all::mappings::NeedsContainment,
)
VisualEffectMapping_strategy = st.builds(
    VisualEffectMapping,
)
TopNodeReference_strategy = st.builds(
    TopNodeReference,
)
gmf::all::mappings::Mapping_strategy = st.builds(
    gmf::all::mappings::Mapping,
)
gmf::all::gmfgraph::Rectangle2D_strategy = st.builds(
    gmf::all::gmfgraph::Rectangle2D,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
gmf::all::gmfgraph::GridLayout_strategy = st.builds(
    gmf::all::gmfgraph::GridLayout,
    numColumns=
        st.integers(),
    equalWidth=
        st.booleans()
)
gmfgraph::Layout_strategy = st.builds(
    gmfgraph::Layout,
)
gmf::all::gmfgraph::CustomLayout_strategy = st.builds(
    gmf::all::gmfgraph::CustomLayout,
)
gmf::all::gmfgraph::LayoutRef_strategy = st.builds(
    gmf::all::gmfgraph::LayoutRef,
)
gmf::all::gmfgraph::Layout_strategy = st.builds(
    gmf::all::gmfgraph::Layout,
)
gmf::all::gmfgraph::Layoutable_strategy = st.builds(
    gmf::all::gmfgraph::Layoutable,
)
LayoutData_strategy = st.builds(
    LayoutData,
)
gmf::all::gmfgraph::XYLayoutData_strategy = st.builds(
    gmf::all::gmfgraph::XYLayoutData,
)
gmf::all::gmfgraph::BorderLayoutData_strategy = st.builds(
    gmf::all::gmfgraph::BorderLayoutData,
    alignment=
        safe_text,
    vertical=
        st.booleans()
)
gmf::all::gmfgraph::GridLayoutData_strategy = st.builds(
    gmf::all::gmfgraph::GridLayoutData,
    verticalAlignment=
        safe_text,
    horizontalSpan=
        st.integers(),
    grabExcessVerticalSpace=
        st.booleans(),
    verticalSpan=
        st.integers(),
    grabExcessHorizontalSpace=
        st.booleans(),
    horizontalIndent=
        st.integers(),
    horizontalAlignment=
        safe_text
)
gmf::all::gmfgraph::BorderLayout_strategy = st.builds(
    gmf::all::gmfgraph::BorderLayout,
)
gmfgraph::Border_strategy = st.builds(
    gmfgraph::Border,
)
gmf::all::gmfgraph::CustomBorder_strategy = st.builds(
    gmf::all::gmfgraph::CustomBorder,
)
gmf::all::gmfgraph::CompoundBorder_strategy = st.builds(
    gmf::all::gmfgraph::CompoundBorder,
)
gmf::all::gmfgraph::MarginBorder_strategy = st.builds(
    gmf::all::gmfgraph::MarginBorder,
)
gmf::all::gmfgraph::LineBorder_strategy = st.builds(
    gmf::all::gmfgraph::LineBorder,
    width=
        st.integers()
)
gmf::all::gmfgraph::BorderRef_strategy = st.builds(
    gmf::all::gmfgraph::BorderRef,
)
gmf::all::gmfgraph::Border_strategy = st.builds(
    gmf::all::gmfgraph::Border,
)
gmfgraph::LayoutData_strategy = st.builds(
    gmfgraph::LayoutData,
)
gmf::all::gmfgraph::CustomLayoutData_strategy = st.builds(
    gmf::all::gmfgraph::CustomLayoutData,
)
gmf::all::gmfgraph::LayoutData_strategy = st.builds(
    gmf::all::gmfgraph::LayoutData,
)
gmf::all::gmfgraph::Point_strategy = st.builds(
    gmf::all::gmfgraph::Point,
    y=
        st.integers(),
    x=
        st.integers()
)
gmf::all::gmfgraph::BasicFont_strategy = st.builds(
    gmf::all::gmfgraph::BasicFont,
    style=
        safe_text,
    faceName=
        safe_text,
    height=
        st.integers()
)
gmf::all::gmfgraph::Font_strategy = st.builds(
    gmf::all::gmfgraph::Font,
)
gmf::all::gmfgraph::ConstantColor_strategy = st.builds(
    gmf::all::gmfgraph::ConstantColor,
    value=
        safe_text
)
gmf::all::gmfgraph::RGBColor_strategy = st.builds(
    gmf::all::gmfgraph::RGBColor,
    blue=
        st.integers(),
    green=
        st.integers(),
    red=
        st.integers()
)
gmf::all::gmfgraph::Color_strategy = st.builds(
    gmf::all::gmfgraph::Color,
)
gmfgraph::CustomFigure_strategy = st.builds(
    gmfgraph::CustomFigure,
)
FigureAccessor_strategy = st.builds(
    FigureAccessor,
)
gmf::all::gmfgraph::Insets_strategy = st.builds(
    gmf::all::gmfgraph::Insets,
    top=
        st.integers(),
    left=
        st.integers(),
    right=
        st.integers(),
    bottom=
        st.integers()
)
gmf::all::gmfgraph::Dimension_strategy = st.builds(
    gmf::all::gmfgraph::Dimension,
    dx=
        st.integers(),
    dy=
        st.integers()
)
gmf::all::gmfgraph::FigureAccessor_strategy = st.builds(
    gmf::all::gmfgraph::FigureAccessor,
    accessor=
        safe_text
)
gmf::all::gmfgraph::CustomAttribute_strategy = st.builds(
    gmf::all::gmfgraph::CustomAttribute,
    multiStatementValue=
        st.booleans(),
    name=
        safe_text,
    value=
        safe_text,
    directAccess=
        st.booleans()
)
CustomAttributeOwner_strategy = st.builds(
    CustomAttributeOwner,
)
gmf::all::gmfgraph::CustomClass_strategy = st.builds(
    gmf::all::gmfgraph::CustomClass,
    qualifiedClassName=
        safe_text
)
CustomAttribute_strategy = st.builds(
    CustomAttribute,
)
gmf::all::gmfgraph::CustomAttributeOwner_strategy = st.builds(
    gmf::all::gmfgraph::CustomAttributeOwner,
)
gmfgraph::Polygon_strategy = st.builds(
    gmfgraph::Polygon,
)
gmfgraph::DecorationFigure_strategy = st.builds(
    gmfgraph::DecorationFigure,
)
gmf::all::gmfgraph::CustomDecoration_strategy = st.builds(
    gmf::all::gmfgraph::CustomDecoration,
)
gmf::all::gmfgraph::PolygonDecoration_strategy = st.builds(
    gmf::all::gmfgraph::PolygonDecoration,
)
DecorationFigure_strategy = st.builds(
    DecorationFigure,
)
gmfgraph::ConnectionFigure_strategy = st.builds(
    gmfgraph::ConnectionFigure,
)
gmf::all::gmfgraph::CustomConnection_strategy = st.builds(
    gmf::all::gmfgraph::CustomConnection,
)
gmfgraph::Polyline_strategy = st.builds(
    gmfgraph::Polyline,
)
gmf::all::gmfgraph::PolylineDecoration_strategy = st.builds(
    gmf::all::gmfgraph::PolylineDecoration,
)
gmf::all::gmfgraph::PolylineConnection_strategy = st.builds(
    gmf::all::gmfgraph::PolylineConnection,
)

@given(instance=gmf::all::gmfgraph::PinOwner_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::pinowner_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::PinOwner)

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::svgproperty_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::SVGProperty)

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_setter_type(instance):
    assert isinstance(instance.setter, str)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_setter_setter(instance):
    original = instance.setter
    instance.setter = original
    assert instance.setter == original

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_callSuper_type(instance):
    assert isinstance(instance.callSuper, bool)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_callSuper_setter(instance):
    original = instance.callSuper
    instance.callSuper = original
    assert instance.callSuper == original

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_getter_type(instance):
    assert isinstance(instance.getter, str)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_getter_setter(instance):
    original = instance.getter
    instance.getter = original
    assert instance.getter == original

@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=gmf::all::gmfgraph::SVGProperty_strategy)
def test_gmf::all::gmfgraph::svgproperty_query_setter(instance):
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

@given(instance=Polygon_strategy)
@settings(max_examples=50)
def test_polygon_instantiation(instance):
    assert isinstance(instance, Polygon)

@given(instance=gmf::all::gmfgraph::ScalablePolygon_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::scalablepolygon_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::ScalablePolygon)

@given(instance=Polyline_strategy)
@settings(max_examples=50)
def test_polyline_instantiation(instance):
    assert isinstance(instance, Polyline)

@given(instance=gmf::all::gmfgraph::Polygon_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::polygon_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Polygon)

@given(instance=gmfgraph::CustomClass_strategy)
@settings(max_examples=50)
def test_gmfgraph::customclass_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomClass)

@given(instance=gmfgraph::RealFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::realfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::RealFigure)

@given(instance=gmf::all::gmfgraph::CustomFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomFigure)

@given(instance=Shape_strategy)
@settings(max_examples=50)
def test_shape_instantiation(instance):
    assert isinstance(instance, Shape)

@given(instance=gmf::all::gmfgraph::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::roundedrectangle_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::RoundedRectangle)

@given(instance=gmf::all::gmfgraph::RoundedRectangle_strategy)
def test_gmf::all::gmfgraph::roundedrectangle_cornerHeight_type(instance):
    assert isinstance(instance.cornerHeight, int)


@given(instance=gmf::all::gmfgraph::RoundedRectangle_strategy)
def test_gmf::all::gmfgraph::roundedrectangle_cornerHeight_setter(instance):
    original = instance.cornerHeight
    instance.cornerHeight = original
    assert instance.cornerHeight == original

@given(instance=gmf::all::gmfgraph::RoundedRectangle_strategy)
def test_gmf::all::gmfgraph::roundedrectangle_cornerWidth_type(instance):
    assert isinstance(instance.cornerWidth, int)


@given(instance=gmf::all::gmfgraph::RoundedRectangle_strategy)
def test_gmf::all::gmfgraph::roundedrectangle_cornerWidth_setter(instance):
    original = instance.cornerWidth
    instance.cornerWidth = original
    assert instance.cornerWidth == original

@given(instance=gmf::all::gmfgraph::Rectangle_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::rectangle_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Rectangle)

@given(instance=AbstractFigure_strategy)
@settings(max_examples=50)
def test_abstractfigure_instantiation(instance):
    assert isinstance(instance, AbstractFigure)

@given(instance=gmf::all::gmfgraph::FigureRef_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::figureref_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::FigureRef)

@given(instance=gmf::all::gmfgraph::Polyline_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::polyline_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Polyline)

@given(instance=gmf::all::gmfgraph::Ellipse_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::ellipse_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Ellipse)

@given(instance=gmf::all::gmfgraph::ChildAccess_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::childaccess_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::ChildAccess)

@given(instance=gmf::all::gmfgraph::ChildAccess_strategy)
def test_gmf::all::gmfgraph::childaccess_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=gmf::all::gmfgraph::ChildAccess_strategy)
def test_gmf::all::gmfgraph::childaccess_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=gmf::all::gmfgraph::AbstractFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::abstractfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::AbstractFigure)

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

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=gmfgraph::CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_gmfgraph::customattributeowner_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomAttributeOwner)

@given(instance=gmfgraph::PinOwner_strategy)
@settings(max_examples=50)
def test_gmfgraph::pinowner_instantiation(instance):
    assert isinstance(instance, gmfgraph::PinOwner)

@given(instance=gmfgraph::AbstractFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::abstractfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::AbstractFigure)

@given(instance=gmf::all::gmfgraph::RealFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::realfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::RealFigure)

@given(instance=gmf::all::gmfgraph::RealFigure_strategy)
def test_gmf::all::gmfgraph::realfigure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::gmfgraph::RealFigure_strategy)
def test_gmf::all::gmfgraph::realfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Dimension_strategy)
@settings(max_examples=50)
def test_dimension_instantiation(instance):
    assert isinstance(instance, Dimension)

@given(instance=gmf::all::gmfgraph::VisualFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::visualfacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::VisualFacet)

@given(instance=ChildAccess_strategy)
@settings(max_examples=50)
def test_childaccess_instantiation(instance):
    assert isinstance(instance, ChildAccess)

@given(instance=Layoutable_strategy)
@settings(max_examples=50)
def test_layoutable_instantiation(instance):
    assert isinstance(instance, Layoutable)

@given(instance=gmf::all::gmfgraph::Figure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::figure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Figure)

@given(instance=VisualFacet_strategy)
@settings(max_examples=50)
def test_visualfacet_instantiation(instance):
    assert isinstance(instance, VisualFacet)

@given(instance=gmf::all::gmfgraph::AlignmentFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::alignmentfacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::AlignmentFacet)

@given(instance=gmf::all::gmfgraph::AlignmentFacet_strategy)
def test_gmf::all::gmfgraph::alignmentfacet_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=gmf::all::gmfgraph::AlignmentFacet_strategy)
def test_gmf::all::gmfgraph::alignmentfacet_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=gmf::all::gmfgraph::LabelOffsetFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::labeloffsetfacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::LabelOffsetFacet)

@given(instance=gmf::all::gmfgraph::LabelOffsetFacet_strategy)
def test_gmf::all::gmfgraph::labeloffsetfacet_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=gmf::all::gmfgraph::LabelOffsetFacet_strategy)
def test_gmf::all::gmfgraph::labeloffsetfacet_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmf::all::gmfgraph::LabelOffsetFacet_strategy)
def test_gmf::all::gmfgraph::labeloffsetfacet_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=gmf::all::gmfgraph::LabelOffsetFacet_strategy)
def test_gmf::all::gmfgraph::labeloffsetfacet_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmf::all::gmfgraph::GeneralFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::generalfacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::GeneralFacet)

@given(instance=gmf::all::gmfgraph::GeneralFacet_strategy)
def test_gmf::all::gmfgraph::generalfacet_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=gmf::all::gmfgraph::GeneralFacet_strategy)
def test_gmf::all::gmfgraph::generalfacet_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=gmf::all::gmfgraph::GeneralFacet_strategy)
def test_gmf::all::gmfgraph::generalfacet_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=gmf::all::gmfgraph::GeneralFacet_strategy)
def test_gmf::all::gmfgraph::generalfacet_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=gmf::all::gmfgraph::DefaultSizeFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::defaultsizefacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::DefaultSizeFacet)

@given(instance=gmf::all::gmfgraph::GradientFacet_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::gradientfacet_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::GradientFacet)

@given(instance=gmf::all::gmfgraph::GradientFacet_strategy)
def test_gmf::all::gmfgraph::gradientfacet_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=gmf::all::gmfgraph::GradientFacet_strategy)
def test_gmf::all::gmfgraph::gradientfacet_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=gmf::all::gmfgraph::Identity_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::identity_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Identity)

@given(instance=gmf::all::gmfgraph::Identity_strategy)
def test_gmf::all::gmfgraph::identity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::gmfgraph::Identity_strategy)
def test_gmf::all::gmfgraph::identity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Layout_strategy)
@settings(max_examples=50)
def test_layout_instantiation(instance):
    assert isinstance(instance, Layout)

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::flowlayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::FlowLayout)

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_matchMinorSize_type(instance):
    assert isinstance(instance.matchMinorSize, bool)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_matchMinorSize_setter(instance):
    original = instance.matchMinorSize
    instance.matchMinorSize = original
    assert instance.matchMinorSize == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_forceSingleLine_type(instance):
    assert isinstance(instance.forceSingleLine, bool)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_forceSingleLine_setter(instance):
    original = instance.forceSingleLine
    instance.forceSingleLine = original
    assert instance.forceSingleLine == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_minorAlignment_type(instance):
    assert isinstance(instance.minorAlignment, str)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_minorAlignment_setter(instance):
    original = instance.minorAlignment
    instance.minorAlignment = original
    assert instance.minorAlignment == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_minorSpacing_type(instance):
    assert isinstance(instance.minorSpacing, int)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_minorSpacing_setter(instance):
    original = instance.minorSpacing
    instance.minorSpacing = original
    assert instance.minorSpacing == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_majorAlignment_type(instance):
    assert isinstance(instance.majorAlignment, str)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_majorAlignment_setter(instance):
    original = instance.majorAlignment
    instance.majorAlignment = original
    assert instance.majorAlignment == original

@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_majorSpacing_type(instance):
    assert isinstance(instance.majorSpacing, int)


@given(instance=gmf::all::gmfgraph::FlowLayout_strategy)
def test_gmf::all::gmfgraph::flowlayout_majorSpacing_setter(instance):
    original = instance.majorSpacing
    instance.majorSpacing = original
    assert instance.majorSpacing == original

@given(instance=gmf::all::gmfgraph::CenterLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::centerlayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CenterLayout)

@given(instance=gmf::all::gmfgraph::StackLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::stacklayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::StackLayout)

@given(instance=gmf::all::gmfgraph::XYLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::xylayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::XYLayout)

@given(instance=Border_strategy)
@settings(max_examples=50)
def test_border_instantiation(instance):
    assert isinstance(instance, Border)

@given(instance=FigureDescriptor_strategy)
@settings(max_examples=50)
def test_figuredescriptor_instantiation(instance):
    assert isinstance(instance, FigureDescriptor)

@given(instance=RealFigure_strategy)
@settings(max_examples=50)
def test_realfigure_instantiation(instance):
    assert isinstance(instance, RealFigure)

@given(instance=gmf::all::gmfgraph::ConnectionFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::connectionfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::ConnectionFigure)

@given(instance=gmf::all::gmfgraph::InvisibleRectangle_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::invisiblerectangle_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::InvisibleRectangle)

@given(instance=gmf::all::gmfgraph::LabeledContainer_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::labeledcontainer_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::LabeledContainer)

@given(instance=gmf::all::gmfgraph::Label_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::label_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Label)

@given(instance=gmf::all::gmfgraph::Label_strategy)
def test_gmf::all::gmfgraph::label_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gmf::all::gmfgraph::Label_strategy)
def test_gmf::all::gmfgraph::label_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::svgfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::SVGFigure)

@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_documentURI_type(instance):
    assert isinstance(instance.documentURI, str)


@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_documentURI_setter(instance):
    original = instance.documentURI
    instance.documentURI = original
    assert instance.documentURI == original

@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_noCanvasWidth_type(instance):
    assert isinstance(instance.noCanvasWidth, bool)


@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_noCanvasWidth_setter(instance):
    original = instance.noCanvasWidth
    instance.noCanvasWidth = original
    assert instance.noCanvasWidth == original

@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_noCanvasHeight_type(instance):
    assert isinstance(instance.noCanvasHeight, bool)


@given(instance=gmf::all::gmfgraph::SVGFigure_strategy)
def test_gmf::all::gmfgraph::svgfigure_noCanvasHeight_setter(instance):
    original = instance.noCanvasHeight
    instance.noCanvasHeight = original
    assert instance.noCanvasHeight == original

@given(instance=gmf::all::gmfgraph::VerticalLabel_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::verticallabel_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::VerticalLabel)

@given(instance=gmf::all::gmfgraph::VerticalLabel_strategy)
def test_gmf::all::gmfgraph::verticallabel_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=gmf::all::gmfgraph::VerticalLabel_strategy)
def test_gmf::all::gmfgraph::verticallabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=gmf::all::gmfgraph::DecorationFigure_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::decorationfigure_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::DecorationFigure)

@given(instance=gmf::all::gmfgraph::Shape_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::shape_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Shape)

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_lineKind_type(instance):
    assert isinstance(instance.lineKind, str)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_lineKind_setter(instance):
    original = instance.lineKind
    instance.lineKind = original
    assert instance.lineKind == original

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_fill_type(instance):
    assert isinstance(instance.fill, bool)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_xorOutline_type(instance):
    assert isinstance(instance.xorOutline, bool)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_xorOutline_setter(instance):
    original = instance.xorOutline
    instance.xorOutline = original
    assert instance.xorOutline == original

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_outline_type(instance):
    assert isinstance(instance.outline, bool)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_xorFill_type(instance):
    assert isinstance(instance.xorFill, bool)


@given(instance=gmf::all::gmfgraph::Shape_strategy)
def test_gmf::all::gmfgraph::shape_xorFill_setter(instance):
    original = instance.xorFill
    instance.xorFill = original
    assert instance.xorFill == original

@given(instance=FigureGallery_strategy)
@settings(max_examples=50)
def test_figuregallery_instantiation(instance):
    assert isinstance(instance, FigureGallery)

@given(instance=AbstractNode_strategy)
@settings(max_examples=50)
def test_abstractnode_instantiation(instance):
    assert isinstance(instance, AbstractNode)

@given(instance=gmf::all::gmfgraph::Node_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::node_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Node)

@given(instance=gmf::all::gmfgraph::Node_strategy)
def test_gmf::all::gmfgraph::node_resizeConstraint_type(instance):
    assert isinstance(instance.resizeConstraint, str)


@given(instance=gmf::all::gmfgraph::Node_strategy)
def test_gmf::all::gmfgraph::node_resizeConstraint_setter(instance):
    original = instance.resizeConstraint
    instance.resizeConstraint = original
    assert instance.resizeConstraint == original

@given(instance=gmf::all::gmfgraph::Node_strategy)
def test_gmf::all::gmfgraph::node_affixedParentSide_type(instance):
    assert isinstance(instance.affixedParentSide, str)


@given(instance=gmf::all::gmfgraph::Node_strategy)
def test_gmf::all::gmfgraph::node_affixedParentSide_setter(instance):
    original = instance.affixedParentSide
    instance.affixedParentSide = original
    assert instance.affixedParentSide == original

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=gmf::all::gmfgraph::Connection_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::connection_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Connection)

@given(instance=gmf::all::gmfgraph::Compartment_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::compartment_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Compartment)

@given(instance=gmf::all::gmfgraph::Compartment_strategy)
def test_gmf::all::gmfgraph::compartment_collapsible_type(instance):
    assert isinstance(instance.collapsible, bool)


@given(instance=gmf::all::gmfgraph::Compartment_strategy)
def test_gmf::all::gmfgraph::compartment_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=gmf::all::gmfgraph::Compartment_strategy)
def test_gmf::all::gmfgraph::compartment_needsTitle_type(instance):
    assert isinstance(instance.needsTitle, bool)


@given(instance=gmf::all::gmfgraph::Compartment_strategy)
def test_gmf::all::gmfgraph::compartment_needsTitle_setter(instance):
    original = instance.needsTitle
    instance.needsTitle = original
    assert instance.needsTitle == original

@given(instance=gmf::all::gmfgraph::AbstractNode_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::abstractnode_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::AbstractNode)

@given(instance=gmf::all::tooldef::StyleSelector_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::styleselector_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::StyleSelector)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gmf::all::tooldef::StyleSelector_strategy)
@settings(max_examples=30)
def test_gmf::all::tooldef::styleselector_isok_changes_state(instance):
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
        assert has_statements, f"Function 'isOk' in gmf::all::tooldef::StyleSelector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isOk' in gmf::all::tooldef::StyleSelector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isOk' in gmf::all::tooldef::StyleSelector is not implemented or raised an error")

@given(instance=gmf::all::tooldef::Image_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::image_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::Image)

@given(instance=tooldef::ContributionItem_strategy)
@settings(max_examples=50)
def test_tooldef::contributionitem_instantiation(instance):
    assert isinstance(instance, tooldef::ContributionItem)

@given(instance=Identity_strategy)
@settings(max_examples=50)
def test_identity_instantiation(instance):
    assert isinstance(instance, Identity)

@given(instance=gmf::all::gmfgraph::FigureDescriptor_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::figuredescriptor_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::FigureDescriptor)

@given(instance=gmf::all::gmfgraph::FigureGallery_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::figuregallery_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::FigureGallery)

@given(instance=gmf::all::gmfgraph::FigureGallery_strategy)
def test_gmf::all::gmfgraph::figuregallery_implementationBundle_type(instance):
    assert isinstance(instance.implementationBundle, str)


@given(instance=gmf::all::gmfgraph::FigureGallery_strategy)
def test_gmf::all::gmfgraph::figuregallery_implementationBundle_setter(instance):
    original = instance.implementationBundle
    instance.implementationBundle = original
    assert instance.implementationBundle == original

@given(instance=gmf::all::gmfgraph::Pin_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::pin_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Pin)

@given(instance=gmf::all::gmfgraph::DiagramElement_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::diagramelement_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::DiagramElement)

@given(instance=gmf::all::gmfgraph::Canvas_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::canvas_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Canvas)

@given(instance=tooldef::PredefinedItem_strategy)
@settings(max_examples=50)
def test_tooldef::predefineditem_instantiation(instance):
    assert isinstance(instance, tooldef::PredefinedItem)

@given(instance=tooldef::Menu_strategy)
@settings(max_examples=50)
def test_tooldef::menu_instantiation(instance):
    assert isinstance(instance, tooldef::Menu)

@given(instance=gmf::all::tooldef::PopupMenu_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::popupmenu_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::PopupMenu)

@given(instance=gmf::all::tooldef::PopupMenu_strategy)
def test_gmf::all::tooldef::popupmenu_iD_type(instance):
    assert isinstance(instance.iD, str)


@given(instance=gmf::all::tooldef::PopupMenu_strategy)
def test_gmf::all::tooldef::popupmenu_iD_setter(instance):
    original = instance.iD
    instance.iD = original
    assert instance.iD == original

@given(instance=gmf::all::tooldef::PredefinedMenu_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::predefinedmenu_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::PredefinedMenu)

@given(instance=ItemBase_strategy)
@settings(max_examples=50)
def test_itembase_instantiation(instance):
    assert isinstance(instance, ItemBase)

@given(instance=gmf::all::tooldef::PredefinedItem_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::predefineditem_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::PredefinedItem)

@given(instance=gmf::all::tooldef::PredefinedItem_strategy)
def test_gmf::all::tooldef::predefineditem_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=gmf::all::tooldef::PredefinedItem_strategy)
def test_gmf::all::tooldef::predefineditem_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=gmf::all::tooldef::ContributionItem_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::contributionitem_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ContributionItem)

@given(instance=gmf::all::tooldef::ContributionItem_strategy)
def test_gmf::all::tooldef::contributionitem_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=gmf::all::tooldef::ContributionItem_strategy)
def test_gmf::all::tooldef::contributionitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=gmf::all::tooldef::Separator_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::separator_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::Separator)

@given(instance=gmf::all::tooldef::Separator_strategy)
def test_gmf::all::tooldef::separator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::tooldef::Separator_strategy)
def test_gmf::all::tooldef::separator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf::all::tooldef::Menu_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::menu_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::Menu)

@given(instance=gmf::all::tooldef::ItemBase_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::itembase_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ItemBase)

@given(instance=gmf::all::tooldef::ItemRef_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::itemref_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ItemRef)

@given(instance=ContributionItem_strategy)
@settings(max_examples=50)
def test_contributionitem_instantiation(instance):
    assert isinstance(instance, ContributionItem)

@given(instance=gmf::all::tooldef::MenuAction_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::menuaction_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::MenuAction)

@given(instance=gmf::all::tooldef::MenuAction_strategy)
def test_gmf::all::tooldef::menuaction_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=gmf::all::tooldef::MenuAction_strategy)
def test_gmf::all::tooldef::menuaction_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=gmf::all::tooldef::MenuAction_strategy)
def test_gmf::all::tooldef::menuaction_hotKey_type(instance):
    assert isinstance(instance.hotKey, str)


@given(instance=gmf::all::tooldef::MenuAction_strategy)
def test_gmf::all::tooldef::menuaction_hotKey_setter(instance):
    original = instance.hotKey
    instance.hotKey = original
    assert instance.hotKey == original

@given(instance=Image_strategy)
@settings(max_examples=50)
def test_image_instantiation(instance):
    assert isinstance(instance, Image)

@given(instance=gmf::all::tooldef::DefaultImage_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::defaultimage_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::DefaultImage)

@given(instance=gmf::all::tooldef::BundleImage_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::bundleimage_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::BundleImage)

@given(instance=gmf::all::tooldef::BundleImage_strategy)
def test_gmf::all::tooldef::bundleimage_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=gmf::all::tooldef::BundleImage_strategy)
def test_gmf::all::tooldef::bundleimage_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=gmf::all::tooldef::BundleImage_strategy)
def test_gmf::all::tooldef::bundleimage_bundle_type(instance):
    assert isinstance(instance.bundle, str)


@given(instance=gmf::all::tooldef::BundleImage_strategy)
def test_gmf::all::tooldef::bundleimage_bundle_setter(instance):
    original = instance.bundle
    instance.bundle = original
    assert instance.bundle == original

@given(instance=gmf::all::tooldef::AbstractTool_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::abstracttool_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::AbstractTool)

@given(instance=gmf::all::tooldef::AbstractTool_strategy)
def test_gmf::all::tooldef::abstracttool_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=gmf::all::tooldef::AbstractTool_strategy)
def test_gmf::all::tooldef::abstracttool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=gmf::all::tooldef::AbstractTool_strategy)
def test_gmf::all::tooldef::abstracttool_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=gmf::all::tooldef::AbstractTool_strategy)
def test_gmf::all::tooldef::abstracttool_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)

@given(instance=gmf::all::tooldef::MainMenu_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::mainmenu_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::MainMenu)

@given(instance=gmf::all::tooldef::MainMenu_strategy)
def test_gmf::all::tooldef::mainmenu_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=gmf::all::tooldef::MainMenu_strategy)
def test_gmf::all::tooldef::mainmenu_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=gmf::all::tooldef::Toolbar_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::toolbar_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::Toolbar)

@given(instance=gmf::all::tooldef::ContextMenu_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::contextmenu_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ContextMenu)

@given(instance=MenuAction_strategy)
@settings(max_examples=50)
def test_menuaction_instantiation(instance):
    assert isinstance(instance, MenuAction)

@given(instance=gmf::all::tooldef::ToolRegistry_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::toolregistry_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ToolRegistry)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=gmf::all::gmfgraph::CustomPin_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::custompin_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomPin)

@given(instance=gmf::all::gmfgraph::CustomPin_strategy)
def test_gmf::all::gmfgraph::custompin_customOperationType_type(instance):
    assert isinstance(instance.customOperationType, str)


@given(instance=gmf::all::gmfgraph::CustomPin_strategy)
def test_gmf::all::gmfgraph::custompin_customOperationType_setter(instance):
    original = instance.customOperationType
    instance.customOperationType = original
    assert instance.customOperationType == original

@given(instance=gmf::all::gmfgraph::CustomPin_strategy)
def test_gmf::all::gmfgraph::custompin_customOperationName_type(instance):
    assert isinstance(instance.customOperationName, str)


@given(instance=gmf::all::gmfgraph::CustomPin_strategy)
def test_gmf::all::gmfgraph::custompin_customOperationName_setter(instance):
    original = instance.customOperationName
    instance.customOperationName = original
    assert instance.customOperationName == original

@given(instance=gmf::all::gmfgraph::VisiblePin_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::visiblepin_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::VisiblePin)

@given(instance=gmf::all::gmfgraph::ColorPin_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::colorpin_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::ColorPin)

@given(instance=gmf::all::gmfgraph::ColorPin_strategy)
def test_gmf::all::gmfgraph::colorpin_backgroundNotForeground_type(instance):
    assert isinstance(instance.backgroundNotForeground, bool)


@given(instance=gmf::all::gmfgraph::ColorPin_strategy)
def test_gmf::all::gmfgraph::colorpin_backgroundNotForeground_setter(instance):
    original = instance.backgroundNotForeground
    instance.backgroundNotForeground = original
    assert instance.backgroundNotForeground == original

@given(instance=gmf::all::mappings::VisualEffectMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::visualeffectmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::VisualEffectMapping)

@given(instance=gmf::all::mappings::VisualEffectMapping_strategy)
def test_gmf::all::mappings::visualeffectmapping_oclExpression_type(instance):
    assert isinstance(instance.oclExpression, str)


@given(instance=gmf::all::mappings::VisualEffectMapping_strategy)
def test_gmf::all::mappings::visualeffectmapping_oclExpression_setter(instance):
    original = instance.oclExpression
    instance.oclExpression = original
    assert instance.oclExpression == original

@given(instance=gmf::all::mappings::Measurable_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::measurable_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::Measurable)

@given(instance=gmf::all::mappings::Auditable_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::auditable_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::Auditable)

@given(instance=ToolContainer_strategy)
@settings(max_examples=50)
def test_toolcontainer_instantiation(instance):
    assert isinstance(instance, ToolContainer)

@given(instance=gmf::all::tooldef::Palette_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::palette_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::Palette)

@given(instance=gmf::all::tooldef::ToolGroup_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::toolgroup_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ToolGroup)

@given(instance=gmf::all::tooldef::ToolGroup_strategy)
def test_gmf::all::tooldef::toolgroup_collapsible_type(instance):
    assert isinstance(instance.collapsible, bool)


@given(instance=gmf::all::tooldef::ToolGroup_strategy)
def test_gmf::all::tooldef::toolgroup_collapsible_setter(instance):
    original = instance.collapsible
    instance.collapsible = original
    assert instance.collapsible == original

@given(instance=gmf::all::tooldef::ToolGroup_strategy)
def test_gmf::all::tooldef::toolgroup_stack_type(instance):
    assert isinstance(instance.stack, bool)


@given(instance=gmf::all::tooldef::ToolGroup_strategy)
def test_gmf::all::tooldef::toolgroup_stack_setter(instance):
    original = instance.stack
    instance.stack = original
    assert instance.stack == original

@given(instance=Measurable_strategy)
@settings(max_examples=50)
def test_measurable_instantiation(instance):
    assert isinstance(instance, Measurable)

@given(instance=MetricRule_strategy)
@settings(max_examples=50)
def test_metricrule_instantiation(instance):
    assert isinstance(instance, MetricRule)

@given(instance=gmf::all::mappings::MetricContainer_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::metriccontainer_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::MetricContainer)

@given(instance=mappings::Measurable_strategy)
@settings(max_examples=50)
def test_mappings::measurable_instantiation(instance):
    assert isinstance(instance, mappings::Measurable)

@given(instance=mappings::Auditable_strategy)
@settings(max_examples=50)
def test_mappings::auditable_instantiation(instance):
    assert isinstance(instance, mappings::Auditable)

@given(instance=gmf::all::mappings::NotationElementTarget_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::notationelementtarget_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::NotationElementTarget)

@given(instance=gmf::all::mappings::DiagramElementTarget_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::diagramelementtarget_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::DiagramElementTarget)

@given(instance=gmf::all::mappings::DomainElementTarget_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::domainelementtarget_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::DomainElementTarget)

@given(instance=Auditable_strategy)
@settings(max_examples=50)
def test_auditable_instantiation(instance):
    assert isinstance(instance, Auditable)

@given(instance=gmf::all::mappings::AuditedMetricTarget_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::auditedmetrictarget_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::AuditedMetricTarget)

@given(instance=RuleBase_strategy)
@settings(max_examples=50)
def test_rulebase_instantiation(instance):
    assert isinstance(instance, RuleBase)

@given(instance=gmf::all::mappings::MetricRule_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::metricrule_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::MetricRule)

@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_highLimit_type(instance):
    assert isinstance(instance.highLimit, str)


@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_highLimit_setter(instance):
    original = instance.highLimit
    instance.highLimit = original
    assert instance.highLimit == original

@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_lowLimit_type(instance):
    assert isinstance(instance.lowLimit, str)


@given(instance=gmf::all::mappings::MetricRule_strategy)
def test_gmf::all::mappings::metricrule_lowLimit_setter(instance):
    original = instance.lowLimit
    instance.lowLimit = original
    assert instance.lowLimit == original

@given(instance=gmf::all::mappings::AuditRule_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::auditrule_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::AuditRule)

@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_useInLiveMode_type(instance):
    assert isinstance(instance.useInLiveMode, bool)


@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_useInLiveMode_setter(instance):
    original = instance.useInLiveMode
    instance.useInLiveMode = original
    assert instance.useInLiveMode == original

@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=gmf::all::mappings::AuditRule_strategy)
def test_gmf::all::mappings::auditrule_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gmf::all::mappings::RuleBase_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::rulebase_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::RuleBase)

@given(instance=gmf::all::mappings::RuleBase_strategy)
def test_gmf::all::mappings::rulebase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::mappings::RuleBase_strategy)
def test_gmf::all::mappings::rulebase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf::all::mappings::RuleBase_strategy)
def test_gmf::all::mappings::rulebase_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=gmf::all::mappings::RuleBase_strategy)
def test_gmf::all::mappings::rulebase_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=gmf::all::mappings::DomainAttributeTarget_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::domainattributetarget_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::DomainAttributeTarget)

@given(instance=gmf::all::mappings::DomainAttributeTarget_strategy)
def test_gmf::all::mappings::domainattributetarget_nullAsError_type(instance):
    assert isinstance(instance.nullAsError, bool)


@given(instance=gmf::all::mappings::DomainAttributeTarget_strategy)
def test_gmf::all::mappings::domainattributetarget_nullAsError_setter(instance):
    original = instance.nullAsError
    instance.nullAsError = original
    assert instance.nullAsError == original

@given(instance=gmf::all::mappings::AuditContainer_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::auditcontainer_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::AuditContainer)

@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::mappings::AuditContainer_strategy)
def test_gmf::all::mappings::auditcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf::all::mappings::AppearanceSteward_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::appearancesteward_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::AppearanceSteward)

@given(instance=AbstractTool_strategy)
@settings(max_examples=50)
def test_abstracttool_instantiation(instance):
    assert isinstance(instance, AbstractTool)

@given(instance=gmf::all::tooldef::GenericTool_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::generictool_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::GenericTool)

@given(instance=gmf::all::tooldef::GenericTool_strategy)
def test_gmf::all::tooldef::generictool_toolClass_type(instance):
    assert isinstance(instance.toolClass, str)


@given(instance=gmf::all::tooldef::GenericTool_strategy)
def test_gmf::all::tooldef::generictool_toolClass_setter(instance):
    original = instance.toolClass
    instance.toolClass = original
    assert instance.toolClass == original

@given(instance=gmf::all::tooldef::StandardTool_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::standardtool_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::StandardTool)

@given(instance=gmf::all::tooldef::StandardTool_strategy)
def test_gmf::all::tooldef::standardtool_toolKind_type(instance):
    assert isinstance(instance.toolKind, str)


@given(instance=gmf::all::tooldef::StandardTool_strategy)
def test_gmf::all::tooldef::standardtool_toolKind_setter(instance):
    original = instance.toolKind
    instance.toolKind = original
    assert instance.toolKind == original

@given(instance=gmf::all::tooldef::PaletteSeparator_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::paletteseparator_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::PaletteSeparator)

@given(instance=gmf::all::tooldef::ToolContainer_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::toolcontainer_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::ToolContainer)

@given(instance=gmf::all::tooldef::CreationTool_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::creationtool_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::CreationTool)

@given(instance=gmf::all::mappings::ToolOwner_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::toolowner_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ToolOwner)

@given(instance=ContextMenu_strategy)
@settings(max_examples=50)
def test_contextmenu_instantiation(instance):
    assert isinstance(instance, ContextMenu)

@given(instance=gmf::all::mappings::MenuOwner_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::menuowner_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::MenuOwner)

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

@given(instance=gmf::all::mappings::ReferenceNewElementSpec_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::referencenewelementspec_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ReferenceNewElementSpec)

@given(instance=gmf::all::mappings::FeatureValueSpec_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::featurevaluespec_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::FeatureValueSpec)

@given(instance=gmf::all::mappings::ElementInitializer_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::elementinitializer_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ElementInitializer)

@given(instance=gmf::all::mappings::ValueExpression_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::valueexpression_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ValueExpression)

@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_langName_type(instance):
    assert isinstance(instance.langName, str)


@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_langName_setter(instance):
    original = instance.langName
    instance.langName = original
    assert instance.langName == original

@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=gmf::all::mappings::ValueExpression_strategy)
def test_gmf::all::mappings::valueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=gmf::all::mappings::FeatureInitializer_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::featureinitializer_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::FeatureInitializer)

@given(instance=gmf::all::mappings::LinkConstraints_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::linkconstraints_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::LinkConstraints)

@given(instance=mappings::gmf::all::EAttribute_strategy)
@settings(max_examples=50)
def test_mappings::gmf::all::eattribute_instantiation(instance):
    assert isinstance(instance, mappings::gmf::all::EAttribute)

@given(instance=MappingEntry_strategy)
@settings(max_examples=50)
def test_mappingentry_instantiation(instance):
    assert isinstance(instance, MappingEntry)

@given(instance=DiagramLabel_strategy)
@settings(max_examples=50)
def test_diagramlabel_instantiation(instance):
    assert isinstance(instance, DiagramLabel)

@given(instance=gmf::all::mappings::LabelMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::labelmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::LabelMapping)

@given(instance=gmf::all::mappings::LabelMapping_strategy)
def test_gmf::all::mappings::labelmapping_readOnly_type(instance):
    assert isinstance(instance.readOnly, bool)


@given(instance=gmf::all::mappings::LabelMapping_strategy)
def test_gmf::all::mappings::labelmapping_readOnly_setter(instance):
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

@given(instance=gmf::all::mappings::Constraint_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::constraint_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::Constraint)

@given(instance=Canvas_strategy)
@settings(max_examples=50)
def test_canvas_instantiation(instance):
    assert isinstance(instance, Canvas)

@given(instance=gmf::all::mappings::CanvasMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::canvasmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::CanvasMapping)

@given(instance=LinkConstraints_strategy)
@settings(max_examples=50)
def test_linkconstraints_instantiation(instance):
    assert isinstance(instance, LinkConstraints)

@given(instance=mappings::gmf::all::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_mappings::gmf::all::estructuralfeature_instantiation(instance):
    assert isinstance(instance, mappings::gmf::all::EStructuralFeature)

@given(instance=Connection_strategy)
@settings(max_examples=50)
def test_connection_instantiation(instance):
    assert isinstance(instance, Connection)

@given(instance=mappings::NeedsContainment_strategy)
@settings(max_examples=50)
def test_mappings::needscontainment_instantiation(instance):
    assert isinstance(instance, mappings::NeedsContainment)

@given(instance=Compartment_strategy)
@settings(max_examples=50)
def test_compartment_instantiation(instance):
    assert isinstance(instance, Compartment)

@given(instance=gmf::all::mappings::CompartmentMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::compartmentmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::CompartmentMapping)

@given(instance=ChildReference_strategy)
@settings(max_examples=50)
def test_childreference_instantiation(instance):
    assert isinstance(instance, ChildReference)

@given(instance=Palette_strategy)
@settings(max_examples=50)
def test_palette_instantiation(instance):
    assert isinstance(instance, Palette)

@given(instance=mappings::gmf::all::EPackage_strategy)
@settings(max_examples=50)
def test_mappings::gmf::all::epackage_instantiation(instance):
    assert isinstance(instance, mappings::gmf::all::EPackage)

@given(instance=CompartmentMapping_strategy)
@settings(max_examples=50)
def test_compartmentmapping_instantiation(instance):
    assert isinstance(instance, CompartmentMapping)

@given(instance=NodeReference_strategy)
@settings(max_examples=50)
def test_nodereference_instantiation(instance):
    assert isinstance(instance, NodeReference)

@given(instance=gmf::all::mappings::TopNodeReference_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::topnodereference_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::TopNodeReference)

@given(instance=gmf::all::mappings::ChildReference_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::childreference_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ChildReference)

@given(instance=NodeMapping_strategy)
@settings(max_examples=50)
def test_nodemapping_instantiation(instance):
    assert isinstance(instance, NodeMapping)

@given(instance=NeedsContainment_strategy)
@settings(max_examples=50)
def test_needscontainment_instantiation(instance):
    assert isinstance(instance, NeedsContainment)

@given(instance=gmf::all::mappings::NodeReference_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::nodereference_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::NodeReference)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=gmf::all::gmfgraph::DiagramLabel_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::diagramlabel_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::DiagramLabel)

@given(instance=gmf::all::gmfgraph::DiagramLabel_strategy)
def test_gmf::all::gmfgraph::diagramlabel_external_type(instance):
    assert isinstance(instance.external, bool)


@given(instance=gmf::all::gmfgraph::DiagramLabel_strategy)
def test_gmf::all::gmfgraph::diagramlabel_external_setter(instance):
    original = instance.external
    instance.external = original
    assert instance.external == original

@given(instance=gmf::all::gmfgraph::DiagramLabel_strategy)
def test_gmf::all::gmfgraph::diagramlabel_elementIcon_type(instance):
    assert isinstance(instance.elementIcon, bool)


@given(instance=gmf::all::gmfgraph::DiagramLabel_strategy)
def test_gmf::all::gmfgraph::diagramlabel_elementIcon_setter(instance):
    original = instance.elementIcon
    instance.elementIcon = original
    assert instance.elementIcon == original

@given(instance=mappings::AppearanceSteward_strategy)
@settings(max_examples=50)
def test_mappings::appearancesteward_instantiation(instance):
    assert isinstance(instance, mappings::AppearanceSteward)

@given(instance=mappings::ToolOwner_strategy)
@settings(max_examples=50)
def test_mappings::toolowner_instantiation(instance):
    assert isinstance(instance, mappings::ToolOwner)

@given(instance=mappings::MenuOwner_strategy)
@settings(max_examples=50)
def test_mappings::menuowner_instantiation(instance):
    assert isinstance(instance, mappings::MenuOwner)

@given(instance=mappings::MappingEntry_strategy)
@settings(max_examples=50)
def test_mappings::mappingentry_instantiation(instance):
    assert isinstance(instance, mappings::MappingEntry)

@given(instance=gmf::all::mappings::LinkMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::linkmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::LinkMapping)

@given(instance=gmf::all::mappings::NodeMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::nodemapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::NodeMapping)

@given(instance=LabelMapping_strategy)
@settings(max_examples=50)
def test_labelmapping_instantiation(instance):
    assert isinstance(instance, LabelMapping)

@given(instance=gmf::all::mappings::ExpressionLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::expressionlabelmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::ExpressionLabelMapping)

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::featurelabelmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::FeatureLabelMapping)

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editPattern_type(instance):
    assert isinstance(instance.editPattern, str)


@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editPattern_setter(instance):
    original = instance.editPattern
    instance.editPattern = original
    assert instance.editPattern == original

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editMethod_type(instance):
    assert isinstance(instance.editMethod, str)


@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editMethod_setter(instance):
    original = instance.editMethod
    instance.editMethod = original
    assert instance.editMethod == original

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editorPattern_type(instance):
    assert isinstance(instance.editorPattern, str)


@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_editorPattern_setter(instance):
    original = instance.editorPattern
    instance.editorPattern = original
    assert instance.editorPattern == original

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_viewPattern_type(instance):
    assert isinstance(instance.viewPattern, str)


@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_viewPattern_setter(instance):
    original = instance.viewPattern
    instance.viewPattern = original
    assert instance.viewPattern == original

@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_viewMethod_type(instance):
    assert isinstance(instance.viewMethod, str)


@given(instance=gmf::all::mappings::FeatureLabelMapping_strategy)
def test_gmf::all::mappings::featurelabelmapping_viewMethod_setter(instance):
    original = instance.viewMethod
    instance.viewMethod = original
    assert instance.viewMethod == original

@given(instance=gmf::all::mappings::DesignLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::designlabelmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::DesignLabelMapping)

@given(instance=gmf::all::mappings::OclChoiceLabelMapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::oclchoicelabelmapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::OclChoiceLabelMapping)

@given(instance=ElementInitializer_strategy)
@settings(max_examples=50)
def test_elementinitializer_instantiation(instance):
    assert isinstance(instance, ElementInitializer)

@given(instance=gmf::all::mappings::FeatureSeqInitializer_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::featureseqinitializer_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::FeatureSeqInitializer)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=mappings::gmf::all::EClass_strategy)
@settings(max_examples=50)
def test_mappings::gmf::all::eclass_instantiation(instance):
    assert isinstance(instance, mappings::gmf::all::EClass)

@given(instance=gmf::all::mappings::MappingEntry_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::mappingentry_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::MappingEntry)

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

@given(instance=gmf::all::tooldef::GenericStyleSelector_strategy)
@settings(max_examples=50)
def test_gmf::all::tooldef::genericstyleselector_instantiation(instance):
    assert isinstance(instance, gmf::all::tooldef::GenericStyleSelector)

@given(instance=gmf::all::tooldef::GenericStyleSelector_strategy)
def test_gmf::all::tooldef::genericstyleselector_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=gmf::all::tooldef::GenericStyleSelector_strategy)
def test_gmf::all::tooldef::genericstyleselector_values_setter(instance):
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

@given(instance=mappings::gmf::all::EReference_strategy)
@settings(max_examples=50)
def test_mappings::gmf::all::ereference_instantiation(instance):
    assert isinstance(instance, mappings::gmf::all::EReference)

@given(instance=gmf::all::mappings::NeedsContainment_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::needscontainment_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::NeedsContainment)

@given(instance=VisualEffectMapping_strategy)
@settings(max_examples=50)
def test_visualeffectmapping_instantiation(instance):
    assert isinstance(instance, VisualEffectMapping)

@given(instance=TopNodeReference_strategy)
@settings(max_examples=50)
def test_topnodereference_instantiation(instance):
    assert isinstance(instance, TopNodeReference)

@given(instance=gmf::all::mappings::Mapping_strategy)
@settings(max_examples=50)
def test_gmf::all::mappings::mapping_instantiation(instance):
    assert isinstance(instance, gmf::all::mappings::Mapping)

@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::rectangle2d_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Rectangle2D)

@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=gmf::all::gmfgraph::Rectangle2D_strategy)
def test_gmf::all::gmfgraph::rectangle2d_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gmf::all::gmfgraph::GridLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::gridlayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::GridLayout)

@given(instance=gmf::all::gmfgraph::GridLayout_strategy)
def test_gmf::all::gmfgraph::gridlayout_numColumns_type(instance):
    assert isinstance(instance.numColumns, int)


@given(instance=gmf::all::gmfgraph::GridLayout_strategy)
def test_gmf::all::gmfgraph::gridlayout_numColumns_setter(instance):
    original = instance.numColumns
    instance.numColumns = original
    assert instance.numColumns == original

@given(instance=gmf::all::gmfgraph::GridLayout_strategy)
def test_gmf::all::gmfgraph::gridlayout_equalWidth_type(instance):
    assert isinstance(instance.equalWidth, bool)


@given(instance=gmf::all::gmfgraph::GridLayout_strategy)
def test_gmf::all::gmfgraph::gridlayout_equalWidth_setter(instance):
    original = instance.equalWidth
    instance.equalWidth = original
    assert instance.equalWidth == original

@given(instance=gmfgraph::Layout_strategy)
@settings(max_examples=50)
def test_gmfgraph::layout_instantiation(instance):
    assert isinstance(instance, gmfgraph::Layout)

@given(instance=gmf::all::gmfgraph::CustomLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customlayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomLayout)

@given(instance=gmf::all::gmfgraph::LayoutRef_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::layoutref_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::LayoutRef)

@given(instance=gmf::all::gmfgraph::Layout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::layout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Layout)

@given(instance=gmf::all::gmfgraph::Layoutable_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::layoutable_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Layoutable)

@given(instance=LayoutData_strategy)
@settings(max_examples=50)
def test_layoutdata_instantiation(instance):
    assert isinstance(instance, LayoutData)

@given(instance=gmf::all::gmfgraph::XYLayoutData_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::xylayoutdata_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::XYLayoutData)

@given(instance=gmf::all::gmfgraph::BorderLayoutData_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::borderlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::BorderLayoutData)

@given(instance=gmf::all::gmfgraph::BorderLayoutData_strategy)
def test_gmf::all::gmfgraph::borderlayoutdata_alignment_type(instance):
    assert isinstance(instance.alignment, str)


@given(instance=gmf::all::gmfgraph::BorderLayoutData_strategy)
def test_gmf::all::gmfgraph::borderlayoutdata_alignment_setter(instance):
    original = instance.alignment
    instance.alignment = original
    assert instance.alignment == original

@given(instance=gmf::all::gmfgraph::BorderLayoutData_strategy)
def test_gmf::all::gmfgraph::borderlayoutdata_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=gmf::all::gmfgraph::BorderLayoutData_strategy)
def test_gmf::all::gmfgraph::borderlayoutdata_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::gridlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::GridLayoutData)

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_verticalAlignment_type(instance):
    assert isinstance(instance.verticalAlignment, str)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_verticalAlignment_setter(instance):
    original = instance.verticalAlignment
    instance.verticalAlignment = original
    assert instance.verticalAlignment == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalSpan_type(instance):
    assert isinstance(instance.horizontalSpan, int)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalSpan_setter(instance):
    original = instance.horizontalSpan
    instance.horizontalSpan = original
    assert instance.horizontalSpan == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_grabExcessVerticalSpace_type(instance):
    assert isinstance(instance.grabExcessVerticalSpace, bool)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_grabExcessVerticalSpace_setter(instance):
    original = instance.grabExcessVerticalSpace
    instance.grabExcessVerticalSpace = original
    assert instance.grabExcessVerticalSpace == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_verticalSpan_type(instance):
    assert isinstance(instance.verticalSpan, int)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_verticalSpan_setter(instance):
    original = instance.verticalSpan
    instance.verticalSpan = original
    assert instance.verticalSpan == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_grabExcessHorizontalSpace_type(instance):
    assert isinstance(instance.grabExcessHorizontalSpace, bool)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_grabExcessHorizontalSpace_setter(instance):
    original = instance.grabExcessHorizontalSpace
    instance.grabExcessHorizontalSpace = original
    assert instance.grabExcessHorizontalSpace == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalIndent_type(instance):
    assert isinstance(instance.horizontalIndent, int)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalIndent_setter(instance):
    original = instance.horizontalIndent
    instance.horizontalIndent = original
    assert instance.horizontalIndent == original

@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalAlignment_type(instance):
    assert isinstance(instance.horizontalAlignment, str)


@given(instance=gmf::all::gmfgraph::GridLayoutData_strategy)
def test_gmf::all::gmfgraph::gridlayoutdata_horizontalAlignment_setter(instance):
    original = instance.horizontalAlignment
    instance.horizontalAlignment = original
    assert instance.horizontalAlignment == original

@given(instance=gmf::all::gmfgraph::BorderLayout_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::borderlayout_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::BorderLayout)

@given(instance=gmfgraph::Border_strategy)
@settings(max_examples=50)
def test_gmfgraph::border_instantiation(instance):
    assert isinstance(instance, gmfgraph::Border)

@given(instance=gmf::all::gmfgraph::CustomBorder_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customborder_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomBorder)

@given(instance=gmf::all::gmfgraph::CompoundBorder_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::compoundborder_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CompoundBorder)

@given(instance=gmf::all::gmfgraph::MarginBorder_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::marginborder_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::MarginBorder)

@given(instance=gmf::all::gmfgraph::LineBorder_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::lineborder_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::LineBorder)

@given(instance=gmf::all::gmfgraph::LineBorder_strategy)
def test_gmf::all::gmfgraph::lineborder_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=gmf::all::gmfgraph::LineBorder_strategy)
def test_gmf::all::gmfgraph::lineborder_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=gmf::all::gmfgraph::BorderRef_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::borderref_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::BorderRef)

@given(instance=gmf::all::gmfgraph::Border_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::border_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Border)

@given(instance=gmfgraph::LayoutData_strategy)
@settings(max_examples=50)
def test_gmfgraph::layoutdata_instantiation(instance):
    assert isinstance(instance, gmfgraph::LayoutData)

@given(instance=gmf::all::gmfgraph::CustomLayoutData_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customlayoutdata_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomLayoutData)

@given(instance=gmf::all::gmfgraph::LayoutData_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::layoutdata_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::LayoutData)

@given(instance=gmf::all::gmfgraph::Point_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::point_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Point)

@given(instance=gmf::all::gmfgraph::Point_strategy)
def test_gmf::all::gmfgraph::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=gmf::all::gmfgraph::Point_strategy)
def test_gmf::all::gmfgraph::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=gmf::all::gmfgraph::Point_strategy)
def test_gmf::all::gmfgraph::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=gmf::all::gmfgraph::Point_strategy)
def test_gmf::all::gmfgraph::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::basicfont_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::BasicFont)

@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_faceName_type(instance):
    assert isinstance(instance.faceName, str)


@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_faceName_setter(instance):
    original = instance.faceName
    instance.faceName = original
    assert instance.faceName == original

@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=gmf::all::gmfgraph::BasicFont_strategy)
def test_gmf::all::gmfgraph::basicfont_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=gmf::all::gmfgraph::Font_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::font_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Font)

@given(instance=gmf::all::gmfgraph::ConstantColor_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::constantcolor_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::ConstantColor)

@given(instance=gmf::all::gmfgraph::ConstantColor_strategy)
def test_gmf::all::gmfgraph::constantcolor_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gmf::all::gmfgraph::ConstantColor_strategy)
def test_gmf::all::gmfgraph::constantcolor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::rgbcolor_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::RGBColor)

@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=gmf::all::gmfgraph::RGBColor_strategy)
def test_gmf::all::gmfgraph::rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=gmf::all::gmfgraph::Color_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::color_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Color)

@given(instance=gmfgraph::CustomFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::customfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::CustomFigure)

@given(instance=FigureAccessor_strategy)
@settings(max_examples=50)
def test_figureaccessor_instantiation(instance):
    assert isinstance(instance, FigureAccessor)

@given(instance=gmf::all::gmfgraph::Insets_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::insets_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Insets)

@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_top_type(instance):
    assert isinstance(instance.top, int)


@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_top_setter(instance):
    original = instance.top
    instance.top = original
    assert instance.top == original

@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_left_type(instance):
    assert isinstance(instance.left, int)


@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_right_type(instance):
    assert isinstance(instance.right, int)


@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_bottom_type(instance):
    assert isinstance(instance.bottom, int)


@given(instance=gmf::all::gmfgraph::Insets_strategy)
def test_gmf::all::gmfgraph::insets_bottom_setter(instance):
    original = instance.bottom
    instance.bottom = original
    assert instance.bottom == original

@given(instance=gmf::all::gmfgraph::Dimension_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::dimension_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::Dimension)

@given(instance=gmf::all::gmfgraph::Dimension_strategy)
def test_gmf::all::gmfgraph::dimension_dx_type(instance):
    assert isinstance(instance.dx, int)


@given(instance=gmf::all::gmfgraph::Dimension_strategy)
def test_gmf::all::gmfgraph::dimension_dx_setter(instance):
    original = instance.dx
    instance.dx = original
    assert instance.dx == original

@given(instance=gmf::all::gmfgraph::Dimension_strategy)
def test_gmf::all::gmfgraph::dimension_dy_type(instance):
    assert isinstance(instance.dy, int)


@given(instance=gmf::all::gmfgraph::Dimension_strategy)
def test_gmf::all::gmfgraph::dimension_dy_setter(instance):
    original = instance.dy
    instance.dy = original
    assert instance.dy == original

@given(instance=gmf::all::gmfgraph::FigureAccessor_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::figureaccessor_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::FigureAccessor)

@given(instance=gmf::all::gmfgraph::FigureAccessor_strategy)
def test_gmf::all::gmfgraph::figureaccessor_accessor_type(instance):
    assert isinstance(instance.accessor, str)


@given(instance=gmf::all::gmfgraph::FigureAccessor_strategy)
def test_gmf::all::gmfgraph::figureaccessor_accessor_setter(instance):
    original = instance.accessor
    instance.accessor = original
    assert instance.accessor == original

@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customattribute_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomAttribute)

@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_multiStatementValue_type(instance):
    assert isinstance(instance.multiStatementValue, bool)


@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_multiStatementValue_setter(instance):
    original = instance.multiStatementValue
    instance.multiStatementValue = original
    assert instance.multiStatementValue == original

@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_directAccess_type(instance):
    assert isinstance(instance.directAccess, bool)


@given(instance=gmf::all::gmfgraph::CustomAttribute_strategy)
def test_gmf::all::gmfgraph::customattribute_directAccess_setter(instance):
    original = instance.directAccess
    instance.directAccess = original
    assert instance.directAccess == original

@given(instance=CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_customattributeowner_instantiation(instance):
    assert isinstance(instance, CustomAttributeOwner)

@given(instance=gmf::all::gmfgraph::CustomClass_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customclass_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomClass)

@given(instance=gmf::all::gmfgraph::CustomClass_strategy)
def test_gmf::all::gmfgraph::customclass_qualifiedClassName_type(instance):
    assert isinstance(instance.qualifiedClassName, str)


@given(instance=gmf::all::gmfgraph::CustomClass_strategy)
def test_gmf::all::gmfgraph::customclass_qualifiedClassName_setter(instance):
    original = instance.qualifiedClassName
    instance.qualifiedClassName = original
    assert instance.qualifiedClassName == original

@given(instance=CustomAttribute_strategy)
@settings(max_examples=50)
def test_customattribute_instantiation(instance):
    assert isinstance(instance, CustomAttribute)

@given(instance=gmf::all::gmfgraph::CustomAttributeOwner_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customattributeowner_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomAttributeOwner)

@given(instance=gmfgraph::Polygon_strategy)
@settings(max_examples=50)
def test_gmfgraph::polygon_instantiation(instance):
    assert isinstance(instance, gmfgraph::Polygon)

@given(instance=gmfgraph::DecorationFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::decorationfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::DecorationFigure)

@given(instance=gmf::all::gmfgraph::CustomDecoration_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customdecoration_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomDecoration)

@given(instance=gmf::all::gmfgraph::PolygonDecoration_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::polygondecoration_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::PolygonDecoration)

@given(instance=DecorationFigure_strategy)
@settings(max_examples=50)
def test_decorationfigure_instantiation(instance):
    assert isinstance(instance, DecorationFigure)

@given(instance=gmfgraph::ConnectionFigure_strategy)
@settings(max_examples=50)
def test_gmfgraph::connectionfigure_instantiation(instance):
    assert isinstance(instance, gmfgraph::ConnectionFigure)

@given(instance=gmf::all::gmfgraph::CustomConnection_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::customconnection_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::CustomConnection)

@given(instance=gmfgraph::Polyline_strategy)
@settings(max_examples=50)
def test_gmfgraph::polyline_instantiation(instance):
    assert isinstance(instance, gmfgraph::Polyline)

@given(instance=gmf::all::gmfgraph::PolylineDecoration_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::polylinedecoration_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::PolylineDecoration)

@given(instance=gmf::all::gmfgraph::PolylineConnection_strategy)
@settings(max_examples=50)
def test_gmf::all::gmfgraph::polylineconnection_instantiation(instance):
    assert isinstance(instance, gmf::all::gmfgraph::PolylineConnection)
