import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ConceptASE::IndividualContainer,
    ConceptASE::Thing,
    Thing,
    ConceptASE::Route,
    ConceptASE::Sensor,
    ConceptASE::SwitchPosition,
    ConceptASE::Signal,
    ConceptASE::Trackelement,
    Trackelement,
    ConceptASE::Switch,
    ConceptASE::Segment,
    SwitchStateKind,
    SignalStateKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_conceptase::individualcontainer_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::IndividualContainer)


def test_conceptase::individualcontainer_constructor_exists():
    assert callable(ConceptASE::IndividualContainer.__init__)


def test_conceptase::individualcontainer_constructor_args():
    sig = inspect.signature(ConceptASE::IndividualContainer.__init__)
    params = list(sig.parameters.keys())



def test_conceptase::thing_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Thing)


def test_conceptase::thing_constructor_exists():
    assert callable(ConceptASE::Thing.__init__)


def test_conceptase::thing_constructor_args():
    sig = inspect.signature(ConceptASE::Thing.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_conceptase::route_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Route)


def test_conceptase::route_constructor_exists():
    assert callable(ConceptASE::Route.__init__)


def test_conceptase::route_constructor_args():
    sig = inspect.signature(ConceptASE::Route.__init__)
    params = list(sig.parameters.keys())



def test_conceptase::sensor_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Sensor)


def test_conceptase::sensor_constructor_exists():
    assert callable(ConceptASE::Sensor.__init__)


def test_conceptase::sensor_constructor_args():
    sig = inspect.signature(ConceptASE::Sensor.__init__)
    params = list(sig.parameters.keys())
    assert "Sensor_year" in params, "Missing parameter 'Sensor_year'"

def test_conceptase::sensor_has_Sensor_year():
    assert hasattr(ConceptASE::Sensor, "Sensor_year")
    descriptor = None
    for klass in ConceptASE::Sensor.__mro__:
        if "Sensor_year" in klass.__dict__:
            descriptor = klass.__dict__["Sensor_year"]
            break
    assert isinstance(descriptor, property)



def test_conceptase::switchposition_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::SwitchPosition)


def test_conceptase::switchposition_constructor_exists():
    assert callable(ConceptASE::SwitchPosition.__init__)


def test_conceptase::switchposition_constructor_args():
    sig = inspect.signature(ConceptASE::SwitchPosition.__init__)
    params = list(sig.parameters.keys())
    assert "SwitchPosition_switchState" in params, "Missing parameter 'SwitchPosition_switchState'"

def test_conceptase::switchposition_has_SwitchPosition_switchState():
    assert hasattr(ConceptASE::SwitchPosition, "SwitchPosition_switchState")
    descriptor = None
    for klass in ConceptASE::SwitchPosition.__mro__:
        if "SwitchPosition_switchState" in klass.__dict__:
            descriptor = klass.__dict__["SwitchPosition_switchState"]
            break
    assert isinstance(descriptor, property)



def test_conceptase::signal_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Signal)


def test_conceptase::signal_constructor_exists():
    assert callable(ConceptASE::Signal.__init__)


def test_conceptase::signal_constructor_args():
    sig = inspect.signature(ConceptASE::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "Signal_actualState" in params, "Missing parameter 'Signal_actualState'"

def test_conceptase::signal_has_Signal_actualState():
    assert hasattr(ConceptASE::Signal, "Signal_actualState")
    descriptor = None
    for klass in ConceptASE::Signal.__mro__:
        if "Signal_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Signal_actualState"]
            break
    assert isinstance(descriptor, property)



def test_conceptase::trackelement_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Trackelement)


def test_conceptase::trackelement_constructor_exists():
    assert callable(ConceptASE::Trackelement.__init__)


def test_conceptase::trackelement_constructor_args():
    sig = inspect.signature(ConceptASE::Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(Trackelement)


def test_trackelement_constructor_exists():
    assert callable(Trackelement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(Trackelement.__init__)
    params = list(sig.parameters.keys())



def test_conceptase::switch_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Switch)


def test_conceptase::switch_constructor_exists():
    assert callable(ConceptASE::Switch.__init__)


def test_conceptase::switch_constructor_args():
    sig = inspect.signature(ConceptASE::Switch.__init__)
    params = list(sig.parameters.keys())
    assert "Switch_actualState" in params, "Missing parameter 'Switch_actualState'"

def test_conceptase::switch_has_Switch_actualState():
    assert hasattr(ConceptASE::Switch, "Switch_actualState")
    descriptor = None
    for klass in ConceptASE::Switch.__mro__:
        if "Switch_actualState" in klass.__dict__:
            descriptor = klass.__dict__["Switch_actualState"]
            break
    assert isinstance(descriptor, property)



def test_conceptase::segment_is_not_abstract():
    assert not inspect.isabstract(ConceptASE::Segment)


def test_conceptase::segment_constructor_exists():
    assert callable(ConceptASE::Segment.__init__)


def test_conceptase::segment_constructor_args():
    sig = inspect.signature(ConceptASE::Segment.__init__)
    params = list(sig.parameters.keys())
    assert "Segment_length" in params, "Missing parameter 'Segment_length'"
    assert "Segment_height" in params, "Missing parameter 'Segment_height'"

def test_conceptase::segment_has_Segment_length():
    assert hasattr(ConceptASE::Segment, "Segment_length")
    descriptor = None
    for klass in ConceptASE::Segment.__mro__:
        if "Segment_length" in klass.__dict__:
            descriptor = klass.__dict__["Segment_length"]
            break
    assert isinstance(descriptor, property)

def test_conceptase::segment_has_Segment_height():
    assert hasattr(ConceptASE::Segment, "Segment_height")
    descriptor = None
    for klass in ConceptASE::Segment.__mro__:
        if "Segment_height" in klass.__dict__:
            descriptor = klass.__dict__["Segment_height"]
            break
    assert isinstance(descriptor, property)

def test_switchstatekind_exists():
    # Check that the Enumeration exists
    assert SwitchStateKind is not None

def test_switchstatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SwitchStateKind]
    expected_literals = [
        "PointStateKind_FAILURE",
        "PointStateKind_STRAIGHT",
        "PointStateKind_LEFT",
        "PointStateKind_RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SwitchStateKind"

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
ConceptASE::IndividualContainer_strategy = st.builds(
    ConceptASE::IndividualContainer,
)
ConceptASE::Thing_strategy = st.builds(
    ConceptASE::Thing,
)
Thing_strategy = st.builds(
    Thing,
)
ConceptASE::Route_strategy = st.builds(
    ConceptASE::Route,
)
ConceptASE::Sensor_strategy = st.builds(
    ConceptASE::Sensor,
    Sensor_year=
        st.integers()
)
ConceptASE::SwitchPosition_strategy = st.builds(
    ConceptASE::SwitchPosition,
    SwitchPosition_switchState=
        safe_text
)
ConceptASE::Signal_strategy = st.builds(
    ConceptASE::Signal,
    Signal_actualState=
        safe_text
)
ConceptASE::Trackelement_strategy = st.builds(
    ConceptASE::Trackelement,
)
Trackelement_strategy = st.builds(
    Trackelement,
)
ConceptASE::Switch_strategy = st.builds(
    ConceptASE::Switch,
    Switch_actualState=
        safe_text
)
ConceptASE::Segment_strategy = st.builds(
    ConceptASE::Segment,
    Segment_length=
        st.integers(),
    Segment_height=
        st.integers()
)

@given(instance=ConceptASE::IndividualContainer_strategy)
@settings(max_examples=50)
def test_conceptase::individualcontainer_instantiation(instance):
    assert isinstance(instance, ConceptASE::IndividualContainer)

@given(instance=ConceptASE::Thing_strategy)
@settings(max_examples=50)
def test_conceptase::thing_instantiation(instance):
    assert isinstance(instance, ConceptASE::Thing)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=ConceptASE::Route_strategy)
@settings(max_examples=50)
def test_conceptase::route_instantiation(instance):
    assert isinstance(instance, ConceptASE::Route)

@given(instance=ConceptASE::Sensor_strategy)
@settings(max_examples=50)
def test_conceptase::sensor_instantiation(instance):
    assert isinstance(instance, ConceptASE::Sensor)

@given(instance=ConceptASE::Sensor_strategy)
def test_conceptase::sensor_Sensor_year_type(instance):
    assert isinstance(instance.Sensor_year, int)


@given(instance=ConceptASE::Sensor_strategy)
def test_conceptase::sensor_Sensor_year_setter(instance):
    original = instance.Sensor_year
    instance.Sensor_year = original
    assert instance.Sensor_year == original

@given(instance=ConceptASE::SwitchPosition_strategy)
@settings(max_examples=50)
def test_conceptase::switchposition_instantiation(instance):
    assert isinstance(instance, ConceptASE::SwitchPosition)

@given(instance=ConceptASE::SwitchPosition_strategy)
def test_conceptase::switchposition_SwitchPosition_switchState_type(instance):
    assert isinstance(instance.SwitchPosition_switchState, str)


@given(instance=ConceptASE::SwitchPosition_strategy)
def test_conceptase::switchposition_SwitchPosition_switchState_setter(instance):
    original = instance.SwitchPosition_switchState
    instance.SwitchPosition_switchState = original
    assert instance.SwitchPosition_switchState == original

@given(instance=ConceptASE::Signal_strategy)
@settings(max_examples=50)
def test_conceptase::signal_instantiation(instance):
    assert isinstance(instance, ConceptASE::Signal)

@given(instance=ConceptASE::Signal_strategy)
def test_conceptase::signal_Signal_actualState_type(instance):
    assert isinstance(instance.Signal_actualState, str)


@given(instance=ConceptASE::Signal_strategy)
def test_conceptase::signal_Signal_actualState_setter(instance):
    original = instance.Signal_actualState
    instance.Signal_actualState = original
    assert instance.Signal_actualState == original

@given(instance=ConceptASE::Trackelement_strategy)
@settings(max_examples=50)
def test_conceptase::trackelement_instantiation(instance):
    assert isinstance(instance, ConceptASE::Trackelement)

@given(instance=Trackelement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, Trackelement)

@given(instance=ConceptASE::Switch_strategy)
@settings(max_examples=50)
def test_conceptase::switch_instantiation(instance):
    assert isinstance(instance, ConceptASE::Switch)

@given(instance=ConceptASE::Switch_strategy)
def test_conceptase::switch_Switch_actualState_type(instance):
    assert isinstance(instance.Switch_actualState, str)


@given(instance=ConceptASE::Switch_strategy)
def test_conceptase::switch_Switch_actualState_setter(instance):
    original = instance.Switch_actualState
    instance.Switch_actualState = original
    assert instance.Switch_actualState == original

@given(instance=ConceptASE::Segment_strategy)
@settings(max_examples=50)
def test_conceptase::segment_instantiation(instance):
    assert isinstance(instance, ConceptASE::Segment)

@given(instance=ConceptASE::Segment_strategy)
def test_conceptase::segment_Segment_length_type(instance):
    assert isinstance(instance.Segment_length, int)


@given(instance=ConceptASE::Segment_strategy)
def test_conceptase::segment_Segment_length_setter(instance):
    original = instance.Segment_length
    instance.Segment_length = original
    assert instance.Segment_length == original

@given(instance=ConceptASE::Segment_strategy)
def test_conceptase::segment_Segment_height_type(instance):
    assert isinstance(instance.Segment_height, int)


@given(instance=ConceptASE::Segment_strategy)
def test_conceptase::segment_Segment_height_setter(instance):
    original = instance.Segment_height
    instance.Segment_height = original
    assert instance.Segment_height == original
