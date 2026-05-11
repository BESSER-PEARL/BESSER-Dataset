import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::Observation,
    ModelElement,
    Measurement,
    metrics::ComplexMeasurement,
    metrics::ValueMeasurement,
    metrics::Measurement,
    metrics::LinkMeasurement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::observation_is_not_abstract():
    assert not inspect.isabstract(metrics::Observation)


def test_metrics::observation_constructor_exists():
    assert callable(metrics::Observation.__init__)


def test_metrics::observation_constructor_args():
    sig = inspect.signature(metrics::Observation.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_measurement_is_not_abstract():
    assert not inspect.isabstract(Measurement)


def test_measurement_constructor_exists():
    assert callable(Measurement.__init__)


def test_measurement_constructor_args():
    sig = inspect.signature(Measurement.__init__)
    params = list(sig.parameters.keys())



def test_metrics::complexmeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics::ComplexMeasurement)


def test_metrics::complexmeasurement_constructor_exists():
    assert callable(metrics::ComplexMeasurement.__init__)


def test_metrics::complexmeasurement_constructor_args():
    sig = inspect.signature(metrics::ComplexMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_metrics::valuemeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics::ValueMeasurement)


def test_metrics::valuemeasurement_constructor_exists():
    assert callable(metrics::ValueMeasurement.__init__)


def test_metrics::valuemeasurement_constructor_args():
    sig = inspect.signature(metrics::ValueMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metrics::valuemeasurement_has_value():
    assert hasattr(metrics::ValueMeasurement, "value")
    descriptor = None
    for klass in metrics::ValueMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metrics::measurement_is_not_abstract():
    assert not inspect.isabstract(metrics::Measurement)


def test_metrics::measurement_constructor_exists():
    assert callable(metrics::Measurement.__init__)


def test_metrics::measurement_constructor_args():
    sig = inspect.signature(metrics::Measurement.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"
    assert "name" in params, "Missing parameter 'name'"
    assert "error" in params, "Missing parameter 'error'"

def test_metrics::measurement_has_tag():
    assert hasattr(metrics::Measurement, "tag")
    descriptor = None
    for klass in metrics::Measurement.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_metrics::measurement_has_name():
    assert hasattr(metrics::Measurement, "name")
    descriptor = None
    for klass in metrics::Measurement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics::measurement_has_error():
    assert hasattr(metrics::Measurement, "error")
    descriptor = None
    for klass in metrics::Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)



def test_metrics::linkmeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics::LinkMeasurement)


def test_metrics::linkmeasurement_constructor_exists():
    assert callable(metrics::LinkMeasurement.__init__)


def test_metrics::linkmeasurement_constructor_args():
    sig = inspect.signature(metrics::LinkMeasurement.__init__)
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
metrics::Observation_strategy = st.builds(
    metrics::Observation,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
Measurement_strategy = st.builds(
    Measurement,
)
metrics::ComplexMeasurement_strategy = st.builds(
    metrics::ComplexMeasurement,
)
metrics::ValueMeasurement_strategy = st.builds(
    metrics::ValueMeasurement,
    value=
        safe_text
)
metrics::Measurement_strategy = st.builds(
    metrics::Measurement,
    tag=
        safe_text,
    name=
        safe_text,
    error=
        safe_text
)
metrics::LinkMeasurement_strategy = st.builds(
    metrics::LinkMeasurement,
)

@given(instance=metrics::Observation_strategy)
@settings(max_examples=50)
def test_metrics::observation_instantiation(instance):
    assert isinstance(instance, metrics::Observation)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=metrics::ComplexMeasurement_strategy)
@settings(max_examples=50)
def test_metrics::complexmeasurement_instantiation(instance):
    assert isinstance(instance, metrics::ComplexMeasurement)

@given(instance=metrics::ValueMeasurement_strategy)
@settings(max_examples=50)
def test_metrics::valuemeasurement_instantiation(instance):
    assert isinstance(instance, metrics::ValueMeasurement)

@given(instance=metrics::ValueMeasurement_strategy)
def test_metrics::valuemeasurement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=metrics::ValueMeasurement_strategy)
def test_metrics::valuemeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metrics::Measurement_strategy)
@settings(max_examples=50)
def test_metrics::measurement_instantiation(instance):
    assert isinstance(instance, metrics::Measurement)

@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_error_type(instance):
    assert isinstance(instance.error, str)


@given(instance=metrics::Measurement_strategy)
def test_metrics::measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original

@given(instance=metrics::LinkMeasurement_strategy)
@settings(max_examples=50)
def test_metrics::linkmeasurement_instantiation(instance):
    assert isinstance(instance, metrics::LinkMeasurement)
