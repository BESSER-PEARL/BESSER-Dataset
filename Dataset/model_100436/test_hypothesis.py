import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    stateMachine::Branch,
    Branch,
    stateMachine::Otherwise,
    stateMachine::Key,
    Transition,
    stateMachine::NoneEvent,
    stateMachine::SMSReceived,
    stateMachine::Timer,
    stateMachine::IVREvent,
    IVREvent,
    stateMachine::Init,
    stateMachine::CollectTimeout,
    stateMachine::Managed,
    stateMachine::Collected,
    stateMachine::Recorderd,
    stateMachine::Terminated,
    stateMachine::Call,
    stateMachine::PickUp,
    stateMachine::Played,
    stateMachine::Cancel,
    stateMachine::Bye,
    Play,
    stateMachine::PlayRecord,
    stateMachine::PlayCollect,
    stateMachine::SMS,
    stateMachine::Action,
    State,
    stateMachine::CompositeState,
    stateMachine::FinalState,
    stateMachine::InitialState,
    IvrAction,
    stateMachine::RemoveRecord,
    stateMachine::NewCall,
    stateMachine::Play,
    stateMachine::Terminate,
    stateMachine::HangUp,
    Action,
    stateMachine::SetTimer,
    stateMachine::SendSms,
    stateMachine::IvrAction,
    stateMachine::Transition,
    stateMachine::State,
    stateMachine::StateMachine,
    stateMachine::Properties,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachine::branch_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Branch)


def test_statemachine::branch_constructor_exists():
    assert callable(stateMachine::Branch.__init__)


def test_statemachine::branch_constructor_args():
    sig = inspect.signature(stateMachine::Branch.__init__)
    params = list(sig.parameters.keys())



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::otherwise_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Otherwise)


def test_statemachine::otherwise_constructor_exists():
    assert callable(stateMachine::Otherwise.__init__)


def test_statemachine::otherwise_constructor_args():
    sig = inspect.signature(stateMachine::Otherwise.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::key_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Key)


def test_statemachine::key_constructor_exists():
    assert callable(stateMachine::Key.__init__)


def test_statemachine::key_constructor_args():
    sig = inspect.signature(stateMachine::Key.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_statemachine::key_has_key():
    assert hasattr(stateMachine::Key, "key")
    descriptor = None
    for klass in stateMachine::Key.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::noneevent_is_not_abstract():
    assert not inspect.isabstract(stateMachine::NoneEvent)


def test_statemachine::noneevent_constructor_exists():
    assert callable(stateMachine::NoneEvent.__init__)


def test_statemachine::noneevent_constructor_args():
    sig = inspect.signature(stateMachine::NoneEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::smsreceived_is_not_abstract():
    assert not inspect.isabstract(stateMachine::SMSReceived)


def test_statemachine::smsreceived_constructor_exists():
    assert callable(stateMachine::SMSReceived.__init__)


def test_statemachine::smsreceived_constructor_args():
    sig = inspect.signature(stateMachine::SMSReceived.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::timer_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Timer)


def test_statemachine::timer_constructor_exists():
    assert callable(stateMachine::Timer.__init__)


def test_statemachine::timer_constructor_args():
    sig = inspect.signature(stateMachine::Timer.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::ivrevent_is_not_abstract():
    assert not inspect.isabstract(stateMachine::IVREvent)


def test_statemachine::ivrevent_constructor_exists():
    assert callable(stateMachine::IVREvent.__init__)


def test_statemachine::ivrevent_constructor_args():
    sig = inspect.signature(stateMachine::IVREvent.__init__)
    params = list(sig.parameters.keys())



def test_ivrevent_is_not_abstract():
    assert not inspect.isabstract(IVREvent)


def test_ivrevent_constructor_exists():
    assert callable(IVREvent.__init__)


def test_ivrevent_constructor_args():
    sig = inspect.signature(IVREvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::init_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Init)


def test_statemachine::init_constructor_exists():
    assert callable(stateMachine::Init.__init__)


def test_statemachine::init_constructor_args():
    sig = inspect.signature(stateMachine::Init.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::collecttimeout_is_not_abstract():
    assert not inspect.isabstract(stateMachine::CollectTimeout)


def test_statemachine::collecttimeout_constructor_exists():
    assert callable(stateMachine::CollectTimeout.__init__)


def test_statemachine::collecttimeout_constructor_args():
    sig = inspect.signature(stateMachine::CollectTimeout.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::managed_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Managed)


def test_statemachine::managed_constructor_exists():
    assert callable(stateMachine::Managed.__init__)


def test_statemachine::managed_constructor_args():
    sig = inspect.signature(stateMachine::Managed.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "success" in params, "Missing parameter 'success'"

def test_statemachine::managed_has_code():
    assert hasattr(stateMachine::Managed, "code")
    descriptor = None
    for klass in stateMachine::Managed.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::managed_has_success():
    assert hasattr(stateMachine::Managed, "success")
    descriptor = None
    for klass in stateMachine::Managed.__mro__:
        if "success" in klass.__dict__:
            descriptor = klass.__dict__["success"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::collected_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Collected)


def test_statemachine::collected_constructor_exists():
    assert callable(stateMachine::Collected.__init__)


def test_statemachine::collected_constructor_args():
    sig = inspect.signature(stateMachine::Collected.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::recorderd_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Recorderd)


def test_statemachine::recorderd_constructor_exists():
    assert callable(stateMachine::Recorderd.__init__)


def test_statemachine::recorderd_constructor_args():
    sig = inspect.signature(stateMachine::Recorderd.__init__)
    params = list(sig.parameters.keys())
    assert "recordId" in params, "Missing parameter 'recordId'"

def test_statemachine::recorderd_has_recordId():
    assert hasattr(stateMachine::Recorderd, "recordId")
    descriptor = None
    for klass in stateMachine::Recorderd.__mro__:
        if "recordId" in klass.__dict__:
            descriptor = klass.__dict__["recordId"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::terminated_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Terminated)


def test_statemachine::terminated_constructor_exists():
    assert callable(stateMachine::Terminated.__init__)


def test_statemachine::terminated_constructor_args():
    sig = inspect.signature(stateMachine::Terminated.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::call_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Call)


def test_statemachine::call_constructor_exists():
    assert callable(stateMachine::Call.__init__)


def test_statemachine::call_constructor_args():
    sig = inspect.signature(stateMachine::Call.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "to" in params, "Missing parameter 'to'"

def test_statemachine::call_has_from_():
    assert hasattr(stateMachine::Call, "from_")
    descriptor = None
    for klass in stateMachine::Call.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::call_has_to():
    assert hasattr(stateMachine::Call, "to")
    descriptor = None
    for klass in stateMachine::Call.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::pickup_is_not_abstract():
    assert not inspect.isabstract(stateMachine::PickUp)


def test_statemachine::pickup_constructor_exists():
    assert callable(stateMachine::PickUp.__init__)


def test_statemachine::pickup_constructor_args():
    sig = inspect.signature(stateMachine::PickUp.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::played_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Played)


def test_statemachine::played_constructor_exists():
    assert callable(stateMachine::Played.__init__)


def test_statemachine::played_constructor_args():
    sig = inspect.signature(stateMachine::Played.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::cancel_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Cancel)


def test_statemachine::cancel_constructor_exists():
    assert callable(stateMachine::Cancel.__init__)


def test_statemachine::cancel_constructor_args():
    sig = inspect.signature(stateMachine::Cancel.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::bye_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Bye)


def test_statemachine::bye_constructor_exists():
    assert callable(stateMachine::Bye.__init__)


def test_statemachine::bye_constructor_args():
    sig = inspect.signature(stateMachine::Bye.__init__)
    params = list(sig.parameters.keys())



def test_play_is_not_abstract():
    assert not inspect.isabstract(Play)


def test_play_constructor_exists():
    assert callable(Play.__init__)


def test_play_constructor_args():
    sig = inspect.signature(Play.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::playrecord_is_not_abstract():
    assert not inspect.isabstract(stateMachine::PlayRecord)


def test_statemachine::playrecord_constructor_exists():
    assert callable(stateMachine::PlayRecord.__init__)


def test_statemachine::playrecord_constructor_args():
    sig = inspect.signature(stateMachine::PlayRecord.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::playcollect_is_not_abstract():
    assert not inspect.isabstract(stateMachine::PlayCollect)


def test_statemachine::playcollect_constructor_exists():
    assert callable(stateMachine::PlayCollect.__init__)


def test_statemachine::playcollect_constructor_args():
    sig = inspect.signature(stateMachine::PlayCollect.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::sms_is_not_abstract():
    assert not inspect.isabstract(stateMachine::SMS)


def test_statemachine::sms_constructor_exists():
    assert callable(stateMachine::SMS.__init__)


def test_statemachine::sms_constructor_args():
    sig = inspect.signature(stateMachine::SMS.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"
    assert "text" in params, "Missing parameter 'text'"
    assert "to" in params, "Missing parameter 'to'"

def test_statemachine::sms_has_from_():
    assert hasattr(stateMachine::SMS, "from_")
    descriptor = None
    for klass in stateMachine::SMS.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::sms_has_text():
    assert hasattr(stateMachine::SMS, "text")
    descriptor = None
    for klass in stateMachine::SMS.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::sms_has_to():
    assert hasattr(stateMachine::SMS, "to")
    descriptor = None
    for klass in stateMachine::SMS.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::action_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Action)


def test_statemachine::action_constructor_exists():
    assert callable(stateMachine::Action.__init__)


def test_statemachine::action_constructor_args():
    sig = inspect.signature(stateMachine::Action.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::compositestate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::CompositeState)


def test_statemachine::compositestate_constructor_exists():
    assert callable(stateMachine::CompositeState.__init__)


def test_statemachine::compositestate_constructor_args():
    sig = inspect.signature(stateMachine::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::finalstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::FinalState)


def test_statemachine::finalstate_constructor_exists():
    assert callable(stateMachine::FinalState.__init__)


def test_statemachine::finalstate_constructor_args():
    sig = inspect.signature(stateMachine::FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::initialstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::InitialState)


def test_statemachine::initialstate_constructor_exists():
    assert callable(stateMachine::InitialState.__init__)


def test_statemachine::initialstate_constructor_args():
    sig = inspect.signature(stateMachine::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_ivraction_is_not_abstract():
    assert not inspect.isabstract(IvrAction)


def test_ivraction_constructor_exists():
    assert callable(IvrAction.__init__)


def test_ivraction_constructor_args():
    sig = inspect.signature(IvrAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::removerecord_is_not_abstract():
    assert not inspect.isabstract(stateMachine::RemoveRecord)


def test_statemachine::removerecord_constructor_exists():
    assert callable(stateMachine::RemoveRecord.__init__)


def test_statemachine::removerecord_constructor_args():
    sig = inspect.signature(stateMachine::RemoveRecord.__init__)
    params = list(sig.parameters.keys())
    assert "recordId" in params, "Missing parameter 'recordId'"

def test_statemachine::removerecord_has_recordId():
    assert hasattr(stateMachine::RemoveRecord, "recordId")
    descriptor = None
    for klass in stateMachine::RemoveRecord.__mro__:
        if "recordId" in klass.__dict__:
            descriptor = klass.__dict__["recordId"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::newcall_is_not_abstract():
    assert not inspect.isabstract(stateMachine::NewCall)


def test_statemachine::newcall_constructor_exists():
    assert callable(stateMachine::NewCall.__init__)


def test_statemachine::newcall_constructor_args():
    sig = inspect.signature(stateMachine::NewCall.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_statemachine::newcall_has_to():
    assert hasattr(stateMachine::NewCall, "to")
    descriptor = None
    for klass in stateMachine::NewCall.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::newcall_has_from_():
    assert hasattr(stateMachine::NewCall, "from_")
    descriptor = None
    for klass in stateMachine::NewCall.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::play_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Play)


def test_statemachine::play_constructor_exists():
    assert callable(stateMachine::Play.__init__)


def test_statemachine::play_constructor_args():
    sig = inspect.signature(stateMachine::Play.__init__)
    params = list(sig.parameters.keys())
    assert "mediaURI" in params, "Missing parameter 'mediaURI'"
    assert "baseURL" in params, "Missing parameter 'baseURL'"

def test_statemachine::play_has_mediaURI():
    assert hasattr(stateMachine::Play, "mediaURI")
    descriptor = None
    for klass in stateMachine::Play.__mro__:
        if "mediaURI" in klass.__dict__:
            descriptor = klass.__dict__["mediaURI"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::play_has_baseURL():
    assert hasattr(stateMachine::Play, "baseURL")
    descriptor = None
    for klass in stateMachine::Play.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::terminate_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Terminate)


def test_statemachine::terminate_constructor_exists():
    assert callable(stateMachine::Terminate.__init__)


def test_statemachine::terminate_constructor_args():
    sig = inspect.signature(stateMachine::Terminate.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::hangup_is_not_abstract():
    assert not inspect.isabstract(stateMachine::HangUp)


def test_statemachine::hangup_constructor_exists():
    assert callable(stateMachine::HangUp.__init__)


def test_statemachine::hangup_constructor_args():
    sig = inspect.signature(stateMachine::HangUp.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::settimer_is_not_abstract():
    assert not inspect.isabstract(stateMachine::SetTimer)


def test_statemachine::settimer_constructor_exists():
    assert callable(stateMachine::SetTimer.__init__)


def test_statemachine::settimer_constructor_args():
    sig = inspect.signature(stateMachine::SetTimer.__init__)
    params = list(sig.parameters.keys())
    assert "millis" in params, "Missing parameter 'millis'"

def test_statemachine::settimer_has_millis():
    assert hasattr(stateMachine::SetTimer, "millis")
    descriptor = None
    for klass in stateMachine::SetTimer.__mro__:
        if "millis" in klass.__dict__:
            descriptor = klass.__dict__["millis"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::sendsms_is_not_abstract():
    assert not inspect.isabstract(stateMachine::SendSms)


def test_statemachine::sendsms_constructor_exists():
    assert callable(stateMachine::SendSms.__init__)


def test_statemachine::sendsms_constructor_args():
    sig = inspect.signature(stateMachine::SendSms.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::ivraction_is_not_abstract():
    assert not inspect.isabstract(stateMachine::IvrAction)


def test_statemachine::ivraction_constructor_exists():
    assert callable(stateMachine::IvrAction.__init__)


def test_statemachine::ivraction_constructor_args():
    sig = inspect.signature(stateMachine::IvrAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Transition)


def test_statemachine::transition_constructor_exists():
    assert callable(stateMachine::Transition.__init__)


def test_statemachine::transition_constructor_args():
    sig = inspect.signature(stateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine::state_is_not_abstract():
    assert not inspect.isabstract(stateMachine::State)


def test_statemachine::state_constructor_exists():
    assert callable(stateMachine::State.__init__)


def test_statemachine::state_constructor_args():
    sig = inspect.signature(stateMachine::State.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_statemachine::state_has_nombre():
    assert hasattr(stateMachine::State, "nombre")
    descriptor = None
    for klass in stateMachine::State.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine::StateMachine)


def test_statemachine::statemachine_constructor_exists():
    assert callable(stateMachine::StateMachine.__init__)


def test_statemachine::statemachine_constructor_args():
    sig = inspect.signature(stateMachine::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_statemachine::statemachine_has_nombre():
    assert hasattr(stateMachine::StateMachine, "nombre")
    descriptor = None
    for klass in stateMachine::StateMachine.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_statemachine::properties_is_not_abstract():
    assert not inspect.isabstract(stateMachine::Properties)


def test_statemachine::properties_constructor_exists():
    assert callable(stateMachine::Properties.__init__)


def test_statemachine::properties_constructor_args():
    sig = inspect.signature(stateMachine::Properties.__init__)
    params = list(sig.parameters.keys())
    assert "setupConference" in params, "Missing parameter 'setupConference'"
    assert "mediaHost" in params, "Missing parameter 'mediaHost'"
    assert "recordPath" in params, "Missing parameter 'recordPath'"
    assert "mediaPort" in params, "Missing parameter 'mediaPort'"
    assert "scscfUser" in params, "Missing parameter 'scscfUser'"
    assert "applicationServerHost" in params, "Missing parameter 'applicationServerHost'"
    assert "mediaFromAddr" in params, "Missing parameter 'mediaFromAddr'"
    assert "applicationServerProtocol" in params, "Missing parameter 'applicationServerProtocol'"
    assert "scscfHost" in params, "Missing parameter 'scscfHost'"
    assert "mediaURI" in params, "Missing parameter 'mediaURI'"
    assert "mediaProtocol" in params, "Missing parameter 'mediaProtocol'"
    assert "applicationAddress" in params, "Missing parameter 'applicationAddress'"
    assert "scscfPort" in params, "Missing parameter 'scscfPort'"
    assert "mediaToAddr" in params, "Missing parameter 'mediaToAddr'"
    assert "applicationServerPort" in params, "Missing parameter 'applicationServerPort'"
    assert "scscfProtocol" in params, "Missing parameter 'scscfProtocol'"

def test_statemachine::properties_has_setupConference():
    assert hasattr(stateMachine::Properties, "setupConference")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "setupConference" in klass.__dict__:
            descriptor = klass.__dict__["setupConference"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaHost():
    assert hasattr(stateMachine::Properties, "mediaHost")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaHost" in klass.__dict__:
            descriptor = klass.__dict__["mediaHost"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_recordPath():
    assert hasattr(stateMachine::Properties, "recordPath")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "recordPath" in klass.__dict__:
            descriptor = klass.__dict__["recordPath"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaPort():
    assert hasattr(stateMachine::Properties, "mediaPort")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaPort" in klass.__dict__:
            descriptor = klass.__dict__["mediaPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_scscfUser():
    assert hasattr(stateMachine::Properties, "scscfUser")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "scscfUser" in klass.__dict__:
            descriptor = klass.__dict__["scscfUser"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_applicationServerHost():
    assert hasattr(stateMachine::Properties, "applicationServerHost")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "applicationServerHost" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerHost"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaFromAddr():
    assert hasattr(stateMachine::Properties, "mediaFromAddr")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaFromAddr" in klass.__dict__:
            descriptor = klass.__dict__["mediaFromAddr"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_applicationServerProtocol():
    assert hasattr(stateMachine::Properties, "applicationServerProtocol")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "applicationServerProtocol" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerProtocol"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_scscfHost():
    assert hasattr(stateMachine::Properties, "scscfHost")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "scscfHost" in klass.__dict__:
            descriptor = klass.__dict__["scscfHost"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaURI():
    assert hasattr(stateMachine::Properties, "mediaURI")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaURI" in klass.__dict__:
            descriptor = klass.__dict__["mediaURI"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaProtocol():
    assert hasattr(stateMachine::Properties, "mediaProtocol")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaProtocol" in klass.__dict__:
            descriptor = klass.__dict__["mediaProtocol"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_applicationAddress():
    assert hasattr(stateMachine::Properties, "applicationAddress")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "applicationAddress" in klass.__dict__:
            descriptor = klass.__dict__["applicationAddress"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_scscfPort():
    assert hasattr(stateMachine::Properties, "scscfPort")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "scscfPort" in klass.__dict__:
            descriptor = klass.__dict__["scscfPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_mediaToAddr():
    assert hasattr(stateMachine::Properties, "mediaToAddr")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "mediaToAddr" in klass.__dict__:
            descriptor = klass.__dict__["mediaToAddr"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_applicationServerPort():
    assert hasattr(stateMachine::Properties, "applicationServerPort")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "applicationServerPort" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine::properties_has_scscfProtocol():
    assert hasattr(stateMachine::Properties, "scscfProtocol")
    descriptor = None
    for klass in stateMachine::Properties.__mro__:
        if "scscfProtocol" in klass.__dict__:
            descriptor = klass.__dict__["scscfProtocol"]
            break
    assert isinstance(descriptor, property)


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
stateMachine::Branch_strategy = st.builds(
    stateMachine::Branch,
)
Branch_strategy = st.builds(
    Branch,
)
stateMachine::Otherwise_strategy = st.builds(
    stateMachine::Otherwise,
)
stateMachine::Key_strategy = st.builds(
    stateMachine::Key,
    key=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
stateMachine::NoneEvent_strategy = st.builds(
    stateMachine::NoneEvent,
)
stateMachine::SMSReceived_strategy = st.builds(
    stateMachine::SMSReceived,
)
stateMachine::Timer_strategy = st.builds(
    stateMachine::Timer,
)
stateMachine::IVREvent_strategy = st.builds(
    stateMachine::IVREvent,
)
IVREvent_strategy = st.builds(
    IVREvent,
)
stateMachine::Init_strategy = st.builds(
    stateMachine::Init,
)
stateMachine::CollectTimeout_strategy = st.builds(
    stateMachine::CollectTimeout,
)
stateMachine::Managed_strategy = st.builds(
    stateMachine::Managed,
    code=
        st.integers(),
    success=
        st.booleans()
)
stateMachine::Collected_strategy = st.builds(
    stateMachine::Collected,
)
stateMachine::Recorderd_strategy = st.builds(
    stateMachine::Recorderd,
    recordId=
        safe_text
)
stateMachine::Terminated_strategy = st.builds(
    stateMachine::Terminated,
)
stateMachine::Call_strategy = st.builds(
    stateMachine::Call,
    from_=
        safe_text,
    to=
        safe_text
)
stateMachine::PickUp_strategy = st.builds(
    stateMachine::PickUp,
)
stateMachine::Played_strategy = st.builds(
    stateMachine::Played,
)
stateMachine::Cancel_strategy = st.builds(
    stateMachine::Cancel,
)
stateMachine::Bye_strategy = st.builds(
    stateMachine::Bye,
)
Play_strategy = st.builds(
    Play,
)
stateMachine::PlayRecord_strategy = st.builds(
    stateMachine::PlayRecord,
)
stateMachine::PlayCollect_strategy = st.builds(
    stateMachine::PlayCollect,
)
stateMachine::SMS_strategy = st.builds(
    stateMachine::SMS,
    from_=
        safe_text,
    text=
        safe_text,
    to=
        safe_text
)
stateMachine::Action_strategy = st.builds(
    stateMachine::Action,
)
State_strategy = st.builds(
    State,
)
stateMachine::CompositeState_strategy = st.builds(
    stateMachine::CompositeState,
)
stateMachine::FinalState_strategy = st.builds(
    stateMachine::FinalState,
)
stateMachine::InitialState_strategy = st.builds(
    stateMachine::InitialState,
)
IvrAction_strategy = st.builds(
    IvrAction,
)
stateMachine::RemoveRecord_strategy = st.builds(
    stateMachine::RemoveRecord,
    recordId=
        safe_text
)
stateMachine::NewCall_strategy = st.builds(
    stateMachine::NewCall,
    to=
        safe_text,
    from_=
        safe_text
)
stateMachine::Play_strategy = st.builds(
    stateMachine::Play,
    mediaURI=
        safe_text,
    baseURL=
        safe_text
)
stateMachine::Terminate_strategy = st.builds(
    stateMachine::Terminate,
)
stateMachine::HangUp_strategy = st.builds(
    stateMachine::HangUp,
)
Action_strategy = st.builds(
    Action,
)
stateMachine::SetTimer_strategy = st.builds(
    stateMachine::SetTimer,
    millis=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
stateMachine::SendSms_strategy = st.builds(
    stateMachine::SendSms,
)
stateMachine::IvrAction_strategy = st.builds(
    stateMachine::IvrAction,
)
stateMachine::Transition_strategy = st.builds(
    stateMachine::Transition,
)
stateMachine::State_strategy = st.builds(
    stateMachine::State,
    nombre=
        safe_text
)
stateMachine::StateMachine_strategy = st.builds(
    stateMachine::StateMachine,
    nombre=
        safe_text
)
stateMachine::Properties_strategy = st.builds(
    stateMachine::Properties,
    setupConference=
        st.booleans(),
    mediaHost=
        safe_text,
    recordPath=
        safe_text,
    mediaPort=
        st.integers(),
    scscfUser=
        safe_text,
    applicationServerHost=
        safe_text,
    mediaFromAddr=
        safe_text,
    applicationServerProtocol=
        safe_text,
    scscfHost=
        safe_text,
    mediaURI=
        safe_text,
    mediaProtocol=
        safe_text,
    applicationAddress=
        safe_text,
    scscfPort=
        st.integers(),
    mediaToAddr=
        safe_text,
    applicationServerPort=
        st.integers(),
    scscfProtocol=
        safe_text
)

@given(instance=stateMachine::Branch_strategy)
@settings(max_examples=50)
def test_statemachine::branch_instantiation(instance):
    assert isinstance(instance, stateMachine::Branch)

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)

@given(instance=stateMachine::Otherwise_strategy)
@settings(max_examples=50)
def test_statemachine::otherwise_instantiation(instance):
    assert isinstance(instance, stateMachine::Otherwise)

@given(instance=stateMachine::Key_strategy)
@settings(max_examples=50)
def test_statemachine::key_instantiation(instance):
    assert isinstance(instance, stateMachine::Key)

@given(instance=stateMachine::Key_strategy)
def test_statemachine::key_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=stateMachine::Key_strategy)
def test_statemachine::key_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=stateMachine::NoneEvent_strategy)
@settings(max_examples=50)
def test_statemachine::noneevent_instantiation(instance):
    assert isinstance(instance, stateMachine::NoneEvent)

@given(instance=stateMachine::SMSReceived_strategy)
@settings(max_examples=50)
def test_statemachine::smsreceived_instantiation(instance):
    assert isinstance(instance, stateMachine::SMSReceived)

@given(instance=stateMachine::Timer_strategy)
@settings(max_examples=50)
def test_statemachine::timer_instantiation(instance):
    assert isinstance(instance, stateMachine::Timer)

@given(instance=stateMachine::IVREvent_strategy)
@settings(max_examples=50)
def test_statemachine::ivrevent_instantiation(instance):
    assert isinstance(instance, stateMachine::IVREvent)

@given(instance=IVREvent_strategy)
@settings(max_examples=50)
def test_ivrevent_instantiation(instance):
    assert isinstance(instance, IVREvent)

@given(instance=stateMachine::Init_strategy)
@settings(max_examples=50)
def test_statemachine::init_instantiation(instance):
    assert isinstance(instance, stateMachine::Init)

@given(instance=stateMachine::CollectTimeout_strategy)
@settings(max_examples=50)
def test_statemachine::collecttimeout_instantiation(instance):
    assert isinstance(instance, stateMachine::CollectTimeout)

@given(instance=stateMachine::Managed_strategy)
@settings(max_examples=50)
def test_statemachine::managed_instantiation(instance):
    assert isinstance(instance, stateMachine::Managed)

@given(instance=stateMachine::Managed_strategy)
def test_statemachine::managed_code_type(instance):
    assert isinstance(instance.code, int)


@given(instance=stateMachine::Managed_strategy)
def test_statemachine::managed_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=stateMachine::Managed_strategy)
def test_statemachine::managed_success_type(instance):
    assert isinstance(instance.success, bool)


@given(instance=stateMachine::Managed_strategy)
def test_statemachine::managed_success_setter(instance):
    original = instance.success
    instance.success = original
    assert instance.success == original

@given(instance=stateMachine::Collected_strategy)
@settings(max_examples=50)
def test_statemachine::collected_instantiation(instance):
    assert isinstance(instance, stateMachine::Collected)

@given(instance=stateMachine::Recorderd_strategy)
@settings(max_examples=50)
def test_statemachine::recorderd_instantiation(instance):
    assert isinstance(instance, stateMachine::Recorderd)

@given(instance=stateMachine::Recorderd_strategy)
def test_statemachine::recorderd_recordId_type(instance):
    assert isinstance(instance.recordId, str)


@given(instance=stateMachine::Recorderd_strategy)
def test_statemachine::recorderd_recordId_setter(instance):
    original = instance.recordId
    instance.recordId = original
    assert instance.recordId == original

@given(instance=stateMachine::Terminated_strategy)
@settings(max_examples=50)
def test_statemachine::terminated_instantiation(instance):
    assert isinstance(instance, stateMachine::Terminated)

@given(instance=stateMachine::Call_strategy)
@settings(max_examples=50)
def test_statemachine::call_instantiation(instance):
    assert isinstance(instance, stateMachine::Call)

@given(instance=stateMachine::Call_strategy)
def test_statemachine::call_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=stateMachine::Call_strategy)
def test_statemachine::call_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=stateMachine::Call_strategy)
def test_statemachine::call_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=stateMachine::Call_strategy)
def test_statemachine::call_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=stateMachine::PickUp_strategy)
@settings(max_examples=50)
def test_statemachine::pickup_instantiation(instance):
    assert isinstance(instance, stateMachine::PickUp)

@given(instance=stateMachine::Played_strategy)
@settings(max_examples=50)
def test_statemachine::played_instantiation(instance):
    assert isinstance(instance, stateMachine::Played)

@given(instance=stateMachine::Cancel_strategy)
@settings(max_examples=50)
def test_statemachine::cancel_instantiation(instance):
    assert isinstance(instance, stateMachine::Cancel)

@given(instance=stateMachine::Bye_strategy)
@settings(max_examples=50)
def test_statemachine::bye_instantiation(instance):
    assert isinstance(instance, stateMachine::Bye)

@given(instance=Play_strategy)
@settings(max_examples=50)
def test_play_instantiation(instance):
    assert isinstance(instance, Play)

@given(instance=stateMachine::PlayRecord_strategy)
@settings(max_examples=50)
def test_statemachine::playrecord_instantiation(instance):
    assert isinstance(instance, stateMachine::PlayRecord)

@given(instance=stateMachine::PlayCollect_strategy)
@settings(max_examples=50)
def test_statemachine::playcollect_instantiation(instance):
    assert isinstance(instance, stateMachine::PlayCollect)

@given(instance=stateMachine::SMS_strategy)
@settings(max_examples=50)
def test_statemachine::sms_instantiation(instance):
    assert isinstance(instance, stateMachine::SMS)

@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=stateMachine::SMS_strategy)
def test_statemachine::sms_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=stateMachine::Action_strategy)
@settings(max_examples=50)
def test_statemachine::action_instantiation(instance):
    assert isinstance(instance, stateMachine::Action)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=stateMachine::CompositeState_strategy)
@settings(max_examples=50)
def test_statemachine::compositestate_instantiation(instance):
    assert isinstance(instance, stateMachine::CompositeState)

@given(instance=stateMachine::FinalState_strategy)
@settings(max_examples=50)
def test_statemachine::finalstate_instantiation(instance):
    assert isinstance(instance, stateMachine::FinalState)

@given(instance=stateMachine::InitialState_strategy)
@settings(max_examples=50)
def test_statemachine::initialstate_instantiation(instance):
    assert isinstance(instance, stateMachine::InitialState)

@given(instance=IvrAction_strategy)
@settings(max_examples=50)
def test_ivraction_instantiation(instance):
    assert isinstance(instance, IvrAction)

@given(instance=stateMachine::RemoveRecord_strategy)
@settings(max_examples=50)
def test_statemachine::removerecord_instantiation(instance):
    assert isinstance(instance, stateMachine::RemoveRecord)

@given(instance=stateMachine::RemoveRecord_strategy)
def test_statemachine::removerecord_recordId_type(instance):
    assert isinstance(instance.recordId, str)


@given(instance=stateMachine::RemoveRecord_strategy)
def test_statemachine::removerecord_recordId_setter(instance):
    original = instance.recordId
    instance.recordId = original
    assert instance.recordId == original

@given(instance=stateMachine::NewCall_strategy)
@settings(max_examples=50)
def test_statemachine::newcall_instantiation(instance):
    assert isinstance(instance, stateMachine::NewCall)

@given(instance=stateMachine::NewCall_strategy)
def test_statemachine::newcall_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=stateMachine::NewCall_strategy)
def test_statemachine::newcall_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=stateMachine::NewCall_strategy)
def test_statemachine::newcall_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=stateMachine::NewCall_strategy)
def test_statemachine::newcall_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=stateMachine::Play_strategy)
@settings(max_examples=50)
def test_statemachine::play_instantiation(instance):
    assert isinstance(instance, stateMachine::Play)

@given(instance=stateMachine::Play_strategy)
def test_statemachine::play_mediaURI_type(instance):
    assert isinstance(instance.mediaURI, str)


@given(instance=stateMachine::Play_strategy)
def test_statemachine::play_mediaURI_setter(instance):
    original = instance.mediaURI
    instance.mediaURI = original
    assert instance.mediaURI == original

@given(instance=stateMachine::Play_strategy)
def test_statemachine::play_baseURL_type(instance):
    assert isinstance(instance.baseURL, str)


@given(instance=stateMachine::Play_strategy)
def test_statemachine::play_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original

@given(instance=stateMachine::Terminate_strategy)
@settings(max_examples=50)
def test_statemachine::terminate_instantiation(instance):
    assert isinstance(instance, stateMachine::Terminate)

@given(instance=stateMachine::HangUp_strategy)
@settings(max_examples=50)
def test_statemachine::hangup_instantiation(instance):
    assert isinstance(instance, stateMachine::HangUp)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=stateMachine::SetTimer_strategy)
@settings(max_examples=50)
def test_statemachine::settimer_instantiation(instance):
    assert isinstance(instance, stateMachine::SetTimer)

@given(instance=stateMachine::SetTimer_strategy)
def test_statemachine::settimer_millis_type(instance):
    assert isinstance(instance.millis, float)


@given(instance=stateMachine::SetTimer_strategy)
def test_statemachine::settimer_millis_setter(instance):
    original = instance.millis
    instance.millis = original
    assert instance.millis == original

@given(instance=stateMachine::SendSms_strategy)
@settings(max_examples=50)
def test_statemachine::sendsms_instantiation(instance):
    assert isinstance(instance, stateMachine::SendSms)

@given(instance=stateMachine::IvrAction_strategy)
@settings(max_examples=50)
def test_statemachine::ivraction_instantiation(instance):
    assert isinstance(instance, stateMachine::IvrAction)

@given(instance=stateMachine::Transition_strategy)
@settings(max_examples=50)
def test_statemachine::transition_instantiation(instance):
    assert isinstance(instance, stateMachine::Transition)

@given(instance=stateMachine::State_strategy)
@settings(max_examples=50)
def test_statemachine::state_instantiation(instance):
    assert isinstance(instance, stateMachine::State)

@given(instance=stateMachine::State_strategy)
def test_statemachine::state_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=stateMachine::State_strategy)
def test_statemachine::state_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=stateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine::statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine::StateMachine)

@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_nombre_type(instance):
    assert isinstance(instance.nombre, str)


@given(instance=stateMachine::StateMachine_strategy)
def test_statemachine::statemachine_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=stateMachine::Properties_strategy)
@settings(max_examples=50)
def test_statemachine::properties_instantiation(instance):
    assert isinstance(instance, stateMachine::Properties)

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_setupConference_type(instance):
    assert isinstance(instance.setupConference, bool)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_setupConference_setter(instance):
    original = instance.setupConference
    instance.setupConference = original
    assert instance.setupConference == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaHost_type(instance):
    assert isinstance(instance.mediaHost, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaHost_setter(instance):
    original = instance.mediaHost
    instance.mediaHost = original
    assert instance.mediaHost == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_recordPath_type(instance):
    assert isinstance(instance.recordPath, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_recordPath_setter(instance):
    original = instance.recordPath
    instance.recordPath = original
    assert instance.recordPath == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaPort_type(instance):
    assert isinstance(instance.mediaPort, int)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaPort_setter(instance):
    original = instance.mediaPort
    instance.mediaPort = original
    assert instance.mediaPort == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfUser_type(instance):
    assert isinstance(instance.scscfUser, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfUser_setter(instance):
    original = instance.scscfUser
    instance.scscfUser = original
    assert instance.scscfUser == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerHost_type(instance):
    assert isinstance(instance.applicationServerHost, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerHost_setter(instance):
    original = instance.applicationServerHost
    instance.applicationServerHost = original
    assert instance.applicationServerHost == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaFromAddr_type(instance):
    assert isinstance(instance.mediaFromAddr, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaFromAddr_setter(instance):
    original = instance.mediaFromAddr
    instance.mediaFromAddr = original
    assert instance.mediaFromAddr == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerProtocol_type(instance):
    assert isinstance(instance.applicationServerProtocol, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerProtocol_setter(instance):
    original = instance.applicationServerProtocol
    instance.applicationServerProtocol = original
    assert instance.applicationServerProtocol == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfHost_type(instance):
    assert isinstance(instance.scscfHost, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfHost_setter(instance):
    original = instance.scscfHost
    instance.scscfHost = original
    assert instance.scscfHost == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaURI_type(instance):
    assert isinstance(instance.mediaURI, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaURI_setter(instance):
    original = instance.mediaURI
    instance.mediaURI = original
    assert instance.mediaURI == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaProtocol_type(instance):
    assert isinstance(instance.mediaProtocol, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaProtocol_setter(instance):
    original = instance.mediaProtocol
    instance.mediaProtocol = original
    assert instance.mediaProtocol == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationAddress_type(instance):
    assert isinstance(instance.applicationAddress, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationAddress_setter(instance):
    original = instance.applicationAddress
    instance.applicationAddress = original
    assert instance.applicationAddress == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfPort_type(instance):
    assert isinstance(instance.scscfPort, int)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfPort_setter(instance):
    original = instance.scscfPort
    instance.scscfPort = original
    assert instance.scscfPort == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaToAddr_type(instance):
    assert isinstance(instance.mediaToAddr, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_mediaToAddr_setter(instance):
    original = instance.mediaToAddr
    instance.mediaToAddr = original
    assert instance.mediaToAddr == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerPort_type(instance):
    assert isinstance(instance.applicationServerPort, int)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_applicationServerPort_setter(instance):
    original = instance.applicationServerPort
    instance.applicationServerPort = original
    assert instance.applicationServerPort == original

@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfProtocol_type(instance):
    assert isinstance(instance.scscfProtocol, str)


@given(instance=stateMachine::Properties_strategy)
def test_statemachine::properties_scscfProtocol_setter(instance):
    original = instance.scscfProtocol
    instance.scscfProtocol = original
    assert instance.scscfProtocol == original
