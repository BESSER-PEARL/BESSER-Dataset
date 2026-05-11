import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ActivityEdge,
    minuml2::ObjectFlow,
    minuml2::ControlFlow,
    minuml2::OpaqueExpression,
    minuml2::ModelElement,
    ActivityNode,
    minuml2::DecisionNode,
    minuml2::ObjectNode,
    minuml2::ActivityFinalNode,
    minuml2::InitialNode,
    minuml2::JoinNode,
    minuml2::ForkNode,
    minuml2::OpaqueAction,
    ModelElement,
    minuml2::ActivityNode,
    minuml2::ActivityEdge,
    minuml2::Activity,
    minuml2::ActivityPartition,
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



def test_minuml2::objectflow_is_not_abstract():
    assert not inspect.isabstract(minuml2::ObjectFlow)


def test_minuml2::objectflow_constructor_exists():
    assert callable(minuml2::ObjectFlow.__init__)


def test_minuml2::objectflow_constructor_args():
    sig = inspect.signature(minuml2::ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::controlflow_is_not_abstract():
    assert not inspect.isabstract(minuml2::ControlFlow)


def test_minuml2::controlflow_constructor_exists():
    assert callable(minuml2::ControlFlow.__init__)


def test_minuml2::controlflow_constructor_args():
    sig = inspect.signature(minuml2::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(minuml2::OpaqueExpression)


def test_minuml2::opaqueexpression_constructor_exists():
    assert callable(minuml2::OpaqueExpression.__init__)


def test_minuml2::opaqueexpression_constructor_args():
    sig = inspect.signature(minuml2::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"

def test_minuml2::opaqueexpression_has_language():
    assert hasattr(minuml2::OpaqueExpression, "language")
    descriptor = None
    for klass in minuml2::OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_minuml2::opaqueexpression_has_body():
    assert hasattr(minuml2::OpaqueExpression, "body")
    descriptor = None
    for klass in minuml2::OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_minuml2::modelelement_is_not_abstract():
    assert not inspect.isabstract(minuml2::ModelElement)


def test_minuml2::modelelement_constructor_exists():
    assert callable(minuml2::ModelElement.__init__)


def test_minuml2::modelelement_constructor_args():
    sig = inspect.signature(minuml2::ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minuml2::modelelement_has_name():
    assert hasattr(minuml2::ModelElement, "name")
    descriptor = None
    for klass in minuml2::ModelElement.__mro__:
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



def test_minuml2::decisionnode_is_not_abstract():
    assert not inspect.isabstract(minuml2::DecisionNode)


def test_minuml2::decisionnode_constructor_exists():
    assert callable(minuml2::DecisionNode.__init__)


def test_minuml2::decisionnode_constructor_args():
    sig = inspect.signature(minuml2::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::objectnode_is_not_abstract():
    assert not inspect.isabstract(minuml2::ObjectNode)


def test_minuml2::objectnode_constructor_exists():
    assert callable(minuml2::ObjectNode.__init__)


def test_minuml2::objectnode_constructor_args():
    sig = inspect.signature(minuml2::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(minuml2::ActivityFinalNode)


def test_minuml2::activityfinalnode_constructor_exists():
    assert callable(minuml2::ActivityFinalNode.__init__)


def test_minuml2::activityfinalnode_constructor_args():
    sig = inspect.signature(minuml2::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::initialnode_is_not_abstract():
    assert not inspect.isabstract(minuml2::InitialNode)


def test_minuml2::initialnode_constructor_exists():
    assert callable(minuml2::InitialNode.__init__)


def test_minuml2::initialnode_constructor_args():
    sig = inspect.signature(minuml2::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::joinnode_is_not_abstract():
    assert not inspect.isabstract(minuml2::JoinNode)


def test_minuml2::joinnode_constructor_exists():
    assert callable(minuml2::JoinNode.__init__)


def test_minuml2::joinnode_constructor_args():
    sig = inspect.signature(minuml2::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::forknode_is_not_abstract():
    assert not inspect.isabstract(minuml2::ForkNode)


def test_minuml2::forknode_constructor_exists():
    assert callable(minuml2::ForkNode.__init__)


def test_minuml2::forknode_constructor_args():
    sig = inspect.signature(minuml2::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(minuml2::OpaqueAction)


def test_minuml2::opaqueaction_constructor_exists():
    assert callable(minuml2::OpaqueAction.__init__)


def test_minuml2::opaqueaction_constructor_args():
    sig = inspect.signature(minuml2::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::activitynode_is_not_abstract():
    assert not inspect.isabstract(minuml2::ActivityNode)


def test_minuml2::activitynode_constructor_exists():
    assert callable(minuml2::ActivityNode.__init__)


def test_minuml2::activitynode_constructor_args():
    sig = inspect.signature(minuml2::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::activityedge_is_not_abstract():
    assert not inspect.isabstract(minuml2::ActivityEdge)


def test_minuml2::activityedge_constructor_exists():
    assert callable(minuml2::ActivityEdge.__init__)


def test_minuml2::activityedge_constructor_args():
    sig = inspect.signature(minuml2::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::activity_is_not_abstract():
    assert not inspect.isabstract(minuml2::Activity)


def test_minuml2::activity_constructor_exists():
    assert callable(minuml2::Activity.__init__)


def test_minuml2::activity_constructor_args():
    sig = inspect.signature(minuml2::Activity.__init__)
    params = list(sig.parameters.keys())



def test_minuml2::activitypartition_is_not_abstract():
    assert not inspect.isabstract(minuml2::ActivityPartition)


def test_minuml2::activitypartition_constructor_exists():
    assert callable(minuml2::ActivityPartition.__init__)


def test_minuml2::activitypartition_constructor_args():
    sig = inspect.signature(minuml2::ActivityPartition.__init__)
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
minuml2::ObjectFlow_strategy = st.builds(
    minuml2::ObjectFlow,
)
minuml2::ControlFlow_strategy = st.builds(
    minuml2::ControlFlow,
)
minuml2::OpaqueExpression_strategy = st.builds(
    minuml2::OpaqueExpression,
    language=
        safe_text,
    body=
        safe_text
)
minuml2::ModelElement_strategy = st.builds(
    minuml2::ModelElement,
    name=
        safe_text
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
minuml2::DecisionNode_strategy = st.builds(
    minuml2::DecisionNode,
)
minuml2::ObjectNode_strategy = st.builds(
    minuml2::ObjectNode,
)
minuml2::ActivityFinalNode_strategy = st.builds(
    minuml2::ActivityFinalNode,
)
minuml2::InitialNode_strategy = st.builds(
    minuml2::InitialNode,
)
minuml2::JoinNode_strategy = st.builds(
    minuml2::JoinNode,
)
minuml2::ForkNode_strategy = st.builds(
    minuml2::ForkNode,
)
minuml2::OpaqueAction_strategy = st.builds(
    minuml2::OpaqueAction,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
minuml2::ActivityNode_strategy = st.builds(
    minuml2::ActivityNode,
)
minuml2::ActivityEdge_strategy = st.builds(
    minuml2::ActivityEdge,
)
minuml2::Activity_strategy = st.builds(
    minuml2::Activity,
)
minuml2::ActivityPartition_strategy = st.builds(
    minuml2::ActivityPartition,
)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=minuml2::ObjectFlow_strategy)
@settings(max_examples=50)
def test_minuml2::objectflow_instantiation(instance):
    assert isinstance(instance, minuml2::ObjectFlow)

@given(instance=minuml2::ControlFlow_strategy)
@settings(max_examples=50)
def test_minuml2::controlflow_instantiation(instance):
    assert isinstance(instance, minuml2::ControlFlow)

@given(instance=minuml2::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_minuml2::opaqueexpression_instantiation(instance):
    assert isinstance(instance, minuml2::OpaqueExpression)

@given(instance=minuml2::OpaqueExpression_strategy)
def test_minuml2::opaqueexpression_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=minuml2::OpaqueExpression_strategy)
def test_minuml2::opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=minuml2::OpaqueExpression_strategy)
def test_minuml2::opaqueexpression_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=minuml2::OpaqueExpression_strategy)
def test_minuml2::opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=minuml2::ModelElement_strategy)
@settings(max_examples=50)
def test_minuml2::modelelement_instantiation(instance):
    assert isinstance(instance, minuml2::ModelElement)

@given(instance=minuml2::ModelElement_strategy)
def test_minuml2::modelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minuml2::ModelElement_strategy)
def test_minuml2::modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=minuml2::DecisionNode_strategy)
@settings(max_examples=50)
def test_minuml2::decisionnode_instantiation(instance):
    assert isinstance(instance, minuml2::DecisionNode)

@given(instance=minuml2::ObjectNode_strategy)
@settings(max_examples=50)
def test_minuml2::objectnode_instantiation(instance):
    assert isinstance(instance, minuml2::ObjectNode)

@given(instance=minuml2::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_minuml2::activityfinalnode_instantiation(instance):
    assert isinstance(instance, minuml2::ActivityFinalNode)

@given(instance=minuml2::InitialNode_strategy)
@settings(max_examples=50)
def test_minuml2::initialnode_instantiation(instance):
    assert isinstance(instance, minuml2::InitialNode)

@given(instance=minuml2::JoinNode_strategy)
@settings(max_examples=50)
def test_minuml2::joinnode_instantiation(instance):
    assert isinstance(instance, minuml2::JoinNode)

@given(instance=minuml2::ForkNode_strategy)
@settings(max_examples=50)
def test_minuml2::forknode_instantiation(instance):
    assert isinstance(instance, minuml2::ForkNode)

@given(instance=minuml2::OpaqueAction_strategy)
@settings(max_examples=50)
def test_minuml2::opaqueaction_instantiation(instance):
    assert isinstance(instance, minuml2::OpaqueAction)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=minuml2::ActivityNode_strategy)
@settings(max_examples=50)
def test_minuml2::activitynode_instantiation(instance):
    assert isinstance(instance, minuml2::ActivityNode)

@given(instance=minuml2::ActivityEdge_strategy)
@settings(max_examples=50)
def test_minuml2::activityedge_instantiation(instance):
    assert isinstance(instance, minuml2::ActivityEdge)

@given(instance=minuml2::Activity_strategy)
@settings(max_examples=50)
def test_minuml2::activity_instantiation(instance):
    assert isinstance(instance, minuml2::Activity)

@given(instance=minuml2::ActivityPartition_strategy)
@settings(max_examples=50)
def test_minuml2::activitypartition_instantiation(instance):
    assert isinstance(instance, minuml2::ActivityPartition)
