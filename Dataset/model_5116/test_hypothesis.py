import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    benchmark::NamedElement,
    benchmark::Property,
    benchmark::TimeResult,
    NamedElement,
    benchmark::TestCase,
    benchmark::Variant,
    benchmark::InputData,
    benchmark::Scenario,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_benchmark::namedelement_is_not_abstract():
    assert not inspect.isabstract(benchmark::NamedElement)


def test_benchmark::namedelement_constructor_exists():
    assert callable(benchmark::NamedElement.__init__)


def test_benchmark::namedelement_constructor_args():
    sig = inspect.signature(benchmark::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_benchmark::namedelement_has_name():
    assert hasattr(benchmark::NamedElement, "name")
    descriptor = None
    for klass in benchmark::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_benchmark::property_is_not_abstract():
    assert not inspect.isabstract(benchmark::Property)


def test_benchmark::property_constructor_exists():
    assert callable(benchmark::Property.__init__)


def test_benchmark::property_constructor_args():
    sig = inspect.signature(benchmark::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_benchmark::property_has_value():
    assert hasattr(benchmark::Property, "value")
    descriptor = None
    for klass in benchmark::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_benchmark::property_has_name():
    assert hasattr(benchmark::Property, "name")
    descriptor = None
    for klass in benchmark::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_benchmark::timeresult_is_not_abstract():
    assert not inspect.isabstract(benchmark::TimeResult)


def test_benchmark::timeresult_constructor_exists():
    assert callable(benchmark::TimeResult.__init__)


def test_benchmark::timeresult_constructor_args():
    sig = inspect.signature(benchmark::TimeResult.__init__)
    params = list(sig.parameters.keys())
    assert "elapsedTime" in params, "Missing parameter 'elapsedTime'"
    assert "elapsedMaxTime" in params, "Missing parameter 'elapsedMaxTime'"

def test_benchmark::timeresult_has_elapsedTime():
    assert hasattr(benchmark::TimeResult, "elapsedTime")
    descriptor = None
    for klass in benchmark::TimeResult.__mro__:
        if "elapsedTime" in klass.__dict__:
            descriptor = klass.__dict__["elapsedTime"]
            break
    assert isinstance(descriptor, property)

def test_benchmark::timeresult_has_elapsedMaxTime():
    assert hasattr(benchmark::TimeResult, "elapsedMaxTime")
    descriptor = None
    for klass in benchmark::TimeResult.__mro__:
        if "elapsedMaxTime" in klass.__dict__:
            descriptor = klass.__dict__["elapsedMaxTime"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_benchmark::testcase_is_not_abstract():
    assert not inspect.isabstract(benchmark::TestCase)


def test_benchmark::testcase_constructor_exists():
    assert callable(benchmark::TestCase.__init__)


def test_benchmark::testcase_constructor_args():
    sig = inspect.signature(benchmark::TestCase.__init__)
    params = list(sig.parameters.keys())



def test_benchmark::variant_is_not_abstract():
    assert not inspect.isabstract(benchmark::Variant)


def test_benchmark::variant_constructor_exists():
    assert callable(benchmark::Variant.__init__)


def test_benchmark::variant_constructor_args():
    sig = inspect.signature(benchmark::Variant.__init__)
    params = list(sig.parameters.keys())



def test_benchmark::inputdata_is_not_abstract():
    assert not inspect.isabstract(benchmark::InputData)


def test_benchmark::inputdata_constructor_exists():
    assert callable(benchmark::InputData.__init__)


def test_benchmark::inputdata_constructor_args():
    sig = inspect.signature(benchmark::InputData.__init__)
    params = list(sig.parameters.keys())



def test_benchmark::scenario_is_not_abstract():
    assert not inspect.isabstract(benchmark::Scenario)


def test_benchmark::scenario_constructor_exists():
    assert callable(benchmark::Scenario.__init__)


def test_benchmark::scenario_constructor_args():
    sig = inspect.signature(benchmark::Scenario.__init__)
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
benchmark::NamedElement_strategy = st.builds(
    benchmark::NamedElement,
    name=
        safe_text
)
benchmark::Property_strategy = st.builds(
    benchmark::Property,
    value=
        safe_text,
    name=
        safe_text
)
benchmark::TimeResult_strategy = st.builds(
    benchmark::TimeResult,
    elapsedTime=
        safe_text,
    elapsedMaxTime=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
benchmark::TestCase_strategy = st.builds(
    benchmark::TestCase,
)
benchmark::Variant_strategy = st.builds(
    benchmark::Variant,
)
benchmark::InputData_strategy = st.builds(
    benchmark::InputData,
)
benchmark::Scenario_strategy = st.builds(
    benchmark::Scenario,
)

@given(instance=benchmark::NamedElement_strategy)
@settings(max_examples=50)
def test_benchmark::namedelement_instantiation(instance):
    assert isinstance(instance, benchmark::NamedElement)

@given(instance=benchmark::NamedElement_strategy)
def test_benchmark::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=benchmark::NamedElement_strategy)
def test_benchmark::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=benchmark::Property_strategy)
@settings(max_examples=50)
def test_benchmark::property_instantiation(instance):
    assert isinstance(instance, benchmark::Property)

@given(instance=benchmark::Property_strategy)
def test_benchmark::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=benchmark::Property_strategy)
def test_benchmark::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=benchmark::Property_strategy)
def test_benchmark::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=benchmark::Property_strategy)
def test_benchmark::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=benchmark::TimeResult_strategy)
@settings(max_examples=50)
def test_benchmark::timeresult_instantiation(instance):
    assert isinstance(instance, benchmark::TimeResult)

@given(instance=benchmark::TimeResult_strategy)
def test_benchmark::timeresult_elapsedTime_type(instance):
    assert isinstance(instance.elapsedTime, str)


@given(instance=benchmark::TimeResult_strategy)
def test_benchmark::timeresult_elapsedTime_setter(instance):
    original = instance.elapsedTime
    instance.elapsedTime = original
    assert instance.elapsedTime == original

@given(instance=benchmark::TimeResult_strategy)
def test_benchmark::timeresult_elapsedMaxTime_type(instance):
    assert isinstance(instance.elapsedMaxTime, str)


@given(instance=benchmark::TimeResult_strategy)
def test_benchmark::timeresult_elapsedMaxTime_setter(instance):
    original = instance.elapsedMaxTime
    instance.elapsedMaxTime = original
    assert instance.elapsedMaxTime == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=benchmark::TestCase_strategy)
@settings(max_examples=50)
def test_benchmark::testcase_instantiation(instance):
    assert isinstance(instance, benchmark::TestCase)

@given(instance=benchmark::Variant_strategy)
@settings(max_examples=50)
def test_benchmark::variant_instantiation(instance):
    assert isinstance(instance, benchmark::Variant)

@given(instance=benchmark::InputData_strategy)
@settings(max_examples=50)
def test_benchmark::inputdata_instantiation(instance):
    assert isinstance(instance, benchmark::InputData)

@given(instance=benchmark::Scenario_strategy)
@settings(max_examples=50)
def test_benchmark::scenario_instantiation(instance):
    assert isinstance(instance, benchmark::Scenario)
