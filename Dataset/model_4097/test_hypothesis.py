import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Signal,
    RDM::TurnoutSignal,
    Section,
    TrackElement,
    RDM::RDMElement,
    RDM::RailwayDomainModel,
    RDM::Station,
    RDMElement,
    RDM::Train,
    RDM::TrackElement,
    RDM::RouteElement,
    RDM::Route,
    RDM::TurnoutDesiredDirection,
    RDM::Signal,
    RDM::ConnectionPoint,
    RDM::Turnout,
    RDM::Section,
    ConnectionDirection,
    TurnoutDirection,
    Speed,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_rdm::turnoutsignal_is_not_abstract():
    assert not inspect.isabstract(RDM::TurnoutSignal)


def test_rdm::turnoutsignal_constructor_exists():
    assert callable(RDM::TurnoutSignal.__init__)


def test_rdm::turnoutsignal_constructor_args():
    sig = inspect.signature(RDM::TurnoutSignal.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_trackelement_is_not_abstract():
    assert not inspect.isabstract(TrackElement)


def test_trackelement_constructor_exists():
    assert callable(TrackElement.__init__)


def test_trackelement_constructor_args():
    sig = inspect.signature(TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm::rdmelement_is_not_abstract():
    assert not inspect.isabstract(RDM::RDMElement)


def test_rdm::rdmelement_constructor_exists():
    assert callable(RDM::RDMElement.__init__)


def test_rdm::rdmelement_constructor_args():
    sig = inspect.signature(RDM::RDMElement.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"

def test_rdm::rdmelement_has_length():
    assert hasattr(RDM::RDMElement, "length")
    descriptor = None
    for klass in RDM::RDMElement.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rdm::rdmelement_has_name():
    assert hasattr(RDM::RDMElement, "name")
    descriptor = None
    for klass in RDM::RDMElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rdm::railwaydomainmodel_is_not_abstract():
    assert not inspect.isabstract(RDM::RailwayDomainModel)


def test_rdm::railwaydomainmodel_constructor_exists():
    assert callable(RDM::RailwayDomainModel.__init__)


def test_rdm::railwaydomainmodel_constructor_args():
    sig = inspect.signature(RDM::RailwayDomainModel.__init__)
    params = list(sig.parameters.keys())



def test_rdm::station_is_not_abstract():
    assert not inspect.isabstract(RDM::Station)


def test_rdm::station_constructor_exists():
    assert callable(RDM::Station.__init__)


def test_rdm::station_constructor_args():
    sig = inspect.signature(RDM::Station.__init__)
    params = list(sig.parameters.keys())



def test_rdmelement_is_not_abstract():
    assert not inspect.isabstract(RDMElement)


def test_rdmelement_constructor_exists():
    assert callable(RDMElement.__init__)


def test_rdmelement_constructor_args():
    sig = inspect.signature(RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm::train_is_not_abstract():
    assert not inspect.isabstract(RDM::Train)


def test_rdm::train_constructor_exists():
    assert callable(RDM::Train.__init__)


def test_rdm::train_constructor_args():
    sig = inspect.signature(RDM::Train.__init__)
    params = list(sig.parameters.keys())
    assert "maxSpeed" in params, "Missing parameter 'maxSpeed'"
    assert "headingSpeed" in params, "Missing parameter 'headingSpeed'"

def test_rdm::train_has_maxSpeed():
    assert hasattr(RDM::Train, "maxSpeed")
    descriptor = None
    for klass in RDM::Train.__mro__:
        if "maxSpeed" in klass.__dict__:
            descriptor = klass.__dict__["maxSpeed"]
            break
    assert isinstance(descriptor, property)

def test_rdm::train_has_headingSpeed():
    assert hasattr(RDM::Train, "headingSpeed")
    descriptor = None
    for klass in RDM::Train.__mro__:
        if "headingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["headingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_rdm::trackelement_is_not_abstract():
    assert not inspect.isabstract(RDM::TrackElement)


def test_rdm::trackelement_constructor_exists():
    assert callable(RDM::TrackElement.__init__)


def test_rdm::trackelement_constructor_args():
    sig = inspect.signature(RDM::TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm::routeelement_is_not_abstract():
    assert not inspect.isabstract(RDM::RouteElement)


def test_rdm::routeelement_constructor_exists():
    assert callable(RDM::RouteElement.__init__)


def test_rdm::routeelement_constructor_args():
    sig = inspect.signature(RDM::RouteElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm::route_is_not_abstract():
    assert not inspect.isabstract(RDM::Route)


def test_rdm::route_constructor_exists():
    assert callable(RDM::Route.__init__)


def test_rdm::route_constructor_args():
    sig = inspect.signature(RDM::Route.__init__)
    params = list(sig.parameters.keys())



def test_rdm::turnoutdesireddirection_is_not_abstract():
    assert not inspect.isabstract(RDM::TurnoutDesiredDirection)


def test_rdm::turnoutdesireddirection_constructor_exists():
    assert callable(RDM::TurnoutDesiredDirection.__init__)


def test_rdm::turnoutdesireddirection_constructor_args():
    sig = inspect.signature(RDM::TurnoutDesiredDirection.__init__)
    params = list(sig.parameters.keys())
    assert "desiredDirection" in params, "Missing parameter 'desiredDirection'"

def test_rdm::turnoutdesireddirection_has_desiredDirection():
    assert hasattr(RDM::TurnoutDesiredDirection, "desiredDirection")
    descriptor = None
    for klass in RDM::TurnoutDesiredDirection.__mro__:
        if "desiredDirection" in klass.__dict__:
            descriptor = klass.__dict__["desiredDirection"]
            break
    assert isinstance(descriptor, property)



def test_rdm::signal_is_not_abstract():
    assert not inspect.isabstract(RDM::Signal)


def test_rdm::signal_constructor_exists():
    assert callable(RDM::Signal.__init__)


def test_rdm::signal_constructor_args():
    sig = inspect.signature(RDM::Signal.__init__)
    params = list(sig.parameters.keys())
    assert "allowedSpeed" in params, "Missing parameter 'allowedSpeed'"

def test_rdm::signal_has_allowedSpeed():
    assert hasattr(RDM::Signal, "allowedSpeed")
    descriptor = None
    for klass in RDM::Signal.__mro__:
        if "allowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["allowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_rdm::connectionpoint_is_not_abstract():
    assert not inspect.isabstract(RDM::ConnectionPoint)


def test_rdm::connectionpoint_constructor_exists():
    assert callable(RDM::ConnectionPoint.__init__)


def test_rdm::connectionpoint_constructor_args():
    sig = inspect.signature(RDM::ConnectionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_rdm::connectionpoint_has_direction():
    assert hasattr(RDM::ConnectionPoint, "direction")
    descriptor = None
    for klass in RDM::ConnectionPoint.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_rdm::turnout_is_not_abstract():
    assert not inspect.isabstract(RDM::Turnout)


def test_rdm::turnout_constructor_exists():
    assert callable(RDM::Turnout.__init__)


def test_rdm::turnout_constructor_args():
    sig = inspect.signature(RDM::Turnout.__init__)
    params = list(sig.parameters.keys())
    assert "currentDirection" in params, "Missing parameter 'currentDirection'"
    assert "switchingDirection" in params, "Missing parameter 'switchingDirection'"

def test_rdm::turnout_has_currentDirection():
    assert hasattr(RDM::Turnout, "currentDirection")
    descriptor = None
    for klass in RDM::Turnout.__mro__:
        if "currentDirection" in klass.__dict__:
            descriptor = klass.__dict__["currentDirection"]
            break
    assert isinstance(descriptor, property)

def test_rdm::turnout_has_switchingDirection():
    assert hasattr(RDM::Turnout, "switchingDirection")
    descriptor = None
    for klass in RDM::Turnout.__mro__:
        if "switchingDirection" in klass.__dict__:
            descriptor = klass.__dict__["switchingDirection"]
            break
    assert isinstance(descriptor, property)



def test_rdm::section_is_not_abstract():
    assert not inspect.isabstract(RDM::Section)


def test_rdm::section_constructor_exists():
    assert callable(RDM::Section.__init__)


def test_rdm::section_constructor_args():
    sig = inspect.signature(RDM::Section.__init__)
    params = list(sig.parameters.keys())

def test_connectiondirection_exists():
    # Check that the Enumeration exists
    assert ConnectionDirection is not None

def test_connectiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionDirection]
    expected_literals = [
        "TOP",
        "RIGHT",
        "STRAIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionDirection"

def test_turnoutdirection_exists():
    # Check that the Enumeration exists
    assert TurnoutDirection is not None

def test_turnoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TurnoutDirection]
    expected_literals = [
        "STRAIGHT",
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TurnoutDirection"

def test_speed_exists():
    # Check that the Enumeration exists
    assert Speed is not None

def test_speed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Speed]
    expected_literals = [
        "FOURTY",
        "TWENTY",
        "ZERO",
        "SIXTY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Speed"


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
Signal_strategy = st.builds(
    Signal,
)
RDM::TurnoutSignal_strategy = st.builds(
    RDM::TurnoutSignal,
)
Section_strategy = st.builds(
    Section,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
RDM::RDMElement_strategy = st.builds(
    RDM::RDMElement,
    length=
        st.integers(),
    name=
        safe_text
)
RDM::RailwayDomainModel_strategy = st.builds(
    RDM::RailwayDomainModel,
)
RDM::Station_strategy = st.builds(
    RDM::Station,
)
RDMElement_strategy = st.builds(
    RDMElement,
)
RDM::Train_strategy = st.builds(
    RDM::Train,
    maxSpeed=
        safe_text,
    headingSpeed=
        safe_text
)
RDM::TrackElement_strategy = st.builds(
    RDM::TrackElement,
)
RDM::RouteElement_strategy = st.builds(
    RDM::RouteElement,
)
RDM::Route_strategy = st.builds(
    RDM::Route,
)
RDM::TurnoutDesiredDirection_strategy = st.builds(
    RDM::TurnoutDesiredDirection,
    desiredDirection=
        safe_text
)
RDM::Signal_strategy = st.builds(
    RDM::Signal,
    allowedSpeed=
        safe_text
)
RDM::ConnectionPoint_strategy = st.builds(
    RDM::ConnectionPoint,
    direction=
        safe_text
)
RDM::Turnout_strategy = st.builds(
    RDM::Turnout,
    currentDirection=
        safe_text,
    switchingDirection=
        safe_text
)
RDM::Section_strategy = st.builds(
    RDM::Section,
)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=RDM::TurnoutSignal_strategy)
@settings(max_examples=50)
def test_rdm::turnoutsignal_instantiation(instance):
    assert isinstance(instance, RDM::TurnoutSignal)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=RDM::RDMElement_strategy)
@settings(max_examples=50)
def test_rdm::rdmelement_instantiation(instance):
    assert isinstance(instance, RDM::RDMElement)

@given(instance=RDM::RDMElement_strategy)
def test_rdm::rdmelement_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=RDM::RDMElement_strategy)
def test_rdm::rdmelement_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=RDM::RDMElement_strategy)
def test_rdm::rdmelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=RDM::RDMElement_strategy)
def test_rdm::rdmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RDM::RailwayDomainModel_strategy)
@settings(max_examples=50)
def test_rdm::railwaydomainmodel_instantiation(instance):
    assert isinstance(instance, RDM::RailwayDomainModel)

@given(instance=RDM::Station_strategy)
@settings(max_examples=50)
def test_rdm::station_instantiation(instance):
    assert isinstance(instance, RDM::Station)

@given(instance=RDMElement_strategy)
@settings(max_examples=50)
def test_rdmelement_instantiation(instance):
    assert isinstance(instance, RDMElement)

@given(instance=RDM::Train_strategy)
@settings(max_examples=50)
def test_rdm::train_instantiation(instance):
    assert isinstance(instance, RDM::Train)

@given(instance=RDM::Train_strategy)
def test_rdm::train_maxSpeed_type(instance):
    assert isinstance(instance.maxSpeed, str)


@given(instance=RDM::Train_strategy)
def test_rdm::train_maxSpeed_setter(instance):
    original = instance.maxSpeed
    instance.maxSpeed = original
    assert instance.maxSpeed == original

@given(instance=RDM::Train_strategy)
def test_rdm::train_headingSpeed_type(instance):
    assert isinstance(instance.headingSpeed, str)


@given(instance=RDM::Train_strategy)
def test_rdm::train_headingSpeed_setter(instance):
    original = instance.headingSpeed
    instance.headingSpeed = original
    assert instance.headingSpeed == original

@given(instance=RDM::TrackElement_strategy)
@settings(max_examples=50)
def test_rdm::trackelement_instantiation(instance):
    assert isinstance(instance, RDM::TrackElement)

@given(instance=RDM::RouteElement_strategy)
@settings(max_examples=50)
def test_rdm::routeelement_instantiation(instance):
    assert isinstance(instance, RDM::RouteElement)

@given(instance=RDM::Route_strategy)
@settings(max_examples=50)
def test_rdm::route_instantiation(instance):
    assert isinstance(instance, RDM::Route)

@given(instance=RDM::TurnoutDesiredDirection_strategy)
@settings(max_examples=50)
def test_rdm::turnoutdesireddirection_instantiation(instance):
    assert isinstance(instance, RDM::TurnoutDesiredDirection)

@given(instance=RDM::TurnoutDesiredDirection_strategy)
def test_rdm::turnoutdesireddirection_desiredDirection_type(instance):
    assert isinstance(instance.desiredDirection, str)


@given(instance=RDM::TurnoutDesiredDirection_strategy)
def test_rdm::turnoutdesireddirection_desiredDirection_setter(instance):
    original = instance.desiredDirection
    instance.desiredDirection = original
    assert instance.desiredDirection == original

@given(instance=RDM::Signal_strategy)
@settings(max_examples=50)
def test_rdm::signal_instantiation(instance):
    assert isinstance(instance, RDM::Signal)

@given(instance=RDM::Signal_strategy)
def test_rdm::signal_allowedSpeed_type(instance):
    assert isinstance(instance.allowedSpeed, str)


@given(instance=RDM::Signal_strategy)
def test_rdm::signal_allowedSpeed_setter(instance):
    original = instance.allowedSpeed
    instance.allowedSpeed = original
    assert instance.allowedSpeed == original

@given(instance=RDM::ConnectionPoint_strategy)
@settings(max_examples=50)
def test_rdm::connectionpoint_instantiation(instance):
    assert isinstance(instance, RDM::ConnectionPoint)

@given(instance=RDM::ConnectionPoint_strategy)
def test_rdm::connectionpoint_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=RDM::ConnectionPoint_strategy)
def test_rdm::connectionpoint_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=RDM::Turnout_strategy)
@settings(max_examples=50)
def test_rdm::turnout_instantiation(instance):
    assert isinstance(instance, RDM::Turnout)

@given(instance=RDM::Turnout_strategy)
def test_rdm::turnout_currentDirection_type(instance):
    assert isinstance(instance.currentDirection, str)


@given(instance=RDM::Turnout_strategy)
def test_rdm::turnout_currentDirection_setter(instance):
    original = instance.currentDirection
    instance.currentDirection = original
    assert instance.currentDirection == original

@given(instance=RDM::Turnout_strategy)
def test_rdm::turnout_switchingDirection_type(instance):
    assert isinstance(instance.switchingDirection, str)


@given(instance=RDM::Turnout_strategy)
def test_rdm::turnout_switchingDirection_setter(instance):
    original = instance.switchingDirection
    instance.switchingDirection = original
    assert instance.switchingDirection == original

@given(instance=RDM::Section_strategy)
@settings(max_examples=50)
def test_rdm::section_instantiation(instance):
    assert isinstance(instance, RDM::Section)
