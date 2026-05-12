import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SBCS::Transition,
    SBCS::SteamBoiler,
    SBCS::ControlProgram,
    Transition,
    SBCS::WaterLevelMeaurementDevice::getLevel,
    SBCS::PumpController::OpenPump,
    SBCS::SteamBoiler::OpenValve,
    SBCS::PumpController::ClosePump,
    SBCS::ControlProgram::Start,
    SBCS::Pump,
    SBCS::PumpControler,
    SBCS::WaterLevelMeasurementDevice,
    SBCS::Snapshot,
    State,
    ValveState,
    Mode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sbcs::transition_is_not_abstract():
    assert not inspect.isabstract(SBCS::Transition)


def test_sbcs::transition_constructor_exists():
    assert callable(SBCS::Transition.__init__)


def test_sbcs::transition_constructor_args():
    sig = inspect.signature(SBCS::Transition.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::steamboiler_is_not_abstract():
    assert not inspect.isabstract(SBCS::SteamBoiler)


def test_sbcs::steamboiler_constructor_exists():
    assert callable(SBCS::SteamBoiler.__init__)


def test_sbcs::steamboiler_constructor_args():
    sig = inspect.signature(SBCS::SteamBoiler.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "minimalNormal" in params, "Missing parameter 'minimalNormal'"
    assert "valveOpen" in params, "Missing parameter 'valveOpen'"
    assert "maximalNormal" in params, "Missing parameter 'maximalNormal'"

def test_sbcs::steamboiler_has_capacity():
    assert hasattr(SBCS::SteamBoiler, "capacity")
    descriptor = None
    for klass in SBCS::SteamBoiler.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_sbcs::steamboiler_has_minimalNormal():
    assert hasattr(SBCS::SteamBoiler, "minimalNormal")
    descriptor = None
    for klass in SBCS::SteamBoiler.__mro__:
        if "minimalNormal" in klass.__dict__:
            descriptor = klass.__dict__["minimalNormal"]
            break
    assert isinstance(descriptor, property)

def test_sbcs::steamboiler_has_valveOpen():
    assert hasattr(SBCS::SteamBoiler, "valveOpen")
    descriptor = None
    for klass in SBCS::SteamBoiler.__mro__:
        if "valveOpen" in klass.__dict__:
            descriptor = klass.__dict__["valveOpen"]
            break
    assert isinstance(descriptor, property)

def test_sbcs::steamboiler_has_maximalNormal():
    assert hasattr(SBCS::SteamBoiler, "maximalNormal")
    descriptor = None
    for klass in SBCS::SteamBoiler.__mro__:
        if "maximalNormal" in klass.__dict__:
            descriptor = klass.__dict__["maximalNormal"]
            break
    assert isinstance(descriptor, property)



def test_sbcs::controlprogram_is_not_abstract():
    assert not inspect.isabstract(SBCS::ControlProgram)


def test_sbcs::controlprogram_constructor_exists():
    assert callable(SBCS::ControlProgram.__init__)


def test_sbcs::controlprogram_constructor_args():
    sig = inspect.signature(SBCS::ControlProgram.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sbcs::controlprogram_has_mode():
    assert hasattr(SBCS::ControlProgram, "mode")
    descriptor = None
    for klass in SBCS::ControlProgram.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::waterlevelmeaurementdevice::getlevel_is_not_abstract():
    assert not inspect.isabstract(SBCS::WaterLevelMeaurementDevice::getLevel)


def test_sbcs::waterlevelmeaurementdevice::getlevel_constructor_exists():
    assert callable(SBCS::WaterLevelMeaurementDevice::getLevel.__init__)


def test_sbcs::waterlevelmeaurementdevice::getlevel_constructor_args():
    sig = inspect.signature(SBCS::WaterLevelMeaurementDevice::getLevel.__init__)
    params = list(sig.parameters.keys())
    assert "ret" in params, "Missing parameter 'ret'"

def test_sbcs::waterlevelmeaurementdevice::getlevel_has_ret():
    assert hasattr(SBCS::WaterLevelMeaurementDevice::getLevel, "ret")
    descriptor = None
    for klass in SBCS::WaterLevelMeaurementDevice::getLevel.__mro__:
        if "ret" in klass.__dict__:
            descriptor = klass.__dict__["ret"]
            break
    assert isinstance(descriptor, property)



def test_sbcs::pumpcontroller::openpump_is_not_abstract():
    assert not inspect.isabstract(SBCS::PumpController::OpenPump)


def test_sbcs::pumpcontroller::openpump_constructor_exists():
    assert callable(SBCS::PumpController::OpenPump.__init__)


def test_sbcs::pumpcontroller::openpump_constructor_args():
    sig = inspect.signature(SBCS::PumpController::OpenPump.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::steamboiler::openvalve_is_not_abstract():
    assert not inspect.isabstract(SBCS::SteamBoiler::OpenValve)


def test_sbcs::steamboiler::openvalve_constructor_exists():
    assert callable(SBCS::SteamBoiler::OpenValve.__init__)


def test_sbcs::steamboiler::openvalve_constructor_args():
    sig = inspect.signature(SBCS::SteamBoiler::OpenValve.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::pumpcontroller::closepump_is_not_abstract():
    assert not inspect.isabstract(SBCS::PumpController::ClosePump)


def test_sbcs::pumpcontroller::closepump_constructor_exists():
    assert callable(SBCS::PumpController::ClosePump.__init__)


def test_sbcs::pumpcontroller::closepump_constructor_args():
    sig = inspect.signature(SBCS::PumpController::ClosePump.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::controlprogram::start_is_not_abstract():
    assert not inspect.isabstract(SBCS::ControlProgram::Start)


def test_sbcs::controlprogram::start_constructor_exists():
    assert callable(SBCS::ControlProgram::Start.__init__)


def test_sbcs::controlprogram::start_constructor_args():
    sig = inspect.signature(SBCS::ControlProgram::Start.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::pump_is_not_abstract():
    assert not inspect.isabstract(SBCS::Pump)


def test_sbcs::pump_constructor_exists():
    assert callable(SBCS::Pump.__init__)


def test_sbcs::pump_constructor_args():
    sig = inspect.signature(SBCS::Pump.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sbcs::pump_has_mode():
    assert hasattr(SBCS::Pump, "mode")
    descriptor = None
    for klass in SBCS::Pump.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sbcs::pumpcontroler_is_not_abstract():
    assert not inspect.isabstract(SBCS::PumpControler)


def test_sbcs::pumpcontroler_constructor_exists():
    assert callable(SBCS::PumpControler.__init__)


def test_sbcs::pumpcontroler_constructor_args():
    sig = inspect.signature(SBCS::PumpControler.__init__)
    params = list(sig.parameters.keys())



def test_sbcs::waterlevelmeasurementdevice_is_not_abstract():
    assert not inspect.isabstract(SBCS::WaterLevelMeasurementDevice)


def test_sbcs::waterlevelmeasurementdevice_constructor_exists():
    assert callable(SBCS::WaterLevelMeasurementDevice.__init__)


def test_sbcs::waterlevelmeasurementdevice_constructor_args():
    sig = inspect.signature(SBCS::WaterLevelMeasurementDevice.__init__)
    params = list(sig.parameters.keys())
    assert "waterLevel" in params, "Missing parameter 'waterLevel'"

def test_sbcs::waterlevelmeasurementdevice_has_waterLevel():
    assert hasattr(SBCS::WaterLevelMeasurementDevice, "waterLevel")
    descriptor = None
    for klass in SBCS::WaterLevelMeasurementDevice.__mro__:
        if "waterLevel" in klass.__dict__:
            descriptor = klass.__dict__["waterLevel"]
            break
    assert isinstance(descriptor, property)



def test_sbcs::snapshot_is_not_abstract():
    assert not inspect.isabstract(SBCS::Snapshot)


def test_sbcs::snapshot_constructor_exists():
    assert callable(SBCS::Snapshot.__init__)


def test_sbcs::snapshot_constructor_args():
    sig = inspect.signature(SBCS::Snapshot.__init__)
    params = list(sig.parameters.keys())

def test_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
        "Off",
        "On",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"

def test_valvestate_exists():
    # Check that the Enumeration exists
    assert ValveState is not None

def test_valvestate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValveState]
    expected_literals = [
        "Closed",
        "Open",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValveState"

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "Initialization",
        "Dameged",
        "Normal",
        "EmergencyStop",
        "Rescue",
        "Degraded",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"


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
SBCS::Transition_strategy = st.builds(
    SBCS::Transition,
)
SBCS::SteamBoiler_strategy = st.builds(
    SBCS::SteamBoiler,
    capacity=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minimalNormal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    valveOpen=
        safe_text,
    maximalNormal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS::ControlProgram_strategy = st.builds(
    SBCS::ControlProgram,
    mode=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
SBCS::WaterLevelMeaurementDevice::getLevel_strategy = st.builds(
    SBCS::WaterLevelMeaurementDevice::getLevel,
    ret=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS::PumpController::OpenPump_strategy = st.builds(
    SBCS::PumpController::OpenPump,
)
SBCS::SteamBoiler::OpenValve_strategy = st.builds(
    SBCS::SteamBoiler::OpenValve,
)
SBCS::PumpController::ClosePump_strategy = st.builds(
    SBCS::PumpController::ClosePump,
)
SBCS::ControlProgram::Start_strategy = st.builds(
    SBCS::ControlProgram::Start,
)
SBCS::Pump_strategy = st.builds(
    SBCS::Pump,
    mode=
        safe_text
)
SBCS::PumpControler_strategy = st.builds(
    SBCS::PumpControler,
)
SBCS::WaterLevelMeasurementDevice_strategy = st.builds(
    SBCS::WaterLevelMeasurementDevice,
    waterLevel=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS::Snapshot_strategy = st.builds(
    SBCS::Snapshot,
)

@given(instance=SBCS::Transition_strategy)
@settings(max_examples=50)
def test_sbcs::transition_instantiation(instance):
    assert isinstance(instance, SBCS::Transition)

@given(instance=SBCS::SteamBoiler_strategy)
@settings(max_examples=50)
def test_sbcs::steamboiler_instantiation(instance):
    assert isinstance(instance, SBCS::SteamBoiler)

@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_capacity_type(instance):
    assert isinstance(instance.capacity, float)


@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_minimalNormal_type(instance):
    assert isinstance(instance.minimalNormal, float)


@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_minimalNormal_setter(instance):
    original = instance.minimalNormal
    instance.minimalNormal = original
    assert instance.minimalNormal == original

@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_valveOpen_type(instance):
    assert isinstance(instance.valveOpen, str)


@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_valveOpen_setter(instance):
    original = instance.valveOpen
    instance.valveOpen = original
    assert instance.valveOpen == original

@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_maximalNormal_type(instance):
    assert isinstance(instance.maximalNormal, float)


@given(instance=SBCS::SteamBoiler_strategy)
def test_sbcs::steamboiler_maximalNormal_setter(instance):
    original = instance.maximalNormal
    instance.maximalNormal = original
    assert instance.maximalNormal == original

@given(instance=SBCS::ControlProgram_strategy)
@settings(max_examples=50)
def test_sbcs::controlprogram_instantiation(instance):
    assert isinstance(instance, SBCS::ControlProgram)

@given(instance=SBCS::ControlProgram_strategy)
def test_sbcs::controlprogram_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=SBCS::ControlProgram_strategy)
def test_sbcs::controlprogram_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=SBCS::WaterLevelMeaurementDevice::getLevel_strategy)
@settings(max_examples=50)
def test_sbcs::waterlevelmeaurementdevice::getlevel_instantiation(instance):
    assert isinstance(instance, SBCS::WaterLevelMeaurementDevice::getLevel)

@given(instance=SBCS::WaterLevelMeaurementDevice::getLevel_strategy)
def test_sbcs::waterlevelmeaurementdevice::getlevel_ret_type(instance):
    assert isinstance(instance.ret, float)


@given(instance=SBCS::WaterLevelMeaurementDevice::getLevel_strategy)
def test_sbcs::waterlevelmeaurementdevice::getlevel_ret_setter(instance):
    original = instance.ret
    instance.ret = original
    assert instance.ret == original

@given(instance=SBCS::PumpController::OpenPump_strategy)
@settings(max_examples=50)
def test_sbcs::pumpcontroller::openpump_instantiation(instance):
    assert isinstance(instance, SBCS::PumpController::OpenPump)

@given(instance=SBCS::SteamBoiler::OpenValve_strategy)
@settings(max_examples=50)
def test_sbcs::steamboiler::openvalve_instantiation(instance):
    assert isinstance(instance, SBCS::SteamBoiler::OpenValve)

@given(instance=SBCS::PumpController::ClosePump_strategy)
@settings(max_examples=50)
def test_sbcs::pumpcontroller::closepump_instantiation(instance):
    assert isinstance(instance, SBCS::PumpController::ClosePump)

@given(instance=SBCS::ControlProgram::Start_strategy)
@settings(max_examples=50)
def test_sbcs::controlprogram::start_instantiation(instance):
    assert isinstance(instance, SBCS::ControlProgram::Start)

@given(instance=SBCS::Pump_strategy)
@settings(max_examples=50)
def test_sbcs::pump_instantiation(instance):
    assert isinstance(instance, SBCS::Pump)

@given(instance=SBCS::Pump_strategy)
def test_sbcs::pump_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=SBCS::Pump_strategy)
def test_sbcs::pump_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SBCS::PumpControler_strategy)
@settings(max_examples=50)
def test_sbcs::pumpcontroler_instantiation(instance):
    assert isinstance(instance, SBCS::PumpControler)

@given(instance=SBCS::WaterLevelMeasurementDevice_strategy)
@settings(max_examples=50)
def test_sbcs::waterlevelmeasurementdevice_instantiation(instance):
    assert isinstance(instance, SBCS::WaterLevelMeasurementDevice)

@given(instance=SBCS::WaterLevelMeasurementDevice_strategy)
def test_sbcs::waterlevelmeasurementdevice_waterLevel_type(instance):
    assert isinstance(instance.waterLevel, float)


@given(instance=SBCS::WaterLevelMeasurementDevice_strategy)
def test_sbcs::waterlevelmeasurementdevice_waterLevel_setter(instance):
    original = instance.waterLevel
    instance.waterLevel = original
    assert instance.waterLevel == original

@given(instance=SBCS::Snapshot_strategy)
@settings(max_examples=50)
def test_sbcs::snapshot_instantiation(instance):
    assert isinstance(instance, SBCS::Snapshot)
