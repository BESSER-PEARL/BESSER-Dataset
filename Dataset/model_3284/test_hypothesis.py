import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smachDSL::Transition,
    smachDSL::ActionState,
    smachDSL::ServiceClient,
    smachDSL::ActionClient,
    smachDSL::Test,
    smachDSL::StateMachine,
    smachDSL::PrimitivePackage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smachdsl::transition_is_not_abstract():
    assert not inspect.isabstract(smachDSL::Transition)


def test_smachdsl::transition_constructor_exists():
    assert callable(smachDSL::Transition.__init__)


def test_smachdsl::transition_constructor_args():
    sig = inspect.signature(smachDSL::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "outcome" in params, "Missing parameter 'outcome'"

def test_smachdsl::transition_has_outcome():
    assert hasattr(smachDSL::Transition, "outcome")
    descriptor = None
    for klass in smachDSL::Transition.__mro__:
        if "outcome" in klass.__dict__:
            descriptor = klass.__dict__["outcome"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::actionstate_is_not_abstract():
    assert not inspect.isabstract(smachDSL::ActionState)


def test_smachdsl::actionstate_constructor_exists():
    assert callable(smachDSL::ActionState.__init__)


def test_smachdsl::actionstate_constructor_args():
    sig = inspect.signature(smachDSL::ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl::actionstate_has_name():
    assert hasattr(smachDSL::ActionState, "name")
    descriptor = None
    for klass in smachDSL::ActionState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::serviceclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL::ServiceClient)


def test_smachdsl::serviceclient_constructor_exists():
    assert callable(smachDSL::ServiceClient.__init__)


def test_smachdsl::serviceclient_constructor_args():
    sig = inspect.signature(smachDSL::ServiceClient.__init__)
    params = list(sig.parameters.keys())
    assert "servicename" in params, "Missing parameter 'servicename'"
    assert "servicesrv" in params, "Missing parameter 'servicesrv'"
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl::serviceclient_has_servicename():
    assert hasattr(smachDSL::ServiceClient, "servicename")
    descriptor = None
    for klass in smachDSL::ServiceClient.__mro__:
        if "servicename" in klass.__dict__:
            descriptor = klass.__dict__["servicename"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl::serviceclient_has_servicesrv():
    assert hasattr(smachDSL::ServiceClient, "servicesrv")
    descriptor = None
    for klass in smachDSL::ServiceClient.__mro__:
        if "servicesrv" in klass.__dict__:
            descriptor = klass.__dict__["servicesrv"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl::serviceclient_has_name():
    assert hasattr(smachDSL::ServiceClient, "name")
    descriptor = None
    for klass in smachDSL::ServiceClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::actionclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL::ActionClient)


def test_smachdsl::actionclient_constructor_exists():
    assert callable(smachDSL::ActionClient.__init__)


def test_smachdsl::actionclient_constructor_args():
    sig = inspect.signature(smachDSL::ActionClient.__init__)
    params = list(sig.parameters.keys())
    assert "actionname" in params, "Missing parameter 'actionname'"
    assert "actiontype" in params, "Missing parameter 'actiontype'"
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl::actionclient_has_actionname():
    assert hasattr(smachDSL::ActionClient, "actionname")
    descriptor = None
    for klass in smachDSL::ActionClient.__mro__:
        if "actionname" in klass.__dict__:
            descriptor = klass.__dict__["actionname"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl::actionclient_has_actiontype():
    assert hasattr(smachDSL::ActionClient, "actiontype")
    descriptor = None
    for klass in smachDSL::ActionClient.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl::actionclient_has_name():
    assert hasattr(smachDSL::ActionClient, "name")
    descriptor = None
    for klass in smachDSL::ActionClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::test_is_not_abstract():
    assert not inspect.isabstract(smachDSL::Test)


def test_smachdsl::test_constructor_exists():
    assert callable(smachDSL::Test.__init__)


def test_smachdsl::test_constructor_args():
    sig = inspect.signature(smachDSL::Test.__init__)
    params = list(sig.parameters.keys())
    assert "ros" in params, "Missing parameter 'ros'"

def test_smachdsl::test_has_ros():
    assert hasattr(smachDSL::Test, "ros")
    descriptor = None
    for klass in smachDSL::Test.__mro__:
        if "ros" in klass.__dict__:
            descriptor = klass.__dict__["ros"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::statemachine_is_not_abstract():
    assert not inspect.isabstract(smachDSL::StateMachine)


def test_smachdsl::statemachine_constructor_exists():
    assert callable(smachDSL::StateMachine.__init__)


def test_smachdsl::statemachine_constructor_args():
    sig = inspect.signature(smachDSL::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl::statemachine_has_name():
    assert hasattr(smachDSL::StateMachine, "name")
    descriptor = None
    for klass in smachDSL::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl::primitivepackage_is_not_abstract():
    assert not inspect.isabstract(smachDSL::PrimitivePackage)


def test_smachdsl::primitivepackage_constructor_exists():
    assert callable(smachDSL::PrimitivePackage.__init__)


def test_smachdsl::primitivepackage_constructor_args():
    sig = inspect.signature(smachDSL::PrimitivePackage.__init__)
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
smachDSL::Transition_strategy = st.builds(
    smachDSL::Transition,
    outcome=
        safe_text
)
smachDSL::ActionState_strategy = st.builds(
    smachDSL::ActionState,
    name=
        safe_text
)
smachDSL::ServiceClient_strategy = st.builds(
    smachDSL::ServiceClient,
    servicename=
        safe_text,
    servicesrv=
        safe_text,
    name=
        safe_text
)
smachDSL::ActionClient_strategy = st.builds(
    smachDSL::ActionClient,
    actionname=
        safe_text,
    actiontype=
        safe_text,
    name=
        safe_text
)
smachDSL::Test_strategy = st.builds(
    smachDSL::Test,
    ros=
        safe_text
)
smachDSL::StateMachine_strategy = st.builds(
    smachDSL::StateMachine,
    name=
        safe_text
)
smachDSL::PrimitivePackage_strategy = st.builds(
    smachDSL::PrimitivePackage,
)

@given(instance=smachDSL::Transition_strategy)
@settings(max_examples=50)
def test_smachdsl::transition_instantiation(instance):
    assert isinstance(instance, smachDSL::Transition)

@given(instance=smachDSL::Transition_strategy)
def test_smachdsl::transition_outcome_type(instance):
    assert isinstance(instance.outcome, str)


@given(instance=smachDSL::Transition_strategy)
def test_smachdsl::transition_outcome_setter(instance):
    original = instance.outcome
    instance.outcome = original
    assert instance.outcome == original

@given(instance=smachDSL::ActionState_strategy)
@settings(max_examples=50)
def test_smachdsl::actionstate_instantiation(instance):
    assert isinstance(instance, smachDSL::ActionState)

@given(instance=smachDSL::ActionState_strategy)
def test_smachdsl::actionstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smachDSL::ActionState_strategy)
def test_smachdsl::actionstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL::ServiceClient_strategy)
@settings(max_examples=50)
def test_smachdsl::serviceclient_instantiation(instance):
    assert isinstance(instance, smachDSL::ServiceClient)

@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_servicename_type(instance):
    assert isinstance(instance.servicename, str)


@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_servicename_setter(instance):
    original = instance.servicename
    instance.servicename = original
    assert instance.servicename == original

@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_servicesrv_type(instance):
    assert isinstance(instance.servicesrv, str)


@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_servicesrv_setter(instance):
    original = instance.servicesrv
    instance.servicesrv = original
    assert instance.servicesrv == original

@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smachDSL::ServiceClient_strategy)
def test_smachdsl::serviceclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL::ActionClient_strategy)
@settings(max_examples=50)
def test_smachdsl::actionclient_instantiation(instance):
    assert isinstance(instance, smachDSL::ActionClient)

@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_actionname_type(instance):
    assert isinstance(instance.actionname, str)


@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_actionname_setter(instance):
    original = instance.actionname
    instance.actionname = original
    assert instance.actionname == original

@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_actiontype_type(instance):
    assert isinstance(instance.actiontype, str)


@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original

@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smachDSL::ActionClient_strategy)
def test_smachdsl::actionclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL::Test_strategy)
@settings(max_examples=50)
def test_smachdsl::test_instantiation(instance):
    assert isinstance(instance, smachDSL::Test)

@given(instance=smachDSL::Test_strategy)
def test_smachdsl::test_ros_type(instance):
    assert isinstance(instance.ros, str)


@given(instance=smachDSL::Test_strategy)
def test_smachdsl::test_ros_setter(instance):
    original = instance.ros
    instance.ros = original
    assert instance.ros == original

@given(instance=smachDSL::StateMachine_strategy)
@settings(max_examples=50)
def test_smachdsl::statemachine_instantiation(instance):
    assert isinstance(instance, smachDSL::StateMachine)

@given(instance=smachDSL::StateMachine_strategy)
def test_smachdsl::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smachDSL::StateMachine_strategy)
def test_smachdsl::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL::PrimitivePackage_strategy)
@settings(max_examples=50)
def test_smachdsl::primitivepackage_instantiation(instance):
    assert isinstance(instance, smachDSL::PrimitivePackage)
