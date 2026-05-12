import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RailwayElement,
    railway_TrackElement,
    railway_Sensor,
    railway_Region,
    railway_Route,
    railway_RailwayContainer,
    TrackElement,
    railway_Switch,
    railway_Segment,
    railway_Semaphore,
    railway_SwitchPosition,
    railway_RailwayElement,
    Signal,
    Position,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_railwayelement_is_not_abstract():
    assert not inspect.isabstract(RailwayElement)


def test_railwayelement_constructor_exists():
    assert callable(RailwayElement.__init__)


def test_railwayelement_constructor_args():
    sig = inspect.signature(RailwayElement.__init__)
    params = list(sig.parameters.keys())



def test_railway_trackelement_is_not_abstract():
    assert not inspect.isabstract(railway_TrackElement)


def test_railway_trackelement_constructor_exists():
    assert callable(railway_TrackElement.__init__)


def test_railway_trackelement_constructor_args():
    sig = inspect.signature(railway_TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_railway_sensor_is_not_abstract():
    assert not inspect.isabstract(railway_Sensor)


def test_railway_sensor_constructor_exists():
    assert callable(railway_Sensor.__init__)


def test_railway_sensor_constructor_args():
    sig = inspect.signature(railway_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_railway_region_is_not_abstract():
    assert not inspect.isabstract(railway_Region)


def test_railway_region_constructor_exists():
    assert callable(railway_Region.__init__)


def test_railway_region_constructor_args():
    sig = inspect.signature(railway_Region.__init__)
    params = list(sig.parameters.keys())



def test_railway_route_is_not_abstract():
    assert not inspect.isabstract(railway_Route)


def test_railway_route_constructor_exists():
    assert callable(railway_Route.__init__)


def test_railway_route_constructor_args():
    sig = inspect.signature(railway_Route.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_railway_route_has_active():
    assert hasattr(railway_Route, "active")
    descriptor = None
    for klass in railway_Route.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_railway_railwaycontainer_is_not_abstract():
    assert not inspect.isabstract(railway_RailwayContainer)


def test_railway_railwaycontainer_constructor_exists():
    assert callable(railway_RailwayContainer.__init__)


def test_railway_railwaycontainer_constructor_args():
    sig = inspect.signature(railway_RailwayContainer.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_railway_switch_is_not_abstract():
    assert not inspect.isabstract(railway_Switch)


def test_railway_switch_constructor_exists():
    assert callable(railway_Switch.__init__)


def test_railway_switch_constructor_args():
    sig = inspect.signature(railway_Switch.__init__)
    params = list(sig.parameters.keys())
    assert "currentPosition" in params, "Missing parameter 'currentPosition'"

def test_railway_switch_has_currentPosition():
    assert hasattr(railway_Switch, "currentPosition")
    descriptor = None
    for klass in railway_Switch.__mro__:
        if "currentPosition" in klass.__dict__:
            descriptor = klass.__dict__["currentPosition"]
            break
    assert isinstance(descriptor, property)



def test_railway_segment_is_not_abstract():
    assert not inspect.isabstract(railway_Segment)


def test_railway_segment_constructor_exists():
    assert callable(railway_Segment.__init__)


def test_railway_segment_constructor_args():
    sig = inspect.signature(railway_Segment.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_railway_segment_has_length():
    assert hasattr(railway_Segment, "length")
    descriptor = None
    for klass in railway_Segment.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_railway_semaphore_is_not_abstract():
    assert not inspect.isabstract(railway_Semaphore)


def test_railway_semaphore_constructor_exists():
    assert callable(railway_Semaphore.__init__)


def test_railway_semaphore_constructor_args():
    sig = inspect.signature(railway_Semaphore.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_railway_semaphore_has_signal():
    assert hasattr(railway_Semaphore, "signal")
    descriptor = None
    for klass in railway_Semaphore.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_railway_switchposition_is_not_abstract():
    assert not inspect.isabstract(railway_SwitchPosition)


def test_railway_switchposition_constructor_exists():
    assert callable(railway_SwitchPosition.__init__)


def test_railway_switchposition_constructor_args():
    sig = inspect.signature(railway_SwitchPosition.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_railway_switchposition_has_position():
    assert hasattr(railway_SwitchPosition, "position")
    descriptor = None
    for klass in railway_SwitchPosition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_railway_railwayelement_is_not_abstract():
    assert not inspect.isabstract(railway_RailwayElement)


def test_railway_railwayelement_constructor_exists():
    assert callable(railway_RailwayElement.__init__)


def test_railway_railwayelement_constructor_args():
    sig = inspect.signature(railway_RailwayElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_railway_railwayelement_has_id():
    assert hasattr(railway_RailwayElement, "id")
    descriptor = None
    for klass in railway_RailwayElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_signal_exists():
    # Check that the Enumeration exists
    assert Signal is not None

def test_signal_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Signal]
    expected_literals = [
        "STOP",
        "FAILURE",
        "GO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Signal"

def test_position_exists():
    # Check that the Enumeration exists
    assert Position is not None

def test_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Position]
    expected_literals = [
        "DIVERGING",
        "STRAIGHT",
        "FAILURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Position"


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
RailwayElement_strategy = st.builds(
    RailwayElement,
)
railway_TrackElement_strategy = st.builds(
    railway_TrackElement,
)
railway_Sensor_strategy = st.builds(
    railway_Sensor,
)
railway_Region_strategy = st.builds(
    railway_Region,
)
railway_Route_strategy = st.builds(
    railway_Route,
    active=
        st.booleans()
)
railway_RailwayContainer_strategy = st.builds(
    railway_RailwayContainer,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
railway_Switch_strategy = st.builds(
    railway_Switch,
    currentPosition=
        safe_text
)
railway_Segment_strategy = st.builds(
    railway_Segment,
    length=
        st.integers()
)
railway_Semaphore_strategy = st.builds(
    railway_Semaphore,
    signal=
        safe_text
)
railway_SwitchPosition_strategy = st.builds(
    railway_SwitchPosition,
    position=
        safe_text
)
railway_RailwayElement_strategy = st.builds(
    railway_RailwayElement,
    id=
        st.integers()
)

@given(instance=RailwayElement_strategy)
@settings(max_examples=50)
def test_railwayelement_instantiation(instance):
    assert isinstance(instance, RailwayElement)

@given(instance=railway_TrackElement_strategy)
@settings(max_examples=50)
def test_railway_trackelement_instantiation(instance):
    assert isinstance(instance, railway_TrackElement)

@given(instance=railway_Sensor_strategy)
@settings(max_examples=50)
def test_railway_sensor_instantiation(instance):
    assert isinstance(instance, railway_Sensor)

@given(instance=railway_Region_strategy)
@settings(max_examples=50)
def test_railway_region_instantiation(instance):
    assert isinstance(instance, railway_Region)

@given(instance=railway_Route_strategy)
@settings(max_examples=50)
def test_railway_route_instantiation(instance):
    assert isinstance(instance, railway_Route)



@given(instance=railway_Route_strategy)
def test_railway_route_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=railway_RailwayContainer_strategy)
@settings(max_examples=50)
def test_railway_railwaycontainer_instantiation(instance):
    assert isinstance(instance, railway_RailwayContainer)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=railway_Switch_strategy)
@settings(max_examples=50)
def test_railway_switch_instantiation(instance):
    assert isinstance(instance, railway_Switch)



@given(instance=railway_Switch_strategy)
def test_railway_switch_currentPosition_setter(instance):
    original = instance.currentPosition
    instance.currentPosition = original
    assert instance.currentPosition == original

@given(instance=railway_Segment_strategy)
@settings(max_examples=50)
def test_railway_segment_instantiation(instance):
    assert isinstance(instance, railway_Segment)



@given(instance=railway_Segment_strategy)
def test_railway_segment_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=railway_Semaphore_strategy)
@settings(max_examples=50)
def test_railway_semaphore_instantiation(instance):
    assert isinstance(instance, railway_Semaphore)



@given(instance=railway_Semaphore_strategy)
def test_railway_semaphore_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=railway_SwitchPosition_strategy)
@settings(max_examples=50)
def test_railway_switchposition_instantiation(instance):
    assert isinstance(instance, railway_SwitchPosition)



@given(instance=railway_SwitchPosition_strategy)
def test_railway_switchposition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=railway_RailwayElement_strategy)
@settings(max_examples=50)
def test_railway_railwayelement_instantiation(instance):
    assert isinstance(instance, railway_RailwayElement)



@given(instance=railway_RailwayElement_strategy)
def test_railway_railwayelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
