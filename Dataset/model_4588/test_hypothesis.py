import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ExecutableNode,
    PiServiceComposition_Action,
    Activity,
    PiServiceComposition_ServiceActivity,
    FinalNode,
    PiServiceComposition_ActivityFinalNode,
    PiServiceComposition_Rule,
    ActivityPartition,
    PiServiceComposition_BussinessCollaborator,
    ControlNode,
    PiServiceComposition_FinalNode,
    PiServiceComposition_MergeNode,
    PiServiceComposition_DecisionNode,
    PiServiceComposition_ForkNode,
    PiServiceComposition_JoinNode,
    PiServiceComposition_InitialNode,
    ActivityNode,
    PiServiceComposition_ControlNode,
    PiServiceComposition_ObjectNode,
    PiServiceComposition_ExecutableNode,
    ActivityEdge,
    PiServiceComposition_ObjectFlow,
    PiServiceComposition_ControlFlow,
    NamedElement,
    PiServiceComposition_ActivityNode,
    PiServiceComposition_NamedElement,
    PiServiceComposition_Variable,
    PiServiceComposition_Policy,
    PiServiceComposition_ActivityEdge,
    PiServiceComposition_Activity,
    PiServiceComposition_ActivityPartition,
    PiServiceComposition_CompositionServiceModel,
    EventType,
    ActionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_action_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_Action)


def test_piservicecomposition_action_constructor_exists():
    assert callable(PiServiceComposition_Action.__init__)


def test_piservicecomposition_action_constructor_args():
    sig = inspect.signature(PiServiceComposition_Action.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_piservicecomposition_action_has_type():
    assert hasattr(PiServiceComposition_Action, "type")
    descriptor = None
    for klass in PiServiceComposition_Action.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_serviceactivity_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ServiceActivity)


def test_piservicecomposition_serviceactivity_constructor_exists():
    assert callable(PiServiceComposition_ServiceActivity.__init__)


def test_piservicecomposition_serviceactivity_constructor_args():
    sig = inspect.signature(PiServiceComposition_ServiceActivity.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ActivityFinalNode)


def test_piservicecomposition_activityfinalnode_constructor_exists():
    assert callable(PiServiceComposition_ActivityFinalNode.__init__)


def test_piservicecomposition_activityfinalnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_rule_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_Rule)


def test_piservicecomposition_rule_constructor_exists():
    assert callable(PiServiceComposition_Rule.__init__)


def test_piservicecomposition_rule_constructor_args():
    sig = inspect.signature(PiServiceComposition_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"
    assert "name" in params, "Missing parameter 'name'"
    assert "event" in params, "Missing parameter 'event'"
    assert "action" in params, "Missing parameter 'action'"

def test_piservicecomposition_rule_has_condition():
    assert hasattr(PiServiceComposition_Rule, "condition")
    descriptor = None
    for klass in PiServiceComposition_Rule.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition_rule_has_name():
    assert hasattr(PiServiceComposition_Rule, "name")
    descriptor = None
    for klass in PiServiceComposition_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition_rule_has_event():
    assert hasattr(PiServiceComposition_Rule, "event")
    descriptor = None
    for klass in PiServiceComposition_Rule.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition_rule_has_action():
    assert hasattr(PiServiceComposition_Rule, "action")
    descriptor = None
    for klass in PiServiceComposition_Rule.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_activitypartition_is_not_abstract():
    assert not inspect.isabstract(ActivityPartition)


def test_activitypartition_constructor_exists():
    assert callable(ActivityPartition.__init__)


def test_activitypartition_constructor_args():
    sig = inspect.signature(ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_bussinesscollaborator_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_BussinessCollaborator)


def test_piservicecomposition_bussinesscollaborator_constructor_exists():
    assert callable(PiServiceComposition_BussinessCollaborator.__init__)


def test_piservicecomposition_bussinesscollaborator_constructor_args():
    sig = inspect.signature(PiServiceComposition_BussinessCollaborator.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_finalnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_FinalNode)


def test_piservicecomposition_finalnode_constructor_exists():
    assert callable(PiServiceComposition_FinalNode.__init__)


def test_piservicecomposition_finalnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_mergenode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_MergeNode)


def test_piservicecomposition_mergenode_constructor_exists():
    assert callable(PiServiceComposition_MergeNode.__init__)


def test_piservicecomposition_mergenode_constructor_args():
    sig = inspect.signature(PiServiceComposition_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_decisionnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_DecisionNode)


def test_piservicecomposition_decisionnode_constructor_exists():
    assert callable(PiServiceComposition_DecisionNode.__init__)


def test_piservicecomposition_decisionnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_forknode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ForkNode)


def test_piservicecomposition_forknode_constructor_exists():
    assert callable(PiServiceComposition_ForkNode.__init__)


def test_piservicecomposition_forknode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_joinnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_JoinNode)


def test_piservicecomposition_joinnode_constructor_exists():
    assert callable(PiServiceComposition_JoinNode.__init__)


def test_piservicecomposition_joinnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_initialnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_InitialNode)


def test_piservicecomposition_initialnode_constructor_exists():
    assert callable(PiServiceComposition_InitialNode.__init__)


def test_piservicecomposition_initialnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_controlnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ControlNode)


def test_piservicecomposition_controlnode_constructor_exists():
    assert callable(PiServiceComposition_ControlNode.__init__)


def test_piservicecomposition_controlnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_objectnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ObjectNode)


def test_piservicecomposition_objectnode_constructor_exists():
    assert callable(PiServiceComposition_ObjectNode.__init__)


def test_piservicecomposition_objectnode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_executablenode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ExecutableNode)


def test_piservicecomposition_executablenode_constructor_exists():
    assert callable(PiServiceComposition_ExecutableNode.__init__)


def test_piservicecomposition_executablenode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_objectflow_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ObjectFlow)


def test_piservicecomposition_objectflow_constructor_exists():
    assert callable(PiServiceComposition_ObjectFlow.__init__)


def test_piservicecomposition_objectflow_constructor_args():
    sig = inspect.signature(PiServiceComposition_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_controlflow_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ControlFlow)


def test_piservicecomposition_controlflow_constructor_exists():
    assert callable(PiServiceComposition_ControlFlow.__init__)


def test_piservicecomposition_controlflow_constructor_args():
    sig = inspect.signature(PiServiceComposition_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_activitynode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ActivityNode)


def test_piservicecomposition_activitynode_constructor_exists():
    assert callable(PiServiceComposition_ActivityNode.__init__)


def test_piservicecomposition_activitynode_constructor_args():
    sig = inspect.signature(PiServiceComposition_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_namedelement_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_NamedElement)


def test_piservicecomposition_namedelement_constructor_exists():
    assert callable(PiServiceComposition_NamedElement.__init__)


def test_piservicecomposition_namedelement_constructor_args():
    sig = inspect.signature(PiServiceComposition_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition_namedelement_has_name():
    assert hasattr(PiServiceComposition_NamedElement, "name")
    descriptor = None
    for klass in PiServiceComposition_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition_variable_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_Variable)


def test_piservicecomposition_variable_constructor_exists():
    assert callable(PiServiceComposition_Variable.__init__)


def test_piservicecomposition_variable_constructor_args():
    sig = inspect.signature(PiServiceComposition_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition_variable_has_type():
    assert hasattr(PiServiceComposition_Variable, "type")
    descriptor = None
    for klass in PiServiceComposition_Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition_variable_has_name():
    assert hasattr(PiServiceComposition_Variable, "name")
    descriptor = None
    for klass in PiServiceComposition_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition_policy_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_Policy)


def test_piservicecomposition_policy_constructor_exists():
    assert callable(PiServiceComposition_Policy.__init__)


def test_piservicecomposition_policy_constructor_args():
    sig = inspect.signature(PiServiceComposition_Policy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition_policy_has_name():
    assert hasattr(PiServiceComposition_Policy, "name")
    descriptor = None
    for klass in PiServiceComposition_Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition_activityedge_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ActivityEdge)


def test_piservicecomposition_activityedge_constructor_exists():
    assert callable(PiServiceComposition_ActivityEdge.__init__)


def test_piservicecomposition_activityedge_constructor_args():
    sig = inspect.signature(PiServiceComposition_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_activity_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_Activity)


def test_piservicecomposition_activity_constructor_exists():
    assert callable(PiServiceComposition_Activity.__init__)


def test_piservicecomposition_activity_constructor_args():
    sig = inspect.signature(PiServiceComposition_Activity.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition_activitypartition_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_ActivityPartition)


def test_piservicecomposition_activitypartition_constructor_exists():
    assert callable(PiServiceComposition_ActivityPartition.__init__)


def test_piservicecomposition_activitypartition_constructor_args():
    sig = inspect.signature(PiServiceComposition_ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "isDimension" in params, "Missing parameter 'isDimension'"

def test_piservicecomposition_activitypartition_has_isExternal():
    assert hasattr(PiServiceComposition_ActivityPartition, "isExternal")
    descriptor = None
    for klass in PiServiceComposition_ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition_activitypartition_has_isDimension():
    assert hasattr(PiServiceComposition_ActivityPartition, "isDimension")
    descriptor = None
    for klass in PiServiceComposition_ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition_compositionservicemodel_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition_CompositionServiceModel)


def test_piservicecomposition_compositionservicemodel_constructor_exists():
    assert callable(PiServiceComposition_CompositionServiceModel.__init__)


def test_piservicecomposition_compositionservicemodel_constructor_args():
    sig = inspect.signature(PiServiceComposition_CompositionServiceModel.__init__)
    params = list(sig.parameters.keys())

def test_eventtype_exists():
    # Check that the Enumeration exists
    assert EventType is not None

def test_eventtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventType]
    expected_literals = [
        "TIME",
        "PRE",
        "POST",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventType"

def test_actiontype_exists():
    # Check that the Enumeration exists
    assert ActionType is not None

def test_actiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionType]
    expected_literals = [
        "AOP",
        "WS",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionType"


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
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
PiServiceComposition_Action_strategy = st.builds(
    PiServiceComposition_Action,
    type=
        safe_text
)
Activity_strategy = st.builds(
    Activity,
)
PiServiceComposition_ServiceActivity_strategy = st.builds(
    PiServiceComposition_ServiceActivity,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
PiServiceComposition_ActivityFinalNode_strategy = st.builds(
    PiServiceComposition_ActivityFinalNode,
)
PiServiceComposition_Rule_strategy = st.builds(
    PiServiceComposition_Rule,
    condition=
        safe_text,
    name=
        safe_text,
    event=
        safe_text,
    action=
        safe_text
)
ActivityPartition_strategy = st.builds(
    ActivityPartition,
)
PiServiceComposition_BussinessCollaborator_strategy = st.builds(
    PiServiceComposition_BussinessCollaborator,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
PiServiceComposition_FinalNode_strategy = st.builds(
    PiServiceComposition_FinalNode,
)
PiServiceComposition_MergeNode_strategy = st.builds(
    PiServiceComposition_MergeNode,
)
PiServiceComposition_DecisionNode_strategy = st.builds(
    PiServiceComposition_DecisionNode,
)
PiServiceComposition_ForkNode_strategy = st.builds(
    PiServiceComposition_ForkNode,
)
PiServiceComposition_JoinNode_strategy = st.builds(
    PiServiceComposition_JoinNode,
)
PiServiceComposition_InitialNode_strategy = st.builds(
    PiServiceComposition_InitialNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
PiServiceComposition_ControlNode_strategy = st.builds(
    PiServiceComposition_ControlNode,
)
PiServiceComposition_ObjectNode_strategy = st.builds(
    PiServiceComposition_ObjectNode,
)
PiServiceComposition_ExecutableNode_strategy = st.builds(
    PiServiceComposition_ExecutableNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
PiServiceComposition_ObjectFlow_strategy = st.builds(
    PiServiceComposition_ObjectFlow,
)
PiServiceComposition_ControlFlow_strategy = st.builds(
    PiServiceComposition_ControlFlow,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PiServiceComposition_ActivityNode_strategy = st.builds(
    PiServiceComposition_ActivityNode,
)
PiServiceComposition_NamedElement_strategy = st.builds(
    PiServiceComposition_NamedElement,
    name=
        safe_text
)
PiServiceComposition_Variable_strategy = st.builds(
    PiServiceComposition_Variable,
    type=
        safe_text,
    name=
        safe_text
)
PiServiceComposition_Policy_strategy = st.builds(
    PiServiceComposition_Policy,
    name=
        safe_text
)
PiServiceComposition_ActivityEdge_strategy = st.builds(
    PiServiceComposition_ActivityEdge,
)
PiServiceComposition_Activity_strategy = st.builds(
    PiServiceComposition_Activity,
)
PiServiceComposition_ActivityPartition_strategy = st.builds(
    PiServiceComposition_ActivityPartition,
    isExternal=
        st.booleans(),
    isDimension=
        st.booleans()
)
PiServiceComposition_CompositionServiceModel_strategy = st.builds(
    PiServiceComposition_CompositionServiceModel,
)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=PiServiceComposition_Action_strategy)
@settings(max_examples=50)
def test_piservicecomposition_action_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_Action)



@given(instance=PiServiceComposition_Action_strategy)
def test_piservicecomposition_action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=PiServiceComposition_ServiceActivity_strategy)
@settings(max_examples=50)
def test_piservicecomposition_serviceactivity_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ServiceActivity)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=PiServiceComposition_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_activityfinalnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ActivityFinalNode)

@given(instance=PiServiceComposition_Rule_strategy)
@settings(max_examples=50)
def test_piservicecomposition_rule_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_Rule)



@given(instance=PiServiceComposition_Rule_strategy)
def test_piservicecomposition_rule_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original



@given(instance=PiServiceComposition_Rule_strategy)
def test_piservicecomposition_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=PiServiceComposition_Rule_strategy)
def test_piservicecomposition_rule_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=PiServiceComposition_Rule_strategy)
def test_piservicecomposition_rule_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=ActivityPartition_strategy)
@settings(max_examples=50)
def test_activitypartition_instantiation(instance):
    assert isinstance(instance, ActivityPartition)

@given(instance=PiServiceComposition_BussinessCollaborator_strategy)
@settings(max_examples=50)
def test_piservicecomposition_bussinesscollaborator_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_BussinessCollaborator)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=PiServiceComposition_FinalNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_finalnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_FinalNode)

@given(instance=PiServiceComposition_MergeNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_mergenode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_MergeNode)

@given(instance=PiServiceComposition_DecisionNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_decisionnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_DecisionNode)

@given(instance=PiServiceComposition_ForkNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_forknode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ForkNode)

@given(instance=PiServiceComposition_JoinNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_joinnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_JoinNode)

@given(instance=PiServiceComposition_InitialNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_initialnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_InitialNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=PiServiceComposition_ControlNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_controlnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ControlNode)

@given(instance=PiServiceComposition_ObjectNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_objectnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ObjectNode)

@given(instance=PiServiceComposition_ExecutableNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_executablenode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ExecutableNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=PiServiceComposition_ObjectFlow_strategy)
@settings(max_examples=50)
def test_piservicecomposition_objectflow_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ObjectFlow)

@given(instance=PiServiceComposition_ControlFlow_strategy)
@settings(max_examples=50)
def test_piservicecomposition_controlflow_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ControlFlow)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PiServiceComposition_ActivityNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition_activitynode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ActivityNode)

@given(instance=PiServiceComposition_NamedElement_strategy)
@settings(max_examples=50)
def test_piservicecomposition_namedelement_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_NamedElement)



@given(instance=PiServiceComposition_NamedElement_strategy)
def test_piservicecomposition_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition_Variable_strategy)
@settings(max_examples=50)
def test_piservicecomposition_variable_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_Variable)



@given(instance=PiServiceComposition_Variable_strategy)
def test_piservicecomposition_variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=PiServiceComposition_Variable_strategy)
def test_piservicecomposition_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition_Policy_strategy)
@settings(max_examples=50)
def test_piservicecomposition_policy_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_Policy)



@given(instance=PiServiceComposition_Policy_strategy)
def test_piservicecomposition_policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition_ActivityEdge_strategy)
@settings(max_examples=50)
def test_piservicecomposition_activityedge_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ActivityEdge)

@given(instance=PiServiceComposition_Activity_strategy)
@settings(max_examples=50)
def test_piservicecomposition_activity_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_Activity)

@given(instance=PiServiceComposition_ActivityPartition_strategy)
@settings(max_examples=50)
def test_piservicecomposition_activitypartition_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_ActivityPartition)



@given(instance=PiServiceComposition_ActivityPartition_strategy)
def test_piservicecomposition_activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=PiServiceComposition_ActivityPartition_strategy)
def test_piservicecomposition_activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=PiServiceComposition_CompositionServiceModel_strategy)
@settings(max_examples=50)
def test_piservicecomposition_compositionservicemodel_instantiation(instance):
    assert isinstance(instance, PiServiceComposition_CompositionServiceModel)
