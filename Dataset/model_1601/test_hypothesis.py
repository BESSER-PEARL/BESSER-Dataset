import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stochasticpetrinet::Arc,
    Node,
    stochasticpetrinet::Place,
    stochasticpetrinet::Transition,
    stochasticpetrinet::Node,
    stochasticpetrinet::PetriNet,
    Transition,
    stochasticpetrinet::ImmediateTransition,
    stochasticpetrinet::TimedTransition,
    ArcKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stochasticpetrinet::arc_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::Arc)


def test_stochasticpetrinet::arc_constructor_exists():
    assert callable(stochasticpetrinet::Arc.__init__)


def test_stochasticpetrinet::arc_constructor_args():
    sig = inspect.signature(stochasticpetrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_stochasticpetrinet::arc_has_kind():
    assert hasattr(stochasticpetrinet::Arc, "kind")
    descriptor = None
    for klass in stochasticpetrinet::Arc.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet::place_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::Place)


def test_stochasticpetrinet::place_constructor_exists():
    assert callable(stochasticpetrinet::Place.__init__)


def test_stochasticpetrinet::place_constructor_args():
    sig = inspect.signature(stochasticpetrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_stochasticpetrinet::place_has_tokens():
    assert hasattr(stochasticpetrinet::Place, "tokens")
    descriptor = None
    for klass in stochasticpetrinet::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_stochasticpetrinet::transition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::Transition)


def test_stochasticpetrinet::transition_constructor_exists():
    assert callable(stochasticpetrinet::Transition.__init__)


def test_stochasticpetrinet::transition_constructor_args():
    sig = inspect.signature(stochasticpetrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet::node_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::Node)


def test_stochasticpetrinet::node_constructor_exists():
    assert callable(stochasticpetrinet::Node.__init__)


def test_stochasticpetrinet::node_constructor_args():
    sig = inspect.signature(stochasticpetrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::PetriNet)


def test_stochasticpetrinet::petrinet_constructor_exists():
    assert callable(stochasticpetrinet::PetriNet.__init__)


def test_stochasticpetrinet::petrinet_constructor_args():
    sig = inspect.signature(stochasticpetrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet::immediatetransition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::ImmediateTransition)


def test_stochasticpetrinet::immediatetransition_constructor_exists():
    assert callable(stochasticpetrinet::ImmediateTransition.__init__)


def test_stochasticpetrinet::immediatetransition_constructor_args():
    sig = inspect.signature(stochasticpetrinet::ImmediateTransition.__init__)
    params = list(sig.parameters.keys())



def test_stochasticpetrinet::timedtransition_is_not_abstract():
    assert not inspect.isabstract(stochasticpetrinet::TimedTransition)


def test_stochasticpetrinet::timedtransition_constructor_exists():
    assert callable(stochasticpetrinet::TimedTransition.__init__)


def test_stochasticpetrinet::timedtransition_constructor_args():
    sig = inspect.signature(stochasticpetrinet::TimedTransition.__init__)
    params = list(sig.parameters.keys())

def test_arckind_exists():
    # Check that the Enumeration exists
    assert ArcKind is not None

def test_arckind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArcKind]
    expected_literals = [
        "INPUT",
        "OUTPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArcKind"


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
stochasticpetrinet::Arc_strategy = st.builds(
    stochasticpetrinet::Arc,
    kind=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
stochasticpetrinet::Place_strategy = st.builds(
    stochasticpetrinet::Place,
    tokens=
        st.integers()
)
stochasticpetrinet::Transition_strategy = st.builds(
    stochasticpetrinet::Transition,
)
stochasticpetrinet::Node_strategy = st.builds(
    stochasticpetrinet::Node,
)
stochasticpetrinet::PetriNet_strategy = st.builds(
    stochasticpetrinet::PetriNet,
)
Transition_strategy = st.builds(
    Transition,
)
stochasticpetrinet::ImmediateTransition_strategy = st.builds(
    stochasticpetrinet::ImmediateTransition,
)
stochasticpetrinet::TimedTransition_strategy = st.builds(
    stochasticpetrinet::TimedTransition,
)

@given(instance=stochasticpetrinet::Arc_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::arc_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::Arc)

@given(instance=stochasticpetrinet::Arc_strategy)
def test_stochasticpetrinet::arc_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=stochasticpetrinet::Arc_strategy)
def test_stochasticpetrinet::arc_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=stochasticpetrinet::Place_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::place_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::Place)

@given(instance=stochasticpetrinet::Place_strategy)
def test_stochasticpetrinet::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=stochasticpetrinet::Place_strategy)
def test_stochasticpetrinet::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=stochasticpetrinet::Transition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::transition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::Transition)

@given(instance=stochasticpetrinet::Node_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::node_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::Node)

@given(instance=stochasticpetrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::petrinet_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::PetriNet)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=stochasticpetrinet::ImmediateTransition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::immediatetransition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::ImmediateTransition)

@given(instance=stochasticpetrinet::TimedTransition_strategy)
@settings(max_examples=50)
def test_stochasticpetrinet::timedtransition_instantiation(instance):
    assert isinstance(instance, stochasticpetrinet::TimedTransition)
