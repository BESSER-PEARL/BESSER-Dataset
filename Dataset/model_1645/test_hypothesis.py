import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    kiamaas_Num,
    kiamaas_Plus,
    kiamaas_Node,
    kiamaas_Top,
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



def test_kiamaas_num_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Num)


def test_kiamaas_num_constructor_exists():
    assert callable(kiamaas_Num.__init__)


def test_kiamaas_num_constructor_args():
    sig = inspect.signature(kiamaas_Num.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kiamaas_num_has_value():
    assert hasattr(kiamaas_Num, "value")
    descriptor = None
    for klass in kiamaas_Num.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas_plus_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Plus)


def test_kiamaas_plus_constructor_exists():
    assert callable(kiamaas_Plus.__init__)


def test_kiamaas_plus_constructor_args():
    sig = inspect.signature(kiamaas_Plus.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas_node_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Node)


def test_kiamaas_node_constructor_exists():
    assert callable(kiamaas_Node.__init__)


def test_kiamaas_node_constructor_args():
    sig = inspect.signature(kiamaas_Node.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "deep" in params, "Missing parameter 'deep'"

def test_kiamaas_node_has_height():
    assert hasattr(kiamaas_Node, "height")
    descriptor = None
    for klass in kiamaas_Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_kiamaas_node_has_deep():
    assert hasattr(kiamaas_Node, "deep")
    descriptor = None
    for klass in kiamaas_Node.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas_top_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Top)


def test_kiamaas_top_constructor_exists():
    assert callable(kiamaas_Top.__init__)


def test_kiamaas_top_constructor_args():
    sig = inspect.signature(kiamaas_Top.__init__)
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
kiamaas_Num_strategy = st.builds(
    kiamaas_Num,
    value=
        st.integers()
)
kiamaas_Plus_strategy = st.builds(
    kiamaas_Plus,
)
kiamaas_Node_strategy = st.builds(
    kiamaas_Node,
    height=
        st.integers(),
    deep=
        st.integers()
)
kiamaas_Top_strategy = st.builds(
    kiamaas_Top,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=kiamaas_Num_strategy)
@settings(max_examples=50)
def test_kiamaas_num_instantiation(instance):
    assert isinstance(instance, kiamaas_Num)



@given(instance=kiamaas_Num_strategy)
def test_kiamaas_num_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kiamaas_Plus_strategy)
@settings(max_examples=50)
def test_kiamaas_plus_instantiation(instance):
    assert isinstance(instance, kiamaas_Plus)

@given(instance=kiamaas_Node_strategy)
@settings(max_examples=50)
def test_kiamaas_node_instantiation(instance):
    assert isinstance(instance, kiamaas_Node)



@given(instance=kiamaas_Node_strategy)
def test_kiamaas_node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=kiamaas_Node_strategy)
def test_kiamaas_node_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=kiamaas_Top_strategy)
@settings(max_examples=50)
def test_kiamaas_top_instantiation(instance):
    assert isinstance(instance, kiamaas_Top)
