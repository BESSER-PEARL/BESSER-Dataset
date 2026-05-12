import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    automation_Output,
    automation_Input,
    automation_Transition,
    automation_State,
    automation_NamedElement,
    automation_Automation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_automation_output_is_not_abstract():
    assert not inspect.isabstract(automation_Output)


def test_automation_output_constructor_exists():
    assert callable(automation_Output.__init__)


def test_automation_output_constructor_args():
    sig = inspect.signature(automation_Output.__init__)
    params = list(sig.parameters.keys())



def test_automation_input_is_not_abstract():
    assert not inspect.isabstract(automation_Input)


def test_automation_input_constructor_exists():
    assert callable(automation_Input.__init__)


def test_automation_input_constructor_args():
    sig = inspect.signature(automation_Input.__init__)
    params = list(sig.parameters.keys())



def test_automation_transition_is_not_abstract():
    assert not inspect.isabstract(automation_Transition)


def test_automation_transition_constructor_exists():
    assert callable(automation_Transition.__init__)


def test_automation_transition_constructor_args():
    sig = inspect.signature(automation_Transition.__init__)
    params = list(sig.parameters.keys())



def test_automation_state_is_not_abstract():
    assert not inspect.isabstract(automation_State)


def test_automation_state_constructor_exists():
    assert callable(automation_State.__init__)


def test_automation_state_constructor_args():
    sig = inspect.signature(automation_State.__init__)
    params = list(sig.parameters.keys())



def test_automation_namedelement_is_not_abstract():
    assert not inspect.isabstract(automation_NamedElement)


def test_automation_namedelement_constructor_exists():
    assert callable(automation_NamedElement.__init__)


def test_automation_namedelement_constructor_args():
    sig = inspect.signature(automation_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automation_namedelement_has_name():
    assert hasattr(automation_NamedElement, "name")
    descriptor = None
    for klass in automation_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automation_automation_is_not_abstract():
    assert not inspect.isabstract(automation_Automation)


def test_automation_automation_constructor_exists():
    assert callable(automation_Automation.__init__)


def test_automation_automation_constructor_args():
    sig = inspect.signature(automation_Automation.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
automation_Output_strategy = st.builds(
    automation_Output,
)
automation_Input_strategy = st.builds(
    automation_Input,
)
automation_Transition_strategy = st.builds(
    automation_Transition,
)
automation_State_strategy = st.builds(
    automation_State,
)
automation_NamedElement_strategy = st.builds(
    automation_NamedElement,
    name=
        safe_text
)
automation_Automation_strategy = st.builds(
    automation_Automation,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=automation_Output_strategy)
@settings(max_examples=50)
def test_automation_output_instantiation(instance):
    assert isinstance(instance, automation_Output)

@given(instance=automation_Input_strategy)
@settings(max_examples=50)
def test_automation_input_instantiation(instance):
    assert isinstance(instance, automation_Input)

@given(instance=automation_Transition_strategy)
@settings(max_examples=50)
def test_automation_transition_instantiation(instance):
    assert isinstance(instance, automation_Transition)

@given(instance=automation_State_strategy)
@settings(max_examples=50)
def test_automation_state_instantiation(instance):
    assert isinstance(instance, automation_State)

@given(instance=automation_NamedElement_strategy)
@settings(max_examples=50)
def test_automation_namedelement_instantiation(instance):
    assert isinstance(instance, automation_NamedElement)



@given(instance=automation_NamedElement_strategy)
def test_automation_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automation_Automation_strategy)
@settings(max_examples=50)
def test_automation_automation_instantiation(instance):
    assert isinstance(instance, automation_Automation)
