import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Event,
    model::Tapped,
    model::Obstacle,
    RandomAction,
    ContinuosAction,
    RotorAction,
    model::Turn,
    model::Move,
    Action,
    model::RandomAction,
    model::ContinuosAction,
    model::RotorAction,
    model::Ending,
    model::Action,
    model::ActionsList,
    model::Event,
    ActionsList,
    model::EventListener,
    model::Main,
    model::RoboProse,
    model::Root,
    Ending,
    model::StartOver,
    model::Wait,
    model::Repeat,
    model::Stop,
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



def test_model::tapped_is_not_abstract():
    assert not inspect.isabstract(model::Tapped)


def test_model::tapped_constructor_exists():
    assert callable(model::Tapped.__init__)


def test_model::tapped_constructor_args():
    sig = inspect.signature(model::Tapped.__init__)
    params = list(sig.parameters.keys())



def test_model::obstacle_is_not_abstract():
    assert not inspect.isabstract(model::Obstacle)


def test_model::obstacle_constructor_exists():
    assert callable(model::Obstacle.__init__)


def test_model::obstacle_constructor_args():
    sig = inspect.signature(model::Obstacle.__init__)
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



def test_rotoraction_is_not_abstract():
    assert not inspect.isabstract(RotorAction)


def test_rotoraction_constructor_exists():
    assert callable(RotorAction.__init__)


def test_rotoraction_constructor_args():
    sig = inspect.signature(RotorAction.__init__)
    params = list(sig.parameters.keys())



def test_model::turn_is_not_abstract():
    assert not inspect.isabstract(model::Turn)


def test_model::turn_constructor_exists():
    assert callable(model::Turn.__init__)


def test_model::turn_constructor_args():
    sig = inspect.signature(model::Turn.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_model::turn_has_direction():
    assert hasattr(model::Turn, "direction")
    descriptor = None
    for klass in model::Turn.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_model::turn_has_degrees():
    assert hasattr(model::Turn, "degrees")
    descriptor = None
    for klass in model::Turn.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_model::move_is_not_abstract():
    assert not inspect.isabstract(model::Move)


def test_model::move_constructor_exists():
    assert callable(model::Move.__init__)


def test_model::move_constructor_args():
    sig = inspect.signature(model::Move.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_model::move_has_direction():
    assert hasattr(model::Move, "direction")
    descriptor = None
    for klass in model::Move.__mro__:
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



def test_model::randomaction_is_not_abstract():
    assert not inspect.isabstract(model::RandomAction)


def test_model::randomaction_constructor_exists():
    assert callable(model::RandomAction.__init__)


def test_model::randomaction_constructor_args():
    sig = inspect.signature(model::RandomAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRandom" in params, "Missing parameter 'isRandom'"

def test_model::randomaction_has_isRandom():
    assert hasattr(model::RandomAction, "isRandom")
    descriptor = None
    for klass in model::RandomAction.__mro__:
        if "isRandom" in klass.__dict__:
            descriptor = klass.__dict__["isRandom"]
            break
    assert isinstance(descriptor, property)



def test_model::continuosaction_is_not_abstract():
    assert not inspect.isabstract(model::ContinuosAction)


def test_model::continuosaction_constructor_exists():
    assert callable(model::ContinuosAction.__init__)


def test_model::continuosaction_constructor_args():
    sig = inspect.signature(model::ContinuosAction.__init__)
    params = list(sig.parameters.keys())
    assert "duration" in params, "Missing parameter 'duration'"

def test_model::continuosaction_has_duration():
    assert hasattr(model::ContinuosAction, "duration")
    descriptor = None
    for klass in model::ContinuosAction.__mro__:
        if "duration" in klass.__dict__:
            descriptor = klass.__dict__["duration"]
            break
    assert isinstance(descriptor, property)



def test_model::rotoraction_is_not_abstract():
    assert not inspect.isabstract(model::RotorAction)


def test_model::rotoraction_constructor_exists():
    assert callable(model::RotorAction.__init__)


def test_model::rotoraction_constructor_args():
    sig = inspect.signature(model::RotorAction.__init__)
    params = list(sig.parameters.keys())



def test_model::ending_is_not_abstract():
    assert not inspect.isabstract(model::Ending)


def test_model::ending_constructor_exists():
    assert callable(model::Ending.__init__)


def test_model::ending_constructor_args():
    sig = inspect.signature(model::Ending.__init__)
    params = list(sig.parameters.keys())



def test_model::action_is_not_abstract():
    assert not inspect.isabstract(model::Action)


def test_model::action_constructor_exists():
    assert callable(model::Action.__init__)


def test_model::action_constructor_args():
    sig = inspect.signature(model::Action.__init__)
    params = list(sig.parameters.keys())



def test_model::actionslist_is_not_abstract():
    assert not inspect.isabstract(model::ActionsList)


def test_model::actionslist_constructor_exists():
    assert callable(model::ActionsList.__init__)


def test_model::actionslist_constructor_args():
    sig = inspect.signature(model::ActionsList.__init__)
    params = list(sig.parameters.keys())



def test_model::event_is_not_abstract():
    assert not inspect.isabstract(model::Event)


def test_model::event_constructor_exists():
    assert callable(model::Event.__init__)


def test_model::event_constructor_args():
    sig = inspect.signature(model::Event.__init__)
    params = list(sig.parameters.keys())



def test_actionslist_is_not_abstract():
    assert not inspect.isabstract(ActionsList)


def test_actionslist_constructor_exists():
    assert callable(ActionsList.__init__)


def test_actionslist_constructor_args():
    sig = inspect.signature(ActionsList.__init__)
    params = list(sig.parameters.keys())



def test_model::eventlistener_is_not_abstract():
    assert not inspect.isabstract(model::EventListener)


def test_model::eventlistener_constructor_exists():
    assert callable(model::EventListener.__init__)


def test_model::eventlistener_constructor_args():
    sig = inspect.signature(model::EventListener.__init__)
    params = list(sig.parameters.keys())



def test_model::main_is_not_abstract():
    assert not inspect.isabstract(model::Main)


def test_model::main_constructor_exists():
    assert callable(model::Main.__init__)


def test_model::main_constructor_args():
    sig = inspect.signature(model::Main.__init__)
    params = list(sig.parameters.keys())



def test_model::roboprose_is_not_abstract():
    assert not inspect.isabstract(model::RoboProse)


def test_model::roboprose_constructor_exists():
    assert callable(model::RoboProse.__init__)


def test_model::roboprose_constructor_args():
    sig = inspect.signature(model::RoboProse.__init__)
    params = list(sig.parameters.keys())



def test_model::root_is_not_abstract():
    assert not inspect.isabstract(model::Root)


def test_model::root_constructor_exists():
    assert callable(model::Root.__init__)


def test_model::root_constructor_args():
    sig = inspect.signature(model::Root.__init__)
    params = list(sig.parameters.keys())



def test_ending_is_not_abstract():
    assert not inspect.isabstract(Ending)


def test_ending_constructor_exists():
    assert callable(Ending.__init__)


def test_ending_constructor_args():
    sig = inspect.signature(Ending.__init__)
    params = list(sig.parameters.keys())



def test_model::startover_is_not_abstract():
    assert not inspect.isabstract(model::StartOver)


def test_model::startover_constructor_exists():
    assert callable(model::StartOver.__init__)


def test_model::startover_constructor_args():
    sig = inspect.signature(model::StartOver.__init__)
    params = list(sig.parameters.keys())



def test_model::wait_is_not_abstract():
    assert not inspect.isabstract(model::Wait)


def test_model::wait_constructor_exists():
    assert callable(model::Wait.__init__)


def test_model::wait_constructor_args():
    sig = inspect.signature(model::Wait.__init__)
    params = list(sig.parameters.keys())



def test_model::repeat_is_not_abstract():
    assert not inspect.isabstract(model::Repeat)


def test_model::repeat_constructor_exists():
    assert callable(model::Repeat.__init__)


def test_model::repeat_constructor_args():
    sig = inspect.signature(model::Repeat.__init__)
    params = list(sig.parameters.keys())



def test_model::stop_is_not_abstract():
    assert not inspect.isabstract(model::Stop)


def test_model::stop_constructor_exists():
    assert callable(model::Stop.__init__)


def test_model::stop_constructor_args():
    sig = inspect.signature(model::Stop.__init__)
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
model::Tapped_strategy = st.builds(
    model::Tapped,
)
model::Obstacle_strategy = st.builds(
    model::Obstacle,
)
RandomAction_strategy = st.builds(
    RandomAction,
)
ContinuosAction_strategy = st.builds(
    ContinuosAction,
)
RotorAction_strategy = st.builds(
    RotorAction,
)
model::Turn_strategy = st.builds(
    model::Turn,
    direction=
        safe_text,
    degrees=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::Move_strategy = st.builds(
    model::Move,
    direction=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
model::RandomAction_strategy = st.builds(
    model::RandomAction,
    isRandom=
        st.booleans()
)
model::ContinuosAction_strategy = st.builds(
    model::ContinuosAction,
    duration=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
model::RotorAction_strategy = st.builds(
    model::RotorAction,
)
model::Ending_strategy = st.builds(
    model::Ending,
)
model::Action_strategy = st.builds(
    model::Action,
)
model::ActionsList_strategy = st.builds(
    model::ActionsList,
)
model::Event_strategy = st.builds(
    model::Event,
)
ActionsList_strategy = st.builds(
    ActionsList,
)
model::EventListener_strategy = st.builds(
    model::EventListener,
)
model::Main_strategy = st.builds(
    model::Main,
)
model::RoboProse_strategy = st.builds(
    model::RoboProse,
)
model::Root_strategy = st.builds(
    model::Root,
)
Ending_strategy = st.builds(
    Ending,
)
model::StartOver_strategy = st.builds(
    model::StartOver,
)
model::Wait_strategy = st.builds(
    model::Wait,
)
model::Repeat_strategy = st.builds(
    model::Repeat,
)
model::Stop_strategy = st.builds(
    model::Stop,
)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=model::Tapped_strategy)
@settings(max_examples=50)
def test_model::tapped_instantiation(instance):
    assert isinstance(instance, model::Tapped)

@given(instance=model::Obstacle_strategy)
@settings(max_examples=50)
def test_model::obstacle_instantiation(instance):
    assert isinstance(instance, model::Obstacle)

@given(instance=RandomAction_strategy)
@settings(max_examples=50)
def test_randomaction_instantiation(instance):
    assert isinstance(instance, RandomAction)

@given(instance=ContinuosAction_strategy)
@settings(max_examples=50)
def test_continuosaction_instantiation(instance):
    assert isinstance(instance, ContinuosAction)

@given(instance=RotorAction_strategy)
@settings(max_examples=50)
def test_rotoraction_instantiation(instance):
    assert isinstance(instance, RotorAction)

@given(instance=model::Turn_strategy)
@settings(max_examples=50)
def test_model::turn_instantiation(instance):
    assert isinstance(instance, model::Turn)

@given(instance=model::Turn_strategy)
def test_model::turn_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=model::Turn_strategy)
def test_model::turn_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=model::Turn_strategy)
def test_model::turn_degrees_type(instance):
    assert isinstance(instance.degrees, float)


@given(instance=model::Turn_strategy)
def test_model::turn_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=model::Move_strategy)
@settings(max_examples=50)
def test_model::move_instantiation(instance):
    assert isinstance(instance, model::Move)

@given(instance=model::Move_strategy)
def test_model::move_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=model::Move_strategy)
def test_model::move_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model::RandomAction_strategy)
@settings(max_examples=50)
def test_model::randomaction_instantiation(instance):
    assert isinstance(instance, model::RandomAction)

@given(instance=model::RandomAction_strategy)
def test_model::randomaction_isRandom_type(instance):
    assert isinstance(instance.isRandom, bool)


@given(instance=model::RandomAction_strategy)
def test_model::randomaction_isRandom_setter(instance):
    original = instance.isRandom
    instance.isRandom = original
    assert instance.isRandom == original

@given(instance=model::ContinuosAction_strategy)
@settings(max_examples=50)
def test_model::continuosaction_instantiation(instance):
    assert isinstance(instance, model::ContinuosAction)

@given(instance=model::ContinuosAction_strategy)
def test_model::continuosaction_duration_type(instance):
    assert isinstance(instance.duration, float)


@given(instance=model::ContinuosAction_strategy)
def test_model::continuosaction_duration_setter(instance):
    original = instance.duration
    instance.duration = original
    assert instance.duration == original

@given(instance=model::RotorAction_strategy)
@settings(max_examples=50)
def test_model::rotoraction_instantiation(instance):
    assert isinstance(instance, model::RotorAction)

@given(instance=model::Ending_strategy)
@settings(max_examples=50)
def test_model::ending_instantiation(instance):
    assert isinstance(instance, model::Ending)

@given(instance=model::Action_strategy)
@settings(max_examples=50)
def test_model::action_instantiation(instance):
    assert isinstance(instance, model::Action)

@given(instance=model::ActionsList_strategy)
@settings(max_examples=50)
def test_model::actionslist_instantiation(instance):
    assert isinstance(instance, model::ActionsList)

@given(instance=model::Event_strategy)
@settings(max_examples=50)
def test_model::event_instantiation(instance):
    assert isinstance(instance, model::Event)

@given(instance=ActionsList_strategy)
@settings(max_examples=50)
def test_actionslist_instantiation(instance):
    assert isinstance(instance, ActionsList)

@given(instance=model::EventListener_strategy)
@settings(max_examples=50)
def test_model::eventlistener_instantiation(instance):
    assert isinstance(instance, model::EventListener)

@given(instance=model::Main_strategy)
@settings(max_examples=50)
def test_model::main_instantiation(instance):
    assert isinstance(instance, model::Main)

@given(instance=model::RoboProse_strategy)
@settings(max_examples=50)
def test_model::roboprose_instantiation(instance):
    assert isinstance(instance, model::RoboProse)

@given(instance=model::Root_strategy)
@settings(max_examples=50)
def test_model::root_instantiation(instance):
    assert isinstance(instance, model::Root)

@given(instance=Ending_strategy)
@settings(max_examples=50)
def test_ending_instantiation(instance):
    assert isinstance(instance, Ending)

@given(instance=model::StartOver_strategy)
@settings(max_examples=50)
def test_model::startover_instantiation(instance):
    assert isinstance(instance, model::StartOver)

@given(instance=model::Wait_strategy)
@settings(max_examples=50)
def test_model::wait_instantiation(instance):
    assert isinstance(instance, model::Wait)

@given(instance=model::Repeat_strategy)
@settings(max_examples=50)
def test_model::repeat_instantiation(instance):
    assert isinstance(instance, model::Repeat)

@given(instance=model::Stop_strategy)
@settings(max_examples=50)
def test_model::stop_instantiation(instance):
    assert isinstance(instance, model::Stop)
