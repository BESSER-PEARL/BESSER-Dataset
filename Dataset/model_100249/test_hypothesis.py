import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Color,
    styles::ColorConstantRef,
    styles::RGBColor,
    ColorWithTransparency,
    ColorOrGradient,
    styles::GradientRef,
    styles::Transparent,
    styles::Color,
    styles::ColorWithTransparency,
    styles::GradientColorArea,
    styles::GradientLayout,
    styles::StyleLayout,
    styles::JvmTypeReference,
    StyleContainerElement,
    styles::Gradient,
    styles::HighlightingValues,
    styles::ColorOrGradient,
    styles::StyleContainerElement,
    styles::StyleContainer,
    styles::Style,
    GradientAllignment,
    LineStyle,
    YesNoBool,
    ColorConstants,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_styles::colorconstantref_is_not_abstract():
    assert not inspect.isabstract(styles::ColorConstantRef)


def test_styles::colorconstantref_constructor_exists():
    assert callable(styles::ColorConstantRef.__init__)


def test_styles::colorconstantref_constructor_args():
    sig = inspect.signature(styles::ColorConstantRef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_styles::colorconstantref_has_value():
    assert hasattr(styles::ColorConstantRef, "value")
    descriptor = None
    for klass in styles::ColorConstantRef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_styles::rgbcolor_is_not_abstract():
    assert not inspect.isabstract(styles::RGBColor)


def test_styles::rgbcolor_constructor_exists():
    assert callable(styles::RGBColor.__init__)


def test_styles::rgbcolor_constructor_args():
    sig = inspect.signature(styles::RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "red" in params, "Missing parameter 'red'"
    assert "green" in params, "Missing parameter 'green'"
    assert "blue" in params, "Missing parameter 'blue'"

def test_styles::rgbcolor_has_red():
    assert hasattr(styles::RGBColor, "red")
    descriptor = None
    for klass in styles::RGBColor.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)

def test_styles::rgbcolor_has_green():
    assert hasattr(styles::RGBColor, "green")
    descriptor = None
    for klass in styles::RGBColor.__mro__:
        if "green" in klass.__dict__:
            descriptor = klass.__dict__["green"]
            break
    assert isinstance(descriptor, property)

def test_styles::rgbcolor_has_blue():
    assert hasattr(styles::RGBColor, "blue")
    descriptor = None
    for klass in styles::RGBColor.__mro__:
        if "blue" in klass.__dict__:
            descriptor = klass.__dict__["blue"]
            break
    assert isinstance(descriptor, property)



def test_colorwithtransparency_is_not_abstract():
    assert not inspect.isabstract(ColorWithTransparency)


def test_colorwithtransparency_constructor_exists():
    assert callable(ColorWithTransparency.__init__)


def test_colorwithtransparency_constructor_args():
    sig = inspect.signature(ColorWithTransparency.__init__)
    params = list(sig.parameters.keys())



def test_colororgradient_is_not_abstract():
    assert not inspect.isabstract(ColorOrGradient)


def test_colororgradient_constructor_exists():
    assert callable(ColorOrGradient.__init__)


def test_colororgradient_constructor_args():
    sig = inspect.signature(ColorOrGradient.__init__)
    params = list(sig.parameters.keys())



def test_styles::gradientref_is_not_abstract():
    assert not inspect.isabstract(styles::GradientRef)


def test_styles::gradientref_constructor_exists():
    assert callable(styles::GradientRef.__init__)


def test_styles::gradientref_constructor_args():
    sig = inspect.signature(styles::GradientRef.__init__)
    params = list(sig.parameters.keys())



def test_styles::transparent_is_not_abstract():
    assert not inspect.isabstract(styles::Transparent)


def test_styles::transparent_constructor_exists():
    assert callable(styles::Transparent.__init__)


def test_styles::transparent_constructor_args():
    sig = inspect.signature(styles::Transparent.__init__)
    params = list(sig.parameters.keys())
    assert "transparent" in params, "Missing parameter 'transparent'"

def test_styles::transparent_has_transparent():
    assert hasattr(styles::Transparent, "transparent")
    descriptor = None
    for klass in styles::Transparent.__mro__:
        if "transparent" in klass.__dict__:
            descriptor = klass.__dict__["transparent"]
            break
    assert isinstance(descriptor, property)



def test_styles::color_is_not_abstract():
    assert not inspect.isabstract(styles::Color)


def test_styles::color_constructor_exists():
    assert callable(styles::Color.__init__)


def test_styles::color_constructor_args():
    sig = inspect.signature(styles::Color.__init__)
    params = list(sig.parameters.keys())



def test_styles::colorwithtransparency_is_not_abstract():
    assert not inspect.isabstract(styles::ColorWithTransparency)


def test_styles::colorwithtransparency_constructor_exists():
    assert callable(styles::ColorWithTransparency.__init__)


def test_styles::colorwithtransparency_constructor_args():
    sig = inspect.signature(styles::ColorWithTransparency.__init__)
    params = list(sig.parameters.keys())



def test_styles::gradientcolorarea_is_not_abstract():
    assert not inspect.isabstract(styles::GradientColorArea)


def test_styles::gradientcolorarea_constructor_exists():
    assert callable(styles::GradientColorArea.__init__)


def test_styles::gradientcolorarea_constructor_args():
    sig = inspect.signature(styles::GradientColorArea.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"

def test_styles::gradientcolorarea_has_offset():
    assert hasattr(styles::GradientColorArea, "offset")
    descriptor = None
    for klass in styles::GradientColorArea.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_styles::gradientlayout_is_not_abstract():
    assert not inspect.isabstract(styles::GradientLayout)


def test_styles::gradientlayout_constructor_exists():
    assert callable(styles::GradientLayout.__init__)


def test_styles::gradientlayout_constructor_args():
    sig = inspect.signature(styles::GradientLayout.__init__)
    params = list(sig.parameters.keys())



def test_styles::stylelayout_is_not_abstract():
    assert not inspect.isabstract(styles::StyleLayout)


def test_styles::stylelayout_constructor_exists():
    assert callable(styles::StyleLayout.__init__)


def test_styles::stylelayout_constructor_args():
    sig = inspect.signature(styles::StyleLayout.__init__)
    params = list(sig.parameters.keys())
    assert "fontBold" in params, "Missing parameter 'fontBold'"
    assert "fontItalic" in params, "Missing parameter 'fontItalic'"
    assert "transparency" in params, "Missing parameter 'transparency'"
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "gradient_orientation" in params, "Missing parameter 'gradient_orientation'"
    assert "fontName" in params, "Missing parameter 'fontName'"
    assert "lineStyle" in params, "Missing parameter 'lineStyle'"
    assert "fontSize" in params, "Missing parameter 'fontSize'"

def test_styles::stylelayout_has_fontBold():
    assert hasattr(styles::StyleLayout, "fontBold")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "fontBold" in klass.__dict__:
            descriptor = klass.__dict__["fontBold"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_fontItalic():
    assert hasattr(styles::StyleLayout, "fontItalic")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "fontItalic" in klass.__dict__:
            descriptor = klass.__dict__["fontItalic"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_transparency():
    assert hasattr(styles::StyleLayout, "transparency")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "transparency" in klass.__dict__:
            descriptor = klass.__dict__["transparency"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_lineWidth():
    assert hasattr(styles::StyleLayout, "lineWidth")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "lineWidth" in klass.__dict__:
            descriptor = klass.__dict__["lineWidth"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_gradient_orientation():
    assert hasattr(styles::StyleLayout, "gradient_orientation")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "gradient_orientation" in klass.__dict__:
            descriptor = klass.__dict__["gradient_orientation"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_fontName():
    assert hasattr(styles::StyleLayout, "fontName")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "fontName" in klass.__dict__:
            descriptor = klass.__dict__["fontName"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_lineStyle():
    assert hasattr(styles::StyleLayout, "lineStyle")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "lineStyle" in klass.__dict__:
            descriptor = klass.__dict__["lineStyle"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylelayout_has_fontSize():
    assert hasattr(styles::StyleLayout, "fontSize")
    descriptor = None
    for klass in styles::StyleLayout.__mro__:
        if "fontSize" in klass.__dict__:
            descriptor = klass.__dict__["fontSize"]
            break
    assert isinstance(descriptor, property)



def test_styles::jvmtypereference_is_not_abstract():
    assert not inspect.isabstract(styles::JvmTypeReference)


def test_styles::jvmtypereference_constructor_exists():
    assert callable(styles::JvmTypeReference.__init__)


def test_styles::jvmtypereference_constructor_args():
    sig = inspect.signature(styles::JvmTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_stylecontainerelement_is_not_abstract():
    assert not inspect.isabstract(StyleContainerElement)


def test_stylecontainerelement_constructor_exists():
    assert callable(StyleContainerElement.__init__)


def test_stylecontainerelement_constructor_args():
    sig = inspect.signature(StyleContainerElement.__init__)
    params = list(sig.parameters.keys())



def test_styles::gradient_is_not_abstract():
    assert not inspect.isabstract(styles::Gradient)


def test_styles::gradient_constructor_exists():
    assert callable(styles::Gradient.__init__)


def test_styles::gradient_constructor_args():
    sig = inspect.signature(styles::Gradient.__init__)
    params = list(sig.parameters.keys())



def test_styles::highlightingvalues_is_not_abstract():
    assert not inspect.isabstract(styles::HighlightingValues)


def test_styles::highlightingvalues_constructor_exists():
    assert callable(styles::HighlightingValues.__init__)


def test_styles::highlightingvalues_constructor_args():
    sig = inspect.signature(styles::HighlightingValues.__init__)
    params = list(sig.parameters.keys())



def test_styles::colororgradient_is_not_abstract():
    assert not inspect.isabstract(styles::ColorOrGradient)


def test_styles::colororgradient_constructor_exists():
    assert callable(styles::ColorOrGradient.__init__)


def test_styles::colororgradient_constructor_args():
    sig = inspect.signature(styles::ColorOrGradient.__init__)
    params = list(sig.parameters.keys())



def test_styles::stylecontainerelement_is_not_abstract():
    assert not inspect.isabstract(styles::StyleContainerElement)


def test_styles::stylecontainerelement_constructor_exists():
    assert callable(styles::StyleContainerElement.__init__)


def test_styles::stylecontainerelement_constructor_args():
    sig = inspect.signature(styles::StyleContainerElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_styles::stylecontainerelement_has_name():
    assert hasattr(styles::StyleContainerElement, "name")
    descriptor = None
    for klass in styles::StyleContainerElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_styles::stylecontainerelement_has_description():
    assert hasattr(styles::StyleContainerElement, "description")
    descriptor = None
    for klass in styles::StyleContainerElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_styles::stylecontainer_is_not_abstract():
    assert not inspect.isabstract(styles::StyleContainer)


def test_styles::stylecontainer_constructor_exists():
    assert callable(styles::StyleContainer.__init__)


def test_styles::stylecontainer_constructor_args():
    sig = inspect.signature(styles::StyleContainer.__init__)
    params = list(sig.parameters.keys())



def test_styles::style_is_not_abstract():
    assert not inspect.isabstract(styles::Style)


def test_styles::style_constructor_exists():
    assert callable(styles::Style.__init__)


def test_styles::style_constructor_args():
    sig = inspect.signature(styles::Style.__init__)
    params = list(sig.parameters.keys())

def test_gradientallignment_exists():
    # Check that the Enumeration exists
    assert GradientAllignment is not None

def test_gradientallignment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GradientAllignment]
    expected_literals = [
        "VERTICAL",
        "NULL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GradientAllignment"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DASHDOT",
        "NULL",
        "DOT",
        "DASH",
        "DASHDOTDOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_yesnobool_exists():
    # Check that the Enumeration exists
    assert YesNoBool is not None

def test_yesnobool_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in YesNoBool]
    expected_literals = [
        "NULL",
        "YES",
        "NO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in YesNoBool"

def test_colorconstants_exists():
    # Check that the Enumeration exists
    assert ColorConstants is not None

def test_colorconstants_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorConstants]
    expected_literals = [
        "LIGHT_LIGHT_GRAY",
        "DARK_ORANGE",
        "GRAY",
        "DARK_BLUE",
        "DARK_GRAY",
        "NULL",
        "DARK_GREEN",
        "LIGHT_GREEN",
        "GREEN",
        "YELLOW",
        "BLACK",
        "BLUE",
        "LIGHT_BLUE",
        "CYAN",
        "LIGHT_ORANGE",
        "ORANGE",
        "WHITE",
        "LIGHT_GRAY",
        "RED",
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
Color_strategy = st.builds(
    Color,
)
styles::ColorConstantRef_strategy = st.builds(
    styles::ColorConstantRef,
    value=
        safe_text
)
styles::RGBColor_strategy = st.builds(
    styles::RGBColor,
    red=
        st.integers(),
    green=
        st.integers(),
    blue=
        st.integers()
)
ColorWithTransparency_strategy = st.builds(
    ColorWithTransparency,
)
ColorOrGradient_strategy = st.builds(
    ColorOrGradient,
)
styles::GradientRef_strategy = st.builds(
    styles::GradientRef,
)
styles::Transparent_strategy = st.builds(
    styles::Transparent,
    transparent=
        st.booleans()
)
styles::Color_strategy = st.builds(
    styles::Color,
)
styles::ColorWithTransparency_strategy = st.builds(
    styles::ColorWithTransparency,
)
styles::GradientColorArea_strategy = st.builds(
    styles::GradientColorArea,
    offset=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
styles::GradientLayout_strategy = st.builds(
    styles::GradientLayout,
)
styles::StyleLayout_strategy = st.builds(
    styles::StyleLayout,
    fontBold=
        safe_text,
    fontItalic=
        safe_text,
    transparency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    lineWidth=
        st.integers(),
    gradient_orientation=
        safe_text,
    fontName=
        safe_text,
    lineStyle=
        safe_text,
    fontSize=
        st.integers()
)
styles::JvmTypeReference_strategy = st.builds(
    styles::JvmTypeReference,
)
StyleContainerElement_strategy = st.builds(
    StyleContainerElement,
)
styles::Gradient_strategy = st.builds(
    styles::Gradient,
)
styles::HighlightingValues_strategy = st.builds(
    styles::HighlightingValues,
)
styles::ColorOrGradient_strategy = st.builds(
    styles::ColorOrGradient,
)
styles::StyleContainerElement_strategy = st.builds(
    styles::StyleContainerElement,
    name=
        safe_text,
    description=
        safe_text
)
styles::StyleContainer_strategy = st.builds(
    styles::StyleContainer,
)
styles::Style_strategy = st.builds(
    styles::Style,
)

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=styles::ColorConstantRef_strategy)
@settings(max_examples=50)
def test_styles::colorconstantref_instantiation(instance):
    assert isinstance(instance, styles::ColorConstantRef)

@given(instance=styles::ColorConstantRef_strategy)
def test_styles::colorconstantref_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=styles::ColorConstantRef_strategy)
def test_styles::colorconstantref_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=styles::RGBColor_strategy)
@settings(max_examples=50)
def test_styles::rgbcolor_instantiation(instance):
    assert isinstance(instance, styles::RGBColor)

@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_red_type(instance):
    assert isinstance(instance.red, int)


@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_green_type(instance):
    assert isinstance(instance.green, int)


@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_green_setter(instance):
    original = instance.green
    instance.green = original
    assert instance.green == original

@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_blue_type(instance):
    assert isinstance(instance.blue, int)


@given(instance=styles::RGBColor_strategy)
def test_styles::rgbcolor_blue_setter(instance):
    original = instance.blue
    instance.blue = original
    assert instance.blue == original

@given(instance=ColorWithTransparency_strategy)
@settings(max_examples=50)
def test_colorwithtransparency_instantiation(instance):
    assert isinstance(instance, ColorWithTransparency)

@given(instance=ColorOrGradient_strategy)
@settings(max_examples=50)
def test_colororgradient_instantiation(instance):
    assert isinstance(instance, ColorOrGradient)

@given(instance=styles::GradientRef_strategy)
@settings(max_examples=50)
def test_styles::gradientref_instantiation(instance):
    assert isinstance(instance, styles::GradientRef)

@given(instance=styles::Transparent_strategy)
@settings(max_examples=50)
def test_styles::transparent_instantiation(instance):
    assert isinstance(instance, styles::Transparent)

@given(instance=styles::Transparent_strategy)
def test_styles::transparent_transparent_type(instance):
    assert isinstance(instance.transparent, bool)


@given(instance=styles::Transparent_strategy)
def test_styles::transparent_transparent_setter(instance):
    original = instance.transparent
    instance.transparent = original
    assert instance.transparent == original

@given(instance=styles::Color_strategy)
@settings(max_examples=50)
def test_styles::color_instantiation(instance):
    assert isinstance(instance, styles::Color)

@given(instance=styles::ColorWithTransparency_strategy)
@settings(max_examples=50)
def test_styles::colorwithtransparency_instantiation(instance):
    assert isinstance(instance, styles::ColorWithTransparency)

@given(instance=styles::GradientColorArea_strategy)
@settings(max_examples=50)
def test_styles::gradientcolorarea_instantiation(instance):
    assert isinstance(instance, styles::GradientColorArea)

@given(instance=styles::GradientColorArea_strategy)
def test_styles::gradientcolorarea_offset_type(instance):
    assert isinstance(instance.offset, float)


@given(instance=styles::GradientColorArea_strategy)
def test_styles::gradientcolorarea_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=styles::GradientLayout_strategy)
@settings(max_examples=50)
def test_styles::gradientlayout_instantiation(instance):
    assert isinstance(instance, styles::GradientLayout)

@given(instance=styles::StyleLayout_strategy)
@settings(max_examples=50)
def test_styles::stylelayout_instantiation(instance):
    assert isinstance(instance, styles::StyleLayout)

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontBold_type(instance):
    assert isinstance(instance.fontBold, str)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontBold_setter(instance):
    original = instance.fontBold
    instance.fontBold = original
    assert instance.fontBold == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontItalic_type(instance):
    assert isinstance(instance.fontItalic, str)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontItalic_setter(instance):
    original = instance.fontItalic
    instance.fontItalic = original
    assert instance.fontItalic == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_transparency_type(instance):
    assert isinstance(instance.transparency, float)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_transparency_setter(instance):
    original = instance.transparency
    instance.transparency = original
    assert instance.transparency == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_lineWidth_type(instance):
    assert isinstance(instance.lineWidth, int)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_gradient_orientation_type(instance):
    assert isinstance(instance.gradient_orientation, str)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_gradient_orientation_setter(instance):
    original = instance.gradient_orientation
    instance.gradient_orientation = original
    assert instance.gradient_orientation == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontName_type(instance):
    assert isinstance(instance.fontName, str)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontName_setter(instance):
    original = instance.fontName
    instance.fontName = original
    assert instance.fontName == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_lineStyle_type(instance):
    assert isinstance(instance.lineStyle, str)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_lineStyle_setter(instance):
    original = instance.lineStyle
    instance.lineStyle = original
    assert instance.lineStyle == original

@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontSize_type(instance):
    assert isinstance(instance.fontSize, int)


@given(instance=styles::StyleLayout_strategy)
def test_styles::stylelayout_fontSize_setter(instance):
    original = instance.fontSize
    instance.fontSize = original
    assert instance.fontSize == original

@given(instance=styles::JvmTypeReference_strategy)
@settings(max_examples=50)
def test_styles::jvmtypereference_instantiation(instance):
    assert isinstance(instance, styles::JvmTypeReference)

@given(instance=StyleContainerElement_strategy)
@settings(max_examples=50)
def test_stylecontainerelement_instantiation(instance):
    assert isinstance(instance, StyleContainerElement)

@given(instance=styles::Gradient_strategy)
@settings(max_examples=50)
def test_styles::gradient_instantiation(instance):
    assert isinstance(instance, styles::Gradient)

@given(instance=styles::HighlightingValues_strategy)
@settings(max_examples=50)
def test_styles::highlightingvalues_instantiation(instance):
    assert isinstance(instance, styles::HighlightingValues)

@given(instance=styles::ColorOrGradient_strategy)
@settings(max_examples=50)
def test_styles::colororgradient_instantiation(instance):
    assert isinstance(instance, styles::ColorOrGradient)

@given(instance=styles::StyleContainerElement_strategy)
@settings(max_examples=50)
def test_styles::stylecontainerelement_instantiation(instance):
    assert isinstance(instance, styles::StyleContainerElement)

@given(instance=styles::StyleContainerElement_strategy)
def test_styles::stylecontainerelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=styles::StyleContainerElement_strategy)
def test_styles::stylecontainerelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=styles::StyleContainerElement_strategy)
def test_styles::stylecontainerelement_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=styles::StyleContainerElement_strategy)
def test_styles::stylecontainerelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=styles::StyleContainer_strategy)
@settings(max_examples=50)
def test_styles::stylecontainer_instantiation(instance):
    assert isinstance(instance, styles::StyleContainer)

@given(instance=styles::Style_strategy)
@settings(max_examples=50)
def test_styles::style_instantiation(instance):
    assert isinstance(instance, styles::Style)
