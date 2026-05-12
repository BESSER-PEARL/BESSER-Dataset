import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smachDSL_ActionState,
    smachDSL_ServiceClient,
    smachDSL_Transition,
    smachDSL_Test,
    smachDSL_StateMachine,
    smachDSL_PrimitivePackage,
    smachDSL_ActionClient,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smachdsl_actionstate_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ActionState)


def test_smachdsl_actionstate_constructor_exists():
    assert callable(smachDSL_ActionState.__init__)


def test_smachdsl_actionstate_constructor_args():
    sig = inspect.signature(smachDSL_ActionState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl_actionstate_has_name():
    assert hasattr(smachDSL_ActionState, "name")
    descriptor = None
    for klass in smachDSL_ActionState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl_serviceclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ServiceClient)


def test_smachdsl_serviceclient_constructor_exists():
    assert callable(smachDSL_ServiceClient.__init__)


def test_smachdsl_serviceclient_constructor_args():
    sig = inspect.signature(smachDSL_ServiceClient.__init__)
    params = list(sig.parameters.keys())
    assert "servicename" in params, "Missing parameter 'servicename'"
    assert "servicesrv" in params, "Missing parameter 'servicesrv'"
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl_serviceclient_has_servicename():
    assert hasattr(smachDSL_ServiceClient, "servicename")
    descriptor = None
    for klass in smachDSL_ServiceClient.__mro__:
        if "servicename" in klass.__dict__:
            descriptor = klass.__dict__["servicename"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl_serviceclient_has_servicesrv():
    assert hasattr(smachDSL_ServiceClient, "servicesrv")
    descriptor = None
    for klass in smachDSL_ServiceClient.__mro__:
        if "servicesrv" in klass.__dict__:
            descriptor = klass.__dict__["servicesrv"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl_serviceclient_has_name():
    assert hasattr(smachDSL_ServiceClient, "name")
    descriptor = None
    for klass in smachDSL_ServiceClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl_transition_is_not_abstract():
    assert not inspect.isabstract(smachDSL_Transition)


def test_smachdsl_transition_constructor_exists():
    assert callable(smachDSL_Transition.__init__)


def test_smachdsl_transition_constructor_args():
    sig = inspect.signature(smachDSL_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "outcome" in params, "Missing parameter 'outcome'"

def test_smachdsl_transition_has_outcome():
    assert hasattr(smachDSL_Transition, "outcome")
    descriptor = None
    for klass in smachDSL_Transition.__mro__:
        if "outcome" in klass.__dict__:
            descriptor = klass.__dict__["outcome"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl_test_is_not_abstract():
    assert not inspect.isabstract(smachDSL_Test)


def test_smachdsl_test_constructor_exists():
    assert callable(smachDSL_Test.__init__)


def test_smachdsl_test_constructor_args():
    sig = inspect.signature(smachDSL_Test.__init__)
    params = list(sig.parameters.keys())
    assert "ros" in params, "Missing parameter 'ros'"

def test_smachdsl_test_has_ros():
    assert hasattr(smachDSL_Test, "ros")
    descriptor = None
    for klass in smachDSL_Test.__mro__:
        if "ros" in klass.__dict__:
            descriptor = klass.__dict__["ros"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl_statemachine_is_not_abstract():
    assert not inspect.isabstract(smachDSL_StateMachine)


def test_smachdsl_statemachine_constructor_exists():
    assert callable(smachDSL_StateMachine.__init__)


def test_smachdsl_statemachine_constructor_args():
    sig = inspect.signature(smachDSL_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smachdsl_statemachine_has_name():
    assert hasattr(smachDSL_StateMachine, "name")
    descriptor = None
    for klass in smachDSL_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smachdsl_primitivepackage_is_not_abstract():
    assert not inspect.isabstract(smachDSL_PrimitivePackage)


def test_smachdsl_primitivepackage_constructor_exists():
    assert callable(smachDSL_PrimitivePackage.__init__)


def test_smachdsl_primitivepackage_constructor_args():
    sig = inspect.signature(smachDSL_PrimitivePackage.__init__)
    params = list(sig.parameters.keys())



def test_smachdsl_actionclient_is_not_abstract():
    assert not inspect.isabstract(smachDSL_ActionClient)


def test_smachdsl_actionclient_constructor_exists():
    assert callable(smachDSL_ActionClient.__init__)


def test_smachdsl_actionclient_constructor_args():
    sig = inspect.signature(smachDSL_ActionClient.__init__)
    params = list(sig.parameters.keys())
    assert "actionname" in params, "Missing parameter 'actionname'"
    assert "name" in params, "Missing parameter 'name'"
    assert "actiontype" in params, "Missing parameter 'actiontype'"

def test_smachdsl_actionclient_has_actionname():
    assert hasattr(smachDSL_ActionClient, "actionname")
    descriptor = None
    for klass in smachDSL_ActionClient.__mro__:
        if "actionname" in klass.__dict__:
            descriptor = klass.__dict__["actionname"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl_actionclient_has_name():
    assert hasattr(smachDSL_ActionClient, "name")
    descriptor = None
    for klass in smachDSL_ActionClient.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smachdsl_actionclient_has_actiontype():
    assert hasattr(smachDSL_ActionClient, "actiontype")
    descriptor = None
    for klass in smachDSL_ActionClient.__mro__:
        if "actiontype" in klass.__dict__:
            descriptor = klass.__dict__["actiontype"]
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
smachDSL_ActionState_strategy = st.builds(
    smachDSL_ActionState,
    name=
        safe_text
)
smachDSL_ServiceClient_strategy = st.builds(
    smachDSL_ServiceClient,
    servicename=
        safe_text,
    servicesrv=
        safe_text,
    name=
        safe_text
)
smachDSL_Transition_strategy = st.builds(
    smachDSL_Transition,
    outcome=
        safe_text
)
smachDSL_Test_strategy = st.builds(
    smachDSL_Test,
    ros=
        safe_text
)
smachDSL_StateMachine_strategy = st.builds(
    smachDSL_StateMachine,
    name=
        safe_text
)
smachDSL_PrimitivePackage_strategy = st.builds(
    smachDSL_PrimitivePackage,
)
smachDSL_ActionClient_strategy = st.builds(
    smachDSL_ActionClient,
    actionname=
        safe_text,
    name=
        safe_text,
    actiontype=
        safe_text
)

@given(instance=smachDSL_ActionState_strategy)
@settings(max_examples=50)
def test_smachdsl_actionstate_instantiation(instance):
    assert isinstance(instance, smachDSL_ActionState)



@given(instance=smachDSL_ActionState_strategy)
def test_smachdsl_actionstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL_ServiceClient_strategy)
@settings(max_examples=50)
def test_smachdsl_serviceclient_instantiation(instance):
    assert isinstance(instance, smachDSL_ServiceClient)



@given(instance=smachDSL_ServiceClient_strategy)
def test_smachdsl_serviceclient_servicename_setter(instance):
    original = instance.servicename
    instance.servicename = original
    assert instance.servicename == original



@given(instance=smachDSL_ServiceClient_strategy)
def test_smachdsl_serviceclient_servicesrv_setter(instance):
    original = instance.servicesrv
    instance.servicesrv = original
    assert instance.servicesrv == original



@given(instance=smachDSL_ServiceClient_strategy)
def test_smachdsl_serviceclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL_Transition_strategy)
@settings(max_examples=50)
def test_smachdsl_transition_instantiation(instance):
    assert isinstance(instance, smachDSL_Transition)



@given(instance=smachDSL_Transition_strategy)
def test_smachdsl_transition_outcome_setter(instance):
    original = instance.outcome
    instance.outcome = original
    assert instance.outcome == original

@given(instance=smachDSL_Test_strategy)
@settings(max_examples=50)
def test_smachdsl_test_instantiation(instance):
    assert isinstance(instance, smachDSL_Test)



@given(instance=smachDSL_Test_strategy)
def test_smachdsl_test_ros_setter(instance):
    original = instance.ros
    instance.ros = original
    assert instance.ros == original

@given(instance=smachDSL_StateMachine_strategy)
@settings(max_examples=50)
def test_smachdsl_statemachine_instantiation(instance):
    assert isinstance(instance, smachDSL_StateMachine)



@given(instance=smachDSL_StateMachine_strategy)
def test_smachdsl_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smachDSL_PrimitivePackage_strategy)
@settings(max_examples=50)
def test_smachdsl_primitivepackage_instantiation(instance):
    assert isinstance(instance, smachDSL_PrimitivePackage)

@given(instance=smachDSL_ActionClient_strategy)
@settings(max_examples=50)
def test_smachdsl_actionclient_instantiation(instance):
    assert isinstance(instance, smachDSL_ActionClient)



@given(instance=smachDSL_ActionClient_strategy)
def test_smachdsl_actionclient_actionname_setter(instance):
    original = instance.actionname
    instance.actionname = original
    assert instance.actionname == original



@given(instance=smachDSL_ActionClient_strategy)
def test_smachdsl_actionclient_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=smachDSL_ActionClient_strategy)
def test_smachdsl_actionclient_actiontype_setter(instance):
    original = instance.actiontype
    instance.actiontype = original
    assert instance.actiontype == original
