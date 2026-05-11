import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    notation::EReference,
    Value,
    notation::ReferenceValue,
    notation::AttributeValue,
    notation::Definition,
    notation::IdElement,
    notation::EAttribute,
    TextualElement,
    notation::Keyword,
    notation::Value,
    notation::Token,
    Figure,
    notation::Rectangle,
    GraphicalElement,
    notation::Label,
    notation::Line,
    notation::Figure,
    NotationElement,
    notation::Composite,
    notation::SyntaxOf,
    notation::TextualElement,
    notation::GraphicalElement,
    IdElement,
    notation::NotationElement,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_notation::ereference_is_not_abstract():
    assert not inspect.isabstract(notation::EReference)


def test_notation::ereference_constructor_exists():
    assert callable(notation::EReference.__init__)


def test_notation::ereference_constructor_args():
    sig = inspect.signature(notation::EReference.__init__)
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



def test_notation::definition_is_not_abstract():
    assert not inspect.isabstract(notation::Definition)


def test_notation::definition_constructor_exists():
    assert callable(notation::Definition.__init__)


def test_notation::definition_constructor_args():
    sig = inspect.signature(notation::Definition.__init__)
    params = list(sig.parameters.keys())



def test_notation::idelement_is_not_abstract():
    assert not inspect.isabstract(notation::IdElement)


def test_notation::idelement_constructor_exists():
    assert callable(notation::IdElement.__init__)


def test_notation::idelement_constructor_args():
    sig = inspect.signature(notation::IdElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_notation::idelement_has_id():
    assert hasattr(notation::IdElement, "id")
    descriptor = None
    for klass in notation::IdElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_notation::eattribute_is_not_abstract():
    assert not inspect.isabstract(notation::EAttribute)


def test_notation::eattribute_constructor_exists():
    assert callable(notation::EAttribute.__init__)


def test_notation::eattribute_constructor_args():
    sig = inspect.signature(notation::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_textualelement_is_not_abstract():
    assert not inspect.isabstract(TextualElement)


def test_textualelement_constructor_exists():
    assert callable(TextualElement.__init__)


def test_textualelement_constructor_args():
    sig = inspect.signature(TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::keyword_is_not_abstract():
    assert not inspect.isabstract(notation::Keyword)


def test_notation::keyword_constructor_exists():
    assert callable(notation::Keyword.__init__)


def test_notation::keyword_constructor_args():
    sig = inspect.signature(notation::Keyword.__init__)
    params = list(sig.parameters.keys())



def test_notation::value_is_not_abstract():
    assert not inspect.isabstract(notation::Value)


def test_notation::value_constructor_exists():
    assert callable(notation::Value.__init__)


def test_notation::value_constructor_args():
    sig = inspect.signature(notation::Value.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_notation::value_has_separator():
    assert hasattr(notation::Value, "separator")
    descriptor = None
    for klass in notation::Value.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_notation::token_is_not_abstract():
    assert not inspect.isabstract(notation::Token)


def test_notation::token_constructor_exists():
    assert callable(notation::Token.__init__)


def test_notation::token_constructor_args():
    sig = inspect.signature(notation::Token.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation::rectangle_is_not_abstract():
    assert not inspect.isabstract(notation::Rectangle)


def test_notation::rectangle_constructor_exists():
    assert callable(notation::Rectangle.__init__)


def test_notation::rectangle_constructor_args():
    sig = inspect.signature(notation::Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::label_is_not_abstract():
    assert not inspect.isabstract(notation::Label)


def test_notation::label_constructor_exists():
    assert callable(notation::Label.__init__)


def test_notation::label_constructor_args():
    sig = inspect.signature(notation::Label.__init__)
    params = list(sig.parameters.keys())



def test_notation::line_is_not_abstract():
    assert not inspect.isabstract(notation::Line)


def test_notation::line_constructor_exists():
    assert callable(notation::Line.__init__)


def test_notation::line_constructor_args():
    sig = inspect.signature(notation::Line.__init__)
    params = list(sig.parameters.keys())



def test_notation::figure_is_not_abstract():
    assert not inspect.isabstract(notation::Figure)


def test_notation::figure_constructor_exists():
    assert callable(notation::Figure.__init__)


def test_notation::figure_constructor_args():
    sig = inspect.signature(notation::Figure.__init__)
    params = list(sig.parameters.keys())



def test_notationelement_is_not_abstract():
    assert not inspect.isabstract(NotationElement)


def test_notationelement_constructor_exists():
    assert callable(NotationElement.__init__)


def test_notationelement_constructor_args():
    sig = inspect.signature(NotationElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::composite_is_not_abstract():
    assert not inspect.isabstract(notation::Composite)


def test_notation::composite_constructor_exists():
    assert callable(notation::Composite.__init__)


def test_notation::composite_constructor_args():
    sig = inspect.signature(notation::Composite.__init__)
    params = list(sig.parameters.keys())



def test_notation::syntaxof_is_not_abstract():
    assert not inspect.isabstract(notation::SyntaxOf)


def test_notation::syntaxof_constructor_exists():
    assert callable(notation::SyntaxOf.__init__)


def test_notation::syntaxof_constructor_args():
    sig = inspect.signature(notation::SyntaxOf.__init__)
    params = list(sig.parameters.keys())



def test_notation::textualelement_is_not_abstract():
    assert not inspect.isabstract(notation::TextualElement)


def test_notation::textualelement_constructor_exists():
    assert callable(notation::TextualElement.__init__)


def test_notation::textualelement_constructor_args():
    sig = inspect.signature(notation::TextualElement.__init__)
    params = list(sig.parameters.keys())
    assert "fill" in params, "Missing parameter 'fill'"

def test_notation::textualelement_has_fill():
    assert hasattr(notation::TextualElement, "fill")
    descriptor = None
    for klass in notation::TextualElement.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)



def test_notation::graphicalelement_is_not_abstract():
    assert not inspect.isabstract(notation::GraphicalElement)


def test_notation::graphicalelement_constructor_exists():
    assert callable(notation::GraphicalElement.__init__)


def test_notation::graphicalelement_constructor_args():
    sig = inspect.signature(notation::GraphicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "fill" in params, "Missing parameter 'fill'"
    assert "height" in params, "Missing parameter 'height'"
    assert "stroke" in params, "Missing parameter 'stroke'"
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "x" in params, "Missing parameter 'x'"

def test_notation::graphicalelement_has_fill():
    assert hasattr(notation::GraphicalElement, "fill")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)

def test_notation::graphicalelement_has_height():
    assert hasattr(notation::GraphicalElement, "height")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation::graphicalelement_has_stroke():
    assert hasattr(notation::GraphicalElement, "stroke")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "stroke" in klass.__dict__:
            descriptor = klass.__dict__["stroke"]
            break
    assert isinstance(descriptor, property)

def test_notation::graphicalelement_has_y():
    assert hasattr(notation::GraphicalElement, "y")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_notation::graphicalelement_has_width():
    assert hasattr(notation::GraphicalElement, "width")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation::graphicalelement_has_x():
    assert hasattr(notation::GraphicalElement, "x")
    descriptor = None
    for klass in notation::GraphicalElement.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_idelement_is_not_abstract():
    assert not inspect.isabstract(IdElement)


def test_idelement_constructor_exists():
    assert callable(IdElement.__init__)


def test_idelement_constructor_args():
    sig = inspect.signature(IdElement.__init__)
    params = list(sig.parameters.keys())



def test_notation::notationelement_is_not_abstract():
    assert not inspect.isabstract(notation::NotationElement)


def test_notation::notationelement_constructor_exists():
    assert callable(notation::NotationElement.__init__)


def test_notation::notationelement_constructor_args():
    sig = inspect.signature(notation::NotationElement.__init__)
    params = list(sig.parameters.keys())

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "BLUE",
        "GREEN",
        "RED",
        "BLACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
notation::EReference_strategy = st.builds(
    notation::EReference,
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
notation::Definition_strategy = st.builds(
    notation::Definition,
)
notation::IdElement_strategy = st.builds(
    notation::IdElement,
    id=
        safe_text
)
notation::EAttribute_strategy = st.builds(
    notation::EAttribute,
)
TextualElement_strategy = st.builds(
    TextualElement,
)
notation::Keyword_strategy = st.builds(
    notation::Keyword,
)
notation::Value_strategy = st.builds(
    notation::Value,
    separator=
        safe_text
)
notation::Token_strategy = st.builds(
    notation::Token,
)
Figure_strategy = st.builds(
    Figure,
)
notation::Rectangle_strategy = st.builds(
    notation::Rectangle,
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
notation::Label_strategy = st.builds(
    notation::Label,
)
notation::Line_strategy = st.builds(
    notation::Line,
)
notation::Figure_strategy = st.builds(
    notation::Figure,
)
NotationElement_strategy = st.builds(
    NotationElement,
)
notation::Composite_strategy = st.builds(
    notation::Composite,
)
notation::SyntaxOf_strategy = st.builds(
    notation::SyntaxOf,
)
notation::TextualElement_strategy = st.builds(
    notation::TextualElement,
    fill=
        safe_text
)
notation::GraphicalElement_strategy = st.builds(
    notation::GraphicalElement,
    fill=
        safe_text,
    height=
        st.integers(),
    stroke=
        safe_text,
    y=
        st.integers(),
    width=
        st.integers(),
    x=
        st.integers()
)
IdElement_strategy = st.builds(
    IdElement,
)
notation::NotationElement_strategy = st.builds(
    notation::NotationElement,
)

@given(instance=notation::EReference_strategy)
@settings(max_examples=50)
def test_notation::ereference_instantiation(instance):
    assert isinstance(instance, notation::EReference)

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

@given(instance=notation::Definition_strategy)
@settings(max_examples=50)
def test_notation::definition_instantiation(instance):
    assert isinstance(instance, notation::Definition)

@given(instance=notation::IdElement_strategy)
@settings(max_examples=50)
def test_notation::idelement_instantiation(instance):
    assert isinstance(instance, notation::IdElement)

@given(instance=notation::IdElement_strategy)
def test_notation::idelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=notation::IdElement_strategy)
def test_notation::idelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=notation::EAttribute_strategy)
@settings(max_examples=50)
def test_notation::eattribute_instantiation(instance):
    assert isinstance(instance, notation::EAttribute)

@given(instance=TextualElement_strategy)
@settings(max_examples=50)
def test_textualelement_instantiation(instance):
    assert isinstance(instance, TextualElement)

@given(instance=notation::Keyword_strategy)
@settings(max_examples=50)
def test_notation::keyword_instantiation(instance):
    assert isinstance(instance, notation::Keyword)

@given(instance=notation::Value_strategy)
@settings(max_examples=50)
def test_notation::value_instantiation(instance):
    assert isinstance(instance, notation::Value)

@given(instance=notation::Value_strategy)
def test_notation::value_separator_type(instance):
    assert isinstance(instance.separator, str)


@given(instance=notation::Value_strategy)
def test_notation::value_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=notation::Token_strategy)
@settings(max_examples=50)
def test_notation::token_instantiation(instance):
    assert isinstance(instance, notation::Token)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=notation::Rectangle_strategy)
@settings(max_examples=50)
def test_notation::rectangle_instantiation(instance):
    assert isinstance(instance, notation::Rectangle)

@given(instance=GraphicalElement_strategy)
@settings(max_examples=50)
def test_graphicalelement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)

@given(instance=notation::Label_strategy)
@settings(max_examples=50)
def test_notation::label_instantiation(instance):
    assert isinstance(instance, notation::Label)

@given(instance=notation::Line_strategy)
@settings(max_examples=50)
def test_notation::line_instantiation(instance):
    assert isinstance(instance, notation::Line)

@given(instance=notation::Figure_strategy)
@settings(max_examples=50)
def test_notation::figure_instantiation(instance):
    assert isinstance(instance, notation::Figure)

@given(instance=NotationElement_strategy)
@settings(max_examples=50)
def test_notationelement_instantiation(instance):
    assert isinstance(instance, NotationElement)

@given(instance=notation::Composite_strategy)
@settings(max_examples=50)
def test_notation::composite_instantiation(instance):
    assert isinstance(instance, notation::Composite)

@given(instance=notation::SyntaxOf_strategy)
@settings(max_examples=50)
def test_notation::syntaxof_instantiation(instance):
    assert isinstance(instance, notation::SyntaxOf)

@given(instance=notation::TextualElement_strategy)
@settings(max_examples=50)
def test_notation::textualelement_instantiation(instance):
    assert isinstance(instance, notation::TextualElement)

@given(instance=notation::TextualElement_strategy)
def test_notation::textualelement_fill_type(instance):
    assert isinstance(instance.fill, str)


@given(instance=notation::TextualElement_strategy)
def test_notation::textualelement_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=notation::GraphicalElement_strategy)
@settings(max_examples=50)
def test_notation::graphicalelement_instantiation(instance):
    assert isinstance(instance, notation::GraphicalElement)

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_fill_type(instance):
    assert isinstance(instance.fill, str)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_stroke_type(instance):
    assert isinstance(instance.stroke, str)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_stroke_setter(instance):
    original = instance.stroke
    instance.stroke = original
    assert instance.stroke == original

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=notation::GraphicalElement_strategy)
def test_notation::graphicalelement_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=IdElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IdElement)

@given(instance=notation::NotationElement_strategy)
@settings(max_examples=50)
def test_notation::notationelement_instantiation(instance):
    assert isinstance(instance, notation::NotationElement)
