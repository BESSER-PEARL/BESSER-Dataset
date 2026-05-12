import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    textualusecase::LoopStatement,
    textualusecase::ConditionalStatement,
    Step,
    Agent,
    textualusecase::Statement,
    textualusecase::FlowOfEvents,
    textualusecase::Action,
    textualusecase::Agent,
    FlowOfEvents,
    textualusecase::Include,
    textualusecase::Condition,
    textualusecase::Step,
    textualusecase::AlternativeFlow,
    textualusecase::Subject,
    textualusecase::Actor,
    textualusecase::UseCase,
    textualusecase::BasicFlow,
    textualusecase::UseCaseModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::loopstatement_is_not_abstract():
    assert not inspect.isabstract(textualusecase::LoopStatement)


def test_textualusecase::loopstatement_constructor_exists():
    assert callable(textualusecase::LoopStatement.__init__)


def test_textualusecase::loopstatement_constructor_args():
    sig = inspect.signature(textualusecase::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(textualusecase::ConditionalStatement)


def test_textualusecase::conditionalstatement_constructor_exists():
    assert callable(textualusecase::ConditionalStatement.__init__)


def test_textualusecase::conditionalstatement_constructor_args():
    sig = inspect.signature(textualusecase::ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_agent_is_not_abstract():
    assert not inspect.isabstract(Agent)


def test_agent_constructor_exists():
    assert callable(Agent.__init__)


def test_agent_constructor_args():
    sig = inspect.signature(Agent.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::statement_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Statement)


def test_textualusecase::statement_constructor_exists():
    assert callable(textualusecase::Statement.__init__)


def test_textualusecase::statement_constructor_args():
    sig = inspect.signature(textualusecase::Statement.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::flowofevents_is_not_abstract():
    assert not inspect.isabstract(textualusecase::FlowOfEvents)


def test_textualusecase::flowofevents_constructor_exists():
    assert callable(textualusecase::FlowOfEvents.__init__)


def test_textualusecase::flowofevents_constructor_args():
    sig = inspect.signature(textualusecase::FlowOfEvents.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_textualusecase::flowofevents_has_name():
    assert hasattr(textualusecase::FlowOfEvents, "name")
    descriptor = None
    for klass in textualusecase::FlowOfEvents.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_textualusecase::action_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Action)


def test_textualusecase::action_constructor_exists():
    assert callable(textualusecase::Action.__init__)


def test_textualusecase::action_constructor_args():
    sig = inspect.signature(textualusecase::Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_textualusecase::action_has_description():
    assert hasattr(textualusecase::Action, "description")
    descriptor = None
    for klass in textualusecase::Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_textualusecase::agent_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Agent)


def test_textualusecase::agent_constructor_exists():
    assert callable(textualusecase::Agent.__init__)


def test_textualusecase::agent_constructor_args():
    sig = inspect.signature(textualusecase::Agent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_textualusecase::agent_has_name():
    assert hasattr(textualusecase::Agent, "name")
    descriptor = None
    for klass in textualusecase::Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_flowofevents_is_not_abstract():
    assert not inspect.isabstract(FlowOfEvents)


def test_flowofevents_constructor_exists():
    assert callable(FlowOfEvents.__init__)


def test_flowofevents_constructor_args():
    sig = inspect.signature(FlowOfEvents.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::include_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Include)


def test_textualusecase::include_constructor_exists():
    assert callable(textualusecase::Include.__init__)


def test_textualusecase::include_constructor_args():
    sig = inspect.signature(textualusecase::Include.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::condition_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Condition)


def test_textualusecase::condition_constructor_exists():
    assert callable(textualusecase::Condition.__init__)


def test_textualusecase::condition_constructor_args():
    sig = inspect.signature(textualusecase::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_textualusecase::condition_has_expression():
    assert hasattr(textualusecase::Condition, "expression")
    descriptor = None
    for klass in textualusecase::Condition.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_textualusecase::step_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Step)


def test_textualusecase::step_constructor_exists():
    assert callable(textualusecase::Step.__init__)


def test_textualusecase::step_constructor_args():
    sig = inspect.signature(textualusecase::Step.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_textualusecase::step_has_name():
    assert hasattr(textualusecase::Step, "name")
    descriptor = None
    for klass in textualusecase::Step.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_textualusecase::alternativeflow_is_not_abstract():
    assert not inspect.isabstract(textualusecase::AlternativeFlow)


def test_textualusecase::alternativeflow_constructor_exists():
    assert callable(textualusecase::AlternativeFlow.__init__)


def test_textualusecase::alternativeflow_constructor_args():
    sig = inspect.signature(textualusecase::AlternativeFlow.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::subject_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Subject)


def test_textualusecase::subject_constructor_exists():
    assert callable(textualusecase::Subject.__init__)


def test_textualusecase::subject_constructor_args():
    sig = inspect.signature(textualusecase::Subject.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::actor_is_not_abstract():
    assert not inspect.isabstract(textualusecase::Actor)


def test_textualusecase::actor_constructor_exists():
    assert callable(textualusecase::Actor.__init__)


def test_textualusecase::actor_constructor_args():
    sig = inspect.signature(textualusecase::Actor.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::usecase_is_not_abstract():
    assert not inspect.isabstract(textualusecase::UseCase)


def test_textualusecase::usecase_constructor_exists():
    assert callable(textualusecase::UseCase.__init__)


def test_textualusecase::usecase_constructor_args():
    sig = inspect.signature(textualusecase::UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_textualusecase::usecase_has_description():
    assert hasattr(textualusecase::UseCase, "description")
    descriptor = None
    for klass in textualusecase::UseCase.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_textualusecase::usecase_has_name():
    assert hasattr(textualusecase::UseCase, "name")
    descriptor = None
    for klass in textualusecase::UseCase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_textualusecase::basicflow_is_not_abstract():
    assert not inspect.isabstract(textualusecase::BasicFlow)


def test_textualusecase::basicflow_constructor_exists():
    assert callable(textualusecase::BasicFlow.__init__)


def test_textualusecase::basicflow_constructor_args():
    sig = inspect.signature(textualusecase::BasicFlow.__init__)
    params = list(sig.parameters.keys())



def test_textualusecase::usecasemodel_is_not_abstract():
    assert not inspect.isabstract(textualusecase::UseCaseModel)


def test_textualusecase::usecasemodel_constructor_exists():
    assert callable(textualusecase::UseCaseModel.__init__)


def test_textualusecase::usecasemodel_constructor_args():
    sig = inspect.signature(textualusecase::UseCaseModel.__init__)
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
Statement_strategy = st.builds(
    Statement,
)
textualusecase::LoopStatement_strategy = st.builds(
    textualusecase::LoopStatement,
)
textualusecase::ConditionalStatement_strategy = st.builds(
    textualusecase::ConditionalStatement,
)
Step_strategy = st.builds(
    Step,
)
Agent_strategy = st.builds(
    Agent,
)
textualusecase::Statement_strategy = st.builds(
    textualusecase::Statement,
)
textualusecase::FlowOfEvents_strategy = st.builds(
    textualusecase::FlowOfEvents,
    name=
        safe_text
)
textualusecase::Action_strategy = st.builds(
    textualusecase::Action,
    description=
        safe_text
)
textualusecase::Agent_strategy = st.builds(
    textualusecase::Agent,
    name=
        safe_text
)
FlowOfEvents_strategy = st.builds(
    FlowOfEvents,
)
textualusecase::Include_strategy = st.builds(
    textualusecase::Include,
)
textualusecase::Condition_strategy = st.builds(
    textualusecase::Condition,
    expression=
        safe_text
)
textualusecase::Step_strategy = st.builds(
    textualusecase::Step,
    name=
        safe_text
)
textualusecase::AlternativeFlow_strategy = st.builds(
    textualusecase::AlternativeFlow,
)
textualusecase::Subject_strategy = st.builds(
    textualusecase::Subject,
)
textualusecase::Actor_strategy = st.builds(
    textualusecase::Actor,
)
textualusecase::UseCase_strategy = st.builds(
    textualusecase::UseCase,
    description=
        safe_text,
    name=
        safe_text
)
textualusecase::BasicFlow_strategy = st.builds(
    textualusecase::BasicFlow,
)
textualusecase::UseCaseModel_strategy = st.builds(
    textualusecase::UseCaseModel,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=textualusecase::LoopStatement_strategy)
@settings(max_examples=50)
def test_textualusecase::loopstatement_instantiation(instance):
    assert isinstance(instance, textualusecase::LoopStatement)

@given(instance=textualusecase::ConditionalStatement_strategy)
@settings(max_examples=50)
def test_textualusecase::conditionalstatement_instantiation(instance):
    assert isinstance(instance, textualusecase::ConditionalStatement)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=Agent_strategy)
@settings(max_examples=50)
def test_agent_instantiation(instance):
    assert isinstance(instance, Agent)

@given(instance=textualusecase::Statement_strategy)
@settings(max_examples=50)
def test_textualusecase::statement_instantiation(instance):
    assert isinstance(instance, textualusecase::Statement)

@given(instance=textualusecase::FlowOfEvents_strategy)
@settings(max_examples=50)
def test_textualusecase::flowofevents_instantiation(instance):
    assert isinstance(instance, textualusecase::FlowOfEvents)

@given(instance=textualusecase::FlowOfEvents_strategy)
def test_textualusecase::flowofevents_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=textualusecase::FlowOfEvents_strategy)
def test_textualusecase::flowofevents_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=textualusecase::Action_strategy)
@settings(max_examples=50)
def test_textualusecase::action_instantiation(instance):
    assert isinstance(instance, textualusecase::Action)

@given(instance=textualusecase::Action_strategy)
def test_textualusecase::action_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=textualusecase::Action_strategy)
def test_textualusecase::action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=textualusecase::Agent_strategy)
@settings(max_examples=50)
def test_textualusecase::agent_instantiation(instance):
    assert isinstance(instance, textualusecase::Agent)

@given(instance=textualusecase::Agent_strategy)
def test_textualusecase::agent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=textualusecase::Agent_strategy)
def test_textualusecase::agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FlowOfEvents_strategy)
@settings(max_examples=50)
def test_flowofevents_instantiation(instance):
    assert isinstance(instance, FlowOfEvents)

@given(instance=textualusecase::Include_strategy)
@settings(max_examples=50)
def test_textualusecase::include_instantiation(instance):
    assert isinstance(instance, textualusecase::Include)

@given(instance=textualusecase::Condition_strategy)
@settings(max_examples=50)
def test_textualusecase::condition_instantiation(instance):
    assert isinstance(instance, textualusecase::Condition)

@given(instance=textualusecase::Condition_strategy)
def test_textualusecase::condition_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=textualusecase::Condition_strategy)
def test_textualusecase::condition_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=textualusecase::Step_strategy)
@settings(max_examples=50)
def test_textualusecase::step_instantiation(instance):
    assert isinstance(instance, textualusecase::Step)

@given(instance=textualusecase::Step_strategy)
def test_textualusecase::step_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=textualusecase::Step_strategy)
def test_textualusecase::step_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=textualusecase::AlternativeFlow_strategy)
@settings(max_examples=50)
def test_textualusecase::alternativeflow_instantiation(instance):
    assert isinstance(instance, textualusecase::AlternativeFlow)

@given(instance=textualusecase::Subject_strategy)
@settings(max_examples=50)
def test_textualusecase::subject_instantiation(instance):
    assert isinstance(instance, textualusecase::Subject)

@given(instance=textualusecase::Actor_strategy)
@settings(max_examples=50)
def test_textualusecase::actor_instantiation(instance):
    assert isinstance(instance, textualusecase::Actor)

@given(instance=textualusecase::UseCase_strategy)
@settings(max_examples=50)
def test_textualusecase::usecase_instantiation(instance):
    assert isinstance(instance, textualusecase::UseCase)

@given(instance=textualusecase::UseCase_strategy)
def test_textualusecase::usecase_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=textualusecase::UseCase_strategy)
def test_textualusecase::usecase_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=textualusecase::UseCase_strategy)
def test_textualusecase::usecase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=textualusecase::UseCase_strategy)
def test_textualusecase::usecase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=textualusecase::BasicFlow_strategy)
@settings(max_examples=50)
def test_textualusecase::basicflow_instantiation(instance):
    assert isinstance(instance, textualusecase::BasicFlow)

@given(instance=textualusecase::UseCaseModel_strategy)
@settings(max_examples=50)
def test_textualusecase::usecasemodel_instantiation(instance):
    assert isinstance(instance, textualusecase::UseCaseModel)
