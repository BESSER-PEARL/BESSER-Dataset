import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TriggerExpression,
    StateMachine_TrainTrackElementChanged,
    StateMachine_SignalAllowedSpeedChanged,
    StateMachine_TrainHeadingSpeedChanged,
    Trigger,
    StateMachine_TriggerExpression,
    Guard,
    StateMachine_GuardExpression,
    Action,
    StateMachine_ActionExpression,
    StateMachine_TurnoutDesiredDirection,
    StateMachine_RouteElement,
    StateMachine_TurnoutDirectionChanged,
    ActionExpression,
    StateMachine_ChangeTrainHeadingSpeed,
    StateMachine_NamedElement,
    State,
    StateMachine_CompositeState,
    GuardExpression,
    StateMachine_TurnoutCurrentDirection,
    StateMachine_TurnoutHasDesiredDirection,
    StateMachine_NextTrackElementIs,
    StateMachine_SignalCurrentAllowedSpeed,
    StateMachine_TrainCurrentlyStandsOn,
    StateMachine_TrainCurrentHeadingSpeed,
    StateMachine_TrackElement,
    StateMachine_ChangeTrainCurrentTrackElement,
    StateMachine_Turnout,
    StateMachine_ChangeTurnoutDirection,
    StateMachine_Signal,
    StateMachine_ChangeSignalAllowedSpeed,
    StateMachine_Train,
    StateMachine_RDMElement,
    NamedElement,
    StateMachine_State,
    StateMachine_Action,
    StateMachine_Trigger,
    StateMachine_Transition,
    StateMachine_Guard,
    StateMachine_StateMachine,
    StateMachine_StateMachineBehavioralModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(TriggerExpression)


def test_triggerexpression_constructor_exists():
    assert callable(TriggerExpression.__init__)


def test_triggerexpression_constructor_args():
    sig = inspect.signature(TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_traintrackelementchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TrainTrackElementChanged)


def test_statemachine_traintrackelementchanged_constructor_exists():
    assert callable(StateMachine_TrainTrackElementChanged.__init__)


def test_statemachine_traintrackelementchanged_constructor_args():
    sig = inspect.signature(StateMachine_TrainTrackElementChanged.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_signalallowedspeedchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine_SignalAllowedSpeedChanged)


def test_statemachine_signalallowedspeedchanged_constructor_exists():
    assert callable(StateMachine_SignalAllowedSpeedChanged.__init__)


def test_statemachine_signalallowedspeedchanged_constructor_args():
    sig = inspect.signature(StateMachine_SignalAllowedSpeedChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newAllowedSpeed" in params, "Missing parameter 'newAllowedSpeed'"

def test_statemachine_signalallowedspeedchanged_has_newAllowedSpeed():
    assert hasattr(StateMachine_SignalAllowedSpeedChanged, "newAllowedSpeed")
    descriptor = None
    for klass in StateMachine_SignalAllowedSpeedChanged.__mro__:
        if "newAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_trainheadingspeedchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TrainHeadingSpeedChanged)


def test_statemachine_trainheadingspeedchanged_constructor_exists():
    assert callable(StateMachine_TrainHeadingSpeedChanged.__init__)


def test_statemachine_trainheadingspeedchanged_constructor_args():
    sig = inspect.signature(StateMachine_TrainHeadingSpeedChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newHeadingSpeed" in params, "Missing parameter 'newHeadingSpeed'"

def test_statemachine_trainheadingspeedchanged_has_newHeadingSpeed():
    assert hasattr(StateMachine_TrainHeadingSpeedChanged, "newHeadingSpeed")
    descriptor = None
    for klass in StateMachine_TrainHeadingSpeedChanged.__mro__:
        if "newHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TriggerExpression)


def test_statemachine_triggerexpression_constructor_exists():
    assert callable(StateMachine_TriggerExpression.__init__)


def test_statemachine_triggerexpression_constructor_args():
    sig = inspect.signature(StateMachine_TriggerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine_triggerexpression_has_expression():
    assert hasattr(StateMachine_TriggerExpression, "expression")
    descriptor = None
    for klass in StateMachine_TriggerExpression.__mro__:
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



def test_statemachine_guardexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine_GuardExpression)


def test_statemachine_guardexpression_constructor_exists():
    assert callable(StateMachine_GuardExpression.__init__)


def test_statemachine_guardexpression_constructor_args():
    sig = inspect.signature(StateMachine_GuardExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine_guardexpression_has_expression():
    assert hasattr(StateMachine_GuardExpression, "expression")
    descriptor = None
    for klass in StateMachine_GuardExpression.__mro__:
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



def test_statemachine_actionexpression_is_not_abstract():
    assert not inspect.isabstract(StateMachine_ActionExpression)


def test_statemachine_actionexpression_constructor_exists():
    assert callable(StateMachine_ActionExpression.__init__)


def test_statemachine_actionexpression_constructor_args():
    sig = inspect.signature(StateMachine_ActionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_statemachine_actionexpression_has_expression():
    assert hasattr(StateMachine_ActionExpression, "expression")
    descriptor = None
    for klass in StateMachine_ActionExpression.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_turnoutdesireddirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TurnoutDesiredDirection)


def test_statemachine_turnoutdesireddirection_constructor_exists():
    assert callable(StateMachine_TurnoutDesiredDirection.__init__)


def test_statemachine_turnoutdesireddirection_constructor_args():
    sig = inspect.signature(StateMachine_TurnoutDesiredDirection.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_routeelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine_RouteElement)


def test_statemachine_routeelement_constructor_exists():
    assert callable(StateMachine_RouteElement.__init__)


def test_statemachine_routeelement_constructor_args():
    sig = inspect.signature(StateMachine_RouteElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_turnoutdirectionchanged_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TurnoutDirectionChanged)


def test_statemachine_turnoutdirectionchanged_constructor_exists():
    assert callable(StateMachine_TurnoutDirectionChanged.__init__)


def test_statemachine_turnoutdirectionchanged_constructor_args():
    sig = inspect.signature(StateMachine_TurnoutDirectionChanged.__init__)
    params = list(sig.parameters.keys())
    assert "newTurnoutDirection" in params, "Missing parameter 'newTurnoutDirection'"

def test_statemachine_turnoutdirectionchanged_has_newTurnoutDirection():
    assert hasattr(StateMachine_TurnoutDirectionChanged, "newTurnoutDirection")
    descriptor = None
    for klass in StateMachine_TurnoutDirectionChanged.__mro__:
        if "newTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["newTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_actionexpression_is_not_abstract():
    assert not inspect.isabstract(ActionExpression)


def test_actionexpression_constructor_exists():
    assert callable(ActionExpression.__init__)


def test_actionexpression_constructor_args():
    sig = inspect.signature(ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_changetrainheadingspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine_ChangeTrainHeadingSpeed)


def test_statemachine_changetrainheadingspeed_constructor_exists():
    assert callable(StateMachine_ChangeTrainHeadingSpeed.__init__)


def test_statemachine_changetrainheadingspeed_constructor_args():
    sig = inspect.signature(StateMachine_ChangeTrainHeadingSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "newHeadingSpeed" in params, "Missing parameter 'newHeadingSpeed'"

def test_statemachine_changetrainheadingspeed_has_newHeadingSpeed():
    assert hasattr(StateMachine_ChangeTrainHeadingSpeed, "newHeadingSpeed")
    descriptor = None
    for klass in StateMachine_ChangeTrainHeadingSpeed.__mro__:
        if "newHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_namedelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine_NamedElement)


def test_statemachine_namedelement_constructor_exists():
    assert callable(StateMachine_NamedElement.__init__)


def test_statemachine_namedelement_constructor_args():
    sig = inspect.signature(StateMachine_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_namedelement_has_name():
    assert hasattr(StateMachine_NamedElement, "name")
    descriptor = None
    for klass in StateMachine_NamedElement.__mro__:
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



def test_statemachine_compositestate_is_not_abstract():
    assert not inspect.isabstract(StateMachine_CompositeState)


def test_statemachine_compositestate_constructor_exists():
    assert callable(StateMachine_CompositeState.__init__)


def test_statemachine_compositestate_constructor_args():
    sig = inspect.signature(StateMachine_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_guardexpression_is_not_abstract():
    assert not inspect.isabstract(GuardExpression)


def test_guardexpression_constructor_exists():
    assert callable(GuardExpression.__init__)


def test_guardexpression_constructor_args():
    sig = inspect.signature(GuardExpression.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_turnoutcurrentdirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TurnoutCurrentDirection)


def test_statemachine_turnoutcurrentdirection_constructor_exists():
    assert callable(StateMachine_TurnoutCurrentDirection.__init__)


def test_statemachine_turnoutcurrentdirection_constructor_args():
    sig = inspect.signature(StateMachine_TurnoutCurrentDirection.__init__)
    params = list(sig.parameters.keys())
    assert "currentTurnoutDirection" in params, "Missing parameter 'currentTurnoutDirection'"

def test_statemachine_turnoutcurrentdirection_has_currentTurnoutDirection():
    assert hasattr(StateMachine_TurnoutCurrentDirection, "currentTurnoutDirection")
    descriptor = None
    for klass in StateMachine_TurnoutCurrentDirection.__mro__:
        if "currentTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["currentTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_turnouthasdesireddirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TurnoutHasDesiredDirection)


def test_statemachine_turnouthasdesireddirection_constructor_exists():
    assert callable(StateMachine_TurnoutHasDesiredDirection.__init__)


def test_statemachine_turnouthasdesireddirection_constructor_args():
    sig = inspect.signature(StateMachine_TurnoutHasDesiredDirection.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_nexttrackelementis_is_not_abstract():
    assert not inspect.isabstract(StateMachine_NextTrackElementIs)


def test_statemachine_nexttrackelementis_constructor_exists():
    assert callable(StateMachine_NextTrackElementIs.__init__)


def test_statemachine_nexttrackelementis_constructor_args():
    sig = inspect.signature(StateMachine_NextTrackElementIs.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_signalcurrentallowedspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine_SignalCurrentAllowedSpeed)


def test_statemachine_signalcurrentallowedspeed_constructor_exists():
    assert callable(StateMachine_SignalCurrentAllowedSpeed.__init__)


def test_statemachine_signalcurrentallowedspeed_constructor_args():
    sig = inspect.signature(StateMachine_SignalCurrentAllowedSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "currentAllowedSpeed" in params, "Missing parameter 'currentAllowedSpeed'"

def test_statemachine_signalcurrentallowedspeed_has_currentAllowedSpeed():
    assert hasattr(StateMachine_SignalCurrentAllowedSpeed, "currentAllowedSpeed")
    descriptor = None
    for klass in StateMachine_SignalCurrentAllowedSpeed.__mro__:
        if "currentAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["currentAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_traincurrentlystandson_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TrainCurrentlyStandsOn)


def test_statemachine_traincurrentlystandson_constructor_exists():
    assert callable(StateMachine_TrainCurrentlyStandsOn.__init__)


def test_statemachine_traincurrentlystandson_constructor_args():
    sig = inspect.signature(StateMachine_TrainCurrentlyStandsOn.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_traincurrentheadingspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TrainCurrentHeadingSpeed)


def test_statemachine_traincurrentheadingspeed_constructor_exists():
    assert callable(StateMachine_TrainCurrentHeadingSpeed.__init__)


def test_statemachine_traincurrentheadingspeed_constructor_args():
    sig = inspect.signature(StateMachine_TrainCurrentHeadingSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "currentHeadingSpeed" in params, "Missing parameter 'currentHeadingSpeed'"

def test_statemachine_traincurrentheadingspeed_has_currentHeadingSpeed():
    assert hasattr(StateMachine_TrainCurrentHeadingSpeed, "currentHeadingSpeed")
    descriptor = None
    for klass in StateMachine_TrainCurrentHeadingSpeed.__mro__:
        if "currentHeadingSpeed" in klass.__dict__:
            descriptor = klass.__dict__["currentHeadingSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_trackelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine_TrackElement)


def test_statemachine_trackelement_constructor_exists():
    assert callable(StateMachine_TrackElement.__init__)


def test_statemachine_trackelement_constructor_args():
    sig = inspect.signature(StateMachine_TrackElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_changetraincurrenttrackelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine_ChangeTrainCurrentTrackElement)


def test_statemachine_changetraincurrenttrackelement_constructor_exists():
    assert callable(StateMachine_ChangeTrainCurrentTrackElement.__init__)


def test_statemachine_changetraincurrenttrackelement_constructor_args():
    sig = inspect.signature(StateMachine_ChangeTrainCurrentTrackElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_turnout_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Turnout)


def test_statemachine_turnout_constructor_exists():
    assert callable(StateMachine_Turnout.__init__)


def test_statemachine_turnout_constructor_args():
    sig = inspect.signature(StateMachine_Turnout.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_changeturnoutdirection_is_not_abstract():
    assert not inspect.isabstract(StateMachine_ChangeTurnoutDirection)


def test_statemachine_changeturnoutdirection_constructor_exists():
    assert callable(StateMachine_ChangeTurnoutDirection.__init__)


def test_statemachine_changeturnoutdirection_constructor_args():
    sig = inspect.signature(StateMachine_ChangeTurnoutDirection.__init__)
    params = list(sig.parameters.keys())
    assert "newTurnoutDirection" in params, "Missing parameter 'newTurnoutDirection'"

def test_statemachine_changeturnoutdirection_has_newTurnoutDirection():
    assert hasattr(StateMachine_ChangeTurnoutDirection, "newTurnoutDirection")
    descriptor = None
    for klass in StateMachine_ChangeTurnoutDirection.__mro__:
        if "newTurnoutDirection" in klass.__dict__:
            descriptor = klass.__dict__["newTurnoutDirection"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_signal_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Signal)


def test_statemachine_signal_constructor_exists():
    assert callable(StateMachine_Signal.__init__)


def test_statemachine_signal_constructor_args():
    sig = inspect.signature(StateMachine_Signal.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_changesignalallowedspeed_is_not_abstract():
    assert not inspect.isabstract(StateMachine_ChangeSignalAllowedSpeed)


def test_statemachine_changesignalallowedspeed_constructor_exists():
    assert callable(StateMachine_ChangeSignalAllowedSpeed.__init__)


def test_statemachine_changesignalallowedspeed_constructor_args():
    sig = inspect.signature(StateMachine_ChangeSignalAllowedSpeed.__init__)
    params = list(sig.parameters.keys())
    assert "newAllowedSpeed" in params, "Missing parameter 'newAllowedSpeed'"

def test_statemachine_changesignalallowedspeed_has_newAllowedSpeed():
    assert hasattr(StateMachine_ChangeSignalAllowedSpeed, "newAllowedSpeed")
    descriptor = None
    for klass in StateMachine_ChangeSignalAllowedSpeed.__mro__:
        if "newAllowedSpeed" in klass.__dict__:
            descriptor = klass.__dict__["newAllowedSpeed"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_train_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Train)


def test_statemachine_train_constructor_exists():
    assert callable(StateMachine_Train.__init__)


def test_statemachine_train_constructor_args():
    sig = inspect.signature(StateMachine_Train.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_rdmelement_is_not_abstract():
    assert not inspect.isabstract(StateMachine_RDMElement)


def test_statemachine_rdmelement_constructor_exists():
    assert callable(StateMachine_RDMElement.__init__)


def test_statemachine_rdmelement_constructor_args():
    sig = inspect.signature(StateMachine_RDMElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(StateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(StateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(StateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_statemachine_state_has_isInitial():
    assert hasattr(StateMachine_State, "isInitial")
    descriptor = None
    for klass in StateMachine_State.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_state_has_isActive():
    assert hasattr(StateMachine_State, "isActive")
    descriptor = None
    for klass in StateMachine_State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Action)


def test_statemachine_action_constructor_exists():
    assert callable(StateMachine_Action.__init__)


def test_statemachine_action_constructor_args():
    sig = inspect.signature(StateMachine_Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_trigger_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Trigger)


def test_statemachine_trigger_constructor_exists():
    assert callable(StateMachine_Trigger.__init__)


def test_statemachine_trigger_constructor_args():
    sig = inspect.signature(StateMachine_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(StateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(StateMachine_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "isEnabled" in params, "Missing parameter 'isEnabled'"
    assert "isFireable" in params, "Missing parameter 'isFireable'"

def test_statemachine_transition_has_isEnabled():
    assert hasattr(StateMachine_Transition, "isEnabled")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "isEnabled" in klass.__dict__:
            descriptor = klass.__dict__["isEnabled"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_transition_has_isFireable():
    assert hasattr(StateMachine_Transition, "isFireable")
    descriptor = None
    for klass in StateMachine_Transition.__mro__:
        if "isFireable" in klass.__dict__:
            descriptor = klass.__dict__["isFireable"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_guard_is_not_abstract():
    assert not inspect.isabstract(StateMachine_Guard)


def test_statemachine_guard_constructor_exists():
    assert callable(StateMachine_Guard.__init__)


def test_statemachine_guard_constructor_args():
    sig = inspect.signature(StateMachine_Guard.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(StateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(StateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachinebehavioralmodel_is_not_abstract():
    assert not inspect.isabstract(StateMachine_StateMachineBehavioralModel)


def test_statemachine_statemachinebehavioralmodel_constructor_exists():
    assert callable(StateMachine_StateMachineBehavioralModel.__init__)


def test_statemachine_statemachinebehavioralmodel_constructor_args():
    sig = inspect.signature(StateMachine_StateMachineBehavioralModel.__init__)
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
TriggerExpression_strategy = st.builds(
    TriggerExpression,
)
StateMachine_TrainTrackElementChanged_strategy = st.builds(
    StateMachine_TrainTrackElementChanged,
)
StateMachine_SignalAllowedSpeedChanged_strategy = st.builds(
    StateMachine_SignalAllowedSpeedChanged,
    newAllowedSpeed=
        safe_text
)
StateMachine_TrainHeadingSpeedChanged_strategy = st.builds(
    StateMachine_TrainHeadingSpeedChanged,
    newHeadingSpeed=
        safe_text
)
Trigger_strategy = st.builds(
    Trigger,
)
StateMachine_TriggerExpression_strategy = st.builds(
    StateMachine_TriggerExpression,
    expression=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
StateMachine_GuardExpression_strategy = st.builds(
    StateMachine_GuardExpression,
    expression=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
StateMachine_ActionExpression_strategy = st.builds(
    StateMachine_ActionExpression,
    expression=
        safe_text
)
StateMachine_TurnoutDesiredDirection_strategy = st.builds(
    StateMachine_TurnoutDesiredDirection,
)
StateMachine_RouteElement_strategy = st.builds(
    StateMachine_RouteElement,
)
StateMachine_TurnoutDirectionChanged_strategy = st.builds(
    StateMachine_TurnoutDirectionChanged,
    newTurnoutDirection=
        safe_text
)
ActionExpression_strategy = st.builds(
    ActionExpression,
)
StateMachine_ChangeTrainHeadingSpeed_strategy = st.builds(
    StateMachine_ChangeTrainHeadingSpeed,
    newHeadingSpeed=
        safe_text
)
StateMachine_NamedElement_strategy = st.builds(
    StateMachine_NamedElement,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
StateMachine_CompositeState_strategy = st.builds(
    StateMachine_CompositeState,
)
GuardExpression_strategy = st.builds(
    GuardExpression,
)
StateMachine_TurnoutCurrentDirection_strategy = st.builds(
    StateMachine_TurnoutCurrentDirection,
    currentTurnoutDirection=
        safe_text
)
StateMachine_TurnoutHasDesiredDirection_strategy = st.builds(
    StateMachine_TurnoutHasDesiredDirection,
)
StateMachine_NextTrackElementIs_strategy = st.builds(
    StateMachine_NextTrackElementIs,
)
StateMachine_SignalCurrentAllowedSpeed_strategy = st.builds(
    StateMachine_SignalCurrentAllowedSpeed,
    currentAllowedSpeed=
        safe_text
)
StateMachine_TrainCurrentlyStandsOn_strategy = st.builds(
    StateMachine_TrainCurrentlyStandsOn,
)
StateMachine_TrainCurrentHeadingSpeed_strategy = st.builds(
    StateMachine_TrainCurrentHeadingSpeed,
    currentHeadingSpeed=
        safe_text
)
StateMachine_TrackElement_strategy = st.builds(
    StateMachine_TrackElement,
)
StateMachine_ChangeTrainCurrentTrackElement_strategy = st.builds(
    StateMachine_ChangeTrainCurrentTrackElement,
)
StateMachine_Turnout_strategy = st.builds(
    StateMachine_Turnout,
)
StateMachine_ChangeTurnoutDirection_strategy = st.builds(
    StateMachine_ChangeTurnoutDirection,
    newTurnoutDirection=
        safe_text
)
StateMachine_Signal_strategy = st.builds(
    StateMachine_Signal,
)
StateMachine_ChangeSignalAllowedSpeed_strategy = st.builds(
    StateMachine_ChangeSignalAllowedSpeed,
    newAllowedSpeed=
        safe_text
)
StateMachine_Train_strategy = st.builds(
    StateMachine_Train,
)
StateMachine_RDMElement_strategy = st.builds(
    StateMachine_RDMElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
StateMachine_State_strategy = st.builds(
    StateMachine_State,
    isInitial=
        st.booleans(),
    isActive=
        st.booleans()
)
StateMachine_Action_strategy = st.builds(
    StateMachine_Action,
)
StateMachine_Trigger_strategy = st.builds(
    StateMachine_Trigger,
)
StateMachine_Transition_strategy = st.builds(
    StateMachine_Transition,
    isEnabled=
        st.booleans(),
    isFireable=
        st.booleans()
)
StateMachine_Guard_strategy = st.builds(
    StateMachine_Guard,
)
StateMachine_StateMachine_strategy = st.builds(
    StateMachine_StateMachine,
)
StateMachine_StateMachineBehavioralModel_strategy = st.builds(
    StateMachine_StateMachineBehavioralModel,
)

@given(instance=TriggerExpression_strategy)
@settings(max_examples=50)
def test_triggerexpression_instantiation(instance):
    assert isinstance(instance, TriggerExpression)

@given(instance=StateMachine_TrainTrackElementChanged_strategy)
@settings(max_examples=50)
def test_statemachine_traintrackelementchanged_instantiation(instance):
    assert isinstance(instance, StateMachine_TrainTrackElementChanged)

@given(instance=StateMachine_SignalAllowedSpeedChanged_strategy)
@settings(max_examples=50)
def test_statemachine_signalallowedspeedchanged_instantiation(instance):
    assert isinstance(instance, StateMachine_SignalAllowedSpeedChanged)



@given(instance=StateMachine_SignalAllowedSpeedChanged_strategy)
def test_statemachine_signalallowedspeedchanged_newAllowedSpeed_setter(instance):
    original = instance.newAllowedSpeed
    instance.newAllowedSpeed = original
    assert instance.newAllowedSpeed == original

@given(instance=StateMachine_TrainHeadingSpeedChanged_strategy)
@settings(max_examples=50)
def test_statemachine_trainheadingspeedchanged_instantiation(instance):
    assert isinstance(instance, StateMachine_TrainHeadingSpeedChanged)



@given(instance=StateMachine_TrainHeadingSpeedChanged_strategy)
def test_statemachine_trainheadingspeedchanged_newHeadingSpeed_setter(instance):
    original = instance.newHeadingSpeed
    instance.newHeadingSpeed = original
    assert instance.newHeadingSpeed == original

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=StateMachine_TriggerExpression_strategy)
@settings(max_examples=50)
def test_statemachine_triggerexpression_instantiation(instance):
    assert isinstance(instance, StateMachine_TriggerExpression)



@given(instance=StateMachine_TriggerExpression_strategy)
def test_statemachine_triggerexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=StateMachine_GuardExpression_strategy)
@settings(max_examples=50)
def test_statemachine_guardexpression_instantiation(instance):
    assert isinstance(instance, StateMachine_GuardExpression)



@given(instance=StateMachine_GuardExpression_strategy)
def test_statemachine_guardexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=StateMachine_ActionExpression_strategy)
@settings(max_examples=50)
def test_statemachine_actionexpression_instantiation(instance):
    assert isinstance(instance, StateMachine_ActionExpression)



@given(instance=StateMachine_ActionExpression_strategy)
def test_statemachine_actionexpression_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=StateMachine_TurnoutDesiredDirection_strategy)
@settings(max_examples=50)
def test_statemachine_turnoutdesireddirection_instantiation(instance):
    assert isinstance(instance, StateMachine_TurnoutDesiredDirection)

@given(instance=StateMachine_RouteElement_strategy)
@settings(max_examples=50)
def test_statemachine_routeelement_instantiation(instance):
    assert isinstance(instance, StateMachine_RouteElement)

@given(instance=StateMachine_TurnoutDirectionChanged_strategy)
@settings(max_examples=50)
def test_statemachine_turnoutdirectionchanged_instantiation(instance):
    assert isinstance(instance, StateMachine_TurnoutDirectionChanged)



@given(instance=StateMachine_TurnoutDirectionChanged_strategy)
def test_statemachine_turnoutdirectionchanged_newTurnoutDirection_setter(instance):
    original = instance.newTurnoutDirection
    instance.newTurnoutDirection = original
    assert instance.newTurnoutDirection == original

@given(instance=ActionExpression_strategy)
@settings(max_examples=50)
def test_actionexpression_instantiation(instance):
    assert isinstance(instance, ActionExpression)

@given(instance=StateMachine_ChangeTrainHeadingSpeed_strategy)
@settings(max_examples=50)
def test_statemachine_changetrainheadingspeed_instantiation(instance):
    assert isinstance(instance, StateMachine_ChangeTrainHeadingSpeed)



@given(instance=StateMachine_ChangeTrainHeadingSpeed_strategy)
def test_statemachine_changetrainheadingspeed_newHeadingSpeed_setter(instance):
    original = instance.newHeadingSpeed
    instance.newHeadingSpeed = original
    assert instance.newHeadingSpeed == original

@given(instance=StateMachine_NamedElement_strategy)
@settings(max_examples=50)
def test_statemachine_namedelement_instantiation(instance):
    assert isinstance(instance, StateMachine_NamedElement)



@given(instance=StateMachine_NamedElement_strategy)
def test_statemachine_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachine_CompositeState_strategy)
@settings(max_examples=50)
def test_statemachine_compositestate_instantiation(instance):
    assert isinstance(instance, StateMachine_CompositeState)

@given(instance=GuardExpression_strategy)
@settings(max_examples=50)
def test_guardexpression_instantiation(instance):
    assert isinstance(instance, GuardExpression)

@given(instance=StateMachine_TurnoutCurrentDirection_strategy)
@settings(max_examples=50)
def test_statemachine_turnoutcurrentdirection_instantiation(instance):
    assert isinstance(instance, StateMachine_TurnoutCurrentDirection)



@given(instance=StateMachine_TurnoutCurrentDirection_strategy)
def test_statemachine_turnoutcurrentdirection_currentTurnoutDirection_setter(instance):
    original = instance.currentTurnoutDirection
    instance.currentTurnoutDirection = original
    assert instance.currentTurnoutDirection == original

@given(instance=StateMachine_TurnoutHasDesiredDirection_strategy)
@settings(max_examples=50)
def test_statemachine_turnouthasdesireddirection_instantiation(instance):
    assert isinstance(instance, StateMachine_TurnoutHasDesiredDirection)

@given(instance=StateMachine_NextTrackElementIs_strategy)
@settings(max_examples=50)
def test_statemachine_nexttrackelementis_instantiation(instance):
    assert isinstance(instance, StateMachine_NextTrackElementIs)

@given(instance=StateMachine_SignalCurrentAllowedSpeed_strategy)
@settings(max_examples=50)
def test_statemachine_signalcurrentallowedspeed_instantiation(instance):
    assert isinstance(instance, StateMachine_SignalCurrentAllowedSpeed)



@given(instance=StateMachine_SignalCurrentAllowedSpeed_strategy)
def test_statemachine_signalcurrentallowedspeed_currentAllowedSpeed_setter(instance):
    original = instance.currentAllowedSpeed
    instance.currentAllowedSpeed = original
    assert instance.currentAllowedSpeed == original

@given(instance=StateMachine_TrainCurrentlyStandsOn_strategy)
@settings(max_examples=50)
def test_statemachine_traincurrentlystandson_instantiation(instance):
    assert isinstance(instance, StateMachine_TrainCurrentlyStandsOn)

@given(instance=StateMachine_TrainCurrentHeadingSpeed_strategy)
@settings(max_examples=50)
def test_statemachine_traincurrentheadingspeed_instantiation(instance):
    assert isinstance(instance, StateMachine_TrainCurrentHeadingSpeed)



@given(instance=StateMachine_TrainCurrentHeadingSpeed_strategy)
def test_statemachine_traincurrentheadingspeed_currentHeadingSpeed_setter(instance):
    original = instance.currentHeadingSpeed
    instance.currentHeadingSpeed = original
    assert instance.currentHeadingSpeed == original

@given(instance=StateMachine_TrackElement_strategy)
@settings(max_examples=50)
def test_statemachine_trackelement_instantiation(instance):
    assert isinstance(instance, StateMachine_TrackElement)

@given(instance=StateMachine_ChangeTrainCurrentTrackElement_strategy)
@settings(max_examples=50)
def test_statemachine_changetraincurrenttrackelement_instantiation(instance):
    assert isinstance(instance, StateMachine_ChangeTrainCurrentTrackElement)

@given(instance=StateMachine_Turnout_strategy)
@settings(max_examples=50)
def test_statemachine_turnout_instantiation(instance):
    assert isinstance(instance, StateMachine_Turnout)

@given(instance=StateMachine_ChangeTurnoutDirection_strategy)
@settings(max_examples=50)
def test_statemachine_changeturnoutdirection_instantiation(instance):
    assert isinstance(instance, StateMachine_ChangeTurnoutDirection)



@given(instance=StateMachine_ChangeTurnoutDirection_strategy)
def test_statemachine_changeturnoutdirection_newTurnoutDirection_setter(instance):
    original = instance.newTurnoutDirection
    instance.newTurnoutDirection = original
    assert instance.newTurnoutDirection == original

@given(instance=StateMachine_Signal_strategy)
@settings(max_examples=50)
def test_statemachine_signal_instantiation(instance):
    assert isinstance(instance, StateMachine_Signal)

@given(instance=StateMachine_ChangeSignalAllowedSpeed_strategy)
@settings(max_examples=50)
def test_statemachine_changesignalallowedspeed_instantiation(instance):
    assert isinstance(instance, StateMachine_ChangeSignalAllowedSpeed)



@given(instance=StateMachine_ChangeSignalAllowedSpeed_strategy)
def test_statemachine_changesignalallowedspeed_newAllowedSpeed_setter(instance):
    original = instance.newAllowedSpeed
    instance.newAllowedSpeed = original
    assert instance.newAllowedSpeed == original

@given(instance=StateMachine_Train_strategy)
@settings(max_examples=50)
def test_statemachine_train_instantiation(instance):
    assert isinstance(instance, StateMachine_Train)

@given(instance=StateMachine_RDMElement_strategy)
@settings(max_examples=50)
def test_statemachine_rdmelement_instantiation(instance):
    assert isinstance(instance, StateMachine_RDMElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=StateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, StateMachine_State)



@given(instance=StateMachine_State_strategy)
def test_statemachine_state_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=StateMachine_State_strategy)
def test_statemachine_state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=StateMachine_Action_strategy)
@settings(max_examples=50)
def test_statemachine_action_instantiation(instance):
    assert isinstance(instance, StateMachine_Action)

@given(instance=StateMachine_Trigger_strategy)
@settings(max_examples=50)
def test_statemachine_trigger_instantiation(instance):
    assert isinstance(instance, StateMachine_Trigger)

@given(instance=StateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, StateMachine_Transition)



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_isEnabled_setter(instance):
    original = instance.isEnabled
    instance.isEnabled = original
    assert instance.isEnabled == original



@given(instance=StateMachine_Transition_strategy)
def test_statemachine_transition_isFireable_setter(instance):
    original = instance.isFireable
    instance.isFireable = original
    assert instance.isFireable == original

@given(instance=StateMachine_Guard_strategy)
@settings(max_examples=50)
def test_statemachine_guard_instantiation(instance):
    assert isinstance(instance, StateMachine_Guard)

@given(instance=StateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine_StateMachine)

@given(instance=StateMachine_StateMachineBehavioralModel_strategy)
@settings(max_examples=50)
def test_statemachine_statemachinebehavioralmodel_instantiation(instance):
    assert isinstance(instance, StateMachine_StateMachineBehavioralModel)
