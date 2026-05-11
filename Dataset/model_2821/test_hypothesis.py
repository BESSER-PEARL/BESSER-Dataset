import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Rectangle,
    sofiagraphics::RoundedRectangle,
    Widget,
    sofiagraphics::Polyline,
    sofiagraphics::Ellipse,
    sofiagraphics::Text,
    sofiagraphics::Rectangle,
    sofiagraphics::Gesture,
    sofiagraphics::Color,
    sofiagraphics::Scene,
    sofiagraphics::Style,
    sofiagraphics::Widget,
    sofiagraphics::Dimension,
    sofiagraphics::Point,
    Alignment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rectangle_is_not_abstract():
    assert not inspect.isabstract(Rectangle)


def test_rectangle_constructor_exists():
    assert callable(Rectangle.__init__)


def test_rectangle_constructor_args():
    sig = inspect.signature(Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::roundedrectangle_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::RoundedRectangle)


def test_sofiagraphics::roundedrectangle_constructor_exists():
    assert callable(sofiagraphics::RoundedRectangle.__init__)


def test_sofiagraphics::roundedrectangle_constructor_args():
    sig = inspect.signature(sofiagraphics::RoundedRectangle.__init__)
    params = list(sig.parameters.keys())



def test_widget_is_not_abstract():
    assert not inspect.isabstract(Widget)


def test_widget_constructor_exists():
    assert callable(Widget.__init__)


def test_widget_constructor_args():
    sig = inspect.signature(Widget.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::polyline_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Polyline)


def test_sofiagraphics::polyline_constructor_exists():
    assert callable(sofiagraphics::Polyline.__init__)


def test_sofiagraphics::polyline_constructor_args():
    sig = inspect.signature(sofiagraphics::Polyline.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::ellipse_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Ellipse)


def test_sofiagraphics::ellipse_constructor_exists():
    assert callable(sofiagraphics::Ellipse.__init__)


def test_sofiagraphics::ellipse_constructor_args():
    sig = inspect.signature(sofiagraphics::Ellipse.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::text_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Text)


def test_sofiagraphics::text_constructor_exists():
    assert callable(sofiagraphics::Text.__init__)


def test_sofiagraphics::text_constructor_args():
    sig = inspect.signature(sofiagraphics::Text.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "halign" in params, "Missing parameter 'halign'"
    assert "attributeName" in params, "Missing parameter 'attributeName'"
    assert "valign" in params, "Missing parameter 'valign'"

def test_sofiagraphics::text_has_text():
    assert hasattr(sofiagraphics::Text, "text")
    descriptor = None
    for klass in sofiagraphics::Text.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::text_has_halign():
    assert hasattr(sofiagraphics::Text, "halign")
    descriptor = None
    for klass in sofiagraphics::Text.__mro__:
        if "halign" in klass.__dict__:
            descriptor = klass.__dict__["halign"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::text_has_attributeName():
    assert hasattr(sofiagraphics::Text, "attributeName")
    descriptor = None
    for klass in sofiagraphics::Text.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::text_has_valign():
    assert hasattr(sofiagraphics::Text, "valign")
    descriptor = None
    for klass in sofiagraphics::Text.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)



def test_sofiagraphics::rectangle_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Rectangle)


def test_sofiagraphics::rectangle_constructor_exists():
    assert callable(sofiagraphics::Rectangle.__init__)


def test_sofiagraphics::rectangle_constructor_args():
    sig = inspect.signature(sofiagraphics::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::gesture_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Gesture)


def test_sofiagraphics::gesture_constructor_exists():
    assert callable(sofiagraphics::Gesture.__init__)


def test_sofiagraphics::gesture_constructor_args():
    sig = inspect.signature(sofiagraphics::Gesture.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::color_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Color)


def test_sofiagraphics::color_constructor_exists():
    assert callable(sofiagraphics::Color.__init__)


def test_sofiagraphics::color_constructor_args():
    sig = inspect.signature(sofiagraphics::Color.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"
    assert "r" in params, "Missing parameter 'r'"
    assert "g" in params, "Missing parameter 'g'"

def test_sofiagraphics::color_has_a():
    assert hasattr(sofiagraphics::Color, "a")
    descriptor = None
    for klass in sofiagraphics::Color.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::color_has_b():
    assert hasattr(sofiagraphics::Color, "b")
    descriptor = None
    for klass in sofiagraphics::Color.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::color_has_r():
    assert hasattr(sofiagraphics::Color, "r")
    descriptor = None
    for klass in sofiagraphics::Color.__mro__:
        if "r" in klass.__dict__:
            descriptor = klass.__dict__["r"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::color_has_g():
    assert hasattr(sofiagraphics::Color, "g")
    descriptor = None
    for klass in sofiagraphics::Color.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)



def test_sofiagraphics::scene_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Scene)


def test_sofiagraphics::scene_constructor_exists():
    assert callable(sofiagraphics::Scene.__init__)


def test_sofiagraphics::scene_constructor_args():
    sig = inspect.signature(sofiagraphics::Scene.__init__)
    params = list(sig.parameters.keys())



def test_sofiagraphics::style_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Style)


def test_sofiagraphics::style_constructor_exists():
    assert callable(sofiagraphics::Style.__init__)


def test_sofiagraphics::style_constructor_args():
    sig = inspect.signature(sofiagraphics::Style.__init__)
    params = list(sig.parameters.keys())
    assert "filled" in params, "Missing parameter 'filled'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"

def test_sofiagraphics::style_has_filled():
    assert hasattr(sofiagraphics::Style, "filled")
    descriptor = None
    for klass in sofiagraphics::Style.__mro__:
        if "filled" in klass.__dict__:
            descriptor = klass.__dict__["filled"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::style_has_lineWidth():
    assert hasattr(sofiagraphics::Style, "lineWidth")
    descriptor = None
    for klass in sofiagraphics::Style.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)



def test_sofiagraphics::widget_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Widget)


def test_sofiagraphics::widget_constructor_exists():
    assert callable(sofiagraphics::Widget.__init__)


def test_sofiagraphics::widget_constructor_args():
    sig = inspect.signature(sofiagraphics::Widget.__init__)
    params = list(sig.parameters.keys())
    assert "gestureOnly" in params, "Missing parameter 'gestureOnly'"
    assert "portYPosition" in params, "Missing parameter 'portYPosition'"

def test_sofiagraphics::widget_has_gestureOnly():
    assert hasattr(sofiagraphics::Widget, "gestureOnly")
    descriptor = None
    for klass in sofiagraphics::Widget.__mro__:
        if "gestureOnly" in klass.__dict__:
            descriptor = klass.__dict__["gestureOnly"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::widget_has_portYPosition():
    assert hasattr(sofiagraphics::Widget, "portYPosition")
    descriptor = None
    for klass in sofiagraphics::Widget.__mro__:
        if "portYPosition" in klass.__dict__:
            descriptor = klass.__dict__["portYPosition"]
            break
    assert isinstance(descriptor, property)



def test_sofiagraphics::dimension_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Dimension)


def test_sofiagraphics::dimension_constructor_exists():
    assert callable(sofiagraphics::Dimension.__init__)


def test_sofiagraphics::dimension_constructor_args():
    sig = inspect.signature(sofiagraphics::Dimension.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "hrelative" in params, "Missing parameter 'hrelative'"
    assert "noresize" in params, "Missing parameter 'noresize'"
    assert "wrelative" in params, "Missing parameter 'wrelative'"
    assert "width" in params, "Missing parameter 'width'"

def test_sofiagraphics::dimension_has_height():
    assert hasattr(sofiagraphics::Dimension, "height")
    descriptor = None
    for klass in sofiagraphics::Dimension.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::dimension_has_hrelative():
    assert hasattr(sofiagraphics::Dimension, "hrelative")
    descriptor = None
    for klass in sofiagraphics::Dimension.__mro__:
        if "hrelative" in klass.__dict__:
            descriptor = klass.__dict__["hrelative"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::dimension_has_noresize():
    assert hasattr(sofiagraphics::Dimension, "noresize")
    descriptor = None
    for klass in sofiagraphics::Dimension.__mro__:
        if "noresize" in klass.__dict__:
            descriptor = klass.__dict__["noresize"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::dimension_has_wrelative():
    assert hasattr(sofiagraphics::Dimension, "wrelative")
    descriptor = None
    for klass in sofiagraphics::Dimension.__mro__:
        if "wrelative" in klass.__dict__:
            descriptor = klass.__dict__["wrelative"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::dimension_has_width():
    assert hasattr(sofiagraphics::Dimension, "width")
    descriptor = None
    for klass in sofiagraphics::Dimension.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_sofiagraphics::point_is_not_abstract():
    assert not inspect.isabstract(sofiagraphics::Point)


def test_sofiagraphics::point_constructor_exists():
    assert callable(sofiagraphics::Point.__init__)


def test_sofiagraphics::point_constructor_args():
    sig = inspect.signature(sofiagraphics::Point.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "yrelative" in params, "Missing parameter 'yrelative'"
    assert "xrelative" in params, "Missing parameter 'xrelative'"
    assert "y" in params, "Missing parameter 'y'"

def test_sofiagraphics::point_has_x():
    assert hasattr(sofiagraphics::Point, "x")
    descriptor = None
    for klass in sofiagraphics::Point.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::point_has_yrelative():
    assert hasattr(sofiagraphics::Point, "yrelative")
    descriptor = None
    for klass in sofiagraphics::Point.__mro__:
        if "yrelative" in klass.__dict__:
            descriptor = klass.__dict__["yrelative"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::point_has_xrelative():
    assert hasattr(sofiagraphics::Point, "xrelative")
    descriptor = None
    for klass in sofiagraphics::Point.__mro__:
        if "xrelative" in klass.__dict__:
            descriptor = klass.__dict__["xrelative"]
            break
    assert isinstance(descriptor, property)

def test_sofiagraphics::point_has_y():
    assert hasattr(sofiagraphics::Point, "y")
    descriptor = None
    for klass in sofiagraphics::Point.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_alignment_exists():
    # Check that the Enumeration exists
    assert Alignment is not None

def test_alignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Alignment]
    expected_literals = [
        "CENTER",
        "UNSPECIFIED",
        "RIGHT",
        "TOP",
        "LEFT",
        "MIDDLE",
        "BOTTOM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Alignment"


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
Rectangle_strategy = st.builds(
    Rectangle,
)
sofiagraphics::RoundedRectangle_strategy = st.builds(
    sofiagraphics::RoundedRectangle,
)
Widget_strategy = st.builds(
    Widget,
)
sofiagraphics::Polyline_strategy = st.builds(
    sofiagraphics::Polyline,
)
sofiagraphics::Ellipse_strategy = st.builds(
    sofiagraphics::Ellipse,
)
sofiagraphics::Text_strategy = st.builds(
    sofiagraphics::Text,
    text=
        safe_text,
    halign=
        safe_text,
    attributeName=
        safe_text,
    valign=
        safe_text
)
sofiagraphics::Rectangle_strategy = st.builds(
    sofiagraphics::Rectangle,
)
sofiagraphics::Gesture_strategy = st.builds(
    sofiagraphics::Gesture,
)
sofiagraphics::Color_strategy = st.builds(
    sofiagraphics::Color,
    a=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    b=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    r=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    g=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sofiagraphics::Scene_strategy = st.builds(
    sofiagraphics::Scene,
)
sofiagraphics::Style_strategy = st.builds(
    sofiagraphics::Style,
    filled=
        st.booleans(),
    lineWidth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sofiagraphics::Widget_strategy = st.builds(
    sofiagraphics::Widget,
    gestureOnly=
        st.booleans(),
    portYPosition=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sofiagraphics::Dimension_strategy = st.builds(
    sofiagraphics::Dimension,
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    hrelative=
        st.booleans(),
    noresize=
        st.booleans(),
    wrelative=
        st.booleans(),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
sofiagraphics::Point_strategy = st.builds(
    sofiagraphics::Point,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    yrelative=
        st.booleans(),
    xrelative=
        st.booleans(),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Rectangle_strategy)
@settings(max_examples=50)
def test_rectangle_instantiation(instance):
    assert isinstance(instance, Rectangle)

@given(instance=sofiagraphics::RoundedRectangle_strategy)
@settings(max_examples=50)
def test_sofiagraphics::roundedrectangle_instantiation(instance):
    assert isinstance(instance, sofiagraphics::RoundedRectangle)

@given(instance=Widget_strategy)
@settings(max_examples=50)
def test_widget_instantiation(instance):
    assert isinstance(instance, Widget)

@given(instance=sofiagraphics::Polyline_strategy)
@settings(max_examples=50)
def test_sofiagraphics::polyline_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Polyline)

@given(instance=sofiagraphics::Ellipse_strategy)
@settings(max_examples=50)
def test_sofiagraphics::ellipse_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Ellipse)

@given(instance=sofiagraphics::Text_strategy)
@settings(max_examples=50)
def test_sofiagraphics::text_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Text)

@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_halign_type(instance):
    assert isinstance(instance.halign, str)


@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_halign_setter(instance):
    original = instance.halign
    instance.halign = original
    assert instance.halign == original

@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=sofiagraphics::Text_strategy)
def test_sofiagraphics::text_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=sofiagraphics::Rectangle_strategy)
@settings(max_examples=50)
def test_sofiagraphics::rectangle_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Rectangle)

@given(instance=sofiagraphics::Gesture_strategy)
@settings(max_examples=50)
def test_sofiagraphics::gesture_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Gesture)

@given(instance=sofiagraphics::Color_strategy)
@settings(max_examples=50)
def test_sofiagraphics::color_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Color)

@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_a_type(instance):
    assert isinstance(instance.a, float)


@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_b_type(instance):
    assert isinstance(instance.b, float)


@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_r_type(instance):
    assert isinstance(instance.r, float)


@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_r_setter(instance):
    original = instance.r
    instance.r = original
    assert instance.r == original

@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_g_type(instance):
    assert isinstance(instance.g, float)


@given(instance=sofiagraphics::Color_strategy)
def test_sofiagraphics::color_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original

@given(instance=sofiagraphics::Scene_strategy)
@settings(max_examples=50)
def test_sofiagraphics::scene_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Scene)

@given(instance=sofiagraphics::Style_strategy)
@settings(max_examples=50)
def test_sofiagraphics::style_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Style)

@given(instance=sofiagraphics::Style_strategy)
def test_sofiagraphics::style_filled_type(instance):
    assert isinstance(instance.filled, bool)


@given(instance=sofiagraphics::Style_strategy)
def test_sofiagraphics::style_filled_setter(instance):
    original = instance.filled
    instance.filled = original
    assert instance.filled == original

@given(instance=sofiagraphics::Style_strategy)
def test_sofiagraphics::style_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, float)


@given(instance=sofiagraphics::Style_strategy)
def test_sofiagraphics::style_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=sofiagraphics::Widget_strategy)
@settings(max_examples=50)
def test_sofiagraphics::widget_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Widget)

@given(instance=sofiagraphics::Widget_strategy)
def test_sofiagraphics::widget_gestureOnly_type(instance):
    assert isinstance(instance.gestureOnly, bool)


@given(instance=sofiagraphics::Widget_strategy)
def test_sofiagraphics::widget_gestureOnly_setter(instance):
    original = instance.gestureOnly
    instance.gestureOnly = original
    assert instance.gestureOnly == original

@given(instance=sofiagraphics::Widget_strategy)
def test_sofiagraphics::widget_portYPosition_type(instance):
    assert isinstance(instance.portYPosition, float)


@given(instance=sofiagraphics::Widget_strategy)
def test_sofiagraphics::widget_portYPosition_setter(instance):
    original = instance.portYPosition
    instance.portYPosition = original
    assert instance.portYPosition == original

@given(instance=sofiagraphics::Dimension_strategy)
@settings(max_examples=50)
def test_sofiagraphics::dimension_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Dimension)

@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_height_type(instance):
    assert isinstance(instance.height, float)


@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_hrelative_type(instance):
    assert isinstance(instance.hrelative, bool)


@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_hrelative_setter(instance):
    original = instance.hrelative
    instance.hrelative = original
    assert instance.hrelative == original

@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_noresize_type(instance):
    assert isinstance(instance.noresize, bool)


@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_noresize_setter(instance):
    original = instance.noresize
    instance.noresize = original
    assert instance.noresize == original

@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_wrelative_type(instance):
    assert isinstance(instance.wrelative, bool)


@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_wrelative_setter(instance):
    original = instance.wrelative
    instance.wrelative = original
    assert instance.wrelative == original

@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_width_type(instance):
    assert isinstance(instance.width, float)


@given(instance=sofiagraphics::Dimension_strategy)
def test_sofiagraphics::dimension_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=sofiagraphics::Point_strategy)
@settings(max_examples=50)
def test_sofiagraphics::point_instantiation(instance):
    assert isinstance(instance, sofiagraphics::Point)

@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_x_type(instance):
    assert isinstance(instance.x, float)


@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_yrelative_type(instance):
    assert isinstance(instance.yrelative, bool)


@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_yrelative_setter(instance):
    original = instance.yrelative
    instance.yrelative = original
    assert instance.yrelative == original

@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_xrelative_type(instance):
    assert isinstance(instance.xrelative, bool)


@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_xrelative_setter(instance):
    original = instance.xrelative
    instance.xrelative = original
    assert instance.xrelative == original

@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_y_type(instance):
    assert isinstance(instance.y, float)


@given(instance=sofiagraphics::Point_strategy)
def test_sofiagraphics::point_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original
