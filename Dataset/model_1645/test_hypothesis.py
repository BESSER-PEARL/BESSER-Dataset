import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    kiamaas::Num,
    kiamaas::Plus,
    kiamaas::Node,
    kiamaas::Top,
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



def test_kiamaas::num_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Num)


def test_kiamaas::num_constructor_exists():
    assert callable(kiamaas::Num.__init__)


def test_kiamaas::num_constructor_args():
    sig = inspect.signature(kiamaas::Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kiamaas::num_has_value():
    assert hasattr(kiamaas::Num, "value")
    descriptor = None
    for klass in kiamaas::Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas::plus_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Plus)


def test_kiamaas::plus_constructor_exists():
    assert callable(kiamaas::Plus.__init__)


def test_kiamaas::plus_constructor_args():
    sig = inspect.signature(kiamaas::Plus.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas::node_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Node)


def test_kiamaas::node_constructor_exists():
    assert callable(kiamaas::Node.__init__)


def test_kiamaas::node_constructor_args():
    sig = inspect.signature(kiamaas::Node.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "deep" in params, "Missing parameter 'deep'"

def test_kiamaas::node_has_height():
    assert hasattr(kiamaas::Node, "height")
    descriptor = None
    for klass in kiamaas::Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_kiamaas::node_has_deep():
    assert hasattr(kiamaas::Node, "deep")
    descriptor = None
    for klass in kiamaas::Node.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas::top_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Top)


def test_kiamaas::top_constructor_exists():
    assert callable(kiamaas::Top.__init__)


def test_kiamaas::top_constructor_args():
    sig = inspect.signature(kiamaas::Top.__init__)
    params = list(sig.parameters.keys())


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
kiamaas::Num_strategy = st.builds(
    kiamaas::Num,
    value=
        st.integers()
)
kiamaas::Plus_strategy = st.builds(
    kiamaas::Plus,
)
kiamaas::Node_strategy = st.builds(
    kiamaas::Node,
    height=
        st.integers(),
    deep=
        st.integers()
)
kiamaas::Top_strategy = st.builds(
    kiamaas::Top,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=kiamaas::Num_strategy)
@settings(max_examples=50)
def test_kiamaas::num_instantiation(instance):
    assert isinstance(instance, kiamaas::Num)

@given(instance=kiamaas::Num_strategy)
def test_kiamaas::num_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=kiamaas::Num_strategy)
def test_kiamaas::num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kiamaas::Plus_strategy)
@settings(max_examples=50)
def test_kiamaas::plus_instantiation(instance):
    assert isinstance(instance, kiamaas::Plus)

@given(instance=kiamaas::Node_strategy)
@settings(max_examples=50)
def test_kiamaas::node_instantiation(instance):
    assert isinstance(instance, kiamaas::Node)

@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_deep_type(instance):
    assert isinstance(instance.deep, int)


@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=kiamaas::Top_strategy)
@settings(max_examples=50)
def test_kiamaas::top_instantiation(instance):
    assert isinstance(instance, kiamaas::Top)
