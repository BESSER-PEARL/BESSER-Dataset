import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ControlNode,
    activitydiagram::InitialNode,
    ActivityNode,
    activitydiagram::ControlNode,
    activitydiagram::SignalNode,
    activitydiagram::ObjectNode,
    activitydiagram::ActionNode,
    ObjectNode,
    activitydiagram::Pin,
    activitydiagram::DataStoreNode,
    activitydiagram::ExpansionNode,
    activitydiagram::ActivityParameterNode,
    FinalNode,
    activitydiagram::FlowFinalNode,
    activitydiagram::ActivityFinalNode,
    activitydiagram::TimeEventNode,
    activitydiagram::AcceptSignalNode,
    activitydiagram::DecisionNode,
    activitydiagram::MergeNode,
    activitydiagram::JoinNode,
    activitydiagram::ForkNode,
    activitydiagram::FinalNode,
    activitydiagram::ADElement,
    ADElement,
    activitydiagram::ActivityEdge,
    activitydiagram::ActivityNode,
    activitydiagram::Activity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::InitialNode)


def test_activitydiagram::initialnode_constructor_exists():
    assert callable(activitydiagram::InitialNode.__init__)


def test_activitydiagram::initialnode_constructor_args():
    sig = inspect.signature(activitydiagram::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::controlnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ControlNode)


def test_activitydiagram::controlnode_constructor_exists():
    assert callable(activitydiagram::ControlNode.__init__)


def test_activitydiagram::controlnode_constructor_args():
    sig = inspect.signature(activitydiagram::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::signalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::SignalNode)


def test_activitydiagram::signalnode_constructor_exists():
    assert callable(activitydiagram::SignalNode.__init__)


def test_activitydiagram::signalnode_constructor_args():
    sig = inspect.signature(activitydiagram::SignalNode.__init__)
    params = list(sig.parameters.keys())
    assert "signalId" in params, "Missing parameter 'signalId'"

def test_activitydiagram::signalnode_has_signalId():
    assert hasattr(activitydiagram::SignalNode, "signalId")
    descriptor = None
    for klass in activitydiagram::SignalNode.__mro__:
        if "signalId" in klass.__dict__:
            descriptor = klass.__dict__["signalId"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::objectnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ObjectNode)


def test_activitydiagram::objectnode_constructor_exists():
    assert callable(activitydiagram::ObjectNode.__init__)


def test_activitydiagram::objectnode_constructor_args():
    sig = inspect.signature(activitydiagram::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::actionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActionNode)


def test_activitydiagram::actionnode_constructor_exists():
    assert callable(activitydiagram::ActionNode.__init__)


def test_activitydiagram::actionnode_constructor_args():
    sig = inspect.signature(activitydiagram::ActionNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::pin_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::Pin)


def test_activitydiagram::pin_constructor_exists():
    assert callable(activitydiagram::Pin.__init__)


def test_activitydiagram::pin_constructor_args():
    sig = inspect.signature(activitydiagram::Pin.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::datastorenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::DataStoreNode)


def test_activitydiagram::datastorenode_constructor_exists():
    assert callable(activitydiagram::DataStoreNode.__init__)


def test_activitydiagram::datastorenode_constructor_args():
    sig = inspect.signature(activitydiagram::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::expansionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ExpansionNode)


def test_activitydiagram::expansionnode_constructor_exists():
    assert callable(activitydiagram::ExpansionNode.__init__)


def test_activitydiagram::expansionnode_constructor_args():
    sig = inspect.signature(activitydiagram::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityParameterNode)


def test_activitydiagram::activityparameternode_constructor_exists():
    assert callable(activitydiagram::ActivityParameterNode.__init__)


def test_activitydiagram::activityparameternode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_activitydiagram::activityparameternode_has_parameter():
    assert hasattr(activitydiagram::ActivityParameterNode, "parameter")
    descriptor = None
    for klass in activitydiagram::ActivityParameterNode.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::FlowFinalNode)


def test_activitydiagram::flowfinalnode_constructor_exists():
    assert callable(activitydiagram::FlowFinalNode.__init__)


def test_activitydiagram::flowfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityFinalNode)


def test_activitydiagram::activityfinalnode_constructor_exists():
    assert callable(activitydiagram::ActivityFinalNode.__init__)


def test_activitydiagram::activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::timeeventnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TimeEventNode)


def test_activitydiagram::timeeventnode_constructor_exists():
    assert callable(activitydiagram::TimeEventNode.__init__)


def test_activitydiagram::timeeventnode_constructor_args():
    sig = inspect.signature(activitydiagram::TimeEventNode.__init__)
    params = list(sig.parameters.keys())
    assert "cycle" in params, "Missing parameter 'cycle'"

def test_activitydiagram::timeeventnode_has_cycle():
    assert hasattr(activitydiagram::TimeEventNode, "cycle")
    descriptor = None
    for klass in activitydiagram::TimeEventNode.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::acceptsignalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::AcceptSignalNode)


def test_activitydiagram::acceptsignalnode_constructor_exists():
    assert callable(activitydiagram::AcceptSignalNode.__init__)


def test_activitydiagram::acceptsignalnode_constructor_args():
    sig = inspect.signature(activitydiagram::AcceptSignalNode.__init__)
    params = list(sig.parameters.keys())
    assert "signalId" in params, "Missing parameter 'signalId'"

def test_activitydiagram::acceptsignalnode_has_signalId():
    assert hasattr(activitydiagram::AcceptSignalNode, "signalId")
    descriptor = None
    for klass in activitydiagram::AcceptSignalNode.__mro__:
        if "signalId" in klass.__dict__:
            descriptor = klass.__dict__["signalId"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::DecisionNode)


def test_activitydiagram::decisionnode_constructor_exists():
    assert callable(activitydiagram::DecisionNode.__init__)


def test_activitydiagram::decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::MergeNode)


def test_activitydiagram::mergenode_constructor_exists():
    assert callable(activitydiagram::MergeNode.__init__)


def test_activitydiagram::mergenode_constructor_args():
    sig = inspect.signature(activitydiagram::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::JoinNode)


def test_activitydiagram::joinnode_constructor_exists():
    assert callable(activitydiagram::JoinNode.__init__)


def test_activitydiagram::joinnode_constructor_args():
    sig = inspect.signature(activitydiagram::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ForkNode)


def test_activitydiagram::forknode_constructor_exists():
    assert callable(activitydiagram::ForkNode.__init__)


def test_activitydiagram::forknode_constructor_args():
    sig = inspect.signature(activitydiagram::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::finalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::FinalNode)


def test_activitydiagram::finalnode_constructor_exists():
    assert callable(activitydiagram::FinalNode.__init__)


def test_activitydiagram::finalnode_constructor_args():
    sig = inspect.signature(activitydiagram::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::adelement_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ADElement)


def test_activitydiagram::adelement_constructor_exists():
    assert callable(activitydiagram::ADElement.__init__)


def test_activitydiagram::adelement_constructor_args():
    sig = inspect.signature(activitydiagram::ADElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activitydiagram::adelement_has_name():
    assert hasattr(activitydiagram::ADElement, "name")
    descriptor = None
    for klass in activitydiagram::ADElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adelement_is_not_abstract():
    assert not inspect.isabstract(ADElement)


def test_adelement_constructor_exists():
    assert callable(ADElement.__init__)


def test_adelement_constructor_args():
    sig = inspect.signature(ADElement.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::activityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityEdge)


def test_activitydiagram::activityedge_constructor_exists():
    assert callable(activitydiagram::ActivityEdge.__init__)


def test_activitydiagram::activityedge_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "guard" in params, "Missing parameter 'guard'"

def test_activitydiagram::activityedge_has_guard():
    assert hasattr(activitydiagram::ActivityEdge, "guard")
    descriptor = None
    for klass in activitydiagram::ActivityEdge.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::activitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::ActivityNode)


def test_activitydiagram::activitynode_constructor_exists():
    assert callable(activitydiagram::ActivityNode.__init__)


def test_activitydiagram::activitynode_constructor_args():
    sig = inspect.signature(activitydiagram::ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "current" in params, "Missing parameter 'current'"

def test_activitydiagram::activitynode_has_current():
    assert hasattr(activitydiagram::ActivityNode, "current")
    descriptor = None
    for klass in activitydiagram::ActivityNode.__mro__:
        if "current" in klass.__dict__:
            descriptor = klass.__dict__["current"]
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
ControlNode_strategy = st.builds(
    ControlNode,
)
activitydiagram::InitialNode_strategy = st.builds(
    activitydiagram::InitialNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
activitydiagram::ControlNode_strategy = st.builds(
    activitydiagram::ControlNode,
)
activitydiagram::SignalNode_strategy = st.builds(
    activitydiagram::SignalNode,
    signalId=
        safe_text
)
activitydiagram::ObjectNode_strategy = st.builds(
    activitydiagram::ObjectNode,
)
activitydiagram::ActionNode_strategy = st.builds(
    activitydiagram::ActionNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
activitydiagram::Pin_strategy = st.builds(
    activitydiagram::Pin,
)
activitydiagram::DataStoreNode_strategy = st.builds(
    activitydiagram::DataStoreNode,
)
activitydiagram::ExpansionNode_strategy = st.builds(
    activitydiagram::ExpansionNode,
)
activitydiagram::ActivityParameterNode_strategy = st.builds(
    activitydiagram::ActivityParameterNode,
    parameter=
        safe_text
)
FinalNode_strategy = st.builds(
    FinalNode,
)
activitydiagram::FlowFinalNode_strategy = st.builds(
    activitydiagram::FlowFinalNode,
)
activitydiagram::ActivityFinalNode_strategy = st.builds(
    activitydiagram::ActivityFinalNode,
)
activitydiagram::TimeEventNode_strategy = st.builds(
    activitydiagram::TimeEventNode,
    cycle=
        safe_text
)
activitydiagram::AcceptSignalNode_strategy = st.builds(
    activitydiagram::AcceptSignalNode,
    signalId=
        safe_text
)
activitydiagram::DecisionNode_strategy = st.builds(
    activitydiagram::DecisionNode,
)
activitydiagram::MergeNode_strategy = st.builds(
    activitydiagram::MergeNode,
)
activitydiagram::JoinNode_strategy = st.builds(
    activitydiagram::JoinNode,
)
activitydiagram::ForkNode_strategy = st.builds(
    activitydiagram::ForkNode,
)
activitydiagram::FinalNode_strategy = st.builds(
    activitydiagram::FinalNode,
)
activitydiagram::ADElement_strategy = st.builds(
    activitydiagram::ADElement,
    name=
        safe_text
)
ADElement_strategy = st.builds(
    ADElement,
)
activitydiagram::ActivityEdge_strategy = st.builds(
    activitydiagram::ActivityEdge,
    guard=
        st.booleans()
)
activitydiagram::ActivityNode_strategy = st.builds(
    activitydiagram::ActivityNode,
    current=
        st.booleans()
)
activitydiagram::Activity_strategy = st.builds(
    activitydiagram::Activity,
)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=activitydiagram::InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::InitialNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=activitydiagram::ControlNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::controlnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ControlNode)

@given(instance=activitydiagram::SignalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::signalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::SignalNode)

@given(instance=activitydiagram::SignalNode_strategy)
def test_activitydiagram::signalnode_signalId_type(instance):
    assert isinstance(instance.signalId, str)


@given(instance=activitydiagram::SignalNode_strategy)
def test_activitydiagram::signalnode_signalId_setter(instance):
    original = instance.signalId
    instance.signalId = original
    assert instance.signalId == original

@given(instance=activitydiagram::ObjectNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::objectnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ObjectNode)

@given(instance=activitydiagram::ActionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::actionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActionNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=activitydiagram::Pin_strategy)
@settings(max_examples=50)
def test_activitydiagram::pin_instantiation(instance):
    assert isinstance(instance, activitydiagram::Pin)

@given(instance=activitydiagram::DataStoreNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::datastorenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::DataStoreNode)

@given(instance=activitydiagram::ExpansionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::expansionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ExpansionNode)

@given(instance=activitydiagram::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityparameternode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityParameterNode)

@given(instance=activitydiagram::ActivityParameterNode_strategy)
def test_activitydiagram::activityparameternode_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=activitydiagram::ActivityParameterNode_strategy)
def test_activitydiagram::activityparameternode_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=activitydiagram::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::flowfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::FlowFinalNode)

@given(instance=activitydiagram::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityFinalNode)

@given(instance=activitydiagram::TimeEventNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::timeeventnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TimeEventNode)

@given(instance=activitydiagram::TimeEventNode_strategy)
def test_activitydiagram::timeeventnode_cycle_type(instance):
    assert isinstance(instance.cycle, str)


@given(instance=activitydiagram::TimeEventNode_strategy)
def test_activitydiagram::timeeventnode_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=activitydiagram::AcceptSignalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::acceptsignalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::AcceptSignalNode)

@given(instance=activitydiagram::AcceptSignalNode_strategy)
def test_activitydiagram::acceptsignalnode_signalId_type(instance):
    assert isinstance(instance.signalId, str)


@given(instance=activitydiagram::AcceptSignalNode_strategy)
def test_activitydiagram::acceptsignalnode_signalId_setter(instance):
    original = instance.signalId
    instance.signalId = original
    assert instance.signalId == original

@given(instance=activitydiagram::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::DecisionNode)

@given(instance=activitydiagram::MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::MergeNode)

@given(instance=activitydiagram::JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::JoinNode)

@given(instance=activitydiagram::ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ForkNode)

@given(instance=activitydiagram::FinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::finalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::FinalNode)

@given(instance=activitydiagram::ADElement_strategy)
@settings(max_examples=50)
def test_activitydiagram::adelement_instantiation(instance):
    assert isinstance(instance, activitydiagram::ADElement)

@given(instance=activitydiagram::ADElement_strategy)
def test_activitydiagram::adelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=activitydiagram::ADElement_strategy)
def test_activitydiagram::adelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ADElement_strategy)
@settings(max_examples=50)
def test_adelement_instantiation(instance):
    assert isinstance(instance, ADElement)

@given(instance=activitydiagram::ActivityEdge_strategy)
@settings(max_examples=50)
def test_activitydiagram::activityedge_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityEdge)

@given(instance=activitydiagram::ActivityEdge_strategy)
def test_activitydiagram::activityedge_guard_type(instance):
    assert isinstance(instance.guard, bool)


@given(instance=activitydiagram::ActivityEdge_strategy)
def test_activitydiagram::activityedge_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original

@given(instance=activitydiagram::ActivityNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::activitynode_instantiation(instance):
    assert isinstance(instance, activitydiagram::ActivityNode)

@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_current_type(instance):
    assert isinstance(instance.current, bool)


@given(instance=activitydiagram::ActivityNode_strategy)
def test_activitydiagram::activitynode_current_setter(instance):
    original = instance.current
    instance.current = original
    assert instance.current == original

@given(instance=activitydiagram::Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram::activity_instantiation(instance):
    assert isinstance(instance, activitydiagram::Activity)
