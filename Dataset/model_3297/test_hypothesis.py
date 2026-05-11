import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Gaussian2ForcingDiseaseModel,
    forcing::Gaussian3ForcingDiseaseModel,
    StochasticSIRDiseaseModel,
    forcing::Gaussian2ForcingDiseaseModel,
    forcing::GaussianForcingDiseaseModel,
    forcing::ForcingDiseaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gaussian2forcingdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(Gaussian2ForcingDiseaseModel)


def test_gaussian2forcingdiseasemodel_constructor_exists():
    assert callable(Gaussian2ForcingDiseaseModel.__init__)


def test_gaussian2forcingdiseasemodel_constructor_args():
    sig = inspect.signature(Gaussian2ForcingDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_forcing::gaussian3forcingdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(forcing::Gaussian3ForcingDiseaseModel)


def test_forcing::gaussian3forcingdiseasemodel_constructor_exists():
    assert callable(forcing::Gaussian3ForcingDiseaseModel.__init__)


def test_forcing::gaussian3forcingdiseasemodel_constructor_args():
    sig = inspect.signature(forcing::Gaussian3ForcingDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "modulationFloor_2" in params, "Missing parameter 'modulationFloor_2'"
    assert "transmissionRate2" in params, "Missing parameter 'transmissionRate2'"
    assert "sigma2_3" in params, "Missing parameter 'sigma2_3'"
    assert "transmissionRate3" in params, "Missing parameter 'transmissionRate3'"

def test_forcing::gaussian3forcingdiseasemodel_has_modulationFloor_2():
    assert hasattr(forcing::Gaussian3ForcingDiseaseModel, "modulationFloor_2")
    descriptor = None
    for klass in forcing::Gaussian3ForcingDiseaseModel.__mro__:
        if "modulationFloor_2" in klass.__dict__:
            descriptor = klass.__dict__["modulationFloor_2"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian3forcingdiseasemodel_has_transmissionRate2():
    assert hasattr(forcing::Gaussian3ForcingDiseaseModel, "transmissionRate2")
    descriptor = None
    for klass in forcing::Gaussian3ForcingDiseaseModel.__mro__:
        if "transmissionRate2" in klass.__dict__:
            descriptor = klass.__dict__["transmissionRate2"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian3forcingdiseasemodel_has_sigma2_3():
    assert hasattr(forcing::Gaussian3ForcingDiseaseModel, "sigma2_3")
    descriptor = None
    for klass in forcing::Gaussian3ForcingDiseaseModel.__mro__:
        if "sigma2_3" in klass.__dict__:
            descriptor = klass.__dict__["sigma2_3"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian3forcingdiseasemodel_has_transmissionRate3():
    assert hasattr(forcing::Gaussian3ForcingDiseaseModel, "transmissionRate3")
    descriptor = None
    for klass in forcing::Gaussian3ForcingDiseaseModel.__mro__:
        if "transmissionRate3" in klass.__dict__:
            descriptor = klass.__dict__["transmissionRate3"]
            break
    assert isinstance(descriptor, property)



def test_stochasticsirdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(StochasticSIRDiseaseModel)


def test_stochasticsirdiseasemodel_constructor_exists():
    assert callable(StochasticSIRDiseaseModel.__init__)


def test_stochasticsirdiseasemodel_constructor_args():
    sig = inspect.signature(StochasticSIRDiseaseModel.__init__)
    params = list(sig.parameters.keys())



def test_forcing::gaussian2forcingdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(forcing::Gaussian2ForcingDiseaseModel)


def test_forcing::gaussian2forcingdiseasemodel_constructor_exists():
    assert callable(forcing::Gaussian2ForcingDiseaseModel.__init__)


def test_forcing::gaussian2forcingdiseasemodel_constructor_args():
    sig = inspect.signature(forcing::Gaussian2ForcingDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "sigma2" in params, "Missing parameter 'sigma2'"
    assert "att4" in params, "Missing parameter 'att4'"
    assert "modulationFloor" in params, "Missing parameter 'modulationFloor'"
    assert "att2" in params, "Missing parameter 'att2'"
    assert "att3" in params, "Missing parameter 'att3'"
    assert "modulationPeriod" in params, "Missing parameter 'modulationPeriod'"
    assert "att1" in params, "Missing parameter 'att1'"
    assert "modulationPhaseShift" in params, "Missing parameter 'modulationPhaseShift'"
    assert "sigma2_2" in params, "Missing parameter 'sigma2_2'"

def test_forcing::gaussian2forcingdiseasemodel_has_sigma2():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "sigma2")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "sigma2" in klass.__dict__:
            descriptor = klass.__dict__["sigma2"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_att4():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "att4")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "att4" in klass.__dict__:
            descriptor = klass.__dict__["att4"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_modulationFloor():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "modulationFloor")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "modulationFloor" in klass.__dict__:
            descriptor = klass.__dict__["modulationFloor"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_att2():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "att2")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_att3():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "att3")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "att3" in klass.__dict__:
            descriptor = klass.__dict__["att3"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_modulationPeriod():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "modulationPeriod")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "modulationPeriod" in klass.__dict__:
            descriptor = klass.__dict__["modulationPeriod"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_att1():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "att1")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_modulationPhaseShift():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "modulationPhaseShift")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "modulationPhaseShift" in klass.__dict__:
            descriptor = klass.__dict__["modulationPhaseShift"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussian2forcingdiseasemodel_has_sigma2_2():
    assert hasattr(forcing::Gaussian2ForcingDiseaseModel, "sigma2_2")
    descriptor = None
    for klass in forcing::Gaussian2ForcingDiseaseModel.__mro__:
        if "sigma2_2" in klass.__dict__:
            descriptor = klass.__dict__["sigma2_2"]
            break
    assert isinstance(descriptor, property)



def test_forcing::gaussianforcingdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(forcing::GaussianForcingDiseaseModel)


def test_forcing::gaussianforcingdiseasemodel_constructor_exists():
    assert callable(forcing::GaussianForcingDiseaseModel.__init__)


def test_forcing::gaussianforcingdiseasemodel_constructor_args():
    sig = inspect.signature(forcing::GaussianForcingDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "modulationFloor" in params, "Missing parameter 'modulationFloor'"
    assert "modulationPhaseShift" in params, "Missing parameter 'modulationPhaseShift'"
    assert "sigma2" in params, "Missing parameter 'sigma2'"
    assert "modulationPeriod" in params, "Missing parameter 'modulationPeriod'"

def test_forcing::gaussianforcingdiseasemodel_has_modulationFloor():
    assert hasattr(forcing::GaussianForcingDiseaseModel, "modulationFloor")
    descriptor = None
    for klass in forcing::GaussianForcingDiseaseModel.__mro__:
        if "modulationFloor" in klass.__dict__:
            descriptor = klass.__dict__["modulationFloor"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussianforcingdiseasemodel_has_modulationPhaseShift():
    assert hasattr(forcing::GaussianForcingDiseaseModel, "modulationPhaseShift")
    descriptor = None
    for klass in forcing::GaussianForcingDiseaseModel.__mro__:
        if "modulationPhaseShift" in klass.__dict__:
            descriptor = klass.__dict__["modulationPhaseShift"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussianforcingdiseasemodel_has_sigma2():
    assert hasattr(forcing::GaussianForcingDiseaseModel, "sigma2")
    descriptor = None
    for klass in forcing::GaussianForcingDiseaseModel.__mro__:
        if "sigma2" in klass.__dict__:
            descriptor = klass.__dict__["sigma2"]
            break
    assert isinstance(descriptor, property)

def test_forcing::gaussianforcingdiseasemodel_has_modulationPeriod():
    assert hasattr(forcing::GaussianForcingDiseaseModel, "modulationPeriod")
    descriptor = None
    for klass in forcing::GaussianForcingDiseaseModel.__mro__:
        if "modulationPeriod" in klass.__dict__:
            descriptor = klass.__dict__["modulationPeriod"]
            break
    assert isinstance(descriptor, property)



def test_forcing::forcingdiseasemodel_is_not_abstract():
    assert not inspect.isabstract(forcing::ForcingDiseaseModel)


def test_forcing::forcingdiseasemodel_constructor_exists():
    assert callable(forcing::ForcingDiseaseModel.__init__)


def test_forcing::forcingdiseasemodel_constructor_args():
    sig = inspect.signature(forcing::ForcingDiseaseModel.__init__)
    params = list(sig.parameters.keys())
    assert "modulationPeriod" in params, "Missing parameter 'modulationPeriod'"
    assert "seasonalModulationFloor" in params, "Missing parameter 'seasonalModulationFloor'"
    assert "seasonalModulationExponent" in params, "Missing parameter 'seasonalModulationExponent'"
    assert "modulationPhaseShift" in params, "Missing parameter 'modulationPhaseShift'"

def test_forcing::forcingdiseasemodel_has_modulationPeriod():
    assert hasattr(forcing::ForcingDiseaseModel, "modulationPeriod")
    descriptor = None
    for klass in forcing::ForcingDiseaseModel.__mro__:
        if "modulationPeriod" in klass.__dict__:
            descriptor = klass.__dict__["modulationPeriod"]
            break
    assert isinstance(descriptor, property)

def test_forcing::forcingdiseasemodel_has_seasonalModulationFloor():
    assert hasattr(forcing::ForcingDiseaseModel, "seasonalModulationFloor")
    descriptor = None
    for klass in forcing::ForcingDiseaseModel.__mro__:
        if "seasonalModulationFloor" in klass.__dict__:
            descriptor = klass.__dict__["seasonalModulationFloor"]
            break
    assert isinstance(descriptor, property)

def test_forcing::forcingdiseasemodel_has_seasonalModulationExponent():
    assert hasattr(forcing::ForcingDiseaseModel, "seasonalModulationExponent")
    descriptor = None
    for klass in forcing::ForcingDiseaseModel.__mro__:
        if "seasonalModulationExponent" in klass.__dict__:
            descriptor = klass.__dict__["seasonalModulationExponent"]
            break
    assert isinstance(descriptor, property)

def test_forcing::forcingdiseasemodel_has_modulationPhaseShift():
    assert hasattr(forcing::ForcingDiseaseModel, "modulationPhaseShift")
    descriptor = None
    for klass in forcing::ForcingDiseaseModel.__mro__:
        if "modulationPhaseShift" in klass.__dict__:
            descriptor = klass.__dict__["modulationPhaseShift"]
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
Gaussian2ForcingDiseaseModel_strategy = st.builds(
    Gaussian2ForcingDiseaseModel,
)
forcing::Gaussian3ForcingDiseaseModel_strategy = st.builds(
    forcing::Gaussian3ForcingDiseaseModel,
    modulationFloor_2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transmissionRate2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    sigma2_3=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    transmissionRate3=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
StochasticSIRDiseaseModel_strategy = st.builds(
    StochasticSIRDiseaseModel,
)
forcing::Gaussian2ForcingDiseaseModel_strategy = st.builds(
    forcing::Gaussian2ForcingDiseaseModel,
    sigma2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    att4=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationFloor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    att2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    att3=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPeriod=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    att1=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPhaseShift=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    sigma2_2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
forcing::GaussianForcingDiseaseModel_strategy = st.builds(
    forcing::GaussianForcingDiseaseModel,
    modulationFloor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPhaseShift=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    sigma2=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPeriod=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
forcing::ForcingDiseaseModel_strategy = st.builds(
    forcing::ForcingDiseaseModel,
    modulationPeriod=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationFloor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    seasonalModulationExponent=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    modulationPhaseShift=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Gaussian2ForcingDiseaseModel_strategy)
@settings(max_examples=50)
def test_gaussian2forcingdiseasemodel_instantiation(instance):
    assert isinstance(instance, Gaussian2ForcingDiseaseModel)

@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
@settings(max_examples=50)
def test_forcing::gaussian3forcingdiseasemodel_instantiation(instance):
    assert isinstance(instance, forcing::Gaussian3ForcingDiseaseModel)

@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_modulationFloor_2_type(instance):
    assert isinstance(instance.modulationFloor_2, float)


@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_modulationFloor_2_setter(instance):
    original = instance.modulationFloor_2
    instance.modulationFloor_2 = original
    assert instance.modulationFloor_2 == original

@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_transmissionRate2_type(instance):
    assert isinstance(instance.transmissionRate2, float)


@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_transmissionRate2_setter(instance):
    original = instance.transmissionRate2
    instance.transmissionRate2 = original
    assert instance.transmissionRate2 == original

@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_sigma2_3_type(instance):
    assert isinstance(instance.sigma2_3, float)


@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_sigma2_3_setter(instance):
    original = instance.sigma2_3
    instance.sigma2_3 = original
    assert instance.sigma2_3 == original

@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_transmissionRate3_type(instance):
    assert isinstance(instance.transmissionRate3, float)


@given(instance=forcing::Gaussian3ForcingDiseaseModel_strategy)
def test_forcing::gaussian3forcingdiseasemodel_transmissionRate3_setter(instance):
    original = instance.transmissionRate3
    instance.transmissionRate3 = original
    assert instance.transmissionRate3 == original

@given(instance=StochasticSIRDiseaseModel_strategy)
@settings(max_examples=50)
def test_stochasticsirdiseasemodel_instantiation(instance):
    assert isinstance(instance, StochasticSIRDiseaseModel)

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
@settings(max_examples=50)
def test_forcing::gaussian2forcingdiseasemodel_instantiation(instance):
    assert isinstance(instance, forcing::Gaussian2ForcingDiseaseModel)

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_sigma2_type(instance):
    assert isinstance(instance.sigma2, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_sigma2_setter(instance):
    original = instance.sigma2
    instance.sigma2 = original
    assert instance.sigma2 == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att4_type(instance):
    assert isinstance(instance.att4, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att4_setter(instance):
    original = instance.att4
    instance.att4 = original
    assert instance.att4 == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationFloor_type(instance):
    assert isinstance(instance.modulationFloor, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationFloor_setter(instance):
    original = instance.modulationFloor
    instance.modulationFloor = original
    assert instance.modulationFloor == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att2_type(instance):
    assert isinstance(instance.att2, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att3_type(instance):
    assert isinstance(instance.att3, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att3_setter(instance):
    original = instance.att3
    instance.att3 = original
    assert instance.att3 == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationPeriod_type(instance):
    assert isinstance(instance.modulationPeriod, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationPeriod_setter(instance):
    original = instance.modulationPeriod
    instance.modulationPeriod = original
    assert instance.modulationPeriod == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att1_type(instance):
    assert isinstance(instance.att1, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationPhaseShift_type(instance):
    assert isinstance(instance.modulationPhaseShift, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_modulationPhaseShift_setter(instance):
    original = instance.modulationPhaseShift
    instance.modulationPhaseShift = original
    assert instance.modulationPhaseShift == original

@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_sigma2_2_type(instance):
    assert isinstance(instance.sigma2_2, float)


@given(instance=forcing::Gaussian2ForcingDiseaseModel_strategy)
def test_forcing::gaussian2forcingdiseasemodel_sigma2_2_setter(instance):
    original = instance.sigma2_2
    instance.sigma2_2 = original
    assert instance.sigma2_2 == original

@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
@settings(max_examples=50)
def test_forcing::gaussianforcingdiseasemodel_instantiation(instance):
    assert isinstance(instance, forcing::GaussianForcingDiseaseModel)

@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationFloor_type(instance):
    assert isinstance(instance.modulationFloor, float)


@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationFloor_setter(instance):
    original = instance.modulationFloor
    instance.modulationFloor = original
    assert instance.modulationFloor == original

@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationPhaseShift_type(instance):
    assert isinstance(instance.modulationPhaseShift, float)


@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationPhaseShift_setter(instance):
    original = instance.modulationPhaseShift
    instance.modulationPhaseShift = original
    assert instance.modulationPhaseShift == original

@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_sigma2_type(instance):
    assert isinstance(instance.sigma2, float)


@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_sigma2_setter(instance):
    original = instance.sigma2
    instance.sigma2 = original
    assert instance.sigma2 == original

@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationPeriod_type(instance):
    assert isinstance(instance.modulationPeriod, float)


@given(instance=forcing::GaussianForcingDiseaseModel_strategy)
def test_forcing::gaussianforcingdiseasemodel_modulationPeriod_setter(instance):
    original = instance.modulationPeriod
    instance.modulationPeriod = original
    assert instance.modulationPeriod == original

@given(instance=forcing::ForcingDiseaseModel_strategy)
@settings(max_examples=50)
def test_forcing::forcingdiseasemodel_instantiation(instance):
    assert isinstance(instance, forcing::ForcingDiseaseModel)

@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_modulationPeriod_type(instance):
    assert isinstance(instance.modulationPeriod, float)


@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_modulationPeriod_setter(instance):
    original = instance.modulationPeriod
    instance.modulationPeriod = original
    assert instance.modulationPeriod == original

@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_seasonalModulationFloor_type(instance):
    assert isinstance(instance.seasonalModulationFloor, float)


@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_seasonalModulationFloor_setter(instance):
    original = instance.seasonalModulationFloor
    instance.seasonalModulationFloor = original
    assert instance.seasonalModulationFloor == original

@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_seasonalModulationExponent_type(instance):
    assert isinstance(instance.seasonalModulationExponent, float)


@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_seasonalModulationExponent_setter(instance):
    original = instance.seasonalModulationExponent
    instance.seasonalModulationExponent = original
    assert instance.seasonalModulationExponent == original

@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_modulationPhaseShift_type(instance):
    assert isinstance(instance.modulationPhaseShift, float)


@given(instance=forcing::ForcingDiseaseModel_strategy)
def test_forcing::forcingdiseasemodel_modulationPhaseShift_setter(instance):
    original = instance.modulationPhaseShift
    instance.modulationPhaseShift = original
    assert instance.modulationPhaseShift == original
