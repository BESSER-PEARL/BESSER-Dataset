import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    notation::Point,
    Figure,
    notation::Cube,
    notation::Polyline,
    notation::Triangle,
    notation::Diamond,
    notation::Cylinder,
    notation::Roundtangle,
    notation::Circle,
    notation::Square,
    notation::Rectangle,
    Style,
    notation::Style,
    Value,
    notation::ReferenceValue,
    notation::AttributeValue,
    TextualElement,
    notation::Value,
    notation::Keyword,
    notation::Token,
    notation::TextualContainment,
    notation::TextStyle,
    notation::IconStyle,
    notation::FigureContainment,
    GraphicalElement,
    notation::Icon,
    notation::Label,
    notation::Composite,
    notation::Image,
    notation::SyntaxOf,
    notation::BorderStyle,
    notation::FigureStyle,
    notation::Figure,
    notation::LineStyle,
    notation::Line,
    DiagramElement,
    notation::Node,
    IDElement,
    notation::GraphicalElement,
    notation::TextualElement,
    notation::IDElement,
    notation::DiagramElement,
    notation::DiagramDefinition,
    Relation,
    notation::Link,
    notation::Compartment,
    notation::Relation,
    notation::NotationDefinition,
    Orientation,
    FillTextureType,
    IconType,
    AudienceType,
    DefinitionType,
    Color,
    LineTextureType,
    Layout,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_notation::point_is_not_abstract():
    assert not inspect.isabstract(notation::Point)


def test_notation::point_constructor_exists():
    assert callable(notation::Point.__init__)


def test_notation::point_constructor_args():
    sig = inspect.signature(notation::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_notation::point_has_x():
    assert hasattr(notation::Point, "x")
    descriptor = None
    for klass in notation::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation::point_has_y():
    assert hasattr(notation::Point, "y")
    descriptor = None
    for klass in notation::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation::cube_is_not_abstract():
    assert not inspect.isabstract(notation::Cube)


def test_notation::cube_constructor_exists():
    assert callable(notation::Cube.__init__)


def test_notation::cube_constructor_args():
    sig = inspect.signature(notation::Cube.__init__)
    params = list(sig.parameters.keys())



def test_notation::polyline_is_not_abstract():
    assert not inspect.isabstract(notation::Polyline)


def test_notation::polyline_constructor_exists():
    assert callable(notation::Polyline.__init__)


def test_notation::polyline_constructor_args():
    sig = inspect.signature(notation::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_notation::triangle_is_not_abstract():
    assert not inspect.isabstract(notation::Triangle)


def test_notation::triangle_constructor_exists():
    assert callable(notation::Triangle.__init__)


def test_notation::triangle_constructor_args():
    sig = inspect.signature(notation::Triangle.__init__)
    params = list(sig.parameters.keys())



def test_notation::diamond_is_not_abstract():
    assert not inspect.isabstract(notation::Diamond)


def test_notation::diamond_constructor_exists():
    assert callable(notation::Diamond.__init__)


def test_notation::diamond_constructor_args():
    sig = inspect.signature(notation::Diamond.__init__)
    params = list(sig.parameters.keys())



def test_notation::cylinder_is_not_abstract():
    assert not inspect.isabstract(notation::Cylinder)


def test_notation::cylinder_constructor_exists():
    assert callable(notation::Cylinder.__init__)


def test_notation::cylinder_constructor_args():
    sig = inspect.signature(notation::Cylinder.__init__)
    params = list(sig.parameters.keys())



def test_notation::roundtangle_is_not_abstract():
    assert not inspect.isabstract(notation::Roundtangle)


def test_notation::roundtangle_constructor_exists():
    assert callable(notation::Roundtangle.__init__)


def test_notation::roundtangle_constructor_args():
    sig = inspect.signature(notation::Roundtangle.__init__)
    params = list(sig.parameters.keys())



def test_notation::circle_is_not_abstract():
    assert not inspect.isabstract(notation::Circle)


def test_notation::circle_constructor_exists():
    assert callable(notation::Circle.__init__)


def test_notation::circle_constructor_args():
    sig = inspect.signature(notation::Circle.__init__)
    params = list(sig.parameters.keys())



def test_notation::square_is_not_abstract():
    assert not inspect.isabstract(notation::Square)


def test_notation::square_constructor_exists():
    assert callable(notation::Square.__init__)


def test_notation::square_constructor_args():
    sig = inspect.signature(notation::Square.__init__)
    params = list(sig.parameters.keys())



def test_notation::rectangle_is_not_abstract():
    assert not inspect.isabstract(notation::Rectangle)


def test_notation::rectangle_constructor_exists():
    assert callable(notation::Rectangle.__init__)


def test_notation::rectangle_constructor_args():
    sig = inspect.signature(notation::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_style_is_not_abstract():
    assert not inspect.isabstract(Style)


def test_style_constructor_exists():
    assert callable(Style.__init__)


def test_style_constructor_args():
    sig = inspect.signature(Style.__init__)
    params = list(sig.parameters.keys())



def test_notation::style_is_not_abstract():
    assert not inspect.isabstract(notation::Style)


def test_notation::style_constructor_exists():
    assert callable(notation::Style.__init__)


def test_notation::style_constructor_args():
    sig = inspect.signature(notation::Style.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_notation::referencevalue_is_not_abstract():
    assert not inspect.isabstract(notation::ReferenceValue)


def test_notation::referencevalue_constructor_exists():
    assert callable(notation::ReferenceValue.__init__)


def test_notation::referencevalue_constructor_args():
    sig = inspect.signature(notation::ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_notation::attributevalue_is_not_abstract():
    assert not inspect.isabstract(notation::AttributeValue)


def test_notation::attributevalue_constructor_exists():
    assert callable(notation::AttributeValue.__init__)


def test_notation::attributevalue_constructor_args():
    sig = inspect.signature(notation::AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_textualelement_is_not_abstract():
    assert not inspect.isabstract(TextualElement)


def test_textualelement_constructor_exists():
    assert callable(TextualElement.__init__)


def test_textualelement_constructor_args():
    sig = inspect.signature(TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::value_is_not_abstract():
    assert not inspect.isabstract(notation::Value)


def test_notation::value_constructor_exists():
    assert callable(notation::Value.__init__)


def test_notation::value_constructor_args():
    sig = inspect.signature(notation::Value.__init__)
    params = list(sig.parameters.keys())



def test_notation::keyword_is_not_abstract():
    assert not inspect.isabstract(notation::Keyword)


def test_notation::keyword_constructor_exists():
    assert callable(notation::Keyword.__init__)


def test_notation::keyword_constructor_args():
    sig = inspect.signature(notation::Keyword.__init__)
    params = list(sig.parameters.keys())



def test_notation::token_is_not_abstract():
    assert not inspect.isabstract(notation::Token)


def test_notation::token_constructor_exists():
    assert callable(notation::Token.__init__)


def test_notation::token_constructor_args():
    sig = inspect.signature(notation::Token.__init__)
    params = list(sig.parameters.keys())



def test_notation::textualcontainment_is_not_abstract():
    assert not inspect.isabstract(notation::TextualContainment)


def test_notation::textualcontainment_constructor_exists():
    assert callable(notation::TextualContainment.__init__)


def test_notation::textualcontainment_constructor_args():
    sig = inspect.signature(notation::TextualContainment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation::textualcontainment_has_layout():
    assert hasattr(notation::TextualContainment, "layout")
    descriptor = None
    for klass in notation::TextualContainment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation::textstyle_is_not_abstract():
    assert not inspect.isabstract(notation::TextStyle)


def test_notation::textstyle_constructor_exists():
    assert callable(notation::TextStyle.__init__)


def test_notation::textstyle_constructor_args():
    sig = inspect.signature(notation::TextStyle.__init__)
    params = list(sig.parameters.keys())
    assert "italic" in params, "Missing parameter 'italic'"
    assert "bold" in params, "Missing parameter 'bold'"
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "underlined" in params, "Missing parameter 'underlined'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"
    assert "fontName" in params, "Missing parameter 'fontName'"

def test_notation::textstyle_has_italic():
    assert hasattr(notation::TextStyle, "italic")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "italic" in klass.__dict__:
            descriptor = klass.__dict__["italic"]
            break
    assert isinstance(descriptor, property)

def test_notation::textstyle_has_bold():
    assert hasattr(notation::TextStyle, "bold")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "bold" in klass.__dict__:
            descriptor = klass.__dict__["bold"]
            break
    assert isinstance(descriptor, property)

def test_notation::textstyle_has_fontColor():
    assert hasattr(notation::TextStyle, "fontColor")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "fontColor" in klass.__dict__:
            descriptor = klass.__dict__["fontColor"]
            break
    assert isinstance(descriptor, property)

def test_notation::textstyle_has_underlined():
    assert hasattr(notation::TextStyle, "underlined")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "underlined" in klass.__dict__:
            descriptor = klass.__dict__["underlined"]
            break
    assert isinstance(descriptor, property)

def test_notation::textstyle_has_fontSize():
    assert hasattr(notation::TextStyle, "fontSize")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)

def test_notation::textstyle_has_fontName():
    assert hasattr(notation::TextStyle, "fontName")
    descriptor = None
    for klass in notation::TextStyle.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)



def test_notation::iconstyle_is_not_abstract():
    assert not inspect.isabstract(notation::IconStyle)


def test_notation::iconstyle_constructor_exists():
    assert callable(notation::IconStyle.__init__)


def test_notation::iconstyle_constructor_args():
    sig = inspect.signature(notation::IconStyle.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "color" in params, "Missing parameter 'color'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "height" in params, "Missing parameter 'height'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_notation::iconstyle_has_width():
    assert hasattr(notation::IconStyle, "width")
    descriptor = None
    for klass in notation::IconStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation::iconstyle_has_color():
    assert hasattr(notation::IconStyle, "color")
    descriptor = None
    for klass in notation::IconStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation::iconstyle_has_brightness():
    assert hasattr(notation::IconStyle, "brightness")
    descriptor = None
    for klass in notation::IconStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_notation::iconstyle_has_height():
    assert hasattr(notation::IconStyle, "height")
    descriptor = None
    for klass in notation::IconStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation::iconstyle_has_orientation():
    assert hasattr(notation::IconStyle, "orientation")
    descriptor = None
    for klass in notation::IconStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_notation::figurecontainment_is_not_abstract():
    assert not inspect.isabstract(notation::FigureContainment)


def test_notation::figurecontainment_constructor_exists():
    assert callable(notation::FigureContainment.__init__)


def test_notation::figurecontainment_constructor_args():
    sig = inspect.signature(notation::FigureContainment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation::figurecontainment_has_layout():
    assert hasattr(notation::FigureContainment, "layout")
    descriptor = None
    for klass in notation::FigureContainment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::icon_is_not_abstract():
    assert not inspect.isabstract(notation::Icon)


def test_notation::icon_constructor_exists():
    assert callable(notation::Icon.__init__)


def test_notation::icon_constructor_args():
    sig = inspect.signature(notation::Icon.__init__)
    params = list(sig.parameters.keys())
    assert "iconType" in params, "Missing parameter 'iconType'"

def test_notation::icon_has_iconType():
    assert hasattr(notation::Icon, "iconType")
    descriptor = None
    for klass in notation::Icon.__mro__:
        if "iconType" in klass.__dict__:
            descriptor = klass.__dict__["iconType"]
            break
    assert isinstance(descriptor, property)



def test_notation::label_is_not_abstract():
    assert not inspect.isabstract(notation::Label)


def test_notation::label_constructor_exists():
    assert callable(notation::Label.__init__)


def test_notation::label_constructor_args():
    sig = inspect.signature(notation::Label.__init__)
    params = list(sig.parameters.keys())



def test_notation::composite_is_not_abstract():
    assert not inspect.isabstract(notation::Composite)


def test_notation::composite_constructor_exists():
    assert callable(notation::Composite.__init__)


def test_notation::composite_constructor_args():
    sig = inspect.signature(notation::Composite.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation::composite_has_layout():
    assert hasattr(notation::Composite, "layout")
    descriptor = None
    for klass in notation::Composite.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation::image_is_not_abstract():
    assert not inspect.isabstract(notation::Image)


def test_notation::image_constructor_exists():
    assert callable(notation::Image.__init__)


def test_notation::image_constructor_args():
    sig = inspect.signature(notation::Image.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_notation::image_has_path():
    assert hasattr(notation::Image, "path")
    descriptor = None
    for klass in notation::Image.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_notation::syntaxof_is_not_abstract():
    assert not inspect.isabstract(notation::SyntaxOf)


def test_notation::syntaxof_constructor_exists():
    assert callable(notation::SyntaxOf.__init__)


def test_notation::syntaxof_constructor_args():
    sig = inspect.signature(notation::SyntaxOf.__init__)
    params = list(sig.parameters.keys())



def test_notation::borderstyle_is_not_abstract():
    assert not inspect.isabstract(notation::BorderStyle)


def test_notation::borderstyle_constructor_exists():
    assert callable(notation::BorderStyle.__init__)


def test_notation::borderstyle_constructor_args():
    sig = inspect.signature(notation::BorderStyle.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "thickness" in params, "Missing parameter 'thickness'"

def test_notation::borderstyle_has_color():
    assert hasattr(notation::BorderStyle, "color")
    descriptor = None
    for klass in notation::BorderStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation::borderstyle_has_texture():
    assert hasattr(notation::BorderStyle, "texture")
    descriptor = None
    for klass in notation::BorderStyle.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_notation::borderstyle_has_thickness():
    assert hasattr(notation::BorderStyle, "thickness")
    descriptor = None
    for klass in notation::BorderStyle.__mro__:
        if "thickness" in klass.__dict__:
            descriptor = klass.__dict__["thickness"]
            break
    assert isinstance(descriptor, property)



def test_notation::figurestyle_is_not_abstract():
    assert not inspect.isabstract(notation::FigureStyle)


def test_notation::figurestyle_constructor_exists():
    assert callable(notation::FigureStyle.__init__)


def test_notation::figurestyle_constructor_args():
    sig = inspect.signature(notation::FigureStyle.__init__)
    params = list(sig.parameters.keys())
    assert "fillTexture" in params, "Missing parameter 'fillTexture'"
    assert "fillTextureColor" in params, "Missing parameter 'fillTextureColor'"
    assert "orientation" in params, "Missing parameter 'orientation'"
    assert "fillOrientation" in params, "Missing parameter 'fillOrientation'"
    assert "width" in params, "Missing parameter 'width'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"
    assert "height" in params, "Missing parameter 'height'"
    assert "brightness" in params, "Missing parameter 'brightness'"

def test_notation::figurestyle_has_fillTexture():
    assert hasattr(notation::FigureStyle, "fillTexture")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "fillTexture" in klass.__dict__:
            descriptor = klass.__dict__["fillTexture"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_fillTextureColor():
    assert hasattr(notation::FigureStyle, "fillTextureColor")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "fillTextureColor" in klass.__dict__:
            descriptor = klass.__dict__["fillTextureColor"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_orientation():
    assert hasattr(notation::FigureStyle, "orientation")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_fillOrientation():
    assert hasattr(notation::FigureStyle, "fillOrientation")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "fillOrientation" in klass.__dict__:
            descriptor = klass.__dict__["fillOrientation"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_width():
    assert hasattr(notation::FigureStyle, "width")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_fillColor():
    assert hasattr(notation::FigureStyle, "fillColor")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "fillColor" in klass.__dict__:
            descriptor = klass.__dict__["fillColor"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_height():
    assert hasattr(notation::FigureStyle, "height")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation::figurestyle_has_brightness():
    assert hasattr(notation::FigureStyle, "brightness")
    descriptor = None
    for klass in notation::FigureStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)



def test_notation::figure_is_not_abstract():
    assert not inspect.isabstract(notation::Figure)


def test_notation::figure_constructor_exists():
    assert callable(notation::Figure.__init__)


def test_notation::figure_constructor_args():
    sig = inspect.signature(notation::Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation::linestyle_is_not_abstract():
    assert not inspect.isabstract(notation::LineStyle)


def test_notation::linestyle_constructor_exists():
    assert callable(notation::LineStyle.__init__)


def test_notation::linestyle_constructor_args():
    sig = inspect.signature(notation::LineStyle.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "color" in params, "Missing parameter 'color'"
    assert "texture" in params, "Missing parameter 'texture'"
    assert "brightness" in params, "Missing parameter 'brightness'"
    assert "thickness" in params, "Missing parameter 'thickness'"
    assert "orientation" in params, "Missing parameter 'orientation'"

def test_notation::linestyle_has_length():
    assert hasattr(notation::LineStyle, "length")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_color():
    assert hasattr(notation::LineStyle, "color")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_texture():
    assert hasattr(notation::LineStyle, "texture")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "texture" in klass.__dict__:
            descriptor = klass.__dict__["texture"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_brightness():
    assert hasattr(notation::LineStyle, "brightness")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "brightness" in klass.__dict__:
            descriptor = klass.__dict__["brightness"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_thickness():
    assert hasattr(notation::LineStyle, "thickness")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "thickness" in klass.__dict__:
            descriptor = klass.__dict__["thickness"]
            break
    assert isinstance(descriptor, property)

def test_notation::linestyle_has_orientation():
    assert hasattr(notation::LineStyle, "orientation")
    descriptor = None
    for klass in notation::LineStyle.__mro__:
        if "orientation" in klass.__dict__:
            descriptor = klass.__dict__["orientation"]
            break
    assert isinstance(descriptor, property)



def test_notation::line_is_not_abstract():
    assert not inspect.isabstract(notation::Line)


def test_notation::line_constructor_exists():
    assert callable(notation::Line.__init__)


def test_notation::line_constructor_args():
    sig = inspect.signature(notation::Line.__init__)
    params = list(sig.parameters.keys())



def test_diagramelement_is_not_abstract():
    assert not inspect.isabstract(DiagramElement)


def test_diagramelement_constructor_exists():
    assert callable(DiagramElement.__init__)


def test_diagramelement_constructor_args():
    sig = inspect.signature(DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::node_is_not_abstract():
    assert not inspect.isabstract(notation::Node)


def test_notation::node_constructor_exists():
    assert callable(notation::Node.__init__)


def test_notation::node_constructor_args():
    sig = inspect.signature(notation::Node.__init__)
    params = list(sig.parameters.keys())



def test_idelement_is_not_abstract():
    assert not inspect.isabstract(IDElement)


def test_idelement_constructor_exists():
    assert callable(IDElement.__init__)


def test_idelement_constructor_args():
    sig = inspect.signature(IDElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::graphicalelement_is_not_abstract():
    assert not inspect.isabstract(notation::GraphicalElement)


def test_notation::graphicalelement_constructor_exists():
    assert callable(notation::GraphicalElement.__init__)


def test_notation::graphicalelement_constructor_args():
    sig = inspect.signature(notation::GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::textualelement_is_not_abstract():
    assert not inspect.isabstract(notation::TextualElement)


def test_notation::textualelement_constructor_exists():
    assert callable(notation::TextualElement.__init__)


def test_notation::textualelement_constructor_args():
    sig = inspect.signature(notation::TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::idelement_is_not_abstract():
    assert not inspect.isabstract(notation::IDElement)


def test_notation::idelement_constructor_exists():
    assert callable(notation::IDElement.__init__)


def test_notation::idelement_constructor_args():
    sig = inspect.signature(notation::IDElement.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_notation::idelement_has_ID():
    assert hasattr(notation::IDElement, "ID")
    descriptor = None
    for klass in notation::IDElement.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_notation::diagramelement_is_not_abstract():
    assert not inspect.isabstract(notation::DiagramElement)


def test_notation::diagramelement_constructor_exists():
    assert callable(notation::DiagramElement.__init__)


def test_notation::diagramelement_constructor_args():
    sig = inspect.signature(notation::DiagramElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::diagramdefinition_is_not_abstract():
    assert not inspect.isabstract(notation::DiagramDefinition)


def test_notation::diagramdefinition_constructor_exists():
    assert callable(notation::DiagramDefinition.__init__)


def test_notation::diagramdefinition_constructor_args():
    sig = inspect.signature(notation::DiagramDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "Legend" in params, "Missing parameter 'Legend'"
    assert "allowChunks" in params, "Missing parameter 'allowChunks'"
    assert "targetedAudience" in params, "Missing parameter 'targetedAudience'"
    assert "Level" in params, "Missing parameter 'Level'"

def test_notation::diagramdefinition_has_Legend():
    assert hasattr(notation::DiagramDefinition, "Legend")
    descriptor = None
    for klass in notation::DiagramDefinition.__mro__:
        if "Legend" in klass.__dict__:
            descriptor = klass.__dict__["Legend"]
            break
    assert isinstance(descriptor, property)

def test_notation::diagramdefinition_has_allowChunks():
    assert hasattr(notation::DiagramDefinition, "allowChunks")
    descriptor = None
    for klass in notation::DiagramDefinition.__mro__:
        if "allowChunks" in klass.__dict__:
            descriptor = klass.__dict__["allowChunks"]
            break
    assert isinstance(descriptor, property)

def test_notation::diagramdefinition_has_targetedAudience():
    assert hasattr(notation::DiagramDefinition, "targetedAudience")
    descriptor = None
    for klass in notation::DiagramDefinition.__mro__:
        if "targetedAudience" in klass.__dict__:
            descriptor = klass.__dict__["targetedAudience"]
            break
    assert isinstance(descriptor, property)

def test_notation::diagramdefinition_has_Level():
    assert hasattr(notation::DiagramDefinition, "Level")
    descriptor = None
    for klass in notation::DiagramDefinition.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_notation::link_is_not_abstract():
    assert not inspect.isabstract(notation::Link)


def test_notation::link_constructor_exists():
    assert callable(notation::Link.__init__)


def test_notation::link_constructor_args():
    sig = inspect.signature(notation::Link.__init__)
    params = list(sig.parameters.keys())



def test_notation::compartment_is_not_abstract():
    assert not inspect.isabstract(notation::Compartment)


def test_notation::compartment_constructor_exists():
    assert callable(notation::Compartment.__init__)


def test_notation::compartment_constructor_args():
    sig = inspect.signature(notation::Compartment.__init__)
    params = list(sig.parameters.keys())
    assert "layout" in params, "Missing parameter 'layout'"

def test_notation::compartment_has_layout():
    assert hasattr(notation::Compartment, "layout")
    descriptor = None
    for klass in notation::Compartment.__mro__:
        if "layout" in klass.__dict__:
            descriptor = klass.__dict__["layout"]
            break
    assert isinstance(descriptor, property)



def test_notation::relation_is_not_abstract():
    assert not inspect.isabstract(notation::Relation)


def test_notation::relation_constructor_exists():
    assert callable(notation::Relation.__init__)


def test_notation::relation_constructor_args():
    sig = inspect.signature(notation::Relation.__init__)
    params = list(sig.parameters.keys())



def test_notation::notationdefinition_is_not_abstract():
    assert not inspect.isabstract(notation::NotationDefinition)


def test_notation::notationdefinition_constructor_exists():
    assert callable(notation::NotationDefinition.__init__)


def test_notation::notationdefinition_constructor_args():
    sig = inspect.signature(notation::NotationDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_notation::notationdefinition_has_Type():
    assert hasattr(notation::NotationDefinition, "Type")
    descriptor = None
    for klass in notation::NotationDefinition.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_orientation_exists():
    # Check that the Enumeration exists
    assert Orientation is not None

def test_orientation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Orientation]
    expected_literals = [
        "RIGHT_DIAGONAL",
        "VERTICAL",
        "HORIZONTAL",
        "LEFT_DIAGONAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Orientation"

def test_filltexturetype_exists():
    # Check that the Enumeration exists
    assert FillTextureType is not None

def test_filltexturetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FillTextureType]
    expected_literals = [
        "STRIP",
        "NONE",
        "DASHDOTDOT",
        "DOT",
        "DASH",
        "DASHDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FillTextureType"

def test_icontype_exists():
    # Check that the Enumeration exists
    assert IconType is not None

def test_icontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IconType]
    expected_literals = [
        "ARROW",
        "CROSS",
        "LETTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IconType"

def test_audiencetype_exists():
    # Check that the Enumeration exists
    assert AudienceType is not None

def test_audiencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AudienceType]
    expected_literals = [
        "BEGINNER",
        "BOTH",
        "EXPERT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AudienceType"

def test_definitiontype_exists():
    # Check that the Enumeration exists
    assert DefinitionType is not None

def test_definitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefinitionType]
    expected_literals = [
        "HYBRID",
        "TEXTUAL",
        "GRAPHICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefinitionType"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "WHITE",
        "DARK_BLUE",
        "CYAN",
        "BLACK",
        "DARK_GRAY",
        "DARK_GREEN",
        "LIGHT_GREEN",
        "GRAY",
        "YELLOW",
        "GREEN",
        "LIGHT_BLUE",
        "BLUE",
        "ORANGE",
        "LIGHT_GRAY",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_linetexturetype_exists():
    # Check that the Enumeration exists
    assert LineTextureType is not None

def test_linetexturetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineTextureType]
    expected_literals = [
        "SOLID",
        "INVISIBLE",
        "DOUBLE",
        "DASHDOTDOT",
        "DASH",
        "DOT",
        "DASHDOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineTextureType"

def test_layout_exists():
    # Check that the Enumeration exists
    assert Layout is not None

def test_layout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Layout]
    expected_literals = [
        "HORIZONTAL",
        "UNKNOWN",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Layout"


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
notation::Point_strategy = st.builds(
    notation::Point,
    x=
        st.integers(),
    y=
        st.integers()
)
Figure_strategy = st.builds(
    Figure,
)
notation::Cube_strategy = st.builds(
    notation::Cube,
)
notation::Polyline_strategy = st.builds(
    notation::Polyline,
)
notation::Triangle_strategy = st.builds(
    notation::Triangle,
)
notation::Diamond_strategy = st.builds(
    notation::Diamond,
)
notation::Cylinder_strategy = st.builds(
    notation::Cylinder,
)
notation::Roundtangle_strategy = st.builds(
    notation::Roundtangle,
)
notation::Circle_strategy = st.builds(
    notation::Circle,
)
notation::Square_strategy = st.builds(
    notation::Square,
)
notation::Rectangle_strategy = st.builds(
    notation::Rectangle,
)
Style_strategy = st.builds(
    Style,
)
notation::Style_strategy = st.builds(
    notation::Style,
)
Value_strategy = st.builds(
    Value,
)
notation::ReferenceValue_strategy = st.builds(
    notation::ReferenceValue,
)
notation::AttributeValue_strategy = st.builds(
    notation::AttributeValue,
)
TextualElement_strategy = st.builds(
    TextualElement,
)
notation::Value_strategy = st.builds(
    notation::Value,
)
notation::Keyword_strategy = st.builds(
    notation::Keyword,
)
notation::Token_strategy = st.builds(
    notation::Token,
)
notation::TextualContainment_strategy = st.builds(
    notation::TextualContainment,
    layout=
        safe_text
)
notation::TextStyle_strategy = st.builds(
    notation::TextStyle,
    italic=
        st.booleans(),
    bold=
        st.booleans(),
    fontColor=
        safe_text,
    underlined=
        st.booleans(),
    fontSize=
        st.integers(),
    fontName=
        safe_text
)
notation::IconStyle_strategy = st.builds(
    notation::IconStyle,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    brightness=
        st.integers(),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    orientation=
        safe_text
)
notation::FigureContainment_strategy = st.builds(
    notation::FigureContainment,
    layout=
        safe_text
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
notation::Icon_strategy = st.builds(
    notation::Icon,
    iconType=
        safe_text
)
notation::Label_strategy = st.builds(
    notation::Label,
)
notation::Composite_strategy = st.builds(
    notation::Composite,
    layout=
        safe_text
)
notation::Image_strategy = st.builds(
    notation::Image,
    path=
        safe_text
)
notation::SyntaxOf_strategy = st.builds(
    notation::SyntaxOf,
)
notation::BorderStyle_strategy = st.builds(
    notation::BorderStyle,
    color=
        safe_text,
    texture=
        safe_text,
    thickness=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
notation::FigureStyle_strategy = st.builds(
    notation::FigureStyle,
    fillTexture=
        safe_text,
    fillTextureColor=
        safe_text,
    orientation=
        safe_text,
    fillOrientation=
        safe_text,
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fillColor=
        safe_text,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    brightness=
        st.integers()
)
notation::Figure_strategy = st.builds(
    notation::Figure,
)
notation::LineStyle_strategy = st.builds(
    notation::LineStyle,
    length=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    color=
        safe_text,
    texture=
        safe_text,
    brightness=
        st.integers(),
    thickness=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    orientation=
        safe_text
)
notation::Line_strategy = st.builds(
    notation::Line,
)
DiagramElement_strategy = st.builds(
    DiagramElement,
)
notation::Node_strategy = st.builds(
    notation::Node,
)
IDElement_strategy = st.builds(
    IDElement,
)
notation::GraphicalElement_strategy = st.builds(
    notation::GraphicalElement,
)
notation::TextualElement_strategy = st.builds(
    notation::TextualElement,
)
notation::IDElement_strategy = st.builds(
    notation::IDElement,
    ID=
        safe_text
)
notation::DiagramElement_strategy = st.builds(
    notation::DiagramElement,
)
notation::DiagramDefinition_strategy = st.builds(
    notation::DiagramDefinition,
    Legend=
        safe_text,
    allowChunks=
        st.booleans(),
    targetedAudience=
        safe_text,
    Level=
        st.integers()
)
Relation_strategy = st.builds(
    Relation,
)
notation::Link_strategy = st.builds(
    notation::Link,
)
notation::Compartment_strategy = st.builds(
    notation::Compartment,
    layout=
        safe_text
)
notation::Relation_strategy = st.builds(
    notation::Relation,
)
notation::NotationDefinition_strategy = st.builds(
    notation::NotationDefinition,
    Type=
        safe_text
)

@given(instance=notation::Point_strategy)
@settings(max_examples=50)
def test_notation::point_instantiation(instance):
    assert isinstance(instance, notation::Point)

@given(instance=notation::Point_strategy)
def test_notation::point_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::Point_strategy)
def test_notation::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=notation::Point_strategy)
def test_notation::point_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::Point_strategy)
def test_notation::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=notation::Cube_strategy)
@settings(max_examples=50)
def test_notation::cube_instantiation(instance):
    assert isinstance(instance, notation::Cube)

@given(instance=notation::Polyline_strategy)
@settings(max_examples=50)
def test_notation::polyline_instantiation(instance):
    assert isinstance(instance, notation::Polyline)

@given(instance=notation::Triangle_strategy)
@settings(max_examples=50)
def test_notation::triangle_instantiation(instance):
    assert isinstance(instance, notation::Triangle)

@given(instance=notation::Diamond_strategy)
@settings(max_examples=50)
def test_notation::diamond_instantiation(instance):
    assert isinstance(instance, notation::Diamond)

@given(instance=notation::Cylinder_strategy)
@settings(max_examples=50)
def test_notation::cylinder_instantiation(instance):
    assert isinstance(instance, notation::Cylinder)

@given(instance=notation::Roundtangle_strategy)
@settings(max_examples=50)
def test_notation::roundtangle_instantiation(instance):
    assert isinstance(instance, notation::Roundtangle)

@given(instance=notation::Circle_strategy)
@settings(max_examples=50)
def test_notation::circle_instantiation(instance):
    assert isinstance(instance, notation::Circle)

@given(instance=notation::Square_strategy)
@settings(max_examples=50)
def test_notation::square_instantiation(instance):
    assert isinstance(instance, notation::Square)

@given(instance=notation::Rectangle_strategy)
@settings(max_examples=50)
def test_notation::rectangle_instantiation(instance):
    assert isinstance(instance, notation::Rectangle)

@given(instance=Style_strategy)
@settings(max_examples=50)
def test_style_instantiation(instance):
    assert isinstance(instance, Style)

@given(instance=notation::Style_strategy)
@settings(max_examples=50)
def test_notation::style_instantiation(instance):
    assert isinstance(instance, notation::Style)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=notation::ReferenceValue_strategy)
@settings(max_examples=50)
def test_notation::referencevalue_instantiation(instance):
    assert isinstance(instance, notation::ReferenceValue)

@given(instance=notation::AttributeValue_strategy)
@settings(max_examples=50)
def test_notation::attributevalue_instantiation(instance):
    assert isinstance(instance, notation::AttributeValue)

@given(instance=TextualElement_strategy)
@settings(max_examples=50)
def test_textualelement_instantiation(instance):
    assert isinstance(instance, TextualElement)

@given(instance=notation::Value_strategy)
@settings(max_examples=50)
def test_notation::value_instantiation(instance):
    assert isinstance(instance, notation::Value)

@given(instance=notation::Keyword_strategy)
@settings(max_examples=50)
def test_notation::keyword_instantiation(instance):
    assert isinstance(instance, notation::Keyword)

@given(instance=notation::Token_strategy)
@settings(max_examples=50)
def test_notation::token_instantiation(instance):
    assert isinstance(instance, notation::Token)

@given(instance=notation::TextualContainment_strategy)
@settings(max_examples=50)
def test_notation::textualcontainment_instantiation(instance):
    assert isinstance(instance, notation::TextualContainment)

@given(instance=notation::TextualContainment_strategy)
def test_notation::textualcontainment_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=notation::TextualContainment_strategy)
def test_notation::textualcontainment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation::TextStyle_strategy)
@settings(max_examples=50)
def test_notation::textstyle_instantiation(instance):
    assert isinstance(instance, notation::TextStyle)

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_italic_type(instance):
    assert isinstance(instance.italic, bool)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_italic_setter(instance):
    original = instance.italic
    instance.italic = original
    assert instance.italic == original

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_bold_type(instance):
    assert isinstance(instance.bold, bool)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_bold_setter(instance):
    original = instance.bold
    instance.bold = original
    assert instance.bold == original

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontColor_type(instance):
    assert isinstance(instance.fontColor, str)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_underlined_type(instance):
    assert isinstance(instance.underlined, bool)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_underlined_setter(instance):
    original = instance.underlined
    instance.underlined = original
    assert instance.underlined == original

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontSize_type(instance):
    assert isinstance(instance.fontSize, int)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original

@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=notation::TextStyle_strategy)
def test_notation::textstyle_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=notation::IconStyle_strategy)
@settings(max_examples=50)
def test_notation::iconstyle_instantiation(instance):
    assert isinstance(instance, notation::IconStyle)

@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_brightness_type(instance):
    assert isinstance(instance.brightness, int)


@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=notation::IconStyle_strategy)
def test_notation::iconstyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=notation::FigureContainment_strategy)
@settings(max_examples=50)
def test_notation::figurecontainment_instantiation(instance):
    assert isinstance(instance, notation::FigureContainment)

@given(instance=notation::FigureContainment_strategy)
def test_notation::figurecontainment_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=notation::FigureContainment_strategy)
def test_notation::figurecontainment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=GraphicalElement_strategy)
@settings(max_examples=50)
def test_graphicalelement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)

@given(instance=notation::Icon_strategy)
@settings(max_examples=50)
def test_notation::icon_instantiation(instance):
    assert isinstance(instance, notation::Icon)

@given(instance=notation::Icon_strategy)
def test_notation::icon_iconType_type(instance):
    assert isinstance(instance.iconType, str)


@given(instance=notation::Icon_strategy)
def test_notation::icon_iconType_setter(instance):
    original = instance.iconType
    instance.iconType = original
    assert instance.iconType == original

@given(instance=notation::Label_strategy)
@settings(max_examples=50)
def test_notation::label_instantiation(instance):
    assert isinstance(instance, notation::Label)

@given(instance=notation::Composite_strategy)
@settings(max_examples=50)
def test_notation::composite_instantiation(instance):
    assert isinstance(instance, notation::Composite)

@given(instance=notation::Composite_strategy)
def test_notation::composite_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=notation::Composite_strategy)
def test_notation::composite_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation::Image_strategy)
@settings(max_examples=50)
def test_notation::image_instantiation(instance):
    assert isinstance(instance, notation::Image)

@given(instance=notation::Image_strategy)
def test_notation::image_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=notation::Image_strategy)
def test_notation::image_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=notation::SyntaxOf_strategy)
@settings(max_examples=50)
def test_notation::syntaxof_instantiation(instance):
    assert isinstance(instance, notation::SyntaxOf)

@given(instance=notation::BorderStyle_strategy)
@settings(max_examples=50)
def test_notation::borderstyle_instantiation(instance):
    assert isinstance(instance, notation::BorderStyle)

@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_texture_type(instance):
    assert isinstance(instance.texture, str)


@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original

@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_thickness_type(instance):
    assert isinstance(instance.thickness, float)


@given(instance=notation::BorderStyle_strategy)
def test_notation::borderstyle_thickness_setter(instance):
    original = instance.thickness
    instance.thickness = original
    assert instance.thickness == original

@given(instance=notation::FigureStyle_strategy)
@settings(max_examples=50)
def test_notation::figurestyle_instantiation(instance):
    assert isinstance(instance, notation::FigureStyle)

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillTexture_type(instance):
    assert isinstance(instance.fillTexture, str)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillTexture_setter(instance):
    original = instance.fillTexture
    instance.fillTexture = original
    assert instance.fillTexture == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillTextureColor_type(instance):
    assert isinstance(instance.fillTextureColor, str)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillTextureColor_setter(instance):
    original = instance.fillTextureColor
    instance.fillTextureColor = original
    assert instance.fillTextureColor == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillOrientation_type(instance):
    assert isinstance(instance.fillOrientation, str)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillOrientation_setter(instance):
    original = instance.fillOrientation
    instance.fillOrientation = original
    assert instance.fillOrientation == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillColor_type(instance):
    assert isinstance(instance.fillColor, str)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_brightness_type(instance):
    assert isinstance(instance.brightness, int)


@given(instance=notation::FigureStyle_strategy)
def test_notation::figurestyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=notation::Figure_strategy)
@settings(max_examples=50)
def test_notation::figure_instantiation(instance):
    assert isinstance(instance, notation::Figure)

@given(instance=notation::LineStyle_strategy)
@settings(max_examples=50)
def test_notation::linestyle_instantiation(instance):
    assert isinstance(instance, notation::LineStyle)

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_length_type(instance):
    assert isinstance(instance.length, float)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_texture_type(instance):
    assert isinstance(instance.texture, str)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_texture_setter(instance):
    original = instance.texture
    instance.texture = original
    assert instance.texture == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_brightness_type(instance):
    assert isinstance(instance.brightness, int)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_brightness_setter(instance):
    original = instance.brightness
    instance.brightness = original
    assert instance.brightness == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_thickness_type(instance):
    assert isinstance(instance.thickness, float)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_thickness_setter(instance):
    original = instance.thickness
    instance.thickness = original
    assert instance.thickness == original

@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_orientation_type(instance):
    assert isinstance(instance.orientation, str)


@given(instance=notation::LineStyle_strategy)
def test_notation::linestyle_orientation_setter(instance):
    original = instance.orientation
    instance.orientation = original
    assert instance.orientation == original

@given(instance=notation::Line_strategy)
@settings(max_examples=50)
def test_notation::line_instantiation(instance):
    assert isinstance(instance, notation::Line)

@given(instance=DiagramElement_strategy)
@settings(max_examples=50)
def test_diagramelement_instantiation(instance):
    assert isinstance(instance, DiagramElement)

@given(instance=notation::Node_strategy)
@settings(max_examples=50)
def test_notation::node_instantiation(instance):
    assert isinstance(instance, notation::Node)

@given(instance=IDElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IDElement)

@given(instance=notation::GraphicalElement_strategy)
@settings(max_examples=50)
def test_notation::graphicalelement_instantiation(instance):
    assert isinstance(instance, notation::GraphicalElement)

@given(instance=notation::TextualElement_strategy)
@settings(max_examples=50)
def test_notation::textualelement_instantiation(instance):
    assert isinstance(instance, notation::TextualElement)

@given(instance=notation::IDElement_strategy)
@settings(max_examples=50)
def test_notation::idelement_instantiation(instance):
    assert isinstance(instance, notation::IDElement)

@given(instance=notation::IDElement_strategy)
def test_notation::idelement_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=notation::IDElement_strategy)
def test_notation::idelement_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=notation::DiagramElement_strategy)
@settings(max_examples=50)
def test_notation::diagramelement_instantiation(instance):
    assert isinstance(instance, notation::DiagramElement)

@given(instance=notation::DiagramDefinition_strategy)
@settings(max_examples=50)
def test_notation::diagramdefinition_instantiation(instance):
    assert isinstance(instance, notation::DiagramDefinition)

@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_Legend_type(instance):
    assert isinstance(instance.Legend, str)


@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_Legend_setter(instance):
    original = instance.Legend
    instance.Legend = original
    assert instance.Legend == original

@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_allowChunks_type(instance):
    assert isinstance(instance.allowChunks, bool)


@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_allowChunks_setter(instance):
    original = instance.allowChunks
    instance.allowChunks = original
    assert instance.allowChunks == original

@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_targetedAudience_type(instance):
    assert isinstance(instance.targetedAudience, str)


@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_targetedAudience_setter(instance):
    original = instance.targetedAudience
    instance.targetedAudience = original
    assert instance.targetedAudience == original

@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_Level_type(instance):
    assert isinstance(instance.Level, int)


@given(instance=notation::DiagramDefinition_strategy)
def test_notation::diagramdefinition_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=notation::Link_strategy)
@settings(max_examples=50)
def test_notation::link_instantiation(instance):
    assert isinstance(instance, notation::Link)

@given(instance=notation::Compartment_strategy)
@settings(max_examples=50)
def test_notation::compartment_instantiation(instance):
    assert isinstance(instance, notation::Compartment)

@given(instance=notation::Compartment_strategy)
def test_notation::compartment_layout_type(instance):
    assert isinstance(instance.layout, str)


@given(instance=notation::Compartment_strategy)
def test_notation::compartment_layout_setter(instance):
    original = instance.layout
    instance.layout = original
    assert instance.layout == original

@given(instance=notation::Relation_strategy)
@settings(max_examples=50)
def test_notation::relation_instantiation(instance):
    assert isinstance(instance, notation::Relation)

@given(instance=notation::NotationDefinition_strategy)
@settings(max_examples=50)
def test_notation::notationdefinition_instantiation(instance):
    assert isinstance(instance, notation::NotationDefinition)

@given(instance=notation::NotationDefinition_strategy)
def test_notation::notationdefinition_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=notation::NotationDefinition_strategy)
def test_notation::notationdefinition_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original
