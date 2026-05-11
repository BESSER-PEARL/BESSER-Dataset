import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StochasticSIRDiseaseModel,
    example::ExampleDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_stochasticsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StochasticSIRDiseaseModel)


def test_stochasticsirdiseasemodel_constructor_exists():
    assert callable(StochasticSIRDiseaseModel.__init__)


def test_stochasticsirdiseasemodel_constructor_args():
    sig = inspect.signature(StochasticSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_example::examplediseasemodel_is_not_abstract():
    assert not inspect.isabstract(example::ExampleDiseaseModel)


def test_example::examplediseasemodel_constructor_exists():
    assert callable(example::ExampleDiseaseModel.__init__)


def test_example::examplediseasemodel_constructor_args():
    sig = inspect.signature(example::ExampleDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "modulationPeriod" in params, "Missing parameter 'modulationPeriod'"
    assert "seasonalModulationFloor" in params, "Missing parameter 'seasonalModulationFloor'"
    assert "modulationPhaseShift" in params, "Missing parameter 'modulationPhaseShift'"
    assert "seasonalModulationExponent" in params, "Missing parameter 'seasonalModulationExponent'"

def test_example::examplediseasemodel_has_modulationPeriod():
    assert hasattr(example::ExampleDiseaseModel, "modulationPeriod")
    descriptor = None
    for klass in example::ExampleDiseaseModel.__mro__:
        if "modulationPeriod" in klass.__dict__:
            descriptor = klass.__dict__["modulationPeriod"]
            break
    assert isinstance(descriptor, property)

def test_example::examplediseasemodel_has_seasonalModulationFloor():
    assert hasattr(example::ExampleDiseaseModel, "seasonalModulationFloor")
    descriptor = None
    for klass in example::ExampleDiseaseModel.__mro__:
        if "seasonalModulationFloor" in klass.__dict__:
            descriptor = klass.__dict__["seasonalModulationFloor"]
            break
    assert isinstance(descriptor, property)

def test_example::examplediseasemodel_has_modulationPhaseShift():
    assert hasattr(example::ExampleDiseaseModel, "modulationPhaseShift")
    descriptor = None
    for klass in example::ExampleDiseaseModel.__mro__:
        if "modulationPhaseShift" in klass.__dict__:
            descriptor = klass.__dict__["modulationPhaseShift"]
            break
    assert isinstance(descriptor, property)

def test_example::examplediseasemodel_has_seasonalModulationExponent():
    assert hasattr(example::ExampleDiseaseModel, "seasonalModulationExponent")
    descriptor = None
    for klass in example::ExampleDiseaseModel.__mro__:
        if "seasonalModulationExponent" in klass.__dict__:
            descriptor = klass.__dict__["seasonalModulationExponent"]
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
StochasticSIRDiseaseModel_strategy = st.builds(
    StochasticSIRDiseaseModel,
)
example::ExampleDiseaseModel_strategy = st.builds(
    example::ExampleDiseaseModel,
    modulationPeriod=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationFloor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPhaseShift=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationExponent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=StochasticSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_stochasticsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, StochasticSIRDiseaseModel)

@given(instance=example::ExampleDiseaseModel_strategy)
@settings(max_examples=50)
def test_example::examplediseasemodel_instantiation(instance):
    assert isinstance(instance, example::ExampleDiseaseModel)

@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_modulationPeriod_type(instance):
    assert isinstance(instance.modulationPeriod, float)


@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_modulationPeriod_setter(instance):
    original = instance.modulationPeriod
    instance.modulationPeriod = original
    assert instance.modulationPeriod == original

@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_seasonalModulationFloor_type(instance):
    assert isinstance(instance.seasonalModulationFloor, float)


@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_seasonalModulationFloor_setter(instance):
    original = instance.seasonalModulationFloor
    instance.seasonalModulationFloor = original
    assert instance.seasonalModulationFloor == original

@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_modulationPhaseShift_type(instance):
    assert isinstance(instance.modulationPhaseShift, float)


@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_modulationPhaseShift_setter(instance):
    original = instance.modulationPhaseShift
    instance.modulationPhaseShift = original
    assert instance.modulationPhaseShift == original

@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_seasonalModulationExponent_type(instance):
    assert isinstance(instance.seasonalModulationExponent, float)


@given(instance=example::ExampleDiseaseModel_strategy)
def test_example::examplediseasemodel_seasonalModulationExponent_setter(instance):
    original = instance.seasonalModulationExponent
    instance.seasonalModulationExponent = original
    assert instance.seasonalModulationExponent == original
