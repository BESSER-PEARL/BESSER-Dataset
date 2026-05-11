import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    automation::Output,
    automation::Input,
    automation::Transition,
    automation::State,
    automation::NamedElement,
    automation::Automation,
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



def test_automation::output_is_not_abstract():
    assert not inspect.isabstract(automation::Output)


def test_automation::output_constructor_exists():
    assert callable(automation::Output.__init__)


def test_automation::output_constructor_args():
    sig = inspect.signature(automation::Output.__init__)
    params = list(sig.parameters.keys())



def test_automation::input_is_not_abstract():
    assert not inspect.isabstract(automation::Input)


def test_automation::input_constructor_exists():
    assert callable(automation::Input.__init__)


def test_automation::input_constructor_args():
    sig = inspect.signature(automation::Input.__init__)
    params = list(sig.parameters.keys())



def test_automation::transition_is_not_abstract():
    assert not inspect.isabstract(automation::Transition)


def test_automation::transition_constructor_exists():
    assert callable(automation::Transition.__init__)


def test_automation::transition_constructor_args():
    sig = inspect.signature(automation::Transition.__init__)
    params = list(sig.parameters.keys())



def test_automation::state_is_not_abstract():
    assert not inspect.isabstract(automation::State)


def test_automation::state_constructor_exists():
    assert callable(automation::State.__init__)


def test_automation::state_constructor_args():
    sig = inspect.signature(automation::State.__init__)
    params = list(sig.parameters.keys())



def test_automation::namedelement_is_not_abstract():
    assert not inspect.isabstract(automation::NamedElement)


def test_automation::namedelement_constructor_exists():
    assert callable(automation::NamedElement.__init__)


def test_automation::namedelement_constructor_args():
    sig = inspect.signature(automation::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_automation::namedelement_has_name():
    assert hasattr(automation::NamedElement, "name")
    descriptor = None
    for klass in automation::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_automation::automation_is_not_abstract():
    assert not inspect.isabstract(automation::Automation)


def test_automation::automation_constructor_exists():
    assert callable(automation::Automation.__init__)


def test_automation::automation_constructor_args():
    sig = inspect.signature(automation::Automation.__init__)
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
automation::Output_strategy = st.builds(
    automation::Output,
)
automation::Input_strategy = st.builds(
    automation::Input,
)
automation::Transition_strategy = st.builds(
    automation::Transition,
)
automation::State_strategy = st.builds(
    automation::State,
)
automation::NamedElement_strategy = st.builds(
    automation::NamedElement,
    name=
        safe_text
)
automation::Automation_strategy = st.builds(
    automation::Automation,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=automation::Output_strategy)
@settings(max_examples=50)
def test_automation::output_instantiation(instance):
    assert isinstance(instance, automation::Output)

@given(instance=automation::Input_strategy)
@settings(max_examples=50)
def test_automation::input_instantiation(instance):
    assert isinstance(instance, automation::Input)

@given(instance=automation::Transition_strategy)
@settings(max_examples=50)
def test_automation::transition_instantiation(instance):
    assert isinstance(instance, automation::Transition)

@given(instance=automation::State_strategy)
@settings(max_examples=50)
def test_automation::state_instantiation(instance):
    assert isinstance(instance, automation::State)

@given(instance=automation::NamedElement_strategy)
@settings(max_examples=50)
def test_automation::namedelement_instantiation(instance):
    assert isinstance(instance, automation::NamedElement)

@given(instance=automation::NamedElement_strategy)
def test_automation::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=automation::NamedElement_strategy)
def test_automation::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=automation::Automation_strategy)
@settings(max_examples=50)
def test_automation::automation_instantiation(instance):
    assert isinstance(instance, automation::Automation)
