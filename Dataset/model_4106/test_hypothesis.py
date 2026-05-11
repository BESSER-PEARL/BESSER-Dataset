import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Concept::Thing,
    Concept::IndividualContainer,
    Thing,
    Concept::Route,
    Concept::Signal,
    Concept::SwitchPosition,
    Concept::Sensor,
    Concept::Trackelement,
    Trackelement,
    Concept::Switch,
    Concept::Segment,
    SignalStateKind,
    SwitchStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_concept::thing_is_not_abstract():
    assert not inspect.isabstract(Concept::Thing)


def test_concept::thing_constructor_exists():
    assert callable(Concept::Thing.__init__)


def test_concept::thing_constructor_args():
    sig = inspect.signature(Concept::Thing.__init__)
    params = list(sig.parameters.keys())



def test_concept::individualcontainer_is_not_abstract():
    assert not inspect.isabstract(Concept::IndividualContainer)


def test_concept::individualcontainer_constructor_exists():
    assert callable(Concept::IndividualContainer.__init__)


def test_concept::individualcontainer_constructor_args():
    sig = inspect.signature(Concept::IndividualContainer.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_concept::route_is_not_abstract():
    assert not inspect.isabstract(Concept::Route)


def test_concept::route_constructor_exists():
    assert callable(Concept::Route.__init__)


def test_concept::route_constructor_args():
    sig = inspect.signature(Concept::Route.__init__)
    params = list(sig.parameters.keys())



def test_concept::signal_is_not_abstract():
    assert not inspect.isabstract(Concept::Signal)


def test_concept::signal_constructor_exists():
    assert callable(Concept::Signal.__init__)


def test_concept::signal_constructor_args():
    sig = inspect.signature(Concept::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "Signal_actualState" in params, "Missing parameter 'Signal_actualState'"

def test_concept::signal_has_Signal_actualState():
    assert hasattr(Concept::Signal, "Signal_actualState")
    descriptor = None
    for klass in Concept::Signal.__mro__:
        if "Signal_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Signal_actualState"]
            break
    assert isinstance(descriptor, property)



def test_concept::switchposition_is_not_abstract():
    assert not inspect.isabstract(Concept::SwitchPosition)


def test_concept::switchposition_constructor_exists():
    assert callable(Concept::SwitchPosition.__init__)


def test_concept::switchposition_constructor_args():
    sig = inspect.signature(Concept::SwitchPosition.__init__)
    params = list(sig.parameters.keys())
    assert "SwitchPosition_switchState" in params, "Missing parameter 'SwitchPosition_switchState'"

def test_concept::switchposition_has_SwitchPosition_switchState():
    assert hasattr(Concept::SwitchPosition, "SwitchPosition_switchState")
    descriptor = None
    for klass in Concept::SwitchPosition.__mro__:
        if "SwitchPosition_switchState" in klass.__dict__:
            descriptor = klass.__dict__["SwitchPosition_switchState"]
            break
    assert isinstance(descriptor, property)



def test_concept::sensor_is_not_abstract():
    assert not inspect.isabstract(Concept::Sensor)


def test_concept::sensor_constructor_exists():
    assert callable(Concept::Sensor.__init__)


def test_concept::sensor_constructor_args():
    sig = inspect.signature(Concept::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_concept::trackelement_is_not_abstract():
    assert not inspect.isabstract(Concept::Trackelement)


def test_concept::trackelement_constructor_exists():
    assert callable(Concept::Trackelement.__init__)


def test_concept::trackelement_constructor_args():
    sig = inspect.signature(Concept::Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(Trackelement)


def test_trackelement_constructor_exists():
    assert callable(Trackelement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_concept::switch_is_not_abstract():
    assert not inspect.isabstract(Concept::Switch)


def test_concept::switch_constructor_exists():
    assert callable(Concept::Switch.__init__)


def test_concept::switch_constructor_args():
    sig = inspect.signature(Concept::Switch.__init__)
    params = list(sig.parameters.keys())
    assert "Switch_actualState" in params, "Missing parameter 'Switch_actualState'"

def test_concept::switch_has_Switch_actualState():
    assert hasattr(Concept::Switch, "Switch_actualState")
    descriptor = None
    for klass in Concept::Switch.__mro__:
        if "Switch_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Switch_actualState"]
            break
    assert isinstance(descriptor, property)



def test_concept::segment_is_not_abstract():
    assert not inspect.isabstract(Concept::Segment)


def test_concept::segment_constructor_exists():
    assert callable(Concept::Segment.__init__)


def test_concept::segment_constructor_args():
    sig = inspect.signature(Concept::Segment.__init__)
    params = list(sig.parameters.keys())
    assert "Segment_length" in params, "Missing parameter 'Segment_length'"

def test_concept::segment_has_Segment_length():
    assert hasattr(Concept::Segment, "Segment_length")
    descriptor = None
    for klass in Concept::Segment.__mro__:
        if "Segment_length" in klass.__dict__:
            descriptor = klass.__dict__["Segment_length"]
            break
    assert isinstance(descriptor, property)

def test_signalstatekind_exists():
    # Check that the Enumeration exists
    assert SignalStateKind is not None

def test_signalstatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignalStateKind]
    expected_literals = [
        "SignalStateKind_STOP",
        "SignalStateKind_GO",
        "SignalStateKind_FAILURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignalStateKind"

def test_switchstatekind_exists():
    # Check that the Enumeration exists
    assert SwitchStateKind is not None

def test_switchstatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwitchStateKind]
    expected_literals = [
        "PointStateKind_RIGHT",
        "PointStateKind_LEFT",
        "PointStateKind_STRAIGHT",
        "PointStateKind_FAILURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwitchStateKind"


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
Concept::Thing_strategy = st.builds(
    Concept::Thing,
)
Concept::IndividualContainer_strategy = st.builds(
    Concept::IndividualContainer,
)
Thing_strategy = st.builds(
    Thing,
)
Concept::Route_strategy = st.builds(
    Concept::Route,
)
Concept::Signal_strategy = st.builds(
    Concept::Signal,
    Signal_actualState=
        safe_text
)
Concept::SwitchPosition_strategy = st.builds(
    Concept::SwitchPosition,
    SwitchPosition_switchState=
        safe_text
)
Concept::Sensor_strategy = st.builds(
    Concept::Sensor,
)
Concept::Trackelement_strategy = st.builds(
    Concept::Trackelement,
)
Trackelement_strategy = st.builds(
    Trackelement,
)
Concept::Switch_strategy = st.builds(
    Concept::Switch,
    Switch_actualState=
        safe_text
)
Concept::Segment_strategy = st.builds(
    Concept::Segment,
    Segment_length=
        st.integers()
)

@given(instance=Concept::Thing_strategy)
@settings(max_examples=50)
def test_concept::thing_instantiation(instance):
    assert isinstance(instance, Concept::Thing)

@given(instance=Concept::IndividualContainer_strategy)
@settings(max_examples=50)
def test_concept::individualcontainer_instantiation(instance):
    assert isinstance(instance, Concept::IndividualContainer)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=Concept::Route_strategy)
@settings(max_examples=50)
def test_concept::route_instantiation(instance):
    assert isinstance(instance, Concept::Route)

@given(instance=Concept::Signal_strategy)
@settings(max_examples=50)
def test_concept::signal_instantiation(instance):
    assert isinstance(instance, Concept::Signal)

@given(instance=Concept::Signal_strategy)
def test_concept::signal_Signal_actualState_type(instance):
    assert isinstance(instance.Signal_actualState, str)


@given(instance=Concept::Signal_strategy)
def test_concept::signal_Signal_actualState_setter(instance):
    original = instance.Signal_actualState
    instance.Signal_actualState = original
    assert instance.Signal_actualState == original

@given(instance=Concept::SwitchPosition_strategy)
@settings(max_examples=50)
def test_concept::switchposition_instantiation(instance):
    assert isinstance(instance, Concept::SwitchPosition)

@given(instance=Concept::SwitchPosition_strategy)
def test_concept::switchposition_SwitchPosition_switchState_type(instance):
    assert isinstance(instance.SwitchPosition_switchState, str)


@given(instance=Concept::SwitchPosition_strategy)
def test_concept::switchposition_SwitchPosition_switchState_setter(instance):
    original = instance.SwitchPosition_switchState
    instance.SwitchPosition_switchState = original
    assert instance.SwitchPosition_switchState == original

@given(instance=Concept::Sensor_strategy)
@settings(max_examples=50)
def test_concept::sensor_instantiation(instance):
    assert isinstance(instance, Concept::Sensor)

@given(instance=Concept::Trackelement_strategy)
@settings(max_examples=50)
def test_concept::trackelement_instantiation(instance):
    assert isinstance(instance, Concept::Trackelement)

@given(instance=Trackelement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, Trackelement)

@given(instance=Concept::Switch_strategy)
@settings(max_examples=50)
def test_concept::switch_instantiation(instance):
    assert isinstance(instance, Concept::Switch)

@given(instance=Concept::Switch_strategy)
def test_concept::switch_Switch_actualState_type(instance):
    assert isinstance(instance.Switch_actualState, str)


@given(instance=Concept::Switch_strategy)
def test_concept::switch_Switch_actualState_setter(instance):
    original = instance.Switch_actualState
    instance.Switch_actualState = original
    assert instance.Switch_actualState == original

@given(instance=Concept::Segment_strategy)
@settings(max_examples=50)
def test_concept::segment_instantiation(instance):
    assert isinstance(instance, Concept::Segment)

@given(instance=Concept::Segment_strategy)
def test_concept::segment_Segment_length_type(instance):
    assert isinstance(instance.Segment_length, int)


@given(instance=Concept::Segment_strategy)
def test_concept::segment_Segment_length_setter(instance):
    original = instance.Segment_length
    instance.Segment_length = original
    assert instance.Segment_length == original
