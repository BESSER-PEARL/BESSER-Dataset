import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::TextPart,
    Value,
    model::StringValue,
    model::BooleanValue,
    model::EnumValue,
    model::DoubleValue,
    model::IntValue,
    model::CustomColor,
    Feature,
    model::ColorFeature,
    model::FontProperties,
    model::Position,
    model::Visible,
    model::Point,
    model::Transparency,
    model::TextValue,
    model::Corner,
    model::Size,
    model::LineWidth,
    model::Layout,
    model::TextAlign,
    model::LineStyle,
    model::Anchor,
    ConnectableElement,
    model::Rhombus,
    model::Label,
    model::Rectangle,
    model::Ellipse,
    model::Triangle,
    model::Image,
    model::Polyline,
    model::Invisible,
    model::Custom,
    model::Color,
    model::Contains,
    model::EClass,
    model::ImportStatement,
    model::CustomFigure,
    model::DiagramElement,
    model::Colors,
    model::Decorator,
    model::EReference,
    FeatureContainer,
    model::Arrow,
    model::Line,
    model::ConnectableElement,
    DiagramElement,
    model::Link,
    model::Node,
    model::Value,
    model::EAttribute,
    model::FeatureContainer,
    model::FeatureConditional,
    model::Feature,
    model::Diagram,
    model::MetaModel,
    model::XDiagram,
    TextAlignValue,
    Operator,
    DefaultColor,
    AnchorDirection,
    LineType,
    BooleanLiteral,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::textpart_is_not_abstract():
    assert not inspect.isabstract(model::TextPart)


def test_model::textpart_constructor_exists():
    assert callable(model::TextPart.__init__)


def test_model::textpart_constructor_args():
    sig = inspect.signature(model::TextPart.__init__)
    params = list(sig.parameters.keys())
    assert "editable" in params, "Missing parameter 'editable'"
    assert "text" in params, "Missing parameter 'text'"

def test_model::textpart_has_editable():
    assert hasattr(model::TextPart, "editable")
    descriptor = None
    for klass in model::TextPart.__mro__:
        if "editable" in klass.__dict__:
            descriptor = klass.__dict__["editable"]
            break
    assert isinstance(descriptor, property)

def test_model::textpart_has_text():
    assert hasattr(model::TextPart, "text")
    descriptor = None
    for klass in model::TextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_model::stringvalue_is_not_abstract():
    assert not inspect.isabstract(model::StringValue)


def test_model::stringvalue_constructor_exists():
    assert callable(model::StringValue.__init__)


def test_model::stringvalue_constructor_args():
    sig = inspect.signature(model::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "null" in params, "Missing parameter 'null'"

def test_model::stringvalue_has_value():
    assert hasattr(model::StringValue, "value")
    descriptor = None
    for klass in model::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::stringvalue_has_null():
    assert hasattr(model::StringValue, "null")
    descriptor = None
    for klass in model::StringValue.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_model::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(model::BooleanValue)


def test_model::booleanvalue_constructor_exists():
    assert callable(model::BooleanValue.__init__)


def test_model::booleanvalue_constructor_args():
    sig = inspect.signature(model::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::booleanvalue_has_value():
    assert hasattr(model::BooleanValue, "value")
    descriptor = None
    for klass in model::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::enumvalue_is_not_abstract():
    assert not inspect.isabstract(model::EnumValue)


def test_model::enumvalue_constructor_exists():
    assert callable(model::EnumValue.__init__)


def test_model::enumvalue_constructor_args():
    sig = inspect.signature(model::EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::enumvalue_has_name():
    assert hasattr(model::EnumValue, "name")
    descriptor = None
    for klass in model::EnumValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::doublevalue_is_not_abstract():
    assert not inspect.isabstract(model::DoubleValue)


def test_model::doublevalue_constructor_exists():
    assert callable(model::DoubleValue.__init__)


def test_model::doublevalue_constructor_args():
    sig = inspect.signature(model::DoubleValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueDecimal" in params, "Missing parameter 'valueDecimal'"
    assert "valueInt" in params, "Missing parameter 'valueInt'"

def test_model::doublevalue_has_valueDecimal():
    assert hasattr(model::DoubleValue, "valueDecimal")
    descriptor = None
    for klass in model::DoubleValue.__mro__:
        if "valueDecimal" in klass.__dict__:
            descriptor = klass.__dict__["valueDecimal"]
            break
    assert isinstance(descriptor, property)

def test_model::doublevalue_has_valueInt():
    assert hasattr(model::DoubleValue, "valueInt")
    descriptor = None
    for klass in model::DoubleValue.__mro__:
        if "valueInt" in klass.__dict__:
            descriptor = klass.__dict__["valueInt"]
            break
    assert isinstance(descriptor, property)



def test_model::intvalue_is_not_abstract():
    assert not inspect.isabstract(model::IntValue)


def test_model::intvalue_constructor_exists():
    assert callable(model::IntValue.__init__)


def test_model::intvalue_constructor_args():
    sig = inspect.signature(model::IntValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::intvalue_has_value():
    assert hasattr(model::IntValue, "value")
    descriptor = None
    for klass in model::IntValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::customcolor_is_not_abstract():
    assert not inspect.isabstract(model::CustomColor)


def test_model::customcolor_constructor_exists():
    assert callable(model::CustomColor.__init__)


def test_model::customcolor_constructor_args():
    sig = inspect.signature(model::CustomColor.__init__)
    params = list(sig.parameters.keys())
    assert "B" in params, "Missing parameter 'B'"
    assert "R" in params, "Missing parameter 'R'"
    assert "G" in params, "Missing parameter 'G'"
    assert "name" in params, "Missing parameter 'name'"

def test_model::customcolor_has_B():
    assert hasattr(model::CustomColor, "B")
    descriptor = None
    for klass in model::CustomColor.__mro__:
        if "B" in klass.__dict__:
            descriptor = klass.__dict__["B"]
            break
    assert isinstance(descriptor, property)

def test_model::customcolor_has_R():
    assert hasattr(model::CustomColor, "R")
    descriptor = None
    for klass in model::CustomColor.__mro__:
        if "R" in klass.__dict__:
            descriptor = klass.__dict__["R"]
            break
    assert isinstance(descriptor, property)

def test_model::customcolor_has_G():
    assert hasattr(model::CustomColor, "G")
    descriptor = None
    for klass in model::CustomColor.__mro__:
        if "G" in klass.__dict__:
            descriptor = klass.__dict__["G"]
            break
    assert isinstance(descriptor, property)

def test_model::customcolor_has_name():
    assert hasattr(model::CustomColor, "name")
    descriptor = None
    for klass in model::CustomColor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_model::colorfeature_is_not_abstract():
    assert not inspect.isabstract(model::ColorFeature)


def test_model::colorfeature_constructor_exists():
    assert callable(model::ColorFeature.__init__)


def test_model::colorfeature_constructor_args():
    sig = inspect.signature(model::ColorFeature.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::colorfeature_has_type():
    assert hasattr(model::ColorFeature, "type")
    descriptor = None
    for klass in model::ColorFeature.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::fontproperties_is_not_abstract():
    assert not inspect.isabstract(model::FontProperties)


def test_model::fontproperties_constructor_exists():
    assert callable(model::FontProperties.__init__)


def test_model::fontproperties_constructor_args():
    sig = inspect.signature(model::FontProperties.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "italics" in params, "Missing parameter 'italics'"
    assert "face" in params, "Missing parameter 'face'"
    assert "bold" in params, "Missing parameter 'bold'"

def test_model::fontproperties_has_size():
    assert hasattr(model::FontProperties, "size")
    descriptor = None
    for klass in model::FontProperties.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_model::fontproperties_has_italics():
    assert hasattr(model::FontProperties, "italics")
    descriptor = None
    for klass in model::FontProperties.__mro__:
        if "italics" in klass.__dict__:
            descriptor = klass.__dict__["italics"]
            break
    assert isinstance(descriptor, property)

def test_model::fontproperties_has_face():
    assert hasattr(model::FontProperties, "face")
    descriptor = None
    for klass in model::FontProperties.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
            break
    assert isinstance(descriptor, property)

def test_model::fontproperties_has_bold():
    assert hasattr(model::FontProperties, "bold")
    descriptor = None
    for klass in model::FontProperties.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)



def test_model::position_is_not_abstract():
    assert not inspect.isabstract(model::Position)


def test_model::position_constructor_exists():
    assert callable(model::Position.__init__)


def test_model::position_constructor_args():
    sig = inspect.signature(model::Position.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"
    assert "yRelative" in params, "Missing parameter 'yRelative'"
    assert "xRelative" in params, "Missing parameter 'xRelative'"

def test_model::position_has_x():
    assert hasattr(model::Position, "x")
    descriptor = None
    for klass in model::Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_model::position_has_y():
    assert hasattr(model::Position, "y")
    descriptor = None
    for klass in model::Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_model::position_has_yRelative():
    assert hasattr(model::Position, "yRelative")
    descriptor = None
    for klass in model::Position.__mro__:
        if "yRelative" in klass.__dict__:
            descriptor = klass.__dict__["yRelative"]
            break
    assert isinstance(descriptor, property)

def test_model::position_has_xRelative():
    assert hasattr(model::Position, "xRelative")
    descriptor = None
    for klass in model::Position.__mro__:
        if "xRelative" in klass.__dict__:
            descriptor = klass.__dict__["xRelative"]
            break
    assert isinstance(descriptor, property)



def test_model::visible_is_not_abstract():
    assert not inspect.isabstract(model::Visible)


def test_model::visible_constructor_exists():
    assert callable(model::Visible.__init__)


def test_model::visible_constructor_args():
    sig = inspect.signature(model::Visible.__init__)
    params = list(sig.parameters.keys())



def test_model::point_is_not_abstract():
    assert not inspect.isabstract(model::Point)


def test_model::point_constructor_exists():
    assert callable(model::Point.__init__)


def test_model::point_constructor_args():
    sig = inspect.signature(model::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_model::point_has_x():
    assert hasattr(model::Point, "x")
    descriptor = None
    for klass in model::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_model::point_has_y():
    assert hasattr(model::Point, "y")
    descriptor = None
    for klass in model::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_model::transparency_is_not_abstract():
    assert not inspect.isabstract(model::Transparency)


def test_model::transparency_constructor_exists():
    assert callable(model::Transparency.__init__)


def test_model::transparency_constructor_args():
    sig = inspect.signature(model::Transparency.__init__)
    params = list(sig.parameters.keys())
    assert "percent" in params, "Missing parameter 'percent'"

def test_model::transparency_has_percent():
    assert hasattr(model::Transparency, "percent")
    descriptor = None
    for klass in model::Transparency.__mro__:
        if "percent" in klass.__dict__:
            descriptor = klass.__dict__["percent"]
            break
    assert isinstance(descriptor, property)



def test_model::textvalue_is_not_abstract():
    assert not inspect.isabstract(model::TextValue)


def test_model::textvalue_constructor_exists():
    assert callable(model::TextValue.__init__)


def test_model::textvalue_constructor_args():
    sig = inspect.signature(model::TextValue.__init__)
    params = list(sig.parameters.keys())



def test_model::corner_is_not_abstract():
    assert not inspect.isabstract(model::Corner)


def test_model::corner_constructor_exists():
    assert callable(model::Corner.__init__)


def test_model::corner_constructor_args():
    sig = inspect.signature(model::Corner.__init__)
    params = list(sig.parameters.keys())
    assert "angle" in params, "Missing parameter 'angle'"

def test_model::corner_has_angle():
    assert hasattr(model::Corner, "angle")
    descriptor = None
    for klass in model::Corner.__mro__:
        if "angle" in klass.__dict__:
            descriptor = klass.__dict__["angle"]
            break
    assert isinstance(descriptor, property)



def test_model::size_is_not_abstract():
    assert not inspect.isabstract(model::Size)


def test_model::size_constructor_exists():
    assert callable(model::Size.__init__)


def test_model::size_constructor_args():
    sig = inspect.signature(model::Size.__init__)
    params = list(sig.parameters.keys())
    assert "widthRelative" in params, "Missing parameter 'widthRelative'"
    assert "width" in params, "Missing parameter 'width'"
    assert "heightRelative" in params, "Missing parameter 'heightRelative'"
    assert "resizable" in params, "Missing parameter 'resizable'"
    assert "height" in params, "Missing parameter 'height'"

def test_model::size_has_widthRelative():
    assert hasattr(model::Size, "widthRelative")
    descriptor = None
    for klass in model::Size.__mro__:
        if "widthRelative" in klass.__dict__:
            descriptor = klass.__dict__["widthRelative"]
            break
    assert isinstance(descriptor, property)

def test_model::size_has_width():
    assert hasattr(model::Size, "width")
    descriptor = None
    for klass in model::Size.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model::size_has_heightRelative():
    assert hasattr(model::Size, "heightRelative")
    descriptor = None
    for klass in model::Size.__mro__:
        if "heightRelative" in klass.__dict__:
            descriptor = klass.__dict__["heightRelative"]
            break
    assert isinstance(descriptor, property)

def test_model::size_has_resizable():
    assert hasattr(model::Size, "resizable")
    descriptor = None
    for klass in model::Size.__mro__:
        if "resizable" in klass.__dict__:
            descriptor = klass.__dict__["resizable"]
            break
    assert isinstance(descriptor, property)

def test_model::size_has_height():
    assert hasattr(model::Size, "height")
    descriptor = None
    for klass in model::Size.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_model::linewidth_is_not_abstract():
    assert not inspect.isabstract(model::LineWidth)


def test_model::linewidth_constructor_exists():
    assert callable(model::LineWidth.__init__)


def test_model::linewidth_constructor_args():
    sig = inspect.signature(model::LineWidth.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"

def test_model::linewidth_has_width():
    assert hasattr(model::LineWidth, "width")
    descriptor = None
    for klass in model::LineWidth.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_model::layout_is_not_abstract():
    assert not inspect.isabstract(model::Layout)


def test_model::layout_constructor_exists():
    assert callable(model::Layout.__init__)


def test_model::layout_constructor_args():
    sig = inspect.signature(model::Layout.__init__)
    params = list(sig.parameters.keys())
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "vertical" in params, "Missing parameter 'vertical'"
    assert "margin" in params, "Missing parameter 'margin'"

def test_model::layout_has_horizontal():
    assert hasattr(model::Layout, "horizontal")
    descriptor = None
    for klass in model::Layout.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_model::layout_has_vertical():
    assert hasattr(model::Layout, "vertical")
    descriptor = None
    for klass in model::Layout.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)

def test_model::layout_has_margin():
    assert hasattr(model::Layout, "margin")
    descriptor = None
    for klass in model::Layout.__mro__:
        if "margin" in klass.__dict__:
            descriptor = klass.__dict__["margin"]
            break
    assert isinstance(descriptor, property)



def test_model::textalign_is_not_abstract():
    assert not inspect.isabstract(model::TextAlign)


def test_model::textalign_constructor_exists():
    assert callable(model::TextAlign.__init__)


def test_model::textalign_constructor_args():
    sig = inspect.signature(model::TextAlign.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_model::textalign_has_value():
    assert hasattr(model::TextAlign, "value")
    descriptor = None
    for klass in model::TextAlign.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model::linestyle_is_not_abstract():
    assert not inspect.isabstract(model::LineStyle)


def test_model::linestyle_constructor_exists():
    assert callable(model::LineStyle.__init__)


def test_model::linestyle_constructor_args():
    sig = inspect.signature(model::LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "manhattan" in params, "Missing parameter 'manhattan'"

def test_model::linestyle_has_style():
    assert hasattr(model::LineStyle, "style")
    descriptor = None
    for klass in model::LineStyle.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_model::linestyle_has_manhattan():
    assert hasattr(model::LineStyle, "manhattan")
    descriptor = None
    for klass in model::LineStyle.__mro__:
        if "manhattan" in klass.__dict__:
            descriptor = klass.__dict__["manhattan"]
            break
    assert isinstance(descriptor, property)



def test_model::anchor_is_not_abstract():
    assert not inspect.isabstract(model::Anchor)


def test_model::anchor_constructor_exists():
    assert callable(model::Anchor.__init__)


def test_model::anchor_constructor_args():
    sig = inspect.signature(model::Anchor.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "max" in params, "Missing parameter 'max'"

def test_model::anchor_has_direction():
    assert hasattr(model::Anchor, "direction")
    descriptor = None
    for klass in model::Anchor.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model::anchor_has_max():
    assert hasattr(model::Anchor, "max")
    descriptor = None
    for klass in model::Anchor.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_model::rhombus_is_not_abstract():
    assert not inspect.isabstract(model::Rhombus)


def test_model::rhombus_constructor_exists():
    assert callable(model::Rhombus.__init__)


def test_model::rhombus_constructor_args():
    sig = inspect.signature(model::Rhombus.__init__)
    params = list(sig.parameters.keys())



def test_model::label_is_not_abstract():
    assert not inspect.isabstract(model::Label)


def test_model::label_constructor_exists():
    assert callable(model::Label.__init__)


def test_model::label_constructor_args():
    sig = inspect.signature(model::Label.__init__)
    params = list(sig.parameters.keys())



def test_model::rectangle_is_not_abstract():
    assert not inspect.isabstract(model::Rectangle)


def test_model::rectangle_constructor_exists():
    assert callable(model::Rectangle.__init__)


def test_model::rectangle_constructor_args():
    sig = inspect.signature(model::Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "square" in params, "Missing parameter 'square'"
    assert "rectangle" in params, "Missing parameter 'rectangle'"

def test_model::rectangle_has_square():
    assert hasattr(model::Rectangle, "square")
    descriptor = None
    for klass in model::Rectangle.__mro__:
        if "square" in klass.__dict__:
            descriptor = klass.__dict__["square"]
            break
    assert isinstance(descriptor, property)

def test_model::rectangle_has_rectangle():
    assert hasattr(model::Rectangle, "rectangle")
    descriptor = None
    for klass in model::Rectangle.__mro__:
        if "rectangle" in klass.__dict__:
            descriptor = klass.__dict__["rectangle"]
            break
    assert isinstance(descriptor, property)



def test_model::ellipse_is_not_abstract():
    assert not inspect.isabstract(model::Ellipse)


def test_model::ellipse_constructor_exists():
    assert callable(model::Ellipse.__init__)


def test_model::ellipse_constructor_args():
    sig = inspect.signature(model::Ellipse.__init__)
    params = list(sig.parameters.keys())
    assert "ellipse" in params, "Missing parameter 'ellipse'"
    assert "circle" in params, "Missing parameter 'circle'"

def test_model::ellipse_has_ellipse():
    assert hasattr(model::Ellipse, "ellipse")
    descriptor = None
    for klass in model::Ellipse.__mro__:
        if "ellipse" in klass.__dict__:
            descriptor = klass.__dict__["ellipse"]
            break
    assert isinstance(descriptor, property)

def test_model::ellipse_has_circle():
    assert hasattr(model::Ellipse, "circle")
    descriptor = None
    for klass in model::Ellipse.__mro__:
        if "circle" in klass.__dict__:
            descriptor = klass.__dict__["circle"]
            break
    assert isinstance(descriptor, property)



def test_model::triangle_is_not_abstract():
    assert not inspect.isabstract(model::Triangle)


def test_model::triangle_constructor_exists():
    assert callable(model::Triangle.__init__)


def test_model::triangle_constructor_args():
    sig = inspect.signature(model::Triangle.__init__)
    params = list(sig.parameters.keys())



def test_model::image_is_not_abstract():
    assert not inspect.isabstract(model::Image)


def test_model::image_constructor_exists():
    assert callable(model::Image.__init__)


def test_model::image_constructor_args():
    sig = inspect.signature(model::Image.__init__)
    params = list(sig.parameters.keys())
    assert "imageId" in params, "Missing parameter 'imageId'"

def test_model::image_has_imageId():
    assert hasattr(model::Image, "imageId")
    descriptor = None
    for klass in model::Image.__mro__:
        if "imageId" in klass.__dict__:
            descriptor = klass.__dict__["imageId"]
            break
    assert isinstance(descriptor, property)



def test_model::polyline_is_not_abstract():
    assert not inspect.isabstract(model::Polyline)


def test_model::polyline_constructor_exists():
    assert callable(model::Polyline.__init__)


def test_model::polyline_constructor_args():
    sig = inspect.signature(model::Polyline.__init__)
    params = list(sig.parameters.keys())
    assert "polyline" in params, "Missing parameter 'polyline'"
    assert "polygon" in params, "Missing parameter 'polygon'"

def test_model::polyline_has_polyline():
    assert hasattr(model::Polyline, "polyline")
    descriptor = None
    for klass in model::Polyline.__mro__:
        if "polyline" in klass.__dict__:
            descriptor = klass.__dict__["polyline"]
            break
    assert isinstance(descriptor, property)

def test_model::polyline_has_polygon():
    assert hasattr(model::Polyline, "polygon")
    descriptor = None
    for klass in model::Polyline.__mro__:
        if "polygon" in klass.__dict__:
            descriptor = klass.__dict__["polygon"]
            break
    assert isinstance(descriptor, property)



def test_model::invisible_is_not_abstract():
    assert not inspect.isabstract(model::Invisible)


def test_model::invisible_constructor_exists():
    assert callable(model::Invisible.__init__)


def test_model::invisible_constructor_args():
    sig = inspect.signature(model::Invisible.__init__)
    params = list(sig.parameters.keys())



def test_model::custom_is_not_abstract():
    assert not inspect.isabstract(model::Custom)


def test_model::custom_constructor_exists():
    assert callable(model::Custom.__init__)


def test_model::custom_constructor_args():
    sig = inspect.signature(model::Custom.__init__)
    params = list(sig.parameters.keys())



def test_model::color_is_not_abstract():
    assert not inspect.isabstract(model::Color)


def test_model::color_constructor_exists():
    assert callable(model::Color.__init__)


def test_model::color_constructor_args():
    sig = inspect.signature(model::Color.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_model::color_has_default():
    assert hasattr(model::Color, "default")
    descriptor = None
    for klass in model::Color.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_model::contains_is_not_abstract():
    assert not inspect.isabstract(model::Contains)


def test_model::contains_constructor_exists():
    assert callable(model::Contains.__init__)


def test_model::contains_constructor_args():
    sig = inspect.signature(model::Contains.__init__)
    params = list(sig.parameters.keys())



def test_model::eclass_is_not_abstract():
    assert not inspect.isabstract(model::EClass)


def test_model::eclass_constructor_exists():
    assert callable(model::EClass.__init__)


def test_model::eclass_constructor_args():
    sig = inspect.signature(model::EClass.__init__)
    params = list(sig.parameters.keys())



def test_model::importstatement_is_not_abstract():
    assert not inspect.isabstract(model::ImportStatement)


def test_model::importstatement_constructor_exists():
    assert callable(model::ImportStatement.__init__)


def test_model::importstatement_constructor_args():
    sig = inspect.signature(model::ImportStatement.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_model::importstatement_has_importedNamespace():
    assert hasattr(model::ImportStatement, "importedNamespace")
    descriptor = None
    for klass in model::ImportStatement.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_model::customfigure_is_not_abstract():
    assert not inspect.isabstract(model::CustomFigure)


def test_model::customfigure_constructor_exists():
    assert callable(model::CustomFigure.__init__)


def test_model::customfigure_constructor_args():
    sig = inspect.signature(model::CustomFigure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::customfigure_has_name():
    assert hasattr(model::CustomFigure, "name")
    descriptor = None
    for klass in model::CustomFigure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::diagramelement_is_not_abstract():
    assert not inspect.isabstract(model::DiagramElement)


def test_model::diagramelement_constructor_exists():
    assert callable(model::DiagramElement.__init__)


def test_model::diagramelement_constructor_args():
    sig = inspect.signature(model::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_model::colors_is_not_abstract():
    assert not inspect.isabstract(model::Colors)


def test_model::colors_constructor_exists():
    assert callable(model::Colors.__init__)


def test_model::colors_constructor_args():
    sig = inspect.signature(model::Colors.__init__)
    params = list(sig.parameters.keys())



def test_model::decorator_is_not_abstract():
    assert not inspect.isabstract(model::Decorator)


def test_model::decorator_constructor_exists():
    assert callable(model::Decorator.__init__)


def test_model::decorator_constructor_args():
    sig = inspect.signature(model::Decorator.__init__)
    params = list(sig.parameters.keys())



def test_model::ereference_is_not_abstract():
    assert not inspect.isabstract(model::EReference)


def test_model::ereference_constructor_exists():
    assert callable(model::EReference.__init__)


def test_model::ereference_constructor_args():
    sig = inspect.signature(model::EReference.__init__)
    params = list(sig.parameters.keys())



def test_featurecontainer_is_not_abstract():
    assert not inspect.isabstract(FeatureContainer)


def test_featurecontainer_constructor_exists():
    assert callable(FeatureContainer.__init__)


def test_featurecontainer_constructor_args():
    sig = inspect.signature(FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::arrow_is_not_abstract():
    assert not inspect.isabstract(model::Arrow)


def test_model::arrow_constructor_exists():
    assert callable(model::Arrow.__init__)


def test_model::arrow_constructor_args():
    sig = inspect.signature(model::Arrow.__init__)
    params = list(sig.parameters.keys())



def test_model::line_is_not_abstract():
    assert not inspect.isabstract(model::Line)


def test_model::line_constructor_exists():
    assert callable(model::Line.__init__)


def test_model::line_constructor_args():
    sig = inspect.signature(model::Line.__init__)
    params = list(sig.parameters.keys())
    assert "horizontal" in params, "Missing parameter 'horizontal'"
    assert "vertical" in params, "Missing parameter 'vertical'"

def test_model::line_has_horizontal():
    assert hasattr(model::Line, "horizontal")
    descriptor = None
    for klass in model::Line.__mro__:
        if "horizontal" in klass.__dict__:
            descriptor = klass.__dict__["horizontal"]
            break
    assert isinstance(descriptor, property)

def test_model::line_has_vertical():
    assert hasattr(model::Line, "vertical")
    descriptor = None
    for klass in model::Line.__mro__:
        if "vertical" in klass.__dict__:
            descriptor = klass.__dict__["vertical"]
            break
    assert isinstance(descriptor, property)



def test_model::connectableelement_is_not_abstract():
    assert not inspect.isabstract(model::ConnectableElement)


def test_model::connectableelement_constructor_exists():
    assert callable(model::ConnectableElement.__init__)


def test_model::connectableelement_constructor_args():
    sig = inspect.signature(model::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_model::link_is_not_abstract():
    assert not inspect.isabstract(model::Link)


def test_model::link_constructor_exists():
    assert callable(model::Link.__init__)


def test_model::link_constructor_args():
    sig = inspect.signature(model::Link.__init__)
    params = list(sig.parameters.keys())
    assert "complex" in params, "Missing parameter 'complex'"
    assert "reference" in params, "Missing parameter 'reference'"

def test_model::link_has_complex():
    assert hasattr(model::Link, "complex")
    descriptor = None
    for klass in model::Link.__mro__:
        if "complex" in klass.__dict__:
            descriptor = klass.__dict__["complex"]
            break
    assert isinstance(descriptor, property)

def test_model::link_has_reference():
    assert hasattr(model::Link, "reference")
    descriptor = None
    for klass in model::Link.__mro__:
        if "reference" in klass.__dict__:
            descriptor = klass.__dict__["reference"]
            break
    assert isinstance(descriptor, property)



def test_model::node_is_not_abstract():
    assert not inspect.isabstract(model::Node)


def test_model::node_constructor_exists():
    assert callable(model::Node.__init__)


def test_model::node_constructor_args():
    sig = inspect.signature(model::Node.__init__)
    params = list(sig.parameters.keys())



def test_model::value_is_not_abstract():
    assert not inspect.isabstract(model::Value)


def test_model::value_constructor_exists():
    assert callable(model::Value.__init__)


def test_model::value_constructor_args():
    sig = inspect.signature(model::Value.__init__)
    params = list(sig.parameters.keys())



def test_model::eattribute_is_not_abstract():
    assert not inspect.isabstract(model::EAttribute)


def test_model::eattribute_constructor_exists():
    assert callable(model::EAttribute.__init__)


def test_model::eattribute_constructor_args():
    sig = inspect.signature(model::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_model::featurecontainer_is_not_abstract():
    assert not inspect.isabstract(model::FeatureContainer)


def test_model::featurecontainer_constructor_exists():
    assert callable(model::FeatureContainer.__init__)


def test_model::featurecontainer_constructor_args():
    sig = inspect.signature(model::FeatureContainer.__init__)
    params = list(sig.parameters.keys())



def test_model::featureconditional_is_not_abstract():
    assert not inspect.isabstract(model::FeatureConditional)


def test_model::featureconditional_constructor_exists():
    assert callable(model::FeatureConditional.__init__)


def test_model::featureconditional_constructor_args():
    sig = inspect.signature(model::FeatureConditional.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_model::featureconditional_has_operator():
    assert hasattr(model::FeatureConditional, "operator")
    descriptor = None
    for klass in model::FeatureConditional.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_model::feature_is_not_abstract():
    assert not inspect.isabstract(model::Feature)


def test_model::feature_constructor_exists():
    assert callable(model::Feature.__init__)


def test_model::feature_constructor_args():
    sig = inspect.signature(model::Feature.__init__)
    params = list(sig.parameters.keys())



def test_model::diagram_is_not_abstract():
    assert not inspect.isabstract(model::Diagram)


def test_model::diagram_constructor_exists():
    assert callable(model::Diagram.__init__)


def test_model::diagram_constructor_args():
    sig = inspect.signature(model::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_model::metamodel_is_not_abstract():
    assert not inspect.isabstract(model::MetaModel)


def test_model::metamodel_constructor_exists():
    assert callable(model::MetaModel.__init__)


def test_model::metamodel_constructor_args():
    sig = inspect.signature(model::MetaModel.__init__)
    params = list(sig.parameters.keys())
    assert "plugin" in params, "Missing parameter 'plugin'"
    assert "ecorePath" in params, "Missing parameter 'ecorePath'"

def test_model::metamodel_has_plugin():
    assert hasattr(model::MetaModel, "plugin")
    descriptor = None
    for klass in model::MetaModel.__mro__:
        if "plugin" in klass.__dict__:
            descriptor = klass.__dict__["plugin"]
            break
    assert isinstance(descriptor, property)

def test_model::metamodel_has_ecorePath():
    assert hasattr(model::MetaModel, "ecorePath")
    descriptor = None
    for klass in model::MetaModel.__mro__:
        if "ecorePath" in klass.__dict__:
            descriptor = klass.__dict__["ecorePath"]
            break
    assert isinstance(descriptor, property)



def test_model::xdiagram_is_not_abstract():
    assert not inspect.isabstract(model::XDiagram)


def test_model::xdiagram_constructor_exists():
    assert callable(model::XDiagram.__init__)


def test_model::xdiagram_constructor_args():
    sig = inspect.signature(model::XDiagram.__init__)
    params = list(sig.parameters.keys())

def test_textalignvalue_exists():
    # Check that the Enumeration exists
    assert TextAlignValue is not None

def test_textalignvalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextAlignValue]
    expected_literals = [
        "CENTER",
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextAlignValue"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "EQUAL",
        "DIFFERENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"

def test_defaultcolor_exists():
    # Check that the Enumeration exists
    assert DefaultColor is not None

def test_defaultcolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefaultColor]
    expected_literals = [
        "GRAY",
        "LIME",
        "SILVER",
        "TEAL",
        "WHITE",
        "GREEN",
        "BLUE",
        "FUCHSIA",
        "PURPLE",
        "BLACK",
        "AQUA",
        "NAVY",
        "YELLOW",
        "MAROON",
        "OLIVE",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefaultColor"

def test_anchordirection_exists():
    # Check that the Enumeration exists
    assert AnchorDirection is not None

def test_anchordirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AnchorDirection]
    expected_literals = [
        "INCOMING",
        "OUTGOING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AnchorDirection"

def test_linetype_exists():
    # Check that the Enumeration exists
    assert LineType is not None

def test_linetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineType]
    expected_literals = [
        "DOT",
        "SOLID",
        "DASH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineType"

def test_booleanliteral_exists():
    # Check that the Enumeration exists
    assert BooleanLiteral is not None

def test_booleanliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanLiteral]
    expected_literals = [
        "TRUE",
        "FALSE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanLiteral"


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
model::TextPart_strategy = st.builds(
    model::TextPart,
    editable=
        st.booleans(),
    text=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
model::StringValue_strategy = st.builds(
    model::StringValue,
    value=
        safe_text,
    null=
        st.booleans()
)
model::BooleanValue_strategy = st.builds(
    model::BooleanValue,
    value=
        safe_text
)
model::EnumValue_strategy = st.builds(
    model::EnumValue,
    name=
        safe_text
)
model::DoubleValue_strategy = st.builds(
    model::DoubleValue,
    valueDecimal=
        st.integers(),
    valueInt=
        st.integers()
)
model::IntValue_strategy = st.builds(
    model::IntValue,
    value=
        st.integers()
)
model::CustomColor_strategy = st.builds(
    model::CustomColor,
    B=
        st.integers(),
    R=
        st.integers(),
    G=
        st.integers(),
    name=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
model::ColorFeature_strategy = st.builds(
    model::ColorFeature,
    type=
        safe_text
)
model::FontProperties_strategy = st.builds(
    model::FontProperties,
    size=
        st.integers(),
    italics=
        st.booleans(),
    face=
        safe_text,
    bold=
        st.booleans()
)
model::Position_strategy = st.builds(
    model::Position,
    x=
        st.integers(),
    y=
        st.integers(),
    yRelative=
        st.booleans(),
    xRelative=
        st.booleans()
)
model::Visible_strategy = st.builds(
    model::Visible,
)
model::Point_strategy = st.builds(
    model::Point,
    x=
        st.integers(),
    y=
        st.integers()
)
model::Transparency_strategy = st.builds(
    model::Transparency,
    percent=
        st.integers()
)
model::TextValue_strategy = st.builds(
    model::TextValue,
)
model::Corner_strategy = st.builds(
    model::Corner,
    angle=
        st.integers()
)
model::Size_strategy = st.builds(
    model::Size,
    widthRelative=
        st.booleans(),
    width=
        st.integers(),
    heightRelative=
        st.booleans(),
    resizable=
        st.booleans(),
    height=
        st.integers()
)
model::LineWidth_strategy = st.builds(
    model::LineWidth,
    width=
        st.integers()
)
model::Layout_strategy = st.builds(
    model::Layout,
    horizontal=
        st.booleans(),
    vertical=
        st.booleans(),
    margin=
        st.integers()
)
model::TextAlign_strategy = st.builds(
    model::TextAlign,
    value=
        safe_text
)
model::LineStyle_strategy = st.builds(
    model::LineStyle,
    style=
        safe_text,
    manhattan=
        st.booleans()
)
model::Anchor_strategy = st.builds(
    model::Anchor,
    direction=
        safe_text,
    max=
        st.integers()
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
model::Rhombus_strategy = st.builds(
    model::Rhombus,
)
model::Label_strategy = st.builds(
    model::Label,
)
model::Rectangle_strategy = st.builds(
    model::Rectangle,
    square=
        st.booleans(),
    rectangle=
        st.booleans()
)
model::Ellipse_strategy = st.builds(
    model::Ellipse,
    ellipse=
        st.booleans(),
    circle=
        st.booleans()
)
model::Triangle_strategy = st.builds(
    model::Triangle,
)
model::Image_strategy = st.builds(
    model::Image,
    imageId=
        safe_text
)
model::Polyline_strategy = st.builds(
    model::Polyline,
    polyline=
        st.booleans(),
    polygon=
        st.booleans()
)
model::Invisible_strategy = st.builds(
    model::Invisible,
)
model::Custom_strategy = st.builds(
    model::Custom,
)
model::Color_strategy = st.builds(
    model::Color,
    default=
        safe_text
)
model::Contains_strategy = st.builds(
    model::Contains,
)
model::EClass_strategy = st.builds(
    model::EClass,
)
model::ImportStatement_strategy = st.builds(
    model::ImportStatement,
    importedNamespace=
        safe_text
)
model::CustomFigure_strategy = st.builds(
    model::CustomFigure,
    name=
        safe_text
)
model::DiagramElement_strategy = st.builds(
    model::DiagramElement,
)
model::Colors_strategy = st.builds(
    model::Colors,
)
model::Decorator_strategy = st.builds(
    model::Decorator,
)
model::EReference_strategy = st.builds(
    model::EReference,
)
FeatureContainer_strategy = st.builds(
    FeatureContainer,
)
model::Arrow_strategy = st.builds(
    model::Arrow,
)
model::Line_strategy = st.builds(
    model::Line,
    horizontal=
        st.booleans(),
    vertical=
        st.booleans()
)
model::ConnectableElement_strategy = st.builds(
    model::ConnectableElement,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
model::Link_strategy = st.builds(
    model::Link,
    complex=
        st.booleans(),
    reference=
        st.booleans()
)
model::Node_strategy = st.builds(
    model::Node,
)
model::Value_strategy = st.builds(
    model::Value,
)
model::EAttribute_strategy = st.builds(
    model::EAttribute,
)
model::FeatureContainer_strategy = st.builds(
    model::FeatureContainer,
)
model::FeatureConditional_strategy = st.builds(
    model::FeatureConditional,
    operator=
        safe_text
)
model::Feature_strategy = st.builds(
    model::Feature,
)
model::Diagram_strategy = st.builds(
    model::Diagram,
)
model::MetaModel_strategy = st.builds(
    model::MetaModel,
    plugin=
        safe_text,
    ecorePath=
        safe_text
)
model::XDiagram_strategy = st.builds(
    model::XDiagram,
)

@given(instance=model::TextPart_strategy)
@settings(max_examples=50)
def test_model::textpart_instantiation(instance):
    assert isinstance(instance, model::TextPart)

@given(instance=model::TextPart_strategy)
def test_model::textpart_editable_type(instance):
    assert isinstance(instance.editable, bool)


@given(instance=model::TextPart_strategy)
def test_model::textpart_editable_setter(instance):
    original = instance.editable
    instance.editable = original
    assert instance.editable == original

@given(instance=model::TextPart_strategy)
def test_model::textpart_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=model::TextPart_strategy)
def test_model::textpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=model::StringValue_strategy)
@settings(max_examples=50)
def test_model::stringvalue_instantiation(instance):
    assert isinstance(instance, model::StringValue)

@given(instance=model::StringValue_strategy)
def test_model::stringvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::StringValue_strategy)
def test_model::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::StringValue_strategy)
def test_model::stringvalue_null_type(instance):
    assert isinstance(instance.null, bool)


@given(instance=model::StringValue_strategy)
def test_model::stringvalue_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=model::BooleanValue_strategy)
@settings(max_examples=50)
def test_model::booleanvalue_instantiation(instance):
    assert isinstance(instance, model::BooleanValue)

@given(instance=model::BooleanValue_strategy)
def test_model::booleanvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::BooleanValue_strategy)
def test_model::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::EnumValue_strategy)
@settings(max_examples=50)
def test_model::enumvalue_instantiation(instance):
    assert isinstance(instance, model::EnumValue)

@given(instance=model::EnumValue_strategy)
def test_model::enumvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::EnumValue_strategy)
def test_model::enumvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::DoubleValue_strategy)
@settings(max_examples=50)
def test_model::doublevalue_instantiation(instance):
    assert isinstance(instance, model::DoubleValue)

@given(instance=model::DoubleValue_strategy)
def test_model::doublevalue_valueDecimal_type(instance):
    assert isinstance(instance.valueDecimal, int)


@given(instance=model::DoubleValue_strategy)
def test_model::doublevalue_valueDecimal_setter(instance):
    original = instance.valueDecimal
    instance.valueDecimal = original
    assert instance.valueDecimal == original

@given(instance=model::DoubleValue_strategy)
def test_model::doublevalue_valueInt_type(instance):
    assert isinstance(instance.valueInt, int)


@given(instance=model::DoubleValue_strategy)
def test_model::doublevalue_valueInt_setter(instance):
    original = instance.valueInt
    instance.valueInt = original
    assert instance.valueInt == original

@given(instance=model::IntValue_strategy)
@settings(max_examples=50)
def test_model::intvalue_instantiation(instance):
    assert isinstance(instance, model::IntValue)

@given(instance=model::IntValue_strategy)
def test_model::intvalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=model::IntValue_strategy)
def test_model::intvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::CustomColor_strategy)
@settings(max_examples=50)
def test_model::customcolor_instantiation(instance):
    assert isinstance(instance, model::CustomColor)

@given(instance=model::CustomColor_strategy)
def test_model::customcolor_B_type(instance):
    assert isinstance(instance.B, int)


@given(instance=model::CustomColor_strategy)
def test_model::customcolor_B_setter(instance):
    original = instance.B
    instance.B = original
    assert instance.B == original

@given(instance=model::CustomColor_strategy)
def test_model::customcolor_R_type(instance):
    assert isinstance(instance.R, int)


@given(instance=model::CustomColor_strategy)
def test_model::customcolor_R_setter(instance):
    original = instance.R
    instance.R = original
    assert instance.R == original

@given(instance=model::CustomColor_strategy)
def test_model::customcolor_G_type(instance):
    assert isinstance(instance.G, int)


@given(instance=model::CustomColor_strategy)
def test_model::customcolor_G_setter(instance):
    original = instance.G
    instance.G = original
    assert instance.G == original

@given(instance=model::CustomColor_strategy)
def test_model::customcolor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::CustomColor_strategy)
def test_model::customcolor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=model::ColorFeature_strategy)
@settings(max_examples=50)
def test_model::colorfeature_instantiation(instance):
    assert isinstance(instance, model::ColorFeature)

@given(instance=model::ColorFeature_strategy)
def test_model::colorfeature_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::ColorFeature_strategy)
def test_model::colorfeature_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::FontProperties_strategy)
@settings(max_examples=50)
def test_model::fontproperties_instantiation(instance):
    assert isinstance(instance, model::FontProperties)

@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_italics_type(instance):
    assert isinstance(instance.italics, bool)


@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_italics_setter(instance):
    original = instance.italics
    instance.italics = original
    assert instance.italics == original

@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_face_type(instance):
    assert isinstance(instance.face, str)


@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original

@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_bold_type(instance):
    assert isinstance(instance.bold, bool)


@given(instance=model::FontProperties_strategy)
def test_model::fontproperties_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original

@given(instance=model::Position_strategy)
@settings(max_examples=50)
def test_model::position_instantiation(instance):
    assert isinstance(instance, model::Position)

@given(instance=model::Position_strategy)
def test_model::position_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=model::Position_strategy)
def test_model::position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model::Position_strategy)
def test_model::position_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=model::Position_strategy)
def test_model::position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=model::Position_strategy)
def test_model::position_yRelative_type(instance):
    assert isinstance(instance.yRelative, bool)


@given(instance=model::Position_strategy)
def test_model::position_yRelative_setter(instance):
    original = instance.yRelative
    instance.yRelative = original
    assert instance.yRelative == original

@given(instance=model::Position_strategy)
def test_model::position_xRelative_type(instance):
    assert isinstance(instance.xRelative, bool)


@given(instance=model::Position_strategy)
def test_model::position_xRelative_setter(instance):
    original = instance.xRelative
    instance.xRelative = original
    assert instance.xRelative == original

@given(instance=model::Visible_strategy)
@settings(max_examples=50)
def test_model::visible_instantiation(instance):
    assert isinstance(instance, model::Visible)

@given(instance=model::Point_strategy)
@settings(max_examples=50)
def test_model::point_instantiation(instance):
    assert isinstance(instance, model::Point)

@given(instance=model::Point_strategy)
def test_model::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=model::Point_strategy)
def test_model::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=model::Point_strategy)
def test_model::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=model::Point_strategy)
def test_model::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=model::Transparency_strategy)
@settings(max_examples=50)
def test_model::transparency_instantiation(instance):
    assert isinstance(instance, model::Transparency)

@given(instance=model::Transparency_strategy)
def test_model::transparency_percent_type(instance):
    assert isinstance(instance.percent, int)


@given(instance=model::Transparency_strategy)
def test_model::transparency_percent_setter(instance):
    original = instance.percent
    instance.percent = original
    assert instance.percent == original

@given(instance=model::TextValue_strategy)
@settings(max_examples=50)
def test_model::textvalue_instantiation(instance):
    assert isinstance(instance, model::TextValue)

@given(instance=model::Corner_strategy)
@settings(max_examples=50)
def test_model::corner_instantiation(instance):
    assert isinstance(instance, model::Corner)

@given(instance=model::Corner_strategy)
def test_model::corner_angle_type(instance):
    assert isinstance(instance.angle, int)


@given(instance=model::Corner_strategy)
def test_model::corner_angle_setter(instance):
    original = instance.angle
    instance.angle = original
    assert instance.angle == original

@given(instance=model::Size_strategy)
@settings(max_examples=50)
def test_model::size_instantiation(instance):
    assert isinstance(instance, model::Size)

@given(instance=model::Size_strategy)
def test_model::size_widthRelative_type(instance):
    assert isinstance(instance.widthRelative, bool)


@given(instance=model::Size_strategy)
def test_model::size_widthRelative_setter(instance):
    original = instance.widthRelative
    instance.widthRelative = original
    assert instance.widthRelative == original

@given(instance=model::Size_strategy)
def test_model::size_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=model::Size_strategy)
def test_model::size_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model::Size_strategy)
def test_model::size_heightRelative_type(instance):
    assert isinstance(instance.heightRelative, bool)


@given(instance=model::Size_strategy)
def test_model::size_heightRelative_setter(instance):
    original = instance.heightRelative
    instance.heightRelative = original
    assert instance.heightRelative == original

@given(instance=model::Size_strategy)
def test_model::size_resizable_type(instance):
    assert isinstance(instance.resizable, bool)


@given(instance=model::Size_strategy)
def test_model::size_resizable_setter(instance):
    original = instance.resizable
    instance.resizable = original
    assert instance.resizable == original

@given(instance=model::Size_strategy)
def test_model::size_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=model::Size_strategy)
def test_model::size_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model::LineWidth_strategy)
@settings(max_examples=50)
def test_model::linewidth_instantiation(instance):
    assert isinstance(instance, model::LineWidth)

@given(instance=model::LineWidth_strategy)
def test_model::linewidth_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=model::LineWidth_strategy)
def test_model::linewidth_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model::Layout_strategy)
@settings(max_examples=50)
def test_model::layout_instantiation(instance):
    assert isinstance(instance, model::Layout)

@given(instance=model::Layout_strategy)
def test_model::layout_horizontal_type(instance):
    assert isinstance(instance.horizontal, bool)


@given(instance=model::Layout_strategy)
def test_model::layout_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original

@given(instance=model::Layout_strategy)
def test_model::layout_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=model::Layout_strategy)
def test_model::layout_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=model::Layout_strategy)
def test_model::layout_margin_type(instance):
    assert isinstance(instance.margin, int)


@given(instance=model::Layout_strategy)
def test_model::layout_margin_setter(instance):
    original = instance.margin
    instance.margin = original
    assert instance.margin == original

@given(instance=model::TextAlign_strategy)
@settings(max_examples=50)
def test_model::textalign_instantiation(instance):
    assert isinstance(instance, model::TextAlign)

@given(instance=model::TextAlign_strategy)
def test_model::textalign_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::TextAlign_strategy)
def test_model::textalign_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::LineStyle_strategy)
@settings(max_examples=50)
def test_model::linestyle_instantiation(instance):
    assert isinstance(instance, model::LineStyle)

@given(instance=model::LineStyle_strategy)
def test_model::linestyle_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=model::LineStyle_strategy)
def test_model::linestyle_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=model::LineStyle_strategy)
def test_model::linestyle_manhattan_type(instance):
    assert isinstance(instance.manhattan, bool)


@given(instance=model::LineStyle_strategy)
def test_model::linestyle_manhattan_setter(instance):
    original = instance.manhattan
    instance.manhattan = original
    assert instance.manhattan == original

@given(instance=model::Anchor_strategy)
@settings(max_examples=50)
def test_model::anchor_instantiation(instance):
    assert isinstance(instance, model::Anchor)

@given(instance=model::Anchor_strategy)
def test_model::anchor_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=model::Anchor_strategy)
def test_model::anchor_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=model::Anchor_strategy)
def test_model::anchor_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=model::Anchor_strategy)
def test_model::anchor_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=model::Rhombus_strategy)
@settings(max_examples=50)
def test_model::rhombus_instantiation(instance):
    assert isinstance(instance, model::Rhombus)

@given(instance=model::Label_strategy)
@settings(max_examples=50)
def test_model::label_instantiation(instance):
    assert isinstance(instance, model::Label)

@given(instance=model::Rectangle_strategy)
@settings(max_examples=50)
def test_model::rectangle_instantiation(instance):
    assert isinstance(instance, model::Rectangle)

@given(instance=model::Rectangle_strategy)
def test_model::rectangle_square_type(instance):
    assert isinstance(instance.square, bool)


@given(instance=model::Rectangle_strategy)
def test_model::rectangle_square_setter(instance):
    original = instance.square
    instance.square = original
    assert instance.square == original

@given(instance=model::Rectangle_strategy)
def test_model::rectangle_rectangle_type(instance):
    assert isinstance(instance.rectangle, bool)


@given(instance=model::Rectangle_strategy)
def test_model::rectangle_rectangle_setter(instance):
    original = instance.rectangle
    instance.rectangle = original
    assert instance.rectangle == original

@given(instance=model::Ellipse_strategy)
@settings(max_examples=50)
def test_model::ellipse_instantiation(instance):
    assert isinstance(instance, model::Ellipse)

@given(instance=model::Ellipse_strategy)
def test_model::ellipse_ellipse_type(instance):
    assert isinstance(instance.ellipse, bool)


@given(instance=model::Ellipse_strategy)
def test_model::ellipse_ellipse_setter(instance):
    original = instance.ellipse
    instance.ellipse = original
    assert instance.ellipse == original

@given(instance=model::Ellipse_strategy)
def test_model::ellipse_circle_type(instance):
    assert isinstance(instance.circle, bool)


@given(instance=model::Ellipse_strategy)
def test_model::ellipse_circle_setter(instance):
    original = instance.circle
    instance.circle = original
    assert instance.circle == original

@given(instance=model::Triangle_strategy)
@settings(max_examples=50)
def test_model::triangle_instantiation(instance):
    assert isinstance(instance, model::Triangle)

@given(instance=model::Image_strategy)
@settings(max_examples=50)
def test_model::image_instantiation(instance):
    assert isinstance(instance, model::Image)

@given(instance=model::Image_strategy)
def test_model::image_imageId_type(instance):
    assert isinstance(instance.imageId, str)


@given(instance=model::Image_strategy)
def test_model::image_imageId_setter(instance):
    original = instance.imageId
    instance.imageId = original
    assert instance.imageId == original

@given(instance=model::Polyline_strategy)
@settings(max_examples=50)
def test_model::polyline_instantiation(instance):
    assert isinstance(instance, model::Polyline)

@given(instance=model::Polyline_strategy)
def test_model::polyline_polyline_type(instance):
    assert isinstance(instance.polyline, bool)


@given(instance=model::Polyline_strategy)
def test_model::polyline_polyline_setter(instance):
    original = instance.polyline
    instance.polyline = original
    assert instance.polyline == original

@given(instance=model::Polyline_strategy)
def test_model::polyline_polygon_type(instance):
    assert isinstance(instance.polygon, bool)


@given(instance=model::Polyline_strategy)
def test_model::polyline_polygon_setter(instance):
    original = instance.polygon
    instance.polygon = original
    assert instance.polygon == original

@given(instance=model::Invisible_strategy)
@settings(max_examples=50)
def test_model::invisible_instantiation(instance):
    assert isinstance(instance, model::Invisible)

@given(instance=model::Custom_strategy)
@settings(max_examples=50)
def test_model::custom_instantiation(instance):
    assert isinstance(instance, model::Custom)

@given(instance=model::Color_strategy)
@settings(max_examples=50)
def test_model::color_instantiation(instance):
    assert isinstance(instance, model::Color)

@given(instance=model::Color_strategy)
def test_model::color_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=model::Color_strategy)
def test_model::color_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=model::Contains_strategy)
@settings(max_examples=50)
def test_model::contains_instantiation(instance):
    assert isinstance(instance, model::Contains)

@given(instance=model::EClass_strategy)
@settings(max_examples=50)
def test_model::eclass_instantiation(instance):
    assert isinstance(instance, model::EClass)

@given(instance=model::ImportStatement_strategy)
@settings(max_examples=50)
def test_model::importstatement_instantiation(instance):
    assert isinstance(instance, model::ImportStatement)

@given(instance=model::ImportStatement_strategy)
def test_model::importstatement_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=model::ImportStatement_strategy)
def test_model::importstatement_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=model::CustomFigure_strategy)
@settings(max_examples=50)
def test_model::customfigure_instantiation(instance):
    assert isinstance(instance, model::CustomFigure)

@given(instance=model::CustomFigure_strategy)
def test_model::customfigure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::CustomFigure_strategy)
def test_model::customfigure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::DiagramElement_strategy)
@settings(max_examples=50)
def test_model::diagramelement_instantiation(instance):
    assert isinstance(instance, model::DiagramElement)

@given(instance=model::Colors_strategy)
@settings(max_examples=50)
def test_model::colors_instantiation(instance):
    assert isinstance(instance, model::Colors)

@given(instance=model::Decorator_strategy)
@settings(max_examples=50)
def test_model::decorator_instantiation(instance):
    assert isinstance(instance, model::Decorator)

@given(instance=model::EReference_strategy)
@settings(max_examples=50)
def test_model::ereference_instantiation(instance):
    assert isinstance(instance, model::EReference)

@given(instance=FeatureContainer_strategy)
@settings(max_examples=50)
def test_featurecontainer_instantiation(instance):
    assert isinstance(instance, FeatureContainer)

@given(instance=model::Arrow_strategy)
@settings(max_examples=50)
def test_model::arrow_instantiation(instance):
    assert isinstance(instance, model::Arrow)

@given(instance=model::Line_strategy)
@settings(max_examples=50)
def test_model::line_instantiation(instance):
    assert isinstance(instance, model::Line)

@given(instance=model::Line_strategy)
def test_model::line_horizontal_type(instance):
    assert isinstance(instance.horizontal, bool)


@given(instance=model::Line_strategy)
def test_model::line_horizontal_setter(instance):
    original = instance.horizontal
    instance.horizontal = original
    assert instance.horizontal == original

@given(instance=model::Line_strategy)
def test_model::line_vertical_type(instance):
    assert isinstance(instance.vertical, bool)


@given(instance=model::Line_strategy)
def test_model::line_vertical_setter(instance):
    original = instance.vertical
    instance.vertical = original
    assert instance.vertical == original

@given(instance=model::ConnectableElement_strategy)
@settings(max_examples=50)
def test_model::connectableelement_instantiation(instance):
    assert isinstance(instance, model::ConnectableElement)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=model::Link_strategy)
@settings(max_examples=50)
def test_model::link_instantiation(instance):
    assert isinstance(instance, model::Link)

@given(instance=model::Link_strategy)
def test_model::link_complex_type(instance):
    assert isinstance(instance.complex, bool)


@given(instance=model::Link_strategy)
def test_model::link_complex_setter(instance):
    original = instance.complex
    instance.complex = original
    assert instance.complex == original

@given(instance=model::Link_strategy)
def test_model::link_reference_type(instance):
    assert isinstance(instance.reference, bool)


@given(instance=model::Link_strategy)
def test_model::link_reference_setter(instance):
    original = instance.reference
    instance.reference = original
    assert instance.reference == original

@given(instance=model::Node_strategy)
@settings(max_examples=50)
def test_model::node_instantiation(instance):
    assert isinstance(instance, model::Node)

@given(instance=model::Value_strategy)
@settings(max_examples=50)
def test_model::value_instantiation(instance):
    assert isinstance(instance, model::Value)

@given(instance=model::EAttribute_strategy)
@settings(max_examples=50)
def test_model::eattribute_instantiation(instance):
    assert isinstance(instance, model::EAttribute)

@given(instance=model::FeatureContainer_strategy)
@settings(max_examples=50)
def test_model::featurecontainer_instantiation(instance):
    assert isinstance(instance, model::FeatureContainer)

@given(instance=model::FeatureConditional_strategy)
@settings(max_examples=50)
def test_model::featureconditional_instantiation(instance):
    assert isinstance(instance, model::FeatureConditional)

@given(instance=model::FeatureConditional_strategy)
def test_model::featureconditional_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=model::FeatureConditional_strategy)
def test_model::featureconditional_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=model::Feature_strategy)
@settings(max_examples=50)
def test_model::feature_instantiation(instance):
    assert isinstance(instance, model::Feature)

@given(instance=model::Diagram_strategy)
@settings(max_examples=50)
def test_model::diagram_instantiation(instance):
    assert isinstance(instance, model::Diagram)

@given(instance=model::MetaModel_strategy)
@settings(max_examples=50)
def test_model::metamodel_instantiation(instance):
    assert isinstance(instance, model::MetaModel)

@given(instance=model::MetaModel_strategy)
def test_model::metamodel_plugin_type(instance):
    assert isinstance(instance.plugin, str)


@given(instance=model::MetaModel_strategy)
def test_model::metamodel_plugin_setter(instance):
    original = instance.plugin
    instance.plugin = original
    assert instance.plugin == original

@given(instance=model::MetaModel_strategy)
def test_model::metamodel_ecorePath_type(instance):
    assert isinstance(instance.ecorePath, str)


@given(instance=model::MetaModel_strategy)
def test_model::metamodel_ecorePath_setter(instance):
    original = instance.ecorePath
    instance.ecorePath = original
    assert instance.ecorePath == original

@given(instance=model::XDiagram_strategy)
@settings(max_examples=50)
def test_model::xdiagram_instantiation(instance):
    assert isinstance(instance, model::XDiagram)
