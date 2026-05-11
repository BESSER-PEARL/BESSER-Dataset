import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataValue,
    xunit::DataValue,
    xunit::Action,
    xunit::ExpectedValue,
    NamedElement,
    xunit::TestCase,
    xunit::Assertion,
    xunit::TestSuite,
    xunit::NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datavalue_is_not_abstract():
    assert not inspect.isabstract(DataValue)


def test_datavalue_constructor_exists():
    assert callable(DataValue.__init__)


def test_datavalue_constructor_args():
    sig = inspect.signature(DataValue.__init__)
    params = list(sig.parameters.keys())



def test_xunit::datavalue_is_not_abstract():
    assert not inspect.isabstract(xunit::DataValue)


def test_xunit::datavalue_constructor_exists():
    assert callable(xunit::DataValue.__init__)


def test_xunit::datavalue_constructor_args():
    sig = inspect.signature(xunit::DataValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xunit::datavalue_has_value():
    assert hasattr(xunit::DataValue, "value")
    descriptor = None
    for klass in xunit::DataValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xunit::action_is_not_abstract():
    assert not inspect.isabstract(xunit::Action)


def test_xunit::action_constructor_exists():
    assert callable(xunit::Action.__init__)


def test_xunit::action_constructor_args():
    sig = inspect.signature(xunit::Action.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"

def test_xunit::action_has_desc():
    assert hasattr(xunit::Action, "desc")
    descriptor = None
    for klass in xunit::Action.__mro__:
        if "desc" in klass.__dict__:
            descriptor = klass.__dict__["desc"]
            break
    assert isinstance(descriptor, property)



def test_xunit::expectedvalue_is_not_abstract():
    assert not inspect.isabstract(xunit::ExpectedValue)


def test_xunit::expectedvalue_constructor_exists():
    assert callable(xunit::ExpectedValue.__init__)


def test_xunit::expectedvalue_constructor_args():
    sig = inspect.signature(xunit::ExpectedValue.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_xunit::testcase_is_not_abstract():
    assert not inspect.isabstract(xunit::TestCase)


def test_xunit::testcase_constructor_exists():
    assert callable(xunit::TestCase.__init__)


def test_xunit::testcase_constructor_args():
    sig = inspect.signature(xunit::TestCase.__init__)
    params = list(sig.parameters.keys())



def test_xunit::assertion_is_not_abstract():
    assert not inspect.isabstract(xunit::Assertion)


def test_xunit::assertion_constructor_exists():
    assert callable(xunit::Assertion.__init__)


def test_xunit::assertion_constructor_args():
    sig = inspect.signature(xunit::Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xunit::assertion_has_type():
    assert hasattr(xunit::Assertion, "type")
    descriptor = None
    for klass in xunit::Assertion.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xunit::testsuite_is_not_abstract():
    assert not inspect.isabstract(xunit::TestSuite)


def test_xunit::testsuite_constructor_exists():
    assert callable(xunit::TestSuite.__init__)


def test_xunit::testsuite_constructor_args():
    sig = inspect.signature(xunit::TestSuite.__init__)
    params = list(sig.parameters.keys())



def test_xunit::namedelement_is_not_abstract():
    assert not inspect.isabstract(xunit::NamedElement)


def test_xunit::namedelement_constructor_exists():
    assert callable(xunit::NamedElement.__init__)


def test_xunit::namedelement_constructor_args():
    sig = inspect.signature(xunit::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xunit::namedelement_has_name():
    assert hasattr(xunit::NamedElement, "name")
    descriptor = None
    for klass in xunit::NamedElement.__mro__:
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
DataValue_strategy = st.builds(
    DataValue,
)
xunit::DataValue_strategy = st.builds(
    xunit::DataValue,
    value=
        safe_text
)
xunit::Action_strategy = st.builds(
    xunit::Action,
    desc=
        safe_text
)
xunit::ExpectedValue_strategy = st.builds(
    xunit::ExpectedValue,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
xunit::TestCase_strategy = st.builds(
    xunit::TestCase,
)
xunit::Assertion_strategy = st.builds(
    xunit::Assertion,
    type=
        safe_text
)
xunit::TestSuite_strategy = st.builds(
    xunit::TestSuite,
)
xunit::NamedElement_strategy = st.builds(
    xunit::NamedElement,
    name=
        safe_text
)

@given(instance=DataValue_strategy)
@settings(max_examples=50)
def test_datavalue_instantiation(instance):
    assert isinstance(instance, DataValue)

@given(instance=xunit::DataValue_strategy)
@settings(max_examples=50)
def test_xunit::datavalue_instantiation(instance):
    assert isinstance(instance, xunit::DataValue)

@given(instance=xunit::DataValue_strategy)
def test_xunit::datavalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xunit::DataValue_strategy)
def test_xunit::datavalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xunit::Action_strategy)
@settings(max_examples=50)
def test_xunit::action_instantiation(instance):
    assert isinstance(instance, xunit::Action)

@given(instance=xunit::Action_strategy)
def test_xunit::action_desc_type(instance):
    assert isinstance(instance.desc, str)


@given(instance=xunit::Action_strategy)
def test_xunit::action_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original

@given(instance=xunit::ExpectedValue_strategy)
@settings(max_examples=50)
def test_xunit::expectedvalue_instantiation(instance):
    assert isinstance(instance, xunit::ExpectedValue)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=xunit::TestCase_strategy)
@settings(max_examples=50)
def test_xunit::testcase_instantiation(instance):
    assert isinstance(instance, xunit::TestCase)

@given(instance=xunit::Assertion_strategy)
@settings(max_examples=50)
def test_xunit::assertion_instantiation(instance):
    assert isinstance(instance, xunit::Assertion)

@given(instance=xunit::Assertion_strategy)
def test_xunit::assertion_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xunit::Assertion_strategy)
def test_xunit::assertion_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xunit::TestSuite_strategy)
@settings(max_examples=50)
def test_xunit::testsuite_instantiation(instance):
    assert isinstance(instance, xunit::TestSuite)

@given(instance=xunit::NamedElement_strategy)
@settings(max_examples=50)
def test_xunit::namedelement_instantiation(instance):
    assert isinstance(instance, xunit::NamedElement)

@given(instance=xunit::NamedElement_strategy)
def test_xunit::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xunit::NamedElement_strategy)
def test_xunit::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
