import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    transitiongraph_Transition,
    transitiongraph_State,
    transitiongraph_TransitionGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_transitiongraph_transition_is_not_abstract():
    assert not inspect.isabstract(transitiongraph_Transition)


def test_transitiongraph_transition_constructor_exists():
    assert callable(transitiongraph_Transition.__init__)


def test_transitiongraph_transition_constructor_args():
    sig = inspect.signature(transitiongraph_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "label" in params, "Missing parameter 'label'"

def test_transitiongraph_transition_has_probability():
    assert hasattr(transitiongraph_Transition, "probability")
    descriptor = None
    for klass in transitiongraph_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph_transition_has_label():
    assert hasattr(transitiongraph_Transition, "label")
    descriptor = None
    for klass in transitiongraph_Transition.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_transitiongraph_state_is_not_abstract():
    assert not inspect.isabstract(transitiongraph_State)


def test_transitiongraph_state_constructor_exists():
    assert callable(transitiongraph_State.__init__)


def test_transitiongraph_state_constructor_args():
    sig = inspect.signature(transitiongraph_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "id" in params, "Missing parameter 'id'"

def test_transitiongraph_state_has_isFinal():
    assert hasattr(transitiongraph_State, "isFinal")
    descriptor = None
    for klass in transitiongraph_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph_state_has_isInitial():
    assert hasattr(transitiongraph_State, "isInitial")
    descriptor = None
    for klass in transitiongraph_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_transitiongraph_state_has_id():
    assert hasattr(transitiongraph_State, "id")
    descriptor = None
    for klass in transitiongraph_State.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_transitiongraph_transitiongraph_is_not_abstract():
    assert not inspect.isabstract(transitiongraph_TransitionGraph)


def test_transitiongraph_transitiongraph_constructor_exists():
    assert callable(transitiongraph_TransitionGraph.__init__)


def test_transitiongraph_transitiongraph_constructor_args():
    sig = inspect.signature(transitiongraph_TransitionGraph.__init__)
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
transitiongraph_Transition_strategy = st.builds(
    transitiongraph_Transition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    label=
        safe_text
)
transitiongraph_State_strategy = st.builds(
    transitiongraph_State,
    isFinal=
        st.booleans(),
    isInitial=
        st.booleans(),
    id=
        st.integers()
)
transitiongraph_TransitionGraph_strategy = st.builds(
    transitiongraph_TransitionGraph,
)

@given(instance=transitiongraph_Transition_strategy)
@settings(max_examples=50)
def test_transitiongraph_transition_instantiation(instance):
    assert isinstance(instance, transitiongraph_Transition)



@given(instance=transitiongraph_Transition_strategy)
def test_transitiongraph_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=transitiongraph_Transition_strategy)
def test_transitiongraph_transition_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=transitiongraph_State_strategy)
@settings(max_examples=50)
def test_transitiongraph_state_instantiation(instance):
    assert isinstance(instance, transitiongraph_State)



@given(instance=transitiongraph_State_strategy)
def test_transitiongraph_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=transitiongraph_State_strategy)
def test_transitiongraph_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=transitiongraph_State_strategy)
def test_transitiongraph_state_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=transitiongraph_TransitionGraph_strategy)
@settings(max_examples=50)
def test_transitiongraph_transitiongraph_instantiation(instance):
    assert isinstance(instance, transitiongraph_TransitionGraph)
