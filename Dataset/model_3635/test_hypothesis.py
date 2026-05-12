import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    umlknes_NamedElement,
    ValueSpecification,
    umlknes_OpaqueExpression,
    Event,
    umlknes_CreationEvent,
    umlknes_DestructionEvent,
    umlknes_ExecutionEvent,
    umlknes_Event,
    RedefinableElement,
    umlknes_ActivityEdge,
    NamedElement,
    umlknes_RedefinableElement,
    umlknes_Trigger,
    Action,
    umlknes_AcceptEventAction,
    ActivityEdge,
    umlknes_ControlFlow,
    umlknes_ValueSpecification,
    ControlNode,
    umlknes_DecisionNode,
    umlknes_InitialNode,
    umlknes_ActivityFinalNode,
    ActivityNode,
    umlknes_Action,
    umlknes_ControlNode,
    umlknes_ActivityNode,
    umlknes_Activity,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_umlknes_namedelement_is_not_abstract():
    assert not inspect.isabstract(umlknes_NamedElement)


def test_umlknes_namedelement_constructor_exists():
    assert callable(umlknes_NamedElement.__init__)


def test_umlknes_namedelement_constructor_args():
    sig = inspect.signature(umlknes_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_umlknes_namedelement_has_visibility():
    assert hasattr(umlknes_NamedElement, "visibility")
    descriptor = None
    for klass in umlknes_NamedElement.__mro__:
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



def test_umlknes_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(umlknes_OpaqueExpression)


def test_umlknes_opaqueexpression_constructor_exists():
    assert callable(umlknes_OpaqueExpression.__init__)


def test_umlknes_opaqueexpression_constructor_args():
    sig = inspect.signature(umlknes_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_creationevent_is_not_abstract():
    assert not inspect.isabstract(umlknes_CreationEvent)


def test_umlknes_creationevent_constructor_exists():
    assert callable(umlknes_CreationEvent.__init__)


def test_umlknes_creationevent_constructor_args():
    sig = inspect.signature(umlknes_CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_destructionevent_is_not_abstract():
    assert not inspect.isabstract(umlknes_DestructionEvent)


def test_umlknes_destructionevent_constructor_exists():
    assert callable(umlknes_DestructionEvent.__init__)


def test_umlknes_destructionevent_constructor_args():
    sig = inspect.signature(umlknes_DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_executionevent_is_not_abstract():
    assert not inspect.isabstract(umlknes_ExecutionEvent)


def test_umlknes_executionevent_constructor_exists():
    assert callable(umlknes_ExecutionEvent.__init__)


def test_umlknes_executionevent_constructor_args():
    sig = inspect.signature(umlknes_ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_event_is_not_abstract():
    assert not inspect.isabstract(umlknes_Event)


def test_umlknes_event_constructor_exists():
    assert callable(umlknes_Event.__init__)


def test_umlknes_event_constructor_args():
    sig = inspect.signature(umlknes_Event.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_activityedge_is_not_abstract():
    assert not inspect.isabstract(umlknes_ActivityEdge)


def test_umlknes_activityedge_constructor_exists():
    assert callable(umlknes_ActivityEdge.__init__)


def test_umlknes_activityedge_constructor_args():
    sig = inspect.signature(umlknes_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(umlknes_RedefinableElement)


def test_umlknes_redefinableelement_constructor_exists():
    assert callable(umlknes_RedefinableElement.__init__)


def test_umlknes_redefinableelement_constructor_args():
    sig = inspect.signature(umlknes_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_umlknes_redefinableelement_has_isLeaf():
    assert hasattr(umlknes_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in umlknes_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_umlknes_trigger_is_not_abstract():
    assert not inspect.isabstract(umlknes_Trigger)


def test_umlknes_trigger_constructor_exists():
    assert callable(umlknes_Trigger.__init__)


def test_umlknes_trigger_constructor_args():
    sig = inspect.signature(umlknes_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(umlknes_AcceptEventAction)


def test_umlknes_accepteventaction_constructor_exists():
    assert callable(umlknes_AcceptEventAction.__init__)


def test_umlknes_accepteventaction_constructor_args():
    sig = inspect.signature(umlknes_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnMarshall" in params, "Missing parameter 'isUnMarshall'"

def test_umlknes_accepteventaction_has_isUnMarshall():
    assert hasattr(umlknes_AcceptEventAction, "isUnMarshall")
    descriptor = None
    for klass in umlknes_AcceptEventAction.__mro__:
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



def test_umlknes_controlflow_is_not_abstract():
    assert not inspect.isabstract(umlknes_ControlFlow)


def test_umlknes_controlflow_constructor_exists():
    assert callable(umlknes_ControlFlow.__init__)


def test_umlknes_controlflow_constructor_args():
    sig = inspect.signature(umlknes_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_valuespecification_is_not_abstract():
    assert not inspect.isabstract(umlknes_ValueSpecification)


def test_umlknes_valuespecification_constructor_exists():
    assert callable(umlknes_ValueSpecification.__init__)


def test_umlknes_valuespecification_constructor_args():
    sig = inspect.signature(umlknes_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_decisionnode_is_not_abstract():
    assert not inspect.isabstract(umlknes_DecisionNode)


def test_umlknes_decisionnode_constructor_exists():
    assert callable(umlknes_DecisionNode.__init__)


def test_umlknes_decisionnode_constructor_args():
    sig = inspect.signature(umlknes_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_initialnode_is_not_abstract():
    assert not inspect.isabstract(umlknes_InitialNode)


def test_umlknes_initialnode_constructor_exists():
    assert callable(umlknes_InitialNode.__init__)


def test_umlknes_initialnode_constructor_args():
    sig = inspect.signature(umlknes_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(umlknes_ActivityFinalNode)


def test_umlknes_activityfinalnode_constructor_exists():
    assert callable(umlknes_ActivityFinalNode.__init__)


def test_umlknes_activityfinalnode_constructor_args():
    sig = inspect.signature(umlknes_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_action_is_not_abstract():
    assert not inspect.isabstract(umlknes_Action)


def test_umlknes_action_constructor_exists():
    assert callable(umlknes_Action.__init__)


def test_umlknes_action_constructor_args():
    sig = inspect.signature(umlknes_Action.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_controlnode_is_not_abstract():
    assert not inspect.isabstract(umlknes_ControlNode)


def test_umlknes_controlnode_constructor_exists():
    assert callable(umlknes_ControlNode.__init__)


def test_umlknes_controlnode_constructor_args():
    sig = inspect.signature(umlknes_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_activitynode_is_not_abstract():
    assert not inspect.isabstract(umlknes_ActivityNode)


def test_umlknes_activitynode_constructor_exists():
    assert callable(umlknes_ActivityNode.__init__)


def test_umlknes_activitynode_constructor_args():
    sig = inspect.signature(umlknes_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlknes_activity_is_not_abstract():
    assert not inspect.isabstract(umlknes_Activity)


def test_umlknes_activity_constructor_exists():
    assert callable(umlknes_Activity.__init__)


def test_umlknes_activity_constructor_args():
    sig = inspect.signature(umlknes_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_umlknes_activity_has_isReadOnly():
    assert hasattr(umlknes_Activity, "isReadOnly")
    descriptor = None
    for klass in umlknes_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_umlknes_activity_has_isSingleExecution():
    assert hasattr(umlknes_Activity, "isSingleExecution")
    descriptor = None
    for klass in umlknes_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "package",
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
umlknes_NamedElement_strategy = st.builds(
    umlknes_NamedElement,
    visibility=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
umlknes_OpaqueExpression_strategy = st.builds(
    umlknes_OpaqueExpression,
)
Event_strategy = st.builds(
    Event,
)
umlknes_CreationEvent_strategy = st.builds(
    umlknes_CreationEvent,
)
umlknes_DestructionEvent_strategy = st.builds(
    umlknes_DestructionEvent,
)
umlknes_ExecutionEvent_strategy = st.builds(
    umlknes_ExecutionEvent,
)
umlknes_Event_strategy = st.builds(
    umlknes_Event,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
umlknes_ActivityEdge_strategy = st.builds(
    umlknes_ActivityEdge,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umlknes_RedefinableElement_strategy = st.builds(
    umlknes_RedefinableElement,
    isLeaf=
        st.booleans()
)
umlknes_Trigger_strategy = st.builds(
    umlknes_Trigger,
)
Action_strategy = st.builds(
    Action,
)
umlknes_AcceptEventAction_strategy = st.builds(
    umlknes_AcceptEventAction,
    isUnMarshall=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
umlknes_ControlFlow_strategy = st.builds(
    umlknes_ControlFlow,
)
umlknes_ValueSpecification_strategy = st.builds(
    umlknes_ValueSpecification,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
umlknes_DecisionNode_strategy = st.builds(
    umlknes_DecisionNode,
)
umlknes_InitialNode_strategy = st.builds(
    umlknes_InitialNode,
)
umlknes_ActivityFinalNode_strategy = st.builds(
    umlknes_ActivityFinalNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
umlknes_Action_strategy = st.builds(
    umlknes_Action,
)
umlknes_ControlNode_strategy = st.builds(
    umlknes_ControlNode,
)
umlknes_ActivityNode_strategy = st.builds(
    umlknes_ActivityNode,
)
umlknes_Activity_strategy = st.builds(
    umlknes_Activity,
    isReadOnly=
        st.booleans(),
    isSingleExecution=
        st.booleans()
)

@given(instance=umlknes_NamedElement_strategy)
@settings(max_examples=50)
def test_umlknes_namedelement_instantiation(instance):
    assert isinstance(instance, umlknes_NamedElement)



@given(instance=umlknes_NamedElement_strategy)
def test_umlknes_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=umlknes_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_umlknes_opaqueexpression_instantiation(instance):
    assert isinstance(instance, umlknes_OpaqueExpression)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=umlknes_CreationEvent_strategy)
@settings(max_examples=50)
def test_umlknes_creationevent_instantiation(instance):
    assert isinstance(instance, umlknes_CreationEvent)

@given(instance=umlknes_DestructionEvent_strategy)
@settings(max_examples=50)
def test_umlknes_destructionevent_instantiation(instance):
    assert isinstance(instance, umlknes_DestructionEvent)

@given(instance=umlknes_ExecutionEvent_strategy)
@settings(max_examples=50)
def test_umlknes_executionevent_instantiation(instance):
    assert isinstance(instance, umlknes_ExecutionEvent)

@given(instance=umlknes_Event_strategy)
@settings(max_examples=50)
def test_umlknes_event_instantiation(instance):
    assert isinstance(instance, umlknes_Event)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=umlknes_ActivityEdge_strategy)
@settings(max_examples=50)
def test_umlknes_activityedge_instantiation(instance):
    assert isinstance(instance, umlknes_ActivityEdge)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=umlknes_RedefinableElement_strategy)
@settings(max_examples=50)
def test_umlknes_redefinableelement_instantiation(instance):
    assert isinstance(instance, umlknes_RedefinableElement)



@given(instance=umlknes_RedefinableElement_strategy)
def test_umlknes_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=umlknes_Trigger_strategy)
@settings(max_examples=50)
def test_umlknes_trigger_instantiation(instance):
    assert isinstance(instance, umlknes_Trigger)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=umlknes_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_umlknes_accepteventaction_instantiation(instance):
    assert isinstance(instance, umlknes_AcceptEventAction)



@given(instance=umlknes_AcceptEventAction_strategy)
def test_umlknes_accepteventaction_isUnMarshall_setter(instance):
    original = instance.isUnMarshall
    instance.isUnMarshall = original
    assert instance.isUnMarshall == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=umlknes_ControlFlow_strategy)
@settings(max_examples=50)
def test_umlknes_controlflow_instantiation(instance):
    assert isinstance(instance, umlknes_ControlFlow)

@given(instance=umlknes_ValueSpecification_strategy)
@settings(max_examples=50)
def test_umlknes_valuespecification_instantiation(instance):
    assert isinstance(instance, umlknes_ValueSpecification)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=umlknes_DecisionNode_strategy)
@settings(max_examples=50)
def test_umlknes_decisionnode_instantiation(instance):
    assert isinstance(instance, umlknes_DecisionNode)

@given(instance=umlknes_InitialNode_strategy)
@settings(max_examples=50)
def test_umlknes_initialnode_instantiation(instance):
    assert isinstance(instance, umlknes_InitialNode)

@given(instance=umlknes_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umlknes_activityfinalnode_instantiation(instance):
    assert isinstance(instance, umlknes_ActivityFinalNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=umlknes_Action_strategy)
@settings(max_examples=50)
def test_umlknes_action_instantiation(instance):
    assert isinstance(instance, umlknes_Action)

@given(instance=umlknes_ControlNode_strategy)
@settings(max_examples=50)
def test_umlknes_controlnode_instantiation(instance):
    assert isinstance(instance, umlknes_ControlNode)

@given(instance=umlknes_ActivityNode_strategy)
@settings(max_examples=50)
def test_umlknes_activitynode_instantiation(instance):
    assert isinstance(instance, umlknes_ActivityNode)

@given(instance=umlknes_Activity_strategy)
@settings(max_examples=50)
def test_umlknes_activity_instantiation(instance):
    assert isinstance(instance, umlknes_Activity)



@given(instance=umlknes_Activity_strategy)
def test_umlknes_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=umlknes_Activity_strategy)
def test_umlknes_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original
