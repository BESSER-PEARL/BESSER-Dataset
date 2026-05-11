import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cstat1::StateChart,
    cstat1::EClass0,
    cstat1::Action,
    cstat1::AbstractState,
    cstat1::Transition,
    AbstractState,
    cstat1::SubState2,
    cstat1::State,
    cstat1::SubState1,
    ActionMode,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cstat1::statechart_is_not_abstract():
    assert not inspect.isabstract(cstat1::StateChart)


def test_cstat1::statechart_constructor_exists():
    assert callable(cstat1::StateChart.__init__)


def test_cstat1::statechart_constructor_args():
    sig = inspect.signature(cstat1::StateChart.__init__)
    params = list(sig.parameters.keys())



def test_cstat1::eclass0_is_not_abstract():
    assert not inspect.isabstract(cstat1::EClass0)


def test_cstat1::eclass0_constructor_exists():
    assert callable(cstat1::EClass0.__init__)


def test_cstat1::eclass0_constructor_args():
    sig = inspect.signature(cstat1::EClass0.__init__)
    params = list(sig.parameters.keys())



def test_cstat1::action_is_not_abstract():
    assert not inspect.isabstract(cstat1::Action)


def test_cstat1::action_constructor_exists():
    assert callable(cstat1::Action.__init__)


def test_cstat1::action_constructor_args():
    sig = inspect.signature(cstat1::Action.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_cstat1::action_has_mode():
    assert hasattr(cstat1::Action, "mode")
    descriptor = None
    for klass in cstat1::Action.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_cstat1::action_has_expression():
    assert hasattr(cstat1::Action, "expression")
    descriptor = None
    for klass in cstat1::Action.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_cstat1::abstractstate_is_not_abstract():
    assert not inspect.isabstract(cstat1::AbstractState)


def test_cstat1::abstractstate_constructor_exists():
    assert callable(cstat1::AbstractState.__init__)


def test_cstat1::abstractstate_constructor_args():
    sig = inspect.signature(cstat1::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "type" in params, "Missing parameter 'type'"

def test_cstat1::abstractstate_has_id():
    assert hasattr(cstat1::AbstractState, "id")
    descriptor = None
    for klass in cstat1::AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cstat1::abstractstate_has_type():
    assert hasattr(cstat1::AbstractState, "type")
    descriptor = None
    for klass in cstat1::AbstractState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cstat1::transition_is_not_abstract():
    assert not inspect.isabstract(cstat1::Transition)


def test_cstat1::transition_constructor_exists():
    assert callable(cstat1::Transition.__init__)


def test_cstat1::transition_constructor_args():
    sig = inspect.signature(cstat1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "guard" in params, "Missing parameter 'guard'"

def test_cstat1::transition_has_event():
    assert hasattr(cstat1::Transition, "event")
    descriptor = None
    for klass in cstat1::Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_cstat1::transition_has_guard():
    assert hasattr(cstat1::Transition, "guard")
    descriptor = None
    for klass in cstat1::Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_cstat1::substate2_is_not_abstract():
    assert not inspect.isabstract(cstat1::SubState2)


def test_cstat1::substate2_constructor_exists():
    assert callable(cstat1::SubState2.__init__)


def test_cstat1::substate2_constructor_args():
    sig = inspect.signature(cstat1::SubState2.__init__)
    params = list(sig.parameters.keys())



def test_cstat1::state_is_not_abstract():
    assert not inspect.isabstract(cstat1::State)


def test_cstat1::state_constructor_exists():
    assert callable(cstat1::State.__init__)


def test_cstat1::state_constructor_args():
    sig = inspect.signature(cstat1::State.__init__)
    params = list(sig.parameters.keys())



def test_cstat1::substate1_is_not_abstract():
    assert not inspect.isabstract(cstat1::SubState1)


def test_cstat1::substate1_constructor_exists():
    assert callable(cstat1::SubState1.__init__)


def test_cstat1::substate1_constructor_args():
    sig = inspect.signature(cstat1::SubState1.__init__)
    params = list(sig.parameters.keys())

def test_actionmode_exists():
    # Check that the Enumeration exists
    assert ActionMode is not None

def test_actionmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionMode]
    expected_literals = [
        "EXIT",
        "ENTRY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionMode"

def test_statetype_exists():
    # Check that the Enumeration exists
    assert StateType is not None

def test_statetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateType]
    expected_literals = [
        "INITIAL",
        "SIMPLE",
        "FINAL",
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
cstat1::StateChart_strategy = st.builds(
    cstat1::StateChart,
)
cstat1::EClass0_strategy = st.builds(
    cstat1::EClass0,
)
cstat1::Action_strategy = st.builds(
    cstat1::Action,
    mode=
        safe_text,
    expression=
        safe_text
)
cstat1::AbstractState_strategy = st.builds(
    cstat1::AbstractState,
    id=
        safe_text,
    type=
        safe_text
)
cstat1::Transition_strategy = st.builds(
    cstat1::Transition,
    event=
        safe_text,
    guard=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
cstat1::SubState2_strategy = st.builds(
    cstat1::SubState2,
)
cstat1::State_strategy = st.builds(
    cstat1::State,
)
cstat1::SubState1_strategy = st.builds(
    cstat1::SubState1,
)

@given(instance=cstat1::StateChart_strategy)
@settings(max_examples=50)
def test_cstat1::statechart_instantiation(instance):
    assert isinstance(instance, cstat1::StateChart)

@given(instance=cstat1::EClass0_strategy)
@settings(max_examples=50)
def test_cstat1::eclass0_instantiation(instance):
    assert isinstance(instance, cstat1::EClass0)

@given(instance=cstat1::Action_strategy)
@settings(max_examples=50)
def test_cstat1::action_instantiation(instance):
    assert isinstance(instance, cstat1::Action)

@given(instance=cstat1::Action_strategy)
def test_cstat1::action_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=cstat1::Action_strategy)
def test_cstat1::action_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=cstat1::Action_strategy)
def test_cstat1::action_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=cstat1::Action_strategy)
def test_cstat1::action_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=cstat1::AbstractState_strategy)
@settings(max_examples=50)
def test_cstat1::abstractstate_instantiation(instance):
    assert isinstance(instance, cstat1::AbstractState)

@given(instance=cstat1::AbstractState_strategy)
def test_cstat1::abstractstate_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=cstat1::AbstractState_strategy)
def test_cstat1::abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=cstat1::AbstractState_strategy)
def test_cstat1::abstractstate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=cstat1::AbstractState_strategy)
def test_cstat1::abstractstate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cstat1::Transition_strategy)
@settings(max_examples=50)
def test_cstat1::transition_instantiation(instance):
    assert isinstance(instance, cstat1::Transition)

@given(instance=cstat1::Transition_strategy)
def test_cstat1::transition_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=cstat1::Transition_strategy)
def test_cstat1::transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=cstat1::Transition_strategy)
def test_cstat1::transition_guard_type(instance):
    assert isinstance(instance.guard, str)


@given(instance=cstat1::Transition_strategy)
def test_cstat1::transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=cstat1::SubState2_strategy)
@settings(max_examples=50)
def test_cstat1::substate2_instantiation(instance):
    assert isinstance(instance, cstat1::SubState2)

@given(instance=cstat1::State_strategy)
@settings(max_examples=50)
def test_cstat1::state_instantiation(instance):
    assert isinstance(instance, cstat1::State)

@given(instance=cstat1::SubState1_strategy)
@settings(max_examples=50)
def test_cstat1::substate1_instantiation(instance):
    assert isinstance(instance, cstat1::SubState1)
