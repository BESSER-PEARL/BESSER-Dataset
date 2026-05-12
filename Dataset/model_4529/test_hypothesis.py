import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    behaviour_Parameter,
    Notify,
    behaviour_MulticastNotify,
    behaviour_UnicastNotify,
    behaviour_BroadcastNotify,
    CommunicationAction,
    behaviour_CheckNotification,
    behaviour_Feedback,
    behaviour_Notify,
    Action,
    behaviour_DeviceAction,
    behaviour_CommunicationAction,
    MoveTransition,
    behaviour_Choice,
    NamedElement,
    behaviour_Behaviour,
    behaviour_NamedElement,
    Move,
    behaviour_Circle,
    behaviour_Land,
    behaviour_Stop,
    behaviour_GoTo,
    behaviour_HeadTo,
    behaviour_Hover,
    behaviour_TakeOff,
    behaviour_Start,
    behaviour_Action,
    behaviour_Slot,
    behaviour_MoveTransition,
    behaviour_Move,
    behaviour_Coordinate,
    behaviour_Drone,
    GoToStrategy,
    TravelMode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_behaviour_parameter_is_not_abstract():
    assert not inspect.isabstract(behaviour_Parameter)


def test_behaviour_parameter_constructor_exists():
    assert callable(behaviour_Parameter.__init__)


def test_behaviour_parameter_constructor_args():
    sig = inspect.signature(behaviour_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_behaviour_parameter_has_key():
    assert hasattr(behaviour_Parameter, "key")
    descriptor = None
    for klass in behaviour_Parameter.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_parameter_has_value():
    assert hasattr(behaviour_Parameter, "value")
    descriptor = None
    for klass in behaviour_Parameter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_notify_is_not_abstract():
    assert not inspect.isabstract(Notify)


def test_notify_constructor_exists():
    assert callable(Notify.__init__)


def test_notify_constructor_args():
    sig = inspect.signature(Notify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_multicastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour_MulticastNotify)


def test_behaviour_multicastnotify_constructor_exists():
    assert callable(behaviour_MulticastNotify.__init__)


def test_behaviour_multicastnotify_constructor_args():
    sig = inspect.signature(behaviour_MulticastNotify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_unicastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour_UnicastNotify)


def test_behaviour_unicastnotify_constructor_exists():
    assert callable(behaviour_UnicastNotify.__init__)


def test_behaviour_unicastnotify_constructor_args():
    sig = inspect.signature(behaviour_UnicastNotify.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_broadcastnotify_is_not_abstract():
    assert not inspect.isabstract(behaviour_BroadcastNotify)


def test_behaviour_broadcastnotify_constructor_exists():
    assert callable(behaviour_BroadcastNotify.__init__)


def test_behaviour_broadcastnotify_constructor_args():
    sig = inspect.signature(behaviour_BroadcastNotify.__init__)
    params = list(sig.parameters.keys())



def test_communicationaction_is_not_abstract():
    assert not inspect.isabstract(CommunicationAction)


def test_communicationaction_constructor_exists():
    assert callable(CommunicationAction.__init__)


def test_communicationaction_constructor_args():
    sig = inspect.signature(CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_checknotification_is_not_abstract():
    assert not inspect.isabstract(behaviour_CheckNotification)


def test_behaviour_checknotification_constructor_exists():
    assert callable(behaviour_CheckNotification.__init__)


def test_behaviour_checknotification_constructor_args():
    sig = inspect.signature(behaviour_CheckNotification.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_feedback_is_not_abstract():
    assert not inspect.isabstract(behaviour_Feedback)


def test_behaviour_feedback_constructor_exists():
    assert callable(behaviour_Feedback.__init__)


def test_behaviour_feedback_constructor_args():
    sig = inspect.signature(behaviour_Feedback.__init__)
    params = list(sig.parameters.keys())
    assert "actionName" in params, "Missing parameter 'actionName'"

def test_behaviour_feedback_has_actionName():
    assert hasattr(behaviour_Feedback, "actionName")
    descriptor = None
    for klass in behaviour_Feedback.__mro__:
        if "actionName" in klass.__dict__:
            descriptor = klass.__dict__["actionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_notify_is_not_abstract():
    assert not inspect.isabstract(behaviour_Notify)


def test_behaviour_notify_constructor_exists():
    assert callable(behaviour_Notify.__init__)


def test_behaviour_notify_constructor_args():
    sig = inspect.signature(behaviour_Notify.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_deviceaction_is_not_abstract():
    assert not inspect.isabstract(behaviour_DeviceAction)


def test_behaviour_deviceaction_constructor_exists():
    assert callable(behaviour_DeviceAction.__init__)


def test_behaviour_deviceaction_constructor_args():
    sig = inspect.signature(behaviour_DeviceAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionName" in params, "Missing parameter 'actionName'"

def test_behaviour_deviceaction_has_actionName():
    assert hasattr(behaviour_DeviceAction, "actionName")
    descriptor = None
    for klass in behaviour_DeviceAction.__mro__:
        if "actionName" in klass.__dict__:
            descriptor = klass.__dict__["actionName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_communicationaction_is_not_abstract():
    assert not inspect.isabstract(behaviour_CommunicationAction)


def test_behaviour_communicationaction_constructor_exists():
    assert callable(behaviour_CommunicationAction.__init__)


def test_behaviour_communicationaction_constructor_args():
    sig = inspect.signature(behaviour_CommunicationAction.__init__)
    params = list(sig.parameters.keys())



def test_movetransition_is_not_abstract():
    assert not inspect.isabstract(MoveTransition)


def test_movetransition_constructor_exists():
    assert callable(MoveTransition.__init__)


def test_movetransition_constructor_args():
    sig = inspect.signature(MoveTransition.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_choice_is_not_abstract():
    assert not inspect.isabstract(behaviour_Choice)


def test_behaviour_choice_constructor_exists():
    assert callable(behaviour_Choice.__init__)


def test_behaviour_choice_constructor_args():
    sig = inspect.signature(behaviour_Choice.__init__)
    params = list(sig.parameters.keys())
    assert "conditionIdentifier" in params, "Missing parameter 'conditionIdentifier'"

def test_behaviour_choice_has_conditionIdentifier():
    assert hasattr(behaviour_Choice, "conditionIdentifier")
    descriptor = None
    for klass in behaviour_Choice.__mro__:
        if "conditionIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["conditionIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour_Behaviour)


def test_behaviour_behaviour_constructor_exists():
    assert callable(behaviour_Behaviour.__init__)


def test_behaviour_behaviour_constructor_args():
    sig = inspect.signature(behaviour_Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "crs" in params, "Missing parameter 'crs'"

def test_behaviour_behaviour_has_crs():
    assert hasattr(behaviour_Behaviour, "crs")
    descriptor = None
    for klass in behaviour_Behaviour.__mro__:
        if "crs" in klass.__dict__:
            descriptor = klass.__dict__["crs"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_namedelement_is_not_abstract():
    assert not inspect.isabstract(behaviour_NamedElement)


def test_behaviour_namedelement_constructor_exists():
    assert callable(behaviour_NamedElement.__init__)


def test_behaviour_namedelement_constructor_args():
    sig = inspect.signature(behaviour_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour_namedelement_has_name():
    assert hasattr(behaviour_NamedElement, "name")
    descriptor = None
    for klass in behaviour_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_move_is_not_abstract():
    assert not inspect.isabstract(Move)


def test_move_constructor_exists():
    assert callable(Move.__init__)


def test_move_constructor_args():
    sig = inspect.signature(Move.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_circle_is_not_abstract():
    assert not inspect.isabstract(behaviour_Circle)


def test_behaviour_circle_constructor_exists():
    assert callable(behaviour_Circle.__init__)


def test_behaviour_circle_constructor_args():
    sig = inspect.signature(behaviour_Circle.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"
    assert "clockwise" in params, "Missing parameter 'clockwise'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "altitude" in params, "Missing parameter 'altitude'"

def test_behaviour_circle_has_duration():
    assert hasattr(behaviour_Circle, "duration")
    descriptor = None
    for klass in behaviour_Circle.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_circle_has_clockwise():
    assert hasattr(behaviour_Circle, "clockwise")
    descriptor = None
    for klass in behaviour_Circle.__mro__:
        if "clockwise" in klass.__dict__:
            descriptor = klass.__dict__["clockwise"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_circle_has_radius():
    assert hasattr(behaviour_Circle, "radius")
    descriptor = None
    for klass in behaviour_Circle.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_circle_has_altitude():
    assert hasattr(behaviour_Circle, "altitude")
    descriptor = None
    for klass in behaviour_Circle.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_land_is_not_abstract():
    assert not inspect.isabstract(behaviour_Land)


def test_behaviour_land_constructor_exists():
    assert callable(behaviour_Land.__init__)


def test_behaviour_land_constructor_args():
    sig = inspect.signature(behaviour_Land.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_stop_is_not_abstract():
    assert not inspect.isabstract(behaviour_Stop)


def test_behaviour_stop_constructor_exists():
    assert callable(behaviour_Stop.__init__)


def test_behaviour_stop_constructor_args():
    sig = inspect.signature(behaviour_Stop.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_goto_is_not_abstract():
    assert not inspect.isabstract(behaviour_GoTo)


def test_behaviour_goto_constructor_exists():
    assert callable(behaviour_GoTo.__init__)


def test_behaviour_goto_constructor_args():
    sig = inspect.signature(behaviour_GoTo.__init__)
    params = list(sig.parameters.keys())
    assert "strategy" in params, "Missing parameter 'strategy'"

def test_behaviour_goto_has_strategy():
    assert hasattr(behaviour_GoTo, "strategy")
    descriptor = None
    for klass in behaviour_GoTo.__mro__:
        if "strategy" in klass.__dict__:
            descriptor = klass.__dict__["strategy"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_headto_is_not_abstract():
    assert not inspect.isabstract(behaviour_HeadTo)


def test_behaviour_headto_constructor_exists():
    assert callable(behaviour_HeadTo.__init__)


def test_behaviour_headto_constructor_args():
    sig = inspect.signature(behaviour_HeadTo.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_behaviour_headto_has_direction():
    assert hasattr(behaviour_HeadTo, "direction")
    descriptor = None
    for klass in behaviour_HeadTo.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_hover_is_not_abstract():
    assert not inspect.isabstract(behaviour_Hover)


def test_behaviour_hover_constructor_exists():
    assert callable(behaviour_Hover.__init__)


def test_behaviour_hover_constructor_args():
    sig = inspect.signature(behaviour_Hover.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_behaviour_hover_has_duration():
    assert hasattr(behaviour_Hover, "duration")
    descriptor = None
    for klass in behaviour_Hover.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_takeoff_is_not_abstract():
    assert not inspect.isabstract(behaviour_TakeOff)


def test_behaviour_takeoff_constructor_exists():
    assert callable(behaviour_TakeOff.__init__)


def test_behaviour_takeoff_constructor_args():
    sig = inspect.signature(behaviour_TakeOff.__init__)
    params = list(sig.parameters.keys())
    assert "altitude" in params, "Missing parameter 'altitude'"

def test_behaviour_takeoff_has_altitude():
    assert hasattr(behaviour_TakeOff, "altitude")
    descriptor = None
    for klass in behaviour_TakeOff.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_start_is_not_abstract():
    assert not inspect.isabstract(behaviour_Start)


def test_behaviour_start_constructor_exists():
    assert callable(behaviour_Start.__init__)


def test_behaviour_start_constructor_args():
    sig = inspect.signature(behaviour_Start.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_action_is_not_abstract():
    assert not inspect.isabstract(behaviour_Action)


def test_behaviour_action_constructor_exists():
    assert callable(behaviour_Action.__init__)


def test_behaviour_action_constructor_args():
    sig = inspect.signature(behaviour_Action.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_slot_is_not_abstract():
    assert not inspect.isabstract(behaviour_Slot)


def test_behaviour_slot_constructor_exists():
    assert callable(behaviour_Slot.__init__)


def test_behaviour_slot_constructor_args():
    sig = inspect.signature(behaviour_Slot.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_movetransition_is_not_abstract():
    assert not inspect.isabstract(behaviour_MoveTransition)


def test_behaviour_movetransition_constructor_exists():
    assert callable(behaviour_MoveTransition.__init__)


def test_behaviour_movetransition_constructor_args():
    sig = inspect.signature(behaviour_MoveTransition.__init__)
    params = list(sig.parameters.keys())
    assert "fluid" in params, "Missing parameter 'fluid'"

def test_behaviour_movetransition_has_fluid():
    assert hasattr(behaviour_MoveTransition, "fluid")
    descriptor = None
    for klass in behaviour_MoveTransition.__mro__:
        if "fluid" in klass.__dict__:
            descriptor = klass.__dict__["fluid"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_move_is_not_abstract():
    assert not inspect.isabstract(behaviour_Move)


def test_behaviour_move_constructor_exists():
    assert callable(behaviour_Move.__init__)


def test_behaviour_move_constructor_args():
    sig = inspect.signature(behaviour_Move.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_coordinate_is_not_abstract():
    assert not inspect.isabstract(behaviour_Coordinate)


def test_behaviour_coordinate_constructor_exists():
    assert callable(behaviour_Coordinate.__init__)


def test_behaviour_coordinate_constructor_args():
    sig = inspect.signature(behaviour_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "longitude" in params, "Missing parameter 'longitude'"
    assert "altitude" in params, "Missing parameter 'altitude'"
    assert "latitude" in params, "Missing parameter 'latitude'"
    assert "heading" in params, "Missing parameter 'heading'"

def test_behaviour_coordinate_has_longitude():
    assert hasattr(behaviour_Coordinate, "longitude")
    descriptor = None
    for klass in behaviour_Coordinate.__mro__:
        if "longitude" in klass.__dict__:
            descriptor = klass.__dict__["longitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_coordinate_has_altitude():
    assert hasattr(behaviour_Coordinate, "altitude")
    descriptor = None
    for klass in behaviour_Coordinate.__mro__:
        if "altitude" in klass.__dict__:
            descriptor = klass.__dict__["altitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_coordinate_has_latitude():
    assert hasattr(behaviour_Coordinate, "latitude")
    descriptor = None
    for klass in behaviour_Coordinate.__mro__:
        if "latitude" in klass.__dict__:
            descriptor = klass.__dict__["latitude"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_coordinate_has_heading():
    assert hasattr(behaviour_Coordinate, "heading")
    descriptor = None
    for klass in behaviour_Coordinate.__mro__:
        if "heading" in klass.__dict__:
            descriptor = klass.__dict__["heading"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_drone_is_not_abstract():
    assert not inspect.isabstract(behaviour_Drone)


def test_behaviour_drone_constructor_exists():
    assert callable(behaviour_Drone.__init__)


def test_behaviour_drone_constructor_args():
    sig = inspect.signature(behaviour_Drone.__init__)
    params = list(sig.parameters.keys())
    assert "travelMode" in params, "Missing parameter 'travelMode'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_behaviour_drone_has_travelMode():
    assert hasattr(behaviour_Drone, "travelMode")
    descriptor = None
    for klass in behaviour_Drone.__mro__:
        if "travelMode" in klass.__dict__:
            descriptor = klass.__dict__["travelMode"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_drone_has_typeName():
    assert hasattr(behaviour_Drone, "typeName")
    descriptor = None
    for klass in behaviour_Drone.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
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
behaviour_Parameter_strategy = st.builds(
    behaviour_Parameter,
    key=
        safe_text,
    value=
        safe_text
)
Notify_strategy = st.builds(
    Notify,
)
behaviour_MulticastNotify_strategy = st.builds(
    behaviour_MulticastNotify,
)
behaviour_UnicastNotify_strategy = st.builds(
    behaviour_UnicastNotify,
)
behaviour_BroadcastNotify_strategy = st.builds(
    behaviour_BroadcastNotify,
)
CommunicationAction_strategy = st.builds(
    CommunicationAction,
)
behaviour_CheckNotification_strategy = st.builds(
    behaviour_CheckNotification,
)
behaviour_Feedback_strategy = st.builds(
    behaviour_Feedback,
    actionName=
        safe_text
)
behaviour_Notify_strategy = st.builds(
    behaviour_Notify,
)
Action_strategy = st.builds(
    Action,
)
behaviour_DeviceAction_strategy = st.builds(
    behaviour_DeviceAction,
    actionName=
        safe_text
)
behaviour_CommunicationAction_strategy = st.builds(
    behaviour_CommunicationAction,
)
MoveTransition_strategy = st.builds(
    MoveTransition,
)
behaviour_Choice_strategy = st.builds(
    behaviour_Choice,
    conditionIdentifier=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behaviour_Behaviour_strategy = st.builds(
    behaviour_Behaviour,
    crs=
        safe_text
)
behaviour_NamedElement_strategy = st.builds(
    behaviour_NamedElement,
    name=
        safe_text
)
Move_strategy = st.builds(
    Move,
)
behaviour_Circle_strategy = st.builds(
    behaviour_Circle,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    clockwise=
        st.booleans(),
    radius=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_Land_strategy = st.builds(
    behaviour_Land,
)
behaviour_Stop_strategy = st.builds(
    behaviour_Stop,
)
behaviour_GoTo_strategy = st.builds(
    behaviour_GoTo,
    strategy=
        safe_text
)
behaviour_HeadTo_strategy = st.builds(
    behaviour_HeadTo,
    direction=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_Hover_strategy = st.builds(
    behaviour_Hover,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_TakeOff_strategy = st.builds(
    behaviour_TakeOff,
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_Start_strategy = st.builds(
    behaviour_Start,
)
behaviour_Action_strategy = st.builds(
    behaviour_Action,
)
behaviour_Slot_strategy = st.builds(
    behaviour_Slot,
)
behaviour_MoveTransition_strategy = st.builds(
    behaviour_MoveTransition,
    fluid=
        st.booleans()
)
behaviour_Move_strategy = st.builds(
    behaviour_Move,
)
behaviour_Coordinate_strategy = st.builds(
    behaviour_Coordinate,
    longitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    altitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    latitude=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    heading=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
behaviour_Drone_strategy = st.builds(
    behaviour_Drone,
    travelMode=
        safe_text,
    typeName=
        safe_text
)

@given(instance=behaviour_Parameter_strategy)
@settings(max_examples=50)
def test_behaviour_parameter_instantiation(instance):
    assert isinstance(instance, behaviour_Parameter)



@given(instance=behaviour_Parameter_strategy)
def test_behaviour_parameter_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=behaviour_Parameter_strategy)
def test_behaviour_parameter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Notify_strategy)
@settings(max_examples=50)
def test_notify_instantiation(instance):
    assert isinstance(instance, Notify)

@given(instance=behaviour_MulticastNotify_strategy)
@settings(max_examples=50)
def test_behaviour_multicastnotify_instantiation(instance):
    assert isinstance(instance, behaviour_MulticastNotify)

@given(instance=behaviour_UnicastNotify_strategy)
@settings(max_examples=50)
def test_behaviour_unicastnotify_instantiation(instance):
    assert isinstance(instance, behaviour_UnicastNotify)

@given(instance=behaviour_BroadcastNotify_strategy)
@settings(max_examples=50)
def test_behaviour_broadcastnotify_instantiation(instance):
    assert isinstance(instance, behaviour_BroadcastNotify)

@given(instance=CommunicationAction_strategy)
@settings(max_examples=50)
def test_communicationaction_instantiation(instance):
    assert isinstance(instance, CommunicationAction)

@given(instance=behaviour_CheckNotification_strategy)
@settings(max_examples=50)
def test_behaviour_checknotification_instantiation(instance):
    assert isinstance(instance, behaviour_CheckNotification)

@given(instance=behaviour_Feedback_strategy)
@settings(max_examples=50)
def test_behaviour_feedback_instantiation(instance):
    assert isinstance(instance, behaviour_Feedback)



@given(instance=behaviour_Feedback_strategy)
def test_behaviour_feedback_actionName_setter(instance):
    original = instance.actionName
    instance.actionName = original
    assert instance.actionName == original

@given(instance=behaviour_Notify_strategy)
@settings(max_examples=50)
def test_behaviour_notify_instantiation(instance):
    assert isinstance(instance, behaviour_Notify)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=behaviour_DeviceAction_strategy)
@settings(max_examples=50)
def test_behaviour_deviceaction_instantiation(instance):
    assert isinstance(instance, behaviour_DeviceAction)



@given(instance=behaviour_DeviceAction_strategy)
def test_behaviour_deviceaction_actionName_setter(instance):
    original = instance.actionName
    instance.actionName = original
    assert instance.actionName == original

@given(instance=behaviour_CommunicationAction_strategy)
@settings(max_examples=50)
def test_behaviour_communicationaction_instantiation(instance):
    assert isinstance(instance, behaviour_CommunicationAction)

@given(instance=MoveTransition_strategy)
@settings(max_examples=50)
def test_movetransition_instantiation(instance):
    assert isinstance(instance, MoveTransition)

@given(instance=behaviour_Choice_strategy)
@settings(max_examples=50)
def test_behaviour_choice_instantiation(instance):
    assert isinstance(instance, behaviour_Choice)



@given(instance=behaviour_Choice_strategy)
def test_behaviour_choice_conditionIdentifier_setter(instance):
    original = instance.conditionIdentifier
    instance.conditionIdentifier = original
    assert instance.conditionIdentifier == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behaviour_Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_behaviour_instantiation(instance):
    assert isinstance(instance, behaviour_Behaviour)



@given(instance=behaviour_Behaviour_strategy)
def test_behaviour_behaviour_crs_setter(instance):
    original = instance.crs
    instance.crs = original
    assert instance.crs == original

@given(instance=behaviour_NamedElement_strategy)
@settings(max_examples=50)
def test_behaviour_namedelement_instantiation(instance):
    assert isinstance(instance, behaviour_NamedElement)



@given(instance=behaviour_NamedElement_strategy)
def test_behaviour_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Move_strategy)
@settings(max_examples=50)
def test_move_instantiation(instance):
    assert isinstance(instance, Move)

@given(instance=behaviour_Circle_strategy)
@settings(max_examples=50)
def test_behaviour_circle_instantiation(instance):
    assert isinstance(instance, behaviour_Circle)



@given(instance=behaviour_Circle_strategy)
def test_behaviour_circle_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original



@given(instance=behaviour_Circle_strategy)
def test_behaviour_circle_clockwise_setter(instance):
    original = instance.clockwise
    instance.clockwise = original
    assert instance.clockwise == original



@given(instance=behaviour_Circle_strategy)
def test_behaviour_circle_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original



@given(instance=behaviour_Circle_strategy)
def test_behaviour_circle_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=behaviour_Land_strategy)
@settings(max_examples=50)
def test_behaviour_land_instantiation(instance):
    assert isinstance(instance, behaviour_Land)

@given(instance=behaviour_Stop_strategy)
@settings(max_examples=50)
def test_behaviour_stop_instantiation(instance):
    assert isinstance(instance, behaviour_Stop)

@given(instance=behaviour_GoTo_strategy)
@settings(max_examples=50)
def test_behaviour_goto_instantiation(instance):
    assert isinstance(instance, behaviour_GoTo)



@given(instance=behaviour_GoTo_strategy)
def test_behaviour_goto_strategy_setter(instance):
    original = instance.strategy
    instance.strategy = original
    assert instance.strategy == original

@given(instance=behaviour_HeadTo_strategy)
@settings(max_examples=50)
def test_behaviour_headto_instantiation(instance):
    assert isinstance(instance, behaviour_HeadTo)



@given(instance=behaviour_HeadTo_strategy)
def test_behaviour_headto_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=behaviour_Hover_strategy)
@settings(max_examples=50)
def test_behaviour_hover_instantiation(instance):
    assert isinstance(instance, behaviour_Hover)



@given(instance=behaviour_Hover_strategy)
def test_behaviour_hover_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=behaviour_TakeOff_strategy)
@settings(max_examples=50)
def test_behaviour_takeoff_instantiation(instance):
    assert isinstance(instance, behaviour_TakeOff)



@given(instance=behaviour_TakeOff_strategy)
def test_behaviour_takeoff_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original

@given(instance=behaviour_Start_strategy)
@settings(max_examples=50)
def test_behaviour_start_instantiation(instance):
    assert isinstance(instance, behaviour_Start)

@given(instance=behaviour_Action_strategy)
@settings(max_examples=50)
def test_behaviour_action_instantiation(instance):
    assert isinstance(instance, behaviour_Action)

@given(instance=behaviour_Slot_strategy)
@settings(max_examples=50)
def test_behaviour_slot_instantiation(instance):
    assert isinstance(instance, behaviour_Slot)

@given(instance=behaviour_MoveTransition_strategy)
@settings(max_examples=50)
def test_behaviour_movetransition_instantiation(instance):
    assert isinstance(instance, behaviour_MoveTransition)



@given(instance=behaviour_MoveTransition_strategy)
def test_behaviour_movetransition_fluid_setter(instance):
    original = instance.fluid
    instance.fluid = original
    assert instance.fluid == original

@given(instance=behaviour_Move_strategy)
@settings(max_examples=50)
def test_behaviour_move_instantiation(instance):
    assert isinstance(instance, behaviour_Move)

@given(instance=behaviour_Coordinate_strategy)
@settings(max_examples=50)
def test_behaviour_coordinate_instantiation(instance):
    assert isinstance(instance, behaviour_Coordinate)



@given(instance=behaviour_Coordinate_strategy)
def test_behaviour_coordinate_longitude_setter(instance):
    original = instance.longitude
    instance.longitude = original
    assert instance.longitude == original



@given(instance=behaviour_Coordinate_strategy)
def test_behaviour_coordinate_altitude_setter(instance):
    original = instance.altitude
    instance.altitude = original
    assert instance.altitude == original



@given(instance=behaviour_Coordinate_strategy)
def test_behaviour_coordinate_latitude_setter(instance):
    original = instance.latitude
    instance.latitude = original
    assert instance.latitude == original



@given(instance=behaviour_Coordinate_strategy)
def test_behaviour_coordinate_heading_setter(instance):
    original = instance.heading
    instance.heading = original
    assert instance.heading == original

@given(instance=behaviour_Drone_strategy)
@settings(max_examples=50)
def test_behaviour_drone_instantiation(instance):
    assert isinstance(instance, behaviour_Drone)



@given(instance=behaviour_Drone_strategy)
def test_behaviour_drone_travelMode_setter(instance):
    original = instance.travelMode
    instance.travelMode = original
    assert instance.travelMode == original



@given(instance=behaviour_Drone_strategy)
def test_behaviour_drone_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original
