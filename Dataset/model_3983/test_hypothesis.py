import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    markov_Label,
    Entity,
    markov_Transition,
    markov_State,
    markov_Entity,
    markov_MarkovChain,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_markov_label_is_not_abstract():
    assert not inspect.isabstract(markov_Label)


def test_markov_label_constructor_exists():
    assert callable(markov_Label.__init__)


def test_markov_label_constructor_args():
    sig = inspect.signature(markov_Label.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_markov_label_has_key():
    assert hasattr(markov_Label, "key")
    descriptor = None
    for klass in markov_Label.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_markov_label_has_value():
    assert hasattr(markov_Label, "value")
    descriptor = None
    for klass in markov_Label.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_markov_transition_is_not_abstract():
    assert not inspect.isabstract(markov_Transition)


def test_markov_transition_constructor_exists():
    assert callable(markov_Transition.__init__)


def test_markov_transition_constructor_args():
    sig = inspect.signature(markov_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_markov_transition_has_probability():
    assert hasattr(markov_Transition, "probability")
    descriptor = None
    for klass in markov_Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_markov_state_is_not_abstract():
    assert not inspect.isabstract(markov_State)


def test_markov_state_constructor_exists():
    assert callable(markov_State.__init__)


def test_markov_state_constructor_args():
    sig = inspect.signature(markov_State.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "traces" in params, "Missing parameter 'traces'"

def test_markov_state_has_type():
    assert hasattr(markov_State, "type")
    descriptor = None
    for klass in markov_State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_markov_state_has_traces():
    assert hasattr(markov_State, "traces")
    descriptor = None
    for klass in markov_State.__mro__:
        if "traces" in klass.__dict__:
            descriptor = klass.__dict__["traces"]
            break
    assert isinstance(descriptor, property)



def test_markov_entity_is_not_abstract():
    assert not inspect.isabstract(markov_Entity)


def test_markov_entity_constructor_exists():
    assert callable(markov_Entity.__init__)


def test_markov_entity_constructor_args():
    sig = inspect.signature(markov_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_markov_entity_has_Name():
    assert hasattr(markov_Entity, "Name")
    descriptor = None
    for klass in markov_Entity.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_markov_markovchain_is_not_abstract():
    assert not inspect.isabstract(markov_MarkovChain)


def test_markov_markovchain_constructor_exists():
    assert callable(markov_MarkovChain.__init__)


def test_markov_markovchain_constructor_args():
    sig = inspect.signature(markov_MarkovChain.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "Start",
        "Default",
        "Success",
        "Failure",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateType"


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
markov_Label_strategy = st.builds(
    markov_Label,
    key=
        safe_text,
    value=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
markov_Transition_strategy = st.builds(
    markov_Transition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
markov_State_strategy = st.builds(
    markov_State,
    type=
        safe_text,
    traces=
        safe_text
)
markov_Entity_strategy = st.builds(
    markov_Entity,
    Name=
        safe_text
)
markov_MarkovChain_strategy = st.builds(
    markov_MarkovChain,
)

@given(instance=markov_Label_strategy)
@settings(max_examples=50)
def test_markov_label_instantiation(instance):
    assert isinstance(instance, markov_Label)



@given(instance=markov_Label_strategy)
def test_markov_label_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=markov_Label_strategy)
def test_markov_label_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=markov_Transition_strategy)
@settings(max_examples=50)
def test_markov_transition_instantiation(instance):
    assert isinstance(instance, markov_Transition)



@given(instance=markov_Transition_strategy)
def test_markov_transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=markov_State_strategy)
@settings(max_examples=50)
def test_markov_state_instantiation(instance):
    assert isinstance(instance, markov_State)



@given(instance=markov_State_strategy)
def test_markov_state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=markov_State_strategy)
def test_markov_state_traces_setter(instance):
    original = instance.traces
    instance.traces = original
    assert instance.traces == original

@given(instance=markov_Entity_strategy)
@settings(max_examples=50)
def test_markov_entity_instantiation(instance):
    assert isinstance(instance, markov_Entity)



@given(instance=markov_Entity_strategy)
def test_markov_entity_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=markov_MarkovChain_strategy)
@settings(max_examples=50)
def test_markov_markovchain_instantiation(instance):
    assert isinstance(instance, markov_MarkovChain)
