import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    Elements::ReferencingNode,
    Element,
    Elements::StrictElement,
    NamedElement,
    Elements::Edge,
    Elements::Node,
    Elements::Element,
    IdentifiedElement,
    Elements::Root,
    Elements::NamedElement,
    Elements::IdentifiedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_elements::referencingnode_is_not_abstract():
    assert not inspect.isabstract(Elements::ReferencingNode)


def test_elements::referencingnode_constructor_exists():
    assert callable(Elements::ReferencingNode.__init__)


def test_elements::referencingnode_constructor_args():
    sig = inspect.signature(Elements::ReferencingNode.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_elements::strictelement_is_not_abstract():
    assert not inspect.isabstract(Elements::StrictElement)


def test_elements::strictelement_constructor_exists():
    assert callable(Elements::StrictElement.__init__)


def test_elements::strictelement_constructor_args():
    sig = inspect.signature(Elements::StrictElement.__init__)
    params = list(sig.parameters.keys())
    assert "sValues" in params, "Missing parameter 'sValues'"
    assert "sValue" in params, "Missing parameter 'sValue'"

def test_elements::strictelement_has_sValues():
    assert hasattr(Elements::StrictElement, "sValues")
    descriptor = None
    for klass in Elements::StrictElement.__mro__:
        if "sValues" in klass.__dict__:
            descriptor = klass.__dict__["sValues"]
            break
    assert isinstance(descriptor, property)

def test_elements::strictelement_has_sValue():
    assert hasattr(Elements::StrictElement, "sValue")
    descriptor = None
    for klass in Elements::StrictElement.__mro__:
        if "sValue" in klass.__dict__:
            descriptor = klass.__dict__["sValue"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_elements::edge_is_not_abstract():
    assert not inspect.isabstract(Elements::Edge)


def test_elements::edge_constructor_exists():
    assert callable(Elements::Edge.__init__)


def test_elements::edge_constructor_args():
    sig = inspect.signature(Elements::Edge.__init__)
    params = list(sig.parameters.keys())



def test_elements::node_is_not_abstract():
    assert not inspect.isabstract(Elements::Node)


def test_elements::node_constructor_exists():
    assert callable(Elements::Node.__init__)


def test_elements::node_constructor_args():
    sig = inspect.signature(Elements::Node.__init__)
    params = list(sig.parameters.keys())



def test_elements::element_is_not_abstract():
    assert not inspect.isabstract(Elements::Element)


def test_elements::element_constructor_exists():
    assert callable(Elements::Element.__init__)


def test_elements::element_constructor_args():
    sig = inspect.signature(Elements::Element.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "values" in params, "Missing parameter 'values'"

def test_elements::element_has_value():
    assert hasattr(Elements::Element, "value")
    descriptor = None
    for klass in Elements::Element.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_elements::element_has_values():
    assert hasattr(Elements::Element, "values")
    descriptor = None
    for klass in Elements::Element.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_identifiedelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiedElement)


def test_identifiedelement_constructor_exists():
    assert callable(IdentifiedElement.__init__)


def test_identifiedelement_constructor_args():
    sig = inspect.signature(IdentifiedElement.__init__)
    params = list(sig.parameters.keys())



def test_elements::root_is_not_abstract():
    assert not inspect.isabstract(Elements::Root)


def test_elements::root_constructor_exists():
    assert callable(Elements::Root.__init__)


def test_elements::root_constructor_args():
    sig = inspect.signature(Elements::Root.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_elements::root_has_name():
    assert hasattr(Elements::Root, "name")
    descriptor = None
    for klass in Elements::Root.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_elements::namedelement_is_not_abstract():
    assert not inspect.isabstract(Elements::NamedElement)


def test_elements::namedelement_constructor_exists():
    assert callable(Elements::NamedElement.__init__)


def test_elements::namedelement_constructor_args():
    sig = inspect.signature(Elements::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_elements::namedelement_has_name():
    assert hasattr(Elements::NamedElement, "name")
    descriptor = None
    for klass in Elements::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_elements::identifiedelement_is_not_abstract():
    assert not inspect.isabstract(Elements::IdentifiedElement)


def test_elements::identifiedelement_constructor_exists():
    assert callable(Elements::IdentifiedElement.__init__)


def test_elements::identifiedelement_constructor_args():
    sig = inspect.signature(Elements::IdentifiedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_elements::identifiedelement_has_id():
    assert hasattr(Elements::IdentifiedElement, "id")
    descriptor = None
    for klass in Elements::IdentifiedElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)


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
Node_strategy = st.builds(
    Node,
)
Elements::ReferencingNode_strategy = st.builds(
    Elements::ReferencingNode,
)
Element_strategy = st.builds(
    Element,
)
Elements::StrictElement_strategy = st.builds(
    Elements::StrictElement,
    sValues=
        st.integers(),
    sValue=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Elements::Edge_strategy = st.builds(
    Elements::Edge,
)
Elements::Node_strategy = st.builds(
    Elements::Node,
)
Elements::Element_strategy = st.builds(
    Elements::Element,
    value=
        st.integers(),
    values=
        st.integers()
)
IdentifiedElement_strategy = st.builds(
    IdentifiedElement,
)
Elements::Root_strategy = st.builds(
    Elements::Root,
    name=
        safe_text
)
Elements::NamedElement_strategy = st.builds(
    Elements::NamedElement,
    name=
        safe_text
)
Elements::IdentifiedElement_strategy = st.builds(
    Elements::IdentifiedElement,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=Elements::ReferencingNode_strategy)
@settings(max_examples=50)
def test_elements::referencingnode_instantiation(instance):
    assert isinstance(instance, Elements::ReferencingNode)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Elements::StrictElement_strategy)
@settings(max_examples=50)
def test_elements::strictelement_instantiation(instance):
    assert isinstance(instance, Elements::StrictElement)

@given(instance=Elements::StrictElement_strategy)
def test_elements::strictelement_sValues_type(instance):
    assert isinstance(instance.sValues, int)


@given(instance=Elements::StrictElement_strategy)
def test_elements::strictelement_sValues_setter(instance):
    original = instance.sValues
    instance.sValues = original
    assert instance.sValues == original

@given(instance=Elements::StrictElement_strategy)
def test_elements::strictelement_sValue_type(instance):
    assert isinstance(instance.sValue, int)


@given(instance=Elements::StrictElement_strategy)
def test_elements::strictelement_sValue_setter(instance):
    original = instance.sValue
    instance.sValue = original
    assert instance.sValue == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Elements::Edge_strategy)
@settings(max_examples=50)
def test_elements::edge_instantiation(instance):
    assert isinstance(instance, Elements::Edge)

@given(instance=Elements::Node_strategy)
@settings(max_examples=50)
def test_elements::node_instantiation(instance):
    assert isinstance(instance, Elements::Node)

@given(instance=Elements::Element_strategy)
@settings(max_examples=50)
def test_elements::element_instantiation(instance):
    assert isinstance(instance, Elements::Element)

@given(instance=Elements::Element_strategy)
def test_elements::element_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=Elements::Element_strategy)
def test_elements::element_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Elements::Element_strategy)
def test_elements::element_values_type(instance):
    assert isinstance(instance.values, int)


@given(instance=Elements::Element_strategy)
def test_elements::element_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=IdentifiedElement_strategy)
@settings(max_examples=50)
def test_identifiedelement_instantiation(instance):
    assert isinstance(instance, IdentifiedElement)

@given(instance=Elements::Root_strategy)
@settings(max_examples=50)
def test_elements::root_instantiation(instance):
    assert isinstance(instance, Elements::Root)

@given(instance=Elements::Root_strategy)
def test_elements::root_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Elements::Root_strategy)
def test_elements::root_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Elements::NamedElement_strategy)
@settings(max_examples=50)
def test_elements::namedelement_instantiation(instance):
    assert isinstance(instance, Elements::NamedElement)

@given(instance=Elements::NamedElement_strategy)
def test_elements::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Elements::NamedElement_strategy)
def test_elements::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Elements::IdentifiedElement_strategy)
@settings(max_examples=50)
def test_elements::identifiedelement_instantiation(instance):
    assert isinstance(instance, Elements::IdentifiedElement)

@given(instance=Elements::IdentifiedElement_strategy)
def test_elements::identifiedelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Elements::IdentifiedElement_strategy)
def test_elements::identifiedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
