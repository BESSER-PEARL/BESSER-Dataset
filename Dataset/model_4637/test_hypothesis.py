import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    notation_Definition,
    notation_EReference,
    Value,
    notation_ReferenceValue,
    notation_AttributeValue,
    notation_EAttribute,
    TextualElement,
    notation_Keyword,
    notation_Value,
    notation_Token,
    Figure,
    notation_Rectangle,
    notation_IdElement,
    GraphicalElement,
    notation_Label,
    notation_Figure,
    notation_Line,
    notation_Image,
    NotationElement,
    notation_TextualElement,
    notation_SyntaxOf,
    notation_Composite,
    notation_GraphicalElement,
    IdElement,
    notation_NotationElement,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_notation_definition_is_not_abstract():
    assert not inspect.isabstract(notation_Definition)


def test_notation_definition_constructor_exists():
    assert callable(notation_Definition.__init__)


def test_notation_definition_constructor_args():
    sig = inspect.signature(notation_Definition.__init__)
    params = list(sig.parameters.keys())



def test_notation_ereference_is_not_abstract():
    assert not inspect.isabstract(notation_EReference)


def test_notation_ereference_constructor_exists():
    assert callable(notation_EReference.__init__)


def test_notation_ereference_constructor_args():
    sig = inspect.signature(notation_EReference.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_notation_referencevalue_is_not_abstract():
    assert not inspect.isabstract(notation_ReferenceValue)


def test_notation_referencevalue_constructor_exists():
    assert callable(notation_ReferenceValue.__init__)


def test_notation_referencevalue_constructor_args():
    sig = inspect.signature(notation_ReferenceValue.__init__)
    params = list(sig.parameters.keys())



def test_notation_attributevalue_is_not_abstract():
    assert not inspect.isabstract(notation_AttributeValue)


def test_notation_attributevalue_constructor_exists():
    assert callable(notation_AttributeValue.__init__)


def test_notation_attributevalue_constructor_args():
    sig = inspect.signature(notation_AttributeValue.__init__)
    params = list(sig.parameters.keys())



def test_notation_eattribute_is_not_abstract():
    assert not inspect.isabstract(notation_EAttribute)


def test_notation_eattribute_constructor_exists():
    assert callable(notation_EAttribute.__init__)


def test_notation_eattribute_constructor_args():
    sig = inspect.signature(notation_EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_textualelement_is_not_abstract():
    assert not inspect.isabstract(TextualElement)


def test_textualelement_constructor_exists():
    assert callable(TextualElement.__init__)


def test_textualelement_constructor_args():
    sig = inspect.signature(TextualElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_keyword_is_not_abstract():
    assert not inspect.isabstract(notation_Keyword)


def test_notation_keyword_constructor_exists():
    assert callable(notation_Keyword.__init__)


def test_notation_keyword_constructor_args():
    sig = inspect.signature(notation_Keyword.__init__)
    params = list(sig.parameters.keys())



def test_notation_value_is_not_abstract():
    assert not inspect.isabstract(notation_Value)


def test_notation_value_constructor_exists():
    assert callable(notation_Value.__init__)


def test_notation_value_constructor_args():
    sig = inspect.signature(notation_Value.__init__)
    params = list(sig.parameters.keys())
    assert "separator" in params, "Missing parameter 'separator'"

def test_notation_value_has_separator():
    assert hasattr(notation_Value, "separator")
    descriptor = None
    for klass in notation_Value.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)



def test_notation_token_is_not_abstract():
    assert not inspect.isabstract(notation_Token)


def test_notation_token_constructor_exists():
    assert callable(notation_Token.__init__)


def test_notation_token_constructor_args():
    sig = inspect.signature(notation_Token.__init__)
    params = list(sig.parameters.keys())



def test_figure_is_not_abstract():
    assert not inspect.isabstract(Figure)


def test_figure_constructor_exists():
    assert callable(Figure.__init__)


def test_figure_constructor_args():
    sig = inspect.signature(Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation_rectangle_is_not_abstract():
    assert not inspect.isabstract(notation_Rectangle)


def test_notation_rectangle_constructor_exists():
    assert callable(notation_Rectangle.__init__)


def test_notation_rectangle_constructor_args():
    sig = inspect.signature(notation_Rectangle.__init__)
    params = list(sig.parameters.keys())



def test_notation_idelement_is_not_abstract():
    assert not inspect.isabstract(notation_IdElement)


def test_notation_idelement_constructor_exists():
    assert callable(notation_IdElement.__init__)


def test_notation_idelement_constructor_args():
    sig = inspect.signature(notation_IdElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_notation_idelement_has_id():
    assert hasattr(notation_IdElement, "id")
    descriptor = None
    for klass in notation_IdElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(GraphicalElement)


def test_graphicalelement_constructor_exists():
    assert callable(GraphicalElement.__init__)


def test_graphicalelement_constructor_args():
    sig = inspect.signature(GraphicalElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_label_is_not_abstract():
    assert not inspect.isabstract(notation_Label)


def test_notation_label_constructor_exists():
    assert callable(notation_Label.__init__)


def test_notation_label_constructor_args():
    sig = inspect.signature(notation_Label.__init__)
    params = list(sig.parameters.keys())



def test_notation_figure_is_not_abstract():
    assert not inspect.isabstract(notation_Figure)


def test_notation_figure_constructor_exists():
    assert callable(notation_Figure.__init__)


def test_notation_figure_constructor_args():
    sig = inspect.signature(notation_Figure.__init__)
    params = list(sig.parameters.keys())



def test_notation_line_is_not_abstract():
    assert not inspect.isabstract(notation_Line)


def test_notation_line_constructor_exists():
    assert callable(notation_Line.__init__)


def test_notation_line_constructor_args():
    sig = inspect.signature(notation_Line.__init__)
    params = list(sig.parameters.keys())



def test_notation_image_is_not_abstract():
    assert not inspect.isabstract(notation_Image)


def test_notation_image_constructor_exists():
    assert callable(notation_Image.__init__)


def test_notation_image_constructor_args():
    sig = inspect.signature(notation_Image.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_notation_image_has_path():
    assert hasattr(notation_Image, "path")
    descriptor = None
    for klass in notation_Image.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_notationelement_is_not_abstract():
    assert not inspect.isabstract(NotationElement)


def test_notationelement_constructor_exists():
    assert callable(NotationElement.__init__)


def test_notationelement_constructor_args():
    sig = inspect.signature(NotationElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_textualelement_is_not_abstract():
    assert not inspect.isabstract(notation_TextualElement)


def test_notation_textualelement_constructor_exists():
    assert callable(notation_TextualElement.__init__)


def test_notation_textualelement_constructor_args():
    sig = inspect.signature(notation_TextualElement.__init__)
    params = list(sig.parameters.keys())
    assert "fill" in params, "Missing parameter 'fill'"

def test_notation_textualelement_has_fill():
    assert hasattr(notation_TextualElement, "fill")
    descriptor = None
    for klass in notation_TextualElement.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)



def test_notation_syntaxof_is_not_abstract():
    assert not inspect.isabstract(notation_SyntaxOf)


def test_notation_syntaxof_constructor_exists():
    assert callable(notation_SyntaxOf.__init__)


def test_notation_syntaxof_constructor_args():
    sig = inspect.signature(notation_SyntaxOf.__init__)
    params = list(sig.parameters.keys())



def test_notation_composite_is_not_abstract():
    assert not inspect.isabstract(notation_Composite)


def test_notation_composite_constructor_exists():
    assert callable(notation_Composite.__init__)


def test_notation_composite_constructor_args():
    sig = inspect.signature(notation_Composite.__init__)
    params = list(sig.parameters.keys())



def test_notation_graphicalelement_is_not_abstract():
    assert not inspect.isabstract(notation_GraphicalElement)


def test_notation_graphicalelement_constructor_exists():
    assert callable(notation_GraphicalElement.__init__)


def test_notation_graphicalelement_constructor_args():
    sig = inspect.signature(notation_GraphicalElement.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "stroke" in params, "Missing parameter 'stroke'"
    assert "x" in params, "Missing parameter 'x'"
    assert "fill" in params, "Missing parameter 'fill'"

def test_notation_graphicalelement_has_y():
    assert hasattr(notation_GraphicalElement, "y")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_notation_graphicalelement_has_width():
    assert hasattr(notation_GraphicalElement, "width")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_notation_graphicalelement_has_height():
    assert hasattr(notation_GraphicalElement, "height")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_notation_graphicalelement_has_stroke():
    assert hasattr(notation_GraphicalElement, "stroke")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "stroke" in klass.__dict__:
            descriptor = klass.__dict__["stroke"]
            break
    assert isinstance(descriptor, property)

def test_notation_graphicalelement_has_x():
    assert hasattr(notation_GraphicalElement, "x")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_notation_graphicalelement_has_fill():
    assert hasattr(notation_GraphicalElement, "fill")
    descriptor = None
    for klass in notation_GraphicalElement.__mro__:
        if "fill" in klass.__dict__:
            descriptor = klass.__dict__["fill"]
            break
    assert isinstance(descriptor, property)



def test_idelement_is_not_abstract():
    assert not inspect.isabstract(IdElement)


def test_idelement_constructor_exists():
    assert callable(IdElement.__init__)


def test_idelement_constructor_args():
    sig = inspect.signature(IdElement.__init__)
    params = list(sig.parameters.keys())



def test_notation_notationelement_is_not_abstract():
    assert not inspect.isabstract(notation_NotationElement)


def test_notation_notationelement_constructor_exists():
    assert callable(notation_NotationElement.__init__)


def test_notation_notationelement_constructor_args():
    sig = inspect.signature(notation_NotationElement.__init__)
    params = list(sig.parameters.keys())

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "RED",
        "BLACK",
        "YELLOW",
        "ORANGE",
        "WHITE",
        "BLUE",
        "GREEN",
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
notation_Definition_strategy = st.builds(
    notation_Definition,
)
notation_EReference_strategy = st.builds(
    notation_EReference,
)
Value_strategy = st.builds(
    Value,
)
notation_ReferenceValue_strategy = st.builds(
    notation_ReferenceValue,
)
notation_AttributeValue_strategy = st.builds(
    notation_AttributeValue,
)
notation_EAttribute_strategy = st.builds(
    notation_EAttribute,
)
TextualElement_strategy = st.builds(
    TextualElement,
)
notation_Keyword_strategy = st.builds(
    notation_Keyword,
)
notation_Value_strategy = st.builds(
    notation_Value,
    separator=
        safe_text
)
notation_Token_strategy = st.builds(
    notation_Token,
)
Figure_strategy = st.builds(
    Figure,
)
notation_Rectangle_strategy = st.builds(
    notation_Rectangle,
)
notation_IdElement_strategy = st.builds(
    notation_IdElement,
    id=
        safe_text
)
GraphicalElement_strategy = st.builds(
    GraphicalElement,
)
notation_Label_strategy = st.builds(
    notation_Label,
)
notation_Figure_strategy = st.builds(
    notation_Figure,
)
notation_Line_strategy = st.builds(
    notation_Line,
)
notation_Image_strategy = st.builds(
    notation_Image,
    path=
        safe_text
)
NotationElement_strategy = st.builds(
    NotationElement,
)
notation_TextualElement_strategy = st.builds(
    notation_TextualElement,
    fill=
        safe_text
)
notation_SyntaxOf_strategy = st.builds(
    notation_SyntaxOf,
)
notation_Composite_strategy = st.builds(
    notation_Composite,
)
notation_GraphicalElement_strategy = st.builds(
    notation_GraphicalElement,
    y=
        st.integers(),
    width=
        st.integers(),
    height=
        st.integers(),
    stroke=
        safe_text,
    x=
        st.integers(),
    fill=
        safe_text
)
IdElement_strategy = st.builds(
    IdElement,
)
notation_NotationElement_strategy = st.builds(
    notation_NotationElement,
)

@given(instance=notation_Definition_strategy)
@settings(max_examples=50)
def test_notation_definition_instantiation(instance):
    assert isinstance(instance, notation_Definition)

@given(instance=notation_EReference_strategy)
@settings(max_examples=50)
def test_notation_ereference_instantiation(instance):
    assert isinstance(instance, notation_EReference)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=notation_ReferenceValue_strategy)
@settings(max_examples=50)
def test_notation_referencevalue_instantiation(instance):
    assert isinstance(instance, notation_ReferenceValue)

@given(instance=notation_AttributeValue_strategy)
@settings(max_examples=50)
def test_notation_attributevalue_instantiation(instance):
    assert isinstance(instance, notation_AttributeValue)

@given(instance=notation_EAttribute_strategy)
@settings(max_examples=50)
def test_notation_eattribute_instantiation(instance):
    assert isinstance(instance, notation_EAttribute)

@given(instance=TextualElement_strategy)
@settings(max_examples=50)
def test_textualelement_instantiation(instance):
    assert isinstance(instance, TextualElement)

@given(instance=notation_Keyword_strategy)
@settings(max_examples=50)
def test_notation_keyword_instantiation(instance):
    assert isinstance(instance, notation_Keyword)

@given(instance=notation_Value_strategy)
@settings(max_examples=50)
def test_notation_value_instantiation(instance):
    assert isinstance(instance, notation_Value)



@given(instance=notation_Value_strategy)
def test_notation_value_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=notation_Token_strategy)
@settings(max_examples=50)
def test_notation_token_instantiation(instance):
    assert isinstance(instance, notation_Token)

@given(instance=Figure_strategy)
@settings(max_examples=50)
def test_figure_instantiation(instance):
    assert isinstance(instance, Figure)

@given(instance=notation_Rectangle_strategy)
@settings(max_examples=50)
def test_notation_rectangle_instantiation(instance):
    assert isinstance(instance, notation_Rectangle)

@given(instance=notation_IdElement_strategy)
@settings(max_examples=50)
def test_notation_idelement_instantiation(instance):
    assert isinstance(instance, notation_IdElement)



@given(instance=notation_IdElement_strategy)
def test_notation_idelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=GraphicalElement_strategy)
@settings(max_examples=50)
def test_graphicalelement_instantiation(instance):
    assert isinstance(instance, GraphicalElement)

@given(instance=notation_Label_strategy)
@settings(max_examples=50)
def test_notation_label_instantiation(instance):
    assert isinstance(instance, notation_Label)

@given(instance=notation_Figure_strategy)
@settings(max_examples=50)
def test_notation_figure_instantiation(instance):
    assert isinstance(instance, notation_Figure)

@given(instance=notation_Line_strategy)
@settings(max_examples=50)
def test_notation_line_instantiation(instance):
    assert isinstance(instance, notation_Line)

@given(instance=notation_Image_strategy)
@settings(max_examples=50)
def test_notation_image_instantiation(instance):
    assert isinstance(instance, notation_Image)



@given(instance=notation_Image_strategy)
def test_notation_image_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=NotationElement_strategy)
@settings(max_examples=50)
def test_notationelement_instantiation(instance):
    assert isinstance(instance, NotationElement)

@given(instance=notation_TextualElement_strategy)
@settings(max_examples=50)
def test_notation_textualelement_instantiation(instance):
    assert isinstance(instance, notation_TextualElement)



@given(instance=notation_TextualElement_strategy)
def test_notation_textualelement_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=notation_SyntaxOf_strategy)
@settings(max_examples=50)
def test_notation_syntaxof_instantiation(instance):
    assert isinstance(instance, notation_SyntaxOf)

@given(instance=notation_Composite_strategy)
@settings(max_examples=50)
def test_notation_composite_instantiation(instance):
    assert isinstance(instance, notation_Composite)

@given(instance=notation_GraphicalElement_strategy)
@settings(max_examples=50)
def test_notation_graphicalelement_instantiation(instance):
    assert isinstance(instance, notation_GraphicalElement)



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_stroke_setter(instance):
    original = instance.stroke
    instance.stroke = original
    assert instance.stroke == original



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=notation_GraphicalElement_strategy)
def test_notation_graphicalelement_fill_setter(instance):
    original = instance.fill
    instance.fill = original
    assert instance.fill == original

@given(instance=IdElement_strategy)
@settings(max_examples=50)
def test_idelement_instantiation(instance):
    assert isinstance(instance, IdElement)

@given(instance=notation_NotationElement_strategy)
@settings(max_examples=50)
def test_notation_notationelement_instantiation(instance):
    assert isinstance(instance, notation_NotationElement)
