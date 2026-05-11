import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testing::Transition,
    testing::Adapter,
    testing::TestCoverage,
    testing::TestSuite,
    testing::TestCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testing::transition_is_not_abstract():
    assert not inspect.isabstract(testing::Transition)


def test_testing::transition_constructor_exists():
    assert callable(testing::Transition.__init__)


def test_testing::transition_constructor_args():
    sig = inspect.signature(testing::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_testing::transition_has_name():
    assert hasattr(testing::Transition, "name")
    descriptor = None
    for klass in testing::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_testing::transition_has_type():
    assert hasattr(testing::Transition, "type")
    descriptor = None
    for klass in testing::Transition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_testing::adapter_is_not_abstract():
    assert not inspect.isabstract(testing::Adapter)


def test_testing::adapter_constructor_exists():
    assert callable(testing::Adapter.__init__)


def test_testing::adapter_constructor_args():
    sig = inspect.signature(testing::Adapter.__init__)
    params = list(sig.parameters.keys())



def test_testing::testcoverage_is_not_abstract():
    assert not inspect.isabstract(testing::TestCoverage)


def test_testing::testcoverage_constructor_exists():
    assert callable(testing::TestCoverage.__init__)


def test_testing::testcoverage_constructor_args():
    sig = inspect.signature(testing::TestCoverage.__init__)
    params = list(sig.parameters.keys())



def test_testing::testsuite_is_not_abstract():
    assert not inspect.isabstract(testing::TestSuite)


def test_testing::testsuite_constructor_exists():
    assert callable(testing::TestSuite.__init__)


def test_testing::testsuite_constructor_args():
    sig = inspect.signature(testing::TestSuite.__init__)
    params = list(sig.parameters.keys())
    assert "sutName" in params, "Missing parameter 'sutName'"

def test_testing::testsuite_has_sutName():
    assert hasattr(testing::TestSuite, "sutName")
    descriptor = None
    for klass in testing::TestSuite.__mro__:
        if "sutName" in klass.__dict__:
            descriptor = klass.__dict__["sutName"]
            break
    assert isinstance(descriptor, property)



def test_testing::testcase_is_not_abstract():
    assert not inspect.isabstract(testing::TestCase)


def test_testing::testcase_constructor_exists():
    assert callable(testing::TestCase.__init__)


def test_testing::testcase_constructor_args():
    sig = inspect.signature(testing::TestCase.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_testing::testcase_has_input():
    assert hasattr(testing::TestCase, "input")
    descriptor = None
    for klass in testing::TestCase.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_testing::testcase_has_output():
    assert hasattr(testing::TestCase, "output")
    descriptor = None
    for klass in testing::TestCase.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
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
testing::Transition_strategy = st.builds(
    testing::Transition,
    name=
        safe_text,
    type=
        safe_text
)
testing::Adapter_strategy = st.builds(
    testing::Adapter,
)
testing::TestCoverage_strategy = st.builds(
    testing::TestCoverage,
)
testing::TestSuite_strategy = st.builds(
    testing::TestSuite,
    sutName=
        safe_text
)
testing::TestCase_strategy = st.builds(
    testing::TestCase,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=testing::Transition_strategy)
@settings(max_examples=50)
def test_testing::transition_instantiation(instance):
    assert isinstance(instance, testing::Transition)

@given(instance=testing::Transition_strategy)
def test_testing::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testing::Transition_strategy)
def test_testing::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testing::Transition_strategy)
def test_testing::transition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=testing::Transition_strategy)
def test_testing::transition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=testing::Adapter_strategy)
@settings(max_examples=50)
def test_testing::adapter_instantiation(instance):
    assert isinstance(instance, testing::Adapter)

@given(instance=testing::TestCoverage_strategy)
@settings(max_examples=50)
def test_testing::testcoverage_instantiation(instance):
    assert isinstance(instance, testing::TestCoverage)

@given(instance=testing::TestSuite_strategy)
@settings(max_examples=50)
def test_testing::testsuite_instantiation(instance):
    assert isinstance(instance, testing::TestSuite)

@given(instance=testing::TestSuite_strategy)
def test_testing::testsuite_sutName_type(instance):
    assert isinstance(instance.sutName, str)


@given(instance=testing::TestSuite_strategy)
def test_testing::testsuite_sutName_setter(instance):
    original = instance.sutName
    instance.sutName = original
    assert instance.sutName == original

@given(instance=testing::TestCase_strategy)
@settings(max_examples=50)
def test_testing::testcase_instantiation(instance):
    assert isinstance(instance, testing::TestCase)

@given(instance=testing::TestCase_strategy)
def test_testing::testcase_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=testing::TestCase_strategy)
def test_testing::testcase_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=testing::TestCase_strategy)
def test_testing::testcase_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=testing::TestCase_strategy)
def test_testing::testcase_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
