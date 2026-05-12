import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    MetaModel_State,
    MetaModel_Operation,
    MetaModel_InitialState,
    MetaModel_Transition,
    MetaModel_EvolutionStyle,
    MetaModel_FinalState,
    MetaModel_IntermidiateState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_state_is_not_abstract():
    assert not inspect.isabstract(MetaModel_State)


def test_metamodel_state_constructor_exists():
    assert callable(MetaModel_State.__init__)


def test_metamodel_state_constructor_args():
    sig = inspect.signature(MetaModel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_state_has_name():
    assert hasattr(MetaModel_State, "name")
    descriptor = None
    for klass in MetaModel_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_operation_is_not_abstract():
    assert not inspect.isabstract(MetaModel_Operation)


def test_metamodel_operation_constructor_exists():
    assert callable(MetaModel_Operation.__init__)


def test_metamodel_operation_constructor_args():
    sig = inspect.signature(MetaModel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_metamodel_operation_has_time():
    assert hasattr(MetaModel_Operation, "time")
    descriptor = None
    for klass in MetaModel_Operation.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_operation_has_name():
    assert hasattr(MetaModel_Operation, "name")
    descriptor = None
    for klass in MetaModel_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_operation_has_cost():
    assert hasattr(MetaModel_Operation, "cost")
    descriptor = None
    for klass in MetaModel_Operation.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_initialstate_is_not_abstract():
    assert not inspect.isabstract(MetaModel_InitialState)


def test_metamodel_initialstate_constructor_exists():
    assert callable(MetaModel_InitialState.__init__)


def test_metamodel_initialstate_constructor_args():
    sig = inspect.signature(MetaModel_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_transition_is_not_abstract():
    assert not inspect.isabstract(MetaModel_Transition)


def test_metamodel_transition_constructor_exists():
    assert callable(MetaModel_Transition.__init__)


def test_metamodel_transition_constructor_args():
    sig = inspect.signature(MetaModel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_transition_has_description():
    assert hasattr(MetaModel_Transition, "description")
    descriptor = None
    for klass in MetaModel_Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_metamodel_transition_has_name():
    assert hasattr(MetaModel_Transition, "name")
    descriptor = None
    for klass in MetaModel_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_evolutionstyle_is_not_abstract():
    assert not inspect.isabstract(MetaModel_EvolutionStyle)


def test_metamodel_evolutionstyle_constructor_exists():
    assert callable(MetaModel_EvolutionStyle.__init__)


def test_metamodel_evolutionstyle_constructor_args():
    sig = inspect.signature(MetaModel_EvolutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel_evolutionstyle_has_name():
    assert hasattr(MetaModel_EvolutionStyle, "name")
    descriptor = None
    for klass in MetaModel_EvolutionStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel_finalstate_is_not_abstract():
    assert not inspect.isabstract(MetaModel_FinalState)


def test_metamodel_finalstate_constructor_exists():
    assert callable(MetaModel_FinalState.__init__)


def test_metamodel_finalstate_constructor_args():
    sig = inspect.signature(MetaModel_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_metamodel_intermidiatestate_is_not_abstract():
    assert not inspect.isabstract(MetaModel_IntermidiateState)


def test_metamodel_intermidiatestate_constructor_exists():
    assert callable(MetaModel_IntermidiateState.__init__)


def test_metamodel_intermidiatestate_constructor_args():
    sig = inspect.signature(MetaModel_IntermidiateState.__init__)
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
State_strategy = st.builds(
    State,
)
MetaModel_State_strategy = st.builds(
    MetaModel_State,
    name=
        safe_text
)
MetaModel_Operation_strategy = st.builds(
    MetaModel_Operation,
    time=
        safe_text,
    name=
        safe_text,
    cost=
        safe_text
)
MetaModel_InitialState_strategy = st.builds(
    MetaModel_InitialState,
)
MetaModel_Transition_strategy = st.builds(
    MetaModel_Transition,
    description=
        safe_text,
    name=
        safe_text
)
MetaModel_EvolutionStyle_strategy = st.builds(
    MetaModel_EvolutionStyle,
    name=
        safe_text
)
MetaModel_FinalState_strategy = st.builds(
    MetaModel_FinalState,
)
MetaModel_IntermidiateState_strategy = st.builds(
    MetaModel_IntermidiateState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=MetaModel_State_strategy)
@settings(max_examples=50)
def test_metamodel_state_instantiation(instance):
    assert isinstance(instance, MetaModel_State)



@given(instance=MetaModel_State_strategy)
def test_metamodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel_Operation_strategy)
@settings(max_examples=50)
def test_metamodel_operation_instantiation(instance):
    assert isinstance(instance, MetaModel_Operation)



@given(instance=MetaModel_Operation_strategy)
def test_metamodel_operation_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=MetaModel_Operation_strategy)
def test_metamodel_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MetaModel_Operation_strategy)
def test_metamodel_operation_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=MetaModel_InitialState_strategy)
@settings(max_examples=50)
def test_metamodel_initialstate_instantiation(instance):
    assert isinstance(instance, MetaModel_InitialState)

@given(instance=MetaModel_Transition_strategy)
@settings(max_examples=50)
def test_metamodel_transition_instantiation(instance):
    assert isinstance(instance, MetaModel_Transition)



@given(instance=MetaModel_Transition_strategy)
def test_metamodel_transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MetaModel_Transition_strategy)
def test_metamodel_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel_EvolutionStyle_strategy)
@settings(max_examples=50)
def test_metamodel_evolutionstyle_instantiation(instance):
    assert isinstance(instance, MetaModel_EvolutionStyle)



@given(instance=MetaModel_EvolutionStyle_strategy)
def test_metamodel_evolutionstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel_FinalState_strategy)
@settings(max_examples=50)
def test_metamodel_finalstate_instantiation(instance):
    assert isinstance(instance, MetaModel_FinalState)

@given(instance=MetaModel_IntermidiateState_strategy)
@settings(max_examples=50)
def test_metamodel_intermidiatestate_instantiation(instance):
    assert isinstance(instance, MetaModel_IntermidiateState)
