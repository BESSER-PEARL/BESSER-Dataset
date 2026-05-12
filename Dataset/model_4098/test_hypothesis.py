import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Train5_RailwayDiagram,
    TrackElement,
    Train5_Station,
    Train5_Segment,
    Train5_Switch,
    NamedElement,
    Train5_Route,
    Train5_SensorNetwork,
    Train5_RoutePart,
    Train5_TrackElement,
    Train5_NamedElement,
    Signal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_train5_railwaydiagram_is_not_abstract():
    assert not inspect.isabstract(Train5_RailwayDiagram)


def test_train5_railwaydiagram_constructor_exists():
    assert callable(Train5_RailwayDiagram.__init__)


def test_train5_railwaydiagram_constructor_args():
    sig = inspect.signature(Train5_RailwayDiagram.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_train5_station_is_not_abstract():
    assert not inspect.isabstract(Train5_Station)


def test_train5_station_constructor_exists():
    assert callable(Train5_Station.__init__)


def test_train5_station_constructor_args():
    sig = inspect.signature(Train5_Station.__init__)
    params = list(sig.parameters.keys())



def test_train5_segment_is_not_abstract():
    assert not inspect.isabstract(Train5_Segment)


def test_train5_segment_constructor_exists():
    assert callable(Train5_Segment.__init__)


def test_train5_segment_constructor_args():
    sig = inspect.signature(Train5_Segment.__init__)
    params = list(sig.parameters.keys())



def test_train5_switch_is_not_abstract():
    assert not inspect.isabstract(Train5_Switch)


def test_train5_switch_constructor_exists():
    assert callable(Train5_Switch.__init__)


def test_train5_switch_constructor_args():
    sig = inspect.signature(Train5_Switch.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_train5_route_is_not_abstract():
    assert not inspect.isabstract(Train5_Route)


def test_train5_route_constructor_exists():
    assert callable(Train5_Route.__init__)


def test_train5_route_constructor_args():
    sig = inspect.signature(Train5_Route.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "currentIndex" in params, "Missing parameter 'currentIndex'"
    assert "leftOver" in params, "Missing parameter 'leftOver'"

def test_train5_route_has_speed():
    assert hasattr(Train5_Route, "speed")
    descriptor = None
    for klass in Train5_Route.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_train5_route_has_currentIndex():
    assert hasattr(Train5_Route, "currentIndex")
    descriptor = None
    for klass in Train5_Route.__mro__:
        if "currentIndex" in klass.__dict__:
            descriptor = klass.__dict__["currentIndex"]
            break
    assert isinstance(descriptor, property)

def test_train5_route_has_leftOver():
    assert hasattr(Train5_Route, "leftOver")
    descriptor = None
    for klass in Train5_Route.__mro__:
        if "leftOver" in klass.__dict__:
            descriptor = klass.__dict__["leftOver"]
            break
    assert isinstance(descriptor, property)



def test_train5_sensornetwork_is_not_abstract():
    assert not inspect.isabstract(Train5_SensorNetwork)


def test_train5_sensornetwork_constructor_exists():
    assert callable(Train5_SensorNetwork.__init__)


def test_train5_sensornetwork_constructor_args():
    sig = inspect.signature(Train5_SensorNetwork.__init__)
    params = list(sig.parameters.keys())



def test_train5_routepart_is_not_abstract():
    assert not inspect.isabstract(Train5_RoutePart)


def test_train5_routepart_constructor_exists():
    assert callable(Train5_RoutePart.__init__)


def test_train5_routepart_constructor_args():
    sig = inspect.signature(Train5_RoutePart.__init__)
    params = list(sig.parameters.keys())



def test_train5_trackelement_is_not_abstract():
    assert not inspect.isabstract(Train5_TrackElement)


def test_train5_trackelement_constructor_exists():
    assert callable(Train5_TrackElement.__init__)


def test_train5_trackelement_constructor_args():
    sig = inspect.signature(Train5_TrackElement.__init__)
    params = list(sig.parameters.keys())
    assert "State" in params, "Missing parameter 'State'"
    assert "length" in params, "Missing parameter 'length'"

def test_train5_trackelement_has_State():
    assert hasattr(Train5_TrackElement, "State")
    descriptor = None
    for klass in Train5_TrackElement.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_train5_trackelement_has_length():
    assert hasattr(Train5_TrackElement, "length")
    descriptor = None
    for klass in Train5_TrackElement.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_train5_namedelement_is_not_abstract():
    assert not inspect.isabstract(Train5_NamedElement)


def test_train5_namedelement_constructor_exists():
    assert callable(Train5_NamedElement.__init__)


def test_train5_namedelement_constructor_args():
    sig = inspect.signature(Train5_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_train5_namedelement_has_id():
    assert hasattr(Train5_NamedElement, "id")
    descriptor = None
    for klass in Train5_NamedElement.__mro__:
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
        "Failure",
        "Go",
        "STOP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Signal"


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
Train5_RailwayDiagram_strategy = st.builds(
    Train5_RailwayDiagram,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
Train5_Station_strategy = st.builds(
    Train5_Station,
)
Train5_Segment_strategy = st.builds(
    Train5_Segment,
)
Train5_Switch_strategy = st.builds(
    Train5_Switch,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Train5_Route_strategy = st.builds(
    Train5_Route,
    speed=
        safe_text,
    currentIndex=
        safe_text,
    leftOver=
        safe_text
)
Train5_SensorNetwork_strategy = st.builds(
    Train5_SensorNetwork,
)
Train5_RoutePart_strategy = st.builds(
    Train5_RoutePart,
)
Train5_TrackElement_strategy = st.builds(
    Train5_TrackElement,
    State=
        safe_text,
    length=
        safe_text
)
Train5_NamedElement_strategy = st.builds(
    Train5_NamedElement,
    id=
        safe_text
)

@given(instance=Train5_RailwayDiagram_strategy)
@settings(max_examples=50)
def test_train5_railwaydiagram_instantiation(instance):
    assert isinstance(instance, Train5_RailwayDiagram)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=Train5_Station_strategy)
@settings(max_examples=50)
def test_train5_station_instantiation(instance):
    assert isinstance(instance, Train5_Station)

@given(instance=Train5_Segment_strategy)
@settings(max_examples=50)
def test_train5_segment_instantiation(instance):
    assert isinstance(instance, Train5_Segment)

@given(instance=Train5_Switch_strategy)
@settings(max_examples=50)
def test_train5_switch_instantiation(instance):
    assert isinstance(instance, Train5_Switch)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Train5_Route_strategy)
@settings(max_examples=50)
def test_train5_route_instantiation(instance):
    assert isinstance(instance, Train5_Route)



@given(instance=Train5_Route_strategy)
def test_train5_route_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=Train5_Route_strategy)
def test_train5_route_currentIndex_setter(instance):
    original = instance.currentIndex
    instance.currentIndex = original
    assert instance.currentIndex == original



@given(instance=Train5_Route_strategy)
def test_train5_route_leftOver_setter(instance):
    original = instance.leftOver
    instance.leftOver = original
    assert instance.leftOver == original

@given(instance=Train5_SensorNetwork_strategy)
@settings(max_examples=50)
def test_train5_sensornetwork_instantiation(instance):
    assert isinstance(instance, Train5_SensorNetwork)

@given(instance=Train5_RoutePart_strategy)
@settings(max_examples=50)
def test_train5_routepart_instantiation(instance):
    assert isinstance(instance, Train5_RoutePart)

@given(instance=Train5_TrackElement_strategy)
@settings(max_examples=50)
def test_train5_trackelement_instantiation(instance):
    assert isinstance(instance, Train5_TrackElement)



@given(instance=Train5_TrackElement_strategy)
def test_train5_trackelement_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original



@given(instance=Train5_TrackElement_strategy)
def test_train5_trackelement_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=Train5_NamedElement_strategy)
@settings(max_examples=50)
def test_train5_namedelement_instantiation(instance):
    assert isinstance(instance, Train5_NamedElement)



@given(instance=Train5_NamedElement_strategy)
def test_train5_namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
