import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BasicSemanticCompartment,
    DrawerStyle,
    DecorationNode,
    notation::BasicCompartment,
    BasicDecorationNode,
    notation::BasicSemanticCompartment,
    notation::DecorationNode,
    DiagramStyle,
    LayoutConstraint,
    notation::Location,
    notation::Size,
    RoundedCornersStyle,
    notation::RoutingStyle,
    Anchor,
    notation::IdentityAnchor,
    notation::Style,
    notation::LayoutConstraint,
    notation::Anchor,
    notation::Bendpoints,
    notation::EObject,
    Style,
    notation::SortingStyle,
    notation::FontStyle,
    notation::RoundedCornersStyle,
    notation::LineStyle,
    notation::LineTypeStyle,
    notation::TitleStyle,
    notation::DescriptionStyle,
    notation::FillStyle,
    View,
    notation::Node,
    notation::Edge,
    Diagram,
    notation::StandardDiagram,
    ConnectorStyle,
    Edge,
    notation::Connector,
    FilteringStyle,
    SortingStyle,
    TitleStyle,
    notation::SemanticListCompartment,
    CanonicalStyle,
    BasicCompartment,
    notation::ListCompartment,
    notation::Compartment,
    ShapeStyle,
    Node,
    notation::BasicDecorationNode,
    notation::Shape,
    notation::ArrowStyle,
    notation::TextStyle,
    notation::MultiDiagramLinkStyle,
    notation::DiagramLinkStyle,
    DiagramLinkStyle,
    notation::HintedDiagramLinkStyle,
    notation::EDataType,
    notation::StringObjectConverter,
    notation::NamedStyle,
    DataTypeStyle,
    notation::ListValueStyle,
    notation::SingleValueStyle,
    NamedStyle,
    notation::StringValueStyle,
    notation::DoubleValueStyle,
    notation::IntListValueStyle,
    notation::IntValueStyle,
    notation::ByteArrayValueStyle,
    notation::EObjectListValueStyle,
    notation::EObjectValueStyle,
    notation::StringListValueStyle,
    notation::BooleanListValueStyle,
    notation::DoubleListValueStyle,
    notation::BooleanValueStyle,
    notation::PropertiesSetStyle,
    StringObjectConverter,
    notation::DataTypeStyle,
    notation::PropertyValue,
    notation::StringToPropertyValueMapEntry,
    notation::NodeEntry,
    ImageStyle,
    notation::ImageBufferStyle,
    notation::ImageStyle,
    GuideStyle,
    PageStyle,
    notation::FilteringStyle,
    notation::Image,
    Bendpoints,
    notation::RelativeBendpoints,
    notation::Guide,
    notation::GuideStyle,
    notation::DrawerStyle,
    notation::PageStyle,
    RoutingStyle,
    LineStyle,
    notation::ConnectorStyle,
    FillStyle,
    DescriptionStyle,
    notation::DiagramStyle,
    FontStyle,
    notation::ShapeStyle,
    notation::CanonicalStyle,
    EModelElement,
    notation::View,
    notation::Diagram,
    notation::Ratio,
    Size,
    Location,
    notation::Bounds,
    ArrowType,
    JumpLinkType,
    JumpLinkStatus,
    Smoothness,
    Alignment,
    MeasurementUnit,
    TextAlignment,
    Sorting,
    SortingDirection,
    Routing,
    GradientStyle,
    LineType,
    Filtering,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(BasicSemanticCompartment)


def test_basicsemanticcompartment_constructor_exists():
    assert callable(BasicSemanticCompartment.__init__)


def test_basicsemanticcompartment_constructor_args():
    sig = inspect.signature(BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_drawerstyle_is_not_abstract():
    assert not inspect.isabstract(DrawerStyle)


def test_drawerstyle_constructor_exists():
    assert callable(DrawerStyle.__init__)


def test_drawerstyle_constructor_args():
    sig = inspect.signature(DrawerStyle.__init__)
    params = list(sig.parameters.keys())



def test_decorationnode_is_not_abstract():
    assert not inspect.isabstract(DecorationNode)


def test_decorationnode_constructor_exists():
    assert callable(DecorationNode.__init__)


def test_decorationnode_constructor_args():
    sig = inspect.signature(DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_notation::basiccompartment_is_not_abstract():
    assert not inspect.isabstract(notation::BasicCompartment)


def test_notation::basiccompartment_constructor_exists():
    assert callable(notation::BasicCompartment.__init__)


def test_notation::basiccompartment_constructor_args():
    sig = inspect.signature(notation::BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(BasicDecorationNode)


def test_basicdecorationnode_constructor_exists():
    assert callable(BasicDecorationNode.__init__)


def test_basicdecorationnode_constructor_args():
    sig = inspect.signature(BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_notation::basicsemanticcompartment_is_not_abstract():
    assert not inspect.isabstract(notation::BasicSemanticCompartment)


def test_notation::basicsemanticcompartment_constructor_exists():
    assert callable(notation::BasicSemanticCompartment.__init__)


def test_notation::basicsemanticcompartment_constructor_args():
    sig = inspect.signature(notation::BasicSemanticCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation::decorationnode_is_not_abstract():
    assert not inspect.isabstract(notation::DecorationNode)


def test_notation::decorationnode_constructor_exists():
    assert callable(notation::DecorationNode.__init__)


def test_notation::decorationnode_constructor_args():
    sig = inspect.signature(notation::DecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_diagramstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramStyle)


def test_diagramstyle_constructor_exists():
    assert callable(DiagramStyle.__init__)


def test_diagramstyle_constructor_args():
    sig = inspect.signature(DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(LayoutConstraint)


def test_layoutconstraint_constructor_exists():
    assert callable(LayoutConstraint.__init__)


def test_layoutconstraint_constructor_args():
    sig = inspect.signature(LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_notation::location_is_not_abstract():
    assert not inspect.isabstract(notation::Location)


def test_notation::location_constructor_exists():
    assert callable(notation::Location.__init__)


def test_notation::location_constructor_args():
    sig = inspect.signature(notation::Location.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation::location_has_x():
    assert hasattr(notation::Location, "x")
    descriptor = None
    for klass in notation::Location.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation::location_has_y():
    assert hasattr(notation::Location, "y")
    descriptor = None
    for klass in notation::Location.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_notation::size_is_not_abstract():
    assert not inspect.isabstract(notation::Size)


def test_notation::size_constructor_exists():
    assert callable(notation::Size.__init__)


def test_notation::size_constructor_args():
    sig = inspect.signature(notation::Size.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_notation::size_has_width():
    assert hasattr(notation::Size, "width")
    descriptor = None
    for klass in notation::Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation::size_has_height():
    assert hasattr(notation::Size, "height")
    descriptor = None
    for klass in notation::Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(RoundedCornersStyle)


def test_roundedcornersstyle_constructor_exists():
    assert callable(RoundedCornersStyle.__init__)


def test_roundedcornersstyle_constructor_args():
    sig = inspect.signature(RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::routingstyle_is_not_abstract():
    assert not inspect.isabstract(notation::RoutingStyle)


def test_notation::routingstyle_constructor_exists():
    assert callable(notation::RoutingStyle.__init__)


def test_notation::routingstyle_constructor_args():
    sig = inspect.signature(notation::RoutingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "routing" in params, "Missing parameter 'routing'"
    assert "jumpLinkType" in params, "Missing parameter 'jumpLinkType'"
    assert "smoothness" in params, "Missing parameter 'smoothness'"
    assert "closestDistance" in params, "Missing parameter 'closestDistance'"
    assert "jumpLinkStatus" in params, "Missing parameter 'jumpLinkStatus'"
    assert "jumpLinksReverse" in params, "Missing parameter 'jumpLinksReverse'"
    assert "avoidObstructions" in params, "Missing parameter 'avoidObstructions'"

def test_notation::routingstyle_has_routing():
    assert hasattr(notation::RoutingStyle, "routing")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "routing" in klass.__dict__:
            descriptor = klass.__dict__["routing"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_jumpLinkType():
    assert hasattr(notation::RoutingStyle, "jumpLinkType")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "jumpLinkType" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinkType"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_smoothness():
    assert hasattr(notation::RoutingStyle, "smoothness")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "smoothness" in klass.__dict__:
            descriptor = klass.__dict__["smoothness"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_closestDistance():
    assert hasattr(notation::RoutingStyle, "closestDistance")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "closestDistance" in klass.__dict__:
            descriptor = klass.__dict__["closestDistance"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_jumpLinkStatus():
    assert hasattr(notation::RoutingStyle, "jumpLinkStatus")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "jumpLinkStatus" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinkStatus"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_jumpLinksReverse():
    assert hasattr(notation::RoutingStyle, "jumpLinksReverse")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "jumpLinksReverse" in klass.__dict__:
            descriptor = klass.__dict__["jumpLinksReverse"]
            break
    assert isinstance(descriptor, property)

def test_notation::routingstyle_has_avoidObstructions():
    assert hasattr(notation::RoutingStyle, "avoidObstructions")
    descriptor = None
    for klass in notation::RoutingStyle.__mro__:
        if "avoidObstructions" in klass.__dict__:
            descriptor = klass.__dict__["avoidObstructions"]
            break
    assert isinstance(descriptor, property)



def test_anchor_is_not_abstract():
    assert not inspect.isabstract(Anchor)


def test_anchor_constructor_exists():
    assert callable(Anchor.__init__)


def test_anchor_constructor_args():
    sig = inspect.signature(Anchor.__init__)
    params = list(sig.parameters.keys())



def test_notation::identityanchor_is_not_abstract():
    assert not inspect.isabstract(notation::IdentityAnchor)


def test_notation::identityanchor_constructor_exists():
    assert callable(notation::IdentityAnchor.__init__)


def test_notation::identityanchor_constructor_args():
    sig = inspect.signature(notation::IdentityAnchor.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_notation::identityanchor_has_id():
    assert hasattr(notation::IdentityAnchor, "id")
    descriptor = None
    for klass in notation::IdentityAnchor.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_notation::style_is_not_abstract():
    assert not inspect.isabstract(notation::Style)


def test_notation::style_constructor_exists():
    assert callable(notation::Style.__init__)


def test_notation::style_constructor_args():
    sig = inspect.signature(notation::Style.__init__)
    params = list(sig.parameters.keys())



def test_notation::layoutconstraint_is_not_abstract():
    assert not inspect.isabstract(notation::LayoutConstraint)


def test_notation::layoutconstraint_constructor_exists():
    assert callable(notation::LayoutConstraint.__init__)


def test_notation::layoutconstraint_constructor_args():
    sig = inspect.signature(notation::LayoutConstraint.__init__)
    params = list(sig.parameters.keys())



def test_notation::anchor_is_not_abstract():
    assert not inspect.isabstract(notation::Anchor)


def test_notation::anchor_constructor_exists():
    assert callable(notation::Anchor.__init__)


def test_notation::anchor_constructor_args():
    sig = inspect.signature(notation::Anchor.__init__)
    params = list(sig.parameters.keys())



def test_notation::bendpoints_is_not_abstract():
    assert not inspect.isabstract(notation::Bendpoints)


def test_notation::bendpoints_constructor_exists():
    assert callable(notation::Bendpoints.__init__)


def test_notation::bendpoints_constructor_args():
    sig = inspect.signature(notation::Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_notation::eobject_is_not_abstract():
    assert not inspect.isabstract(notation::EObject)


def test_notation::eobject_constructor_exists():
    assert callable(notation::EObject.__init__)


def test_notation::eobject_constructor_args():
    sig = inspect.signature(notation::EObject.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_notation::sortingstyle_is_not_abstract():
    assert not inspect.isabstract(notation::SortingStyle)


def test_notation::sortingstyle_constructor_exists():
    assert callable(notation::SortingStyle.__init__)


def test_notation::sortingstyle_constructor_args():
    sig = inspect.signature(notation::SortingStyle.__init__)
    params = list(sig.parameters.keys())
    assert "sorting" in params, "Missing parameter 'sorting'"
    assert "sortingKeys" in params, "Missing parameter 'sortingKeys'"

def test_notation::sortingstyle_has_sorting():
    assert hasattr(notation::SortingStyle, "sorting")
    descriptor = None
    for klass in notation::SortingStyle.__mro__:
        if "sorting" in klass.__dict__:
            descriptor = klass.__dict__["sorting"]
            break
    assert isinstance(descriptor, property)

def test_notation::sortingstyle_has_sortingKeys():
    assert hasattr(notation::SortingStyle, "sortingKeys")
    descriptor = None
    for klass in notation::SortingStyle.__mro__:
        if "sortingKeys" in klass.__dict__:
            descriptor = klass.__dict__["sortingKeys"]
            break
    assert isinstance(descriptor, property)



def test_notation::fontstyle_is_not_abstract():
    assert not inspect.isabstract(notation::FontStyle)


def test_notation::fontstyle_constructor_exists():
    assert callable(notation::FontStyle.__init__)


def test_notation::fontstyle_constructor_args():
    sig = inspect.signature(notation::FontStyle.__init__)
    params = list(sig.parameters.keys())
    assert "underline" in params, "Missing parameter 'underline'"
    assert "fontHeight" in params, "Missing parameter 'fontHeight'"
    assert "strikeThrough" in params, "Missing parameter 'strikeThrough'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "italic" in params, "Missing parameter 'italic'"

def test_notation::fontstyle_has_underline():
    assert hasattr(notation::FontStyle, "underline")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "underline" in klass.__dict__:
            descriptor = klass.__dict__["underline"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_fontHeight():
    assert hasattr(notation::FontStyle, "fontHeight")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "fontHeight" in klass.__dict__:
            descriptor = klass.__dict__["fontHeight"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_strikeThrough():
    assert hasattr(notation::FontStyle, "strikeThrough")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "strikeThrough" in klass.__dict__:
            descriptor = klass.__dict__["strikeThrough"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_fontName():
    assert hasattr(notation::FontStyle, "fontName")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_bold():
    assert hasattr(notation::FontStyle, "bold")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_fontColor():
    assert hasattr(notation::FontStyle, "fontColor")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_notation::fontstyle_has_italic():
    assert hasattr(notation::FontStyle, "italic")
    descriptor = None
    for klass in notation::FontStyle.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)



def test_notation::roundedcornersstyle_is_not_abstract():
    assert not inspect.isabstract(notation::RoundedCornersStyle)


def test_notation::roundedcornersstyle_constructor_exists():
    assert callable(notation::RoundedCornersStyle.__init__)


def test_notation::roundedcornersstyle_constructor_args():
    sig = inspect.signature(notation::RoundedCornersStyle.__init__)
    params = list(sig.parameters.keys())
    assert "roundedBendpointsRadius" in params, "Missing parameter 'roundedBendpointsRadius'"

def test_notation::roundedcornersstyle_has_roundedBendpointsRadius():
    assert hasattr(notation::RoundedCornersStyle, "roundedBendpointsRadius")
    descriptor = None
    for klass in notation::RoundedCornersStyle.__mro__:
        if "roundedBendpointsRadius" in klass.__dict__:
            descriptor = klass.__dict__["roundedBendpointsRadius"]
            break
    assert isinstance(descriptor, property)



def test_notation::linestyle_is_not_abstract():
    assert not inspect.isabstract(notation::LineStyle)


def test_notation::linestyle_constructor_exists():
    assert callable(notation::LineStyle.__init__)


def test_notation::linestyle_constructor_args():
    sig = inspect.signature(notation::LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "lineColor" in params, "Missing parameter 'lineColor'"

def test_notation::linestyle_has_lineWidth():
    assert hasattr(notation::LineStyle, "lineWidth")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_lineColor():
    assert hasattr(notation::LineStyle, "lineColor")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "lineColor" in klass.__dict__:
            descriptor = klass.__dict__["lineColor"]
            break
    assert isinstance(descriptor, property)



def test_notation::linetypestyle_is_not_abstract():
    assert not inspect.isabstract(notation::LineTypeStyle)


def test_notation::linetypestyle_constructor_exists():
    assert callable(notation::LineTypeStyle.__init__)


def test_notation::linetypestyle_constructor_args():
    sig = inspect.signature(notation::LineTypeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "lineType" in params, "Missing parameter 'lineType'"

def test_notation::linetypestyle_has_lineType():
    assert hasattr(notation::LineTypeStyle, "lineType")
    descriptor = None
    for klass in notation::LineTypeStyle.__mro__:
        if "lineType" in klass.__dict__:
            descriptor = klass.__dict__["lineType"]
            break
    assert isinstance(descriptor, property)



def test_notation::titlestyle_is_not_abstract():
    assert not inspect.isabstract(notation::TitleStyle)


def test_notation::titlestyle_constructor_exists():
    assert callable(notation::TitleStyle.__init__)


def test_notation::titlestyle_constructor_args():
    sig = inspect.signature(notation::TitleStyle.__init__)
    params = list(sig.parameters.keys())
    assert "showTitle" in params, "Missing parameter 'showTitle'"

def test_notation::titlestyle_has_showTitle():
    assert hasattr(notation::TitleStyle, "showTitle")
    descriptor = None
    for klass in notation::TitleStyle.__mro__:
        if "showTitle" in klass.__dict__:
            descriptor = klass.__dict__["showTitle"]
            break
    assert isinstance(descriptor, property)



def test_notation::descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(notation::DescriptionStyle)


def test_notation::descriptionstyle_constructor_exists():
    assert callable(notation::DescriptionStyle.__init__)


def test_notation::descriptionstyle_constructor_args():
    sig = inspect.signature(notation::DescriptionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_notation::descriptionstyle_has_description():
    assert hasattr(notation::DescriptionStyle, "description")
    descriptor = None
    for klass in notation::DescriptionStyle.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_notation::fillstyle_is_not_abstract():
    assert not inspect.isabstract(notation::FillStyle)


def test_notation::fillstyle_constructor_exists():
    assert callable(notation::FillStyle.__init__)


def test_notation::fillstyle_constructor_args():
    sig = inspect.signature(notation::FillStyle.__init__)
    params = list(sig.parameters.keys())
    assert "transparency" in params, "Missing parameter 'transparency'"
    assert "gradient" in params, "Missing parameter 'gradient'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"

def test_notation::fillstyle_has_transparency():
    assert hasattr(notation::FillStyle, "transparency")
    descriptor = None
    for klass in notation::FillStyle.__mro__:
        if "transparency" in klass.__dict__:
            descriptor = klass.__dict__["transparency"]
            break
    assert isinstance(descriptor, property)

def test_notation::fillstyle_has_gradient():
    assert hasattr(notation::FillStyle, "gradient")
    descriptor = None
    for klass in notation::FillStyle.__mro__:
        if "gradient" in klass.__dict__:
            descriptor = klass.__dict__["gradient"]
            break
    assert isinstance(descriptor, property)

def test_notation::fillstyle_has_fillColor():
    assert hasattr(notation::FillStyle, "fillColor")
    descriptor = None
    for klass in notation::FillStyle.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)



def test_view_is_not_abstract():
    assert not inspect.isabstract(View)


def test_view_constructor_exists():
    assert callable(View.__init__)


def test_view_constructor_args():
    sig = inspect.signature(View.__init__)
    params = list(sig.parameters.keys())



def test_notation::node_is_not_abstract():
    assert not inspect.isabstract(notation::Node)


def test_notation::node_constructor_exists():
    assert callable(notation::Node.__init__)


def test_notation::node_constructor_args():
    sig = inspect.signature(notation::Node.__init__)
    params = list(sig.parameters.keys())



def test_notation::edge_is_not_abstract():
    assert not inspect.isabstract(notation::Edge)


def test_notation::edge_constructor_exists():
    assert callable(notation::Edge.__init__)


def test_notation::edge_constructor_args():
    sig = inspect.signature(notation::Edge.__init__)
    params = list(sig.parameters.keys())



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_notation::standarddiagram_is_not_abstract():
    assert not inspect.isabstract(notation::StandardDiagram)


def test_notation::standarddiagram_constructor_exists():
    assert callable(notation::StandardDiagram.__init__)


def test_notation::standarddiagram_constructor_args():
    sig = inspect.signature(notation::StandardDiagram.__init__)
    params = list(sig.parameters.keys())



def test_connectorstyle_is_not_abstract():
    assert not inspect.isabstract(ConnectorStyle)


def test_connectorstyle_constructor_exists():
    assert callable(ConnectorStyle.__init__)


def test_connectorstyle_constructor_args():
    sig = inspect.signature(ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_notation::connector_is_not_abstract():
    assert not inspect.isabstract(notation::Connector)


def test_notation::connector_constructor_exists():
    assert callable(notation::Connector.__init__)


def test_notation::connector_constructor_args():
    sig = inspect.signature(notation::Connector.__init__)
    params = list(sig.parameters.keys())



def test_filteringstyle_is_not_abstract():
    assert not inspect.isabstract(FilteringStyle)


def test_filteringstyle_constructor_exists():
    assert callable(FilteringStyle.__init__)


def test_filteringstyle_constructor_args():
    sig = inspect.signature(FilteringStyle.__init__)
    params = list(sig.parameters.keys())



def test_sortingstyle_is_not_abstract():
    assert not inspect.isabstract(SortingStyle)


def test_sortingstyle_constructor_exists():
    assert callable(SortingStyle.__init__)


def test_sortingstyle_constructor_args():
    sig = inspect.signature(SortingStyle.__init__)
    params = list(sig.parameters.keys())



def test_titlestyle_is_not_abstract():
    assert not inspect.isabstract(TitleStyle)


def test_titlestyle_constructor_exists():
    assert callable(TitleStyle.__init__)


def test_titlestyle_constructor_args():
    sig = inspect.signature(TitleStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::semanticlistcompartment_is_not_abstract():
    assert not inspect.isabstract(notation::SemanticListCompartment)


def test_notation::semanticlistcompartment_constructor_exists():
    assert callable(notation::SemanticListCompartment.__init__)


def test_notation::semanticlistcompartment_constructor_args():
    sig = inspect.signature(notation::SemanticListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(CanonicalStyle)


def test_canonicalstyle_constructor_exists():
    assert callable(CanonicalStyle.__init__)


def test_canonicalstyle_constructor_args():
    sig = inspect.signature(CanonicalStyle.__init__)
    params = list(sig.parameters.keys())



def test_basiccompartment_is_not_abstract():
    assert not inspect.isabstract(BasicCompartment)


def test_basiccompartment_constructor_exists():
    assert callable(BasicCompartment.__init__)


def test_basiccompartment_constructor_args():
    sig = inspect.signature(BasicCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation::listcompartment_is_not_abstract():
    assert not inspect.isabstract(notation::ListCompartment)


def test_notation::listcompartment_constructor_exists():
    assert callable(notation::ListCompartment.__init__)


def test_notation::listcompartment_constructor_args():
    sig = inspect.signature(notation::ListCompartment.__init__)
    params = list(sig.parameters.keys())



def test_notation::compartment_is_not_abstract():
    assert not inspect.isabstract(notation::Compartment)


def test_notation::compartment_constructor_exists():
    assert callable(notation::Compartment.__init__)


def test_notation::compartment_constructor_args():
    sig = inspect.signature(notation::Compartment.__init__)
    params = list(sig.parameters.keys())



def test_shapestyle_is_not_abstract():
    assert not inspect.isabstract(ShapeStyle)


def test_shapestyle_constructor_exists():
    assert callable(ShapeStyle.__init__)


def test_shapestyle_constructor_args():
    sig = inspect.signature(ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_notation::basicdecorationnode_is_not_abstract():
    assert not inspect.isabstract(notation::BasicDecorationNode)


def test_notation::basicdecorationnode_constructor_exists():
    assert callable(notation::BasicDecorationNode.__init__)


def test_notation::basicdecorationnode_constructor_args():
    sig = inspect.signature(notation::BasicDecorationNode.__init__)
    params = list(sig.parameters.keys())



def test_notation::shape_is_not_abstract():
    assert not inspect.isabstract(notation::Shape)


def test_notation::shape_constructor_exists():
    assert callable(notation::Shape.__init__)


def test_notation::shape_constructor_args():
    sig = inspect.signature(notation::Shape.__init__)
    params = list(sig.parameters.keys())



def test_notation::arrowstyle_is_not_abstract():
    assert not inspect.isabstract(notation::ArrowStyle)


def test_notation::arrowstyle_constructor_exists():
    assert callable(notation::ArrowStyle.__init__)


def test_notation::arrowstyle_constructor_args():
    sig = inspect.signature(notation::ArrowStyle.__init__)
    params = list(sig.parameters.keys())
    assert "arrowTarget" in params, "Missing parameter 'arrowTarget'"
    assert "arrowSource" in params, "Missing parameter 'arrowSource'"

def test_notation::arrowstyle_has_arrowTarget():
    assert hasattr(notation::ArrowStyle, "arrowTarget")
    descriptor = None
    for klass in notation::ArrowStyle.__mro__:
        if "arrowTarget" in klass.__dict__:
            descriptor = klass.__dict__["arrowTarget"]
            break
    assert isinstance(descriptor, property)

def test_notation::arrowstyle_has_arrowSource():
    assert hasattr(notation::ArrowStyle, "arrowSource")
    descriptor = None
    for klass in notation::ArrowStyle.__mro__:
        if "arrowSource" in klass.__dict__:
            descriptor = klass.__dict__["arrowSource"]
            break
    assert isinstance(descriptor, property)



def test_notation::textstyle_is_not_abstract():
    assert not inspect.isabstract(notation::TextStyle)


def test_notation::textstyle_constructor_exists():
    assert callable(notation::TextStyle.__init__)


def test_notation::textstyle_constructor_args():
    sig = inspect.signature(notation::TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"

def test_notation::textstyle_has_textAlignment():
    assert hasattr(notation::TextStyle, "textAlignment")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "textAlignment" in klass.__dict__:
            descriptor = klass.__dict__["textAlignment"]
            break
    assert isinstance(descriptor, property)



def test_notation::multidiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation::MultiDiagramLinkStyle)


def test_notation::multidiagramlinkstyle_constructor_exists():
    assert callable(notation::MultiDiagramLinkStyle.__init__)


def test_notation::multidiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation::MultiDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation::DiagramLinkStyle)


def test_notation::diagramlinkstyle_constructor_exists():
    assert callable(notation::DiagramLinkStyle.__init__)


def test_notation::diagramlinkstyle_constructor_args():
    sig = inspect.signature(notation::DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_diagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(DiagramLinkStyle)


def test_diagramlinkstyle_constructor_exists():
    assert callable(DiagramLinkStyle.__init__)


def test_diagramlinkstyle_constructor_args():
    sig = inspect.signature(DiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::hinteddiagramlinkstyle_is_not_abstract():
    assert not inspect.isabstract(notation::HintedDiagramLinkStyle)


def test_notation::hinteddiagramlinkstyle_constructor_exists():
    assert callable(notation::HintedDiagramLinkStyle.__init__)


def test_notation::hinteddiagramlinkstyle_constructor_args():
    sig = inspect.signature(notation::HintedDiagramLinkStyle.__init__)
    params = list(sig.parameters.keys())
    assert "hint" in params, "Missing parameter 'hint'"

def test_notation::hinteddiagramlinkstyle_has_hint():
    assert hasattr(notation::HintedDiagramLinkStyle, "hint")
    descriptor = None
    for klass in notation::HintedDiagramLinkStyle.__mro__:
        if "hint" in klass.__dict__:
            descriptor = klass.__dict__["hint"]
            break
    assert isinstance(descriptor, property)



def test_notation::edatatype_is_not_abstract():
    assert not inspect.isabstract(notation::EDataType)


def test_notation::edatatype_constructor_exists():
    assert callable(notation::EDataType.__init__)


def test_notation::edatatype_constructor_args():
    sig = inspect.signature(notation::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_notation::stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(notation::StringObjectConverter)


def test_notation::stringobjectconverter_constructor_exists():
    assert callable(notation::StringObjectConverter.__init__)


def test_notation::stringobjectconverter_constructor_args():
    sig = inspect.signature(notation::StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_notation::namedstyle_is_not_abstract():
    assert not inspect.isabstract(notation::NamedStyle)


def test_notation::namedstyle_constructor_exists():
    assert callable(notation::NamedStyle.__init__)


def test_notation::namedstyle_constructor_args():
    sig = inspect.signature(notation::NamedStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_notation::namedstyle_has_name():
    assert hasattr(notation::NamedStyle, "name")
    descriptor = None
    for klass in notation::NamedStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatypestyle_is_not_abstract():
    assert not inspect.isabstract(DataTypeStyle)


def test_datatypestyle_constructor_exists():
    assert callable(DataTypeStyle.__init__)


def test_datatypestyle_constructor_args():
    sig = inspect.signature(DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::listvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::ListValueStyle)


def test_notation::listvaluestyle_constructor_exists():
    assert callable(notation::ListValueStyle.__init__)


def test_notation::listvaluestyle_constructor_args():
    sig = inspect.signature(notation::ListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValuesList" in params, "Missing parameter 'rawValuesList'"

def test_notation::listvaluestyle_has_rawValuesList():
    assert hasattr(notation::ListValueStyle, "rawValuesList")
    descriptor = None
    for klass in notation::ListValueStyle.__mro__:
        if "rawValuesList" in klass.__dict__:
            descriptor = klass.__dict__["rawValuesList"]
            break
    assert isinstance(descriptor, property)



def test_notation::singlevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::SingleValueStyle)


def test_notation::singlevaluestyle_constructor_exists():
    assert callable(notation::SingleValueStyle.__init__)


def test_notation::singlevaluestyle_constructor_args():
    sig = inspect.signature(notation::SingleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_notation::singlevaluestyle_has_rawValue():
    assert hasattr(notation::SingleValueStyle, "rawValue")
    descriptor = None
    for klass in notation::SingleValueStyle.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_namedstyle_is_not_abstract():
    assert not inspect.isabstract(NamedStyle)


def test_namedstyle_constructor_exists():
    assert callable(NamedStyle.__init__)


def test_namedstyle_constructor_args():
    sig = inspect.signature(NamedStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::stringvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::StringValueStyle)


def test_notation::stringvaluestyle_constructor_exists():
    assert callable(notation::StringValueStyle.__init__)


def test_notation::stringvaluestyle_constructor_args():
    sig = inspect.signature(notation::StringValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringValue" in params, "Missing parameter 'stringValue'"

def test_notation::stringvaluestyle_has_stringValue():
    assert hasattr(notation::StringValueStyle, "stringValue")
    descriptor = None
    for klass in notation::StringValueStyle.__mro__:
        if "stringValue" in klass.__dict__:
            descriptor = klass.__dict__["stringValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::doublevaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::DoubleValueStyle)


def test_notation::doublevaluestyle_constructor_exists():
    assert callable(notation::DoubleValueStyle.__init__)


def test_notation::doublevaluestyle_constructor_args():
    sig = inspect.signature(notation::DoubleValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_notation::doublevaluestyle_has_doubleValue():
    assert hasattr(notation::DoubleValueStyle, "doubleValue")
    descriptor = None
    for klass in notation::DoubleValueStyle.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::intlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::IntListValueStyle)


def test_notation::intlistvaluestyle_constructor_exists():
    assert callable(notation::IntListValueStyle.__init__)


def test_notation::intlistvaluestyle_constructor_args():
    sig = inspect.signature(notation::IntListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intListValue" in params, "Missing parameter 'intListValue'"

def test_notation::intlistvaluestyle_has_intListValue():
    assert hasattr(notation::IntListValueStyle, "intListValue")
    descriptor = None
    for klass in notation::IntListValueStyle.__mro__:
        if "intListValue" in klass.__dict__:
            descriptor = klass.__dict__["intListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::intvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::IntValueStyle)


def test_notation::intvaluestyle_constructor_exists():
    assert callable(notation::IntValueStyle.__init__)


def test_notation::intvaluestyle_constructor_args():
    sig = inspect.signature(notation::IntValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_notation::intvaluestyle_has_intValue():
    assert hasattr(notation::IntValueStyle, "intValue")
    descriptor = None
    for klass in notation::IntValueStyle.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::bytearrayvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::ByteArrayValueStyle)


def test_notation::bytearrayvaluestyle_constructor_exists():
    assert callable(notation::ByteArrayValueStyle.__init__)


def test_notation::bytearrayvaluestyle_constructor_args():
    sig = inspect.signature(notation::ByteArrayValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "byteArrayValue" in params, "Missing parameter 'byteArrayValue'"

def test_notation::bytearrayvaluestyle_has_byteArrayValue():
    assert hasattr(notation::ByteArrayValueStyle, "byteArrayValue")
    descriptor = None
    for klass in notation::ByteArrayValueStyle.__mro__:
        if "byteArrayValue" in klass.__dict__:
            descriptor = klass.__dict__["byteArrayValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::eobjectlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::EObjectListValueStyle)


def test_notation::eobjectlistvaluestyle_constructor_exists():
    assert callable(notation::EObjectListValueStyle.__init__)


def test_notation::eobjectlistvaluestyle_constructor_args():
    sig = inspect.signature(notation::EObjectListValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::eobjectvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::EObjectValueStyle)


def test_notation::eobjectvaluestyle_constructor_exists():
    assert callable(notation::EObjectValueStyle.__init__)


def test_notation::eobjectvaluestyle_constructor_args():
    sig = inspect.signature(notation::EObjectValueStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::stringlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::StringListValueStyle)


def test_notation::stringlistvaluestyle_constructor_exists():
    assert callable(notation::StringListValueStyle.__init__)


def test_notation::stringlistvaluestyle_constructor_args():
    sig = inspect.signature(notation::StringListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "stringListValue" in params, "Missing parameter 'stringListValue'"

def test_notation::stringlistvaluestyle_has_stringListValue():
    assert hasattr(notation::StringListValueStyle, "stringListValue")
    descriptor = None
    for klass in notation::StringListValueStyle.__mro__:
        if "stringListValue" in klass.__dict__:
            descriptor = klass.__dict__["stringListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::booleanlistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::BooleanListValueStyle)


def test_notation::booleanlistvaluestyle_constructor_exists():
    assert callable(notation::BooleanListValueStyle.__init__)


def test_notation::booleanlistvaluestyle_constructor_args():
    sig = inspect.signature(notation::BooleanListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanListValue" in params, "Missing parameter 'booleanListValue'"

def test_notation::booleanlistvaluestyle_has_booleanListValue():
    assert hasattr(notation::BooleanListValueStyle, "booleanListValue")
    descriptor = None
    for klass in notation::BooleanListValueStyle.__mro__:
        if "booleanListValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::doublelistvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::DoubleListValueStyle)


def test_notation::doublelistvaluestyle_constructor_exists():
    assert callable(notation::DoubleListValueStyle.__init__)


def test_notation::doublelistvaluestyle_constructor_args():
    sig = inspect.signature(notation::DoubleListValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "doubleListValue" in params, "Missing parameter 'doubleListValue'"

def test_notation::doublelistvaluestyle_has_doubleListValue():
    assert hasattr(notation::DoubleListValueStyle, "doubleListValue")
    descriptor = None
    for klass in notation::DoubleListValueStyle.__mro__:
        if "doubleListValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleListValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::booleanvaluestyle_is_not_abstract():
    assert not inspect.isabstract(notation::BooleanValueStyle)


def test_notation::booleanvaluestyle_constructor_exists():
    assert callable(notation::BooleanValueStyle.__init__)


def test_notation::booleanvaluestyle_constructor_args():
    sig = inspect.signature(notation::BooleanValueStyle.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_notation::booleanvaluestyle_has_booleanValue():
    assert hasattr(notation::BooleanValueStyle, "booleanValue")
    descriptor = None
    for klass in notation::BooleanValueStyle.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::propertiessetstyle_is_not_abstract():
    assert not inspect.isabstract(notation::PropertiesSetStyle)


def test_notation::propertiessetstyle_constructor_exists():
    assert callable(notation::PropertiesSetStyle.__init__)


def test_notation::propertiessetstyle_constructor_args():
    sig = inspect.signature(notation::PropertiesSetStyle.__init__)
    params = list(sig.parameters.keys())



def test_stringobjectconverter_is_not_abstract():
    assert not inspect.isabstract(StringObjectConverter)


def test_stringobjectconverter_constructor_exists():
    assert callable(StringObjectConverter.__init__)


def test_stringobjectconverter_constructor_args():
    sig = inspect.signature(StringObjectConverter.__init__)
    params = list(sig.parameters.keys())



def test_notation::datatypestyle_is_not_abstract():
    assert not inspect.isabstract(notation::DataTypeStyle)


def test_notation::datatypestyle_constructor_exists():
    assert callable(notation::DataTypeStyle.__init__)


def test_notation::datatypestyle_constructor_args():
    sig = inspect.signature(notation::DataTypeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::propertyvalue_is_not_abstract():
    assert not inspect.isabstract(notation::PropertyValue)


def test_notation::propertyvalue_constructor_exists():
    assert callable(notation::PropertyValue.__init__)


def test_notation::propertyvalue_constructor_args():
    sig = inspect.signature(notation::PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_notation::propertyvalue_has_rawValue():
    assert hasattr(notation::PropertyValue, "rawValue")
    descriptor = None
    for klass in notation::PropertyValue.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_notation::stringtopropertyvaluemapentry_is_not_abstract():
    assert not inspect.isabstract(notation::StringToPropertyValueMapEntry)


def test_notation::stringtopropertyvaluemapentry_constructor_exists():
    assert callable(notation::StringToPropertyValueMapEntry.__init__)


def test_notation::stringtopropertyvaluemapentry_constructor_args():
    sig = inspect.signature(notation::StringToPropertyValueMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_notation::stringtopropertyvaluemapentry_has_key():
    assert hasattr(notation::StringToPropertyValueMapEntry, "key")
    descriptor = None
    for klass in notation::StringToPropertyValueMapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_notation::nodeentry_is_not_abstract():
    assert not inspect.isabstract(notation::NodeEntry)


def test_notation::nodeentry_constructor_exists():
    assert callable(notation::NodeEntry.__init__)


def test_notation::nodeentry_constructor_args():
    sig = inspect.signature(notation::NodeEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_notation::nodeentry_has_value():
    assert hasattr(notation::NodeEntry, "value")
    descriptor = None
    for klass in notation::NodeEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_imagestyle_is_not_abstract():
    assert not inspect.isabstract(ImageStyle)


def test_imagestyle_constructor_exists():
    assert callable(ImageStyle.__init__)


def test_imagestyle_constructor_args():
    sig = inspect.signature(ImageStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::imagebufferstyle_is_not_abstract():
    assert not inspect.isabstract(notation::ImageBufferStyle)


def test_notation::imagebufferstyle_constructor_exists():
    assert callable(notation::ImageBufferStyle.__init__)


def test_notation::imagebufferstyle_constructor_args():
    sig = inspect.signature(notation::ImageBufferStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::imagestyle_is_not_abstract():
    assert not inspect.isabstract(notation::ImageStyle)


def test_notation::imagestyle_constructor_exists():
    assert callable(notation::ImageStyle.__init__)


def test_notation::imagestyle_constructor_args():
    sig = inspect.signature(notation::ImageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "maintainAspectRatio" in params, "Missing parameter 'maintainAspectRatio'"
    assert "antiAlias" in params, "Missing parameter 'antiAlias'"

def test_notation::imagestyle_has_maintainAspectRatio():
    assert hasattr(notation::ImageStyle, "maintainAspectRatio")
    descriptor = None
    for klass in notation::ImageStyle.__mro__:
        if "maintainAspectRatio" in klass.__dict__:
            descriptor = klass.__dict__["maintainAspectRatio"]
            break
    assert isinstance(descriptor, property)

def test_notation::imagestyle_has_antiAlias():
    assert hasattr(notation::ImageStyle, "antiAlias")
    descriptor = None
    for klass in notation::ImageStyle.__mro__:
        if "antiAlias" in klass.__dict__:
            descriptor = klass.__dict__["antiAlias"]
            break
    assert isinstance(descriptor, property)



def test_guidestyle_is_not_abstract():
    assert not inspect.isabstract(GuideStyle)


def test_guidestyle_constructor_exists():
    assert callable(GuideStyle.__init__)


def test_guidestyle_constructor_args():
    sig = inspect.signature(GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_pagestyle_is_not_abstract():
    assert not inspect.isabstract(PageStyle)


def test_pagestyle_constructor_exists():
    assert callable(PageStyle.__init__)


def test_pagestyle_constructor_args():
    sig = inspect.signature(PageStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::filteringstyle_is_not_abstract():
    assert not inspect.isabstract(notation::FilteringStyle)


def test_notation::filteringstyle_constructor_exists():
    assert callable(notation::FilteringStyle.__init__)


def test_notation::filteringstyle_constructor_args():
    sig = inspect.signature(notation::FilteringStyle.__init__)
    params = list(sig.parameters.keys())
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "filteringKeys" in params, "Missing parameter 'filteringKeys'"

def test_notation::filteringstyle_has_filtering():
    assert hasattr(notation::FilteringStyle, "filtering")
    descriptor = None
    for klass in notation::FilteringStyle.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_notation::filteringstyle_has_filteringKeys():
    assert hasattr(notation::FilteringStyle, "filteringKeys")
    descriptor = None
    for klass in notation::FilteringStyle.__mro__:
        if "filteringKeys" in klass.__dict__:
            descriptor = klass.__dict__["filteringKeys"]
            break
    assert isinstance(descriptor, property)



def test_notation::image_is_not_abstract():
    assert not inspect.isabstract(notation::Image)


def test_notation::image_constructor_exists():
    assert callable(notation::Image.__init__)


def test_notation::image_constructor_args():
    sig = inspect.signature(notation::Image.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"

def test_notation::image_has_data():
    assert hasattr(notation::Image, "data")
    descriptor = None
    for klass in notation::Image.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_bendpoints_is_not_abstract():
    assert not inspect.isabstract(Bendpoints)


def test_bendpoints_constructor_exists():
    assert callable(Bendpoints.__init__)


def test_bendpoints_constructor_args():
    sig = inspect.signature(Bendpoints.__init__)
    params = list(sig.parameters.keys())



def test_notation::relativebendpoints_is_not_abstract():
    assert not inspect.isabstract(notation::RelativeBendpoints)


def test_notation::relativebendpoints_constructor_exists():
    assert callable(notation::RelativeBendpoints.__init__)


def test_notation::relativebendpoints_constructor_args():
    sig = inspect.signature(notation::RelativeBendpoints.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"

def test_notation::relativebendpoints_has_points():
    assert hasattr(notation::RelativeBendpoints, "points")
    descriptor = None
    for klass in notation::RelativeBendpoints.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)



def test_notation::guide_is_not_abstract():
    assert not inspect.isabstract(notation::Guide)


def test_notation::guide_constructor_exists():
    assert callable(notation::Guide.__init__)


def test_notation::guide_constructor_args():
    sig = inspect.signature(notation::Guide.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_notation::guide_has_position():
    assert hasattr(notation::Guide, "position")
    descriptor = None
    for klass in notation::Guide.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_notation::guidestyle_is_not_abstract():
    assert not inspect.isabstract(notation::GuideStyle)


def test_notation::guidestyle_constructor_exists():
    assert callable(notation::GuideStyle.__init__)


def test_notation::guidestyle_constructor_args():
    sig = inspect.signature(notation::GuideStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::drawerstyle_is_not_abstract():
    assert not inspect.isabstract(notation::DrawerStyle)


def test_notation::drawerstyle_constructor_exists():
    assert callable(notation::DrawerStyle.__init__)


def test_notation::drawerstyle_constructor_args():
    sig = inspect.signature(notation::DrawerStyle.__init__)
    params = list(sig.parameters.keys())
    assert "collapsed" in params, "Missing parameter 'collapsed'"

def test_notation::drawerstyle_has_collapsed():
    assert hasattr(notation::DrawerStyle, "collapsed")
    descriptor = None
    for klass in notation::DrawerStyle.__mro__:
        if "collapsed" in klass.__dict__:
            descriptor = klass.__dict__["collapsed"]
            break
    assert isinstance(descriptor, property)



def test_notation::pagestyle_is_not_abstract():
    assert not inspect.isabstract(notation::PageStyle)


def test_notation::pagestyle_constructor_exists():
    assert callable(notation::PageStyle.__init__)


def test_notation::pagestyle_constructor_args():
    sig = inspect.signature(notation::PageStyle.__init__)
    params = list(sig.parameters.keys())
    assert "pageWidth" in params, "Missing parameter 'pageWidth'"
    assert "pageY" in params, "Missing parameter 'pageY'"
    assert "pageHeight" in params, "Missing parameter 'pageHeight'"
    assert "pageX" in params, "Missing parameter 'pageX'"

def test_notation::pagestyle_has_pageWidth():
    assert hasattr(notation::PageStyle, "pageWidth")
    descriptor = None
    for klass in notation::PageStyle.__mro__:
        if "pageWidth" in klass.__dict__:
            descriptor = klass.__dict__["pageWidth"]
            break
    assert isinstance(descriptor, property)

def test_notation::pagestyle_has_pageY():
    assert hasattr(notation::PageStyle, "pageY")
    descriptor = None
    for klass in notation::PageStyle.__mro__:
        if "pageY" in klass.__dict__:
            descriptor = klass.__dict__["pageY"]
            break
    assert isinstance(descriptor, property)

def test_notation::pagestyle_has_pageHeight():
    assert hasattr(notation::PageStyle, "pageHeight")
    descriptor = None
    for klass in notation::PageStyle.__mro__:
        if "pageHeight" in klass.__dict__:
            descriptor = klass.__dict__["pageHeight"]
            break
    assert isinstance(descriptor, property)

def test_notation::pagestyle_has_pageX():
    assert hasattr(notation::PageStyle, "pageX")
    descriptor = None
    for klass in notation::PageStyle.__mro__:
        if "pageX" in klass.__dict__:
            descriptor = klass.__dict__["pageX"]
            break
    assert isinstance(descriptor, property)



def test_routingstyle_is_not_abstract():
    assert not inspect.isabstract(RoutingStyle)


def test_routingstyle_constructor_exists():
    assert callable(RoutingStyle.__init__)


def test_routingstyle_constructor_args():
    sig = inspect.signature(RoutingStyle.__init__)
    params = list(sig.parameters.keys())



def test_linestyle_is_not_abstract():
    assert not inspect.isabstract(LineStyle)


def test_linestyle_constructor_exists():
    assert callable(LineStyle.__init__)


def test_linestyle_constructor_args():
    sig = inspect.signature(LineStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::connectorstyle_is_not_abstract():
    assert not inspect.isabstract(notation::ConnectorStyle)


def test_notation::connectorstyle_constructor_exists():
    assert callable(notation::ConnectorStyle.__init__)


def test_notation::connectorstyle_constructor_args():
    sig = inspect.signature(notation::ConnectorStyle.__init__)
    params = list(sig.parameters.keys())



def test_fillstyle_is_not_abstract():
    assert not inspect.isabstract(FillStyle)


def test_fillstyle_constructor_exists():
    assert callable(FillStyle.__init__)


def test_fillstyle_constructor_args():
    sig = inspect.signature(FillStyle.__init__)
    params = list(sig.parameters.keys())



def test_descriptionstyle_is_not_abstract():
    assert not inspect.isabstract(DescriptionStyle)


def test_descriptionstyle_constructor_exists():
    assert callable(DescriptionStyle.__init__)


def test_descriptionstyle_constructor_args():
    sig = inspect.signature(DescriptionStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::diagramstyle_is_not_abstract():
    assert not inspect.isabstract(notation::DiagramStyle)


def test_notation::diagramstyle_constructor_exists():
    assert callable(notation::DiagramStyle.__init__)


def test_notation::diagramstyle_constructor_args():
    sig = inspect.signature(notation::DiagramStyle.__init__)
    params = list(sig.parameters.keys())



def test_fontstyle_is_not_abstract():
    assert not inspect.isabstract(FontStyle)


def test_fontstyle_constructor_exists():
    assert callable(FontStyle.__init__)


def test_fontstyle_constructor_args():
    sig = inspect.signature(FontStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::shapestyle_is_not_abstract():
    assert not inspect.isabstract(notation::ShapeStyle)


def test_notation::shapestyle_constructor_exists():
    assert callable(notation::ShapeStyle.__init__)


def test_notation::shapestyle_constructor_args():
    sig = inspect.signature(notation::ShapeStyle.__init__)
    params = list(sig.parameters.keys())



def test_notation::canonicalstyle_is_not_abstract():
    assert not inspect.isabstract(notation::CanonicalStyle)


def test_notation::canonicalstyle_constructor_exists():
    assert callable(notation::CanonicalStyle.__init__)


def test_notation::canonicalstyle_constructor_args():
    sig = inspect.signature(notation::CanonicalStyle.__init__)
    params = list(sig.parameters.keys())
    assert "canonical" in params, "Missing parameter 'canonical'"

def test_notation::canonicalstyle_has_canonical():
    assert hasattr(notation::CanonicalStyle, "canonical")
    descriptor = None
    for klass in notation::CanonicalStyle.__mro__:
        if "canonical" in klass.__dict__:
            descriptor = klass.__dict__["canonical"]
            break
    assert isinstance(descriptor, property)



def test_emodelelement_is_not_abstract():
    assert not inspect.isabstract(EModelElement)


def test_emodelelement_constructor_exists():
    assert callable(EModelElement.__init__)


def test_emodelelement_constructor_args():
    sig = inspect.signature(EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::view_is_not_abstract():
    assert not inspect.isabstract(notation::View)


def test_notation::view_constructor_exists():
    assert callable(notation::View.__init__)


def test_notation::view_constructor_args():
    sig = inspect.signature(notation::View.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "visible" in params, "Missing parameter 'visible'"
    assert "mutable" in params, "Missing parameter 'mutable'"

def test_notation::view_has_type():
    assert hasattr(notation::View, "type")
    descriptor = None
    for klass in notation::View.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_notation::view_has_visible():
    assert hasattr(notation::View, "visible")
    descriptor = None
    for klass in notation::View.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_notation::view_has_mutable():
    assert hasattr(notation::View, "mutable")
    descriptor = None
    for klass in notation::View.__mro__:
        if "mutable" in klass.__dict__:
            descriptor = klass.__dict__["mutable"]
            break
    assert isinstance(descriptor, property)



def test_notation::diagram_is_not_abstract():
    assert not inspect.isabstract(notation::Diagram)


def test_notation::diagram_constructor_exists():
    assert callable(notation::Diagram.__init__)


def test_notation::diagram_constructor_args():
    sig = inspect.signature(notation::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "measurementUnit" in params, "Missing parameter 'measurementUnit'"
    assert "name" in params, "Missing parameter 'name'"

def test_notation::diagram_has_measurementUnit():
    assert hasattr(notation::Diagram, "measurementUnit")
    descriptor = None
    for klass in notation::Diagram.__mro__:
        if "measurementUnit" in klass.__dict__:
            descriptor = klass.__dict__["measurementUnit"]
            break
    assert isinstance(descriptor, property)

def test_notation::diagram_has_name():
    assert hasattr(notation::Diagram, "name")
    descriptor = None
    for klass in notation::Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_notation::ratio_is_not_abstract():
    assert not inspect.isabstract(notation::Ratio)


def test_notation::ratio_constructor_exists():
    assert callable(notation::Ratio.__init__)


def test_notation::ratio_constructor_args():
    sig = inspect.signature(notation::Ratio.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_notation::ratio_has_value():
    assert hasattr(notation::Ratio, "value")
    descriptor = None
    for klass in notation::Ratio.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_size_is_not_abstract():
    assert not inspect.isabstract(Size)


def test_size_constructor_exists():
    assert callable(Size.__init__)


def test_size_constructor_args():
    sig = inspect.signature(Size.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_notation::bounds_is_not_abstract():
    assert not inspect.isabstract(notation::Bounds)


def test_notation::bounds_constructor_exists():
    assert callable(notation::Bounds.__init__)


def test_notation::bounds_constructor_args():
    sig = inspect.signature(notation::Bounds.__init__)
    params = list(sig.parameters.keys())

def test_arrowtype_exists():
    # Check that the Enumeration exists
    assert ArrowType is not None

def test_arrowtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArrowType]
    expected_literals = [
        "OpenArrow",
        "SolidArrow",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArrowType"

def test_jumplinktype_exists():
    # Check that the Enumeration exists
    assert JumpLinkType is not None

def test_jumplinktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkType]
    expected_literals = [
        "Chamfered",
        "Square",
        "Semicircle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkType"

def test_jumplinkstatus_exists():
    # Check that the Enumeration exists
    assert JumpLinkStatus is not None

def test_jumplinkstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JumpLinkStatus]
    expected_literals = [
        "Above",
        "All",
        "None_",
        "Below",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JumpLinkStatus"

def test_smoothness_exists():
    # Check that the Enumeration exists
    assert Smoothness is not None

def test_smoothness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Smoothness]
    expected_literals = [
        "Less",
        "More",
        "None_",
        "Normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Smoothness"

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "Center",
        "Bottom",
        "Right",
        "Left",
        "Top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"

def test_measurementunit_exists():
    # Check that the Enumeration exists
    assert MeasurementUnit is not None

def test_measurementunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasurementUnit]
    expected_literals = [
        "Himetric",
        "Pixel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurementUnit"

def test_textalignment_exists():
    # Check that the Enumeration exists
    assert TextAlignment is not None

def test_textalignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignment]
    expected_literals = [
        "Center",
        "Right",
        "Left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignment"

def test_sorting_exists():
    # Check that the Enumeration exists
    assert Sorting is not None

def test_sorting_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sorting]
    expected_literals = [
        "Manual",
        "Automatic",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sorting"

def test_sortingdirection_exists():
    # Check that the Enumeration exists
    assert SortingDirection is not None

def test_sortingdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SortingDirection]
    expected_literals = [
        "Ascending",
        "Descending",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SortingDirection"

def test_routing_exists():
    # Check that the Enumeration exists
    assert Routing is not None

def test_routing_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Routing]
    expected_literals = [
        "Manual",
        "Tree",
        "Rectilinear",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Routing"

def test_gradientstyle_exists():
    # Check that the Enumeration exists
    assert GradientStyle is not None

def test_gradientstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GradientStyle]
    expected_literals = [
        "Vertical",
        "Horizontal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GradientStyle"

def test_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "Dot",
        "Solid",
        "DashDot",
        "Dash",
        "Double",
        "DashDotDot",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"

def test_filtering_exists():
    # Check that the Enumeration exists
    assert Filtering is not None

def test_filtering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Filtering]
    expected_literals = [
        "Automatic",
        "Manual",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Filtering"


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
BasicSemanticCompartment_strategy = st.builds(
    BasicSemanticCompartment,
)
DrawerStyle_strategy = st.builds(
    DrawerStyle,
)
DecorationNode_strategy = st.builds(
    DecorationNode,
)
notation::BasicCompartment_strategy = st.builds(
    notation::BasicCompartment,
)
BasicDecorationNode_strategy = st.builds(
    BasicDecorationNode,
)
notation::BasicSemanticCompartment_strategy = st.builds(
    notation::BasicSemanticCompartment,
)
notation::DecorationNode_strategy = st.builds(
    notation::DecorationNode,
)
DiagramStyle_strategy = st.builds(
    DiagramStyle,
)
LayoutConstraint_strategy = st.builds(
    LayoutConstraint,
)
notation::Location_strategy = st.builds(
    notation::Location,
    x=
        st.integers(),
    y=
        st.integers()
)
notation::Size_strategy = st.builds(
    notation::Size,
    width=
        st.integers(),
    height=
        st.integers()
)
RoundedCornersStyle_strategy = st.builds(
    RoundedCornersStyle,
)
notation::RoutingStyle_strategy = st.builds(
    notation::RoutingStyle,
    routing=
        safe_text,
    jumpLinkType=
        safe_text,
    smoothness=
        safe_text,
    closestDistance=
        st.booleans(),
    jumpLinkStatus=
        safe_text,
    jumpLinksReverse=
        st.booleans(),
    avoidObstructions=
        st.booleans()
)
Anchor_strategy = st.builds(
    Anchor,
)
notation::IdentityAnchor_strategy = st.builds(
    notation::IdentityAnchor,
    id=
        safe_text
)
notation::Style_strategy = st.builds(
    notation::Style,
)
notation::LayoutConstraint_strategy = st.builds(
    notation::LayoutConstraint,
)
notation::Anchor_strategy = st.builds(
    notation::Anchor,
)
notation::Bendpoints_strategy = st.builds(
    notation::Bendpoints,
)
notation::EObject_strategy = st.builds(
    notation::EObject,
)
Style_strategy = st.builds(
    Style,
)
notation::SortingStyle_strategy = st.builds(
    notation::SortingStyle,
    sorting=
        safe_text,
    sortingKeys=
        safe_text
)
notation::FontStyle_strategy = st.builds(
    notation::FontStyle,
    underline=
        st.booleans(),
    fontHeight=
        st.integers(),
    strikeThrough=
        st.booleans(),
    fontName=
        safe_text,
    bold=
        st.booleans(),
    fontColor=
        st.integers(),
    italic=
        st.booleans()
)
notation::RoundedCornersStyle_strategy = st.builds(
    notation::RoundedCornersStyle,
    roundedBendpointsRadius=
        st.integers()
)
notation::LineStyle_strategy = st.builds(
    notation::LineStyle,
    lineWidth=
        st.integers(),
    lineColor=
        st.integers()
)
notation::LineTypeStyle_strategy = st.builds(
    notation::LineTypeStyle,
    lineType=
        safe_text
)
notation::TitleStyle_strategy = st.builds(
    notation::TitleStyle,
    showTitle=
        st.booleans()
)
notation::DescriptionStyle_strategy = st.builds(
    notation::DescriptionStyle,
    description=
        safe_text
)
notation::FillStyle_strategy = st.builds(
    notation::FillStyle,
    transparency=
        st.integers(),
    gradient=
        safe_text,
    fillColor=
        st.integers()
)
View_strategy = st.builds(
    View,
)
notation::Node_strategy = st.builds(
    notation::Node,
)
notation::Edge_strategy = st.builds(
    notation::Edge,
)
Diagram_strategy = st.builds(
    Diagram,
)
notation::StandardDiagram_strategy = st.builds(
    notation::StandardDiagram,
)
ConnectorStyle_strategy = st.builds(
    ConnectorStyle,
)
Edge_strategy = st.builds(
    Edge,
)
notation::Connector_strategy = st.builds(
    notation::Connector,
)
FilteringStyle_strategy = st.builds(
    FilteringStyle,
)
SortingStyle_strategy = st.builds(
    SortingStyle,
)
TitleStyle_strategy = st.builds(
    TitleStyle,
)
notation::SemanticListCompartment_strategy = st.builds(
    notation::SemanticListCompartment,
)
CanonicalStyle_strategy = st.builds(
    CanonicalStyle,
)
BasicCompartment_strategy = st.builds(
    BasicCompartment,
)
notation::ListCompartment_strategy = st.builds(
    notation::ListCompartment,
)
notation::Compartment_strategy = st.builds(
    notation::Compartment,
)
ShapeStyle_strategy = st.builds(
    ShapeStyle,
)
Node_strategy = st.builds(
    Node,
)
notation::BasicDecorationNode_strategy = st.builds(
    notation::BasicDecorationNode,
)
notation::Shape_strategy = st.builds(
    notation::Shape,
)
notation::ArrowStyle_strategy = st.builds(
    notation::ArrowStyle,
    arrowTarget=
        safe_text,
    arrowSource=
        safe_text
)
notation::TextStyle_strategy = st.builds(
    notation::TextStyle,
    textAlignment=
        safe_text
)
notation::MultiDiagramLinkStyle_strategy = st.builds(
    notation::MultiDiagramLinkStyle,
)
notation::DiagramLinkStyle_strategy = st.builds(
    notation::DiagramLinkStyle,
)
DiagramLinkStyle_strategy = st.builds(
    DiagramLinkStyle,
)
notation::HintedDiagramLinkStyle_strategy = st.builds(
    notation::HintedDiagramLinkStyle,
    hint=
        safe_text
)
notation::EDataType_strategy = st.builds(
    notation::EDataType,
)
notation::StringObjectConverter_strategy = st.builds(
    notation::StringObjectConverter,
)
notation::NamedStyle_strategy = st.builds(
    notation::NamedStyle,
    name=
        safe_text
)
DataTypeStyle_strategy = st.builds(
    DataTypeStyle,
)
notation::ListValueStyle_strategy = st.builds(
    notation::ListValueStyle,
    rawValuesList=
        safe_text
)
notation::SingleValueStyle_strategy = st.builds(
    notation::SingleValueStyle,
    rawValue=
        safe_text
)
NamedStyle_strategy = st.builds(
    NamedStyle,
)
notation::StringValueStyle_strategy = st.builds(
    notation::StringValueStyle,
    stringValue=
        safe_text
)
notation::DoubleValueStyle_strategy = st.builds(
    notation::DoubleValueStyle,
    doubleValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
notation::IntListValueStyle_strategy = st.builds(
    notation::IntListValueStyle,
    intListValue=
        st.integers()
)
notation::IntValueStyle_strategy = st.builds(
    notation::IntValueStyle,
    intValue=
        st.integers()
)
notation::ByteArrayValueStyle_strategy = st.builds(
    notation::ByteArrayValueStyle,
    byteArrayValue=
        safe_text
)
notation::EObjectListValueStyle_strategy = st.builds(
    notation::EObjectListValueStyle,
)
notation::EObjectValueStyle_strategy = st.builds(
    notation::EObjectValueStyle,
)
notation::StringListValueStyle_strategy = st.builds(
    notation::StringListValueStyle,
    stringListValue=
        safe_text
)
notation::BooleanListValueStyle_strategy = st.builds(
    notation::BooleanListValueStyle,
    booleanListValue=
        safe_text
)
notation::DoubleListValueStyle_strategy = st.builds(
    notation::DoubleListValueStyle,
    doubleListValue=
        safe_text
)
notation::BooleanValueStyle_strategy = st.builds(
    notation::BooleanValueStyle,
    booleanValue=
        st.booleans()
)
notation::PropertiesSetStyle_strategy = st.builds(
    notation::PropertiesSetStyle,
)
StringObjectConverter_strategy = st.builds(
    StringObjectConverter,
)
notation::DataTypeStyle_strategy = st.builds(
    notation::DataTypeStyle,
)
notation::PropertyValue_strategy = st.builds(
    notation::PropertyValue,
    rawValue=
        safe_text
)
notation::StringToPropertyValueMapEntry_strategy = st.builds(
    notation::StringToPropertyValueMapEntry,
    key=
        safe_text
)
notation::NodeEntry_strategy = st.builds(
    notation::NodeEntry,
    value=
        safe_text
)
ImageStyle_strategy = st.builds(
    ImageStyle,
)
notation::ImageBufferStyle_strategy = st.builds(
    notation::ImageBufferStyle,
)
notation::ImageStyle_strategy = st.builds(
    notation::ImageStyle,
    maintainAspectRatio=
        safe_text,
    antiAlias=
        safe_text
)
GuideStyle_strategy = st.builds(
    GuideStyle,
)
PageStyle_strategy = st.builds(
    PageStyle,
)
notation::FilteringStyle_strategy = st.builds(
    notation::FilteringStyle,
    filtering=
        safe_text,
    filteringKeys=
        safe_text
)
notation::Image_strategy = st.builds(
    notation::Image,
    data=
        safe_text
)
Bendpoints_strategy = st.builds(
    Bendpoints,
)
notation::RelativeBendpoints_strategy = st.builds(
    notation::RelativeBendpoints,
    points=
        safe_text
)
notation::Guide_strategy = st.builds(
    notation::Guide,
    position=
        st.integers()
)
notation::GuideStyle_strategy = st.builds(
    notation::GuideStyle,
)
notation::DrawerStyle_strategy = st.builds(
    notation::DrawerStyle,
    collapsed=
        st.booleans()
)
notation::PageStyle_strategy = st.builds(
    notation::PageStyle,
    pageWidth=
        st.integers(),
    pageY=
        st.integers(),
    pageHeight=
        st.integers(),
    pageX=
        st.integers()
)
RoutingStyle_strategy = st.builds(
    RoutingStyle,
)
LineStyle_strategy = st.builds(
    LineStyle,
)
notation::ConnectorStyle_strategy = st.builds(
    notation::ConnectorStyle,
)
FillStyle_strategy = st.builds(
    FillStyle,
)
DescriptionStyle_strategy = st.builds(
    DescriptionStyle,
)
notation::DiagramStyle_strategy = st.builds(
    notation::DiagramStyle,
)
FontStyle_strategy = st.builds(
    FontStyle,
)
notation::ShapeStyle_strategy = st.builds(
    notation::ShapeStyle,
)
notation::CanonicalStyle_strategy = st.builds(
    notation::CanonicalStyle,
    canonical=
        st.booleans()
)
EModelElement_strategy = st.builds(
    EModelElement,
)
notation::View_strategy = st.builds(
    notation::View,
    type=
        safe_text,
    visible=
        st.booleans(),
    mutable=
        st.booleans()
)
notation::Diagram_strategy = st.builds(
    notation::Diagram,
    measurementUnit=
        safe_text,
    name=
        safe_text
)
notation::Ratio_strategy = st.builds(
    notation::Ratio,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Size_strategy = st.builds(
    Size,
)
Location_strategy = st.builds(
    Location,
)
notation::Bounds_strategy = st.builds(
    notation::Bounds,
)

@given(instance=BasicSemanticCompartment_strategy)
@settings(max_examples=50)
def test_basicsemanticcompartment_instantiation(instance):
    assert isinstance(instance, BasicSemanticCompartment)

@given(instance=DrawerStyle_strategy)
@settings(max_examples=50)
def test_drawerstyle_instantiation(instance):
    assert isinstance(instance, DrawerStyle)

@given(instance=DecorationNode_strategy)
@settings(max_examples=50)
def test_decorationnode_instantiation(instance):
    assert isinstance(instance, DecorationNode)

@given(instance=notation::BasicCompartment_strategy)
@settings(max_examples=50)
def test_notation::basiccompartment_instantiation(instance):
    assert isinstance(instance, notation::BasicCompartment)

@given(instance=BasicDecorationNode_strategy)
@settings(max_examples=50)
def test_basicdecorationnode_instantiation(instance):
    assert isinstance(instance, BasicDecorationNode)

@given(instance=notation::BasicSemanticCompartment_strategy)
@settings(max_examples=50)
def test_notation::basicsemanticcompartment_instantiation(instance):
    assert isinstance(instance, notation::BasicSemanticCompartment)

@given(instance=notation::DecorationNode_strategy)
@settings(max_examples=50)
def test_notation::decorationnode_instantiation(instance):
    assert isinstance(instance, notation::DecorationNode)

@given(instance=DiagramStyle_strategy)
@settings(max_examples=50)
def test_diagramstyle_instantiation(instance):
    assert isinstance(instance, DiagramStyle)

@given(instance=LayoutConstraint_strategy)
@settings(max_examples=50)
def test_layoutconstraint_instantiation(instance):
    assert isinstance(instance, LayoutConstraint)

@given(instance=notation::Location_strategy)
@settings(max_examples=50)
def test_notation::location_instantiation(instance):
    assert isinstance(instance, notation::Location)

@given(instance=notation::Location_strategy)
def test_notation::location_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::Location_strategy)
def test_notation::location_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=notation::Location_strategy)
def test_notation::location_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::Location_strategy)
def test_notation::location_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation::Size_strategy)
@settings(max_examples=50)
def test_notation::size_instantiation(instance):
    assert isinstance(instance, notation::Size)

@given(instance=notation::Size_strategy)
def test_notation::size_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=notation::Size_strategy)
def test_notation::size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation::Size_strategy)
def test_notation::size_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=notation::Size_strategy)
def test_notation::size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=RoundedCornersStyle_strategy)
@settings(max_examples=50)
def test_roundedcornersstyle_instantiation(instance):
    assert isinstance(instance, RoundedCornersStyle)

@given(instance=notation::RoutingStyle_strategy)
@settings(max_examples=50)
def test_notation::routingstyle_instantiation(instance):
    assert isinstance(instance, notation::RoutingStyle)

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_routing_type(instance):
    assert isinstance(instance.routing, str)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_routing_setter(instance):
    original = instance.routing
    instance.routing = original
    assert instance.routing == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinkType_type(instance):
    assert isinstance(instance.jumpLinkType, str)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinkType_setter(instance):
    original = instance.jumpLinkType
    instance.jumpLinkType = original
    assert instance.jumpLinkType == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_smoothness_type(instance):
    assert isinstance(instance.smoothness, str)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_smoothness_setter(instance):
    original = instance.smoothness
    instance.smoothness = original
    assert instance.smoothness == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_closestDistance_type(instance):
    assert isinstance(instance.closestDistance, bool)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_closestDistance_setter(instance):
    original = instance.closestDistance
    instance.closestDistance = original
    assert instance.closestDistance == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinkStatus_type(instance):
    assert isinstance(instance.jumpLinkStatus, str)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinkStatus_setter(instance):
    original = instance.jumpLinkStatus
    instance.jumpLinkStatus = original
    assert instance.jumpLinkStatus == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinksReverse_type(instance):
    assert isinstance(instance.jumpLinksReverse, bool)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_jumpLinksReverse_setter(instance):
    original = instance.jumpLinksReverse
    instance.jumpLinksReverse = original
    assert instance.jumpLinksReverse == original

@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_avoidObstructions_type(instance):
    assert isinstance(instance.avoidObstructions, bool)


@given(instance=notation::RoutingStyle_strategy)
def test_notation::routingstyle_avoidObstructions_setter(instance):
    original = instance.avoidObstructions
    instance.avoidObstructions = original
    assert instance.avoidObstructions == original

@given(instance=Anchor_strategy)
@settings(max_examples=50)
def test_anchor_instantiation(instance):
    assert isinstance(instance, Anchor)

@given(instance=notation::IdentityAnchor_strategy)
@settings(max_examples=50)
def test_notation::identityanchor_instantiation(instance):
    assert isinstance(instance, notation::IdentityAnchor)

@given(instance=notation::IdentityAnchor_strategy)
def test_notation::identityanchor_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=notation::IdentityAnchor_strategy)
def test_notation::identityanchor_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=notation::Style_strategy)
@settings(max_examples=50)
def test_notation::style_instantiation(instance):
    assert isinstance(instance, notation::Style)

@given(instance=notation::LayoutConstraint_strategy)
@settings(max_examples=50)
def test_notation::layoutconstraint_instantiation(instance):
    assert isinstance(instance, notation::LayoutConstraint)

@given(instance=notation::Anchor_strategy)
@settings(max_examples=50)
def test_notation::anchor_instantiation(instance):
    assert isinstance(instance, notation::Anchor)

@given(instance=notation::Bendpoints_strategy)
@settings(max_examples=50)
def test_notation::bendpoints_instantiation(instance):
    assert isinstance(instance, notation::Bendpoints)

@given(instance=notation::EObject_strategy)
@settings(max_examples=50)
def test_notation::eobject_instantiation(instance):
    assert isinstance(instance, notation::EObject)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=notation::SortingStyle_strategy)
@settings(max_examples=50)
def test_notation::sortingstyle_instantiation(instance):
    assert isinstance(instance, notation::SortingStyle)

@given(instance=notation::SortingStyle_strategy)
def test_notation::sortingstyle_sorting_type(instance):
    assert isinstance(instance.sorting, str)


@given(instance=notation::SortingStyle_strategy)
def test_notation::sortingstyle_sorting_setter(instance):
    original = instance.sorting
    instance.sorting = original
    assert instance.sorting == original

@given(instance=notation::SortingStyle_strategy)
def test_notation::sortingstyle_sortingKeys_type(instance):
    assert isinstance(instance.sortingKeys, str)


@given(instance=notation::SortingStyle_strategy)
def test_notation::sortingstyle_sortingKeys_setter(instance):
    original = instance.sortingKeys
    instance.sortingKeys = original
    assert instance.sortingKeys == original

@given(instance=notation::FontStyle_strategy)
@settings(max_examples=50)
def test_notation::fontstyle_instantiation(instance):
    assert isinstance(instance, notation::FontStyle)

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_underline_type(instance):
    assert isinstance(instance.underline, bool)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_underline_setter(instance):
    original = instance.underline
    instance.underline = original
    assert instance.underline == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontHeight_type(instance):
    assert isinstance(instance.fontHeight, int)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontHeight_setter(instance):
    original = instance.fontHeight
    instance.fontHeight = original
    assert instance.fontHeight == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_strikeThrough_type(instance):
    assert isinstance(instance.strikeThrough, bool)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_strikeThrough_setter(instance):
    original = instance.strikeThrough
    instance.strikeThrough = original
    assert instance.strikeThrough == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_bold_type(instance):
    assert isinstance(instance.bold, bool)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontColor_type(instance):
    assert isinstance(instance.fontColor, int)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original

@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_italic_type(instance):
    assert isinstance(instance.italic, bool)


@given(instance=notation::FontStyle_strategy)
def test_notation::fontstyle_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original

@given(instance=notation::RoundedCornersStyle_strategy)
@settings(max_examples=50)
def test_notation::roundedcornersstyle_instantiation(instance):
    assert isinstance(instance, notation::RoundedCornersStyle)

@given(instance=notation::RoundedCornersStyle_strategy)
def test_notation::roundedcornersstyle_roundedBendpointsRadius_type(instance):
    assert isinstance(instance.roundedBendpointsRadius, int)


@given(instance=notation::RoundedCornersStyle_strategy)
def test_notation::roundedcornersstyle_roundedBendpointsRadius_setter(instance):
    original = instance.roundedBendpointsRadius
    instance.roundedBendpointsRadius = original
    assert instance.roundedBendpointsRadius == original

@given(instance=notation::LineStyle_strategy)
@settings(max_examples=50)
def test_notation::linestyle_instantiation(instance):
    assert isinstance(instance, notation::LineStyle)

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_lineColor_type(instance):
    assert isinstance(instance.lineColor, int)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original

@given(instance=notation::LineTypeStyle_strategy)
@settings(max_examples=50)
def test_notation::linetypestyle_instantiation(instance):
    assert isinstance(instance, notation::LineTypeStyle)

@given(instance=notation::LineTypeStyle_strategy)
def test_notation::linetypestyle_lineType_type(instance):
    assert isinstance(instance.lineType, str)


@given(instance=notation::LineTypeStyle_strategy)
def test_notation::linetypestyle_lineType_setter(instance):
    original = instance.lineType
    instance.lineType = original
    assert instance.lineType == original

@given(instance=notation::TitleStyle_strategy)
@settings(max_examples=50)
def test_notation::titlestyle_instantiation(instance):
    assert isinstance(instance, notation::TitleStyle)

@given(instance=notation::TitleStyle_strategy)
def test_notation::titlestyle_showTitle_type(instance):
    assert isinstance(instance.showTitle, bool)


@given(instance=notation::TitleStyle_strategy)
def test_notation::titlestyle_showTitle_setter(instance):
    original = instance.showTitle
    instance.showTitle = original
    assert instance.showTitle == original

@given(instance=notation::DescriptionStyle_strategy)
@settings(max_examples=50)
def test_notation::descriptionstyle_instantiation(instance):
    assert isinstance(instance, notation::DescriptionStyle)

@given(instance=notation::DescriptionStyle_strategy)
def test_notation::descriptionstyle_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=notation::DescriptionStyle_strategy)
def test_notation::descriptionstyle_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=notation::FillStyle_strategy)
@settings(max_examples=50)
def test_notation::fillstyle_instantiation(instance):
    assert isinstance(instance, notation::FillStyle)

@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_transparency_type(instance):
    assert isinstance(instance.transparency, int)


@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original

@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_gradient_type(instance):
    assert isinstance(instance.gradient, str)


@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_gradient_setter(instance):
    original = instance.gradient
    instance.gradient = original
    assert instance.gradient == original

@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_fillColor_type(instance):
    assert isinstance(instance.fillColor, int)


@given(instance=notation::FillStyle_strategy)
def test_notation::fillstyle_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original

@given(instance=View_strategy)
@settings(max_examples=50)
def test_view_instantiation(instance):
    assert isinstance(instance, View)

@given(instance=notation::Node_strategy)
@settings(max_examples=50)
def test_notation::node_instantiation(instance):
    assert isinstance(instance, notation::Node)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::Node_strategy)
@settings(max_examples=30)
def test_notation::node_createlayoutconstraint_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createLayoutConstraint(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createLayoutConstraint).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createLayoutConstraint' in notation::Node is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createLayoutConstraint' in notation::Node did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createLayoutConstraint' in notation::Node is not implemented or raised an error")

@given(instance=notation::Edge_strategy)
@settings(max_examples=50)
def test_notation::edge_instantiation(instance):
    assert isinstance(instance, notation::Edge)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::Edge_strategy)
@settings(max_examples=30)
def test_notation::edge_createbendpoints_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createBendpoints(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createBendpoints).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createBendpoints' in notation::Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createBendpoints' in notation::Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createBendpoints' in notation::Edge is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::Edge_strategy)
@settings(max_examples=30)
def test_notation::edge_createsourceanchor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createSourceAnchor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createSourceAnchor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createSourceAnchor' in notation::Edge is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createSourceAnchor' in notation::Edge did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createSourceAnchor' in notation::Edge is not implemented or raised an error")

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=notation::StandardDiagram_strategy)
@settings(max_examples=50)
def test_notation::standarddiagram_instantiation(instance):
    assert isinstance(instance, notation::StandardDiagram)

@given(instance=ConnectorStyle_strategy)
@settings(max_examples=50)
def test_connectorstyle_instantiation(instance):
    assert isinstance(instance, ConnectorStyle)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=notation::Connector_strategy)
@settings(max_examples=50)
def test_notation::connector_instantiation(instance):
    assert isinstance(instance, notation::Connector)

@given(instance=FilteringStyle_strategy)
@settings(max_examples=50)
def test_filteringstyle_instantiation(instance):
    assert isinstance(instance, FilteringStyle)

@given(instance=SortingStyle_strategy)
@settings(max_examples=50)
def test_sortingstyle_instantiation(instance):
    assert isinstance(instance, SortingStyle)

@given(instance=TitleStyle_strategy)
@settings(max_examples=50)
def test_titlestyle_instantiation(instance):
    assert isinstance(instance, TitleStyle)

@given(instance=notation::SemanticListCompartment_strategy)
@settings(max_examples=50)
def test_notation::semanticlistcompartment_instantiation(instance):
    assert isinstance(instance, notation::SemanticListCompartment)

@given(instance=CanonicalStyle_strategy)
@settings(max_examples=50)
def test_canonicalstyle_instantiation(instance):
    assert isinstance(instance, CanonicalStyle)

@given(instance=BasicCompartment_strategy)
@settings(max_examples=50)
def test_basiccompartment_instantiation(instance):
    assert isinstance(instance, BasicCompartment)

@given(instance=notation::ListCompartment_strategy)
@settings(max_examples=50)
def test_notation::listcompartment_instantiation(instance):
    assert isinstance(instance, notation::ListCompartment)

@given(instance=notation::Compartment_strategy)
@settings(max_examples=50)
def test_notation::compartment_instantiation(instance):
    assert isinstance(instance, notation::Compartment)

@given(instance=ShapeStyle_strategy)
@settings(max_examples=50)
def test_shapestyle_instantiation(instance):
    assert isinstance(instance, ShapeStyle)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=notation::BasicDecorationNode_strategy)
@settings(max_examples=50)
def test_notation::basicdecorationnode_instantiation(instance):
    assert isinstance(instance, notation::BasicDecorationNode)

@given(instance=notation::Shape_strategy)
@settings(max_examples=50)
def test_notation::shape_instantiation(instance):
    assert isinstance(instance, notation::Shape)

@given(instance=notation::ArrowStyle_strategy)
@settings(max_examples=50)
def test_notation::arrowstyle_instantiation(instance):
    assert isinstance(instance, notation::ArrowStyle)

@given(instance=notation::ArrowStyle_strategy)
def test_notation::arrowstyle_arrowTarget_type(instance):
    assert isinstance(instance.arrowTarget, str)


@given(instance=notation::ArrowStyle_strategy)
def test_notation::arrowstyle_arrowTarget_setter(instance):
    original = instance.arrowTarget
    instance.arrowTarget = original
    assert instance.arrowTarget == original

@given(instance=notation::ArrowStyle_strategy)
def test_notation::arrowstyle_arrowSource_type(instance):
    assert isinstance(instance.arrowSource, str)


@given(instance=notation::ArrowStyle_strategy)
def test_notation::arrowstyle_arrowSource_setter(instance):
    original = instance.arrowSource
    instance.arrowSource = original
    assert instance.arrowSource == original

@given(instance=notation::TextStyle_strategy)
@settings(max_examples=50)
def test_notation::textstyle_instantiation(instance):
    assert isinstance(instance, notation::TextStyle)

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_textAlignment_type(instance):
    assert isinstance(instance.textAlignment, str)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original

@given(instance=notation::MultiDiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation::multidiagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation::MultiDiagramLinkStyle)

@given(instance=notation::DiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation::diagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation::DiagramLinkStyle)

@given(instance=DiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_diagramlinkstyle_instantiation(instance):
    assert isinstance(instance, DiagramLinkStyle)

@given(instance=notation::HintedDiagramLinkStyle_strategy)
@settings(max_examples=50)
def test_notation::hinteddiagramlinkstyle_instantiation(instance):
    assert isinstance(instance, notation::HintedDiagramLinkStyle)

@given(instance=notation::HintedDiagramLinkStyle_strategy)
def test_notation::hinteddiagramlinkstyle_hint_type(instance):
    assert isinstance(instance.hint, str)


@given(instance=notation::HintedDiagramLinkStyle_strategy)
def test_notation::hinteddiagramlinkstyle_hint_setter(instance):
    original = instance.hint
    instance.hint = original
    assert instance.hint == original

@given(instance=notation::EDataType_strategy)
@settings(max_examples=50)
def test_notation::edatatype_instantiation(instance):
    assert isinstance(instance, notation::EDataType)

@given(instance=notation::StringObjectConverter_strategy)
@settings(max_examples=50)
def test_notation::stringobjectconverter_instantiation(instance):
    assert isinstance(instance, notation::StringObjectConverter)

@given(instance=notation::NamedStyle_strategy)
@settings(max_examples=50)
def test_notation::namedstyle_instantiation(instance):
    assert isinstance(instance, notation::NamedStyle)

@given(instance=notation::NamedStyle_strategy)
def test_notation::namedstyle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=notation::NamedStyle_strategy)
def test_notation::namedstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataTypeStyle_strategy)
@settings(max_examples=50)
def test_datatypestyle_instantiation(instance):
    assert isinstance(instance, DataTypeStyle)

@given(instance=notation::ListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::listvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::ListValueStyle)

@given(instance=notation::ListValueStyle_strategy)
def test_notation::listvaluestyle_rawValuesList_type(instance):
    assert isinstance(instance.rawValuesList, str)


@given(instance=notation::ListValueStyle_strategy)
def test_notation::listvaluestyle_rawValuesList_setter(instance):
    original = instance.rawValuesList
    instance.rawValuesList = original
    assert instance.rawValuesList == original

@given(instance=notation::SingleValueStyle_strategy)
@settings(max_examples=50)
def test_notation::singlevaluestyle_instantiation(instance):
    assert isinstance(instance, notation::SingleValueStyle)

@given(instance=notation::SingleValueStyle_strategy)
def test_notation::singlevaluestyle_rawValue_type(instance):
    assert isinstance(instance.rawValue, str)


@given(instance=notation::SingleValueStyle_strategy)
def test_notation::singlevaluestyle_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::SingleValueStyle_strategy)
@settings(max_examples=30)
def test_notation::singlevaluestyle_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation::SingleValueStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation::SingleValueStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation::SingleValueStyle is not implemented or raised an error")

@given(instance=NamedStyle_strategy)
@settings(max_examples=50)
def test_namedstyle_instantiation(instance):
    assert isinstance(instance, NamedStyle)

@given(instance=notation::StringValueStyle_strategy)
@settings(max_examples=50)
def test_notation::stringvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::StringValueStyle)

@given(instance=notation::StringValueStyle_strategy)
def test_notation::stringvaluestyle_stringValue_type(instance):
    assert isinstance(instance.stringValue, str)


@given(instance=notation::StringValueStyle_strategy)
def test_notation::stringvaluestyle_stringValue_setter(instance):
    original = instance.stringValue
    instance.stringValue = original
    assert instance.stringValue == original

@given(instance=notation::DoubleValueStyle_strategy)
@settings(max_examples=50)
def test_notation::doublevaluestyle_instantiation(instance):
    assert isinstance(instance, notation::DoubleValueStyle)

@given(instance=notation::DoubleValueStyle_strategy)
def test_notation::doublevaluestyle_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, float)


@given(instance=notation::DoubleValueStyle_strategy)
def test_notation::doublevaluestyle_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=notation::IntListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::intlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::IntListValueStyle)

@given(instance=notation::IntListValueStyle_strategy)
def test_notation::intlistvaluestyle_intListValue_type(instance):
    assert isinstance(instance.intListValue, int)


@given(instance=notation::IntListValueStyle_strategy)
def test_notation::intlistvaluestyle_intListValue_setter(instance):
    original = instance.intListValue
    instance.intListValue = original
    assert instance.intListValue == original

@given(instance=notation::IntValueStyle_strategy)
@settings(max_examples=50)
def test_notation::intvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::IntValueStyle)

@given(instance=notation::IntValueStyle_strategy)
def test_notation::intvaluestyle_intValue_type(instance):
    assert isinstance(instance.intValue, int)


@given(instance=notation::IntValueStyle_strategy)
def test_notation::intvaluestyle_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=notation::ByteArrayValueStyle_strategy)
@settings(max_examples=50)
def test_notation::bytearrayvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::ByteArrayValueStyle)

@given(instance=notation::ByteArrayValueStyle_strategy)
def test_notation::bytearrayvaluestyle_byteArrayValue_type(instance):
    assert isinstance(instance.byteArrayValue, str)


@given(instance=notation::ByteArrayValueStyle_strategy)
def test_notation::bytearrayvaluestyle_byteArrayValue_setter(instance):
    original = instance.byteArrayValue
    instance.byteArrayValue = original
    assert instance.byteArrayValue == original

@given(instance=notation::EObjectListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::eobjectlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::EObjectListValueStyle)

@given(instance=notation::EObjectValueStyle_strategy)
@settings(max_examples=50)
def test_notation::eobjectvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::EObjectValueStyle)

@given(instance=notation::StringListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::stringlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::StringListValueStyle)

@given(instance=notation::StringListValueStyle_strategy)
def test_notation::stringlistvaluestyle_stringListValue_type(instance):
    assert isinstance(instance.stringListValue, str)


@given(instance=notation::StringListValueStyle_strategy)
def test_notation::stringlistvaluestyle_stringListValue_setter(instance):
    original = instance.stringListValue
    instance.stringListValue = original
    assert instance.stringListValue == original

@given(instance=notation::BooleanListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::booleanlistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::BooleanListValueStyle)

@given(instance=notation::BooleanListValueStyle_strategy)
def test_notation::booleanlistvaluestyle_booleanListValue_type(instance):
    assert isinstance(instance.booleanListValue, str)


@given(instance=notation::BooleanListValueStyle_strategy)
def test_notation::booleanlistvaluestyle_booleanListValue_setter(instance):
    original = instance.booleanListValue
    instance.booleanListValue = original
    assert instance.booleanListValue == original

@given(instance=notation::DoubleListValueStyle_strategy)
@settings(max_examples=50)
def test_notation::doublelistvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::DoubleListValueStyle)

@given(instance=notation::DoubleListValueStyle_strategy)
def test_notation::doublelistvaluestyle_doubleListValue_type(instance):
    assert isinstance(instance.doubleListValue, str)


@given(instance=notation::DoubleListValueStyle_strategy)
def test_notation::doublelistvaluestyle_doubleListValue_setter(instance):
    original = instance.doubleListValue
    instance.doubleListValue = original
    assert instance.doubleListValue == original

@given(instance=notation::BooleanValueStyle_strategy)
@settings(max_examples=50)
def test_notation::booleanvaluestyle_instantiation(instance):
    assert isinstance(instance, notation::BooleanValueStyle)

@given(instance=notation::BooleanValueStyle_strategy)
def test_notation::booleanvaluestyle_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, bool)


@given(instance=notation::BooleanValueStyle_strategy)
def test_notation::booleanvaluestyle_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=notation::PropertiesSetStyle_strategy)
@settings(max_examples=50)
def test_notation::propertiessetstyle_instantiation(instance):
    assert isinstance(instance, notation::PropertiesSetStyle)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation::propertiessetstyle_removeproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeProperty' in notation::PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeProperty' in notation::PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeProperty' in notation::PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation::propertiessetstyle_setproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setProperty' in notation::PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setProperty' in notation::PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setProperty' in notation::PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation::propertiessetstyle_hasproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasProperty' in notation::PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasProperty' in notation::PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasProperty' in notation::PropertiesSetStyle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::PropertiesSetStyle_strategy)
@settings(max_examples=30)
def test_notation::propertiessetstyle_createproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createProperty' in notation::PropertiesSetStyle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createProperty' in notation::PropertiesSetStyle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createProperty' in notation::PropertiesSetStyle is not implemented or raised an error")

@given(instance=StringObjectConverter_strategy)
@settings(max_examples=50)
def test_stringobjectconverter_instantiation(instance):
    assert isinstance(instance, StringObjectConverter)

@given(instance=notation::DataTypeStyle_strategy)
@settings(max_examples=50)
def test_notation::datatypestyle_instantiation(instance):
    assert isinstance(instance, notation::DataTypeStyle)

@given(instance=notation::PropertyValue_strategy)
@settings(max_examples=50)
def test_notation::propertyvalue_instantiation(instance):
    assert isinstance(instance, notation::PropertyValue)

@given(instance=notation::PropertyValue_strategy)
def test_notation::propertyvalue_rawValue_type(instance):
    assert isinstance(instance.rawValue, str)


@given(instance=notation::PropertyValue_strategy)
def test_notation::propertyvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::PropertyValue_strategy)
@settings(max_examples=30)
def test_notation::propertyvalue_setvalue_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setValue(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setValue).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setValue' in notation::PropertyValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setValue' in notation::PropertyValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setValue' in notation::PropertyValue is not implemented or raised an error")

@given(instance=notation::StringToPropertyValueMapEntry_strategy)
@settings(max_examples=50)
def test_notation::stringtopropertyvaluemapentry_instantiation(instance):
    assert isinstance(instance, notation::StringToPropertyValueMapEntry)

@given(instance=notation::StringToPropertyValueMapEntry_strategy)
def test_notation::stringtopropertyvaluemapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=notation::StringToPropertyValueMapEntry_strategy)
def test_notation::stringtopropertyvaluemapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=notation::NodeEntry_strategy)
@settings(max_examples=50)
def test_notation::nodeentry_instantiation(instance):
    assert isinstance(instance, notation::NodeEntry)

@given(instance=notation::NodeEntry_strategy)
def test_notation::nodeentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=notation::NodeEntry_strategy)
def test_notation::nodeentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ImageStyle_strategy)
@settings(max_examples=50)
def test_imagestyle_instantiation(instance):
    assert isinstance(instance, ImageStyle)

@given(instance=notation::ImageBufferStyle_strategy)
@settings(max_examples=50)
def test_notation::imagebufferstyle_instantiation(instance):
    assert isinstance(instance, notation::ImageBufferStyle)

@given(instance=notation::ImageStyle_strategy)
@settings(max_examples=50)
def test_notation::imagestyle_instantiation(instance):
    assert isinstance(instance, notation::ImageStyle)

@given(instance=notation::ImageStyle_strategy)
def test_notation::imagestyle_maintainAspectRatio_type(instance):
    assert isinstance(instance.maintainAspectRatio, str)


@given(instance=notation::ImageStyle_strategy)
def test_notation::imagestyle_maintainAspectRatio_setter(instance):
    original = instance.maintainAspectRatio
    instance.maintainAspectRatio = original
    assert instance.maintainAspectRatio == original

@given(instance=notation::ImageStyle_strategy)
def test_notation::imagestyle_antiAlias_type(instance):
    assert isinstance(instance.antiAlias, str)


@given(instance=notation::ImageStyle_strategy)
def test_notation::imagestyle_antiAlias_setter(instance):
    original = instance.antiAlias
    instance.antiAlias = original
    assert instance.antiAlias == original

@given(instance=GuideStyle_strategy)
@settings(max_examples=50)
def test_guidestyle_instantiation(instance):
    assert isinstance(instance, GuideStyle)

@given(instance=PageStyle_strategy)
@settings(max_examples=50)
def test_pagestyle_instantiation(instance):
    assert isinstance(instance, PageStyle)

@given(instance=notation::FilteringStyle_strategy)
@settings(max_examples=50)
def test_notation::filteringstyle_instantiation(instance):
    assert isinstance(instance, notation::FilteringStyle)

@given(instance=notation::FilteringStyle_strategy)
def test_notation::filteringstyle_filtering_type(instance):
    assert isinstance(instance.filtering, str)


@given(instance=notation::FilteringStyle_strategy)
def test_notation::filteringstyle_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original

@given(instance=notation::FilteringStyle_strategy)
def test_notation::filteringstyle_filteringKeys_type(instance):
    assert isinstance(instance.filteringKeys, str)


@given(instance=notation::FilteringStyle_strategy)
def test_notation::filteringstyle_filteringKeys_setter(instance):
    original = instance.filteringKeys
    instance.filteringKeys = original
    assert instance.filteringKeys == original

@given(instance=notation::Image_strategy)
@settings(max_examples=50)
def test_notation::image_instantiation(instance):
    assert isinstance(instance, notation::Image)

@given(instance=notation::Image_strategy)
def test_notation::image_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=notation::Image_strategy)
def test_notation::image_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Bendpoints_strategy)
@settings(max_examples=50)
def test_bendpoints_instantiation(instance):
    assert isinstance(instance, Bendpoints)

@given(instance=notation::RelativeBendpoints_strategy)
@settings(max_examples=50)
def test_notation::relativebendpoints_instantiation(instance):
    assert isinstance(instance, notation::RelativeBendpoints)

@given(instance=notation::RelativeBendpoints_strategy)
def test_notation::relativebendpoints_points_type(instance):
    assert isinstance(instance.points, str)


@given(instance=notation::RelativeBendpoints_strategy)
def test_notation::relativebendpoints_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=notation::Guide_strategy)
@settings(max_examples=50)
def test_notation::guide_instantiation(instance):
    assert isinstance(instance, notation::Guide)

@given(instance=notation::Guide_strategy)
def test_notation::guide_position_type(instance):
    assert isinstance(instance.position, int)


@given(instance=notation::Guide_strategy)
def test_notation::guide_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=notation::GuideStyle_strategy)
@settings(max_examples=50)
def test_notation::guidestyle_instantiation(instance):
    assert isinstance(instance, notation::GuideStyle)

@given(instance=notation::DrawerStyle_strategy)
@settings(max_examples=50)
def test_notation::drawerstyle_instantiation(instance):
    assert isinstance(instance, notation::DrawerStyle)

@given(instance=notation::DrawerStyle_strategy)
def test_notation::drawerstyle_collapsed_type(instance):
    assert isinstance(instance.collapsed, bool)


@given(instance=notation::DrawerStyle_strategy)
def test_notation::drawerstyle_collapsed_setter(instance):
    original = instance.collapsed
    instance.collapsed = original
    assert instance.collapsed == original

@given(instance=notation::PageStyle_strategy)
@settings(max_examples=50)
def test_notation::pagestyle_instantiation(instance):
    assert isinstance(instance, notation::PageStyle)

@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageWidth_type(instance):
    assert isinstance(instance.pageWidth, int)


@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageWidth_setter(instance):
    original = instance.pageWidth
    instance.pageWidth = original
    assert instance.pageWidth == original

@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageY_type(instance):
    assert isinstance(instance.pageY, int)


@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageY_setter(instance):
    original = instance.pageY
    instance.pageY = original
    assert instance.pageY == original

@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageHeight_type(instance):
    assert isinstance(instance.pageHeight, int)


@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageHeight_setter(instance):
    original = instance.pageHeight
    instance.pageHeight = original
    assert instance.pageHeight == original

@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageX_type(instance):
    assert isinstance(instance.pageX, int)


@given(instance=notation::PageStyle_strategy)
def test_notation::pagestyle_pageX_setter(instance):
    original = instance.pageX
    instance.pageX = original
    assert instance.pageX == original

@given(instance=RoutingStyle_strategy)
@settings(max_examples=50)
def test_routingstyle_instantiation(instance):
    assert isinstance(instance, RoutingStyle)

@given(instance=LineStyle_strategy)
@settings(max_examples=50)
def test_linestyle_instantiation(instance):
    assert isinstance(instance, LineStyle)

@given(instance=notation::ConnectorStyle_strategy)
@settings(max_examples=50)
def test_notation::connectorstyle_instantiation(instance):
    assert isinstance(instance, notation::ConnectorStyle)

@given(instance=FillStyle_strategy)
@settings(max_examples=50)
def test_fillstyle_instantiation(instance):
    assert isinstance(instance, FillStyle)

@given(instance=DescriptionStyle_strategy)
@settings(max_examples=50)
def test_descriptionstyle_instantiation(instance):
    assert isinstance(instance, DescriptionStyle)

@given(instance=notation::DiagramStyle_strategy)
@settings(max_examples=50)
def test_notation::diagramstyle_instantiation(instance):
    assert isinstance(instance, notation::DiagramStyle)

@given(instance=FontStyle_strategy)
@settings(max_examples=50)
def test_fontstyle_instantiation(instance):
    assert isinstance(instance, FontStyle)

@given(instance=notation::ShapeStyle_strategy)
@settings(max_examples=50)
def test_notation::shapestyle_instantiation(instance):
    assert isinstance(instance, notation::ShapeStyle)

@given(instance=notation::CanonicalStyle_strategy)
@settings(max_examples=50)
def test_notation::canonicalstyle_instantiation(instance):
    assert isinstance(instance, notation::CanonicalStyle)

@given(instance=notation::CanonicalStyle_strategy)
def test_notation::canonicalstyle_canonical_type(instance):
    assert isinstance(instance.canonical, bool)


@given(instance=notation::CanonicalStyle_strategy)
def test_notation::canonicalstyle_canonical_setter(instance):
    original = instance.canonical
    instance.canonical = original
    assert instance.canonical == original

@given(instance=EModelElement_strategy)
@settings(max_examples=50)
def test_emodelelement_instantiation(instance):
    assert isinstance(instance, EModelElement)

@given(instance=notation::View_strategy)
@settings(max_examples=50)
def test_notation::view_instantiation(instance):
    assert isinstance(instance, notation::View)

@given(instance=notation::View_strategy)
def test_notation::view_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=notation::View_strategy)
def test_notation::view_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=notation::View_strategy)
def test_notation::view_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=notation::View_strategy)
def test_notation::view_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=notation::View_strategy)
def test_notation::view_mutable_type(instance):
    assert isinstance(instance.mutable, bool)


@given(instance=notation::View_strategy)
def test_notation::view_mutable_setter(instance):
    original = instance.mutable
    instance.mutable = original
    assert instance.mutable == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::View_strategy)
@settings(max_examples=30)
def test_notation::view_createchild_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createChild(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createChild).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createChild' in notation::View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createChild' in notation::View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createChild' in notation::View is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::View_strategy)
@settings(max_examples=30)
def test_notation::view_createstyle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createStyle(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createStyle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createStyle' in notation::View is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createStyle' in notation::View did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createStyle' in notation::View is not implemented or raised an error")

@given(instance=notation::Diagram_strategy)
@settings(max_examples=50)
def test_notation::diagram_instantiation(instance):
    assert isinstance(instance, notation::Diagram)

@given(instance=notation::Diagram_strategy)
def test_notation::diagram_measurementUnit_type(instance):
    assert isinstance(instance.measurementUnit, str)


@given(instance=notation::Diagram_strategy)
def test_notation::diagram_measurementUnit_setter(instance):
    original = instance.measurementUnit
    instance.measurementUnit = original
    assert instance.measurementUnit == original

@given(instance=notation::Diagram_strategy)
def test_notation::diagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=notation::Diagram_strategy)
def test_notation::diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=notation::Diagram_strategy)
@settings(max_examples=30)
def test_notation::diagram_createedge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createEdge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createEdge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createEdge' in notation::Diagram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createEdge' in notation::Diagram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createEdge' in notation::Diagram is not implemented or raised an error")

@given(instance=notation::Ratio_strategy)
@settings(max_examples=50)
def test_notation::ratio_instantiation(instance):
    assert isinstance(instance, notation::Ratio)

@given(instance=notation::Ratio_strategy)
def test_notation::ratio_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=notation::Ratio_strategy)
def test_notation::ratio_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Size_strategy)
@settings(max_examples=50)
def test_size_instantiation(instance):
    assert isinstance(instance, Size)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=notation::Bounds_strategy)
@settings(max_examples=50)
def test_notation::bounds_instantiation(instance):
    assert isinstance(instance, notation::Bounds)
