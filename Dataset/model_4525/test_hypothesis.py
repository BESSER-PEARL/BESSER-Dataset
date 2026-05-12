import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Event,
    model_Tapped,
    model_Obstacle,
    RandomAction,
    ContinuosAction,
    model_Stop,
    RotorAction,
    model_Turn,
    model_Move,
    Action,
    model_ContinuosAction,
    model_RandomAction,
    model_RotorAction,
    model_Ending,
    model_Action,
    model_ActionsList,
    model_Event,
    ActionsList,
    model_EventListener,
    model_Main,
    model_RoboProse,
    model_Root,
    Ending,
    model_StartOver,
    model_Wait,
    model_Repeat,
    TURN_DIRECTION,
    MOVE_DIRECTION,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_model_tapped_is_not_abstract():
    assert not inspect.isabstract(model_Tapped)


def test_model_tapped_constructor_exists():
    assert callable(model_Tapped.__init__)


def test_model_tapped_constructor_args():
    sig = inspect.signature(model_Tapped.__init__)
    params = list(sig.parameters.keys())



def test_model_obstacle_is_not_abstract():
    assert not inspect.isabstract(model_Obstacle)


def test_model_obstacle_constructor_exists():
    assert callable(model_Obstacle.__init__)


def test_model_obstacle_constructor_args():
    sig = inspect.signature(model_Obstacle.__init__)
    params = list(sig.parameters.keys())



def test_randomaction_is_not_abstract():
    assert not inspect.isabstract(RandomAction)


def test_randomaction_constructor_exists():
    assert callable(RandomAction.__init__)


def test_randomaction_constructor_args():
    sig = inspect.signature(RandomAction.__init__)
    params = list(sig.parameters.keys())



def test_continuosaction_is_not_abstract():
    assert not inspect.isabstract(ContinuosAction)


def test_continuosaction_constructor_exists():
    assert callable(ContinuosAction.__init__)


def test_continuosaction_constructor_args():
    sig = inspect.signature(ContinuosAction.__init__)
    params = list(sig.parameters.keys())



def test_model_stop_is_not_abstract():
    assert not inspect.isabstract(model_Stop)


def test_model_stop_constructor_exists():
    assert callable(model_Stop.__init__)


def test_model_stop_constructor_args():
    sig = inspect.signature(model_Stop.__init__)
    params = list(sig.parameters.keys())



def test_rotoraction_is_not_abstract():
    assert not inspect.isabstract(RotorAction)


def test_rotoraction_constructor_exists():
    assert callable(RotorAction.__init__)


def test_rotoraction_constructor_args():
    sig = inspect.signature(RotorAction.__init__)
    params = list(sig.parameters.keys())



def test_model_turn_is_not_abstract():
    assert not inspect.isabstract(model_Turn)


def test_model_turn_constructor_exists():
    assert callable(model_Turn.__init__)


def test_model_turn_constructor_args():
    sig = inspect.signature(model_Turn.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_model_turn_has_direction():
    assert hasattr(model_Turn, "direction")
    descriptor = None
    for klass in model_Turn.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model_turn_has_degrees():
    assert hasattr(model_Turn, "degrees")
    descriptor = None
    for klass in model_Turn.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_model_move_is_not_abstract():
    assert not inspect.isabstract(model_Move)


def test_model_move_constructor_exists():
    assert callable(model_Move.__init__)


def test_model_move_constructor_args():
    sig = inspect.signature(model_Move.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_model_move_has_direction():
    assert hasattr(model_Move, "direction")
    descriptor = None
    for klass in model_Move.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_model_continuosaction_is_not_abstract():
    assert not inspect.isabstract(model_ContinuosAction)


def test_model_continuosaction_constructor_exists():
    assert callable(model_ContinuosAction.__init__)


def test_model_continuosaction_constructor_args():
    sig = inspect.signature(model_ContinuosAction.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_model_continuosaction_has_duration():
    assert hasattr(model_ContinuosAction, "duration")
    descriptor = None
    for klass in model_ContinuosAction.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_model_randomaction_is_not_abstract():
    assert not inspect.isabstract(model_RandomAction)


def test_model_randomaction_constructor_exists():
    assert callable(model_RandomAction.__init__)


def test_model_randomaction_constructor_args():
    sig = inspect.signature(model_RandomAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRandom" in params, "Missing parameter 'isRandom'"

def test_model_randomaction_has_isRandom():
    assert hasattr(model_RandomAction, "isRandom")
    descriptor = None
    for klass in model_RandomAction.__mro__:
        if "isRandom" in klass.__dict__:
            descriptor = klass.__dict__["isRandom"]
            break
    assert isinstance(descriptor, property)



def test_model_rotoraction_is_not_abstract():
    assert not inspect.isabstract(model_RotorAction)


def test_model_rotoraction_constructor_exists():
    assert callable(model_RotorAction.__init__)


def test_model_rotoraction_constructor_args():
    sig = inspect.signature(model_RotorAction.__init__)
    params = list(sig.parameters.keys())



def test_model_ending_is_not_abstract():
    assert not inspect.isabstract(model_Ending)


def test_model_ending_constructor_exists():
    assert callable(model_Ending.__init__)


def test_model_ending_constructor_args():
    sig = inspect.signature(model_Ending.__init__)
    params = list(sig.parameters.keys())



def test_model_action_is_not_abstract():
    assert not inspect.isabstract(model_Action)


def test_model_action_constructor_exists():
    assert callable(model_Action.__init__)


def test_model_action_constructor_args():
    sig = inspect.signature(model_Action.__init__)
    params = list(sig.parameters.keys())



def test_model_actionslist_is_not_abstract():
    assert not inspect.isabstract(model_ActionsList)


def test_model_actionslist_constructor_exists():
    assert callable(model_ActionsList.__init__)


def test_model_actionslist_constructor_args():
    sig = inspect.signature(model_ActionsList.__init__)
    params = list(sig.parameters.keys())



def test_model_event_is_not_abstract():
    assert not inspect.isabstract(model_Event)


def test_model_event_constructor_exists():
    assert callable(model_Event.__init__)


def test_model_event_constructor_args():
    sig = inspect.signature(model_Event.__init__)
    params = list(sig.parameters.keys())



def test_actionslist_is_not_abstract():
    assert not inspect.isabstract(ActionsList)


def test_actionslist_constructor_exists():
    assert callable(ActionsList.__init__)


def test_actionslist_constructor_args():
    sig = inspect.signature(ActionsList.__init__)
    params = list(sig.parameters.keys())



def test_model_eventlistener_is_not_abstract():
    assert not inspect.isabstract(model_EventListener)


def test_model_eventlistener_constructor_exists():
    assert callable(model_EventListener.__init__)


def test_model_eventlistener_constructor_args():
    sig = inspect.signature(model_EventListener.__init__)
    params = list(sig.parameters.keys())



def test_model_main_is_not_abstract():
    assert not inspect.isabstract(model_Main)


def test_model_main_constructor_exists():
    assert callable(model_Main.__init__)


def test_model_main_constructor_args():
    sig = inspect.signature(model_Main.__init__)
    params = list(sig.parameters.keys())



def test_model_roboprose_is_not_abstract():
    assert not inspect.isabstract(model_RoboProse)


def test_model_roboprose_constructor_exists():
    assert callable(model_RoboProse.__init__)


def test_model_roboprose_constructor_args():
    sig = inspect.signature(model_RoboProse.__init__)
    params = list(sig.parameters.keys())



def test_model_root_is_not_abstract():
    assert not inspect.isabstract(model_Root)


def test_model_root_constructor_exists():
    assert callable(model_Root.__init__)


def test_model_root_constructor_args():
    sig = inspect.signature(model_Root.__init__)
    params = list(sig.parameters.keys())



def test_ending_is_not_abstract():
    assert not inspect.isabstract(Ending)


def test_ending_constructor_exists():
    assert callable(Ending.__init__)


def test_ending_constructor_args():
    sig = inspect.signature(Ending.__init__)
    params = list(sig.parameters.keys())



def test_model_startover_is_not_abstract():
    assert not inspect.isabstract(model_StartOver)


def test_model_startover_constructor_exists():
    assert callable(model_StartOver.__init__)


def test_model_startover_constructor_args():
    sig = inspect.signature(model_StartOver.__init__)
    params = list(sig.parameters.keys())



def test_model_wait_is_not_abstract():
    assert not inspect.isabstract(model_Wait)


def test_model_wait_constructor_exists():
    assert callable(model_Wait.__init__)


def test_model_wait_constructor_args():
    sig = inspect.signature(model_Wait.__init__)
    params = list(sig.parameters.keys())



def test_model_repeat_is_not_abstract():
    assert not inspect.isabstract(model_Repeat)


def test_model_repeat_constructor_exists():
    assert callable(model_Repeat.__init__)


def test_model_repeat_constructor_args():
    sig = inspect.signature(model_Repeat.__init__)
    params = list(sig.parameters.keys())

def test_turn_direction_exists():
    # Check that the Enumeration exists
    assert TURN_DIRECTION is not None

def test_turn_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TURN_DIRECTION]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TURN_DIRECTION"

def test_move_direction_exists():
    # Check that the Enumeration exists
    assert MOVE_DIRECTION is not None

def test_move_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MOVE_DIRECTION]
    expected_literals = [
        "FORWARDS",
        "BACKWARDS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MOVE_DIRECTION"


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
Event_strategy = st.builds(
    Event,
)
model_Tapped_strategy = st.builds(
    model_Tapped,
)
model_Obstacle_strategy = st.builds(
    model_Obstacle,
)
RandomAction_strategy = st.builds(
    RandomAction,
)
ContinuosAction_strategy = st.builds(
    ContinuosAction,
)
model_Stop_strategy = st.builds(
    model_Stop,
)
RotorAction_strategy = st.builds(
    RotorAction,
)
model_Turn_strategy = st.builds(
    model_Turn,
    direction=
        safe_text,
    degrees=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_Move_strategy = st.builds(
    model_Move,
    direction=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
model_ContinuosAction_strategy = st.builds(
    model_ContinuosAction,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model_RandomAction_strategy = st.builds(
    model_RandomAction,
    isRandom=
        st.booleans()
)
model_RotorAction_strategy = st.builds(
    model_RotorAction,
)
model_Ending_strategy = st.builds(
    model_Ending,
)
model_Action_strategy = st.builds(
    model_Action,
)
model_ActionsList_strategy = st.builds(
    model_ActionsList,
)
model_Event_strategy = st.builds(
    model_Event,
)
ActionsList_strategy = st.builds(
    ActionsList,
)
model_EventListener_strategy = st.builds(
    model_EventListener,
)
model_Main_strategy = st.builds(
    model_Main,
)
model_RoboProse_strategy = st.builds(
    model_RoboProse,
)
model_Root_strategy = st.builds(
    model_Root,
)
Ending_strategy = st.builds(
    Ending,
)
model_StartOver_strategy = st.builds(
    model_StartOver,
)
model_Wait_strategy = st.builds(
    model_Wait,
)
model_Repeat_strategy = st.builds(
    model_Repeat,
)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=model_Tapped_strategy)
@settings(max_examples=50)
def test_model_tapped_instantiation(instance):
    assert isinstance(instance, model_Tapped)

@given(instance=model_Obstacle_strategy)
@settings(max_examples=50)
def test_model_obstacle_instantiation(instance):
    assert isinstance(instance, model_Obstacle)

@given(instance=RandomAction_strategy)
@settings(max_examples=50)
def test_randomaction_instantiation(instance):
    assert isinstance(instance, RandomAction)

@given(instance=ContinuosAction_strategy)
@settings(max_examples=50)
def test_continuosaction_instantiation(instance):
    assert isinstance(instance, ContinuosAction)

@given(instance=model_Stop_strategy)
@settings(max_examples=50)
def test_model_stop_instantiation(instance):
    assert isinstance(instance, model_Stop)

@given(instance=RotorAction_strategy)
@settings(max_examples=50)
def test_rotoraction_instantiation(instance):
    assert isinstance(instance, RotorAction)

@given(instance=model_Turn_strategy)
@settings(max_examples=50)
def test_model_turn_instantiation(instance):
    assert isinstance(instance, model_Turn)



@given(instance=model_Turn_strategy)
def test_model_turn_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=model_Turn_strategy)
def test_model_turn_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=model_Move_strategy)
@settings(max_examples=50)
def test_model_move_instantiation(instance):
    assert isinstance(instance, model_Move)



@given(instance=model_Move_strategy)
def test_model_move_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model_ContinuosAction_strategy)
@settings(max_examples=50)
def test_model_continuosaction_instantiation(instance):
    assert isinstance(instance, model_ContinuosAction)



@given(instance=model_ContinuosAction_strategy)
def test_model_continuosaction_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=model_RandomAction_strategy)
@settings(max_examples=50)
def test_model_randomaction_instantiation(instance):
    assert isinstance(instance, model_RandomAction)



@given(instance=model_RandomAction_strategy)
def test_model_randomaction_isRandom_setter(instance):
    original = instance.isRandom
    instance.isRandom = original
    assert instance.isRandom == original

@given(instance=model_RotorAction_strategy)
@settings(max_examples=50)
def test_model_rotoraction_instantiation(instance):
    assert isinstance(instance, model_RotorAction)

@given(instance=model_Ending_strategy)
@settings(max_examples=50)
def test_model_ending_instantiation(instance):
    assert isinstance(instance, model_Ending)

@given(instance=model_Action_strategy)
@settings(max_examples=50)
def test_model_action_instantiation(instance):
    assert isinstance(instance, model_Action)

@given(instance=model_ActionsList_strategy)
@settings(max_examples=50)
def test_model_actionslist_instantiation(instance):
    assert isinstance(instance, model_ActionsList)

@given(instance=model_Event_strategy)
@settings(max_examples=50)
def test_model_event_instantiation(instance):
    assert isinstance(instance, model_Event)

@given(instance=ActionsList_strategy)
@settings(max_examples=50)
def test_actionslist_instantiation(instance):
    assert isinstance(instance, ActionsList)

@given(instance=model_EventListener_strategy)
@settings(max_examples=50)
def test_model_eventlistener_instantiation(instance):
    assert isinstance(instance, model_EventListener)

@given(instance=model_Main_strategy)
@settings(max_examples=50)
def test_model_main_instantiation(instance):
    assert isinstance(instance, model_Main)

@given(instance=model_RoboProse_strategy)
@settings(max_examples=50)
def test_model_roboprose_instantiation(instance):
    assert isinstance(instance, model_RoboProse)

@given(instance=model_Root_strategy)
@settings(max_examples=50)
def test_model_root_instantiation(instance):
    assert isinstance(instance, model_Root)

@given(instance=Ending_strategy)
@settings(max_examples=50)
def test_ending_instantiation(instance):
    assert isinstance(instance, Ending)

@given(instance=model_StartOver_strategy)
@settings(max_examples=50)
def test_model_startover_instantiation(instance):
    assert isinstance(instance, model_StartOver)

@given(instance=model_Wait_strategy)
@settings(max_examples=50)
def test_model_wait_instantiation(instance):
    assert isinstance(instance, model_Wait)

@given(instance=model_Repeat_strategy)
@settings(max_examples=50)
def test_model_repeat_instantiation(instance):
    assert isinstance(instance, model_Repeat)
