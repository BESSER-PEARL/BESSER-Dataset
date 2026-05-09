import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    fsm::IncreaseValueAction,
    fsm::DecreaseValueAction,
    fsm::AssignValueAction,
    NumberGuard,
    fsm::LessThanNumberGuard,
    fsm::GreaterThanNumberGuard,
    fsm::EqualNumberGuard,
    Guard,
    fsm::NumberGuard,
    Variable,
    fsm::NumberVariable,
    fsm::NamedElement,
    fsm::Action,
    fsm::Guard,
    fsm::Variable,
    NamedElement,
    fsm::State,
    fsm::Transition,
    fsm::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_fsm::increasevalueaction_is_not_abstract():
    assert not inspect.isabstract(fsm::IncreaseValueAction)


def test_fsm::increasevalueaction_constructor_exists():
    assert callable(fsm::IncreaseValueAction.__init__)


def test_fsm::increasevalueaction_constructor_args():
    sig = inspect.signature(fsm::IncreaseValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "stepValue" in params, "Missing parameter 'stepValue'"

def test_fsm::increasevalueaction_has_stepValue():
    assert hasattr(fsm::IncreaseValueAction, "stepValue")
    descriptor = None
    for klass in fsm::IncreaseValueAction.__mro__:
        if "stepValue" in klass.__dict__:
            descriptor = klass.__dict__["stepValue"]
            break
    assert isinstance(descriptor, property)



def test_fsm::decreasevalueaction_is_not_abstract():
    assert not inspect.isabstract(fsm::DecreaseValueAction)


def test_fsm::decreasevalueaction_constructor_exists():
    assert callable(fsm::DecreaseValueAction.__init__)


def test_fsm::decreasevalueaction_constructor_args():
    sig = inspect.signature(fsm::DecreaseValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "stepValue" in params, "Missing parameter 'stepValue'"

def test_fsm::decreasevalueaction_has_stepValue():
    assert hasattr(fsm::DecreaseValueAction, "stepValue")
    descriptor = None
    for klass in fsm::DecreaseValueAction.__mro__:
        if "stepValue" in klass.__dict__:
            descriptor = klass.__dict__["stepValue"]
            break
    assert isinstance(descriptor, property)



def test_fsm::assignvalueaction_is_not_abstract():
    assert not inspect.isabstract(fsm::AssignValueAction)


def test_fsm::assignvalueaction_constructor_exists():
    assert callable(fsm::AssignValueAction.__init__)


def test_fsm::assignvalueaction_constructor_args():
    sig = inspect.signature(fsm::AssignValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::assignvalueaction_has_value():
    assert hasattr(fsm::AssignValueAction, "value")
    descriptor = None
    for klass in fsm::AssignValueAction.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numberguard_is_not_abstract():
    assert not inspect.isabstract(NumberGuard)


def test_numberguard_constructor_exists():
    assert callable(NumberGuard.__init__)


def test_numberguard_constructor_args():
    sig = inspect.signature(NumberGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsm::lessthannumberguard_is_not_abstract():
    assert not inspect.isabstract(fsm::LessThanNumberGuard)


def test_fsm::lessthannumberguard_constructor_exists():
    assert callable(fsm::LessThanNumberGuard.__init__)


def test_fsm::lessthannumberguard_constructor_args():
    sig = inspect.signature(fsm::LessThanNumberGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsm::greaterthannumberguard_is_not_abstract():
    assert not inspect.isabstract(fsm::GreaterThanNumberGuard)


def test_fsm::greaterthannumberguard_constructor_exists():
    assert callable(fsm::GreaterThanNumberGuard.__init__)


def test_fsm::greaterthannumberguard_constructor_args():
    sig = inspect.signature(fsm::GreaterThanNumberGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsm::equalnumberguard_is_not_abstract():
    assert not inspect.isabstract(fsm::EqualNumberGuard)


def test_fsm::equalnumberguard_constructor_exists():
    assert callable(fsm::EqualNumberGuard.__init__)


def test_fsm::equalnumberguard_constructor_args():
    sig = inspect.signature(fsm::EqualNumberGuard.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_fsm::numberguard_is_not_abstract():
    assert not inspect.isabstract(fsm::NumberGuard)


def test_fsm::numberguard_constructor_exists():
    assert callable(fsm::NumberGuard.__init__)


def test_fsm::numberguard_constructor_args():
    sig = inspect.signature(fsm::NumberGuard.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fsm::numberguard_has_value():
    assert hasattr(fsm::NumberGuard, "value")
    descriptor = None
    for klass in fsm::NumberGuard.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_fsm::numbervariable_is_not_abstract():
    assert not inspect.isabstract(fsm::NumberVariable)


def test_fsm::numbervariable_constructor_exists():
    assert callable(fsm::NumberVariable.__init__)


def test_fsm::numbervariable_constructor_args():
    sig = inspect.signature(fsm::NumberVariable.__init__)
    params = list(sig.parameters.keys())
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_fsm::numbervariable_has_initialValue():
    assert hasattr(fsm::NumberVariable, "initialValue")
    descriptor = None
    for klass in fsm::NumberVariable.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_fsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(fsm::NamedElement)


def test_fsm::namedelement_constructor_exists():
    assert callable(fsm::NamedElement.__init__)


def test_fsm::namedelement_constructor_args():
    sig = inspect.signature(fsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::namedelement_has_name():
    assert hasattr(fsm::NamedElement, "name")
    descriptor = None
    for klass in fsm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm::action_is_not_abstract():
    assert not inspect.isabstract(fsm::Action)


def test_fsm::action_constructor_exists():
    assert callable(fsm::Action.__init__)


def test_fsm::action_constructor_args():
    sig = inspect.signature(fsm::Action.__init__)
    params = list(sig.parameters.keys())



def test_fsm::guard_is_not_abstract():
    assert not inspect.isabstract(fsm::Guard)


def test_fsm::guard_constructor_exists():
    assert callable(fsm::Guard.__init__)


def test_fsm::guard_constructor_args():
    sig = inspect.signature(fsm::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_fsm::guard_has_not_():
    assert hasattr(fsm::Guard, "not_")
    descriptor = None
    for klass in fsm::Guard.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_fsm::variable_is_not_abstract():
    assert not inspect.isabstract(fsm::Variable)


def test_fsm::variable_constructor_exists():
    assert callable(fsm::Variable.__init__)


def test_fsm::variable_constructor_args():
    sig = inspect.signature(fsm::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm::variable_has_name():
    assert hasattr(fsm::Variable, "name")
    descriptor = None
    for klass in fsm::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsm::StateMachine)


def test_fsm::statemachine_constructor_exists():
    assert callable(fsm::StateMachine.__init__)


def test_fsm::statemachine_constructor_args():
    sig = inspect.signature(fsm::StateMachine.__init__)
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
Action_strategy = st.builds(
    Action,
)
fsm::IncreaseValueAction_strategy = st.builds(
    fsm::IncreaseValueAction,
    stepValue=
        st.integers()
)
fsm::DecreaseValueAction_strategy = st.builds(
    fsm::DecreaseValueAction,
    stepValue=
        st.integers()
)
fsm::AssignValueAction_strategy = st.builds(
    fsm::AssignValueAction,
    value=
        st.integers()
)
NumberGuard_strategy = st.builds(
    NumberGuard,
)
fsm::LessThanNumberGuard_strategy = st.builds(
    fsm::LessThanNumberGuard,
)
fsm::GreaterThanNumberGuard_strategy = st.builds(
    fsm::GreaterThanNumberGuard,
)
fsm::EqualNumberGuard_strategy = st.builds(
    fsm::EqualNumberGuard,
)
Guard_strategy = st.builds(
    Guard,
)
fsm::NumberGuard_strategy = st.builds(
    fsm::NumberGuard,
    value=
        st.integers()
)
Variable_strategy = st.builds(
    Variable,
)
fsm::NumberVariable_strategy = st.builds(
    fsm::NumberVariable,
    initialValue=
        st.integers()
)
fsm::NamedElement_strategy = st.builds(
    fsm::NamedElement,
    name=
        safe_text
)
fsm::Action_strategy = st.builds(
    fsm::Action,
)
fsm::Guard_strategy = st.builds(
    fsm::Guard,
    not_=
        st.booleans()
)
fsm::Variable_strategy = st.builds(
    fsm::Variable,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
fsm::State_strategy = st.builds(
    fsm::State,
)
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::StateMachine_strategy = st.builds(
    fsm::StateMachine,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=fsm::IncreaseValueAction_strategy)
@settings(max_examples=50)
def test_fsm::increasevalueaction_instantiation(instance):
    assert isinstance(instance, fsm::IncreaseValueAction)

@given(instance=fsm::IncreaseValueAction_strategy)
def test_fsm::increasevalueaction_stepValue_type(instance):
    assert isinstance(instance.stepValue, int)


@given(instance=fsm::IncreaseValueAction_strategy)
def test_fsm::increasevalueaction_stepValue_setter(instance):
    original = instance.stepValue
    instance.stepValue = original
    assert instance.stepValue == original

@given(instance=fsm::DecreaseValueAction_strategy)
@settings(max_examples=50)
def test_fsm::decreasevalueaction_instantiation(instance):
    assert isinstance(instance, fsm::DecreaseValueAction)

@given(instance=fsm::DecreaseValueAction_strategy)
def test_fsm::decreasevalueaction_stepValue_type(instance):
    assert isinstance(instance.stepValue, int)


@given(instance=fsm::DecreaseValueAction_strategy)
def test_fsm::decreasevalueaction_stepValue_setter(instance):
    original = instance.stepValue
    instance.stepValue = original
    assert instance.stepValue == original

@given(instance=fsm::AssignValueAction_strategy)
@settings(max_examples=50)
def test_fsm::assignvalueaction_instantiation(instance):
    assert isinstance(instance, fsm::AssignValueAction)

@given(instance=fsm::AssignValueAction_strategy)
def test_fsm::assignvalueaction_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fsm::AssignValueAction_strategy)
def test_fsm::assignvalueaction_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberGuard_strategy)
@settings(max_examples=50)
def test_numberguard_instantiation(instance):
    assert isinstance(instance, NumberGuard)

@given(instance=fsm::LessThanNumberGuard_strategy)
@settings(max_examples=50)
def test_fsm::lessthannumberguard_instantiation(instance):
    assert isinstance(instance, fsm::LessThanNumberGuard)

@given(instance=fsm::GreaterThanNumberGuard_strategy)
@settings(max_examples=50)
def test_fsm::greaterthannumberguard_instantiation(instance):
    assert isinstance(instance, fsm::GreaterThanNumberGuard)

@given(instance=fsm::EqualNumberGuard_strategy)
@settings(max_examples=50)
def test_fsm::equalnumberguard_instantiation(instance):
    assert isinstance(instance, fsm::EqualNumberGuard)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=fsm::NumberGuard_strategy)
@settings(max_examples=50)
def test_fsm::numberguard_instantiation(instance):
    assert isinstance(instance, fsm::NumberGuard)

@given(instance=fsm::NumberGuard_strategy)
def test_fsm::numberguard_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=fsm::NumberGuard_strategy)
def test_fsm::numberguard_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=fsm::NumberVariable_strategy)
@settings(max_examples=50)
def test_fsm::numbervariable_instantiation(instance):
    assert isinstance(instance, fsm::NumberVariable)

@given(instance=fsm::NumberVariable_strategy)
def test_fsm::numbervariable_initialValue_type(instance):
    assert isinstance(instance.initialValue, int)


@given(instance=fsm::NumberVariable_strategy)
def test_fsm::numbervariable_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=fsm::NamedElement_strategy)
@settings(max_examples=50)
def test_fsm::namedelement_instantiation(instance):
    assert isinstance(instance, fsm::NamedElement)

@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::NamedElement_strategy)
def test_fsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm::Action_strategy)
@settings(max_examples=50)
def test_fsm::action_instantiation(instance):
    assert isinstance(instance, fsm::Action)

@given(instance=fsm::Guard_strategy)
@settings(max_examples=50)
def test_fsm::guard_instantiation(instance):
    assert isinstance(instance, fsm::Guard)

@given(instance=fsm::Guard_strategy)
def test_fsm::guard_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=fsm::Guard_strategy)
def test_fsm::guard_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=fsm::Variable_strategy)
@settings(max_examples=50)
def test_fsm::variable_instantiation(instance):
    assert isinstance(instance, fsm::Variable)

@given(instance=fsm::Variable_strategy)
def test_fsm::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsm::Variable_strategy)
def test_fsm::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::StateMachine_strategy)
@settings(max_examples=50)
def test_fsm::statemachine_instantiation(instance):
    assert isinstance(instance, fsm::StateMachine)
