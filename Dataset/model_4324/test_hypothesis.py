import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metrics_Observation,
    ModelElement,
    Measurement,
    metrics_ComplexMeasurement,
    metrics_ValueMeasurement,
    metrics_Measurement,
    metrics_LinkMeasurement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics_observation_is_not_abstract():
    assert not inspect.isabstract(metrics_Observation)


def test_metrics_observation_constructor_exists():
    assert callable(metrics_Observation.__init__)


def test_metrics_observation_constructor_args():
    sig = inspect.signature(metrics_Observation.__init__)
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



def test_metrics_complexmeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics_ComplexMeasurement)


def test_metrics_complexmeasurement_constructor_exists():
    assert callable(metrics_ComplexMeasurement.__init__)


def test_metrics_complexmeasurement_constructor_args():
    sig = inspect.signature(metrics_ComplexMeasurement.__init__)
    params = list(sig.parameters.keys())



def test_metrics_valuemeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics_ValueMeasurement)


def test_metrics_valuemeasurement_constructor_exists():
    assert callable(metrics_ValueMeasurement.__init__)


def test_metrics_valuemeasurement_constructor_args():
    sig = inspect.signature(metrics_ValueMeasurement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_metrics_valuemeasurement_has_value():
    assert hasattr(metrics_ValueMeasurement, "value")
    descriptor = None
    for klass in metrics_ValueMeasurement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_metrics_measurement_is_not_abstract():
    assert not inspect.isabstract(metrics_Measurement)


def test_metrics_measurement_constructor_exists():
    assert callable(metrics_Measurement.__init__)


def test_metrics_measurement_constructor_args():
    sig = inspect.signature(metrics_Measurement.__init__)
    params = list(sig.parameters.keys())
    assert "error" in params, "Missing parameter 'error'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics_measurement_has_error():
    assert hasattr(metrics_Measurement, "error")
    descriptor = None
    for klass in metrics_Measurement.__mro__:
        if "error" in klass.__dict__:
            descriptor = klass.__dict__["error"]
            break
    assert isinstance(descriptor, property)

def test_metrics_measurement_has_tag():
    assert hasattr(metrics_Measurement, "tag")
    descriptor = None
    for klass in metrics_Measurement.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_metrics_measurement_has_name():
    assert hasattr(metrics_Measurement, "name")
    descriptor = None
    for klass in metrics_Measurement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics_linkmeasurement_is_not_abstract():
    assert not inspect.isabstract(metrics_LinkMeasurement)


def test_metrics_linkmeasurement_constructor_exists():
    assert callable(metrics_LinkMeasurement.__init__)


def test_metrics_linkmeasurement_constructor_args():
    sig = inspect.signature(metrics_LinkMeasurement.__init__)
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
metrics_Observation_strategy = st.builds(
    metrics_Observation,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
Measurement_strategy = st.builds(
    Measurement,
)
metrics_ComplexMeasurement_strategy = st.builds(
    metrics_ComplexMeasurement,
)
metrics_ValueMeasurement_strategy = st.builds(
    metrics_ValueMeasurement,
    value=
        safe_text
)
metrics_Measurement_strategy = st.builds(
    metrics_Measurement,
    error=
        safe_text,
    tag=
        safe_text,
    name=
        safe_text
)
metrics_LinkMeasurement_strategy = st.builds(
    metrics_LinkMeasurement,
)

@given(instance=metrics_Observation_strategy)
@settings(max_examples=50)
def test_metrics_observation_instantiation(instance):
    assert isinstance(instance, metrics_Observation)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=Measurement_strategy)
@settings(max_examples=50)
def test_measurement_instantiation(instance):
    assert isinstance(instance, Measurement)

@given(instance=metrics_ComplexMeasurement_strategy)
@settings(max_examples=50)
def test_metrics_complexmeasurement_instantiation(instance):
    assert isinstance(instance, metrics_ComplexMeasurement)

@given(instance=metrics_ValueMeasurement_strategy)
@settings(max_examples=50)
def test_metrics_valuemeasurement_instantiation(instance):
    assert isinstance(instance, metrics_ValueMeasurement)



@given(instance=metrics_ValueMeasurement_strategy)
def test_metrics_valuemeasurement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=metrics_Measurement_strategy)
@settings(max_examples=50)
def test_metrics_measurement_instantiation(instance):
    assert isinstance(instance, metrics_Measurement)



@given(instance=metrics_Measurement_strategy)
def test_metrics_measurement_error_setter(instance):
    original = instance.error
    instance.error = original
    assert instance.error == original



@given(instance=metrics_Measurement_strategy)
def test_metrics_measurement_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=metrics_Measurement_strategy)
def test_metrics_measurement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics_LinkMeasurement_strategy)
@settings(max_examples=50)
def test_metrics_linkmeasurement_instantiation(instance):
    assert isinstance(instance, metrics_LinkMeasurement)
