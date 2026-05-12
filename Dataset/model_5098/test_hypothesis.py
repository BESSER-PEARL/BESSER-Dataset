import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Component,
    testport_Base,
    testport_Required,
    testport_Component,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_testport_base_is_not_abstract():
    assert not inspect.isabstract(testport_Base)


def test_testport_base_constructor_exists():
    assert callable(testport_Base.__init__)


def test_testport_base_constructor_args():
    sig = inspect.signature(testport_Base.__init__)
    params = list(sig.parameters.keys())



def test_testport_required_is_not_abstract():
    assert not inspect.isabstract(testport_Required)


def test_testport_required_constructor_exists():
    assert callable(testport_Required.__init__)


def test_testport_required_constructor_args():
    sig = inspect.signature(testport_Required.__init__)
    params = list(sig.parameters.keys())



def test_testport_component_is_not_abstract():
    assert not inspect.isabstract(testport_Component)


def test_testport_component_constructor_exists():
    assert callable(testport_Component.__init__)


def test_testport_component_constructor_args():
    sig = inspect.signature(testport_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testport_component_has_name():
    assert hasattr(testport_Component, "name")
    descriptor = None
    for klass in testport_Component.__mro__:
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
Component_strategy = st.builds(
    Component,
)
testport_Base_strategy = st.builds(
    testport_Base,
)
testport_Required_strategy = st.builds(
    testport_Required,
)
testport_Component_strategy = st.builds(
    testport_Component,
    name=
        safe_text
)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=testport_Base_strategy)
@settings(max_examples=50)
def test_testport_base_instantiation(instance):
    assert isinstance(instance, testport_Base)

@given(instance=testport_Required_strategy)
@settings(max_examples=50)
def test_testport_required_instantiation(instance):
    assert isinstance(instance, testport_Required)

@given(instance=testport_Component_strategy)
@settings(max_examples=50)
def test_testport_component_instantiation(instance):
    assert isinstance(instance, testport_Component)



@given(instance=testport_Component_strategy)
def test_testport_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
