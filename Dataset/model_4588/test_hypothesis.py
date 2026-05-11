import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ActivityNode,
    PiServiceComposition::ObjectNode,
    PiServiceComposition::ControlNode,
    PiServiceComposition::ExecutableNode,
    ActivityEdge,
    PiServiceComposition::ObjectFlow,
    PiServiceComposition::ControlFlow,
    NamedElement,
    PiServiceComposition::ActivityNode,
    PiServiceComposition::NamedElement,
    PiServiceComposition::Variable,
    PiServiceComposition::Policy,
    PiServiceComposition::ActivityEdge,
    PiServiceComposition::Activity,
    PiServiceComposition::ActivityPartition,
    PiServiceComposition::CompositionServiceModel,
    ExecutableNode,
    PiServiceComposition::Action,
    Activity,
    PiServiceComposition::ServiceActivity,
    FinalNode,
    PiServiceComposition::ActivityFinalNode,
    PiServiceComposition::Rule,
    ActivityPartition,
    PiServiceComposition::BussinessCollaborator,
    ControlNode,
    PiServiceComposition::InitialNode,
    PiServiceComposition::MergeNode,
    PiServiceComposition::FinalNode,
    PiServiceComposition::ForkNode,
    PiServiceComposition::DecisionNode,
    PiServiceComposition::JoinNode,
    EventType,
    ActionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::objectnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ObjectNode)


def test_piservicecomposition::objectnode_constructor_exists():
    assert callable(PiServiceComposition::ObjectNode.__init__)


def test_piservicecomposition::objectnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::controlnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ControlNode)


def test_piservicecomposition::controlnode_constructor_exists():
    assert callable(PiServiceComposition::ControlNode.__init__)


def test_piservicecomposition::controlnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::executablenode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ExecutableNode)


def test_piservicecomposition::executablenode_constructor_exists():
    assert callable(PiServiceComposition::ExecutableNode.__init__)


def test_piservicecomposition::executablenode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::objectflow_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ObjectFlow)


def test_piservicecomposition::objectflow_constructor_exists():
    assert callable(PiServiceComposition::ObjectFlow.__init__)


def test_piservicecomposition::objectflow_constructor_args():
    sig = inspect.signature(PiServiceComposition::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::controlflow_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ControlFlow)


def test_piservicecomposition::controlflow_constructor_exists():
    assert callable(PiServiceComposition::ControlFlow.__init__)


def test_piservicecomposition::controlflow_constructor_args():
    sig = inspect.signature(PiServiceComposition::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::activitynode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ActivityNode)


def test_piservicecomposition::activitynode_constructor_exists():
    assert callable(PiServiceComposition::ActivityNode.__init__)


def test_piservicecomposition::activitynode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::namedelement_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::NamedElement)


def test_piservicecomposition::namedelement_constructor_exists():
    assert callable(PiServiceComposition::NamedElement.__init__)


def test_piservicecomposition::namedelement_constructor_args():
    sig = inspect.signature(PiServiceComposition::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition::namedelement_has_name():
    assert hasattr(PiServiceComposition::NamedElement, "name")
    descriptor = None
    for klass in PiServiceComposition::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition::variable_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::Variable)


def test_piservicecomposition::variable_constructor_exists():
    assert callable(PiServiceComposition::Variable.__init__)


def test_piservicecomposition::variable_constructor_args():
    sig = inspect.signature(PiServiceComposition::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition::variable_has_type():
    assert hasattr(PiServiceComposition::Variable, "type")
    descriptor = None
    for klass in PiServiceComposition::Variable.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition::variable_has_name():
    assert hasattr(PiServiceComposition::Variable, "name")
    descriptor = None
    for klass in PiServiceComposition::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition::policy_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::Policy)


def test_piservicecomposition::policy_constructor_exists():
    assert callable(PiServiceComposition::Policy.__init__)


def test_piservicecomposition::policy_constructor_args():
    sig = inspect.signature(PiServiceComposition::Policy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_piservicecomposition::policy_has_name():
    assert hasattr(PiServiceComposition::Policy, "name")
    descriptor = None
    for klass in PiServiceComposition::Policy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition::activityedge_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ActivityEdge)


def test_piservicecomposition::activityedge_constructor_exists():
    assert callable(PiServiceComposition::ActivityEdge.__init__)


def test_piservicecomposition::activityedge_constructor_args():
    sig = inspect.signature(PiServiceComposition::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::activity_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::Activity)


def test_piservicecomposition::activity_constructor_exists():
    assert callable(PiServiceComposition::Activity.__init__)


def test_piservicecomposition::activity_constructor_args():
    sig = inspect.signature(PiServiceComposition::Activity.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::activitypartition_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ActivityPartition)


def test_piservicecomposition::activitypartition_constructor_exists():
    assert callable(PiServiceComposition::ActivityPartition.__init__)


def test_piservicecomposition::activitypartition_constructor_args():
    sig = inspect.signature(PiServiceComposition::ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_piservicecomposition::activitypartition_has_isDimension():
    assert hasattr(PiServiceComposition::ActivityPartition, "isDimension")
    descriptor = None
    for klass in PiServiceComposition::ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition::activitypartition_has_isExternal():
    assert hasattr(PiServiceComposition::ActivityPartition, "isExternal")
    descriptor = None
    for klass in PiServiceComposition::ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_piservicecomposition::compositionservicemodel_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::CompositionServiceModel)


def test_piservicecomposition::compositionservicemodel_constructor_exists():
    assert callable(PiServiceComposition::CompositionServiceModel.__init__)


def test_piservicecomposition::compositionservicemodel_constructor_args():
    sig = inspect.signature(PiServiceComposition::CompositionServiceModel.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::action_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::Action)


def test_piservicecomposition::action_constructor_exists():
    assert callable(PiServiceComposition::Action.__init__)


def test_piservicecomposition::action_constructor_args():
    sig = inspect.signature(PiServiceComposition::Action.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_piservicecomposition::action_has_type():
    assert hasattr(PiServiceComposition::Action, "type")
    descriptor = None
    for klass in PiServiceComposition::Action.__mro__:
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



def test_piservicecomposition::serviceactivity_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ServiceActivity)


def test_piservicecomposition::serviceactivity_constructor_exists():
    assert callable(PiServiceComposition::ServiceActivity.__init__)


def test_piservicecomposition::serviceactivity_constructor_args():
    sig = inspect.signature(PiServiceComposition::ServiceActivity.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ActivityFinalNode)


def test_piservicecomposition::activityfinalnode_constructor_exists():
    assert callable(PiServiceComposition::ActivityFinalNode.__init__)


def test_piservicecomposition::activityfinalnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::rule_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::Rule)


def test_piservicecomposition::rule_constructor_exists():
    assert callable(PiServiceComposition::Rule.__init__)


def test_piservicecomposition::rule_constructor_args():
    sig = inspect.signature(PiServiceComposition::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "action" in params, "Missing parameter 'action'"
    assert "event" in params, "Missing parameter 'event'"
    assert "condition" in params, "Missing parameter 'condition'"

def test_piservicecomposition::rule_has_name():
    assert hasattr(PiServiceComposition::Rule, "name")
    descriptor = None
    for klass in PiServiceComposition::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition::rule_has_action():
    assert hasattr(PiServiceComposition::Rule, "action")
    descriptor = None
    for klass in PiServiceComposition::Rule.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition::rule_has_event():
    assert hasattr(PiServiceComposition::Rule, "event")
    descriptor = None
    for klass in PiServiceComposition::Rule.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_piservicecomposition::rule_has_condition():
    assert hasattr(PiServiceComposition::Rule, "condition")
    descriptor = None
    for klass in PiServiceComposition::Rule.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_activitypartition_is_not_abstract():
    assert not inspect.isabstract(ActivityPartition)


def test_activitypartition_constructor_exists():
    assert callable(ActivityPartition.__init__)


def test_activitypartition_constructor_args():
    sig = inspect.signature(ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::bussinesscollaborator_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::BussinessCollaborator)


def test_piservicecomposition::bussinesscollaborator_constructor_exists():
    assert callable(PiServiceComposition::BussinessCollaborator.__init__)


def test_piservicecomposition::bussinesscollaborator_constructor_args():
    sig = inspect.signature(PiServiceComposition::BussinessCollaborator.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::initialnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::InitialNode)


def test_piservicecomposition::initialnode_constructor_exists():
    assert callable(PiServiceComposition::InitialNode.__init__)


def test_piservicecomposition::initialnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::mergenode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::MergeNode)


def test_piservicecomposition::mergenode_constructor_exists():
    assert callable(PiServiceComposition::MergeNode.__init__)


def test_piservicecomposition::mergenode_constructor_args():
    sig = inspect.signature(PiServiceComposition::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::finalnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::FinalNode)


def test_piservicecomposition::finalnode_constructor_exists():
    assert callable(PiServiceComposition::FinalNode.__init__)


def test_piservicecomposition::finalnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::forknode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::ForkNode)


def test_piservicecomposition::forknode_constructor_exists():
    assert callable(PiServiceComposition::ForkNode.__init__)


def test_piservicecomposition::forknode_constructor_args():
    sig = inspect.signature(PiServiceComposition::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::decisionnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::DecisionNode)


def test_piservicecomposition::decisionnode_constructor_exists():
    assert callable(PiServiceComposition::DecisionNode.__init__)


def test_piservicecomposition::decisionnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_piservicecomposition::joinnode_is_not_abstract():
    assert not inspect.isabstract(PiServiceComposition::JoinNode)


def test_piservicecomposition::joinnode_constructor_exists():
    assert callable(PiServiceComposition::JoinNode.__init__)


def test_piservicecomposition::joinnode_constructor_args():
    sig = inspect.signature(PiServiceComposition::JoinNode.__init__)
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
        "WS",
        "AOP",
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
ActivityNode_strategy = st.builds(
    ActivityNode,
)
PiServiceComposition::ObjectNode_strategy = st.builds(
    PiServiceComposition::ObjectNode,
)
PiServiceComposition::ControlNode_strategy = st.builds(
    PiServiceComposition::ControlNode,
)
PiServiceComposition::ExecutableNode_strategy = st.builds(
    PiServiceComposition::ExecutableNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
PiServiceComposition::ObjectFlow_strategy = st.builds(
    PiServiceComposition::ObjectFlow,
)
PiServiceComposition::ControlFlow_strategy = st.builds(
    PiServiceComposition::ControlFlow,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PiServiceComposition::ActivityNode_strategy = st.builds(
    PiServiceComposition::ActivityNode,
)
PiServiceComposition::NamedElement_strategy = st.builds(
    PiServiceComposition::NamedElement,
    name=
        safe_text
)
PiServiceComposition::Variable_strategy = st.builds(
    PiServiceComposition::Variable,
    type=
        safe_text,
    name=
        safe_text
)
PiServiceComposition::Policy_strategy = st.builds(
    PiServiceComposition::Policy,
    name=
        safe_text
)
PiServiceComposition::ActivityEdge_strategy = st.builds(
    PiServiceComposition::ActivityEdge,
)
PiServiceComposition::Activity_strategy = st.builds(
    PiServiceComposition::Activity,
)
PiServiceComposition::ActivityPartition_strategy = st.builds(
    PiServiceComposition::ActivityPartition,
    isDimension=
        st.booleans(),
    isExternal=
        st.booleans()
)
PiServiceComposition::CompositionServiceModel_strategy = st.builds(
    PiServiceComposition::CompositionServiceModel,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
PiServiceComposition::Action_strategy = st.builds(
    PiServiceComposition::Action,
    type=
        safe_text
)
Activity_strategy = st.builds(
    Activity,
)
PiServiceComposition::ServiceActivity_strategy = st.builds(
    PiServiceComposition::ServiceActivity,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
PiServiceComposition::ActivityFinalNode_strategy = st.builds(
    PiServiceComposition::ActivityFinalNode,
)
PiServiceComposition::Rule_strategy = st.builds(
    PiServiceComposition::Rule,
    name=
        safe_text,
    action=
        safe_text,
    event=
        safe_text,
    condition=
        safe_text
)
ActivityPartition_strategy = st.builds(
    ActivityPartition,
)
PiServiceComposition::BussinessCollaborator_strategy = st.builds(
    PiServiceComposition::BussinessCollaborator,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
PiServiceComposition::InitialNode_strategy = st.builds(
    PiServiceComposition::InitialNode,
)
PiServiceComposition::MergeNode_strategy = st.builds(
    PiServiceComposition::MergeNode,
)
PiServiceComposition::FinalNode_strategy = st.builds(
    PiServiceComposition::FinalNode,
)
PiServiceComposition::ForkNode_strategy = st.builds(
    PiServiceComposition::ForkNode,
)
PiServiceComposition::DecisionNode_strategy = st.builds(
    PiServiceComposition::DecisionNode,
)
PiServiceComposition::JoinNode_strategy = st.builds(
    PiServiceComposition::JoinNode,
)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=PiServiceComposition::ObjectNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::objectnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ObjectNode)

@given(instance=PiServiceComposition::ControlNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::controlnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ControlNode)

@given(instance=PiServiceComposition::ExecutableNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::executablenode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ExecutableNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=PiServiceComposition::ObjectFlow_strategy)
@settings(max_examples=50)
def test_piservicecomposition::objectflow_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ObjectFlow)

@given(instance=PiServiceComposition::ControlFlow_strategy)
@settings(max_examples=50)
def test_piservicecomposition::controlflow_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ControlFlow)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PiServiceComposition::ActivityNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::activitynode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ActivityNode)

@given(instance=PiServiceComposition::NamedElement_strategy)
@settings(max_examples=50)
def test_piservicecomposition::namedelement_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::NamedElement)

@given(instance=PiServiceComposition::NamedElement_strategy)
def test_piservicecomposition::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PiServiceComposition::NamedElement_strategy)
def test_piservicecomposition::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition::Variable_strategy)
@settings(max_examples=50)
def test_piservicecomposition::variable_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::Variable)

@given(instance=PiServiceComposition::Variable_strategy)
def test_piservicecomposition::variable_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PiServiceComposition::Variable_strategy)
def test_piservicecomposition::variable_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=PiServiceComposition::Variable_strategy)
def test_piservicecomposition::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PiServiceComposition::Variable_strategy)
def test_piservicecomposition::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition::Policy_strategy)
@settings(max_examples=50)
def test_piservicecomposition::policy_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::Policy)

@given(instance=PiServiceComposition::Policy_strategy)
def test_piservicecomposition::policy_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PiServiceComposition::Policy_strategy)
def test_piservicecomposition::policy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition::ActivityEdge_strategy)
@settings(max_examples=50)
def test_piservicecomposition::activityedge_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ActivityEdge)

@given(instance=PiServiceComposition::Activity_strategy)
@settings(max_examples=50)
def test_piservicecomposition::activity_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::Activity)

@given(instance=PiServiceComposition::ActivityPartition_strategy)
@settings(max_examples=50)
def test_piservicecomposition::activitypartition_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ActivityPartition)

@given(instance=PiServiceComposition::ActivityPartition_strategy)
def test_piservicecomposition::activitypartition_isDimension_type(instance):
    assert isinstance(instance.isDimension, bool)


@given(instance=PiServiceComposition::ActivityPartition_strategy)
def test_piservicecomposition::activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original

@given(instance=PiServiceComposition::ActivityPartition_strategy)
def test_piservicecomposition::activitypartition_isExternal_type(instance):
    assert isinstance(instance.isExternal, bool)


@given(instance=PiServiceComposition::ActivityPartition_strategy)
def test_piservicecomposition::activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=PiServiceComposition::CompositionServiceModel_strategy)
@settings(max_examples=50)
def test_piservicecomposition::compositionservicemodel_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::CompositionServiceModel)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=PiServiceComposition::Action_strategy)
@settings(max_examples=50)
def test_piservicecomposition::action_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::Action)

@given(instance=PiServiceComposition::Action_strategy)
def test_piservicecomposition::action_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=PiServiceComposition::Action_strategy)
def test_piservicecomposition::action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=PiServiceComposition::ServiceActivity_strategy)
@settings(max_examples=50)
def test_piservicecomposition::serviceactivity_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ServiceActivity)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=PiServiceComposition::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::activityfinalnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ActivityFinalNode)

@given(instance=PiServiceComposition::Rule_strategy)
@settings(max_examples=50)
def test_piservicecomposition::rule_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::Rule)

@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_event_type(instance):
    assert isinstance(instance.event, str)


@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=PiServiceComposition::Rule_strategy)
def test_piservicecomposition::rule_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=ActivityPartition_strategy)
@settings(max_examples=50)
def test_activitypartition_instantiation(instance):
    assert isinstance(instance, ActivityPartition)

@given(instance=PiServiceComposition::BussinessCollaborator_strategy)
@settings(max_examples=50)
def test_piservicecomposition::bussinesscollaborator_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::BussinessCollaborator)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=PiServiceComposition::InitialNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::initialnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::InitialNode)

@given(instance=PiServiceComposition::MergeNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::mergenode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::MergeNode)

@given(instance=PiServiceComposition::FinalNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::finalnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::FinalNode)

@given(instance=PiServiceComposition::ForkNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::forknode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::ForkNode)

@given(instance=PiServiceComposition::DecisionNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::decisionnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::DecisionNode)

@given(instance=PiServiceComposition::JoinNode_strategy)
@settings(max_examples=50)
def test_piservicecomposition::joinnode_instantiation(instance):
    assert isinstance(instance, PiServiceComposition::JoinNode)
