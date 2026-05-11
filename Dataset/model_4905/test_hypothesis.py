import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Service::JavaService,
    Service::Tool,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_service::javaservice_is_not_abstract():
    assert not inspect.isabstract(Service::JavaService)


def test_service::javaservice_constructor_exists():
    assert callable(Service::JavaService.__init__)


def test_service::javaservice_constructor_args():
    sig = inspect.signature(Service::JavaService.__init__)
    params = list(sig.parameters.keys())
    assert "option" in params, "Missing parameter 'option'"
    assert "name" in params, "Missing parameter 'name'"

def test_service::javaservice_has_option():
    assert hasattr(Service::JavaService, "option")
    descriptor = None
    for klass in Service::JavaService.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)

def test_service::javaservice_has_name():
    assert hasattr(Service::JavaService, "name")
    descriptor = None
    for klass in Service::JavaService.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_service::tool_is_not_abstract():
    assert not inspect.isabstract(Service::Tool)


def test_service::tool_constructor_exists():
    assert callable(Service::Tool.__init__)


def test_service::tool_constructor_args():
    sig = inspect.signature(Service::Tool.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_service::tool_has_name():
    assert hasattr(Service::Tool, "name")
    descriptor = None
    for klass in Service::Tool.__mro__:
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
Service::JavaService_strategy = st.builds(
    Service::JavaService,
    option=
        safe_text,
    name=
        safe_text
)
Service::Tool_strategy = st.builds(
    Service::Tool,
    name=
        safe_text
)

@given(instance=Service::JavaService_strategy)
@settings(max_examples=50)
def test_service::javaservice_instantiation(instance):
    assert isinstance(instance, Service::JavaService)

@given(instance=Service::JavaService_strategy)
def test_service::javaservice_option_type(instance):
    assert isinstance(instance.option, str)


@given(instance=Service::JavaService_strategy)
def test_service::javaservice_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original

@given(instance=Service::JavaService_strategy)
def test_service::javaservice_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Service::JavaService_strategy)
def test_service::javaservice_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Service::Tool_strategy)
@settings(max_examples=50)
def test_service::tool_instantiation(instance):
    assert isinstance(instance, Service::Tool)

@given(instance=Service::Tool_strategy)
def test_service::tool_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Service::Tool_strategy)
def test_service::tool_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
