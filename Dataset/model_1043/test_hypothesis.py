import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    MetaModel::State,
    MetaModel::Operation,
    MetaModel::InitialState,
    MetaModel::Transition,
    MetaModel::EvolutionStyle,
    MetaModel::FinalState,
    MetaModel::IntermidiateState,
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



def test_metamodel::state_is_not_abstract():
    assert not inspect.isabstract(MetaModel::State)


def test_metamodel::state_constructor_exists():
    assert callable(MetaModel::State.__init__)


def test_metamodel::state_constructor_args():
    sig = inspect.signature(MetaModel::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::state_has_name():
    assert hasattr(MetaModel::State, "name")
    descriptor = None
    for klass in MetaModel::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::operation_is_not_abstract():
    assert not inspect.isabstract(MetaModel::Operation)


def test_metamodel::operation_constructor_exists():
    assert callable(MetaModel::Operation.__init__)


def test_metamodel::operation_constructor_args():
    sig = inspect.signature(MetaModel::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "name" in params, "Missing parameter 'name'"
    assert "cost" in params, "Missing parameter 'cost'"

def test_metamodel::operation_has_time():
    assert hasattr(MetaModel::Operation, "time")
    descriptor = None
    for klass in MetaModel::Operation.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::operation_has_name():
    assert hasattr(MetaModel::Operation, "name")
    descriptor = None
    for klass in MetaModel::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::operation_has_cost():
    assert hasattr(MetaModel::Operation, "cost")
    descriptor = None
    for klass in MetaModel::Operation.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::initialstate_is_not_abstract():
    assert not inspect.isabstract(MetaModel::InitialState)


def test_metamodel::initialstate_constructor_exists():
    assert callable(MetaModel::InitialState.__init__)


def test_metamodel::initialstate_constructor_args():
    sig = inspect.signature(MetaModel::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::transition_is_not_abstract():
    assert not inspect.isabstract(MetaModel::Transition)


def test_metamodel::transition_constructor_exists():
    assert callable(MetaModel::Transition.__init__)


def test_metamodel::transition_constructor_args():
    sig = inspect.signature(MetaModel::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_metamodel::transition_has_name():
    assert hasattr(MetaModel::Transition, "name")
    descriptor = None
    for klass in MetaModel::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodel::transition_has_description():
    assert hasattr(MetaModel::Transition, "description")
    descriptor = None
    for klass in MetaModel::Transition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::evolutionstyle_is_not_abstract():
    assert not inspect.isabstract(MetaModel::EvolutionStyle)


def test_metamodel::evolutionstyle_constructor_exists():
    assert callable(MetaModel::EvolutionStyle.__init__)


def test_metamodel::evolutionstyle_constructor_args():
    sig = inspect.signature(MetaModel::EvolutionStyle.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodel::evolutionstyle_has_name():
    assert hasattr(MetaModel::EvolutionStyle, "name")
    descriptor = None
    for klass in MetaModel::EvolutionStyle.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodel::finalstate_is_not_abstract():
    assert not inspect.isabstract(MetaModel::FinalState)


def test_metamodel::finalstate_constructor_exists():
    assert callable(MetaModel::FinalState.__init__)


def test_metamodel::finalstate_constructor_args():
    sig = inspect.signature(MetaModel::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_metamodel::intermidiatestate_is_not_abstract():
    assert not inspect.isabstract(MetaModel::IntermidiateState)


def test_metamodel::intermidiatestate_constructor_exists():
    assert callable(MetaModel::IntermidiateState.__init__)


def test_metamodel::intermidiatestate_constructor_args():
    sig = inspect.signature(MetaModel::IntermidiateState.__init__)
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
MetaModel::State_strategy = st.builds(
    MetaModel::State,
    name=
        safe_text
)
MetaModel::Operation_strategy = st.builds(
    MetaModel::Operation,
    time=
        safe_text,
    name=
        safe_text,
    cost=
        safe_text
)
MetaModel::InitialState_strategy = st.builds(
    MetaModel::InitialState,
)
MetaModel::Transition_strategy = st.builds(
    MetaModel::Transition,
    name=
        safe_text,
    description=
        safe_text
)
MetaModel::EvolutionStyle_strategy = st.builds(
    MetaModel::EvolutionStyle,
    name=
        safe_text
)
MetaModel::FinalState_strategy = st.builds(
    MetaModel::FinalState,
)
MetaModel::IntermidiateState_strategy = st.builds(
    MetaModel::IntermidiateState,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=MetaModel::State_strategy)
@settings(max_examples=50)
def test_metamodel::state_instantiation(instance):
    assert isinstance(instance, MetaModel::State)

@given(instance=MetaModel::State_strategy)
def test_metamodel::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetaModel::State_strategy)
def test_metamodel::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel::Operation_strategy)
@settings(max_examples=50)
def test_metamodel::operation_instantiation(instance):
    assert isinstance(instance, MetaModel::Operation)

@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_cost_type(instance):
    assert isinstance(instance.cost, str)


@given(instance=MetaModel::Operation_strategy)
def test_metamodel::operation_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=MetaModel::InitialState_strategy)
@settings(max_examples=50)
def test_metamodel::initialstate_instantiation(instance):
    assert isinstance(instance, MetaModel::InitialState)

@given(instance=MetaModel::Transition_strategy)
@settings(max_examples=50)
def test_metamodel::transition_instantiation(instance):
    assert isinstance(instance, MetaModel::Transition)

@given(instance=MetaModel::Transition_strategy)
def test_metamodel::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetaModel::Transition_strategy)
def test_metamodel::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel::Transition_strategy)
def test_metamodel::transition_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MetaModel::Transition_strategy)
def test_metamodel::transition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MetaModel::EvolutionStyle_strategy)
@settings(max_examples=50)
def test_metamodel::evolutionstyle_instantiation(instance):
    assert isinstance(instance, MetaModel::EvolutionStyle)

@given(instance=MetaModel::EvolutionStyle_strategy)
def test_metamodel::evolutionstyle_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MetaModel::EvolutionStyle_strategy)
def test_metamodel::evolutionstyle_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MetaModel::FinalState_strategy)
@settings(max_examples=50)
def test_metamodel::finalstate_instantiation(instance):
    assert isinstance(instance, MetaModel::FinalState)

@given(instance=MetaModel::IntermidiateState_strategy)
@settings(max_examples=50)
def test_metamodel::intermidiatestate_instantiation(instance):
    assert isinstance(instance, MetaModel::IntermidiateState)
