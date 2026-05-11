import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traces::Value,
    traces::Variable,
    traces::SimulatorRun,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traces::value_is_not_abstract():
    assert not inspect.isabstract(traces::Value)


def test_traces::value_constructor_exists():
    assert callable(traces::Value.__init__)


def test_traces::value_constructor_args():
    sig = inspect.signature(traces::Value.__init__)
    params = list(sig.parameters.keys())
    assert "valueMax" in params, "Missing parameter 'valueMax'"
    assert "valueMin" in params, "Missing parameter 'valueMin'"
    assert "clockMin" in params, "Missing parameter 'clockMin'"
    assert "clockMax" in params, "Missing parameter 'clockMax'"

def test_traces::value_has_valueMax():
    assert hasattr(traces::Value, "valueMax")
    descriptor = None
    for klass in traces::Value.__mro__:
        if "valueMax" in klass.__dict__:
            descriptor = klass.__dict__["valueMax"]
            break
    assert isinstance(descriptor, property)

def test_traces::value_has_valueMin():
    assert hasattr(traces::Value, "valueMin")
    descriptor = None
    for klass in traces::Value.__mro__:
        if "valueMin" in klass.__dict__:
            descriptor = klass.__dict__["valueMin"]
            break
    assert isinstance(descriptor, property)

def test_traces::value_has_clockMin():
    assert hasattr(traces::Value, "clockMin")
    descriptor = None
    for klass in traces::Value.__mro__:
        if "clockMin" in klass.__dict__:
            descriptor = klass.__dict__["clockMin"]
            break
    assert isinstance(descriptor, property)

def test_traces::value_has_clockMax():
    assert hasattr(traces::Value, "clockMax")
    descriptor = None
    for klass in traces::Value.__mro__:
        if "clockMax" in klass.__dict__:
            descriptor = klass.__dict__["clockMax"]
            break
    assert isinstance(descriptor, property)



def test_traces::variable_is_not_abstract():
    assert not inspect.isabstract(traces::Variable)


def test_traces::variable_constructor_exists():
    assert callable(traces::Variable.__init__)


def test_traces::variable_constructor_args():
    sig = inspect.signature(traces::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_traces::variable_has_name():
    assert hasattr(traces::Variable, "name")
    descriptor = None
    for klass in traces::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_traces::simulatorrun_is_not_abstract():
    assert not inspect.isabstract(traces::SimulatorRun)


def test_traces::simulatorrun_constructor_exists():
    assert callable(traces::SimulatorRun.__init__)


def test_traces::simulatorrun_constructor_args():
    sig = inspect.signature(traces::SimulatorRun.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "behaviorName" in params, "Missing parameter 'behaviorName'"

def test_traces::simulatorrun_has_id():
    assert hasattr(traces::SimulatorRun, "id")
    descriptor = None
    for klass in traces::SimulatorRun.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_traces::simulatorrun_has_timestamp():
    assert hasattr(traces::SimulatorRun, "timestamp")
    descriptor = None
    for klass in traces::SimulatorRun.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_traces::simulatorrun_has_behaviorName():
    assert hasattr(traces::SimulatorRun, "behaviorName")
    descriptor = None
    for klass in traces::SimulatorRun.__mro__:
        if "behaviorName" in klass.__dict__:
            descriptor = klass.__dict__["behaviorName"]
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
traces::Value_strategy = st.builds(
    traces::Value,
    valueMax=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    valueMin=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    clockMin=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    clockMax=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
traces::Variable_strategy = st.builds(
    traces::Variable,
    name=
        safe_text
)
traces::SimulatorRun_strategy = st.builds(
    traces::SimulatorRun,
    id=
        st.integers(),
    timestamp=
        st.dates(),
    behaviorName=
        safe_text
)

@given(instance=traces::Value_strategy)
@settings(max_examples=50)
def test_traces::value_instantiation(instance):
    assert isinstance(instance, traces::Value)

@given(instance=traces::Value_strategy)
def test_traces::value_valueMax_type(instance):
    assert isinstance(instance.valueMax, float)


@given(instance=traces::Value_strategy)
def test_traces::value_valueMax_setter(instance):
    original = instance.valueMax
    instance.valueMax = original
    assert instance.valueMax == original

@given(instance=traces::Value_strategy)
def test_traces::value_valueMin_type(instance):
    assert isinstance(instance.valueMin, float)


@given(instance=traces::Value_strategy)
def test_traces::value_valueMin_setter(instance):
    original = instance.valueMin
    instance.valueMin = original
    assert instance.valueMin == original

@given(instance=traces::Value_strategy)
def test_traces::value_clockMin_type(instance):
    assert isinstance(instance.clockMin, float)


@given(instance=traces::Value_strategy)
def test_traces::value_clockMin_setter(instance):
    original = instance.clockMin
    instance.clockMin = original
    assert instance.clockMin == original

@given(instance=traces::Value_strategy)
def test_traces::value_clockMax_type(instance):
    assert isinstance(instance.clockMax, float)


@given(instance=traces::Value_strategy)
def test_traces::value_clockMax_setter(instance):
    original = instance.clockMax
    instance.clockMax = original
    assert instance.clockMax == original

@given(instance=traces::Variable_strategy)
@settings(max_examples=50)
def test_traces::variable_instantiation(instance):
    assert isinstance(instance, traces::Variable)

@given(instance=traces::Variable_strategy)
def test_traces::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traces::Variable_strategy)
def test_traces::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=traces::SimulatorRun_strategy)
@settings(max_examples=50)
def test_traces::simulatorrun_instantiation(instance):
    assert isinstance(instance, traces::SimulatorRun)

@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_behaviorName_type(instance):
    assert isinstance(instance.behaviorName, str)


@given(instance=traces::SimulatorRun_strategy)
def test_traces::simulatorrun_behaviorName_setter(instance):
    original = instance.behaviorName
    instance.behaviorName = original
    assert instance.behaviorName == original
