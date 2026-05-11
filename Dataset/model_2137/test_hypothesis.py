import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    transitiongraph::Transition,
    transitiongraph::State,
    transitiongraph::TransitionGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transitiongraph::transition_is_not_abstract():
    assert not inspect.isabstract(transitiongraph::Transition)


def test_transitiongraph::transition_constructor_exists():
    assert callable(transitiongraph::Transition.__init__)


def test_transitiongraph::transition_constructor_args():
    sig = inspect.signature(transitiongraph::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "label" in params, "Missing parameter 'label'"

def test_transitiongraph::transition_has_probability():
    assert hasattr(transitiongraph::Transition, "probability")
    descriptor = None
    for klass in transitiongraph::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph::transition_has_label():
    assert hasattr(transitiongraph::Transition, "label")
    descriptor = None
    for klass in transitiongraph::Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_transitiongraph::state_is_not_abstract():
    assert not inspect.isabstract(transitiongraph::State)


def test_transitiongraph::state_constructor_exists():
    assert callable(transitiongraph::State.__init__)


def test_transitiongraph::state_constructor_args():
    sig = inspect.signature(transitiongraph::State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "id" in params, "Missing parameter 'id'"

def test_transitiongraph::state_has_isInitial():
    assert hasattr(transitiongraph::State, "isInitial")
    descriptor = None
    for klass in transitiongraph::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph::state_has_isFinal():
    assert hasattr(transitiongraph::State, "isFinal")
    descriptor = None
    for klass in transitiongraph::State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph::state_has_id():
    assert hasattr(transitiongraph::State, "id")
    descriptor = None
    for klass in transitiongraph::State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_transitiongraph::transitiongraph_is_not_abstract():
    assert not inspect.isabstract(transitiongraph::TransitionGraph)


def test_transitiongraph::transitiongraph_constructor_exists():
    assert callable(transitiongraph::TransitionGraph.__init__)


def test_transitiongraph::transitiongraph_constructor_args():
    sig = inspect.signature(transitiongraph::TransitionGraph.__init__)
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
transitiongraph::Transition_strategy = st.builds(
    transitiongraph::Transition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    label=
        safe_text
)
transitiongraph::State_strategy = st.builds(
    transitiongraph::State,
    isInitial=
        st.booleans(),
    isFinal=
        st.booleans(),
    id=
        st.integers()
)
transitiongraph::TransitionGraph_strategy = st.builds(
    transitiongraph::TransitionGraph,
)

@given(instance=transitiongraph::Transition_strategy)
@settings(max_examples=50)
def test_transitiongraph::transition_instantiation(instance):
    assert isinstance(instance, transitiongraph::Transition)

@given(instance=transitiongraph::Transition_strategy)
def test_transitiongraph::transition_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=transitiongraph::Transition_strategy)
def test_transitiongraph::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=transitiongraph::Transition_strategy)
def test_transitiongraph::transition_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=transitiongraph::Transition_strategy)
def test_transitiongraph::transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=transitiongraph::State_strategy)
@settings(max_examples=50)
def test_transitiongraph::state_instantiation(instance):
    assert isinstance(instance, transitiongraph::State)

@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=transitiongraph::State_strategy)
def test_transitiongraph::state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=transitiongraph::TransitionGraph_strategy)
@settings(max_examples=50)
def test_transitiongraph::transitiongraph_instantiation(instance):
    assert isinstance(instance, transitiongraph::TransitionGraph)
