import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Service_JavaService,
    Service_Tool,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_service_javaservice_is_not_abstract():
    assert not inspect.isabstract(Service_JavaService)


def test_service_javaservice_constructor_exists():
    assert callable(Service_JavaService.__init__)


def test_service_javaservice_constructor_args():
    sig = inspect.signature(Service_JavaService.__init__)
    params = list(sig.parameters.keys())
    assert "option" in params, "Missing parameter 'option'"
    assert "name" in params, "Missing parameter 'name'"

def test_service_javaservice_has_option():
    assert hasattr(Service_JavaService, "option")
    descriptor = None
    for klass in Service_JavaService.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)

def test_service_javaservice_has_name():
    assert hasattr(Service_JavaService, "name")
    descriptor = None
    for klass in Service_JavaService.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_service_tool_is_not_abstract():
    assert not inspect.isabstract(Service_Tool)


def test_service_tool_constructor_exists():
    assert callable(Service_Tool.__init__)


def test_service_tool_constructor_args():
    sig = inspect.signature(Service_Tool.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_service_tool_has_name():
    assert hasattr(Service_Tool, "name")
    descriptor = None
    for klass in Service_Tool.__mro__:
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
Service_JavaService_strategy = st.builds(
    Service_JavaService,
    option=
        safe_text,
    name=
        safe_text
)
Service_Tool_strategy = st.builds(
    Service_Tool,
    name=
        safe_text
)

@given(instance=Service_JavaService_strategy)
@settings(max_examples=50)
def test_service_javaservice_instantiation(instance):
    assert isinstance(instance, Service_JavaService)



@given(instance=Service_JavaService_strategy)
def test_service_javaservice_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original



@given(instance=Service_JavaService_strategy)
def test_service_javaservice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Service_Tool_strategy)
@settings(max_examples=50)
def test_service_tool_instantiation(instance):
    assert isinstance(instance, Service_Tool)



@given(instance=Service_Tool_strategy)
def test_service_tool_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
