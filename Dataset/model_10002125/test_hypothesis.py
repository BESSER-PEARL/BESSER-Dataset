import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Bewegungssensor,
    Fenstersensor,
    T_rsensor,
    Sensoren,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bewegungssensor_is_not_abstract():
    assert not inspect.isabstract(Bewegungssensor)


def test_bewegungssensor_constructor_exists():
    assert callable(Bewegungssensor.__init__)


def test_bewegungssensor_constructor_args():
    sig = inspect.signature(Bewegungssensor.__init__)
    params = list(sig.parameters.keys())
    assert "bewegungssensorID" in params, "Missing parameter 'bewegungssensorID'"

def test_bewegungssensor_has_bewegungssensorID():
    assert hasattr(Bewegungssensor, "bewegungssensorID")
    descriptor = None
    for klass in Bewegungssensor.__mro__:
        if "bewegungssensorID" in klass.__dict__:
            descriptor = klass.__dict__["bewegungssensorID"]
            break
    assert isinstance(descriptor, property)



def test_fenstersensor_is_not_abstract():
    assert not inspect.isabstract(Fenstersensor)


def test_fenstersensor_constructor_exists():
    assert callable(Fenstersensor.__init__)


def test_fenstersensor_constructor_args():
    sig = inspect.signature(Fenstersensor.__init__)
    params = list(sig.parameters.keys())
    assert "fenstersensorID" in params, "Missing parameter 'fenstersensorID'"

def test_fenstersensor_has_fenstersensorID():
    assert hasattr(Fenstersensor, "fenstersensorID")
    descriptor = None
    for klass in Fenstersensor.__mro__:
        if "fenstersensorID" in klass.__dict__:
            descriptor = klass.__dict__["fenstersensorID"]
            break
    assert isinstance(descriptor, property)



def test_t_rsensor_is_not_abstract():
    assert not inspect.isabstract(T_rsensor)


def test_t_rsensor_constructor_exists():
    assert callable(T_rsensor.__init__)


def test_t_rsensor_constructor_args():
    sig = inspect.signature(T_rsensor.__init__)
    params = list(sig.parameters.keys())
    assert "t_rsensorID" in params, "Missing parameter 't_rsensorID'"

def test_t_rsensor_has_t_rsensorID():
    assert hasattr(T_rsensor, "t_rsensorID")
    descriptor = None
    for klass in T_rsensor.__mro__:
        if "t_rsensorID" in klass.__dict__:
            descriptor = klass.__dict__["t_rsensorID"]
            break
    assert isinstance(descriptor, property)



def test_sensoren_is_not_abstract():
    assert not inspect.isabstract(Sensoren)


def test_sensoren_constructor_exists():
    assert callable(Sensoren.__init__)


def test_sensoren_constructor_args():
    sig = inspect.signature(Sensoren.__init__)
    params = list(sig.parameters.keys())
    assert "sensorID" in params, "Missing parameter 'sensorID'"

def test_sensoren_has_sensorID():
    assert hasattr(Sensoren, "sensorID")
    descriptor = None
    for klass in Sensoren.__mro__:
        if "sensorID" in klass.__dict__:
            descriptor = klass.__dict__["sensorID"]
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
Bewegungssensor_strategy = st.builds(
    Bewegungssensor,
    bewegungssensorID=
        st.integers()
)
Fenstersensor_strategy = st.builds(
    Fenstersensor,
    fenstersensorID=
        st.integers()
)
T_rsensor_strategy = st.builds(
    T_rsensor,
    t_rsensorID=
        st.integers()
)
Sensoren_strategy = st.builds(
    Sensoren,
    sensorID=
        st.integers()
)

@given(instance=Bewegungssensor_strategy)
@settings(max_examples=50)
def test_bewegungssensor_instantiation(instance):
    assert isinstance(instance, Bewegungssensor)



@given(instance=Bewegungssensor_strategy)
def test_bewegungssensor_bewegungssensorID_setter(instance):
    original = instance.bewegungssensorID
    instance.bewegungssensorID = original
    assert instance.bewegungssensorID == original

@given(instance=Fenstersensor_strategy)
@settings(max_examples=50)
def test_fenstersensor_instantiation(instance):
    assert isinstance(instance, Fenstersensor)



@given(instance=Fenstersensor_strategy)
def test_fenstersensor_fenstersensorID_setter(instance):
    original = instance.fenstersensorID
    instance.fenstersensorID = original
    assert instance.fenstersensorID == original

@given(instance=T_rsensor_strategy)
@settings(max_examples=50)
def test_t_rsensor_instantiation(instance):
    assert isinstance(instance, T_rsensor)



@given(instance=T_rsensor_strategy)
def test_t_rsensor_t_rsensorID_setter(instance):
    original = instance.t_rsensorID
    instance.t_rsensorID = original
    assert instance.t_rsensorID == original

@given(instance=Sensoren_strategy)
@settings(max_examples=50)
def test_sensoren_instantiation(instance):
    assert isinstance(instance, Sensoren)



@given(instance=Sensoren_strategy)
def test_sensoren_sensorID_setter(instance):
    original = instance.sensorID
    instance.sensorID = original
    assert instance.sensorID == original
