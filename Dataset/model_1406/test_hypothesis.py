import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smach::SMACHTransition,
    smach::SMACHState,
    Node,
    ServiceClient,
    SMACHState,
    smach::FinalState,
    smach::ServiceState,
    smach::InitActionState,
    smach::InitStraightState,
    ActionClient,
    smach::ActionState,
    smach::SMACHStateMachine,
    SMACHGoalTypes,
    SMACHStateOutcomes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smach::smachtransition_is_not_abstract():
    assert not inspect.isabstract(smach::SMACHTransition)


def test_smach::smachtransition_constructor_exists():
    assert callable(smach::SMACHTransition.__init__)


def test_smach::smachtransition_constructor_args():
    sig = inspect.signature(smach::SMACHTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smach::smachtransition_has_name():
    assert hasattr(smach::SMACHTransition, "name")
    descriptor = None
    for klass in smach::SMACHTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smach::smachstate_is_not_abstract():
    assert not inspect.isabstract(smach::SMACHState)


def test_smach::smachstate_constructor_exists():
    assert callable(smach::SMACHState.__init__)


def test_smach::smachstate_constructor_args():
    sig = inspect.signature(smach::SMACHState.__init__)
    params = list(sig.parameters.keys())
    assert "remap_overwrite" in params, "Missing parameter 'remap_overwrite'"
    assert "goal" in params, "Missing parameter 'goal'"
    assert "goal_type" in params, "Missing parameter 'goal_type'"

def test_smach::smachstate_has_remap_overwrite():
    assert hasattr(smach::SMACHState, "remap_overwrite")
    descriptor = None
    for klass in smach::SMACHState.__mro__:
        if "remap_overwrite" in klass.__dict__:
            descriptor = klass.__dict__["remap_overwrite"]
            break
    assert isinstance(descriptor, property)

def test_smach::smachstate_has_goal():
    assert hasattr(smach::SMACHState, "goal")
    descriptor = None
    for klass in smach::SMACHState.__mro__:
        if "goal" in klass.__dict__:
            descriptor = klass.__dict__["goal"]
            break
    assert isinstance(descriptor, property)

def test_smach::smachstate_has_goal_type():
    assert hasattr(smach::SMACHState, "goal_type")
    descriptor = None
    for klass in smach::SMACHState.__mro__:
        if "goal_type" in klass.__dict__:
            descriptor = klass.__dict__["goal_type"]
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



def test_smach::finalstate_is_not_abstract():
    assert not inspect.isabstract(smach::FinalState)


def test_smach::finalstate_constructor_exists():
    assert callable(smach::FinalState.__init__)


def test_smach::finalstate_constructor_args():
    sig = inspect.signature(smach::FinalState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_smach::finalstate_has_type():
    assert hasattr(smach::FinalState, "type")
    descriptor = None
    for klass in smach::FinalState.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_smach::servicestate_is_not_abstract():
    assert not inspect.isabstract(smach::ServiceState)


def test_smach::servicestate_constructor_exists():
    assert callable(smach::ServiceState.__init__)


def test_smach::servicestate_constructor_args():
    sig = inspect.signature(smach::ServiceState.__init__)
    params = list(sig.parameters.keys())



def test_smach::initactionstate_is_not_abstract():
    assert not inspect.isabstract(smach::InitActionState)


def test_smach::initactionstate_constructor_exists():
    assert callable(smach::InitActionState.__init__)


def test_smach::initactionstate_constructor_args():
    sig = inspect.signature(smach::InitActionState.__init__)
    params = list(sig.parameters.keys())



def test_smach::initstraightstate_is_not_abstract():
    assert not inspect.isabstract(smach::InitStraightState)


def test_smach::initstraightstate_constructor_exists():
    assert callable(smach::InitStraightState.__init__)


def test_smach::initstraightstate_constructor_args():
    sig = inspect.signature(smach::InitStraightState.__init__)
    params = list(sig.parameters.keys())



def test_actionclient_is_not_abstract():
    assert not inspect.isabstract(ActionClient)


def test_actionclient_constructor_exists():
    assert callable(ActionClient.__init__)


def test_actionclient_constructor_args():
    sig = inspect.signature(ActionClient.__init__)
    params = list(sig.parameters.keys())



def test_smach::actionstate_is_not_abstract():
    assert not inspect.isabstract(smach::ActionState)


def test_smach::actionstate_constructor_exists():
    assert callable(smach::ActionState.__init__)


def test_smach::actionstate_constructor_args():
    sig = inspect.signature(smach::ActionState.__init__)
    params = list(sig.parameters.keys())



def test_smach::smachstatemachine_is_not_abstract():
    assert not inspect.isabstract(smach::SMACHStateMachine)


def test_smach::smachstatemachine_constructor_exists():
    assert callable(smach::SMACHStateMachine.__init__)


def test_smach::smachstatemachine_constructor_args():
    sig = inspect.signature(smach::SMACHStateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "SkillInterface" in params, "Missing parameter 'SkillInterface'"

def test_smach::smachstatemachine_has_SkillInterface():
    assert hasattr(smach::SMACHStateMachine, "SkillInterface")
    descriptor = None
    for klass in smach::SMACHStateMachine.__mro__:
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
        "userdata_goal",
        "static_goal",
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
        "preempted",
        "succeeded",
        "aborted",
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
smach::SMACHTransition_strategy = st.builds(
    smach::SMACHTransition,
    name=
        safe_text
)
smach::SMACHState_strategy = st.builds(
    smach::SMACHState,
    remap_overwrite=
        safe_text,
    goal=
        safe_text,
    goal_type=
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
smach::FinalState_strategy = st.builds(
    smach::FinalState,
    type=
        safe_text
)
smach::ServiceState_strategy = st.builds(
    smach::ServiceState,
)
smach::InitActionState_strategy = st.builds(
    smach::InitActionState,
)
smach::InitStraightState_strategy = st.builds(
    smach::InitStraightState,
)
ActionClient_strategy = st.builds(
    ActionClient,
)
smach::ActionState_strategy = st.builds(
    smach::ActionState,
)
smach::SMACHStateMachine_strategy = st.builds(
    smach::SMACHStateMachine,
    SkillInterface=
        st.booleans()
)

@given(instance=smach::SMACHTransition_strategy)
@settings(max_examples=50)
def test_smach::smachtransition_instantiation(instance):
    assert isinstance(instance, smach::SMACHTransition)

@given(instance=smach::SMACHTransition_strategy)
def test_smach::smachtransition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smach::SMACHTransition_strategy)
def test_smach::smachtransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smach::SMACHState_strategy)
@settings(max_examples=50)
def test_smach::smachstate_instantiation(instance):
    assert isinstance(instance, smach::SMACHState)

@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_remap_overwrite_type(instance):
    assert isinstance(instance.remap_overwrite, str)


@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_remap_overwrite_setter(instance):
    original = instance.remap_overwrite
    instance.remap_overwrite = original
    assert instance.remap_overwrite == original

@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_goal_type(instance):
    assert isinstance(instance.goal, str)


@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_goal_setter(instance):
    original = instance.goal
    instance.goal = original
    assert instance.goal == original

@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_goal_type_type(instance):
    assert isinstance(instance.goal_type, str)


@given(instance=smach::SMACHState_strategy)
def test_smach::smachstate_goal_type_setter(instance):
    original = instance.goal_type
    instance.goal_type = original
    assert instance.goal_type == original

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

@given(instance=smach::FinalState_strategy)
@settings(max_examples=50)
def test_smach::finalstate_instantiation(instance):
    assert isinstance(instance, smach::FinalState)

@given(instance=smach::FinalState_strategy)
def test_smach::finalstate_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=smach::FinalState_strategy)
def test_smach::finalstate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=smach::ServiceState_strategy)
@settings(max_examples=50)
def test_smach::servicestate_instantiation(instance):
    assert isinstance(instance, smach::ServiceState)

@given(instance=smach::InitActionState_strategy)
@settings(max_examples=50)
def test_smach::initactionstate_instantiation(instance):
    assert isinstance(instance, smach::InitActionState)

@given(instance=smach::InitStraightState_strategy)
@settings(max_examples=50)
def test_smach::initstraightstate_instantiation(instance):
    assert isinstance(instance, smach::InitStraightState)

@given(instance=ActionClient_strategy)
@settings(max_examples=50)
def test_actionclient_instantiation(instance):
    assert isinstance(instance, ActionClient)

@given(instance=smach::ActionState_strategy)
@settings(max_examples=50)
def test_smach::actionstate_instantiation(instance):
    assert isinstance(instance, smach::ActionState)

@given(instance=smach::SMACHStateMachine_strategy)
@settings(max_examples=50)
def test_smach::smachstatemachine_instantiation(instance):
    assert isinstance(instance, smach::SMACHStateMachine)

@given(instance=smach::SMACHStateMachine_strategy)
def test_smach::smachstatemachine_SkillInterface_type(instance):
    assert isinstance(instance.SkillInterface, bool)


@given(instance=smach::SMACHStateMachine_strategy)
def test_smach::smachstatemachine_SkillInterface_setter(instance):
    original = instance.SkillInterface
    instance.SkillInterface = original
    assert instance.SkillInterface == original
