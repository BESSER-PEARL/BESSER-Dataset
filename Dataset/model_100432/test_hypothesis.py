import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Trigger,
    StateMachine::TriggerExpression,
    Guard,
    StateMachine::GuardExpression,
    Action,
    StateMachine::ActionExpression,
    StateMachine::TurnoutDesiredDirection,
    StateMachine::RouteElement,
    TriggerExpression,
    StateMachine::SignalAllowedSpeedChanged,
    StateMachine::TurnoutDirectionChanged,
    StateMachine::TrainTrackElementChanged,
    StateMachine::TrainHeadingSpeedChanged,
    GuardExpression,
    StateMachine::SignalCurrentAllowedSpeed,
    StateMachine::NextTrackElementIs,
    StateMachine::TurnoutCurrentDirection,
    StateMachine::TrainCurrentlyStandsOn,
    StateMachine::TurnoutHasDesiredDirection,
    StateMachine::TrainCurrentHeadingSpeed,
    StateMachine::TrackElement,
    StateMachine::Turnout,
    StateMachine::Signal,
    StateMachine::Train,
    ActionExpression,
    StateMachine::ChangeSignalAllowedSpeed,
    StateMachine::ChangeTrainCurrentTrackElement,
    StateMachine::ChangeTurnoutDirection,
    StateMachine::ChangeTrainHeadingSpeed,
    StateMachine::NamedElement,
    State,
    StateMachine::CompositeState,
    StateMachine::RDMElement,
    StateMachine::StateMachineBehavioralModel,
    NamedElement,
    StateMachine::Action,
    StateMachine::State,
    StateMachine::Transition,
    StateMachine::Trigger,
    StateMachine::Guard,
    StateMachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::triggerexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TriggerExpression)


def test_statemachine::triggerexpression_constructor_exists():
    assert callable(StateMachine::TriggerExpression.__init__)


def test_statemachine::triggerexpression_constructor_args():
    sig = inspect.signature(StateMachine::TriggerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine::triggerexpression_has_expression():
    assert hasattr(StateMachine::TriggerExpression, "expression")
    descriptor = None
    for klass in StateMachine::TriggerExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::guardexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine::GuardExpression)


def test_statemachine::guardexpression_constructor_exists():
    assert callable(StateMachine::GuardExpression.__init__)


def test_statemachine::guardexpression_constructor_args():
    sig = inspect.signature(StateMachine::GuardExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine::guardexpression_has_expression():
    assert hasattr(StateMachine::GuardExpression, "expression")
    descriptor = None
    for klass in StateMachine::GuardExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::actionexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine::ActionExpression)


def test_statemachine::actionexpression_constructor_exists():
    assert callable(StateMachine::ActionExpression.__init__)


def test_statemachine::actionexpression_constructor_args():
    sig = inspect.signature(StateMachine::ActionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine::actionexpression_has_expression():
    assert hasattr(StateMachine::ActionExpression, "expression")
    descriptor = None
    for klass in StateMachine::ActionExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::turnoutdesireddirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TurnoutDesiredDirection)


def test_statemachine::turnoutdesireddirection_constructor_exists():
    assert callable(StateMachine::TurnoutDesiredDirection.__init__)


def test_statemachine::turnoutdesireddirection_constructor_args():
    sig = inspect.signature(StateMachine::TurnoutDesiredDirection.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::routeelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine::RouteElement)


def test_statemachine::routeelement_constructor_exists():
    assert callable(StateMachine::RouteElement.__init__)


def test_statemachine::routeelement_constructor_args():
    sig = inspect.signature(StateMachine::RouteElement.__init__)
    params = list(sig.parameters.keys())



def test_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(TriggerExpression)


def test_triggerexpression_constructor_exists():
    assert callable(TriggerExpression.__init__)


def test_triggerexpression_constructor_args():
    sig = inspect.signature(TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::signalallowedspeedchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine::SignalAllowedSpeedChanged)


def test_statemachine::signalallowedspeedchanged_constructor_exists():
    assert callable(StateMachine::SignalAllowedSpeedChanged.__init__)


def test_statemachine::signalallowedspeedchanged_constructor_args():
    sig = inspect.signature(StateMachine::SignalAllowedSpeedChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newAllowedSpeed" in params, "Missing parameter 'newAllowedSpeed'"

def test_statemachine::signalallowedspeedchanged_has_newAllowedSpeed():
    assert hasattr(StateMachine::SignalAllowedSpeedChanged, "newAllowedSpeed")
    descriptor = None
    for klass in StateMachine::SignalAllowedSpeedChanged.__mro__:
        if "newAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::turnoutdirectionchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TurnoutDirectionChanged)


def test_statemachine::turnoutdirectionchanged_constructor_exists():
    assert callable(StateMachine::TurnoutDirectionChanged.__init__)


def test_statemachine::turnoutdirectionchanged_constructor_args():
    sig = inspect.signature(StateMachine::TurnoutDirectionChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newTurnoutDirection" in params, "Missing parameter 'newTurnoutDirection'"

def test_statemachine::turnoutdirectionchanged_has_newTurnoutDirection():
    assert hasattr(StateMachine::TurnoutDirectionChanged, "newTurnoutDirection")
    descriptor = None
    for klass in StateMachine::TurnoutDirectionChanged.__mro__:
        if "newTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["newTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::traintrackelementchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TrainTrackElementChanged)


def test_statemachine::traintrackelementchanged_constructor_exists():
    assert callable(StateMachine::TrainTrackElementChanged.__init__)


def test_statemachine::traintrackelementchanged_constructor_args():
    sig = inspect.signature(StateMachine::TrainTrackElementChanged.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::trainheadingspeedchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TrainHeadingSpeedChanged)


def test_statemachine::trainheadingspeedchanged_constructor_exists():
    assert callable(StateMachine::TrainHeadingSpeedChanged.__init__)


def test_statemachine::trainheadingspeedchanged_constructor_args():
    sig = inspect.signature(StateMachine::TrainHeadingSpeedChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newHeadingSpeed" in params, "Missing parameter 'newHeadingSpeed'"

def test_statemachine::trainheadingspeedchanged_has_newHeadingSpeed():
    assert hasattr(StateMachine::TrainHeadingSpeedChanged, "newHeadingSpeed")
    descriptor = None
    for klass in StateMachine::TrainHeadingSpeedChanged.__mro__:
        if "newHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_guardexpression_is_not_abstract():
    assert not inspect.isabstract(GuardExpression)


def test_guardexpression_constructor_exists():
    assert callable(GuardExpression.__init__)


def test_guardexpression_constructor_args():
    sig = inspect.signature(GuardExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::signalcurrentallowedspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine::SignalCurrentAllowedSpeed)


def test_statemachine::signalcurrentallowedspeed_constructor_exists():
    assert callable(StateMachine::SignalCurrentAllowedSpeed.__init__)


def test_statemachine::signalcurrentallowedspeed_constructor_args():
    sig = inspect.signature(StateMachine::SignalCurrentAllowedSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "currentAllowedSpeed" in params, "Missing parameter 'currentAllowedSpeed'"

def test_statemachine::signalcurrentallowedspeed_has_currentAllowedSpeed():
    assert hasattr(StateMachine::SignalCurrentAllowedSpeed, "currentAllowedSpeed")
    descriptor = None
    for klass in StateMachine::SignalCurrentAllowedSpeed.__mro__:
        if "currentAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["currentAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::nexttrackelementis_is_not_abstract():
    assert not inspect.isabstract(StateMachine::NextTrackElementIs)


def test_statemachine::nexttrackelementis_constructor_exists():
    assert callable(StateMachine::NextTrackElementIs.__init__)


def test_statemachine::nexttrackelementis_constructor_args():
    sig = inspect.signature(StateMachine::NextTrackElementIs.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::turnoutcurrentdirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TurnoutCurrentDirection)


def test_statemachine::turnoutcurrentdirection_constructor_exists():
    assert callable(StateMachine::TurnoutCurrentDirection.__init__)


def test_statemachine::turnoutcurrentdirection_constructor_args():
    sig = inspect.signature(StateMachine::TurnoutCurrentDirection.__init__)
    params = list(sig.parameters.keys())
    assert "currentTurnoutDirection" in params, "Missing parameter 'currentTurnoutDirection'"

def test_statemachine::turnoutcurrentdirection_has_currentTurnoutDirection():
    assert hasattr(StateMachine::TurnoutCurrentDirection, "currentTurnoutDirection")
    descriptor = None
    for klass in StateMachine::TurnoutCurrentDirection.__mro__:
        if "currentTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["currentTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::traincurrentlystandson_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TrainCurrentlyStandsOn)


def test_statemachine::traincurrentlystandson_constructor_exists():
    assert callable(StateMachine::TrainCurrentlyStandsOn.__init__)


def test_statemachine::traincurrentlystandson_constructor_args():
    sig = inspect.signature(StateMachine::TrainCurrentlyStandsOn.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::turnouthasdesireddirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TurnoutHasDesiredDirection)


def test_statemachine::turnouthasdesireddirection_constructor_exists():
    assert callable(StateMachine::TurnoutHasDesiredDirection.__init__)


def test_statemachine::turnouthasdesireddirection_constructor_args():
    sig = inspect.signature(StateMachine::TurnoutHasDesiredDirection.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::traincurrentheadingspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TrainCurrentHeadingSpeed)


def test_statemachine::traincurrentheadingspeed_constructor_exists():
    assert callable(StateMachine::TrainCurrentHeadingSpeed.__init__)


def test_statemachine::traincurrentheadingspeed_constructor_args():
    sig = inspect.signature(StateMachine::TrainCurrentHeadingSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "currentHeadingSpeed" in params, "Missing parameter 'currentHeadingSpeed'"

def test_statemachine::traincurrentheadingspeed_has_currentHeadingSpeed():
    assert hasattr(StateMachine::TrainCurrentHeadingSpeed, "currentHeadingSpeed")
    descriptor = None
    for klass in StateMachine::TrainCurrentHeadingSpeed.__mro__:
        if "currentHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["currentHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::trackelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine::TrackElement)


def test_statemachine::trackelement_constructor_exists():
    assert callable(StateMachine::TrackElement.__init__)


def test_statemachine::trackelement_constructor_args():
    sig = inspect.signature(StateMachine::TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::turnout_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Turnout)


def test_statemachine::turnout_constructor_exists():
    assert callable(StateMachine::Turnout.__init__)


def test_statemachine::turnout_constructor_args():
    sig = inspect.signature(StateMachine::Turnout.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::signal_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Signal)


def test_statemachine::signal_constructor_exists():
    assert callable(StateMachine::Signal.__init__)


def test_statemachine::signal_constructor_args():
    sig = inspect.signature(StateMachine::Signal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::train_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Train)


def test_statemachine::train_constructor_exists():
    assert callable(StateMachine::Train.__init__)


def test_statemachine::train_constructor_args():
    sig = inspect.signature(StateMachine::Train.__init__)
    params = list(sig.parameters.keys())



def test_actionexpression_is_not_abstract():
    assert not inspect.isabstract(ActionExpression)


def test_actionexpression_constructor_exists():
    assert callable(ActionExpression.__init__)


def test_actionexpression_constructor_args():
    sig = inspect.signature(ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::changesignalallowedspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine::ChangeSignalAllowedSpeed)


def test_statemachine::changesignalallowedspeed_constructor_exists():
    assert callable(StateMachine::ChangeSignalAllowedSpeed.__init__)


def test_statemachine::changesignalallowedspeed_constructor_args():
    sig = inspect.signature(StateMachine::ChangeSignalAllowedSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "newAllowedSpeed" in params, "Missing parameter 'newAllowedSpeed'"

def test_statemachine::changesignalallowedspeed_has_newAllowedSpeed():
    assert hasattr(StateMachine::ChangeSignalAllowedSpeed, "newAllowedSpeed")
    descriptor = None
    for klass in StateMachine::ChangeSignalAllowedSpeed.__mro__:
        if "newAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::changetraincurrenttrackelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine::ChangeTrainCurrentTrackElement)


def test_statemachine::changetraincurrenttrackelement_constructor_exists():
    assert callable(StateMachine::ChangeTrainCurrentTrackElement.__init__)


def test_statemachine::changetraincurrenttrackelement_constructor_args():
    sig = inspect.signature(StateMachine::ChangeTrainCurrentTrackElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::changeturnoutdirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine::ChangeTurnoutDirection)


def test_statemachine::changeturnoutdirection_constructor_exists():
    assert callable(StateMachine::ChangeTurnoutDirection.__init__)


def test_statemachine::changeturnoutdirection_constructor_args():
    sig = inspect.signature(StateMachine::ChangeTurnoutDirection.__init__)
    params = list(sig.parameters.keys())
    assert "newTurnoutDirection" in params, "Missing parameter 'newTurnoutDirection'"

def test_statemachine::changeturnoutdirection_has_newTurnoutDirection():
    assert hasattr(StateMachine::ChangeTurnoutDirection, "newTurnoutDirection")
    descriptor = None
    for klass in StateMachine::ChangeTurnoutDirection.__mro__:
        if "newTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["newTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::changetrainheadingspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine::ChangeTrainHeadingSpeed)


def test_statemachine::changetrainheadingspeed_constructor_exists():
    assert callable(StateMachine::ChangeTrainHeadingSpeed.__init__)


def test_statemachine::changetrainheadingspeed_constructor_args():
    sig = inspect.signature(StateMachine::ChangeTrainHeadingSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "newHeadingSpeed" in params, "Missing parameter 'newHeadingSpeed'"

def test_statemachine::changetrainheadingspeed_has_newHeadingSpeed():
    assert hasattr(StateMachine::ChangeTrainHeadingSpeed, "newHeadingSpeed")
    descriptor = None
    for klass in StateMachine::ChangeTrainHeadingSpeed.__mro__:
        if "newHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::namedelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine::NamedElement)


def test_statemachine::namedelement_constructor_exists():
    assert callable(StateMachine::NamedElement.__init__)


def test_statemachine::namedelement_constructor_args():
    sig = inspect.signature(StateMachine::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine::namedelement_has_name():
    assert hasattr(StateMachine::NamedElement, "name")
    descriptor = None
    for klass in StateMachine::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::compositestate_is_not_abstract():
    assert not inspect.isabstract(StateMachine::CompositeState)


def test_statemachine::compositestate_constructor_exists():
    assert callable(StateMachine::CompositeState.__init__)


def test_statemachine::compositestate_constructor_args():
    sig = inspect.signature(StateMachine::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::rdmelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine::RDMElement)


def test_statemachine::rdmelement_constructor_exists():
    assert callable(StateMachine::RDMElement.__init__)


def test_statemachine::rdmelement_constructor_args():
    sig = inspect.signature(StateMachine::RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachinebehavioralmodel_is_not_abstract():
    assert not inspect.isabstract(StateMachine::StateMachineBehavioralModel)


def test_statemachine::statemachinebehavioralmodel_constructor_exists():
    assert callable(StateMachine::StateMachineBehavioralModel.__init__)


def test_statemachine::statemachinebehavioralmodel_constructor_args():
    sig = inspect.signature(StateMachine::StateMachineBehavioralModel.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::action_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Action)


def test_statemachine::action_constructor_exists():
    assert callable(StateMachine::Action.__init__)


def test_statemachine::action_constructor_args():
    sig = inspect.signature(StateMachine::Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(StateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(StateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(StateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_statemachine::state_has_isActive():
    assert hasattr(StateMachine::State, "isActive")
    descriptor = None
    for klass in StateMachine::State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::state_has_isInitial():
    assert hasattr(StateMachine::State, "isInitial")
    descriptor = None
    for klass in StateMachine::State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(StateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(StateMachine::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "isFireable" in params, "Missing parameter 'isFireable'"
    assert "isEnabled" in params, "Missing parameter 'isEnabled'"

def test_statemachine::transition_has_isFireable():
    assert hasattr(StateMachine::Transition, "isFireable")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "isFireable" in klass.__dict__:
            descriptor = klass.__dict__["isFireable"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::transition_has_isEnabled():
    assert hasattr(StateMachine::Transition, "isEnabled")
    descriptor = None
    for klass in StateMachine::Transition.__mro__:
        if "isEnabled" in klass.__dict__:
            descriptor = klass.__dict__["isEnabled"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Trigger)


def test_statemachine::trigger_constructor_exists():
    assert callable(StateMachine::Trigger.__init__)


def test_statemachine::trigger_constructor_args():
    sig = inspect.signature(StateMachine::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::guard_is_not_abstract():
    assert not inspect.isabstract(StateMachine::Guard)


def test_statemachine::guard_constructor_exists():
    assert callable(StateMachine::Guard.__init__)


def test_statemachine::guard_constructor_args():
    sig = inspect.signature(StateMachine::Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(StateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(StateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())


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
Trigger_strategy = st.builds(
    Trigger,
)
StateMachine::TriggerExpression_strategy = st.builds(
    StateMachine::TriggerExpression,
    expression=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
StateMachine::GuardExpression_strategy = st.builds(
    StateMachine::GuardExpression,
    expression=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
StateMachine::ActionExpression_strategy = st.builds(
    StateMachine::ActionExpression,
    expression=
        safe_text
)
StateMachine::TurnoutDesiredDirection_strategy = st.builds(
    StateMachine::TurnoutDesiredDirection,
)
StateMachine::RouteElement_strategy = st.builds(
    StateMachine::RouteElement,
)
TriggerExpression_strategy = st.builds(
    TriggerExpression,
)
StateMachine::SignalAllowedSpeedChanged_strategy = st.builds(
    StateMachine::SignalAllowedSpeedChanged,
    newAllowedSpeed=
        safe_text
)
StateMachine::TurnoutDirectionChanged_strategy = st.builds(
    StateMachine::TurnoutDirectionChanged,
    newTurnoutDirection=
        safe_text
)
StateMachine::TrainTrackElementChanged_strategy = st.builds(
    StateMachine::TrainTrackElementChanged,
)
StateMachine::TrainHeadingSpeedChanged_strategy = st.builds(
    StateMachine::TrainHeadingSpeedChanged,
    newHeadingSpeed=
        safe_text
)
GuardExpression_strategy = st.builds(
    GuardExpression,
)
StateMachine::SignalCurrentAllowedSpeed_strategy = st.builds(
    StateMachine::SignalCurrentAllowedSpeed,
    currentAllowedSpeed=
        safe_text
)
StateMachine::NextTrackElementIs_strategy = st.builds(
    StateMachine::NextTrackElementIs,
)
StateMachine::TurnoutCurrentDirection_strategy = st.builds(
    StateMachine::TurnoutCurrentDirection,
    currentTurnoutDirection=
        safe_text
)
StateMachine::TrainCurrentlyStandsOn_strategy = st.builds(
    StateMachine::TrainCurrentlyStandsOn,
)
StateMachine::TurnoutHasDesiredDirection_strategy = st.builds(
    StateMachine::TurnoutHasDesiredDirection,
)
StateMachine::TrainCurrentHeadingSpeed_strategy = st.builds(
    StateMachine::TrainCurrentHeadingSpeed,
    currentHeadingSpeed=
        safe_text
)
StateMachine::TrackElement_strategy = st.builds(
    StateMachine::TrackElement,
)
StateMachine::Turnout_strategy = st.builds(
    StateMachine::Turnout,
)
StateMachine::Signal_strategy = st.builds(
    StateMachine::Signal,
)
StateMachine::Train_strategy = st.builds(
    StateMachine::Train,
)
ActionExpression_strategy = st.builds(
    ActionExpression,
)
StateMachine::ChangeSignalAllowedSpeed_strategy = st.builds(
    StateMachine::ChangeSignalAllowedSpeed,
    newAllowedSpeed=
        safe_text
)
StateMachine::ChangeTrainCurrentTrackElement_strategy = st.builds(
    StateMachine::ChangeTrainCurrentTrackElement,
)
StateMachine::ChangeTurnoutDirection_strategy = st.builds(
    StateMachine::ChangeTurnoutDirection,
    newTurnoutDirection=
        safe_text
)
StateMachine::ChangeTrainHeadingSpeed_strategy = st.builds(
    StateMachine::ChangeTrainHeadingSpeed,
    newHeadingSpeed=
        safe_text
)
StateMachine::NamedElement_strategy = st.builds(
    StateMachine::NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
StateMachine::CompositeState_strategy = st.builds(
    StateMachine::CompositeState,
)
StateMachine::RDMElement_strategy = st.builds(
    StateMachine::RDMElement,
)
StateMachine::StateMachineBehavioralModel_strategy = st.builds(
    StateMachine::StateMachineBehavioralModel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StateMachine::Action_strategy = st.builds(
    StateMachine::Action,
)
StateMachine::State_strategy = st.builds(
    StateMachine::State,
    isActive=
        st.booleans(),
    isInitial=
        st.booleans()
)
StateMachine::Transition_strategy = st.builds(
    StateMachine::Transition,
    isFireable=
        st.booleans(),
    isEnabled=
        st.booleans()
)
StateMachine::Trigger_strategy = st.builds(
    StateMachine::Trigger,
)
StateMachine::Guard_strategy = st.builds(
    StateMachine::Guard,
)
StateMachine::StateMachine_strategy = st.builds(
    StateMachine::StateMachine,
)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=StateMachine::TriggerExpression_strategy)
@settings(max_examples=50)
def test_statemachine::triggerexpression_instantiation(instance):
    assert isinstance(instance, StateMachine::TriggerExpression)

@given(instance=StateMachine::TriggerExpression_strategy)
def test_statemachine::triggerexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=StateMachine::TriggerExpression_strategy)
def test_statemachine::triggerexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=StateMachine::GuardExpression_strategy)
@settings(max_examples=50)
def test_statemachine::guardexpression_instantiation(instance):
    assert isinstance(instance, StateMachine::GuardExpression)

@given(instance=StateMachine::GuardExpression_strategy)
def test_statemachine::guardexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=StateMachine::GuardExpression_strategy)
def test_statemachine::guardexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=StateMachine::ActionExpression_strategy)
@settings(max_examples=50)
def test_statemachine::actionexpression_instantiation(instance):
    assert isinstance(instance, StateMachine::ActionExpression)

@given(instance=StateMachine::ActionExpression_strategy)
def test_statemachine::actionexpression_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=StateMachine::ActionExpression_strategy)
def test_statemachine::actionexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=StateMachine::TurnoutDesiredDirection_strategy)
@settings(max_examples=50)
def test_statemachine::turnoutdesireddirection_instantiation(instance):
    assert isinstance(instance, StateMachine::TurnoutDesiredDirection)

@given(instance=StateMachine::RouteElement_strategy)
@settings(max_examples=50)
def test_statemachine::routeelement_instantiation(instance):
    assert isinstance(instance, StateMachine::RouteElement)

@given(instance=TriggerExpression_strategy)
@settings(max_examples=50)
def test_triggerexpression_instantiation(instance):
    assert isinstance(instance, TriggerExpression)

@given(instance=StateMachine::SignalAllowedSpeedChanged_strategy)
@settings(max_examples=50)
def test_statemachine::signalallowedspeedchanged_instantiation(instance):
    assert isinstance(instance, StateMachine::SignalAllowedSpeedChanged)

@given(instance=StateMachine::SignalAllowedSpeedChanged_strategy)
def test_statemachine::signalallowedspeedchanged_newAllowedSpeed_type(instance):
    assert isinstance(instance.newAllowedSpeed, str)


@given(instance=StateMachine::SignalAllowedSpeedChanged_strategy)
def test_statemachine::signalallowedspeedchanged_newAllowedSpeed_setter(instance):
    original = instance.newAllowedSpeed
    instance.newAllowedSpeed = original
    assert instance.newAllowedSpeed == original

@given(instance=StateMachine::TurnoutDirectionChanged_strategy)
@settings(max_examples=50)
def test_statemachine::turnoutdirectionchanged_instantiation(instance):
    assert isinstance(instance, StateMachine::TurnoutDirectionChanged)

@given(instance=StateMachine::TurnoutDirectionChanged_strategy)
def test_statemachine::turnoutdirectionchanged_newTurnoutDirection_type(instance):
    assert isinstance(instance.newTurnoutDirection, str)


@given(instance=StateMachine::TurnoutDirectionChanged_strategy)
def test_statemachine::turnoutdirectionchanged_newTurnoutDirection_setter(instance):
    original = instance.newTurnoutDirection
    instance.newTurnoutDirection = original
    assert instance.newTurnoutDirection == original

@given(instance=StateMachine::TrainTrackElementChanged_strategy)
@settings(max_examples=50)
def test_statemachine::traintrackelementchanged_instantiation(instance):
    assert isinstance(instance, StateMachine::TrainTrackElementChanged)

@given(instance=StateMachine::TrainHeadingSpeedChanged_strategy)
@settings(max_examples=50)
def test_statemachine::trainheadingspeedchanged_instantiation(instance):
    assert isinstance(instance, StateMachine::TrainHeadingSpeedChanged)

@given(instance=StateMachine::TrainHeadingSpeedChanged_strategy)
def test_statemachine::trainheadingspeedchanged_newHeadingSpeed_type(instance):
    assert isinstance(instance.newHeadingSpeed, str)


@given(instance=StateMachine::TrainHeadingSpeedChanged_strategy)
def test_statemachine::trainheadingspeedchanged_newHeadingSpeed_setter(instance):
    original = instance.newHeadingSpeed
    instance.newHeadingSpeed = original
    assert instance.newHeadingSpeed == original

@given(instance=GuardExpression_strategy)
@settings(max_examples=50)
def test_guardexpression_instantiation(instance):
    assert isinstance(instance, GuardExpression)

@given(instance=StateMachine::SignalCurrentAllowedSpeed_strategy)
@settings(max_examples=50)
def test_statemachine::signalcurrentallowedspeed_instantiation(instance):
    assert isinstance(instance, StateMachine::SignalCurrentAllowedSpeed)

@given(instance=StateMachine::SignalCurrentAllowedSpeed_strategy)
def test_statemachine::signalcurrentallowedspeed_currentAllowedSpeed_type(instance):
    assert isinstance(instance.currentAllowedSpeed, str)


@given(instance=StateMachine::SignalCurrentAllowedSpeed_strategy)
def test_statemachine::signalcurrentallowedspeed_currentAllowedSpeed_setter(instance):
    original = instance.currentAllowedSpeed
    instance.currentAllowedSpeed = original
    assert instance.currentAllowedSpeed == original

@given(instance=StateMachine::NextTrackElementIs_strategy)
@settings(max_examples=50)
def test_statemachine::nexttrackelementis_instantiation(instance):
    assert isinstance(instance, StateMachine::NextTrackElementIs)

@given(instance=StateMachine::TurnoutCurrentDirection_strategy)
@settings(max_examples=50)
def test_statemachine::turnoutcurrentdirection_instantiation(instance):
    assert isinstance(instance, StateMachine::TurnoutCurrentDirection)

@given(instance=StateMachine::TurnoutCurrentDirection_strategy)
def test_statemachine::turnoutcurrentdirection_currentTurnoutDirection_type(instance):
    assert isinstance(instance.currentTurnoutDirection, str)


@given(instance=StateMachine::TurnoutCurrentDirection_strategy)
def test_statemachine::turnoutcurrentdirection_currentTurnoutDirection_setter(instance):
    original = instance.currentTurnoutDirection
    instance.currentTurnoutDirection = original
    assert instance.currentTurnoutDirection == original

@given(instance=StateMachine::TrainCurrentlyStandsOn_strategy)
@settings(max_examples=50)
def test_statemachine::traincurrentlystandson_instantiation(instance):
    assert isinstance(instance, StateMachine::TrainCurrentlyStandsOn)

@given(instance=StateMachine::TurnoutHasDesiredDirection_strategy)
@settings(max_examples=50)
def test_statemachine::turnouthasdesireddirection_instantiation(instance):
    assert isinstance(instance, StateMachine::TurnoutHasDesiredDirection)

@given(instance=StateMachine::TrainCurrentHeadingSpeed_strategy)
@settings(max_examples=50)
def test_statemachine::traincurrentheadingspeed_instantiation(instance):
    assert isinstance(instance, StateMachine::TrainCurrentHeadingSpeed)

@given(instance=StateMachine::TrainCurrentHeadingSpeed_strategy)
def test_statemachine::traincurrentheadingspeed_currentHeadingSpeed_type(instance):
    assert isinstance(instance.currentHeadingSpeed, str)


@given(instance=StateMachine::TrainCurrentHeadingSpeed_strategy)
def test_statemachine::traincurrentheadingspeed_currentHeadingSpeed_setter(instance):
    original = instance.currentHeadingSpeed
    instance.currentHeadingSpeed = original
    assert instance.currentHeadingSpeed == original

@given(instance=StateMachine::TrackElement_strategy)
@settings(max_examples=50)
def test_statemachine::trackelement_instantiation(instance):
    assert isinstance(instance, StateMachine::TrackElement)

@given(instance=StateMachine::Turnout_strategy)
@settings(max_examples=50)
def test_statemachine::turnout_instantiation(instance):
    assert isinstance(instance, StateMachine::Turnout)

@given(instance=StateMachine::Signal_strategy)
@settings(max_examples=50)
def test_statemachine::signal_instantiation(instance):
    assert isinstance(instance, StateMachine::Signal)

@given(instance=StateMachine::Train_strategy)
@settings(max_examples=50)
def test_statemachine::train_instantiation(instance):
    assert isinstance(instance, StateMachine::Train)

@given(instance=ActionExpression_strategy)
@settings(max_examples=50)
def test_actionexpression_instantiation(instance):
    assert isinstance(instance, ActionExpression)

@given(instance=StateMachine::ChangeSignalAllowedSpeed_strategy)
@settings(max_examples=50)
def test_statemachine::changesignalallowedspeed_instantiation(instance):
    assert isinstance(instance, StateMachine::ChangeSignalAllowedSpeed)

@given(instance=StateMachine::ChangeSignalAllowedSpeed_strategy)
def test_statemachine::changesignalallowedspeed_newAllowedSpeed_type(instance):
    assert isinstance(instance.newAllowedSpeed, str)


@given(instance=StateMachine::ChangeSignalAllowedSpeed_strategy)
def test_statemachine::changesignalallowedspeed_newAllowedSpeed_setter(instance):
    original = instance.newAllowedSpeed
    instance.newAllowedSpeed = original
    assert instance.newAllowedSpeed == original

@given(instance=StateMachine::ChangeTrainCurrentTrackElement_strategy)
@settings(max_examples=50)
def test_statemachine::changetraincurrenttrackelement_instantiation(instance):
    assert isinstance(instance, StateMachine::ChangeTrainCurrentTrackElement)

@given(instance=StateMachine::ChangeTurnoutDirection_strategy)
@settings(max_examples=50)
def test_statemachine::changeturnoutdirection_instantiation(instance):
    assert isinstance(instance, StateMachine::ChangeTurnoutDirection)

@given(instance=StateMachine::ChangeTurnoutDirection_strategy)
def test_statemachine::changeturnoutdirection_newTurnoutDirection_type(instance):
    assert isinstance(instance.newTurnoutDirection, str)


@given(instance=StateMachine::ChangeTurnoutDirection_strategy)
def test_statemachine::changeturnoutdirection_newTurnoutDirection_setter(instance):
    original = instance.newTurnoutDirection
    instance.newTurnoutDirection = original
    assert instance.newTurnoutDirection == original

@given(instance=StateMachine::ChangeTrainHeadingSpeed_strategy)
@settings(max_examples=50)
def test_statemachine::changetrainheadingspeed_instantiation(instance):
    assert isinstance(instance, StateMachine::ChangeTrainHeadingSpeed)

@given(instance=StateMachine::ChangeTrainHeadingSpeed_strategy)
def test_statemachine::changetrainheadingspeed_newHeadingSpeed_type(instance):
    assert isinstance(instance.newHeadingSpeed, str)


@given(instance=StateMachine::ChangeTrainHeadingSpeed_strategy)
def test_statemachine::changetrainheadingspeed_newHeadingSpeed_setter(instance):
    original = instance.newHeadingSpeed
    instance.newHeadingSpeed = original
    assert instance.newHeadingSpeed == original

@given(instance=StateMachine::NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine::namedelement_instantiation(instance):
    assert isinstance(instance, StateMachine::NamedElement)

@given(instance=StateMachine::NamedElement_strategy)
def test_statemachine::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=StateMachine::NamedElement_strategy)
def test_statemachine::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine::CompositeState_strategy)
@settings(max_examples=50)
def test_statemachine::compositestate_instantiation(instance):
    assert isinstance(instance, StateMachine::CompositeState)

@given(instance=StateMachine::RDMElement_strategy)
@settings(max_examples=50)
def test_statemachine::rdmelement_instantiation(instance):
    assert isinstance(instance, StateMachine::RDMElement)

@given(instance=StateMachine::StateMachineBehavioralModel_strategy)
@settings(max_examples=50)
def test_statemachine::statemachinebehavioralmodel_instantiation(instance):
    assert isinstance(instance, StateMachine::StateMachineBehavioralModel)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StateMachine::Action_strategy)
@settings(max_examples=50)
def test_statemachine::action_instantiation(instance):
    assert isinstance(instance, StateMachine::Action)

@given(instance=StateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, StateMachine::State)

@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=StateMachine::State_strategy)
def test_statemachine::state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=StateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, StateMachine::Transition)

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_isFireable_type(instance):
    assert isinstance(instance.isFireable, bool)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_isFireable_setter(instance):
    original = instance.isFireable
    instance.isFireable = original
    assert instance.isFireable == original

@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_isEnabled_type(instance):
    assert isinstance(instance.isEnabled, bool)


@given(instance=StateMachine::Transition_strategy)
def test_statemachine::transition_isEnabled_setter(instance):
    original = instance.isEnabled
    instance.isEnabled = original
    assert instance.isEnabled == original

@given(instance=StateMachine::Trigger_strategy)
@settings(max_examples=50)
def test_statemachine::trigger_instantiation(instance):
    assert isinstance(instance, StateMachine::Trigger)

@given(instance=StateMachine::Guard_strategy)
@settings(max_examples=50)
def test_statemachine::guard_instantiation(instance):
    assert isinstance(instance, StateMachine::Guard)

@given(instance=StateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine::StateMachine)
