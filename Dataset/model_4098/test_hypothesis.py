import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Train5::RailwayDiagram,
    TrackElement,
    Train5::Segment,
    Train5::Station,
    Train5::Switch,
    NamedElement,
    Train5::Route,
    Train5::SensorNetwork,
    Train5::RoutePart,
    Train5::TrackElement,
    Train5::NamedElement,
    Signal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_train5::railwaydiagram_is_not_abstract():
    assert not inspect.isabstract(Train5::RailwayDiagram)


def test_train5::railwaydiagram_constructor_exists():
    assert callable(Train5::RailwayDiagram.__init__)


def test_train5::railwaydiagram_constructor_args():
    sig = inspect.signature(Train5::RailwayDiagram.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_train5::segment_is_not_abstract():
    assert not inspect.isabstract(Train5::Segment)


def test_train5::segment_constructor_exists():
    assert callable(Train5::Segment.__init__)


def test_train5::segment_constructor_args():
    sig = inspect.signature(Train5::Segment.__init__)
    params = list(sig.parameters.keys())



def test_train5::station_is_not_abstract():
    assert not inspect.isabstract(Train5::Station)


def test_train5::station_constructor_exists():
    assert callable(Train5::Station.__init__)


def test_train5::station_constructor_args():
    sig = inspect.signature(Train5::Station.__init__)
    params = list(sig.parameters.keys())



def test_train5::switch_is_not_abstract():
    assert not inspect.isabstract(Train5::Switch)


def test_train5::switch_constructor_exists():
    assert callable(Train5::Switch.__init__)


def test_train5::switch_constructor_args():
    sig = inspect.signature(Train5::Switch.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_train5::route_is_not_abstract():
    assert not inspect.isabstract(Train5::Route)


def test_train5::route_constructor_exists():
    assert callable(Train5::Route.__init__)


def test_train5::route_constructor_args():
    sig = inspect.signature(Train5::Route.__init__)
    params = list(sig.parameters.keys())
    assert "currentIndex" in params, "Missing parameter 'currentIndex'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "leftOver" in params, "Missing parameter 'leftOver'"

def test_train5::route_has_currentIndex():
    assert hasattr(Train5::Route, "currentIndex")
    descriptor = None
    for klass in Train5::Route.__mro__:
        if "currentIndex" in klass.__dict__:
            descriptor = klass.__dict__["currentIndex"]
            break
    assert isinstance(descriptor, property)

def test_train5::route_has_speed():
    assert hasattr(Train5::Route, "speed")
    descriptor = None
    for klass in Train5::Route.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_train5::route_has_leftOver():
    assert hasattr(Train5::Route, "leftOver")
    descriptor = None
    for klass in Train5::Route.__mro__:
        if "leftOver" in klass.__dict__:
            descriptor = klass.__dict__["leftOver"]
            break
    assert isinstance(descriptor, property)



def test_train5::sensornetwork_is_not_abstract():
    assert not inspect.isabstract(Train5::SensorNetwork)


def test_train5::sensornetwork_constructor_exists():
    assert callable(Train5::SensorNetwork.__init__)


def test_train5::sensornetwork_constructor_args():
    sig = inspect.signature(Train5::SensorNetwork.__init__)
    params = list(sig.parameters.keys())



def test_train5::routepart_is_not_abstract():
    assert not inspect.isabstract(Train5::RoutePart)


def test_train5::routepart_constructor_exists():
    assert callable(Train5::RoutePart.__init__)


def test_train5::routepart_constructor_args():
    sig = inspect.signature(Train5::RoutePart.__init__)
    params = list(sig.parameters.keys())



def test_train5::trackelement_is_not_abstract():
    assert not inspect.isabstract(Train5::TrackElement)


def test_train5::trackelement_constructor_exists():
    assert callable(Train5::TrackElement.__init__)


def test_train5::trackelement_constructor_args():
    sig = inspect.signature(Train5::TrackElement.__init__)
    params = list(sig.parameters.keys())
    assert "State" in params, "Missing parameter 'State'"
    assert "length" in params, "Missing parameter 'length'"

def test_train5::trackelement_has_State():
    assert hasattr(Train5::TrackElement, "State")
    descriptor = None
    for klass in Train5::TrackElement.__mro__:
        if "State" in klass.__dict__:
            descriptor = klass.__dict__["State"]
            break
    assert isinstance(descriptor, property)

def test_train5::trackelement_has_length():
    assert hasattr(Train5::TrackElement, "length")
    descriptor = None
    for klass in Train5::TrackElement.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_train5::namedelement_is_not_abstract():
    assert not inspect.isabstract(Train5::NamedElement)


def test_train5::namedelement_constructor_exists():
    assert callable(Train5::NamedElement.__init__)


def test_train5::namedelement_constructor_args():
    sig = inspect.signature(Train5::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_train5::namedelement_has_id():
    assert hasattr(Train5::NamedElement, "id")
    descriptor = None
    for klass in Train5::NamedElement.__mro__:
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
        "Go",
        "STOP",
        "Failure",
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
Train5::RailwayDiagram_strategy = st.builds(
    Train5::RailwayDiagram,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
Train5::Segment_strategy = st.builds(
    Train5::Segment,
)
Train5::Station_strategy = st.builds(
    Train5::Station,
)
Train5::Switch_strategy = st.builds(
    Train5::Switch,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Train5::Route_strategy = st.builds(
    Train5::Route,
    currentIndex=
        safe_text,
    speed=
        safe_text,
    leftOver=
        safe_text
)
Train5::SensorNetwork_strategy = st.builds(
    Train5::SensorNetwork,
)
Train5::RoutePart_strategy = st.builds(
    Train5::RoutePart,
)
Train5::TrackElement_strategy = st.builds(
    Train5::TrackElement,
    State=
        safe_text,
    length=
        safe_text
)
Train5::NamedElement_strategy = st.builds(
    Train5::NamedElement,
    id=
        safe_text
)

@given(instance=Train5::RailwayDiagram_strategy)
@settings(max_examples=50)
def test_train5::railwaydiagram_instantiation(instance):
    assert isinstance(instance, Train5::RailwayDiagram)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=Train5::Segment_strategy)
@settings(max_examples=50)
def test_train5::segment_instantiation(instance):
    assert isinstance(instance, Train5::Segment)

@given(instance=Train5::Station_strategy)
@settings(max_examples=50)
def test_train5::station_instantiation(instance):
    assert isinstance(instance, Train5::Station)

@given(instance=Train5::Switch_strategy)
@settings(max_examples=50)
def test_train5::switch_instantiation(instance):
    assert isinstance(instance, Train5::Switch)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Train5::Route_strategy)
@settings(max_examples=50)
def test_train5::route_instantiation(instance):
    assert isinstance(instance, Train5::Route)

@given(instance=Train5::Route_strategy)
def test_train5::route_currentIndex_type(instance):
    assert isinstance(instance.currentIndex, str)


@given(instance=Train5::Route_strategy)
def test_train5::route_currentIndex_setter(instance):
    original = instance.currentIndex
    instance.currentIndex = original
    assert instance.currentIndex == original

@given(instance=Train5::Route_strategy)
def test_train5::route_speed_type(instance):
    assert isinstance(instance.speed, str)


@given(instance=Train5::Route_strategy)
def test_train5::route_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=Train5::Route_strategy)
def test_train5::route_leftOver_type(instance):
    assert isinstance(instance.leftOver, str)


@given(instance=Train5::Route_strategy)
def test_train5::route_leftOver_setter(instance):
    original = instance.leftOver
    instance.leftOver = original
    assert instance.leftOver == original

@given(instance=Train5::SensorNetwork_strategy)
@settings(max_examples=50)
def test_train5::sensornetwork_instantiation(instance):
    assert isinstance(instance, Train5::SensorNetwork)

@given(instance=Train5::RoutePart_strategy)
@settings(max_examples=50)
def test_train5::routepart_instantiation(instance):
    assert isinstance(instance, Train5::RoutePart)

@given(instance=Train5::TrackElement_strategy)
@settings(max_examples=50)
def test_train5::trackelement_instantiation(instance):
    assert isinstance(instance, Train5::TrackElement)

@given(instance=Train5::TrackElement_strategy)
def test_train5::trackelement_State_type(instance):
    assert isinstance(instance.State, str)


@given(instance=Train5::TrackElement_strategy)
def test_train5::trackelement_State_setter(instance):
    original = instance.State
    instance.State = original
    assert instance.State == original

@given(instance=Train5::TrackElement_strategy)
def test_train5::trackelement_length_type(instance):
    assert isinstance(instance.length, str)


@given(instance=Train5::TrackElement_strategy)
def test_train5::trackelement_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=Train5::NamedElement_strategy)
@settings(max_examples=50)
def test_train5::namedelement_instantiation(instance):
    assert isinstance(instance, Train5::NamedElement)

@given(instance=Train5::NamedElement_strategy)
def test_train5::namedelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Train5::NamedElement_strategy)
def test_train5::namedelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
