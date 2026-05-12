import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Signal,
    RDM_TurnoutSignal,
    Section,
    TrackElement,
    RDM_RDMElement,
    RDM_RailwayDomainModel,
    RDM_Station,
    RDMElement,
    RDM_TrackElement,
    RDM_Train,
    RDM_RouteElement,
    RDM_Route,
    RDM_TurnoutDesiredDirection,
    RDM_Signal,
    RDM_ConnectionPoint,
    RDM_Turnout,
    RDM_Section,
    Speed,
    TurnoutDirection,
    ConnectionDirection,
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



def test_rdm_turnoutsignal_is_not_abstract():
    assert not inspect.isabstract(RDM_TurnoutSignal)


def test_rdm_turnoutsignal_constructor_exists():
    assert callable(RDM_TurnoutSignal.__init__)


def test_rdm_turnoutsignal_constructor_args():
    sig = inspect.signature(RDM_TurnoutSignal.__init__)
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



def test_rdm_rdmelement_is_not_abstract():
    assert not inspect.isabstract(RDM_RDMElement)


def test_rdm_rdmelement_constructor_exists():
    assert callable(RDM_RDMElement.__init__)


def test_rdm_rdmelement_constructor_args():
    sig = inspect.signature(RDM_RDMElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "length" in params, "Missing parameter 'length'"

def test_rdm_rdmelement_has_name():
    assert hasattr(RDM_RDMElement, "name")
    descriptor = None
    for klass in RDM_RDMElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_rdm_rdmelement_has_length():
    assert hasattr(RDM_RDMElement, "length")
    descriptor = None
    for klass in RDM_RDMElement.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)



def test_rdm_railwaydomainmodel_is_not_abstract():
    assert not inspect.isabstract(RDM_RailwayDomainModel)


def test_rdm_railwaydomainmodel_constructor_exists():
    assert callable(RDM_RailwayDomainModel.__init__)


def test_rdm_railwaydomainmodel_constructor_args():
    sig = inspect.signature(RDM_RailwayDomainModel.__init__)
    params = list(sig.parameters.keys())



def test_rdm_station_is_not_abstract():
    assert not inspect.isabstract(RDM_Station)


def test_rdm_station_constructor_exists():
    assert callable(RDM_Station.__init__)


def test_rdm_station_constructor_args():
    sig = inspect.signature(RDM_Station.__init__)
    params = list(sig.parameters.keys())



def test_rdmelement_is_not_abstract():
    assert not inspect.isabstract(RDMElement)


def test_rdmelement_constructor_exists():
    assert callable(RDMElement.__init__)


def test_rdmelement_constructor_args():
    sig = inspect.signature(RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm_trackelement_is_not_abstract():
    assert not inspect.isabstract(RDM_TrackElement)


def test_rdm_trackelement_constructor_exists():
    assert callable(RDM_TrackElement.__init__)


def test_rdm_trackelement_constructor_args():
    sig = inspect.signature(RDM_TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm_train_is_not_abstract():
    assert not inspect.isabstract(RDM_Train)


def test_rdm_train_constructor_exists():
    assert callable(RDM_Train.__init__)


def test_rdm_train_constructor_args():
    sig = inspect.signature(RDM_Train.__init__)
    params = list(sig.parameters.keys())
    assert "headingSpeed" in params, "Missing parameter 'headingSpeed'"
    assert "maxSpeed" in params, "Missing parameter 'maxSpeed'"

def test_rdm_train_has_headingSpeed():
    assert hasattr(RDM_Train, "headingSpeed")
    descriptor = None
    for klass in RDM_Train.__mro__:
        if "headingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["headingSpeed"]
            break
    assert isinstance(descriptor, property)

def test_rdm_train_has_maxSpeed():
    assert hasattr(RDM_Train, "maxSpeed")
    descriptor = None
    for klass in RDM_Train.__mro__:
        if "maxSpeed" in klass.__dict__:
            descriptor = klass.__dict__["maxSpeed"]
            break
    assert isinstance(descriptor, property)



def test_rdm_routeelement_is_not_abstract():
    assert not inspect.isabstract(RDM_RouteElement)


def test_rdm_routeelement_constructor_exists():
    assert callable(RDM_RouteElement.__init__)


def test_rdm_routeelement_constructor_args():
    sig = inspect.signature(RDM_RouteElement.__init__)
    params = list(sig.parameters.keys())



def test_rdm_route_is_not_abstract():
    assert not inspect.isabstract(RDM_Route)


def test_rdm_route_constructor_exists():
    assert callable(RDM_Route.__init__)


def test_rdm_route_constructor_args():
    sig = inspect.signature(RDM_Route.__init__)
    params = list(sig.parameters.keys())



def test_rdm_turnoutdesireddirection_is_not_abstract():
    assert not inspect.isabstract(RDM_TurnoutDesiredDirection)


def test_rdm_turnoutdesireddirection_constructor_exists():
    assert callable(RDM_TurnoutDesiredDirection.__init__)


def test_rdm_turnoutdesireddirection_constructor_args():
    sig = inspect.signature(RDM_TurnoutDesiredDirection.__init__)
    params = list(sig.parameters.keys())
    assert "desiredDirection" in params, "Missing parameter 'desiredDirection'"

def test_rdm_turnoutdesireddirection_has_desiredDirection():
    assert hasattr(RDM_TurnoutDesiredDirection, "desiredDirection")
    descriptor = None
    for klass in RDM_TurnoutDesiredDirection.__mro__:
        if "desiredDirection" in klass.__dict__:
            descriptor = klass.__dict__["desiredDirection"]
            break
    assert isinstance(descriptor, property)



def test_rdm_signal_is_not_abstract():
    assert not inspect.isabstract(RDM_Signal)


def test_rdm_signal_constructor_exists():
    assert callable(RDM_Signal.__init__)


def test_rdm_signal_constructor_args():
    sig = inspect.signature(RDM_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "allowedSpeed" in params, "Missing parameter 'allowedSpeed'"

def test_rdm_signal_has_allowedSpeed():
    assert hasattr(RDM_Signal, "allowedSpeed")
    descriptor = None
    for klass in RDM_Signal.__mro__:
        if "allowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["allowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_rdm_connectionpoint_is_not_abstract():
    assert not inspect.isabstract(RDM_ConnectionPoint)


def test_rdm_connectionpoint_constructor_exists():
    assert callable(RDM_ConnectionPoint.__init__)


def test_rdm_connectionpoint_constructor_args():
    sig = inspect.signature(RDM_ConnectionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_rdm_connectionpoint_has_direction():
    assert hasattr(RDM_ConnectionPoint, "direction")
    descriptor = None
    for klass in RDM_ConnectionPoint.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_rdm_turnout_is_not_abstract():
    assert not inspect.isabstract(RDM_Turnout)


def test_rdm_turnout_constructor_exists():
    assert callable(RDM_Turnout.__init__)


def test_rdm_turnout_constructor_args():
    sig = inspect.signature(RDM_Turnout.__init__)
    params = list(sig.parameters.keys())
    assert "currentDirection" in params, "Missing parameter 'currentDirection'"
    assert "switchingDirection" in params, "Missing parameter 'switchingDirection'"

def test_rdm_turnout_has_currentDirection():
    assert hasattr(RDM_Turnout, "currentDirection")
    descriptor = None
    for klass in RDM_Turnout.__mro__:
        if "currentDirection" in klass.__dict__:
            descriptor = klass.__dict__["currentDirection"]
            break
    assert isinstance(descriptor, property)

def test_rdm_turnout_has_switchingDirection():
    assert hasattr(RDM_Turnout, "switchingDirection")
    descriptor = None
    for klass in RDM_Turnout.__mro__:
        if "switchingDirection" in klass.__dict__:
            descriptor = klass.__dict__["switchingDirection"]
            break
    assert isinstance(descriptor, property)



def test_rdm_section_is_not_abstract():
    assert not inspect.isabstract(RDM_Section)


def test_rdm_section_constructor_exists():
    assert callable(RDM_Section.__init__)


def test_rdm_section_constructor_args():
    sig = inspect.signature(RDM_Section.__init__)
    params = list(sig.parameters.keys())

def test_speed_exists():
    # Check that the Enumeration exists
    assert Speed is not None

def test_speed_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Speed]
    expected_literals = [
        "ZERO",
        "TWENTY",
        "SIXTY",
        "FOURTY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Speed"

def test_turnoutdirection_exists():
    # Check that the Enumeration exists
    assert TurnoutDirection is not None

def test_turnoutdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TurnoutDirection]
    expected_literals = [
        "RIGHT",
        "STRAIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TurnoutDirection"

def test_connectiondirection_exists():
    # Check that the Enumeration exists
    assert ConnectionDirection is not None

def test_connectiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectionDirection]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "TOP",
        "STRAIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectionDirection"


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
RDM_TurnoutSignal_strategy = st.builds(
    RDM_TurnoutSignal,
)
Section_strategy = st.builds(
    Section,
)
TrackElement_strategy = st.builds(
    TrackElement,
)
RDM_RDMElement_strategy = st.builds(
    RDM_RDMElement,
    name=
        safe_text,
    length=
        st.integers()
)
RDM_RailwayDomainModel_strategy = st.builds(
    RDM_RailwayDomainModel,
)
RDM_Station_strategy = st.builds(
    RDM_Station,
)
RDMElement_strategy = st.builds(
    RDMElement,
)
RDM_TrackElement_strategy = st.builds(
    RDM_TrackElement,
)
RDM_Train_strategy = st.builds(
    RDM_Train,
    headingSpeed=
        safe_text,
    maxSpeed=
        safe_text
)
RDM_RouteElement_strategy = st.builds(
    RDM_RouteElement,
)
RDM_Route_strategy = st.builds(
    RDM_Route,
)
RDM_TurnoutDesiredDirection_strategy = st.builds(
    RDM_TurnoutDesiredDirection,
    desiredDirection=
        safe_text
)
RDM_Signal_strategy = st.builds(
    RDM_Signal,
    allowedSpeed=
        safe_text
)
RDM_ConnectionPoint_strategy = st.builds(
    RDM_ConnectionPoint,
    direction=
        safe_text
)
RDM_Turnout_strategy = st.builds(
    RDM_Turnout,
    currentDirection=
        safe_text,
    switchingDirection=
        safe_text
)
RDM_Section_strategy = st.builds(
    RDM_Section,
)

@given(instance=Signal_strategy)
@settings(max_examples=50)
def test_signal_instantiation(instance):
    assert isinstance(instance, Signal)

@given(instance=RDM_TurnoutSignal_strategy)
@settings(max_examples=50)
def test_rdm_turnoutsignal_instantiation(instance):
    assert isinstance(instance, RDM_TurnoutSignal)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=TrackElement_strategy)
@settings(max_examples=50)
def test_trackelement_instantiation(instance):
    assert isinstance(instance, TrackElement)

@given(instance=RDM_RDMElement_strategy)
@settings(max_examples=50)
def test_rdm_rdmelement_instantiation(instance):
    assert isinstance(instance, RDM_RDMElement)



@given(instance=RDM_RDMElement_strategy)
def test_rdm_rdmelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=RDM_RDMElement_strategy)
def test_rdm_rdmelement_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=RDM_RailwayDomainModel_strategy)
@settings(max_examples=50)
def test_rdm_railwaydomainmodel_instantiation(instance):
    assert isinstance(instance, RDM_RailwayDomainModel)

@given(instance=RDM_Station_strategy)
@settings(max_examples=50)
def test_rdm_station_instantiation(instance):
    assert isinstance(instance, RDM_Station)

@given(instance=RDMElement_strategy)
@settings(max_examples=50)
def test_rdmelement_instantiation(instance):
    assert isinstance(instance, RDMElement)

@given(instance=RDM_TrackElement_strategy)
@settings(max_examples=50)
def test_rdm_trackelement_instantiation(instance):
    assert isinstance(instance, RDM_TrackElement)

@given(instance=RDM_Train_strategy)
@settings(max_examples=50)
def test_rdm_train_instantiation(instance):
    assert isinstance(instance, RDM_Train)



@given(instance=RDM_Train_strategy)
def test_rdm_train_headingSpeed_setter(instance):
    original = instance.headingSpeed
    instance.headingSpeed = original
    assert instance.headingSpeed == original



@given(instance=RDM_Train_strategy)
def test_rdm_train_maxSpeed_setter(instance):
    original = instance.maxSpeed
    instance.maxSpeed = original
    assert instance.maxSpeed == original

@given(instance=RDM_RouteElement_strategy)
@settings(max_examples=50)
def test_rdm_routeelement_instantiation(instance):
    assert isinstance(instance, RDM_RouteElement)

@given(instance=RDM_Route_strategy)
@settings(max_examples=50)
def test_rdm_route_instantiation(instance):
    assert isinstance(instance, RDM_Route)

@given(instance=RDM_TurnoutDesiredDirection_strategy)
@settings(max_examples=50)
def test_rdm_turnoutdesireddirection_instantiation(instance):
    assert isinstance(instance, RDM_TurnoutDesiredDirection)



@given(instance=RDM_TurnoutDesiredDirection_strategy)
def test_rdm_turnoutdesireddirection_desiredDirection_setter(instance):
    original = instance.desiredDirection
    instance.desiredDirection = original
    assert instance.desiredDirection == original

@given(instance=RDM_Signal_strategy)
@settings(max_examples=50)
def test_rdm_signal_instantiation(instance):
    assert isinstance(instance, RDM_Signal)



@given(instance=RDM_Signal_strategy)
def test_rdm_signal_allowedSpeed_setter(instance):
    original = instance.allowedSpeed
    instance.allowedSpeed = original
    assert instance.allowedSpeed == original

@given(instance=RDM_ConnectionPoint_strategy)
@settings(max_examples=50)
def test_rdm_connectionpoint_instantiation(instance):
    assert isinstance(instance, RDM_ConnectionPoint)



@given(instance=RDM_ConnectionPoint_strategy)
def test_rdm_connectionpoint_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=RDM_Turnout_strategy)
@settings(max_examples=50)
def test_rdm_turnout_instantiation(instance):
    assert isinstance(instance, RDM_Turnout)



@given(instance=RDM_Turnout_strategy)
def test_rdm_turnout_currentDirection_setter(instance):
    original = instance.currentDirection
    instance.currentDirection = original
    assert instance.currentDirection == original



@given(instance=RDM_Turnout_strategy)
def test_rdm_turnout_switchingDirection_setter(instance):
    original = instance.switchingDirection
    instance.switchingDirection = original
    assert instance.switchingDirection == original

@given(instance=RDM_Section_strategy)
@settings(max_examples=50)
def test_rdm_section_instantiation(instance):
    assert isinstance(instance, RDM_Section)
