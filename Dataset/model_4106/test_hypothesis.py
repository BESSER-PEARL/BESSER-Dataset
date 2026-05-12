import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Concept_Thing,
    Concept_IndividualContainer,
    Thing,
    Concept_Sensor,
    Concept_Route,
    Concept_Signal,
    Concept_SwitchPosition,
    Concept_Trackelement,
    Trackelement,
    Concept_Switch,
    Concept_Segment,
    SignalStateKind,
    SwitchStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_concept_thing_is_not_abstract():
    assert not inspect.isabstract(Concept_Thing)


def test_concept_thing_constructor_exists():
    assert callable(Concept_Thing.__init__)


def test_concept_thing_constructor_args():
    sig = inspect.signature(Concept_Thing.__init__)
    params = list(sig.parameters.keys())



def test_concept_individualcontainer_is_not_abstract():
    assert not inspect.isabstract(Concept_IndividualContainer)


def test_concept_individualcontainer_constructor_exists():
    assert callable(Concept_IndividualContainer.__init__)


def test_concept_individualcontainer_constructor_args():
    sig = inspect.signature(Concept_IndividualContainer.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_concept_sensor_is_not_abstract():
    assert not inspect.isabstract(Concept_Sensor)


def test_concept_sensor_constructor_exists():
    assert callable(Concept_Sensor.__init__)


def test_concept_sensor_constructor_args():
    sig = inspect.signature(Concept_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_concept_route_is_not_abstract():
    assert not inspect.isabstract(Concept_Route)


def test_concept_route_constructor_exists():
    assert callable(Concept_Route.__init__)


def test_concept_route_constructor_args():
    sig = inspect.signature(Concept_Route.__init__)
    params = list(sig.parameters.keys())



def test_concept_signal_is_not_abstract():
    assert not inspect.isabstract(Concept_Signal)


def test_concept_signal_constructor_exists():
    assert callable(Concept_Signal.__init__)


def test_concept_signal_constructor_args():
    sig = inspect.signature(Concept_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "Signal_actualState" in params, "Missing parameter 'Signal_actualState'"

def test_concept_signal_has_Signal_actualState():
    assert hasattr(Concept_Signal, "Signal_actualState")
    descriptor = None
    for klass in Concept_Signal.__mro__:
        if "Signal_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Signal_actualState"]
            break
    assert isinstance(descriptor, property)



def test_concept_switchposition_is_not_abstract():
    assert not inspect.isabstract(Concept_SwitchPosition)


def test_concept_switchposition_constructor_exists():
    assert callable(Concept_SwitchPosition.__init__)


def test_concept_switchposition_constructor_args():
    sig = inspect.signature(Concept_SwitchPosition.__init__)
    params = list(sig.parameters.keys())
    assert "SwitchPosition_switchState" in params, "Missing parameter 'SwitchPosition_switchState'"

def test_concept_switchposition_has_SwitchPosition_switchState():
    assert hasattr(Concept_SwitchPosition, "SwitchPosition_switchState")
    descriptor = None
    for klass in Concept_SwitchPosition.__mro__:
        if "SwitchPosition_switchState" in klass.__dict__:
            descriptor = klass.__dict__["SwitchPosition_switchState"]
            break
    assert isinstance(descriptor, property)



def test_concept_trackelement_is_not_abstract():
    assert not inspect.isabstract(Concept_Trackelement)


def test_concept_trackelement_constructor_exists():
    assert callable(Concept_Trackelement.__init__)


def test_concept_trackelement_constructor_args():
    sig = inspect.signature(Concept_Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(Trackelement)


def test_trackelement_constructor_exists():
    assert callable(Trackelement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_concept_switch_is_not_abstract():
    assert not inspect.isabstract(Concept_Switch)


def test_concept_switch_constructor_exists():
    assert callable(Concept_Switch.__init__)


def test_concept_switch_constructor_args():
    sig = inspect.signature(Concept_Switch.__init__)
    params = list(sig.parameters.keys())
    assert "Switch_actualState" in params, "Missing parameter 'Switch_actualState'"

def test_concept_switch_has_Switch_actualState():
    assert hasattr(Concept_Switch, "Switch_actualState")
    descriptor = None
    for klass in Concept_Switch.__mro__:
        if "Switch_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Switch_actualState"]
            break
    assert isinstance(descriptor, property)



def test_concept_segment_is_not_abstract():
    assert not inspect.isabstract(Concept_Segment)


def test_concept_segment_constructor_exists():
    assert callable(Concept_Segment.__init__)


def test_concept_segment_constructor_args():
    sig = inspect.signature(Concept_Segment.__init__)
    params = list(sig.parameters.keys())
    assert "Segment_length" in params, "Missing parameter 'Segment_length'"

def test_concept_segment_has_Segment_length():
    assert hasattr(Concept_Segment, "Segment_length")
    descriptor = None
    for klass in Concept_Segment.__mro__:
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
        "SignalStateKind_FAILURE",
        "SignalStateKind_GO",
        "SignalStateKind_STOP",
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
        "PointStateKind_STRAIGHT",
        "PointStateKind_FAILURE",
        "PointStateKind_LEFT",
        "PointStateKind_RIGHT",
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
Concept_Thing_strategy = st.builds(
    Concept_Thing,
)
Concept_IndividualContainer_strategy = st.builds(
    Concept_IndividualContainer,
)
Thing_strategy = st.builds(
    Thing,
)
Concept_Sensor_strategy = st.builds(
    Concept_Sensor,
)
Concept_Route_strategy = st.builds(
    Concept_Route,
)
Concept_Signal_strategy = st.builds(
    Concept_Signal,
    Signal_actualState=
        safe_text
)
Concept_SwitchPosition_strategy = st.builds(
    Concept_SwitchPosition,
    SwitchPosition_switchState=
        safe_text
)
Concept_Trackelement_strategy = st.builds(
    Concept_Trackelement,
)
Trackelement_strategy = st.builds(
    Trackelement,
)
Concept_Switch_strategy = st.builds(
    Concept_Switch,
    Switch_actualState=
        safe_text
)
Concept_Segment_strategy = st.builds(
    Concept_Segment,
    Segment_length=
        st.integers()
)

@given(instance=Concept_Thing_strategy)
@settings(max_examples=50)
def test_concept_thing_instantiation(instance):
    assert isinstance(instance, Concept_Thing)

@given(instance=Concept_IndividualContainer_strategy)
@settings(max_examples=50)
def test_concept_individualcontainer_instantiation(instance):
    assert isinstance(instance, Concept_IndividualContainer)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=Concept_Sensor_strategy)
@settings(max_examples=50)
def test_concept_sensor_instantiation(instance):
    assert isinstance(instance, Concept_Sensor)

@given(instance=Concept_Route_strategy)
@settings(max_examples=50)
def test_concept_route_instantiation(instance):
    assert isinstance(instance, Concept_Route)

@given(instance=Concept_Signal_strategy)
@settings(max_examples=50)
def test_concept_signal_instantiation(instance):
    assert isinstance(instance, Concept_Signal)



@given(instance=Concept_Signal_strategy)
def test_concept_signal_Signal_actualState_setter(instance):
    original = instance.Signal_actualState
    instance.Signal_actualState = original
    assert instance.Signal_actualState == original

@given(instance=Concept_SwitchPosition_strategy)
@settings(max_examples=50)
def test_concept_switchposition_instantiation(instance):
    assert isinstance(instance, Concept_SwitchPosition)



@given(instance=Concept_SwitchPosition_strategy)
def test_concept_switchposition_SwitchPosition_switchState_setter(instance):
    original = instance.SwitchPosition_switchState
    instance.SwitchPosition_switchState = original
    assert instance.SwitchPosition_switchState == original

@given(instance=Concept_Trackelement_strategy)
@settings(max_examples=50)
def test_concept_trackelement_instantiation(instance):
    assert isinstance(instance, Concept_Trackelement)

@given(instance=Trackelement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, Trackelement)

@given(instance=Concept_Switch_strategy)
@settings(max_examples=50)
def test_concept_switch_instantiation(instance):
    assert isinstance(instance, Concept_Switch)



@given(instance=Concept_Switch_strategy)
def test_concept_switch_Switch_actualState_setter(instance):
    original = instance.Switch_actualState
    instance.Switch_actualState = original
    assert instance.Switch_actualState == original

@given(instance=Concept_Segment_strategy)
@settings(max_examples=50)
def test_concept_segment_instantiation(instance):
    assert isinstance(instance, Concept_Segment)



@given(instance=Concept_Segment_strategy)
def test_concept_segment_Segment_length_setter(instance):
    original = instance.Segment_length
    instance.Segment_length = original
    assert instance.Segment_length == original
