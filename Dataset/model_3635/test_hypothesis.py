import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    umlknes::NamedElement,
    ValueSpecification,
    umlknes::OpaqueExpression,
    Event,
    umlknes::DestructionEvent,
    umlknes::CreationEvent,
    umlknes::ExecutionEvent,
    umlknes::Event,
    RedefinableElement,
    umlknes::ActivityEdge,
    NamedElement,
    umlknes::RedefinableElement,
    umlknes::Trigger,
    Action,
    umlknes::AcceptEventAction,
    ActivityEdge,
    umlknes::ControlFlow,
    umlknes::ValueSpecification,
    ControlNode,
    umlknes::DecisionNode,
    umlknes::InitialNode,
    umlknes::ActivityFinalNode,
    ActivityNode,
    umlknes::Action,
    umlknes::ControlNode,
    umlknes::ActivityNode,
    umlknes::Activity,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlknes::namedelement_is_not_abstract():
    assert not inspect.isabstract(umlknes::NamedElement)


def test_umlknes::namedelement_constructor_exists():
    assert callable(umlknes::NamedElement.__init__)


def test_umlknes::namedelement_constructor_args():
    sig = inspect.signature(umlknes::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_umlknes::namedelement_has_visibility():
    assert hasattr(umlknes::NamedElement, "visibility")
    descriptor = None
    for klass in umlknes::NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(umlknes::OpaqueExpression)


def test_umlknes::opaqueexpression_constructor_exists():
    assert callable(umlknes::OpaqueExpression.__init__)


def test_umlknes::opaqueexpression_constructor_args():
    sig = inspect.signature(umlknes::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::destructionevent_is_not_abstract():
    assert not inspect.isabstract(umlknes::DestructionEvent)


def test_umlknes::destructionevent_constructor_exists():
    assert callable(umlknes::DestructionEvent.__init__)


def test_umlknes::destructionevent_constructor_args():
    sig = inspect.signature(umlknes::DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::creationevent_is_not_abstract():
    assert not inspect.isabstract(umlknes::CreationEvent)


def test_umlknes::creationevent_constructor_exists():
    assert callable(umlknes::CreationEvent.__init__)


def test_umlknes::creationevent_constructor_args():
    sig = inspect.signature(umlknes::CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::executionevent_is_not_abstract():
    assert not inspect.isabstract(umlknes::ExecutionEvent)


def test_umlknes::executionevent_constructor_exists():
    assert callable(umlknes::ExecutionEvent.__init__)


def test_umlknes::executionevent_constructor_args():
    sig = inspect.signature(umlknes::ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::event_is_not_abstract():
    assert not inspect.isabstract(umlknes::Event)


def test_umlknes::event_constructor_exists():
    assert callable(umlknes::Event.__init__)


def test_umlknes::event_constructor_args():
    sig = inspect.signature(umlknes::Event.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::activityedge_is_not_abstract():
    assert not inspect.isabstract(umlknes::ActivityEdge)


def test_umlknes::activityedge_constructor_exists():
    assert callable(umlknes::ActivityEdge.__init__)


def test_umlknes::activityedge_constructor_args():
    sig = inspect.signature(umlknes::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::redefinableelement_is_not_abstract():
    assert not inspect.isabstract(umlknes::RedefinableElement)


def test_umlknes::redefinableelement_constructor_exists():
    assert callable(umlknes::RedefinableElement.__init__)


def test_umlknes::redefinableelement_constructor_args():
    sig = inspect.signature(umlknes::RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_umlknes::redefinableelement_has_isLeaf():
    assert hasattr(umlknes::RedefinableElement, "isLeaf")
    descriptor = None
    for klass in umlknes::RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_umlknes::trigger_is_not_abstract():
    assert not inspect.isabstract(umlknes::Trigger)


def test_umlknes::trigger_constructor_exists():
    assert callable(umlknes::Trigger.__init__)


def test_umlknes::trigger_constructor_args():
    sig = inspect.signature(umlknes::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::accepteventaction_is_not_abstract():
    assert not inspect.isabstract(umlknes::AcceptEventAction)


def test_umlknes::accepteventaction_constructor_exists():
    assert callable(umlknes::AcceptEventAction.__init__)


def test_umlknes::accepteventaction_constructor_args():
    sig = inspect.signature(umlknes::AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnMarshall" in params, "Missing parameter 'isUnMarshall'"

def test_umlknes::accepteventaction_has_isUnMarshall():
    assert hasattr(umlknes::AcceptEventAction, "isUnMarshall")
    descriptor = None
    for klass in umlknes::AcceptEventAction.__mro__:
        if "isUnMarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnMarshall"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::controlflow_is_not_abstract():
    assert not inspect.isabstract(umlknes::ControlFlow)


def test_umlknes::controlflow_constructor_exists():
    assert callable(umlknes::ControlFlow.__init__)


def test_umlknes::controlflow_constructor_args():
    sig = inspect.signature(umlknes::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::valuespecification_is_not_abstract():
    assert not inspect.isabstract(umlknes::ValueSpecification)


def test_umlknes::valuespecification_constructor_exists():
    assert callable(umlknes::ValueSpecification.__init__)


def test_umlknes::valuespecification_constructor_args():
    sig = inspect.signature(umlknes::ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::decisionnode_is_not_abstract():
    assert not inspect.isabstract(umlknes::DecisionNode)


def test_umlknes::decisionnode_constructor_exists():
    assert callable(umlknes::DecisionNode.__init__)


def test_umlknes::decisionnode_constructor_args():
    sig = inspect.signature(umlknes::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::initialnode_is_not_abstract():
    assert not inspect.isabstract(umlknes::InitialNode)


def test_umlknes::initialnode_constructor_exists():
    assert callable(umlknes::InitialNode.__init__)


def test_umlknes::initialnode_constructor_args():
    sig = inspect.signature(umlknes::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlknes::ActivityFinalNode)


def test_umlknes::activityfinalnode_constructor_exists():
    assert callable(umlknes::ActivityFinalNode.__init__)


def test_umlknes::activityfinalnode_constructor_args():
    sig = inspect.signature(umlknes::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::action_is_not_abstract():
    assert not inspect.isabstract(umlknes::Action)


def test_umlknes::action_constructor_exists():
    assert callable(umlknes::Action.__init__)


def test_umlknes::action_constructor_args():
    sig = inspect.signature(umlknes::Action.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::controlnode_is_not_abstract():
    assert not inspect.isabstract(umlknes::ControlNode)


def test_umlknes::controlnode_constructor_exists():
    assert callable(umlknes::ControlNode.__init__)


def test_umlknes::controlnode_constructor_args():
    sig = inspect.signature(umlknes::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::activitynode_is_not_abstract():
    assert not inspect.isabstract(umlknes::ActivityNode)


def test_umlknes::activitynode_constructor_exists():
    assert callable(umlknes::ActivityNode.__init__)


def test_umlknes::activitynode_constructor_args():
    sig = inspect.signature(umlknes::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes::activity_is_not_abstract():
    assert not inspect.isabstract(umlknes::Activity)


def test_umlknes::activity_constructor_exists():
    assert callable(umlknes::Activity.__init__)


def test_umlknes::activity_constructor_args():
    sig = inspect.signature(umlknes::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_umlknes::activity_has_isSingleExecution():
    assert hasattr(umlknes::Activity, "isSingleExecution")
    descriptor = None
    for klass in umlknes::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_umlknes::activity_has_isReadOnly():
    assert hasattr(umlknes::Activity, "isReadOnly")
    descriptor = None
    for klass in umlknes::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "package",
        "protected",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
umlknes::NamedElement_strategy = st.builds(
    umlknes::NamedElement,
    visibility=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
umlknes::OpaqueExpression_strategy = st.builds(
    umlknes::OpaqueExpression,
)
Event_strategy = st.builds(
    Event,
)
umlknes::DestructionEvent_strategy = st.builds(
    umlknes::DestructionEvent,
)
umlknes::CreationEvent_strategy = st.builds(
    umlknes::CreationEvent,
)
umlknes::ExecutionEvent_strategy = st.builds(
    umlknes::ExecutionEvent,
)
umlknes::Event_strategy = st.builds(
    umlknes::Event,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
umlknes::ActivityEdge_strategy = st.builds(
    umlknes::ActivityEdge,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umlknes::RedefinableElement_strategy = st.builds(
    umlknes::RedefinableElement,
    isLeaf=
        st.booleans()
)
umlknes::Trigger_strategy = st.builds(
    umlknes::Trigger,
)
Action_strategy = st.builds(
    Action,
)
umlknes::AcceptEventAction_strategy = st.builds(
    umlknes::AcceptEventAction,
    isUnMarshall=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
umlknes::ControlFlow_strategy = st.builds(
    umlknes::ControlFlow,
)
umlknes::ValueSpecification_strategy = st.builds(
    umlknes::ValueSpecification,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
umlknes::DecisionNode_strategy = st.builds(
    umlknes::DecisionNode,
)
umlknes::InitialNode_strategy = st.builds(
    umlknes::InitialNode,
)
umlknes::ActivityFinalNode_strategy = st.builds(
    umlknes::ActivityFinalNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
umlknes::Action_strategy = st.builds(
    umlknes::Action,
)
umlknes::ControlNode_strategy = st.builds(
    umlknes::ControlNode,
)
umlknes::ActivityNode_strategy = st.builds(
    umlknes::ActivityNode,
)
umlknes::Activity_strategy = st.builds(
    umlknes::Activity,
    isSingleExecution=
        st.booleans(),
    isReadOnly=
        st.booleans()
)

@given(instance=umlknes::NamedElement_strategy)
@settings(max_examples=50)
def test_umlknes::namedelement_instantiation(instance):
    assert isinstance(instance, umlknes::NamedElement)

@given(instance=umlknes::NamedElement_strategy)
def test_umlknes::namedelement_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=umlknes::NamedElement_strategy)
def test_umlknes::namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=umlknes::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_umlknes::opaqueexpression_instantiation(instance):
    assert isinstance(instance, umlknes::OpaqueExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=umlknes::DestructionEvent_strategy)
@settings(max_examples=50)
def test_umlknes::destructionevent_instantiation(instance):
    assert isinstance(instance, umlknes::DestructionEvent)

@given(instance=umlknes::CreationEvent_strategy)
@settings(max_examples=50)
def test_umlknes::creationevent_instantiation(instance):
    assert isinstance(instance, umlknes::CreationEvent)

@given(instance=umlknes::ExecutionEvent_strategy)
@settings(max_examples=50)
def test_umlknes::executionevent_instantiation(instance):
    assert isinstance(instance, umlknes::ExecutionEvent)

@given(instance=umlknes::Event_strategy)
@settings(max_examples=50)
def test_umlknes::event_instantiation(instance):
    assert isinstance(instance, umlknes::Event)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=umlknes::ActivityEdge_strategy)
@settings(max_examples=50)
def test_umlknes::activityedge_instantiation(instance):
    assert isinstance(instance, umlknes::ActivityEdge)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=umlknes::RedefinableElement_strategy)
@settings(max_examples=50)
def test_umlknes::redefinableelement_instantiation(instance):
    assert isinstance(instance, umlknes::RedefinableElement)

@given(instance=umlknes::RedefinableElement_strategy)
def test_umlknes::redefinableelement_isLeaf_type(instance):
    assert isinstance(instance.isLeaf, bool)


@given(instance=umlknes::RedefinableElement_strategy)
def test_umlknes::redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=umlknes::Trigger_strategy)
@settings(max_examples=50)
def test_umlknes::trigger_instantiation(instance):
    assert isinstance(instance, umlknes::Trigger)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=umlknes::AcceptEventAction_strategy)
@settings(max_examples=50)
def test_umlknes::accepteventaction_instantiation(instance):
    assert isinstance(instance, umlknes::AcceptEventAction)

@given(instance=umlknes::AcceptEventAction_strategy)
def test_umlknes::accepteventaction_isUnMarshall_type(instance):
    assert isinstance(instance.isUnMarshall, bool)


@given(instance=umlknes::AcceptEventAction_strategy)
def test_umlknes::accepteventaction_isUnMarshall_setter(instance):
    original = instance.isUnMarshall
    instance.isUnMarshall = original
    assert instance.isUnMarshall == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=umlknes::ControlFlow_strategy)
@settings(max_examples=50)
def test_umlknes::controlflow_instantiation(instance):
    assert isinstance(instance, umlknes::ControlFlow)

@given(instance=umlknes::ValueSpecification_strategy)
@settings(max_examples=50)
def test_umlknes::valuespecification_instantiation(instance):
    assert isinstance(instance, umlknes::ValueSpecification)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=umlknes::DecisionNode_strategy)
@settings(max_examples=50)
def test_umlknes::decisionnode_instantiation(instance):
    assert isinstance(instance, umlknes::DecisionNode)

@given(instance=umlknes::InitialNode_strategy)
@settings(max_examples=50)
def test_umlknes::initialnode_instantiation(instance):
    assert isinstance(instance, umlknes::InitialNode)

@given(instance=umlknes::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umlknes::activityfinalnode_instantiation(instance):
    assert isinstance(instance, umlknes::ActivityFinalNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=umlknes::Action_strategy)
@settings(max_examples=50)
def test_umlknes::action_instantiation(instance):
    assert isinstance(instance, umlknes::Action)

@given(instance=umlknes::ControlNode_strategy)
@settings(max_examples=50)
def test_umlknes::controlnode_instantiation(instance):
    assert isinstance(instance, umlknes::ControlNode)

@given(instance=umlknes::ActivityNode_strategy)
@settings(max_examples=50)
def test_umlknes::activitynode_instantiation(instance):
    assert isinstance(instance, umlknes::ActivityNode)

@given(instance=umlknes::Activity_strategy)
@settings(max_examples=50)
def test_umlknes::activity_instantiation(instance):
    assert isinstance(instance, umlknes::Activity)

@given(instance=umlknes::Activity_strategy)
def test_umlknes::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, bool)


@given(instance=umlknes::Activity_strategy)
def test_umlknes::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=umlknes::Activity_strategy)
def test_umlknes::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=umlknes::Activity_strategy)
def test_umlknes::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original
