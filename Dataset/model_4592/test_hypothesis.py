import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ActivityEdge,
    minuml2_ObjectFlow,
    minuml2_ControlFlow,
    minuml2_OpaqueExpression,
    minuml2_ModelElement,
    ActivityNode,
    minuml2_InitialNode,
    minuml2_DecisionNode,
    minuml2_JoinNode,
    minuml2_ForkNode,
    minuml2_ObjectNode,
    minuml2_ActivityFinalNode,
    minuml2_OpaqueAction,
    ModelElement,
    minuml2_ActivityEdge,
    minuml2_ActivityNode,
    minuml2_Activity,
    minuml2_ActivityPartition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_objectflow_is_not_abstract():
    assert not inspect.isabstract(minuml2_ObjectFlow)


def test_minuml2_objectflow_constructor_exists():
    assert callable(minuml2_ObjectFlow.__init__)


def test_minuml2_objectflow_constructor_args():
    sig = inspect.signature(minuml2_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_controlflow_is_not_abstract():
    assert not inspect.isabstract(minuml2_ControlFlow)


def test_minuml2_controlflow_constructor_exists():
    assert callable(minuml2_ControlFlow.__init__)


def test_minuml2_controlflow_constructor_args():
    sig = inspect.signature(minuml2_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(minuml2_OpaqueExpression)


def test_minuml2_opaqueexpression_constructor_exists():
    assert callable(minuml2_OpaqueExpression.__init__)


def test_minuml2_opaqueexpression_constructor_args():
    sig = inspect.signature(minuml2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_minuml2_opaqueexpression_has_body():
    assert hasattr(minuml2_OpaqueExpression, "body")
    descriptor = None
    for klass in minuml2_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_minuml2_opaqueexpression_has_language():
    assert hasattr(minuml2_OpaqueExpression, "language")
    descriptor = None
    for klass in minuml2_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_minuml2_modelelement_is_not_abstract():
    assert not inspect.isabstract(minuml2_ModelElement)


def test_minuml2_modelelement_constructor_exists():
    assert callable(minuml2_ModelElement.__init__)


def test_minuml2_modelelement_constructor_args():
    sig = inspect.signature(minuml2_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minuml2_modelelement_has_name():
    assert hasattr(minuml2_ModelElement, "name")
    descriptor = None
    for klass in minuml2_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_initialnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_InitialNode)


def test_minuml2_initialnode_constructor_exists():
    assert callable(minuml2_InitialNode.__init__)


def test_minuml2_initialnode_constructor_args():
    sig = inspect.signature(minuml2_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_decisionnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_DecisionNode)


def test_minuml2_decisionnode_constructor_exists():
    assert callable(minuml2_DecisionNode.__init__)


def test_minuml2_decisionnode_constructor_args():
    sig = inspect.signature(minuml2_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_joinnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_JoinNode)


def test_minuml2_joinnode_constructor_exists():
    assert callable(minuml2_JoinNode.__init__)


def test_minuml2_joinnode_constructor_args():
    sig = inspect.signature(minuml2_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_forknode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ForkNode)


def test_minuml2_forknode_constructor_exists():
    assert callable(minuml2_ForkNode.__init__)


def test_minuml2_forknode_constructor_args():
    sig = inspect.signature(minuml2_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_objectnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ObjectNode)


def test_minuml2_objectnode_constructor_exists():
    assert callable(minuml2_ObjectNode.__init__)


def test_minuml2_objectnode_constructor_args():
    sig = inspect.signature(minuml2_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityFinalNode)


def test_minuml2_activityfinalnode_constructor_exists():
    assert callable(minuml2_ActivityFinalNode.__init__)


def test_minuml2_activityfinalnode_constructor_args():
    sig = inspect.signature(minuml2_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(minuml2_OpaqueAction)


def test_minuml2_opaqueaction_constructor_exists():
    assert callable(minuml2_OpaqueAction.__init__)


def test_minuml2_opaqueaction_constructor_args():
    sig = inspect.signature(minuml2_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_activityedge_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityEdge)


def test_minuml2_activityedge_constructor_exists():
    assert callable(minuml2_ActivityEdge.__init__)


def test_minuml2_activityedge_constructor_args():
    sig = inspect.signature(minuml2_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_activitynode_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityNode)


def test_minuml2_activitynode_constructor_exists():
    assert callable(minuml2_ActivityNode.__init__)


def test_minuml2_activitynode_constructor_args():
    sig = inspect.signature(minuml2_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_activity_is_not_abstract():
    assert not inspect.isabstract(minuml2_Activity)


def test_minuml2_activity_constructor_exists():
    assert callable(minuml2_Activity.__init__)


def test_minuml2_activity_constructor_args():
    sig = inspect.signature(minuml2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_minuml2_activitypartition_is_not_abstract():
    assert not inspect.isabstract(minuml2_ActivityPartition)


def test_minuml2_activitypartition_constructor_exists():
    assert callable(minuml2_ActivityPartition.__init__)


def test_minuml2_activitypartition_constructor_args():
    sig = inspect.signature(minuml2_ActivityPartition.__init__)
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
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
minuml2_ObjectFlow_strategy = st.builds(
    minuml2_ObjectFlow,
)
minuml2_ControlFlow_strategy = st.builds(
    minuml2_ControlFlow,
)
minuml2_OpaqueExpression_strategy = st.builds(
    minuml2_OpaqueExpression,
    body=
        safe_text,
    language=
        safe_text
)
minuml2_ModelElement_strategy = st.builds(
    minuml2_ModelElement,
    name=
        safe_text
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
minuml2_InitialNode_strategy = st.builds(
    minuml2_InitialNode,
)
minuml2_DecisionNode_strategy = st.builds(
    minuml2_DecisionNode,
)
minuml2_JoinNode_strategy = st.builds(
    minuml2_JoinNode,
)
minuml2_ForkNode_strategy = st.builds(
    minuml2_ForkNode,
)
minuml2_ObjectNode_strategy = st.builds(
    minuml2_ObjectNode,
)
minuml2_ActivityFinalNode_strategy = st.builds(
    minuml2_ActivityFinalNode,
)
minuml2_OpaqueAction_strategy = st.builds(
    minuml2_OpaqueAction,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
minuml2_ActivityEdge_strategy = st.builds(
    minuml2_ActivityEdge,
)
minuml2_ActivityNode_strategy = st.builds(
    minuml2_ActivityNode,
)
minuml2_Activity_strategy = st.builds(
    minuml2_Activity,
)
minuml2_ActivityPartition_strategy = st.builds(
    minuml2_ActivityPartition,
)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=minuml2_ObjectFlow_strategy)
@settings(max_examples=50)
def test_minuml2_objectflow_instantiation(instance):
    assert isinstance(instance, minuml2_ObjectFlow)

@given(instance=minuml2_ControlFlow_strategy)
@settings(max_examples=50)
def test_minuml2_controlflow_instantiation(instance):
    assert isinstance(instance, minuml2_ControlFlow)

@given(instance=minuml2_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_minuml2_opaqueexpression_instantiation(instance):
    assert isinstance(instance, minuml2_OpaqueExpression)



@given(instance=minuml2_OpaqueExpression_strategy)
def test_minuml2_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=minuml2_OpaqueExpression_strategy)
def test_minuml2_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=minuml2_ModelElement_strategy)
@settings(max_examples=50)
def test_minuml2_modelelement_instantiation(instance):
    assert isinstance(instance, minuml2_ModelElement)



@given(instance=minuml2_ModelElement_strategy)
def test_minuml2_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=minuml2_InitialNode_strategy)
@settings(max_examples=50)
def test_minuml2_initialnode_instantiation(instance):
    assert isinstance(instance, minuml2_InitialNode)

@given(instance=minuml2_DecisionNode_strategy)
@settings(max_examples=50)
def test_minuml2_decisionnode_instantiation(instance):
    assert isinstance(instance, minuml2_DecisionNode)

@given(instance=minuml2_JoinNode_strategy)
@settings(max_examples=50)
def test_minuml2_joinnode_instantiation(instance):
    assert isinstance(instance, minuml2_JoinNode)

@given(instance=minuml2_ForkNode_strategy)
@settings(max_examples=50)
def test_minuml2_forknode_instantiation(instance):
    assert isinstance(instance, minuml2_ForkNode)

@given(instance=minuml2_ObjectNode_strategy)
@settings(max_examples=50)
def test_minuml2_objectnode_instantiation(instance):
    assert isinstance(instance, minuml2_ObjectNode)

@given(instance=minuml2_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_minuml2_activityfinalnode_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityFinalNode)

@given(instance=minuml2_OpaqueAction_strategy)
@settings(max_examples=50)
def test_minuml2_opaqueaction_instantiation(instance):
    assert isinstance(instance, minuml2_OpaqueAction)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=minuml2_ActivityEdge_strategy)
@settings(max_examples=50)
def test_minuml2_activityedge_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityEdge)

@given(instance=minuml2_ActivityNode_strategy)
@settings(max_examples=50)
def test_minuml2_activitynode_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityNode)

@given(instance=minuml2_Activity_strategy)
@settings(max_examples=50)
def test_minuml2_activity_instantiation(instance):
    assert isinstance(instance, minuml2_Activity)

@given(instance=minuml2_ActivityPartition_strategy)
@settings(max_examples=50)
def test_minuml2_activitypartition_instantiation(instance):
    assert isinstance(instance, minuml2_ActivityPartition)
