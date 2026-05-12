import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cstat1_StateChart,
    cstat1_EClass0,
    cstat1_Action,
    cstat1_AbstractState,
    cstat1_Transition,
    AbstractState,
    cstat1_SubState2,
    cstat1_State,
    cstat1_SubState1,
    ActionMode,
    StateType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cstat1_statechart_is_not_abstract():
    assert not inspect.isabstract(cstat1_StateChart)


def test_cstat1_statechart_constructor_exists():
    assert callable(cstat1_StateChart.__init__)


def test_cstat1_statechart_constructor_args():
    sig = inspect.signature(cstat1_StateChart.__init__)
    params = list(sig.parameters.keys())



def test_cstat1_eclass0_is_not_abstract():
    assert not inspect.isabstract(cstat1_EClass0)


def test_cstat1_eclass0_constructor_exists():
    assert callable(cstat1_EClass0.__init__)


def test_cstat1_eclass0_constructor_args():
    sig = inspect.signature(cstat1_EClass0.__init__)
    params = list(sig.parameters.keys())



def test_cstat1_action_is_not_abstract():
    assert not inspect.isabstract(cstat1_Action)


def test_cstat1_action_constructor_exists():
    assert callable(cstat1_Action.__init__)


def test_cstat1_action_constructor_args():
    sig = inspect.signature(cstat1_Action.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "expression" in params, "Missing parameter 'expression'"

def test_cstat1_action_has_mode():
    assert hasattr(cstat1_Action, "mode")
    descriptor = None
    for klass in cstat1_Action.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_cstat1_action_has_expression():
    assert hasattr(cstat1_Action, "expression")
    descriptor = None
    for klass in cstat1_Action.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_cstat1_abstractstate_is_not_abstract():
    assert not inspect.isabstract(cstat1_AbstractState)


def test_cstat1_abstractstate_constructor_exists():
    assert callable(cstat1_AbstractState.__init__)


def test_cstat1_abstractstate_constructor_args():
    sig = inspect.signature(cstat1_AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_cstat1_abstractstate_has_type():
    assert hasattr(cstat1_AbstractState, "type")
    descriptor = None
    for klass in cstat1_AbstractState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cstat1_abstractstate_has_id():
    assert hasattr(cstat1_AbstractState, "id")
    descriptor = None
    for klass in cstat1_AbstractState.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cstat1_transition_is_not_abstract():
    assert not inspect.isabstract(cstat1_Transition)


def test_cstat1_transition_constructor_exists():
    assert callable(cstat1_Transition.__init__)


def test_cstat1_transition_constructor_args():
    sig = inspect.signature(cstat1_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "guard" in params, "Missing parameter 'guard'"

def test_cstat1_transition_has_event():
    assert hasattr(cstat1_Transition, "event")
    descriptor = None
    for klass in cstat1_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_cstat1_transition_has_guard():
    assert hasattr(cstat1_Transition, "guard")
    descriptor = None
    for klass in cstat1_Transition.__mro__:
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



def test_cstat1_substate2_is_not_abstract():
    assert not inspect.isabstract(cstat1_SubState2)


def test_cstat1_substate2_constructor_exists():
    assert callable(cstat1_SubState2.__init__)


def test_cstat1_substate2_constructor_args():
    sig = inspect.signature(cstat1_SubState2.__init__)
    params = list(sig.parameters.keys())



def test_cstat1_state_is_not_abstract():
    assert not inspect.isabstract(cstat1_State)


def test_cstat1_state_constructor_exists():
    assert callable(cstat1_State.__init__)


def test_cstat1_state_constructor_args():
    sig = inspect.signature(cstat1_State.__init__)
    params = list(sig.parameters.keys())



def test_cstat1_substate1_is_not_abstract():
    assert not inspect.isabstract(cstat1_SubState1)


def test_cstat1_substate1_constructor_exists():
    assert callable(cstat1_SubState1.__init__)


def test_cstat1_substate1_constructor_args():
    sig = inspect.signature(cstat1_SubState1.__init__)
    params = list(sig.parameters.keys())

def test_actionmode_exists():
    # Check that the Enumeration exists
    assert ActionMode is not None

def test_actionmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionMode]
    expected_literals = [
        "ENTRY",
        "EXIT",
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
        "SIMPLE",
        "FINAL",
        "INITIAL",
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
cstat1_StateChart_strategy = st.builds(
    cstat1_StateChart,
)
cstat1_EClass0_strategy = st.builds(
    cstat1_EClass0,
)
cstat1_Action_strategy = st.builds(
    cstat1_Action,
    mode=
        safe_text,
    expression=
        safe_text
)
cstat1_AbstractState_strategy = st.builds(
    cstat1_AbstractState,
    type=
        safe_text,
    id=
        safe_text
)
cstat1_Transition_strategy = st.builds(
    cstat1_Transition,
    event=
        safe_text,
    guard=
        safe_text
)
AbstractState_strategy = st.builds(
    AbstractState,
)
cstat1_SubState2_strategy = st.builds(
    cstat1_SubState2,
)
cstat1_State_strategy = st.builds(
    cstat1_State,
)
cstat1_SubState1_strategy = st.builds(
    cstat1_SubState1,
)

@given(instance=cstat1_StateChart_strategy)
@settings(max_examples=50)
def test_cstat1_statechart_instantiation(instance):
    assert isinstance(instance, cstat1_StateChart)

@given(instance=cstat1_EClass0_strategy)
@settings(max_examples=50)
def test_cstat1_eclass0_instantiation(instance):
    assert isinstance(instance, cstat1_EClass0)

@given(instance=cstat1_Action_strategy)
@settings(max_examples=50)
def test_cstat1_action_instantiation(instance):
    assert isinstance(instance, cstat1_Action)



@given(instance=cstat1_Action_strategy)
def test_cstat1_action_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=cstat1_Action_strategy)
def test_cstat1_action_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=cstat1_AbstractState_strategy)
@settings(max_examples=50)
def test_cstat1_abstractstate_instantiation(instance):
    assert isinstance(instance, cstat1_AbstractState)



@given(instance=cstat1_AbstractState_strategy)
def test_cstat1_abstractstate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=cstat1_AbstractState_strategy)
def test_cstat1_abstractstate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=cstat1_Transition_strategy)
@settings(max_examples=50)
def test_cstat1_transition_instantiation(instance):
    assert isinstance(instance, cstat1_Transition)



@given(instance=cstat1_Transition_strategy)
def test_cstat1_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=cstat1_Transition_strategy)
def test_cstat1_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=cstat1_SubState2_strategy)
@settings(max_examples=50)
def test_cstat1_substate2_instantiation(instance):
    assert isinstance(instance, cstat1_SubState2)

@given(instance=cstat1_State_strategy)
@settings(max_examples=50)
def test_cstat1_state_instantiation(instance):
    assert isinstance(instance, cstat1_State)

@given(instance=cstat1_SubState1_strategy)
@settings(max_examples=50)
def test_cstat1_substate1_instantiation(instance):
    assert isinstance(instance, cstat1_SubState1)
