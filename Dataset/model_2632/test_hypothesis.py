import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    modeldraw::EEnumLiteral,
    modeldraw::Enumerator,
    Relation,
    modeldraw::Level,
    modeldraw::Edge,
    modeldraw::EAttribute,
    Item,
    modeldraw::NamedItem,
    modeldraw::Information,
    modeldraw::NodeEnumerator,
    modeldraw::BooleanAttribute,
    modeldraw::MutatorDraw,
    modeldraw::EClass,
    modeldraw::Item,
    modeldraw::EReference,
    NamedItem,
    modeldraw::Content,
    modeldraw::Node,
    modeldraw::Relation,
    NodeType,
    NodeStyle,
    Decoration,
    NodeShape,
    DrawType,
    NodeColor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modeldraw::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(modeldraw::EEnumLiteral)


def test_modeldraw::eenumliteral_constructor_exists():
    assert callable(modeldraw::EEnumLiteral.__init__)


def test_modeldraw::eenumliteral_constructor_args():
    sig = inspect.signature(modeldraw::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::enumerator_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Enumerator)


def test_modeldraw::enumerator_constructor_exists():
    assert callable(modeldraw::Enumerator.__init__)


def test_modeldraw::enumerator_constructor_args():
    sig = inspect.signature(modeldraw::Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_modeldraw::enumerator_has_value():
    assert hasattr(modeldraw::Enumerator, "value")
    descriptor = None
    for klass in modeldraw::Enumerator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::level_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Level)


def test_modeldraw::level_constructor_exists():
    assert callable(modeldraw::Level.__init__)


def test_modeldraw::level_constructor_args():
    sig = inspect.signature(modeldraw::Level.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::edge_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Edge)


def test_modeldraw::edge_constructor_exists():
    assert callable(modeldraw::Edge.__init__)


def test_modeldraw::edge_constructor_args():
    sig = inspect.signature(modeldraw::Edge.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::eattribute_is_not_abstract():
    assert not inspect.isabstract(modeldraw::EAttribute)


def test_modeldraw::eattribute_constructor_exists():
    assert callable(modeldraw::EAttribute.__init__)


def test_modeldraw::eattribute_constructor_args():
    sig = inspect.signature(modeldraw::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_item_is_not_abstract():
    assert not inspect.isabstract(Item)


def test_item_constructor_exists():
    assert callable(Item.__init__)


def test_item_constructor_args():
    sig = inspect.signature(Item.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::nameditem_is_not_abstract():
    assert not inspect.isabstract(modeldraw::NamedItem)


def test_modeldraw::nameditem_constructor_exists():
    assert callable(modeldraw::NamedItem.__init__)


def test_modeldraw::nameditem_constructor_args():
    sig = inspect.signature(modeldraw::NamedItem.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::information_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Information)


def test_modeldraw::information_constructor_exists():
    assert callable(modeldraw::Information.__init__)


def test_modeldraw::information_constructor_args():
    sig = inspect.signature(modeldraw::Information.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::nodeenumerator_is_not_abstract():
    assert not inspect.isabstract(modeldraw::NodeEnumerator)


def test_modeldraw::nodeenumerator_constructor_exists():
    assert callable(modeldraw::NodeEnumerator.__init__)


def test_modeldraw::nodeenumerator_constructor_args():
    sig = inspect.signature(modeldraw::NodeEnumerator.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::booleanattribute_is_not_abstract():
    assert not inspect.isabstract(modeldraw::BooleanAttribute)


def test_modeldraw::booleanattribute_constructor_exists():
    assert callable(modeldraw::BooleanAttribute.__init__)


def test_modeldraw::booleanattribute_constructor_args():
    sig = inspect.signature(modeldraw::BooleanAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "negation" in params, "Missing parameter 'negation'"

def test_modeldraw::booleanattribute_has_negation():
    assert hasattr(modeldraw::BooleanAttribute, "negation")
    descriptor = None
    for klass in modeldraw::BooleanAttribute.__mro__:
        if "negation" in klass.__dict__:
            descriptor = klass.__dict__["negation"]
            break
    assert isinstance(descriptor, property)



def test_modeldraw::mutatordraw_is_not_abstract():
    assert not inspect.isabstract(modeldraw::MutatorDraw)


def test_modeldraw::mutatordraw_constructor_exists():
    assert callable(modeldraw::MutatorDraw.__init__)


def test_modeldraw::mutatordraw_constructor_args():
    sig = inspect.signature(modeldraw::MutatorDraw.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"
    assert "type" in params, "Missing parameter 'type'"

def test_modeldraw::mutatordraw_has_metamodel():
    assert hasattr(modeldraw::MutatorDraw, "metamodel")
    descriptor = None
    for klass in modeldraw::MutatorDraw.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)

def test_modeldraw::mutatordraw_has_type():
    assert hasattr(modeldraw::MutatorDraw, "type")
    descriptor = None
    for klass in modeldraw::MutatorDraw.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_modeldraw::eclass_is_not_abstract():
    assert not inspect.isabstract(modeldraw::EClass)


def test_modeldraw::eclass_constructor_exists():
    assert callable(modeldraw::EClass.__init__)


def test_modeldraw::eclass_constructor_args():
    sig = inspect.signature(modeldraw::EClass.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::item_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Item)


def test_modeldraw::item_constructor_exists():
    assert callable(modeldraw::Item.__init__)


def test_modeldraw::item_constructor_args():
    sig = inspect.signature(modeldraw::Item.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::ereference_is_not_abstract():
    assert not inspect.isabstract(modeldraw::EReference)


def test_modeldraw::ereference_constructor_exists():
    assert callable(modeldraw::EReference.__init__)


def test_modeldraw::ereference_constructor_args():
    sig = inspect.signature(modeldraw::EReference.__init__)
    params = list(sig.parameters.keys())



def test_nameditem_is_not_abstract():
    assert not inspect.isabstract(NamedItem)


def test_nameditem_constructor_exists():
    assert callable(NamedItem.__init__)


def test_nameditem_constructor_args():
    sig = inspect.signature(NamedItem.__init__)
    params = list(sig.parameters.keys())



def test_modeldraw::content_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Content)


def test_modeldraw::content_constructor_exists():
    assert callable(modeldraw::Content.__init__)


def test_modeldraw::content_constructor_args():
    sig = inspect.signature(modeldraw::Content.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_modeldraw::content_has_symbol():
    assert hasattr(modeldraw::Content, "symbol")
    descriptor = None
    for klass in modeldraw::Content.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_modeldraw::node_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Node)


def test_modeldraw::node_constructor_exists():
    assert callable(modeldraw::Node.__init__)


def test_modeldraw::node_constructor_args():
    sig = inspect.signature(modeldraw::Node.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "type" in params, "Missing parameter 'type'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "color" in params, "Missing parameter 'color'"

def test_modeldraw::node_has_style():
    assert hasattr(modeldraw::Node, "style")
    descriptor = None
    for klass in modeldraw::Node.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_modeldraw::node_has_type():
    assert hasattr(modeldraw::Node, "type")
    descriptor = None
    for klass in modeldraw::Node.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_modeldraw::node_has_shape():
    assert hasattr(modeldraw::Node, "shape")
    descriptor = None
    for klass in modeldraw::Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_modeldraw::node_has_color():
    assert hasattr(modeldraw::Node, "color")
    descriptor = None
    for klass in modeldraw::Node.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_modeldraw::relation_is_not_abstract():
    assert not inspect.isabstract(modeldraw::Relation)


def test_modeldraw::relation_constructor_exists():
    assert callable(modeldraw::Relation.__init__)


def test_modeldraw::relation_constructor_args():
    sig = inspect.signature(modeldraw::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "tar_decoration" in params, "Missing parameter 'tar_decoration'"
    assert "src_decoration" in params, "Missing parameter 'src_decoration'"

def test_modeldraw::relation_has_tar_decoration():
    assert hasattr(modeldraw::Relation, "tar_decoration")
    descriptor = None
    for klass in modeldraw::Relation.__mro__:
        if "tar_decoration" in klass.__dict__:
            descriptor = klass.__dict__["tar_decoration"]
            break
    assert isinstance(descriptor, property)

def test_modeldraw::relation_has_src_decoration():
    assert hasattr(modeldraw::Relation, "src_decoration")
    descriptor = None
    for klass in modeldraw::Relation.__mro__:
        if "src_decoration" in klass.__dict__:
            descriptor = klass.__dict__["src_decoration"]
            break
    assert isinstance(descriptor, property)

def test_nodetype_exists():
    # Check that the Enumeration exists
    assert NodeType is not None

def test_nodetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeType]
    expected_literals = [
        "markednode",
        "node",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeType"

def test_nodestyle_exists():
    # Check that the Enumeration exists
    assert NodeStyle is not None

def test_nodestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeStyle]
    expected_literals = [
        "underline",
        "italic",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeStyle"

def test_decoration_exists():
    # Check that the Enumeration exists
    assert Decoration is not None

def test_decoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Decoration]
    expected_literals = [
        "none",
        "open",
        "empty",
        "triangle",
        "diamond",
        "odiamond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Decoration"

def test_nodeshape_exists():
    # Check that the Enumeration exists
    assert NodeShape is not None

def test_nodeshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeShape]
    expected_literals = [
        "record",
        "circle",
        "doublecircle",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeShape"

def test_drawtype_exists():
    # Check that the Enumeration exists
    assert DrawType is not None

def test_drawtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DrawType]
    expected_literals = [
        "diagram",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DrawType"

def test_nodecolor_exists():
    # Check that the Enumeration exists
    assert NodeColor is not None

def test_nodecolor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NodeColor]
    expected_literals = [
        "gray95",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NodeColor"


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
modeldraw::EEnumLiteral_strategy = st.builds(
    modeldraw::EEnumLiteral,
)
modeldraw::Enumerator_strategy = st.builds(
    modeldraw::Enumerator,
    value=
        safe_text
)
Relation_strategy = st.builds(
    Relation,
)
modeldraw::Level_strategy = st.builds(
    modeldraw::Level,
)
modeldraw::Edge_strategy = st.builds(
    modeldraw::Edge,
)
modeldraw::EAttribute_strategy = st.builds(
    modeldraw::EAttribute,
)
Item_strategy = st.builds(
    Item,
)
modeldraw::NamedItem_strategy = st.builds(
    modeldraw::NamedItem,
)
modeldraw::Information_strategy = st.builds(
    modeldraw::Information,
)
modeldraw::NodeEnumerator_strategy = st.builds(
    modeldraw::NodeEnumerator,
)
modeldraw::BooleanAttribute_strategy = st.builds(
    modeldraw::BooleanAttribute,
    negation=
        st.booleans()
)
modeldraw::MutatorDraw_strategy = st.builds(
    modeldraw::MutatorDraw,
    metamodel=
        safe_text,
    type=
        safe_text
)
modeldraw::EClass_strategy = st.builds(
    modeldraw::EClass,
)
modeldraw::Item_strategy = st.builds(
    modeldraw::Item,
)
modeldraw::EReference_strategy = st.builds(
    modeldraw::EReference,
)
NamedItem_strategy = st.builds(
    NamedItem,
)
modeldraw::Content_strategy = st.builds(
    modeldraw::Content,
    symbol=
        safe_text
)
modeldraw::Node_strategy = st.builds(
    modeldraw::Node,
    style=
        safe_text,
    type=
        safe_text,
    shape=
        safe_text,
    color=
        safe_text
)
modeldraw::Relation_strategy = st.builds(
    modeldraw::Relation,
    tar_decoration=
        safe_text,
    src_decoration=
        safe_text
)

@given(instance=modeldraw::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_modeldraw::eenumliteral_instantiation(instance):
    assert isinstance(instance, modeldraw::EEnumLiteral)

@given(instance=modeldraw::Enumerator_strategy)
@settings(max_examples=50)
def test_modeldraw::enumerator_instantiation(instance):
    assert isinstance(instance, modeldraw::Enumerator)

@given(instance=modeldraw::Enumerator_strategy)
def test_modeldraw::enumerator_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=modeldraw::Enumerator_strategy)
def test_modeldraw::enumerator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=modeldraw::Level_strategy)
@settings(max_examples=50)
def test_modeldraw::level_instantiation(instance):
    assert isinstance(instance, modeldraw::Level)

@given(instance=modeldraw::Edge_strategy)
@settings(max_examples=50)
def test_modeldraw::edge_instantiation(instance):
    assert isinstance(instance, modeldraw::Edge)

@given(instance=modeldraw::EAttribute_strategy)
@settings(max_examples=50)
def test_modeldraw::eattribute_instantiation(instance):
    assert isinstance(instance, modeldraw::EAttribute)

@given(instance=Item_strategy)
@settings(max_examples=50)
def test_item_instantiation(instance):
    assert isinstance(instance, Item)

@given(instance=modeldraw::NamedItem_strategy)
@settings(max_examples=50)
def test_modeldraw::nameditem_instantiation(instance):
    assert isinstance(instance, modeldraw::NamedItem)

@given(instance=modeldraw::Information_strategy)
@settings(max_examples=50)
def test_modeldraw::information_instantiation(instance):
    assert isinstance(instance, modeldraw::Information)

@given(instance=modeldraw::NodeEnumerator_strategy)
@settings(max_examples=50)
def test_modeldraw::nodeenumerator_instantiation(instance):
    assert isinstance(instance, modeldraw::NodeEnumerator)

@given(instance=modeldraw::BooleanAttribute_strategy)
@settings(max_examples=50)
def test_modeldraw::booleanattribute_instantiation(instance):
    assert isinstance(instance, modeldraw::BooleanAttribute)

@given(instance=modeldraw::BooleanAttribute_strategy)
def test_modeldraw::booleanattribute_negation_type(instance):
    assert isinstance(instance.negation, bool)


@given(instance=modeldraw::BooleanAttribute_strategy)
def test_modeldraw::booleanattribute_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original

@given(instance=modeldraw::MutatorDraw_strategy)
@settings(max_examples=50)
def test_modeldraw::mutatordraw_instantiation(instance):
    assert isinstance(instance, modeldraw::MutatorDraw)

@given(instance=modeldraw::MutatorDraw_strategy)
def test_modeldraw::mutatordraw_metamodel_type(instance):
    assert isinstance(instance.metamodel, str)


@given(instance=modeldraw::MutatorDraw_strategy)
def test_modeldraw::mutatordraw_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=modeldraw::MutatorDraw_strategy)
def test_modeldraw::mutatordraw_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=modeldraw::MutatorDraw_strategy)
def test_modeldraw::mutatordraw_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=modeldraw::EClass_strategy)
@settings(max_examples=50)
def test_modeldraw::eclass_instantiation(instance):
    assert isinstance(instance, modeldraw::EClass)

@given(instance=modeldraw::Item_strategy)
@settings(max_examples=50)
def test_modeldraw::item_instantiation(instance):
    assert isinstance(instance, modeldraw::Item)

@given(instance=modeldraw::EReference_strategy)
@settings(max_examples=50)
def test_modeldraw::ereference_instantiation(instance):
    assert isinstance(instance, modeldraw::EReference)

@given(instance=NamedItem_strategy)
@settings(max_examples=50)
def test_nameditem_instantiation(instance):
    assert isinstance(instance, NamedItem)

@given(instance=modeldraw::Content_strategy)
@settings(max_examples=50)
def test_modeldraw::content_instantiation(instance):
    assert isinstance(instance, modeldraw::Content)

@given(instance=modeldraw::Content_strategy)
def test_modeldraw::content_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=modeldraw::Content_strategy)
def test_modeldraw::content_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=modeldraw::Node_strategy)
@settings(max_examples=50)
def test_modeldraw::node_instantiation(instance):
    assert isinstance(instance, modeldraw::Node)

@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=modeldraw::Node_strategy)
def test_modeldraw::node_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=modeldraw::Relation_strategy)
@settings(max_examples=50)
def test_modeldraw::relation_instantiation(instance):
    assert isinstance(instance, modeldraw::Relation)

@given(instance=modeldraw::Relation_strategy)
def test_modeldraw::relation_tar_decoration_type(instance):
    assert isinstance(instance.tar_decoration, str)


@given(instance=modeldraw::Relation_strategy)
def test_modeldraw::relation_tar_decoration_setter(instance):
    original = instance.tar_decoration
    instance.tar_decoration = original
    assert instance.tar_decoration == original

@given(instance=modeldraw::Relation_strategy)
def test_modeldraw::relation_src_decoration_type(instance):
    assert isinstance(instance.src_decoration, str)


@given(instance=modeldraw::Relation_strategy)
def test_modeldraw::relation_src_decoration_setter(instance):
    original = instance.src_decoration
    instance.src_decoration = original
    assert instance.src_decoration == original
