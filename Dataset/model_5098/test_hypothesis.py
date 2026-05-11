import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Component,
    testport::Base,
    testport::Required,
    testport::Component,
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



def test_testport::base_is_not_abstract():
    assert not inspect.isabstract(testport::Base)


def test_testport::base_constructor_exists():
    assert callable(testport::Base.__init__)


def test_testport::base_constructor_args():
    sig = inspect.signature(testport::Base.__init__)
    params = list(sig.parameters.keys())



def test_testport::required_is_not_abstract():
    assert not inspect.isabstract(testport::Required)


def test_testport::required_constructor_exists():
    assert callable(testport::Required.__init__)


def test_testport::required_constructor_args():
    sig = inspect.signature(testport::Required.__init__)
    params = list(sig.parameters.keys())



def test_testport::component_is_not_abstract():
    assert not inspect.isabstract(testport::Component)


def test_testport::component_constructor_exists():
    assert callable(testport::Component.__init__)


def test_testport::component_constructor_args():
    sig = inspect.signature(testport::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testport::component_has_name():
    assert hasattr(testport::Component, "name")
    descriptor = None
    for klass in testport::Component.__mro__:
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
testport::Base_strategy = st.builds(
    testport::Base,
)
testport::Required_strategy = st.builds(
    testport::Required,
)
testport::Component_strategy = st.builds(
    testport::Component,
    name=
        safe_text
)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=testport::Base_strategy)
@settings(max_examples=50)
def test_testport::base_instantiation(instance):
    assert isinstance(instance, testport::Base)

@given(instance=testport::Required_strategy)
@settings(max_examples=50)
def test_testport::required_instantiation(instance):
    assert isinstance(instance, testport::Required)

@given(instance=testport::Component_strategy)
@settings(max_examples=50)
def test_testport::component_instantiation(instance):
    assert isinstance(instance, testport::Component)

@given(instance=testport::Component_strategy)
def test_testport::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testport::Component_strategy)
def test_testport::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
