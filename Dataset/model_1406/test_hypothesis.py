import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smach_SMACHTransition,
    smach_SMACHState,
    Node,
    ServiceClient,
    SMACHState,
    smach_InitActionState,
    smach_InitStraightState,
    smach_ServiceState,
    smach_FinalState,
    ActionClient,
    smach_ActionState,
    smach_SMACHStateMachine,
    SMACHGoalTypes,
    SMACHStateOutcomes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smach_smachtransition_is_not_abstract():
    assert not inspect.isabstract(smach_SMACHTransition)


def test_smach_smachtransition_constructor_exists():
    assert callable(smach_SMACHTransition.__init__)


def test_smach_smachtransition_constructor_args():
    sig = inspect.signature(smach_SMACHTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smach_smachtransition_has_name():
    assert hasattr(smach_SMACHTransition, "name")
    descriptor = None
    for klass in smach_SMACHTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smach_smachstate_is_not_abstract():
    assert not inspect.isabstract(smach_SMACHState)


def test_smach_smachstate_constructor_exists():
    assert callable(smach_SMACHState.__init__)


def test_smach_smachstate_constructor_args():
    sig = inspect.signature(smach_SMACHState.__init__)
    params = list(sig.parameters.keys())
    assert "goal_type" in params, "Missing parameter 'goal_type'"
    assert "goal" in params, "Missing parameter 'goal'"
    assert "remap_overwrite" in params, "Missing parameter 'remap_overwrite'"

def test_smach_smachstate_has_goal_type():
    assert hasattr(smach_SMACHState, "goal_type")
    descriptor = None
    for klass in smach_SMACHState.__mro__:
        if "goal_type" in klass.__dict__:
            descriptor = klass.__dict__["goal_type"]
            break
    assert isinstance(descriptor, property)

def test_smach_smachstate_has_goal():
    assert hasattr(smach_SMACHState, "goal")
    descriptor = None
    for klass in smach_SMACHState.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)

def test_smach_smachstate_has_remap_overwrite():
    assert hasattr(smach_SMACHState, "remap_overwrite")
    descriptor = None
    for klass in smach_SMACHState.__mro__:
        if "remap_overwrite" in klass.__dict__:
            descriptor = klass.__dict__["remap_overwrite"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_serviceclient_is_not_abstract():
    assert not inspect.isabstract(ServiceClient)


def test_serviceclient_constructor_exists():
    assert callable(ServiceClient.__init__)


def test_serviceclient_constructor_args():
    sig = inspect.signature(ServiceClient.__init__)
    params = list(sig.parameters.keys())



def test_smachstate_is_not_abstract():
    assert not inspect.isabstract(SMACHState)


def test_smachstate_constructor_exists():
    assert callable(SMACHState.__init__)


def test_smachstate_constructor_args():
    sig = inspect.signature(SMACHState.__init__)
    params = list(sig.parameters.keys())



def test_smach_initactionstate_is_not_abstract():
    assert not inspect.isabstract(smach_InitActionState)


def test_smach_initactionstate_constructor_exists():
    assert callable(smach_InitActionState.__init__)


def test_smach_initactionstate_constructor_args():
    sig = inspect.signature(smach_InitActionState.__init__)
    params = list(sig.parameters.keys())



def test_smach_initstraightstate_is_not_abstract():
    assert not inspect.isabstract(smach_InitStraightState)


def test_smach_initstraightstate_constructor_exists():
    assert callable(smach_InitStraightState.__init__)


def test_smach_initstraightstate_constructor_args():
    sig = inspect.signature(smach_InitStraightState.__init__)
    params = list(sig.parameters.keys())



def test_smach_servicestate_is_not_abstract():
    assert not inspect.isabstract(smach_ServiceState)


def test_smach_servicestate_constructor_exists():
    assert callable(smach_ServiceState.__init__)


def test_smach_servicestate_constructor_args():
    sig = inspect.signature(smach_ServiceState.__init__)
    params = list(sig.parameters.keys())



def test_smach_finalstate_is_not_abstract():
    assert not inspect.isabstract(smach_FinalState)


def test_smach_finalstate_constructor_exists():
    assert callable(smach_FinalState.__init__)


def test_smach_finalstate_constructor_args():
    sig = inspect.signature(smach_FinalState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_smach_finalstate_has_type():
    assert hasattr(smach_FinalState, "type")
    descriptor = None
    for klass in smach_FinalState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_actionclient_is_not_abstract():
    assert not inspect.isabstract(ActionClient)


def test_actionclient_constructor_exists():
    assert callable(ActionClient.__init__)


def test_actionclient_constructor_args():
    sig = inspect.signature(ActionClient.__init__)
    params = list(sig.parameters.keys())



def test_smach_actionstate_is_not_abstract():
    assert not inspect.isabstract(smach_ActionState)


def test_smach_actionstate_constructor_exists():
    assert callable(smach_ActionState.__init__)


def test_smach_actionstate_constructor_args():
    sig = inspect.signature(smach_ActionState.__init__)
    params = list(sig.parameters.keys())



def test_smach_smachstatemachine_is_not_abstract():
    assert not inspect.isabstract(smach_SMACHStateMachine)


def test_smach_smachstatemachine_constructor_exists():
    assert callable(smach_SMACHStateMachine.__init__)


def test_smach_smachstatemachine_constructor_args():
    sig = inspect.signature(smach_SMACHStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "SkillInterface" in params, "Missing parameter 'SkillInterface'"

def test_smach_smachstatemachine_has_SkillInterface():
    assert hasattr(smach_SMACHStateMachine, "SkillInterface")
    descriptor = None
    for klass in smach_SMACHStateMachine.__mro__:
        if "SkillInterface" in klass.__dict__:
            descriptor = klass.__dict__["SkillInterface"]
            break
    assert isinstance(descriptor, property)

def test_smachgoaltypes_exists():
    # Check that the Enumeration exists
    assert SMACHGoalTypes is not None

def test_smachgoaltypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SMACHGoalTypes]
    expected_literals = [
        "static_goal",
        "userdata_goal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SMACHGoalTypes"

def test_smachstateoutcomes_exists():
    # Check that the Enumeration exists
    assert SMACHStateOutcomes is not None

def test_smachstateoutcomes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SMACHStateOutcomes]
    expected_literals = [
        "succeeded",
        "aborted",
        "preempted",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SMACHStateOutcomes"


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
smach_SMACHTransition_strategy = st.builds(
    smach_SMACHTransition,
    name=
        safe_text
)
smach_SMACHState_strategy = st.builds(
    smach_SMACHState,
    goal_type=
        safe_text,
    goal=
        safe_text,
    remap_overwrite=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
ServiceClient_strategy = st.builds(
    ServiceClient,
)
SMACHState_strategy = st.builds(
    SMACHState,
)
smach_InitActionState_strategy = st.builds(
    smach_InitActionState,
)
smach_InitStraightState_strategy = st.builds(
    smach_InitStraightState,
)
smach_ServiceState_strategy = st.builds(
    smach_ServiceState,
)
smach_FinalState_strategy = st.builds(
    smach_FinalState,
    type=
        safe_text
)
ActionClient_strategy = st.builds(
    ActionClient,
)
smach_ActionState_strategy = st.builds(
    smach_ActionState,
)
smach_SMACHStateMachine_strategy = st.builds(
    smach_SMACHStateMachine,
    SkillInterface=
        st.booleans()
)

@given(instance=smach_SMACHTransition_strategy)
@settings(max_examples=50)
def test_smach_smachtransition_instantiation(instance):
    assert isinstance(instance, smach_SMACHTransition)



@given(instance=smach_SMACHTransition_strategy)
def test_smach_smachtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smach_SMACHState_strategy)
@settings(max_examples=50)
def test_smach_smachstate_instantiation(instance):
    assert isinstance(instance, smach_SMACHState)



@given(instance=smach_SMACHState_strategy)
def test_smach_smachstate_goal_type_setter(instance):
    original = instance.goal_type
    instance.goal_type = original
    assert instance.goal_type == original



@given(instance=smach_SMACHState_strategy)
def test_smach_smachstate_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original



@given(instance=smach_SMACHState_strategy)
def test_smach_smachstate_remap_overwrite_setter(instance):
    original = instance.remap_overwrite
    instance.remap_overwrite = original
    assert instance.remap_overwrite == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ServiceClient_strategy)
@settings(max_examples=50)
def test_serviceclient_instantiation(instance):
    assert isinstance(instance, ServiceClient)

@given(instance=SMACHState_strategy)
@settings(max_examples=50)
def test_smachstate_instantiation(instance):
    assert isinstance(instance, SMACHState)

@given(instance=smach_InitActionState_strategy)
@settings(max_examples=50)
def test_smach_initactionstate_instantiation(instance):
    assert isinstance(instance, smach_InitActionState)

@given(instance=smach_InitStraightState_strategy)
@settings(max_examples=50)
def test_smach_initstraightstate_instantiation(instance):
    assert isinstance(instance, smach_InitStraightState)

@given(instance=smach_ServiceState_strategy)
@settings(max_examples=50)
def test_smach_servicestate_instantiation(instance):
    assert isinstance(instance, smach_ServiceState)

@given(instance=smach_FinalState_strategy)
@settings(max_examples=50)
def test_smach_finalstate_instantiation(instance):
    assert isinstance(instance, smach_FinalState)



@given(instance=smach_FinalState_strategy)
def test_smach_finalstate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ActionClient_strategy)
@settings(max_examples=50)
def test_actionclient_instantiation(instance):
    assert isinstance(instance, ActionClient)

@given(instance=smach_ActionState_strategy)
@settings(max_examples=50)
def test_smach_actionstate_instantiation(instance):
    assert isinstance(instance, smach_ActionState)

@given(instance=smach_SMACHStateMachine_strategy)
@settings(max_examples=50)
def test_smach_smachstatemachine_instantiation(instance):
    assert isinstance(instance, smach_SMACHStateMachine)



@given(instance=smach_SMACHStateMachine_strategy)
def test_smach_smachstatemachine_SkillInterface_setter(instance):
    original = instance.SkillInterface
    instance.SkillInterface = original
    assert instance.SkillInterface == original
