import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateContainer,
    Named,
    workflow::AbstractState,
    workflow::StateTransition,
    workflow::Workflow,
    IntermediateState,
    workflow::SubProcess,
    workflow::Decision,
    workflow::Processing,
    workflow::Fork,
    workflow::Join,
    workflow::Task,
    ToState,
    FromState,
    AbstractState,
    workflow::End,
    workflow::IntermediateState,
    workflow::Start,
    workflow::StateContainer,
    workflow::ToState,
    workflow::FromState,
    EObject,
    workflow::Named,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statecontainer_is_not_abstract():
    assert not inspect.isabstract(StateContainer)


def test_statecontainer_constructor_exists():
    assert callable(StateContainer.__init__)


def test_statecontainer_constructor_args():
    sig = inspect.signature(StateContainer.__init__)
    params = list(sig.parameters.keys())



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_workflow::abstractstate_is_not_abstract():
    assert not inspect.isabstract(workflow::AbstractState)


def test_workflow::abstractstate_constructor_exists():
    assert callable(workflow::AbstractState.__init__)


def test_workflow::abstractstate_constructor_args():
    sig = inspect.signature(workflow::AbstractState.__init__)
    params = list(sig.parameters.keys())
    assert "associatedClass" in params, "Missing parameter 'associatedClass'"

def test_workflow::abstractstate_has_associatedClass():
    assert hasattr(workflow::AbstractState, "associatedClass")
    descriptor = None
    for klass in workflow::AbstractState.__mro__:
        if "associatedClass" in klass.__dict__:
            descriptor = klass.__dict__["associatedClass"]
            break
    assert isinstance(descriptor, property)



def test_workflow::statetransition_is_not_abstract():
    assert not inspect.isabstract(workflow::StateTransition)


def test_workflow::statetransition_constructor_exists():
    assert callable(workflow::StateTransition.__init__)


def test_workflow::statetransition_constructor_args():
    sig = inspect.signature(workflow::StateTransition.__init__)
    params = list(sig.parameters.keys())



def test_workflow::workflow_is_not_abstract():
    assert not inspect.isabstract(workflow::Workflow)


def test_workflow::workflow_constructor_exists():
    assert callable(workflow::Workflow.__init__)


def test_workflow::workflow_constructor_args():
    sig = inspect.signature(workflow::Workflow.__init__)
    params = list(sig.parameters.keys())



def test_intermediatestate_is_not_abstract():
    assert not inspect.isabstract(IntermediateState)


def test_intermediatestate_constructor_exists():
    assert callable(IntermediateState.__init__)


def test_intermediatestate_constructor_args():
    sig = inspect.signature(IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_workflow::subprocess_is_not_abstract():
    assert not inspect.isabstract(workflow::SubProcess)


def test_workflow::subprocess_constructor_exists():
    assert callable(workflow::SubProcess.__init__)


def test_workflow::subprocess_constructor_args():
    sig = inspect.signature(workflow::SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_workflow::decision_is_not_abstract():
    assert not inspect.isabstract(workflow::Decision)


def test_workflow::decision_constructor_exists():
    assert callable(workflow::Decision.__init__)


def test_workflow::decision_constructor_args():
    sig = inspect.signature(workflow::Decision.__init__)
    params = list(sig.parameters.keys())



def test_workflow::processing_is_not_abstract():
    assert not inspect.isabstract(workflow::Processing)


def test_workflow::processing_constructor_exists():
    assert callable(workflow::Processing.__init__)


def test_workflow::processing_constructor_args():
    sig = inspect.signature(workflow::Processing.__init__)
    params = list(sig.parameters.keys())



def test_workflow::fork_is_not_abstract():
    assert not inspect.isabstract(workflow::Fork)


def test_workflow::fork_constructor_exists():
    assert callable(workflow::Fork.__init__)


def test_workflow::fork_constructor_args():
    sig = inspect.signature(workflow::Fork.__init__)
    params = list(sig.parameters.keys())



def test_workflow::join_is_not_abstract():
    assert not inspect.isabstract(workflow::Join)


def test_workflow::join_constructor_exists():
    assert callable(workflow::Join.__init__)


def test_workflow::join_constructor_args():
    sig = inspect.signature(workflow::Join.__init__)
    params = list(sig.parameters.keys())



def test_workflow::task_is_not_abstract():
    assert not inspect.isabstract(workflow::Task)


def test_workflow::task_constructor_exists():
    assert callable(workflow::Task.__init__)


def test_workflow::task_constructor_args():
    sig = inspect.signature(workflow::Task.__init__)
    params = list(sig.parameters.keys())



def test_tostate_is_not_abstract():
    assert not inspect.isabstract(ToState)


def test_tostate_constructor_exists():
    assert callable(ToState.__init__)


def test_tostate_constructor_args():
    sig = inspect.signature(ToState.__init__)
    params = list(sig.parameters.keys())



def test_fromstate_is_not_abstract():
    assert not inspect.isabstract(FromState)


def test_fromstate_constructor_exists():
    assert callable(FromState.__init__)


def test_fromstate_constructor_args():
    sig = inspect.signature(FromState.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_workflow::end_is_not_abstract():
    assert not inspect.isabstract(workflow::End)


def test_workflow::end_constructor_exists():
    assert callable(workflow::End.__init__)


def test_workflow::end_constructor_args():
    sig = inspect.signature(workflow::End.__init__)
    params = list(sig.parameters.keys())



def test_workflow::intermediatestate_is_not_abstract():
    assert not inspect.isabstract(workflow::IntermediateState)


def test_workflow::intermediatestate_constructor_exists():
    assert callable(workflow::IntermediateState.__init__)


def test_workflow::intermediatestate_constructor_args():
    sig = inspect.signature(workflow::IntermediateState.__init__)
    params = list(sig.parameters.keys())



def test_workflow::start_is_not_abstract():
    assert not inspect.isabstract(workflow::Start)


def test_workflow::start_constructor_exists():
    assert callable(workflow::Start.__init__)


def test_workflow::start_constructor_args():
    sig = inspect.signature(workflow::Start.__init__)
    params = list(sig.parameters.keys())



def test_workflow::statecontainer_is_not_abstract():
    assert not inspect.isabstract(workflow::StateContainer)


def test_workflow::statecontainer_constructor_exists():
    assert callable(workflow::StateContainer.__init__)


def test_workflow::statecontainer_constructor_args():
    sig = inspect.signature(workflow::StateContainer.__init__)
    params = list(sig.parameters.keys())



def test_workflow::tostate_is_not_abstract():
    assert not inspect.isabstract(workflow::ToState)


def test_workflow::tostate_constructor_exists():
    assert callable(workflow::ToState.__init__)


def test_workflow::tostate_constructor_args():
    sig = inspect.signature(workflow::ToState.__init__)
    params = list(sig.parameters.keys())



def test_workflow::fromstate_is_not_abstract():
    assert not inspect.isabstract(workflow::FromState)


def test_workflow::fromstate_constructor_exists():
    assert callable(workflow::FromState.__init__)


def test_workflow::fromstate_constructor_args():
    sig = inspect.signature(workflow::FromState.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_workflow::named_is_not_abstract():
    assert not inspect.isabstract(workflow::Named)


def test_workflow::named_constructor_exists():
    assert callable(workflow::Named.__init__)


def test_workflow::named_constructor_args():
    sig = inspect.signature(workflow::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::named_has_name():
    assert hasattr(workflow::Named, "name")
    descriptor = None
    for klass in workflow::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
StateContainer_strategy = st.builds(
    StateContainer,
)
Named_strategy = st.builds(
    Named,
)
workflow::AbstractState_strategy = st.builds(
    workflow::AbstractState,
    associatedClass=
        safe_text
)
workflow::StateTransition_strategy = st.builds(
    workflow::StateTransition,
)
workflow::Workflow_strategy = st.builds(
    workflow::Workflow,
)
IntermediateState_strategy = st.builds(
    IntermediateState,
)
workflow::SubProcess_strategy = st.builds(
    workflow::SubProcess,
)
workflow::Decision_strategy = st.builds(
    workflow::Decision,
)
workflow::Processing_strategy = st.builds(
    workflow::Processing,
)
workflow::Fork_strategy = st.builds(
    workflow::Fork,
)
workflow::Join_strategy = st.builds(
    workflow::Join,
)
workflow::Task_strategy = st.builds(
    workflow::Task,
)
ToState_strategy = st.builds(
    ToState,
)
FromState_strategy = st.builds(
    FromState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
workflow::End_strategy = st.builds(
    workflow::End,
)
workflow::IntermediateState_strategy = st.builds(
    workflow::IntermediateState,
)
workflow::Start_strategy = st.builds(
    workflow::Start,
)
workflow::StateContainer_strategy = st.builds(
    workflow::StateContainer,
)
workflow::ToState_strategy = st.builds(
    workflow::ToState,
)
workflow::FromState_strategy = st.builds(
    workflow::FromState,
)
EObject_strategy = st.builds(
    EObject,
)
workflow::Named_strategy = st.builds(
    workflow::Named,
    name=
        safe_text
)

@given(instance=StateContainer_strategy)
@settings(max_examples=50)
def test_statecontainer_instantiation(instance):
    assert isinstance(instance, StateContainer)

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=workflow::AbstractState_strategy)
@settings(max_examples=50)
def test_workflow::abstractstate_instantiation(instance):
    assert isinstance(instance, workflow::AbstractState)

@given(instance=workflow::AbstractState_strategy)
def test_workflow::abstractstate_associatedClass_type(instance):
    assert isinstance(instance.associatedClass, str)


@given(instance=workflow::AbstractState_strategy)
def test_workflow::abstractstate_associatedClass_setter(instance):
    original = instance.associatedClass
    instance.associatedClass = original
    assert instance.associatedClass == original

@given(instance=workflow::StateTransition_strategy)
@settings(max_examples=50)
def test_workflow::statetransition_instantiation(instance):
    assert isinstance(instance, workflow::StateTransition)

@given(instance=workflow::Workflow_strategy)
@settings(max_examples=50)
def test_workflow::workflow_instantiation(instance):
    assert isinstance(instance, workflow::Workflow)

@given(instance=IntermediateState_strategy)
@settings(max_examples=50)
def test_intermediatestate_instantiation(instance):
    assert isinstance(instance, IntermediateState)

@given(instance=workflow::SubProcess_strategy)
@settings(max_examples=50)
def test_workflow::subprocess_instantiation(instance):
    assert isinstance(instance, workflow::SubProcess)

@given(instance=workflow::Decision_strategy)
@settings(max_examples=50)
def test_workflow::decision_instantiation(instance):
    assert isinstance(instance, workflow::Decision)

@given(instance=workflow::Processing_strategy)
@settings(max_examples=50)
def test_workflow::processing_instantiation(instance):
    assert isinstance(instance, workflow::Processing)

@given(instance=workflow::Fork_strategy)
@settings(max_examples=50)
def test_workflow::fork_instantiation(instance):
    assert isinstance(instance, workflow::Fork)

@given(instance=workflow::Join_strategy)
@settings(max_examples=50)
def test_workflow::join_instantiation(instance):
    assert isinstance(instance, workflow::Join)

@given(instance=workflow::Task_strategy)
@settings(max_examples=50)
def test_workflow::task_instantiation(instance):
    assert isinstance(instance, workflow::Task)

@given(instance=ToState_strategy)
@settings(max_examples=50)
def test_tostate_instantiation(instance):
    assert isinstance(instance, ToState)

@given(instance=FromState_strategy)
@settings(max_examples=50)
def test_fromstate_instantiation(instance):
    assert isinstance(instance, FromState)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=workflow::End_strategy)
@settings(max_examples=50)
def test_workflow::end_instantiation(instance):
    assert isinstance(instance, workflow::End)

@given(instance=workflow::IntermediateState_strategy)
@settings(max_examples=50)
def test_workflow::intermediatestate_instantiation(instance):
    assert isinstance(instance, workflow::IntermediateState)

@given(instance=workflow::Start_strategy)
@settings(max_examples=50)
def test_workflow::start_instantiation(instance):
    assert isinstance(instance, workflow::Start)

@given(instance=workflow::StateContainer_strategy)
@settings(max_examples=50)
def test_workflow::statecontainer_instantiation(instance):
    assert isinstance(instance, workflow::StateContainer)

@given(instance=workflow::ToState_strategy)
@settings(max_examples=50)
def test_workflow::tostate_instantiation(instance):
    assert isinstance(instance, workflow::ToState)

@given(instance=workflow::FromState_strategy)
@settings(max_examples=50)
def test_workflow::fromstate_instantiation(instance):
    assert isinstance(instance, workflow::FromState)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=workflow::Named_strategy)
@settings(max_examples=50)
def test_workflow::named_instantiation(instance):
    assert isinstance(instance, workflow::Named)

@given(instance=workflow::Named_strategy)
def test_workflow::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Named_strategy)
def test_workflow::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
