import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    markov::Label,
    Entity,
    markov::Transition,
    markov::State,
    markov::Entity,
    markov::MarkovChain,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_markov::label_is_not_abstract():
    assert not inspect.isabstract(markov::Label)


def test_markov::label_constructor_exists():
    assert callable(markov::Label.__init__)


def test_markov::label_constructor_args():
    sig = inspect.signature(markov::Label.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_markov::label_has_value():
    assert hasattr(markov::Label, "value")
    descriptor = None
    for klass in markov::Label.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_markov::label_has_key():
    assert hasattr(markov::Label, "key")
    descriptor = None
    for klass in markov::Label.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_markov::transition_is_not_abstract():
    assert not inspect.isabstract(markov::Transition)


def test_markov::transition_constructor_exists():
    assert callable(markov::Transition.__init__)


def test_markov::transition_constructor_args():
    sig = inspect.signature(markov::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_markov::transition_has_probability():
    assert hasattr(markov::Transition, "probability")
    descriptor = None
    for klass in markov::Transition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_markov::state_is_not_abstract():
    assert not inspect.isabstract(markov::State)


def test_markov::state_constructor_exists():
    assert callable(markov::State.__init__)


def test_markov::state_constructor_args():
    sig = inspect.signature(markov::State.__init__)
    params = list(sig.parameters.keys())
    assert "traces" in params, "Missing parameter 'traces'"
    assert "type" in params, "Missing parameter 'type'"

def test_markov::state_has_traces():
    assert hasattr(markov::State, "traces")
    descriptor = None
    for klass in markov::State.__mro__:
        if "traces" in klass.__dict__:
            descriptor = klass.__dict__["traces"]
            break
    assert isinstance(descriptor, property)

def test_markov::state_has_type():
    assert hasattr(markov::State, "type")
    descriptor = None
    for klass in markov::State.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_markov::entity_is_not_abstract():
    assert not inspect.isabstract(markov::Entity)


def test_markov::entity_constructor_exists():
    assert callable(markov::Entity.__init__)


def test_markov::entity_constructor_args():
    sig = inspect.signature(markov::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_markov::entity_has_Name():
    assert hasattr(markov::Entity, "Name")
    descriptor = None
    for klass in markov::Entity.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_markov::markovchain_is_not_abstract():
    assert not inspect.isabstract(markov::MarkovChain)


def test_markov::markovchain_constructor_exists():
    assert callable(markov::MarkovChain.__init__)


def test_markov::markovchain_constructor_args():
    sig = inspect.signature(markov::MarkovChain.__init__)
    params = list(sig.parameters.keys())

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "Default",
        "Failure",
        "Start",
        "Success",
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
markov::Label_strategy = st.builds(
    markov::Label,
    value=
        safe_text,
    key=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
markov::Transition_strategy = st.builds(
    markov::Transition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
markov::State_strategy = st.builds(
    markov::State,
    traces=
        safe_text,
    type=
        safe_text
)
markov::Entity_strategy = st.builds(
    markov::Entity,
    Name=
        safe_text
)
markov::MarkovChain_strategy = st.builds(
    markov::MarkovChain,
)

@given(instance=markov::Label_strategy)
@settings(max_examples=50)
def test_markov::label_instantiation(instance):
    assert isinstance(instance, markov::Label)

@given(instance=markov::Label_strategy)
def test_markov::label_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=markov::Label_strategy)
def test_markov::label_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=markov::Label_strategy)
def test_markov::label_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=markov::Label_strategy)
def test_markov::label_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=markov::Transition_strategy)
@settings(max_examples=50)
def test_markov::transition_instantiation(instance):
    assert isinstance(instance, markov::Transition)

@given(instance=markov::Transition_strategy)
def test_markov::transition_probability_type(instance):
    assert isinstance(instance.probability, float)


@given(instance=markov::Transition_strategy)
def test_markov::transition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=markov::State_strategy)
@settings(max_examples=50)
def test_markov::state_instantiation(instance):
    assert isinstance(instance, markov::State)

@given(instance=markov::State_strategy)
def test_markov::state_traces_type(instance):
    assert isinstance(instance.traces, str)


@given(instance=markov::State_strategy)
def test_markov::state_traces_setter(instance):
    original = instance.traces
    instance.traces = original
    assert instance.traces == original

@given(instance=markov::State_strategy)
def test_markov::state_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=markov::State_strategy)
def test_markov::state_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=markov::Entity_strategy)
@settings(max_examples=50)
def test_markov::entity_instantiation(instance):
    assert isinstance(instance, markov::Entity)

@given(instance=markov::Entity_strategy)
def test_markov::entity_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=markov::Entity_strategy)
def test_markov::entity_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=markov::MarkovChain_strategy)
@settings(max_examples=50)
def test_markov::markovchain_instantiation(instance):
    assert isinstance(instance, markov::MarkovChain)
