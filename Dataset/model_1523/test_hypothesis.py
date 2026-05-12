import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cpsml_Fright,
    cpsml_DeVariable,
    cpsml_IndeVariable,
    cpsml_Interval,
    cpsml_Condition,
    cpsml_Function,
    Transition,
    cpsml_ProbTransition,
    cpsml_ComTransition,
    cpsml_ODE,
    cpsml_Transition,
    cpsml_State,
    cpsml_Variable,
    cpsml_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cpsml_fright_is_not_abstract():
    assert not inspect.isabstract(cpsml_Fright)


def test_cpsml_fright_constructor_exists():
    assert callable(cpsml_Fright.__init__)


def test_cpsml_fright_constructor_args():
    sig = inspect.signature(cpsml_Fright.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_fright_has_name():
    assert hasattr(cpsml_Fright, "name")
    descriptor = None
    for klass in cpsml_Fright.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_devariable_is_not_abstract():
    assert not inspect.isabstract(cpsml_DeVariable)


def test_cpsml_devariable_constructor_exists():
    assert callable(cpsml_DeVariable.__init__)


def test_cpsml_devariable_constructor_args():
    sig = inspect.signature(cpsml_DeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_devariable_has_name():
    assert hasattr(cpsml_DeVariable, "name")
    descriptor = None
    for klass in cpsml_DeVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_indevariable_is_not_abstract():
    assert not inspect.isabstract(cpsml_IndeVariable)


def test_cpsml_indevariable_constructor_exists():
    assert callable(cpsml_IndeVariable.__init__)


def test_cpsml_indevariable_constructor_args():
    sig = inspect.signature(cpsml_IndeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_indevariable_has_name():
    assert hasattr(cpsml_IndeVariable, "name")
    descriptor = None
    for klass in cpsml_IndeVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_interval_is_not_abstract():
    assert not inspect.isabstract(cpsml_Interval)


def test_cpsml_interval_constructor_exists():
    assert callable(cpsml_Interval.__init__)


def test_cpsml_interval_constructor_args():
    sig = inspect.signature(cpsml_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"
    assert "name" in params, "Missing parameter 'name'"
    assert "right" in params, "Missing parameter 'right'"
    assert "subinterval" in params, "Missing parameter 'subinterval'"

def test_cpsml_interval_has_left():
    assert hasattr(cpsml_Interval, "left")
    descriptor = None
    for klass in cpsml_Interval.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_interval_has_name():
    assert hasattr(cpsml_Interval, "name")
    descriptor = None
    for klass in cpsml_Interval.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_interval_has_right():
    assert hasattr(cpsml_Interval, "right")
    descriptor = None
    for klass in cpsml_Interval.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_interval_has_subinterval():
    assert hasattr(cpsml_Interval, "subinterval")
    descriptor = None
    for klass in cpsml_Interval.__mro__:
        if "subinterval" in klass.__dict__:
            descriptor = klass.__dict__["subinterval"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_condition_is_not_abstract():
    assert not inspect.isabstract(cpsml_Condition)


def test_cpsml_condition_constructor_exists():
    assert callable(cpsml_Condition.__init__)


def test_cpsml_condition_constructor_args():
    sig = inspect.signature(cpsml_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_condition_has_name():
    assert hasattr(cpsml_Condition, "name")
    descriptor = None
    for klass in cpsml_Condition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_function_is_not_abstract():
    assert not inspect.isabstract(cpsml_Function)


def test_cpsml_function_constructor_exists():
    assert callable(cpsml_Function.__init__)


def test_cpsml_function_constructor_args():
    sig = inspect.signature(cpsml_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_function_has_name():
    assert hasattr(cpsml_Function, "name")
    descriptor = None
    for klass in cpsml_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_cpsml_probtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml_ProbTransition)


def test_cpsml_probtransition_constructor_exists():
    assert callable(cpsml_ProbTransition.__init__)


def test_cpsml_probtransition_constructor_args():
    sig = inspect.signature(cpsml_ProbTransition.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"

def test_cpsml_probtransition_has_probability():
    assert hasattr(cpsml_ProbTransition, "probability")
    descriptor = None
    for klass in cpsml_ProbTransition.__mro__:
        if "probability" in klass.__dict__:
            descriptor = klass.__dict__["probability"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_comtransition_is_not_abstract():
    assert not inspect.isabstract(cpsml_ComTransition)


def test_cpsml_comtransition_constructor_exists():
    assert callable(cpsml_ComTransition.__init__)


def test_cpsml_comtransition_constructor_args():
    sig = inspect.signature(cpsml_ComTransition.__init__)
    params = list(sig.parameters.keys())



def test_cpsml_ode_is_not_abstract():
    assert not inspect.isabstract(cpsml_ODE)


def test_cpsml_ode_constructor_exists():
    assert callable(cpsml_ODE.__init__)


def test_cpsml_ode_constructor_args():
    sig = inspect.signature(cpsml_ODE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_ode_has_name():
    assert hasattr(cpsml_ODE, "name")
    descriptor = None
    for klass in cpsml_ODE.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_transition_is_not_abstract():
    assert not inspect.isabstract(cpsml_Transition)


def test_cpsml_transition_constructor_exists():
    assert callable(cpsml_Transition.__init__)


def test_cpsml_transition_constructor_args():
    sig = inspect.signature(cpsml_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "event" in params, "Missing parameter 'event'"
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_transition_has_action():
    assert hasattr(cpsml_Transition, "action")
    descriptor = None
    for klass in cpsml_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_transition_has_guard():
    assert hasattr(cpsml_Transition, "guard")
    descriptor = None
    for klass in cpsml_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_transition_has_event():
    assert hasattr(cpsml_Transition, "event")
    descriptor = None
    for klass in cpsml_Transition.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_cpsml_transition_has_name():
    assert hasattr(cpsml_Transition, "name")
    descriptor = None
    for klass in cpsml_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_state_is_not_abstract():
    assert not inspect.isabstract(cpsml_State)


def test_cpsml_state_constructor_exists():
    assert callable(cpsml_State.__init__)


def test_cpsml_state_constructor_args():
    sig = inspect.signature(cpsml_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_state_has_name():
    assert hasattr(cpsml_State, "name")
    descriptor = None
    for klass in cpsml_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_variable_is_not_abstract():
    assert not inspect.isabstract(cpsml_Variable)


def test_cpsml_variable_constructor_exists():
    assert callable(cpsml_Variable.__init__)


def test_cpsml_variable_constructor_args():
    sig = inspect.signature(cpsml_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cpsml_variable_has_value():
    assert hasattr(cpsml_Variable, "value")
    descriptor = None
    for klass in cpsml_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cpsml_system_is_not_abstract():
    assert not inspect.isabstract(cpsml_System)


def test_cpsml_system_constructor_exists():
    assert callable(cpsml_System.__init__)


def test_cpsml_system_constructor_args():
    sig = inspect.signature(cpsml_System.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cpsml_system_has_name():
    assert hasattr(cpsml_System, "name")
    descriptor = None
    for klass in cpsml_System.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
cpsml_Fright_strategy = st.builds(
    cpsml_Fright,
    name=
        safe_text
)
cpsml_DeVariable_strategy = st.builds(
    cpsml_DeVariable,
    name=
        safe_text
)
cpsml_IndeVariable_strategy = st.builds(
    cpsml_IndeVariable,
    name=
        safe_text
)
cpsml_Interval_strategy = st.builds(
    cpsml_Interval,
    left=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    name=
        safe_text,
    right=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subinterval=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml_Condition_strategy = st.builds(
    cpsml_Condition,
    name=
        safe_text
)
cpsml_Function_strategy = st.builds(
    cpsml_Function,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
cpsml_ProbTransition_strategy = st.builds(
    cpsml_ProbTransition,
    probability=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml_ComTransition_strategy = st.builds(
    cpsml_ComTransition,
)
cpsml_ODE_strategy = st.builds(
    cpsml_ODE,
    name=
        safe_text
)
cpsml_Transition_strategy = st.builds(
    cpsml_Transition,
    action=
        safe_text,
    guard=
        safe_text,
    event=
        safe_text,
    name=
        safe_text
)
cpsml_State_strategy = st.builds(
    cpsml_State,
    name=
        safe_text
)
cpsml_Variable_strategy = st.builds(
    cpsml_Variable,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cpsml_System_strategy = st.builds(
    cpsml_System,
    name=
        safe_text
)

@given(instance=cpsml_Fright_strategy)
@settings(max_examples=50)
def test_cpsml_fright_instantiation(instance):
    assert isinstance(instance, cpsml_Fright)



@given(instance=cpsml_Fright_strategy)
def test_cpsml_fright_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_DeVariable_strategy)
@settings(max_examples=50)
def test_cpsml_devariable_instantiation(instance):
    assert isinstance(instance, cpsml_DeVariable)



@given(instance=cpsml_DeVariable_strategy)
def test_cpsml_devariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_IndeVariable_strategy)
@settings(max_examples=50)
def test_cpsml_indevariable_instantiation(instance):
    assert isinstance(instance, cpsml_IndeVariable)



@given(instance=cpsml_IndeVariable_strategy)
def test_cpsml_indevariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_Interval_strategy)
@settings(max_examples=50)
def test_cpsml_interval_instantiation(instance):
    assert isinstance(instance, cpsml_Interval)



@given(instance=cpsml_Interval_strategy)
def test_cpsml_interval_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original



@given(instance=cpsml_Interval_strategy)
def test_cpsml_interval_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cpsml_Interval_strategy)
def test_cpsml_interval_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original



@given(instance=cpsml_Interval_strategy)
def test_cpsml_interval_subinterval_setter(instance):
    original = instance.subinterval
    instance.subinterval = original
    assert instance.subinterval == original

@given(instance=cpsml_Condition_strategy)
@settings(max_examples=50)
def test_cpsml_condition_instantiation(instance):
    assert isinstance(instance, cpsml_Condition)



@given(instance=cpsml_Condition_strategy)
def test_cpsml_condition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_Function_strategy)
@settings(max_examples=50)
def test_cpsml_function_instantiation(instance):
    assert isinstance(instance, cpsml_Function)



@given(instance=cpsml_Function_strategy)
def test_cpsml_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=cpsml_ProbTransition_strategy)
@settings(max_examples=50)
def test_cpsml_probtransition_instantiation(instance):
    assert isinstance(instance, cpsml_ProbTransition)



@given(instance=cpsml_ProbTransition_strategy)
def test_cpsml_probtransition_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original

@given(instance=cpsml_ComTransition_strategy)
@settings(max_examples=50)
def test_cpsml_comtransition_instantiation(instance):
    assert isinstance(instance, cpsml_ComTransition)

@given(instance=cpsml_ODE_strategy)
@settings(max_examples=50)
def test_cpsml_ode_instantiation(instance):
    assert isinstance(instance, cpsml_ODE)



@given(instance=cpsml_ODE_strategy)
def test_cpsml_ode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_Transition_strategy)
@settings(max_examples=50)
def test_cpsml_transition_instantiation(instance):
    assert isinstance(instance, cpsml_Transition)



@given(instance=cpsml_Transition_strategy)
def test_cpsml_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=cpsml_Transition_strategy)
def test_cpsml_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=cpsml_Transition_strategy)
def test_cpsml_transition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=cpsml_Transition_strategy)
def test_cpsml_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_State_strategy)
@settings(max_examples=50)
def test_cpsml_state_instantiation(instance):
    assert isinstance(instance, cpsml_State)



@given(instance=cpsml_State_strategy)
def test_cpsml_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cpsml_Variable_strategy)
@settings(max_examples=50)
def test_cpsml_variable_instantiation(instance):
    assert isinstance(instance, cpsml_Variable)



@given(instance=cpsml_Variable_strategy)
def test_cpsml_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cpsml_System_strategy)
@settings(max_examples=50)
def test_cpsml_system_instantiation(instance):
    assert isinstance(instance, cpsml_System)



@given(instance=cpsml_System_strategy)
def test_cpsml_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
