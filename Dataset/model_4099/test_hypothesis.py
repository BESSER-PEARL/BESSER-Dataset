import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    railway::RailwayElement,
    railway::RailwayContainer,
    RailwayElement,
    railway::Route,
    railway::SwitchPosition,
    railway::Semaphore,
    railway::Sensor,
    railway::TrackElement,
    TrackElement,
    railway::Switch,
    railway::Segment,
    Signal,
    Position,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_railway::railwayelement_is_not_abstract():
    assert not inspect.isabstract(railway::RailwayElement)


def test_railway::railwayelement_constructor_exists():
    assert callable(railway::RailwayElement.__init__)


def test_railway::railwayelement_constructor_args():
    sig = inspect.signature(railway::RailwayElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_railway::railwayelement_has_id():
    assert hasattr(railway::RailwayElement, "id")
    descriptor = None
    for klass in railway::RailwayElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_railway::railwaycontainer_is_not_abstract():
    assert not inspect.isabstract(railway::RailwayContainer)


def test_railway::railwaycontainer_constructor_exists():
    assert callable(railway::RailwayContainer.__init__)


def test_railway::railwaycontainer_constructor_args():
    sig = inspect.signature(railway::RailwayContainer.__init__)
    params = list(sig.parameters.keys())



def test_railwayelement_is_not_abstract():
    assert not inspect.isabstract(RailwayElement)


def test_railwayelement_constructor_exists():
    assert callable(RailwayElement.__init__)


def test_railwayelement_constructor_args():
    sig = inspect.signature(RailwayElement.__init__)
    params = list(sig.parameters.keys())



def test_railway::route_is_not_abstract():
    assert not inspect.isabstract(railway::Route)


def test_railway::route_constructor_exists():
    assert callable(railway::Route.__init__)


def test_railway::route_constructor_args():
    sig = inspect.signature(railway::Route.__init__)
    params = list(sig.parameters.keys())



def test_railway::switchposition_is_not_abstract():
    assert not inspect.isabstract(railway::SwitchPosition)


def test_railway::switchposition_constructor_exists():
    assert callable(railway::SwitchPosition.__init__)


def test_railway::switchposition_constructor_args():
    sig = inspect.signature(railway::SwitchPosition.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_railway::switchposition_has_position():
    assert hasattr(railway::SwitchPosition, "position")
    descriptor = None
    for klass in railway::SwitchPosition.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_railway::semaphore_is_not_abstract():
    assert not inspect.isabstract(railway::Semaphore)


def test_railway::semaphore_constructor_exists():
    assert callable(railway::Semaphore.__init__)


def test_railway::semaphore_constructor_args():
    sig = inspect.signature(railway::Semaphore.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_railway::semaphore_has_signal():
    assert hasattr(railway::Semaphore, "signal")
    descriptor = None
    for klass in railway::Semaphore.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_railway::sensor_is_not_abstract():
    assert not inspect.isabstract(railway::Sensor)


def test_railway::sensor_constructor_exists():
    assert callable(railway::Sensor.__init__)


def test_railway::sensor_constructor_args():
    sig = inspect.signature(railway::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_railway::trackelement_is_not_abstract():
    assert not inspect.isabstract(railway::TrackElement)


def test_railway::trackelement_constructor_exists():
    assert callable(railway::TrackElement.__init__)


def test_railway::trackelement_constructor_args():
    sig = inspect.signature(railway::TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_railway::switch_is_not_abstract():
    assert not inspect.isabstract(railway::Switch)


def test_railway::switch_constructor_exists():
    assert callable(railway::Switch.__init__)


def test_railway::switch_constructor_args():
    sig = inspect.signature(railway::Switch.__init__)
    params = list(sig.parameters.keys())
    assert "currentPosition" in params, "Missing parameter 'currentPosition'"

def test_railway::switch_has_currentPosition():
    assert hasattr(railway::Switch, "currentPosition")
    descriptor = None
    for klass in railway::Switch.__mro__:
        if "currentPosition" in klass.__dict__:
            descriptor = klass.__dict__["currentPosition"]
            break
    assert isinstance(descriptor, property)



def test_railway::segment_is_not_abstract():
    assert not inspect.isabstract(railway::Segment)


def test_railway::segment_constructor_exists():
    assert callable(railway::Segment.__init__)


def test_railway::segment_constructor_args():
    sig = inspect.signature(railway::Segment.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"

def test_railway::segment_has_length():
    assert hasattr(railway::Segment, "length")
    descriptor = None
    for klass in railway::Segment.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
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
        "GO",
        "FAILURE",
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
        "STRAIGHT",
        "FAILURE",
        "RIGHT",
        "LEFT",
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
railway::RailwayElement_strategy = st.builds(
    railway::RailwayElement,
    id=
        st.integers()
)
railway::RailwayContainer_strategy = st.builds(
    railway::RailwayContainer,
)
RailwayElement_strategy = st.builds(
    RailwayElement,
)
railway::Route_strategy = st.builds(
    railway::Route,
)
railway::SwitchPosition_strategy = st.builds(
    railway::SwitchPosition,
    position=
        safe_text
)
railway::Semaphore_strategy = st.builds(
    railway::Semaphore,
    signal=
        safe_text
)
railway::Sensor_strategy = st.builds(
    railway::Sensor,
)
railway::TrackElement_strategy = st.builds(
    railway::TrackElement,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
railway::Switch_strategy = st.builds(
    railway::Switch,
    currentPosition=
        safe_text
)
railway::Segment_strategy = st.builds(
    railway::Segment,
    length=
        st.integers()
)

@given(instance=railway::RailwayElement_strategy)
@settings(max_examples=50)
def test_railway::railwayelement_instantiation(instance):
    assert isinstance(instance, railway::RailwayElement)

@given(instance=railway::RailwayElement_strategy)
def test_railway::railwayelement_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=railway::RailwayElement_strategy)
def test_railway::railwayelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=railway::RailwayContainer_strategy)
@settings(max_examples=50)
def test_railway::railwaycontainer_instantiation(instance):
    assert isinstance(instance, railway::RailwayContainer)

@given(instance=RailwayElement_strategy)
@settings(max_examples=50)
def test_railwayelement_instantiation(instance):
    assert isinstance(instance, RailwayElement)

@given(instance=railway::Route_strategy)
@settings(max_examples=50)
def test_railway::route_instantiation(instance):
    assert isinstance(instance, railway::Route)

@given(instance=railway::SwitchPosition_strategy)
@settings(max_examples=50)
def test_railway::switchposition_instantiation(instance):
    assert isinstance(instance, railway::SwitchPosition)

@given(instance=railway::SwitchPosition_strategy)
def test_railway::switchposition_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=railway::SwitchPosition_strategy)
def test_railway::switchposition_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=railway::Semaphore_strategy)
@settings(max_examples=50)
def test_railway::semaphore_instantiation(instance):
    assert isinstance(instance, railway::Semaphore)

@given(instance=railway::Semaphore_strategy)
def test_railway::semaphore_signal_type(instance):
    assert isinstance(instance.signal, str)


@given(instance=railway::Semaphore_strategy)
def test_railway::semaphore_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=railway::Sensor_strategy)
@settings(max_examples=50)
def test_railway::sensor_instantiation(instance):
    assert isinstance(instance, railway::Sensor)

@given(instance=railway::TrackElement_strategy)
@settings(max_examples=50)
def test_railway::trackelement_instantiation(instance):
    assert isinstance(instance, railway::TrackElement)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=railway::Switch_strategy)
@settings(max_examples=50)
def test_railway::switch_instantiation(instance):
    assert isinstance(instance, railway::Switch)

@given(instance=railway::Switch_strategy)
def test_railway::switch_currentPosition_type(instance):
    assert isinstance(instance.currentPosition, str)


@given(instance=railway::Switch_strategy)
def test_railway::switch_currentPosition_setter(instance):
    original = instance.currentPosition
    instance.currentPosition = original
    assert instance.currentPosition == original

@given(instance=railway::Segment_strategy)
@settings(max_examples=50)
def test_railway::segment_instantiation(instance):
    assert isinstance(instance, railway::Segment)

@given(instance=railway::Segment_strategy)
def test_railway::segment_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=railway::Segment_strategy)
def test_railway::segment_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original
