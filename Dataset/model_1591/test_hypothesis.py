import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet101::Token,
    Node,
    petrinet101::Transition,
    petrinet101::Place,
    petrinet101::Arc,
    petrinet101::Node,
    petrinet101::Petrinet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet101::token_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Token)


def test_petrinet101::token_constructor_exists():
    assert callable(petrinet101::Token.__init__)


def test_petrinet101::token_constructor_args():
    sig = inspect.signature(petrinet101::Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Transition)


def test_petrinet101::transition_constructor_exists():
    assert callable(petrinet101::Transition.__init__)


def test_petrinet101::transition_constructor_args():
    sig = inspect.signature(petrinet101::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101::place_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Place)


def test_petrinet101::place_constructor_exists():
    assert callable(petrinet101::Place.__init__)


def test_petrinet101::place_constructor_args():
    sig = inspect.signature(petrinet101::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Arc)


def test_petrinet101::arc_constructor_exists():
    assert callable(petrinet101::Arc.__init__)


def test_petrinet101::arc_constructor_args():
    sig = inspect.signature(petrinet101::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101::node_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Node)


def test_petrinet101::node_constructor_exists():
    assert callable(petrinet101::Node.__init__)


def test_petrinet101::node_constructor_args():
    sig = inspect.signature(petrinet101::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet101::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet101::Petrinet)


def test_petrinet101::petrinet_constructor_exists():
    assert callable(petrinet101::Petrinet.__init__)


def test_petrinet101::petrinet_constructor_args():
    sig = inspect.signature(petrinet101::Petrinet.__init__)
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
petrinet101::Token_strategy = st.builds(
    petrinet101::Token,
)
Node_strategy = st.builds(
    Node,
)
petrinet101::Transition_strategy = st.builds(
    petrinet101::Transition,
)
petrinet101::Place_strategy = st.builds(
    petrinet101::Place,
)
petrinet101::Arc_strategy = st.builds(
    petrinet101::Arc,
)
petrinet101::Node_strategy = st.builds(
    petrinet101::Node,
)
petrinet101::Petrinet_strategy = st.builds(
    petrinet101::Petrinet,
)

@given(instance=petrinet101::Token_strategy)
@settings(max_examples=50)
def test_petrinet101::token_instantiation(instance):
    assert isinstance(instance, petrinet101::Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet101::Transition_strategy)
@settings(max_examples=50)
def test_petrinet101::transition_instantiation(instance):
    assert isinstance(instance, petrinet101::Transition)

@given(instance=petrinet101::Place_strategy)
@settings(max_examples=50)
def test_petrinet101::place_instantiation(instance):
    assert isinstance(instance, petrinet101::Place)

@given(instance=petrinet101::Arc_strategy)
@settings(max_examples=50)
def test_petrinet101::arc_instantiation(instance):
    assert isinstance(instance, petrinet101::Arc)

@given(instance=petrinet101::Node_strategy)
@settings(max_examples=50)
def test_petrinet101::node_instantiation(instance):
    assert isinstance(instance, petrinet101::Node)

@given(instance=petrinet101::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet101::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet101::Petrinet)
