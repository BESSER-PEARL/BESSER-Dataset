import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Branch,
    stateMachine_Otherwise,
    stateMachine_Key,
    stateMachine_Branch,
    IVREvent,
    stateMachine_PickUp,
    stateMachine_Init,
    stateMachine_Recorderd,
    stateMachine_Call,
    stateMachine_Terminated,
    stateMachine_Played,
    stateMachine_Managed,
    stateMachine_Cancel,
    stateMachine_Collected,
    stateMachine_CollectTimeout,
    stateMachine_Bye,
    Transition,
    stateMachine_NoneEvent,
    stateMachine_Timer,
    stateMachine_SMSReceived,
    stateMachine_IVREvent,
    stateMachine_SMS,
    IvrAction,
    stateMachine_Terminate,
    stateMachine_Play,
    Action,
    stateMachine_SetTimer,
    stateMachine_SendSms,
    stateMachine_IvrAction,
    stateMachine_Action,
    State,
    stateMachine_FinalState,
    stateMachine_CompositeState,
    stateMachine_InitialState,
    stateMachine_Transition,
    stateMachine_Properties,
    stateMachine_State,
    stateMachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_branch_is_not_abstract():
    assert not inspect.isabstract(Branch)


def test_branch_constructor_exists():
    assert callable(Branch.__init__)


def test_branch_constructor_args():
    sig = inspect.signature(Branch.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_otherwise_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Otherwise)


def test_statemachine_otherwise_constructor_exists():
    assert callable(stateMachine_Otherwise.__init__)


def test_statemachine_otherwise_constructor_args():
    sig = inspect.signature(stateMachine_Otherwise.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_key_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Key)


def test_statemachine_key_constructor_exists():
    assert callable(stateMachine_Key.__init__)


def test_statemachine_key_constructor_args():
    sig = inspect.signature(stateMachine_Key.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_statemachine_key_has_key():
    assert hasattr(stateMachine_Key, "key")
    descriptor = None
    for klass in stateMachine_Key.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_branch_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Branch)


def test_statemachine_branch_constructor_exists():
    assert callable(stateMachine_Branch.__init__)


def test_statemachine_branch_constructor_args():
    sig = inspect.signature(stateMachine_Branch.__init__)
    params = list(sig.parameters.keys())



def test_ivrevent_is_not_abstract():
    assert not inspect.isabstract(IVREvent)


def test_ivrevent_constructor_exists():
    assert callable(IVREvent.__init__)


def test_ivrevent_constructor_args():
    sig = inspect.signature(IVREvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_pickup_is_not_abstract():
    assert not inspect.isabstract(stateMachine_PickUp)


def test_statemachine_pickup_constructor_exists():
    assert callable(stateMachine_PickUp.__init__)


def test_statemachine_pickup_constructor_args():
    sig = inspect.signature(stateMachine_PickUp.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_init_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Init)


def test_statemachine_init_constructor_exists():
    assert callable(stateMachine_Init.__init__)


def test_statemachine_init_constructor_args():
    sig = inspect.signature(stateMachine_Init.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_recorderd_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Recorderd)


def test_statemachine_recorderd_constructor_exists():
    assert callable(stateMachine_Recorderd.__init__)


def test_statemachine_recorderd_constructor_args():
    sig = inspect.signature(stateMachine_Recorderd.__init__)
    params = list(sig.parameters.keys())
    assert "recordId" in params, "Missing parameter 'recordId'"

def test_statemachine_recorderd_has_recordId():
    assert hasattr(stateMachine_Recorderd, "recordId")
    descriptor = None
    for klass in stateMachine_Recorderd.__mro__:
        if "recordId" in klass.__dict__:
            descriptor = klass.__dict__["recordId"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_call_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Call)


def test_statemachine_call_constructor_exists():
    assert callable(stateMachine_Call.__init__)


def test_statemachine_call_constructor_args():
    sig = inspect.signature(stateMachine_Call.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_statemachine_call_has_to():
    assert hasattr(stateMachine_Call, "to")
    descriptor = None
    for klass in stateMachine_Call.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_call_has_from_():
    assert hasattr(stateMachine_Call, "from_")
    descriptor = None
    for klass in stateMachine_Call.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_terminated_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Terminated)


def test_statemachine_terminated_constructor_exists():
    assert callable(stateMachine_Terminated.__init__)


def test_statemachine_terminated_constructor_args():
    sig = inspect.signature(stateMachine_Terminated.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_played_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Played)


def test_statemachine_played_constructor_exists():
    assert callable(stateMachine_Played.__init__)


def test_statemachine_played_constructor_args():
    sig = inspect.signature(stateMachine_Played.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_managed_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Managed)


def test_statemachine_managed_constructor_exists():
    assert callable(stateMachine_Managed.__init__)


def test_statemachine_managed_constructor_args():
    sig = inspect.signature(stateMachine_Managed.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "success" in params, "Missing parameter 'success'"

def test_statemachine_managed_has_code():
    assert hasattr(stateMachine_Managed, "code")
    descriptor = None
    for klass in stateMachine_Managed.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_managed_has_success():
    assert hasattr(stateMachine_Managed, "success")
    descriptor = None
    for klass in stateMachine_Managed.__mro__:
        if "success" in klass.__dict__:
            descriptor = klass.__dict__["success"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_cancel_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Cancel)


def test_statemachine_cancel_constructor_exists():
    assert callable(stateMachine_Cancel.__init__)


def test_statemachine_cancel_constructor_args():
    sig = inspect.signature(stateMachine_Cancel.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_collected_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Collected)


def test_statemachine_collected_constructor_exists():
    assert callable(stateMachine_Collected.__init__)


def test_statemachine_collected_constructor_args():
    sig = inspect.signature(stateMachine_Collected.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_collecttimeout_is_not_abstract():
    assert not inspect.isabstract(stateMachine_CollectTimeout)


def test_statemachine_collecttimeout_constructor_exists():
    assert callable(stateMachine_CollectTimeout.__init__)


def test_statemachine_collecttimeout_constructor_args():
    sig = inspect.signature(stateMachine_CollectTimeout.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_bye_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Bye)


def test_statemachine_bye_constructor_exists():
    assert callable(stateMachine_Bye.__init__)


def test_statemachine_bye_constructor_args():
    sig = inspect.signature(stateMachine_Bye.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_noneevent_is_not_abstract():
    assert not inspect.isabstract(stateMachine_NoneEvent)


def test_statemachine_noneevent_constructor_exists():
    assert callable(stateMachine_NoneEvent.__init__)


def test_statemachine_noneevent_constructor_args():
    sig = inspect.signature(stateMachine_NoneEvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_timer_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Timer)


def test_statemachine_timer_constructor_exists():
    assert callable(stateMachine_Timer.__init__)


def test_statemachine_timer_constructor_args():
    sig = inspect.signature(stateMachine_Timer.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_smsreceived_is_not_abstract():
    assert not inspect.isabstract(stateMachine_SMSReceived)


def test_statemachine_smsreceived_constructor_exists():
    assert callable(stateMachine_SMSReceived.__init__)


def test_statemachine_smsreceived_constructor_args():
    sig = inspect.signature(stateMachine_SMSReceived.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_ivrevent_is_not_abstract():
    assert not inspect.isabstract(stateMachine_IVREvent)


def test_statemachine_ivrevent_constructor_exists():
    assert callable(stateMachine_IVREvent.__init__)


def test_statemachine_ivrevent_constructor_args():
    sig = inspect.signature(stateMachine_IVREvent.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_sms_is_not_abstract():
    assert not inspect.isabstract(stateMachine_SMS)


def test_statemachine_sms_constructor_exists():
    assert callable(stateMachine_SMS.__init__)


def test_statemachine_sms_constructor_args():
    sig = inspect.signature(stateMachine_SMS.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "text" in params, "Missing parameter 'text'"

def test_statemachine_sms_has_to():
    assert hasattr(stateMachine_SMS, "to")
    descriptor = None
    for klass in stateMachine_SMS.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_sms_has_from_():
    assert hasattr(stateMachine_SMS, "from_")
    descriptor = None
    for klass in stateMachine_SMS.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_sms_has_text():
    assert hasattr(stateMachine_SMS, "text")
    descriptor = None
    for klass in stateMachine_SMS.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ivraction_is_not_abstract():
    assert not inspect.isabstract(IvrAction)


def test_ivraction_constructor_exists():
    assert callable(IvrAction.__init__)


def test_ivraction_constructor_args():
    sig = inspect.signature(IvrAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_terminate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Terminate)


def test_statemachine_terminate_constructor_exists():
    assert callable(stateMachine_Terminate.__init__)


def test_statemachine_terminate_constructor_args():
    sig = inspect.signature(stateMachine_Terminate.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_play_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Play)


def test_statemachine_play_constructor_exists():
    assert callable(stateMachine_Play.__init__)


def test_statemachine_play_constructor_args():
    sig = inspect.signature(stateMachine_Play.__init__)
    params = list(sig.parameters.keys())
    assert "mediaURI" in params, "Missing parameter 'mediaURI'"
    assert "baseURL" in params, "Missing parameter 'baseURL'"

def test_statemachine_play_has_mediaURI():
    assert hasattr(stateMachine_Play, "mediaURI")
    descriptor = None
    for klass in stateMachine_Play.__mro__:
        if "mediaURI" in klass.__dict__:
            descriptor = klass.__dict__["mediaURI"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_play_has_baseURL():
    assert hasattr(stateMachine_Play, "baseURL")
    descriptor = None
    for klass in stateMachine_Play.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_settimer_is_not_abstract():
    assert not inspect.isabstract(stateMachine_SetTimer)


def test_statemachine_settimer_constructor_exists():
    assert callable(stateMachine_SetTimer.__init__)


def test_statemachine_settimer_constructor_args():
    sig = inspect.signature(stateMachine_SetTimer.__init__)
    params = list(sig.parameters.keys())
    assert "millis" in params, "Missing parameter 'millis'"

def test_statemachine_settimer_has_millis():
    assert hasattr(stateMachine_SetTimer, "millis")
    descriptor = None
    for klass in stateMachine_SetTimer.__mro__:
        if "millis" in klass.__dict__:
            descriptor = klass.__dict__["millis"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_sendsms_is_not_abstract():
    assert not inspect.isabstract(stateMachine_SendSms)


def test_statemachine_sendsms_constructor_exists():
    assert callable(stateMachine_SendSms.__init__)


def test_statemachine_sendsms_constructor_args():
    sig = inspect.signature(stateMachine_SendSms.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_ivraction_is_not_abstract():
    assert not inspect.isabstract(stateMachine_IvrAction)


def test_statemachine_ivraction_constructor_exists():
    assert callable(stateMachine_IvrAction.__init__)


def test_statemachine_ivraction_constructor_args():
    sig = inspect.signature(stateMachine_IvrAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_action_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Action)


def test_statemachine_action_constructor_exists():
    assert callable(stateMachine_Action.__init__)


def test_statemachine_action_constructor_args():
    sig = inspect.signature(stateMachine_Action.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(stateMachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(stateMachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_compositestate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_CompositeState)


def test_statemachine_compositestate_constructor_exists():
    assert callable(stateMachine_CompositeState.__init__)


def test_statemachine_compositestate_constructor_args():
    sig = inspect.signature(stateMachine_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(stateMachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(stateMachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(stateMachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(stateMachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(stateMachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_properties_is_not_abstract():
    assert not inspect.isabstract(stateMachine_Properties)


def test_statemachine_properties_constructor_exists():
    assert callable(stateMachine_Properties.__init__)


def test_statemachine_properties_constructor_args():
    sig = inspect.signature(stateMachine_Properties.__init__)
    params = list(sig.parameters.keys())
    assert "applicationServerHost" in params, "Missing parameter 'applicationServerHost'"
    assert "applicationAddress" in params, "Missing parameter 'applicationAddress'"
    assert "applicationServerPort" in params, "Missing parameter 'applicationServerPort'"
    assert "mediaPort" in params, "Missing parameter 'mediaPort'"
    assert "scscfProtocol" in params, "Missing parameter 'scscfProtocol'"
    assert "recordPath" in params, "Missing parameter 'recordPath'"
    assert "mediaHost" in params, "Missing parameter 'mediaHost'"
    assert "applicationServerProtocol" in params, "Missing parameter 'applicationServerProtocol'"
    assert "scscfUser" in params, "Missing parameter 'scscfUser'"
    assert "mediaURI" in params, "Missing parameter 'mediaURI'"
    assert "mediaFromAddr" in params, "Missing parameter 'mediaFromAddr'"
    assert "mediaProtocol" in params, "Missing parameter 'mediaProtocol'"
    assert "scscfPort" in params, "Missing parameter 'scscfPort'"
    assert "mediaToAddr" in params, "Missing parameter 'mediaToAddr'"
    assert "setupConference" in params, "Missing parameter 'setupConference'"
    assert "scscfHost" in params, "Missing parameter 'scscfHost'"

def test_statemachine_properties_has_applicationServerHost():
    assert hasattr(stateMachine_Properties, "applicationServerHost")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "applicationServerHost" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerHost"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_applicationAddress():
    assert hasattr(stateMachine_Properties, "applicationAddress")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "applicationAddress" in klass.__dict__:
            descriptor = klass.__dict__["applicationAddress"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_applicationServerPort():
    assert hasattr(stateMachine_Properties, "applicationServerPort")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "applicationServerPort" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaPort():
    assert hasattr(stateMachine_Properties, "mediaPort")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaPort" in klass.__dict__:
            descriptor = klass.__dict__["mediaPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_scscfProtocol():
    assert hasattr(stateMachine_Properties, "scscfProtocol")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "scscfProtocol" in klass.__dict__:
            descriptor = klass.__dict__["scscfProtocol"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_recordPath():
    assert hasattr(stateMachine_Properties, "recordPath")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "recordPath" in klass.__dict__:
            descriptor = klass.__dict__["recordPath"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaHost():
    assert hasattr(stateMachine_Properties, "mediaHost")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaHost" in klass.__dict__:
            descriptor = klass.__dict__["mediaHost"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_applicationServerProtocol():
    assert hasattr(stateMachine_Properties, "applicationServerProtocol")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "applicationServerProtocol" in klass.__dict__:
            descriptor = klass.__dict__["applicationServerProtocol"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_scscfUser():
    assert hasattr(stateMachine_Properties, "scscfUser")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "scscfUser" in klass.__dict__:
            descriptor = klass.__dict__["scscfUser"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaURI():
    assert hasattr(stateMachine_Properties, "mediaURI")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaURI" in klass.__dict__:
            descriptor = klass.__dict__["mediaURI"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaFromAddr():
    assert hasattr(stateMachine_Properties, "mediaFromAddr")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaFromAddr" in klass.__dict__:
            descriptor = klass.__dict__["mediaFromAddr"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaProtocol():
    assert hasattr(stateMachine_Properties, "mediaProtocol")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaProtocol" in klass.__dict__:
            descriptor = klass.__dict__["mediaProtocol"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_scscfPort():
    assert hasattr(stateMachine_Properties, "scscfPort")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "scscfPort" in klass.__dict__:
            descriptor = klass.__dict__["scscfPort"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_mediaToAddr():
    assert hasattr(stateMachine_Properties, "mediaToAddr")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "mediaToAddr" in klass.__dict__:
            descriptor = klass.__dict__["mediaToAddr"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_setupConference():
    assert hasattr(stateMachine_Properties, "setupConference")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "setupConference" in klass.__dict__:
            descriptor = klass.__dict__["setupConference"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_properties_has_scscfHost():
    assert hasattr(stateMachine_Properties, "scscfHost")
    descriptor = None
    for klass in stateMachine_Properties.__mro__:
        if "scscfHost" in klass.__dict__:
            descriptor = klass.__dict__["scscfHost"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(stateMachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(stateMachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(stateMachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_statemachine_state_has_nombre():
    assert hasattr(stateMachine_State, "nombre")
    descriptor = None
    for klass in stateMachine_State.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(stateMachine_StateMachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(stateMachine_StateMachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(stateMachine_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "nombre" in params, "Missing parameter 'nombre'"

def test_statemachine_statemachine_has_nombre():
    assert hasattr(stateMachine_StateMachine, "nombre")
    descriptor = None
    for klass in stateMachine_StateMachine.__mro__:
        if "nombre" in klass.__dict__:
            descriptor = klass.__dict__["nombre"]
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
Branch_strategy = st.builds(
    Branch,
)
stateMachine_Otherwise_strategy = st.builds(
    stateMachine_Otherwise,
)
stateMachine_Key_strategy = st.builds(
    stateMachine_Key,
    key=
        safe_text
)
stateMachine_Branch_strategy = st.builds(
    stateMachine_Branch,
)
IVREvent_strategy = st.builds(
    IVREvent,
)
stateMachine_PickUp_strategy = st.builds(
    stateMachine_PickUp,
)
stateMachine_Init_strategy = st.builds(
    stateMachine_Init,
)
stateMachine_Recorderd_strategy = st.builds(
    stateMachine_Recorderd,
    recordId=
        safe_text
)
stateMachine_Call_strategy = st.builds(
    stateMachine_Call,
    to=
        safe_text,
    from_=
        safe_text
)
stateMachine_Terminated_strategy = st.builds(
    stateMachine_Terminated,
)
stateMachine_Played_strategy = st.builds(
    stateMachine_Played,
)
stateMachine_Managed_strategy = st.builds(
    stateMachine_Managed,
    code=
        st.integers(),
    success=
        st.booleans()
)
stateMachine_Cancel_strategy = st.builds(
    stateMachine_Cancel,
)
stateMachine_Collected_strategy = st.builds(
    stateMachine_Collected,
)
stateMachine_CollectTimeout_strategy = st.builds(
    stateMachine_CollectTimeout,
)
stateMachine_Bye_strategy = st.builds(
    stateMachine_Bye,
)
Transition_strategy = st.builds(
    Transition,
)
stateMachine_NoneEvent_strategy = st.builds(
    stateMachine_NoneEvent,
)
stateMachine_Timer_strategy = st.builds(
    stateMachine_Timer,
)
stateMachine_SMSReceived_strategy = st.builds(
    stateMachine_SMSReceived,
)
stateMachine_IVREvent_strategy = st.builds(
    stateMachine_IVREvent,
)
stateMachine_SMS_strategy = st.builds(
    stateMachine_SMS,
    to=
        safe_text,
    from_=
        safe_text,
    text=
        safe_text
)
IvrAction_strategy = st.builds(
    IvrAction,
)
stateMachine_Terminate_strategy = st.builds(
    stateMachine_Terminate,
)
stateMachine_Play_strategy = st.builds(
    stateMachine_Play,
    mediaURI=
        safe_text,
    baseURL=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
stateMachine_SetTimer_strategy = st.builds(
    stateMachine_SetTimer,
    millis=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
stateMachine_SendSms_strategy = st.builds(
    stateMachine_SendSms,
)
stateMachine_IvrAction_strategy = st.builds(
    stateMachine_IvrAction,
)
stateMachine_Action_strategy = st.builds(
    stateMachine_Action,
)
State_strategy = st.builds(
    State,
)
stateMachine_FinalState_strategy = st.builds(
    stateMachine_FinalState,
)
stateMachine_CompositeState_strategy = st.builds(
    stateMachine_CompositeState,
)
stateMachine_InitialState_strategy = st.builds(
    stateMachine_InitialState,
)
stateMachine_Transition_strategy = st.builds(
    stateMachine_Transition,
)
stateMachine_Properties_strategy = st.builds(
    stateMachine_Properties,
    applicationServerHost=
        safe_text,
    applicationAddress=
        safe_text,
    applicationServerPort=
        st.integers(),
    mediaPort=
        st.integers(),
    scscfProtocol=
        safe_text,
    recordPath=
        safe_text,
    mediaHost=
        safe_text,
    applicationServerProtocol=
        safe_text,
    scscfUser=
        safe_text,
    mediaURI=
        safe_text,
    mediaFromAddr=
        safe_text,
    mediaProtocol=
        safe_text,
    scscfPort=
        st.integers(),
    mediaToAddr=
        safe_text,
    setupConference=
        st.booleans(),
    scscfHost=
        safe_text
)
stateMachine_State_strategy = st.builds(
    stateMachine_State,
    nombre=
        safe_text
)
stateMachine_StateMachine_strategy = st.builds(
    stateMachine_StateMachine,
    nombre=
        safe_text
)

@given(instance=Branch_strategy)
@settings(max_examples=50)
def test_branch_instantiation(instance):
    assert isinstance(instance, Branch)

@given(instance=stateMachine_Otherwise_strategy)
@settings(max_examples=50)
def test_statemachine_otherwise_instantiation(instance):
    assert isinstance(instance, stateMachine_Otherwise)

@given(instance=stateMachine_Key_strategy)
@settings(max_examples=50)
def test_statemachine_key_instantiation(instance):
    assert isinstance(instance, stateMachine_Key)



@given(instance=stateMachine_Key_strategy)
def test_statemachine_key_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=stateMachine_Branch_strategy)
@settings(max_examples=50)
def test_statemachine_branch_instantiation(instance):
    assert isinstance(instance, stateMachine_Branch)

@given(instance=IVREvent_strategy)
@settings(max_examples=50)
def test_ivrevent_instantiation(instance):
    assert isinstance(instance, IVREvent)

@given(instance=stateMachine_PickUp_strategy)
@settings(max_examples=50)
def test_statemachine_pickup_instantiation(instance):
    assert isinstance(instance, stateMachine_PickUp)

@given(instance=stateMachine_Init_strategy)
@settings(max_examples=50)
def test_statemachine_init_instantiation(instance):
    assert isinstance(instance, stateMachine_Init)

@given(instance=stateMachine_Recorderd_strategy)
@settings(max_examples=50)
def test_statemachine_recorderd_instantiation(instance):
    assert isinstance(instance, stateMachine_Recorderd)



@given(instance=stateMachine_Recorderd_strategy)
def test_statemachine_recorderd_recordId_setter(instance):
    original = instance.recordId
    instance.recordId = original
    assert instance.recordId == original

@given(instance=stateMachine_Call_strategy)
@settings(max_examples=50)
def test_statemachine_call_instantiation(instance):
    assert isinstance(instance, stateMachine_Call)



@given(instance=stateMachine_Call_strategy)
def test_statemachine_call_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=stateMachine_Call_strategy)
def test_statemachine_call_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=stateMachine_Terminated_strategy)
@settings(max_examples=50)
def test_statemachine_terminated_instantiation(instance):
    assert isinstance(instance, stateMachine_Terminated)

@given(instance=stateMachine_Played_strategy)
@settings(max_examples=50)
def test_statemachine_played_instantiation(instance):
    assert isinstance(instance, stateMachine_Played)

@given(instance=stateMachine_Managed_strategy)
@settings(max_examples=50)
def test_statemachine_managed_instantiation(instance):
    assert isinstance(instance, stateMachine_Managed)



@given(instance=stateMachine_Managed_strategy)
def test_statemachine_managed_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=stateMachine_Managed_strategy)
def test_statemachine_managed_success_setter(instance):
    original = instance.success
    instance.success = original
    assert instance.success == original

@given(instance=stateMachine_Cancel_strategy)
@settings(max_examples=50)
def test_statemachine_cancel_instantiation(instance):
    assert isinstance(instance, stateMachine_Cancel)

@given(instance=stateMachine_Collected_strategy)
@settings(max_examples=50)
def test_statemachine_collected_instantiation(instance):
    assert isinstance(instance, stateMachine_Collected)

@given(instance=stateMachine_CollectTimeout_strategy)
@settings(max_examples=50)
def test_statemachine_collecttimeout_instantiation(instance):
    assert isinstance(instance, stateMachine_CollectTimeout)

@given(instance=stateMachine_Bye_strategy)
@settings(max_examples=50)
def test_statemachine_bye_instantiation(instance):
    assert isinstance(instance, stateMachine_Bye)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=stateMachine_NoneEvent_strategy)
@settings(max_examples=50)
def test_statemachine_noneevent_instantiation(instance):
    assert isinstance(instance, stateMachine_NoneEvent)

@given(instance=stateMachine_Timer_strategy)
@settings(max_examples=50)
def test_statemachine_timer_instantiation(instance):
    assert isinstance(instance, stateMachine_Timer)

@given(instance=stateMachine_SMSReceived_strategy)
@settings(max_examples=50)
def test_statemachine_smsreceived_instantiation(instance):
    assert isinstance(instance, stateMachine_SMSReceived)

@given(instance=stateMachine_IVREvent_strategy)
@settings(max_examples=50)
def test_statemachine_ivrevent_instantiation(instance):
    assert isinstance(instance, stateMachine_IVREvent)

@given(instance=stateMachine_SMS_strategy)
@settings(max_examples=50)
def test_statemachine_sms_instantiation(instance):
    assert isinstance(instance, stateMachine_SMS)



@given(instance=stateMachine_SMS_strategy)
def test_statemachine_sms_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=stateMachine_SMS_strategy)
def test_statemachine_sms_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=stateMachine_SMS_strategy)
def test_statemachine_sms_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=IvrAction_strategy)
@settings(max_examples=50)
def test_ivraction_instantiation(instance):
    assert isinstance(instance, IvrAction)

@given(instance=stateMachine_Terminate_strategy)
@settings(max_examples=50)
def test_statemachine_terminate_instantiation(instance):
    assert isinstance(instance, stateMachine_Terminate)

@given(instance=stateMachine_Play_strategy)
@settings(max_examples=50)
def test_statemachine_play_instantiation(instance):
    assert isinstance(instance, stateMachine_Play)



@given(instance=stateMachine_Play_strategy)
def test_statemachine_play_mediaURI_setter(instance):
    original = instance.mediaURI
    instance.mediaURI = original
    assert instance.mediaURI == original



@given(instance=stateMachine_Play_strategy)
def test_statemachine_play_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=stateMachine_SetTimer_strategy)
@settings(max_examples=50)
def test_statemachine_settimer_instantiation(instance):
    assert isinstance(instance, stateMachine_SetTimer)



@given(instance=stateMachine_SetTimer_strategy)
def test_statemachine_settimer_millis_setter(instance):
    original = instance.millis
    instance.millis = original
    assert instance.millis == original

@given(instance=stateMachine_SendSms_strategy)
@settings(max_examples=50)
def test_statemachine_sendsms_instantiation(instance):
    assert isinstance(instance, stateMachine_SendSms)

@given(instance=stateMachine_IvrAction_strategy)
@settings(max_examples=50)
def test_statemachine_ivraction_instantiation(instance):
    assert isinstance(instance, stateMachine_IvrAction)

@given(instance=stateMachine_Action_strategy)
@settings(max_examples=50)
def test_statemachine_action_instantiation(instance):
    assert isinstance(instance, stateMachine_Action)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=stateMachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, stateMachine_FinalState)

@given(instance=stateMachine_CompositeState_strategy)
@settings(max_examples=50)
def test_statemachine_compositestate_instantiation(instance):
    assert isinstance(instance, stateMachine_CompositeState)

@given(instance=stateMachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, stateMachine_InitialState)

@given(instance=stateMachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, stateMachine_Transition)

@given(instance=stateMachine_Properties_strategy)
@settings(max_examples=50)
def test_statemachine_properties_instantiation(instance):
    assert isinstance(instance, stateMachine_Properties)



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_applicationServerHost_setter(instance):
    original = instance.applicationServerHost
    instance.applicationServerHost = original
    assert instance.applicationServerHost == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_applicationAddress_setter(instance):
    original = instance.applicationAddress
    instance.applicationAddress = original
    assert instance.applicationAddress == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_applicationServerPort_setter(instance):
    original = instance.applicationServerPort
    instance.applicationServerPort = original
    assert instance.applicationServerPort == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaPort_setter(instance):
    original = instance.mediaPort
    instance.mediaPort = original
    assert instance.mediaPort == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_scscfProtocol_setter(instance):
    original = instance.scscfProtocol
    instance.scscfProtocol = original
    assert instance.scscfProtocol == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_recordPath_setter(instance):
    original = instance.recordPath
    instance.recordPath = original
    assert instance.recordPath == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaHost_setter(instance):
    original = instance.mediaHost
    instance.mediaHost = original
    assert instance.mediaHost == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_applicationServerProtocol_setter(instance):
    original = instance.applicationServerProtocol
    instance.applicationServerProtocol = original
    assert instance.applicationServerProtocol == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_scscfUser_setter(instance):
    original = instance.scscfUser
    instance.scscfUser = original
    assert instance.scscfUser == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaURI_setter(instance):
    original = instance.mediaURI
    instance.mediaURI = original
    assert instance.mediaURI == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaFromAddr_setter(instance):
    original = instance.mediaFromAddr
    instance.mediaFromAddr = original
    assert instance.mediaFromAddr == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaProtocol_setter(instance):
    original = instance.mediaProtocol
    instance.mediaProtocol = original
    assert instance.mediaProtocol == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_scscfPort_setter(instance):
    original = instance.scscfPort
    instance.scscfPort = original
    assert instance.scscfPort == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_mediaToAddr_setter(instance):
    original = instance.mediaToAddr
    instance.mediaToAddr = original
    assert instance.mediaToAddr == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_setupConference_setter(instance):
    original = instance.setupConference
    instance.setupConference = original
    assert instance.setupConference == original



@given(instance=stateMachine_Properties_strategy)
def test_statemachine_properties_scscfHost_setter(instance):
    original = instance.scscfHost
    instance.scscfHost = original
    assert instance.scscfHost == original

@given(instance=stateMachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, stateMachine_State)



@given(instance=stateMachine_State_strategy)
def test_statemachine_state_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original

@given(instance=stateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, stateMachine_StateMachine)



@given(instance=stateMachine_StateMachine_strategy)
def test_statemachine_statemachine_nombre_setter(instance):
    original = instance.nombre
    instance.nombre = original
    assert instance.nombre == original
