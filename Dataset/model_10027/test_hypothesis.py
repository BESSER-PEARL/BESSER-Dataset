import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SBCS_PumpControler,
    Transition,
    SBCS_WaterLevelMeaurementDevice_getLevel,
    SBCS_PumpController_ClosePump,
    SBCS_ControlProgram_Start,
    SBCS_PumpController_OpenPump,
    SBCS_Transition,
    SBCS_ControlProgram,
    SBCS_Snapshot,
    SBCS_Pump,
    SBCS_SteamBoiler,
    SBCS_SteamBoiler_OpenValve,
    SBCS_WaterLevelMeasurementDevice,
    State,
    Mode,
    ValveState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sbcs_pumpcontroler_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpControler)


def test_sbcs_pumpcontroler_constructor_exists():
    assert callable(SBCS_PumpControler.__init__)


def test_sbcs_pumpcontroler_constructor_args():
    sig = inspect.signature(SBCS_PumpControler.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_waterlevelmeaurementdevice_getlevel_is_not_abstract():
    assert not inspect.isabstract(SBCS_WaterLevelMeaurementDevice_getLevel)


def test_sbcs_waterlevelmeaurementdevice_getlevel_constructor_exists():
    assert callable(SBCS_WaterLevelMeaurementDevice_getLevel.__init__)


def test_sbcs_waterlevelmeaurementdevice_getlevel_constructor_args():
    sig = inspect.signature(SBCS_WaterLevelMeaurementDevice_getLevel.__init__)
    params = list(sig.parameters.keys())
    assert "ret" in params, "Missing parameter 'ret'"

def test_sbcs_waterlevelmeaurementdevice_getlevel_has_ret():
    assert hasattr(SBCS_WaterLevelMeaurementDevice_getLevel, "ret")
    descriptor = None
    for klass in SBCS_WaterLevelMeaurementDevice_getLevel.__mro__:
        if "ret" in klass.__dict__:
            descriptor = klass.__dict__["ret"]
            break
    assert isinstance(descriptor, property)



def test_sbcs_pumpcontroller_closepump_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpController_ClosePump)


def test_sbcs_pumpcontroller_closepump_constructor_exists():
    assert callable(SBCS_PumpController_ClosePump.__init__)


def test_sbcs_pumpcontroller_closepump_constructor_args():
    sig = inspect.signature(SBCS_PumpController_ClosePump.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_controlprogram_start_is_not_abstract():
    assert not inspect.isabstract(SBCS_ControlProgram_Start)


def test_sbcs_controlprogram_start_constructor_exists():
    assert callable(SBCS_ControlProgram_Start.__init__)


def test_sbcs_controlprogram_start_constructor_args():
    sig = inspect.signature(SBCS_ControlProgram_Start.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_pumpcontroller_openpump_is_not_abstract():
    assert not inspect.isabstract(SBCS_PumpController_OpenPump)


def test_sbcs_pumpcontroller_openpump_constructor_exists():
    assert callable(SBCS_PumpController_OpenPump.__init__)


def test_sbcs_pumpcontroller_openpump_constructor_args():
    sig = inspect.signature(SBCS_PumpController_OpenPump.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_transition_is_not_abstract():
    assert not inspect.isabstract(SBCS_Transition)


def test_sbcs_transition_constructor_exists():
    assert callable(SBCS_Transition.__init__)


def test_sbcs_transition_constructor_args():
    sig = inspect.signature(SBCS_Transition.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_controlprogram_is_not_abstract():
    assert not inspect.isabstract(SBCS_ControlProgram)


def test_sbcs_controlprogram_constructor_exists():
    assert callable(SBCS_ControlProgram.__init__)


def test_sbcs_controlprogram_constructor_args():
    sig = inspect.signature(SBCS_ControlProgram.__init__)
    params = list(sig.parameters.keys())
    assert "wlmdFailure" in params, "Missing parameter 'wlmdFailure'"
    assert "mode" in params, "Missing parameter 'mode'"

def test_sbcs_controlprogram_has_wlmdFailure():
    assert hasattr(SBCS_ControlProgram, "wlmdFailure")
    descriptor = None
    for klass in SBCS_ControlProgram.__mro__:
        if "wlmdFailure" in klass.__dict__:
            descriptor = klass.__dict__["wlmdFailure"]
            break
    assert isinstance(descriptor, property)

def test_sbcs_controlprogram_has_mode():
    assert hasattr(SBCS_ControlProgram, "mode")
    descriptor = None
    for klass in SBCS_ControlProgram.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sbcs_snapshot_is_not_abstract():
    assert not inspect.isabstract(SBCS_Snapshot)


def test_sbcs_snapshot_constructor_exists():
    assert callable(SBCS_Snapshot.__init__)


def test_sbcs_snapshot_constructor_args():
    sig = inspect.signature(SBCS_Snapshot.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_pump_is_not_abstract():
    assert not inspect.isabstract(SBCS_Pump)


def test_sbcs_pump_constructor_exists():
    assert callable(SBCS_Pump.__init__)


def test_sbcs_pump_constructor_args():
    sig = inspect.signature(SBCS_Pump.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_sbcs_pump_has_mode():
    assert hasattr(SBCS_Pump, "mode")
    descriptor = None
    for klass in SBCS_Pump.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_sbcs_steamboiler_is_not_abstract():
    assert not inspect.isabstract(SBCS_SteamBoiler)


def test_sbcs_steamboiler_constructor_exists():
    assert callable(SBCS_SteamBoiler.__init__)


def test_sbcs_steamboiler_constructor_args():
    sig = inspect.signature(SBCS_SteamBoiler.__init__)
    params = list(sig.parameters.keys())
    assert "valveOpen" in params, "Missing parameter 'valveOpen'"

def test_sbcs_steamboiler_has_valveOpen():
    assert hasattr(SBCS_SteamBoiler, "valveOpen")
    descriptor = None
    for klass in SBCS_SteamBoiler.__mro__:
        if "valveOpen" in klass.__dict__:
            descriptor = klass.__dict__["valveOpen"]
            break
    assert isinstance(descriptor, property)



def test_sbcs_steamboiler_openvalve_is_not_abstract():
    assert not inspect.isabstract(SBCS_SteamBoiler_OpenValve)


def test_sbcs_steamboiler_openvalve_constructor_exists():
    assert callable(SBCS_SteamBoiler_OpenValve.__init__)


def test_sbcs_steamboiler_openvalve_constructor_args():
    sig = inspect.signature(SBCS_SteamBoiler_OpenValve.__init__)
    params = list(sig.parameters.keys())



def test_sbcs_waterlevelmeasurementdevice_is_not_abstract():
    assert not inspect.isabstract(SBCS_WaterLevelMeasurementDevice)


def test_sbcs_waterlevelmeasurementdevice_constructor_exists():
    assert callable(SBCS_WaterLevelMeasurementDevice.__init__)


def test_sbcs_waterlevelmeasurementdevice_constructor_args():
    sig = inspect.signature(SBCS_WaterLevelMeasurementDevice.__init__)
    params = list(sig.parameters.keys())
    assert "waterLevel" in params, "Missing parameter 'waterLevel'"

def test_sbcs_waterlevelmeasurementdevice_has_waterLevel():
    assert hasattr(SBCS_WaterLevelMeasurementDevice, "waterLevel")
    descriptor = None
    for klass in SBCS_WaterLevelMeasurementDevice.__mro__:
        if "waterLevel" in klass.__dict__:
            descriptor = klass.__dict__["waterLevel"]
            break
    assert isinstance(descriptor, property)

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

def test_mode_exists():
    # Check that the Enumeration exists
    assert Mode is not None

def test_mode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Mode]
    expected_literals = [
        "Initialization",
        "Normal",
        "Rescue",
        "Degraded",
        "Dameged",
        "EmergencyStop",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Mode"

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
SBCS_PumpControler_strategy = st.builds(
    SBCS_PumpControler,
)
Transition_strategy = st.builds(
    Transition,
)
SBCS_WaterLevelMeaurementDevice_getLevel_strategy = st.builds(
    SBCS_WaterLevelMeaurementDevice_getLevel,
    ret=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
SBCS_PumpController_ClosePump_strategy = st.builds(
    SBCS_PumpController_ClosePump,
)
SBCS_ControlProgram_Start_strategy = st.builds(
    SBCS_ControlProgram_Start,
)
SBCS_PumpController_OpenPump_strategy = st.builds(
    SBCS_PumpController_OpenPump,
)
SBCS_Transition_strategy = st.builds(
    SBCS_Transition,
)
SBCS_ControlProgram_strategy = st.builds(
    SBCS_ControlProgram,
    wlmdFailure=
        st.booleans(),
    mode=
        safe_text
)
SBCS_Snapshot_strategy = st.builds(
    SBCS_Snapshot,
)
SBCS_Pump_strategy = st.builds(
    SBCS_Pump,
    mode=
        safe_text
)
SBCS_SteamBoiler_strategy = st.builds(
    SBCS_SteamBoiler,
    valveOpen=
        safe_text
)
SBCS_SteamBoiler_OpenValve_strategy = st.builds(
    SBCS_SteamBoiler_OpenValve,
)
SBCS_WaterLevelMeasurementDevice_strategy = st.builds(
    SBCS_WaterLevelMeasurementDevice,
    waterLevel=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=SBCS_PumpControler_strategy)
@settings(max_examples=50)
def test_sbcs_pumpcontroler_instantiation(instance):
    assert isinstance(instance, SBCS_PumpControler)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=SBCS_WaterLevelMeaurementDevice_getLevel_strategy)
@settings(max_examples=50)
def test_sbcs_waterlevelmeaurementdevice_getlevel_instantiation(instance):
    assert isinstance(instance, SBCS_WaterLevelMeaurementDevice_getLevel)



@given(instance=SBCS_WaterLevelMeaurementDevice_getLevel_strategy)
def test_sbcs_waterlevelmeaurementdevice_getlevel_ret_setter(instance):
    original = instance.ret
    instance.ret = original
    assert instance.ret == original

@given(instance=SBCS_PumpController_ClosePump_strategy)
@settings(max_examples=50)
def test_sbcs_pumpcontroller_closepump_instantiation(instance):
    assert isinstance(instance, SBCS_PumpController_ClosePump)

@given(instance=SBCS_ControlProgram_Start_strategy)
@settings(max_examples=50)
def test_sbcs_controlprogram_start_instantiation(instance):
    assert isinstance(instance, SBCS_ControlProgram_Start)

@given(instance=SBCS_PumpController_OpenPump_strategy)
@settings(max_examples=50)
def test_sbcs_pumpcontroller_openpump_instantiation(instance):
    assert isinstance(instance, SBCS_PumpController_OpenPump)

@given(instance=SBCS_Transition_strategy)
@settings(max_examples=50)
def test_sbcs_transition_instantiation(instance):
    assert isinstance(instance, SBCS_Transition)

@given(instance=SBCS_ControlProgram_strategy)
@settings(max_examples=50)
def test_sbcs_controlprogram_instantiation(instance):
    assert isinstance(instance, SBCS_ControlProgram)



@given(instance=SBCS_ControlProgram_strategy)
def test_sbcs_controlprogram_wlmdFailure_setter(instance):
    original = instance.wlmdFailure
    instance.wlmdFailure = original
    assert instance.wlmdFailure == original



@given(instance=SBCS_ControlProgram_strategy)
def test_sbcs_controlprogram_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SBCS_Snapshot_strategy)
@settings(max_examples=50)
def test_sbcs_snapshot_instantiation(instance):
    assert isinstance(instance, SBCS_Snapshot)

@given(instance=SBCS_Pump_strategy)
@settings(max_examples=50)
def test_sbcs_pump_instantiation(instance):
    assert isinstance(instance, SBCS_Pump)



@given(instance=SBCS_Pump_strategy)
def test_sbcs_pump_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=SBCS_SteamBoiler_strategy)
@settings(max_examples=50)
def test_sbcs_steamboiler_instantiation(instance):
    assert isinstance(instance, SBCS_SteamBoiler)



@given(instance=SBCS_SteamBoiler_strategy)
def test_sbcs_steamboiler_valveOpen_setter(instance):
    original = instance.valveOpen
    instance.valveOpen = original
    assert instance.valveOpen == original

@given(instance=SBCS_SteamBoiler_OpenValve_strategy)
@settings(max_examples=50)
def test_sbcs_steamboiler_openvalve_instantiation(instance):
    assert isinstance(instance, SBCS_SteamBoiler_OpenValve)

@given(instance=SBCS_WaterLevelMeasurementDevice_strategy)
@settings(max_examples=50)
def test_sbcs_waterlevelmeasurementdevice_instantiation(instance):
    assert isinstance(instance, SBCS_WaterLevelMeasurementDevice)



@given(instance=SBCS_WaterLevelMeasurementDevice_strategy)
def test_sbcs_waterlevelmeasurementdevice_waterLevel_setter(instance):
    original = instance.waterLevel
    instance.waterLevel = original
    assert instance.waterLevel == original
