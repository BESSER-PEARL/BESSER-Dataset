import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    behaviour::Parameter,
    Action,
    behaviour::DeviceAction,
    behaviour::CommunicationAction,
    Notify,
    behaviour::MulticastNotify,
    behaviour::UnicastNotify,
    behaviour::BroadcastNotify,
    CommunicationAction,
    behaviour::Notify,
    behaviour::CheckNotification,
    behaviour::Feedback,
    MoveTransition,
    behaviour::Choice,
    Move,
    behaviour::Stop,
    behaviour::Hover,
    behaviour::HeadTo,
    behaviour::Circle,
    behaviour::Start,
    behaviour::MoveTransition,
    behaviour::Coordinate,
    behaviour::GoTo,
    behaviour::Land,
    behaviour::TakeOff,
    NamedElement,
    behaviour::Drone,
    behaviour::Slot,
    behaviour::Move,
    behaviour::Action,
    behaviour::Behaviour,
    behaviour::NamedElement,
    GoToStrategy,
    TravelMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behaviour::parameter_is_not_abstract():
    assert not inspect.isabstract(behaviour::Parameter)


def test_behaviour::parameter_constructor_exists():
    assert callable(behaviour::Parameter.__init__)


def test_behaviour::parameter_constructor_args():
    sig = inspect.signature(behaviour::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour::parameter_has_key():
    assert hasattr(behaviour::Parameter, "key")
    descriptor = None
    for klass in behaviour::Parameter.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::parameter_has_value():
    assert hasattr(behaviour::Parameter, "value")
    descriptor = None
    for klass in behaviour::Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::deviceaction_is_not_abstract():
    assert not inspect.isabstract(behaviour::DeviceAction)


def test_behaviour::deviceaction_constructor_exists():
    assert callable(behaviour::DeviceAction.__init__)


def test_behaviour::deviceaction_constructor_args():
    sig = inspect.signature(behaviour::DeviceAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionName" in params, "Missing parameter 'actionName'"

def test_behaviour::deviceaction_has_actionName():
    assert hasattr(behaviour::DeviceAction, "actionName")
    descriptor = None
    for klass in behaviour::DeviceAction.__mro__:
        if "actionName" in klass.__dict__:
            descriptor = klass.__dict__["actionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::communicationaction_is_not_abstract():
    assert not inspect.isabstract(behaviour::CommunicationAction)


def test_behaviour::communicationaction_constructor_exists():
    assert callable(behaviour::CommunicationAction.__init__)


def test_behaviour::communicationaction_constructor_args():
    sig = inspect.signature(behaviour::CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_notify_is_not_abstract():
    assert not inspect.isabstract(Notify)


def test_notify_constructor_exists():
    assert callable(Notify.__init__)


def test_notify_constructor_args():
    sig = inspect.signature(Notify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::multicastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour::MulticastNotify)


def test_behaviour::multicastnotify_constructor_exists():
    assert callable(behaviour::MulticastNotify.__init__)


def test_behaviour::multicastnotify_constructor_args():
    sig = inspect.signature(behaviour::MulticastNotify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::unicastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour::UnicastNotify)


def test_behaviour::unicastnotify_constructor_exists():
    assert callable(behaviour::UnicastNotify.__init__)


def test_behaviour::unicastnotify_constructor_args():
    sig = inspect.signature(behaviour::UnicastNotify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::broadcastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour::BroadcastNotify)


def test_behaviour::broadcastnotify_constructor_exists():
    assert callable(behaviour::BroadcastNotify.__init__)


def test_behaviour::broadcastnotify_constructor_args():
    sig = inspect.signature(behaviour::BroadcastNotify.__init__)
    params = list(sig.parameters.keys())



def test_communicationaction_is_not_abstract():
    assert not inspect.isabstract(CommunicationAction)


def test_communicationaction_constructor_exists():
    assert callable(CommunicationAction.__init__)


def test_communicationaction_constructor_args():
    sig = inspect.signature(CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::notify_is_not_abstract():
    assert not inspect.isabstract(behaviour::Notify)


def test_behaviour::notify_constructor_exists():
    assert callable(behaviour::Notify.__init__)


def test_behaviour::notify_constructor_args():
    sig = inspect.signature(behaviour::Notify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::checknotification_is_not_abstract():
    assert not inspect.isabstract(behaviour::CheckNotification)


def test_behaviour::checknotification_constructor_exists():
    assert callable(behaviour::CheckNotification.__init__)


def test_behaviour::checknotification_constructor_args():
    sig = inspect.signature(behaviour::CheckNotification.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::feedback_is_not_abstract():
    assert not inspect.isabstract(behaviour::Feedback)


def test_behaviour::feedback_constructor_exists():
    assert callable(behaviour::Feedback.__init__)


def test_behaviour::feedback_constructor_args():
    sig = inspect.signature(behaviour::Feedback.__init__)
    params = list(sig.parameters.keys())
    assert "actionName" in params, "Missing parameter 'actionName'"

def test_behaviour::feedback_has_actionName():
    assert hasattr(behaviour::Feedback, "actionName")
    descriptor = None
    for klass in behaviour::Feedback.__mro__:
        if "actionName" in klass.__dict__:
            descriptor = klass.__dict__["actionName"]
            break
    assert isinstance(descriptor, property)



def test_movetransition_is_not_abstract():
    assert not inspect.isabstract(MoveTransition)


def test_movetransition_constructor_exists():
    assert callable(MoveTransition.__init__)


def test_movetransition_constructor_args():
    sig = inspect.signature(MoveTransition.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::choice_is_not_abstract():
    assert not inspect.isabstract(behaviour::Choice)


def test_behaviour::choice_constructor_exists():
    assert callable(behaviour::Choice.__init__)


def test_behaviour::choice_constructor_args():
    sig = inspect.signature(behaviour::Choice.__init__)
    params = list(sig.parameters.keys())
    assert "conditionIdentifier" in params, "Missing parameter 'conditionIdentifier'"

def test_behaviour::choice_has_conditionIdentifier():
    assert hasattr(behaviour::Choice, "conditionIdentifier")
    descriptor = None
    for klass in behaviour::Choice.__mro__:
        if "conditionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["conditionIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_move_is_not_abstract():
    assert not inspect.isabstract(Move)


def test_move_constructor_exists():
    assert callable(Move.__init__)


def test_move_constructor_args():
    sig = inspect.signature(Move.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::stop_is_not_abstract():
    assert not inspect.isabstract(behaviour::Stop)


def test_behaviour::stop_constructor_exists():
    assert callable(behaviour::Stop.__init__)


def test_behaviour::stop_constructor_args():
    sig = inspect.signature(behaviour::Stop.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::hover_is_not_abstract():
    assert not inspect.isabstract(behaviour::Hover)


def test_behaviour::hover_constructor_exists():
    assert callable(behaviour::Hover.__init__)


def test_behaviour::hover_constructor_args():
    sig = inspect.signature(behaviour::Hover.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_behaviour::hover_has_duration():
    assert hasattr(behaviour::Hover, "duration")
    descriptor = None
    for klass in behaviour::Hover.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::headto_is_not_abstract():
    assert not inspect.isabstract(behaviour::HeadTo)


def test_behaviour::headto_constructor_exists():
    assert callable(behaviour::HeadTo.__init__)


def test_behaviour::headto_constructor_args():
    sig = inspect.signature(behaviour::HeadTo.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_behaviour::headto_has_direction():
    assert hasattr(behaviour::HeadTo, "direction")
    descriptor = None
    for klass in behaviour::HeadTo.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::circle_is_not_abstract():
    assert not inspect.isabstract(behaviour::Circle)


def test_behaviour::circle_constructor_exists():
    assert callable(behaviour::Circle.__init__)


def test_behaviour::circle_constructor_args():
    sig = inspect.signature(behaviour::Circle.__init__)
    params = list(sig.parameters.keys())
    assert "radius" in params, "Missing parameter 'radius'"
    assert "clockwise" in params, "Missing parameter 'clockwise'"
    assert "altitude" in params, "Missing parameter 'altitude'"
    assert "duration" in params, "Missing parameter 'duration'"

def test_behaviour::circle_has_radius():
    assert hasattr(behaviour::Circle, "radius")
    descriptor = None
    for klass in behaviour::Circle.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::circle_has_clockwise():
    assert hasattr(behaviour::Circle, "clockwise")
    descriptor = None
    for klass in behaviour::Circle.__mro__:
        if "clockwise" in klass.__dict__:
            descriptor = klass.__dict__["clockwise"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::circle_has_altitude():
    assert hasattr(behaviour::Circle, "altitude")
    descriptor = None
    for klass in behaviour::Circle.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::circle_has_duration():
    assert hasattr(behaviour::Circle, "duration")
    descriptor = None
    for klass in behaviour::Circle.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::start_is_not_abstract():
    assert not inspect.isabstract(behaviour::Start)


def test_behaviour::start_constructor_exists():
    assert callable(behaviour::Start.__init__)


def test_behaviour::start_constructor_args():
    sig = inspect.signature(behaviour::Start.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::movetransition_is_not_abstract():
    assert not inspect.isabstract(behaviour::MoveTransition)


def test_behaviour::movetransition_constructor_exists():
    assert callable(behaviour::MoveTransition.__init__)


def test_behaviour::movetransition_constructor_args():
    sig = inspect.signature(behaviour::MoveTransition.__init__)
    params = list(sig.parameters.keys())
    assert "fluid" in params, "Missing parameter 'fluid'"

def test_behaviour::movetransition_has_fluid():
    assert hasattr(behaviour::MoveTransition, "fluid")
    descriptor = None
    for klass in behaviour::MoveTransition.__mro__:
        if "fluid" in klass.__dict__:
            descriptor = klass.__dict__["fluid"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::coordinate_is_not_abstract():
    assert not inspect.isabstract(behaviour::Coordinate)


def test_behaviour::coordinate_constructor_exists():
    assert callable(behaviour::Coordinate.__init__)


def test_behaviour::coordinate_constructor_args():
    sig = inspect.signature(behaviour::Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "heading" in params, "Missing parameter 'heading'"
    assert "altitude" in params, "Missing parameter 'altitude'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "longitude" in params, "Missing parameter 'longitude'"

def test_behaviour::coordinate_has_heading():
    assert hasattr(behaviour::Coordinate, "heading")
    descriptor = None
    for klass in behaviour::Coordinate.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::coordinate_has_altitude():
    assert hasattr(behaviour::Coordinate, "altitude")
    descriptor = None
    for klass in behaviour::Coordinate.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::coordinate_has_latitude():
    assert hasattr(behaviour::Coordinate, "latitude")
    descriptor = None
    for klass in behaviour::Coordinate.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::coordinate_has_longitude():
    assert hasattr(behaviour::Coordinate, "longitude")
    descriptor = None
    for klass in behaviour::Coordinate.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::goto_is_not_abstract():
    assert not inspect.isabstract(behaviour::GoTo)


def test_behaviour::goto_constructor_exists():
    assert callable(behaviour::GoTo.__init__)


def test_behaviour::goto_constructor_args():
    sig = inspect.signature(behaviour::GoTo.__init__)
    params = list(sig.parameters.keys())
    assert "strategy" in params, "Missing parameter 'strategy'"

def test_behaviour::goto_has_strategy():
    assert hasattr(behaviour::GoTo, "strategy")
    descriptor = None
    for klass in behaviour::GoTo.__mro__:
        if "strategy" in klass.__dict__:
            descriptor = klass.__dict__["strategy"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::land_is_not_abstract():
    assert not inspect.isabstract(behaviour::Land)


def test_behaviour::land_constructor_exists():
    assert callable(behaviour::Land.__init__)


def test_behaviour::land_constructor_args():
    sig = inspect.signature(behaviour::Land.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::takeoff_is_not_abstract():
    assert not inspect.isabstract(behaviour::TakeOff)


def test_behaviour::takeoff_constructor_exists():
    assert callable(behaviour::TakeOff.__init__)


def test_behaviour::takeoff_constructor_args():
    sig = inspect.signature(behaviour::TakeOff.__init__)
    params = list(sig.parameters.keys())
    assert "altitude" in params, "Missing parameter 'altitude'"

def test_behaviour::takeoff_has_altitude():
    assert hasattr(behaviour::TakeOff, "altitude")
    descriptor = None
    for klass in behaviour::TakeOff.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::drone_is_not_abstract():
    assert not inspect.isabstract(behaviour::Drone)


def test_behaviour::drone_constructor_exists():
    assert callable(behaviour::Drone.__init__)


def test_behaviour::drone_constructor_args():
    sig = inspect.signature(behaviour::Drone.__init__)
    params = list(sig.parameters.keys())
    assert "travelMode" in params, "Missing parameter 'travelMode'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_behaviour::drone_has_travelMode():
    assert hasattr(behaviour::Drone, "travelMode")
    descriptor = None
    for klass in behaviour::Drone.__mro__:
        if "travelMode" in klass.__dict__:
            descriptor = klass.__dict__["travelMode"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::drone_has_typeName():
    assert hasattr(behaviour::Drone, "typeName")
    descriptor = None
    for klass in behaviour::Drone.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::slot_is_not_abstract():
    assert not inspect.isabstract(behaviour::Slot)


def test_behaviour::slot_constructor_exists():
    assert callable(behaviour::Slot.__init__)


def test_behaviour::slot_constructor_args():
    sig = inspect.signature(behaviour::Slot.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::move_is_not_abstract():
    assert not inspect.isabstract(behaviour::Move)


def test_behaviour::move_constructor_exists():
    assert callable(behaviour::Move.__init__)


def test_behaviour::move_constructor_args():
    sig = inspect.signature(behaviour::Move.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::action_is_not_abstract():
    assert not inspect.isabstract(behaviour::Action)


def test_behaviour::action_constructor_exists():
    assert callable(behaviour::Action.__init__)


def test_behaviour::action_constructor_args():
    sig = inspect.signature(behaviour::Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour::Behaviour)


def test_behaviour::behaviour_constructor_exists():
    assert callable(behaviour::Behaviour.__init__)


def test_behaviour::behaviour_constructor_args():
    sig = inspect.signature(behaviour::Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "crs" in params, "Missing parameter 'crs'"

def test_behaviour::behaviour_has_crs():
    assert hasattr(behaviour::Behaviour, "crs")
    descriptor = None
    for klass in behaviour::Behaviour.__mro__:
        if "crs" in klass.__dict__:
            descriptor = klass.__dict__["crs"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::namedelement_is_not_abstract():
    assert not inspect.isabstract(behaviour::NamedElement)


def test_behaviour::namedelement_constructor_exists():
    assert callable(behaviour::NamedElement.__init__)


def test_behaviour::namedelement_constructor_args():
    sig = inspect.signature(behaviour::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour::namedelement_has_name():
    assert hasattr(behaviour::NamedElement, "name")
    descriptor = None
    for klass in behaviour::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gotostrategy_exists():
    # Check that the Enumeration exists
    assert GoToStrategy is not None

def test_gotostrategy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoToStrategy]
    expected_literals = [
        "VERTICAL_FIRST",
        "DIRECT",
        "HORIZONTAL_FIRST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoToStrategy"

def test_travelmode_exists():
    # Check that the Enumeration exists
    assert TravelMode is not None

def test_travelmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TravelMode]
    expected_literals = [
        "SAFE",
        "NORMAL",
        "AGGRESSIVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TravelMode"


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
behaviour::Parameter_strategy = st.builds(
    behaviour::Parameter,
    key=
        safe_text,
    value=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
behaviour::DeviceAction_strategy = st.builds(
    behaviour::DeviceAction,
    actionName=
        safe_text
)
behaviour::CommunicationAction_strategy = st.builds(
    behaviour::CommunicationAction,
)
Notify_strategy = st.builds(
    Notify,
)
behaviour::MulticastNotify_strategy = st.builds(
    behaviour::MulticastNotify,
)
behaviour::UnicastNotify_strategy = st.builds(
    behaviour::UnicastNotify,
)
behaviour::BroadcastNotify_strategy = st.builds(
    behaviour::BroadcastNotify,
)
CommunicationAction_strategy = st.builds(
    CommunicationAction,
)
behaviour::Notify_strategy = st.builds(
    behaviour::Notify,
)
behaviour::CheckNotification_strategy = st.builds(
    behaviour::CheckNotification,
)
behaviour::Feedback_strategy = st.builds(
    behaviour::Feedback,
    actionName=
        safe_text
)
MoveTransition_strategy = st.builds(
    MoveTransition,
)
behaviour::Choice_strategy = st.builds(
    behaviour::Choice,
    conditionIdentifier=
        safe_text
)
Move_strategy = st.builds(
    Move,
)
behaviour::Stop_strategy = st.builds(
    behaviour::Stop,
)
behaviour::Hover_strategy = st.builds(
    behaviour::Hover,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::HeadTo_strategy = st.builds(
    behaviour::HeadTo,
    direction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::Circle_strategy = st.builds(
    behaviour::Circle,
    radius=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    clockwise=
        st.booleans(),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::Start_strategy = st.builds(
    behaviour::Start,
)
behaviour::MoveTransition_strategy = st.builds(
    behaviour::MoveTransition,
    fluid=
        st.booleans()
)
behaviour::Coordinate_strategy = st.builds(
    behaviour::Coordinate,
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour::GoTo_strategy = st.builds(
    behaviour::GoTo,
    strategy=
        safe_text
)
behaviour::Land_strategy = st.builds(
    behaviour::Land,
)
behaviour::TakeOff_strategy = st.builds(
    behaviour::TakeOff,
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour::Drone_strategy = st.builds(
    behaviour::Drone,
    travelMode=
        safe_text,
    typeName=
        safe_text
)
behaviour::Slot_strategy = st.builds(
    behaviour::Slot,
)
behaviour::Move_strategy = st.builds(
    behaviour::Move,
)
behaviour::Action_strategy = st.builds(
    behaviour::Action,
)
behaviour::Behaviour_strategy = st.builds(
    behaviour::Behaviour,
    crs=
        safe_text
)
behaviour::NamedElement_strategy = st.builds(
    behaviour::NamedElement,
    name=
        safe_text
)

@given(instance=behaviour::Parameter_strategy)
@settings(max_examples=50)
def test_behaviour::parameter_instantiation(instance):
    assert isinstance(instance, behaviour::Parameter)

@given(instance=behaviour::Parameter_strategy)
def test_behaviour::parameter_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=behaviour::Parameter_strategy)
def test_behaviour::parameter_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=behaviour::Parameter_strategy)
def test_behaviour::parameter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=behaviour::Parameter_strategy)
def test_behaviour::parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=behaviour::DeviceAction_strategy)
@settings(max_examples=50)
def test_behaviour::deviceaction_instantiation(instance):
    assert isinstance(instance, behaviour::DeviceAction)

@given(instance=behaviour::DeviceAction_strategy)
def test_behaviour::deviceaction_actionName_type(instance):
    assert isinstance(instance.actionName, str)


@given(instance=behaviour::DeviceAction_strategy)
def test_behaviour::deviceaction_actionName_setter(instance):
    original = instance.actionName
    instance.actionName = original
    assert instance.actionName == original

@given(instance=behaviour::CommunicationAction_strategy)
@settings(max_examples=50)
def test_behaviour::communicationaction_instantiation(instance):
    assert isinstance(instance, behaviour::CommunicationAction)

@given(instance=Notify_strategy)
@settings(max_examples=50)
def test_notify_instantiation(instance):
    assert isinstance(instance, Notify)

@given(instance=behaviour::MulticastNotify_strategy)
@settings(max_examples=50)
def test_behaviour::multicastnotify_instantiation(instance):
    assert isinstance(instance, behaviour::MulticastNotify)

@given(instance=behaviour::UnicastNotify_strategy)
@settings(max_examples=50)
def test_behaviour::unicastnotify_instantiation(instance):
    assert isinstance(instance, behaviour::UnicastNotify)

@given(instance=behaviour::BroadcastNotify_strategy)
@settings(max_examples=50)
def test_behaviour::broadcastnotify_instantiation(instance):
    assert isinstance(instance, behaviour::BroadcastNotify)

@given(instance=CommunicationAction_strategy)
@settings(max_examples=50)
def test_communicationaction_instantiation(instance):
    assert isinstance(instance, CommunicationAction)

@given(instance=behaviour::Notify_strategy)
@settings(max_examples=50)
def test_behaviour::notify_instantiation(instance):
    assert isinstance(instance, behaviour::Notify)

@given(instance=behaviour::CheckNotification_strategy)
@settings(max_examples=50)
def test_behaviour::checknotification_instantiation(instance):
    assert isinstance(instance, behaviour::CheckNotification)

@given(instance=behaviour::Feedback_strategy)
@settings(max_examples=50)
def test_behaviour::feedback_instantiation(instance):
    assert isinstance(instance, behaviour::Feedback)

@given(instance=behaviour::Feedback_strategy)
def test_behaviour::feedback_actionName_type(instance):
    assert isinstance(instance.actionName, str)


@given(instance=behaviour::Feedback_strategy)
def test_behaviour::feedback_actionName_setter(instance):
    original = instance.actionName
    instance.actionName = original
    assert instance.actionName == original

@given(instance=MoveTransition_strategy)
@settings(max_examples=50)
def test_movetransition_instantiation(instance):
    assert isinstance(instance, MoveTransition)

@given(instance=behaviour::Choice_strategy)
@settings(max_examples=50)
def test_behaviour::choice_instantiation(instance):
    assert isinstance(instance, behaviour::Choice)

@given(instance=behaviour::Choice_strategy)
def test_behaviour::choice_conditionIdentifier_type(instance):
    assert isinstance(instance.conditionIdentifier, str)


@given(instance=behaviour::Choice_strategy)
def test_behaviour::choice_conditionIdentifier_setter(instance):
    original = instance.conditionIdentifier
    instance.conditionIdentifier = original
    assert instance.conditionIdentifier == original

@given(instance=Move_strategy)
@settings(max_examples=50)
def test_move_instantiation(instance):
    assert isinstance(instance, Move)

@given(instance=behaviour::Stop_strategy)
@settings(max_examples=50)
def test_behaviour::stop_instantiation(instance):
    assert isinstance(instance, behaviour::Stop)

@given(instance=behaviour::Hover_strategy)
@settings(max_examples=50)
def test_behaviour::hover_instantiation(instance):
    assert isinstance(instance, behaviour::Hover)

@given(instance=behaviour::Hover_strategy)
def test_behaviour::hover_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=behaviour::Hover_strategy)
def test_behaviour::hover_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=behaviour::HeadTo_strategy)
@settings(max_examples=50)
def test_behaviour::headto_instantiation(instance):
    assert isinstance(instance, behaviour::HeadTo)

@given(instance=behaviour::HeadTo_strategy)
def test_behaviour::headto_direction_type(instance):
    assert isinstance(instance.direction, float)


@given(instance=behaviour::HeadTo_strategy)
def test_behaviour::headto_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=behaviour::Circle_strategy)
@settings(max_examples=50)
def test_behaviour::circle_instantiation(instance):
    assert isinstance(instance, behaviour::Circle)

@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_radius_type(instance):
    assert isinstance(instance.radius, float)


@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_clockwise_type(instance):
    assert isinstance(instance.clockwise, bool)


@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_clockwise_setter(instance):
    original = instance.clockwise
    instance.clockwise = original
    assert instance.clockwise == original

@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_altitude_type(instance):
    assert isinstance(instance.altitude, float)


@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=behaviour::Circle_strategy)
def test_behaviour::circle_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=behaviour::Start_strategy)
@settings(max_examples=50)
def test_behaviour::start_instantiation(instance):
    assert isinstance(instance, behaviour::Start)

@given(instance=behaviour::MoveTransition_strategy)
@settings(max_examples=50)
def test_behaviour::movetransition_instantiation(instance):
    assert isinstance(instance, behaviour::MoveTransition)

@given(instance=behaviour::MoveTransition_strategy)
def test_behaviour::movetransition_fluid_type(instance):
    assert isinstance(instance.fluid, bool)


@given(instance=behaviour::MoveTransition_strategy)
def test_behaviour::movetransition_fluid_setter(instance):
    original = instance.fluid
    instance.fluid = original
    assert instance.fluid == original

@given(instance=behaviour::Coordinate_strategy)
@settings(max_examples=50)
def test_behaviour::coordinate_instantiation(instance):
    assert isinstance(instance, behaviour::Coordinate)

@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_heading_type(instance):
    assert isinstance(instance.heading, float)


@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_altitude_type(instance):
    assert isinstance(instance.altitude, float)


@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_latitude_type(instance):
    assert isinstance(instance.latitude, float)


@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original

@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_longitude_type(instance):
    assert isinstance(instance.longitude, float)


@given(instance=behaviour::Coordinate_strategy)
def test_behaviour::coordinate_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original

@given(instance=behaviour::GoTo_strategy)
@settings(max_examples=50)
def test_behaviour::goto_instantiation(instance):
    assert isinstance(instance, behaviour::GoTo)

@given(instance=behaviour::GoTo_strategy)
def test_behaviour::goto_strategy_type(instance):
    assert isinstance(instance.strategy, str)


@given(instance=behaviour::GoTo_strategy)
def test_behaviour::goto_strategy_setter(instance):
    original = instance.strategy
    instance.strategy = original
    assert instance.strategy == original

@given(instance=behaviour::Land_strategy)
@settings(max_examples=50)
def test_behaviour::land_instantiation(instance):
    assert isinstance(instance, behaviour::Land)

@given(instance=behaviour::TakeOff_strategy)
@settings(max_examples=50)
def test_behaviour::takeoff_instantiation(instance):
    assert isinstance(instance, behaviour::TakeOff)

@given(instance=behaviour::TakeOff_strategy)
def test_behaviour::takeoff_altitude_type(instance):
    assert isinstance(instance.altitude, float)


@given(instance=behaviour::TakeOff_strategy)
def test_behaviour::takeoff_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behaviour::Drone_strategy)
@settings(max_examples=50)
def test_behaviour::drone_instantiation(instance):
    assert isinstance(instance, behaviour::Drone)

@given(instance=behaviour::Drone_strategy)
def test_behaviour::drone_travelMode_type(instance):
    assert isinstance(instance.travelMode, str)


@given(instance=behaviour::Drone_strategy)
def test_behaviour::drone_travelMode_setter(instance):
    original = instance.travelMode
    instance.travelMode = original
    assert instance.travelMode == original

@given(instance=behaviour::Drone_strategy)
def test_behaviour::drone_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=behaviour::Drone_strategy)
def test_behaviour::drone_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=behaviour::Slot_strategy)
@settings(max_examples=50)
def test_behaviour::slot_instantiation(instance):
    assert isinstance(instance, behaviour::Slot)

@given(instance=behaviour::Move_strategy)
@settings(max_examples=50)
def test_behaviour::move_instantiation(instance):
    assert isinstance(instance, behaviour::Move)

@given(instance=behaviour::Action_strategy)
@settings(max_examples=50)
def test_behaviour::action_instantiation(instance):
    assert isinstance(instance, behaviour::Action)

@given(instance=behaviour::Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour::behaviour_instantiation(instance):
    assert isinstance(instance, behaviour::Behaviour)

@given(instance=behaviour::Behaviour_strategy)
def test_behaviour::behaviour_crs_type(instance):
    assert isinstance(instance.crs, str)


@given(instance=behaviour::Behaviour_strategy)
def test_behaviour::behaviour_crs_setter(instance):
    original = instance.crs
    instance.crs = original
    assert instance.crs == original

@given(instance=behaviour::NamedElement_strategy)
@settings(max_examples=50)
def test_behaviour::namedelement_instantiation(instance):
    assert isinstance(instance, behaviour::NamedElement)

@given(instance=behaviour::NamedElement_strategy)
def test_behaviour::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behaviour::NamedElement_strategy)
def test_behaviour::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
