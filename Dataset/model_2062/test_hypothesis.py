import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    activitydiagram::Context,
    Value,
    activitydiagram::IntegerValue,
    activitydiagram::BooleanValue,
    Variable,
    activitydiagram::IntegerVariable,
    activitydiagram::Input,
    activitydiagram::InputValue,
    activitydiagram::Value,
    FinalNode,
    activitydiagram::ActivityFinalNode,
    activitydiagram::Trace,
    Token,
    activitydiagram::ForkedToken,
    activitydiagram::ControlToken,
    ActivityEdge,
    activitydiagram::ControlFlow,
    activitydiagram::Offer,
    activitydiagram::Token,
    activitydiagram::Variable,
    ControlNode,
    activitydiagram::FinalNode,
    activitydiagram::JoinNode,
    activitydiagram::MergeNode,
    activitydiagram::DecisionNode,
    activitydiagram::ForkNode,
    activitydiagram::InitialNode,
    activitydiagram::NamedActivity,
    activitydiagram::Exp,
    Action,
    activitydiagram::OpaqueAction,
    ExecutableNode,
    activitydiagram::Action,
    ActivityNode,
    activitydiagram::ExecutableNode,
    activitydiagram::ControlNode,
    activitydiagram::BooleanVariable,
    NamedActivity,
    activitydiagram::ActivityEdge,
    activitydiagram::ActivityNode,
    activitydiagram::Activity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activitydiagram::context_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Context)


def test_activitydiagram::context_constructor_exists():
    assert callable(activitydiagram::Context.__init__)


def test_activitydiagram::context_constructor_args():
    sig = inspect.signature(activitydiagram::Context.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integervalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerValue)


def test_activitydiagram::integervalue_constructor_exists():
    assert callable(activitydiagram::IntegerValue.__init__)


def test_activitydiagram::integervalue_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_activitydiagram::integervalue_has_value():
    assert hasattr(activitydiagram::IntegerValue, "value")
    descriptor = None
    for klass in activitydiagram::IntegerValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanValue)


def test_activitydiagram::booleanvalue_constructor_exists():
    assert callable(activitydiagram::BooleanValue.__init__)


def test_activitydiagram::booleanvalue_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_activitydiagram::booleanvalue_has_value():
    assert hasattr(activitydiagram::BooleanValue, "value")
    descriptor = None
    for klass in activitydiagram::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::integervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::IntegerVariable)


def test_activitydiagram::integervariable_constructor_exists():
    assert callable(activitydiagram::IntegerVariable.__init__)


def test_activitydiagram::integervariable_constructor_args():
    sig = inspect.signature(activitydiagram::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::input_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Input)


def test_activitydiagram::input_constructor_exists():
    assert callable(activitydiagram::Input.__init__)


def test_activitydiagram::input_constructor_args():
    sig = inspect.signature(activitydiagram::Input.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::inputvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::InputValue)


def test_activitydiagram::inputvalue_constructor_exists():
    assert callable(activitydiagram::InputValue.__init__)


def test_activitydiagram::inputvalue_constructor_args():
    sig = inspect.signature(activitydiagram::InputValue.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::value_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Value)


def test_activitydiagram::value_constructor_exists():
    assert callable(activitydiagram::Value.__init__)


def test_activitydiagram::value_constructor_args():
    sig = inspect.signature(activitydiagram::Value.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityFinalNode)


def test_activitydiagram::activityfinalnode_constructor_exists():
    assert callable(activitydiagram::ActivityFinalNode.__init__)


def test_activitydiagram::activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Trace)


def test_activitydiagram::trace_constructor_exists():
    assert callable(activitydiagram::Trace.__init__)


def test_activitydiagram::trace_constructor_args():
    sig = inspect.signature(activitydiagram::Trace.__init__)
    params = list(sig.parameters.keys())



def test_token_is_not_abstract():
    assert not inspect.isabstract(Token)


def test_token_constructor_exists():
    assert callable(Token.__init__)


def test_token_constructor_args():
    sig = inspect.signature(Token.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::forkedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ForkedToken)


def test_activitydiagram::forkedtoken_constructor_exists():
    assert callable(activitydiagram::ForkedToken.__init__)


def test_activitydiagram::forkedtoken_constructor_args():
    sig = inspect.signature(activitydiagram::ForkedToken.__init__)
    params = list(sig.parameters.keys())
    assert "remainingOffersCount" in params, "Missing parameter 'remainingOffersCount'"

def test_activitydiagram::forkedtoken_has_remainingOffersCount():
    assert hasattr(activitydiagram::ForkedToken, "remainingOffersCount")
    descriptor = None
    for klass in activitydiagram::ForkedToken.__mro__:
        if "remainingOffersCount" in klass.__dict__:
            descriptor = klass.__dict__["remainingOffersCount"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::controltoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlToken)


def test_activitydiagram::controltoken_constructor_exists():
    assert callable(activitydiagram::ControlToken.__init__)


def test_activitydiagram::controltoken_constructor_args():
    sig = inspect.signature(activitydiagram::ControlToken.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::controlflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlFlow)


def test_activitydiagram::controlflow_constructor_exists():
    assert callable(activitydiagram::ControlFlow.__init__)


def test_activitydiagram::controlflow_constructor_args():
    sig = inspect.signature(activitydiagram::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::offer_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Offer)


def test_activitydiagram::offer_constructor_exists():
    assert callable(activitydiagram::Offer.__init__)


def test_activitydiagram::offer_constructor_args():
    sig = inspect.signature(activitydiagram::Offer.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::token_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Token)


def test_activitydiagram::token_constructor_exists():
    assert callable(activitydiagram::Token.__init__)


def test_activitydiagram::token_constructor_args():
    sig = inspect.signature(activitydiagram::Token.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::variable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Variable)


def test_activitydiagram::variable_constructor_exists():
    assert callable(activitydiagram::Variable.__init__)


def test_activitydiagram::variable_constructor_args():
    sig = inspect.signature(activitydiagram::Variable.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::finalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::FinalNode)


def test_activitydiagram::finalnode_constructor_exists():
    assert callable(activitydiagram::FinalNode.__init__)


def test_activitydiagram::finalnode_constructor_args():
    sig = inspect.signature(activitydiagram::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::JoinNode)


def test_activitydiagram::joinnode_constructor_exists():
    assert callable(activitydiagram::JoinNode.__init__)


def test_activitydiagram::joinnode_constructor_args():
    sig = inspect.signature(activitydiagram::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::MergeNode)


def test_activitydiagram::mergenode_constructor_exists():
    assert callable(activitydiagram::MergeNode.__init__)


def test_activitydiagram::mergenode_constructor_args():
    sig = inspect.signature(activitydiagram::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::DecisionNode)


def test_activitydiagram::decisionnode_constructor_exists():
    assert callable(activitydiagram::DecisionNode.__init__)


def test_activitydiagram::decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ForkNode)


def test_activitydiagram::forknode_constructor_exists():
    assert callable(activitydiagram::ForkNode.__init__)


def test_activitydiagram::forknode_constructor_args():
    sig = inspect.signature(activitydiagram::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::InitialNode)


def test_activitydiagram::initialnode_constructor_exists():
    assert callable(activitydiagram::InitialNode.__init__)


def test_activitydiagram::initialnode_constructor_args():
    sig = inspect.signature(activitydiagram::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::namedactivity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::NamedActivity)


def test_activitydiagram::namedactivity_constructor_exists():
    assert callable(activitydiagram::NamedActivity.__init__)


def test_activitydiagram::namedactivity_constructor_args():
    sig = inspect.signature(activitydiagram::NamedActivity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activitydiagram::namedactivity_has_name():
    assert hasattr(activitydiagram::NamedActivity, "name")
    descriptor = None
    for klass in activitydiagram::NamedActivity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::exp_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Exp)


def test_activitydiagram::exp_constructor_exists():
    assert callable(activitydiagram::Exp.__init__)


def test_activitydiagram::exp_constructor_args():
    sig = inspect.signature(activitydiagram::Exp.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::OpaqueAction)


def test_activitydiagram::opaqueaction_constructor_exists():
    assert callable(activitydiagram::OpaqueAction.__init__)


def test_activitydiagram::opaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::action_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Action)


def test_activitydiagram::action_constructor_exists():
    assert callable(activitydiagram::Action.__init__)


def test_activitydiagram::action_constructor_args():
    sig = inspect.signature(activitydiagram::Action.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::executablenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ExecutableNode)


def test_activitydiagram::executablenode_constructor_exists():
    assert callable(activitydiagram::ExecutableNode.__init__)


def test_activitydiagram::executablenode_constructor_args():
    sig = inspect.signature(activitydiagram::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::controlnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlNode)


def test_activitydiagram::controlnode_constructor_exists():
    assert callable(activitydiagram::ControlNode.__init__)


def test_activitydiagram::controlnode_constructor_args():
    sig = inspect.signature(activitydiagram::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::BooleanVariable)


def test_activitydiagram::booleanvariable_constructor_exists():
    assert callable(activitydiagram::BooleanVariable.__init__)


def test_activitydiagram::booleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_namedactivity_is_not_abstract():
    assert not inspect.isabstract(NamedActivity)


def test_namedactivity_constructor_exists():
    assert callable(NamedActivity.__init__)


def test_namedactivity_constructor_args():
    sig = inspect.signature(NamedActivity.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityEdge)


def test_activitydiagram::activityedge_constructor_exists():
    assert callable(activitydiagram::ActivityEdge.__init__)


def test_activitydiagram::activityedge_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityNode)


def test_activitydiagram::activitynode_constructor_exists():
    assert callable(activitydiagram::ActivityNode.__init__)


def test_activitydiagram::activitynode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_activitydiagram::activitynode_has_running():
    assert hasattr(activitydiagram::ActivityNode, "running")
    descriptor = None
    for klass in activitydiagram::ActivityNode.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Activity)


def test_activitydiagram::activity_constructor_exists():
    assert callable(activitydiagram::Activity.__init__)


def test_activitydiagram::activity_constructor_args():
    sig = inspect.signature(activitydiagram::Activity.__init__)
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
activitydiagram::Context_strategy = st.builds(
    activitydiagram::Context,
)
Value_strategy = st.builds(
    Value,
)
activitydiagram::IntegerValue_strategy = st.builds(
    activitydiagram::IntegerValue,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
activitydiagram::BooleanValue_strategy = st.builds(
    activitydiagram::BooleanValue,
    value=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
activitydiagram::IntegerVariable_strategy = st.builds(
    activitydiagram::IntegerVariable,
)
activitydiagram::Input_strategy = st.builds(
    activitydiagram::Input,
)
activitydiagram::InputValue_strategy = st.builds(
    activitydiagram::InputValue,
)
activitydiagram::Value_strategy = st.builds(
    activitydiagram::Value,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
activitydiagram::ActivityFinalNode_strategy = st.builds(
    activitydiagram::ActivityFinalNode,
)
activitydiagram::Trace_strategy = st.builds(
    activitydiagram::Trace,
)
Token_strategy = st.builds(
    Token,
)
activitydiagram::ForkedToken_strategy = st.builds(
    activitydiagram::ForkedToken,
    remainingOffersCount=
        st.integers()
)
activitydiagram::ControlToken_strategy = st.builds(
    activitydiagram::ControlToken,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
activitydiagram::ControlFlow_strategy = st.builds(
    activitydiagram::ControlFlow,
)
activitydiagram::Offer_strategy = st.builds(
    activitydiagram::Offer,
)
activitydiagram::Token_strategy = st.builds(
    activitydiagram::Token,
)
activitydiagram::Variable_strategy = st.builds(
    activitydiagram::Variable,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
activitydiagram::FinalNode_strategy = st.builds(
    activitydiagram::FinalNode,
)
activitydiagram::JoinNode_strategy = st.builds(
    activitydiagram::JoinNode,
)
activitydiagram::MergeNode_strategy = st.builds(
    activitydiagram::MergeNode,
)
activitydiagram::DecisionNode_strategy = st.builds(
    activitydiagram::DecisionNode,
)
activitydiagram::ForkNode_strategy = st.builds(
    activitydiagram::ForkNode,
)
activitydiagram::InitialNode_strategy = st.builds(
    activitydiagram::InitialNode,
)
activitydiagram::NamedActivity_strategy = st.builds(
    activitydiagram::NamedActivity,
    name=
        safe_text
)
activitydiagram::Exp_strategy = st.builds(
    activitydiagram::Exp,
)
Action_strategy = st.builds(
    Action,
)
activitydiagram::OpaqueAction_strategy = st.builds(
    activitydiagram::OpaqueAction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
activitydiagram::Action_strategy = st.builds(
    activitydiagram::Action,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
activitydiagram::ExecutableNode_strategy = st.builds(
    activitydiagram::ExecutableNode,
)
activitydiagram::ControlNode_strategy = st.builds(
    activitydiagram::ControlNode,
)
activitydiagram::BooleanVariable_strategy = st.builds(
    activitydiagram::BooleanVariable,
)
NamedActivity_strategy = st.builds(
    NamedActivity,
)
activitydiagram::ActivityEdge_strategy = st.builds(
    activitydiagram::ActivityEdge,
)
activitydiagram::ActivityNode_strategy = st.builds(
    activitydiagram::ActivityNode,
    running=
        st.booleans()
)
activitydiagram::Activity_strategy = st.builds(
    activitydiagram::Activity,
)

@given(instance=activitydiagram::Context_strategy)
@settings(max_examples=50)
def test_activitydiagram::context_instantiation(instance):
    assert isinstance(instance, activitydiagram::Context)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=activitydiagram::IntegerValue_strategy)
@settings(max_examples=50)
def test_activitydiagram::integervalue_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerValue)

@given(instance=activitydiagram::IntegerValue_strategy)
def test_activitydiagram::integervalue_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=activitydiagram::IntegerValue_strategy)
def test_activitydiagram::integervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=activitydiagram::BooleanValue_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanvalue_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanValue)

@given(instance=activitydiagram::BooleanValue_strategy)
def test_activitydiagram::booleanvalue_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=activitydiagram::BooleanValue_strategy)
def test_activitydiagram::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=activitydiagram::IntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::integervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::IntegerVariable)

@given(instance=activitydiagram::Input_strategy)
@settings(max_examples=50)
def test_activitydiagram::input_instantiation(instance):
    assert isinstance(instance, activitydiagram::Input)

@given(instance=activitydiagram::InputValue_strategy)
@settings(max_examples=50)
def test_activitydiagram::inputvalue_instantiation(instance):
    assert isinstance(instance, activitydiagram::InputValue)

@given(instance=activitydiagram::Value_strategy)
@settings(max_examples=50)
def test_activitydiagram::value_instantiation(instance):
    assert isinstance(instance, activitydiagram::Value)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=activitydiagram::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityFinalNode)

@given(instance=activitydiagram::Trace_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace_instantiation(instance):
    assert isinstance(instance, activitydiagram::Trace)

@given(instance=Token_strategy)
@settings(max_examples=50)
def test_token_instantiation(instance):
    assert isinstance(instance, Token)

@given(instance=activitydiagram::ForkedToken_strategy)
@settings(max_examples=50)
def test_activitydiagram::forkedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagram::ForkedToken)

@given(instance=activitydiagram::ForkedToken_strategy)
def test_activitydiagram::forkedtoken_remainingOffersCount_type(instance):
    assert isinstance(instance.remainingOffersCount, int)


@given(instance=activitydiagram::ForkedToken_strategy)
def test_activitydiagram::forkedtoken_remainingOffersCount_setter(instance):
    original = instance.remainingOffersCount
    instance.remainingOffersCount = original
    assert instance.remainingOffersCount == original

@given(instance=activitydiagram::ControlToken_strategy)
@settings(max_examples=50)
def test_activitydiagram::controltoken_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlToken)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=activitydiagram::ControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::controlflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlFlow)

@given(instance=activitydiagram::Offer_strategy)
@settings(max_examples=50)
def test_activitydiagram::offer_instantiation(instance):
    assert isinstance(instance, activitydiagram::Offer)

@given(instance=activitydiagram::Token_strategy)
@settings(max_examples=50)
def test_activitydiagram::token_instantiation(instance):
    assert isinstance(instance, activitydiagram::Token)

@given(instance=activitydiagram::Variable_strategy)
@settings(max_examples=50)
def test_activitydiagram::variable_instantiation(instance):
    assert isinstance(instance, activitydiagram::Variable)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=activitydiagram::FinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::finalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::FinalNode)

@given(instance=activitydiagram::JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::JoinNode)

@given(instance=activitydiagram::MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::MergeNode)

@given(instance=activitydiagram::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::DecisionNode)

@given(instance=activitydiagram::ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ForkNode)

@given(instance=activitydiagram::InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::InitialNode)

@given(instance=activitydiagram::NamedActivity_strategy)
@settings(max_examples=50)
def test_activitydiagram::namedactivity_instantiation(instance):
    assert isinstance(instance, activitydiagram::NamedActivity)

@given(instance=activitydiagram::NamedActivity_strategy)
def test_activitydiagram::namedactivity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=activitydiagram::NamedActivity_strategy)
def test_activitydiagram::namedactivity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activitydiagram::Exp_strategy)
@settings(max_examples=50)
def test_activitydiagram::exp_instantiation(instance):
    assert isinstance(instance, activitydiagram::Exp)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=activitydiagram::OpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::opaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::OpaqueAction)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=activitydiagram::Action_strategy)
@settings(max_examples=50)
def test_activitydiagram::action_instantiation(instance):
    assert isinstance(instance, activitydiagram::Action)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=activitydiagram::ExecutableNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::executablenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ExecutableNode)

@given(instance=activitydiagram::ControlNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::controlnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlNode)

@given(instance=activitydiagram::BooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::booleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::BooleanVariable)

@given(instance=NamedActivity_strategy)
@settings(max_examples=50)
def test_namedactivity_instantiation(instance):
    assert isinstance(instance, NamedActivity)

@given(instance=activitydiagram::ActivityEdge_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityedge_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityEdge)

@given(instance=activitydiagram::ActivityNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activitynode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityNode)

@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_running_type(instance):
    assert isinstance(instance.running, bool)


@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=activitydiagram::Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram::activity_instantiation(instance):
    assert isinstance(instance, activitydiagram::Activity)
