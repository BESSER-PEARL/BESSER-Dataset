import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::Token,
    Node,
    petrinet::Place,
    petrinet::Transition,
    petrinet::Arc,
    petrinet::Node,
    petrinet::Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(petrinet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(petrinet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(petrinet::Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(petrinet::Node, "name")
    descriptor = None
    for klass in petrinet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::Petrinet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::Petrinet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petrinet::Petrinet, "name")
    descriptor = None
    for klass in petrinet::Petrinet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
petrinet::Token_strategy = st.builds(
    petrinet::Token,
)
Node_strategy = st.builds(
    Node,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
    name=
        safe_text
)
petrinet::Petrinet_strategy = st.builds(
    petrinet::Petrinet,
    name=
        safe_text
)

@given(instance=petrinet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, petrinet::Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::Petrinet)

@given(instance=petrinet::Petrinet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Petrinet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
