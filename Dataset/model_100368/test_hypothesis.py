import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbstractAction,
    ClassicalExpression::BinaryIntegerExpression,
    FSMModel::IntegerAssignement,
    ClockExpressionAndRelation::BindableEntity,
    AbstractTrigger,
    ClassicalExpression::ClassicalExpression,
    ClockExpressionAndRelation::ConcreteEntity,
    FSMModel::Trigger,
    ClassicalExpression::BooleanExpression,
    AbstractGuard,
    FSMModel::Guard,
    FSMModel::AbstractTrigger,
    FSMModel::AbstractGuard,
    FSMModel::DeclarationBlock,
    FSMModel::AbstractAction,
    NamedElement,
    FSMModel::StateMachineDefinition,
    FSMModel::Transition,
    FSMModel::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractaction_is_not_abstract():
    assert not inspect.isabstract(AbstractAction)


def test_abstractaction_constructor_exists():
    assert callable(AbstractAction.__init__)


def test_abstractaction_constructor_args():
    sig = inspect.signature(AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_classicalexpression::binaryintegerexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression::BinaryIntegerExpression)


def test_classicalexpression::binaryintegerexpression_constructor_exists():
    assert callable(ClassicalExpression::BinaryIntegerExpression.__init__)


def test_classicalexpression::binaryintegerexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression::BinaryIntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::integerassignement_is_not_abstract():
    assert not inspect.isabstract(FSMModel::IntegerAssignement)


def test_fsmmodel::integerassignement_constructor_exists():
    assert callable(FSMModel::IntegerAssignement.__init__)


def test_fsmmodel::integerassignement_constructor_args():
    sig = inspect.signature(FSMModel::IntegerAssignement.__init__)
    params = list(sig.parameters.keys())



def test_clockexpressionandrelation::bindableentity_is_not_abstract():
    assert not inspect.isabstract(ClockExpressionAndRelation::BindableEntity)


def test_clockexpressionandrelation::bindableentity_constructor_exists():
    assert callable(ClockExpressionAndRelation::BindableEntity.__init__)


def test_clockexpressionandrelation::bindableentity_constructor_args():
    sig = inspect.signature(ClockExpressionAndRelation::BindableEntity.__init__)
    params = list(sig.parameters.keys())



def test_abstracttrigger_is_not_abstract():
    assert not inspect.isabstract(AbstractTrigger)


def test_abstracttrigger_constructor_exists():
    assert callable(AbstractTrigger.__init__)


def test_abstracttrigger_constructor_args():
    sig = inspect.signature(AbstractTrigger.__init__)
    params = list(sig.parameters.keys())



def test_classicalexpression::classicalexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression::ClassicalExpression)


def test_classicalexpression::classicalexpression_constructor_exists():
    assert callable(ClassicalExpression::ClassicalExpression.__init__)


def test_classicalexpression::classicalexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression::ClassicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_clockexpressionandrelation::concreteentity_is_not_abstract():
    assert not inspect.isabstract(ClockExpressionAndRelation::ConcreteEntity)


def test_clockexpressionandrelation::concreteentity_constructor_exists():
    assert callable(ClockExpressionAndRelation::ConcreteEntity.__init__)


def test_clockexpressionandrelation::concreteentity_constructor_args():
    sig = inspect.signature(ClockExpressionAndRelation::ConcreteEntity.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::trigger_is_not_abstract():
    assert not inspect.isabstract(FSMModel::Trigger)


def test_fsmmodel::trigger_constructor_exists():
    assert callable(FSMModel::Trigger.__init__)


def test_fsmmodel::trigger_constructor_args():
    sig = inspect.signature(FSMModel::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_classicalexpression::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression::BooleanExpression)


def test_classicalexpression::booleanexpression_constructor_exists():
    assert callable(ClassicalExpression::BooleanExpression.__init__)


def test_classicalexpression::booleanexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractguard_is_not_abstract():
    assert not inspect.isabstract(AbstractGuard)


def test_abstractguard_constructor_exists():
    assert callable(AbstractGuard.__init__)


def test_abstractguard_constructor_args():
    sig = inspect.signature(AbstractGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::guard_is_not_abstract():
    assert not inspect.isabstract(FSMModel::Guard)


def test_fsmmodel::guard_constructor_exists():
    assert callable(FSMModel::Guard.__init__)


def test_fsmmodel::guard_constructor_args():
    sig = inspect.signature(FSMModel::Guard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::abstracttrigger_is_not_abstract():
    assert not inspect.isabstract(FSMModel::AbstractTrigger)


def test_fsmmodel::abstracttrigger_constructor_exists():
    assert callable(FSMModel::AbstractTrigger.__init__)


def test_fsmmodel::abstracttrigger_constructor_args():
    sig = inspect.signature(FSMModel::AbstractTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::abstractguard_is_not_abstract():
    assert not inspect.isabstract(FSMModel::AbstractGuard)


def test_fsmmodel::abstractguard_constructor_exists():
    assert callable(FSMModel::AbstractGuard.__init__)


def test_fsmmodel::abstractguard_constructor_args():
    sig = inspect.signature(FSMModel::AbstractGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::declarationblock_is_not_abstract():
    assert not inspect.isabstract(FSMModel::DeclarationBlock)


def test_fsmmodel::declarationblock_constructor_exists():
    assert callable(FSMModel::DeclarationBlock.__init__)


def test_fsmmodel::declarationblock_constructor_args():
    sig = inspect.signature(FSMModel::DeclarationBlock.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::abstractaction_is_not_abstract():
    assert not inspect.isabstract(FSMModel::AbstractAction)


def test_fsmmodel::abstractaction_constructor_exists():
    assert callable(FSMModel::AbstractAction.__init__)


def test_fsmmodel::abstractaction_constructor_args():
    sig = inspect.signature(FSMModel::AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::statemachinedefinition_is_not_abstract():
    assert not inspect.isabstract(FSMModel::StateMachineDefinition)


def test_fsmmodel::statemachinedefinition_constructor_exists():
    assert callable(FSMModel::StateMachineDefinition.__init__)


def test_fsmmodel::statemachinedefinition_constructor_args():
    sig = inspect.signature(FSMModel::StateMachineDefinition.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::transition_is_not_abstract():
    assert not inspect.isabstract(FSMModel::Transition)


def test_fsmmodel::transition_constructor_exists():
    assert callable(FSMModel::Transition.__init__)


def test_fsmmodel::transition_constructor_args():
    sig = inspect.signature(FSMModel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel::state_is_not_abstract():
    assert not inspect.isabstract(FSMModel::State)


def test_fsmmodel::state_constructor_exists():
    assert callable(FSMModel::State.__init__)


def test_fsmmodel::state_constructor_args():
    sig = inspect.signature(FSMModel::State.__init__)
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
AbstractAction_strategy = st.builds(
    AbstractAction,
)
ClassicalExpression::BinaryIntegerExpression_strategy = st.builds(
    ClassicalExpression::BinaryIntegerExpression,
)
FSMModel::IntegerAssignement_strategy = st.builds(
    FSMModel::IntegerAssignement,
)
ClockExpressionAndRelation::BindableEntity_strategy = st.builds(
    ClockExpressionAndRelation::BindableEntity,
)
AbstractTrigger_strategy = st.builds(
    AbstractTrigger,
)
ClassicalExpression::ClassicalExpression_strategy = st.builds(
    ClassicalExpression::ClassicalExpression,
)
ClockExpressionAndRelation::ConcreteEntity_strategy = st.builds(
    ClockExpressionAndRelation::ConcreteEntity,
)
FSMModel::Trigger_strategy = st.builds(
    FSMModel::Trigger,
)
ClassicalExpression::BooleanExpression_strategy = st.builds(
    ClassicalExpression::BooleanExpression,
)
AbstractGuard_strategy = st.builds(
    AbstractGuard,
)
FSMModel::Guard_strategy = st.builds(
    FSMModel::Guard,
)
FSMModel::AbstractTrigger_strategy = st.builds(
    FSMModel::AbstractTrigger,
)
FSMModel::AbstractGuard_strategy = st.builds(
    FSMModel::AbstractGuard,
)
FSMModel::DeclarationBlock_strategy = st.builds(
    FSMModel::DeclarationBlock,
)
FSMModel::AbstractAction_strategy = st.builds(
    FSMModel::AbstractAction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FSMModel::StateMachineDefinition_strategy = st.builds(
    FSMModel::StateMachineDefinition,
)
FSMModel::Transition_strategy = st.builds(
    FSMModel::Transition,
)
FSMModel::State_strategy = st.builds(
    FSMModel::State,
)

@given(instance=AbstractAction_strategy)
@settings(max_examples=50)
def test_abstractaction_instantiation(instance):
    assert isinstance(instance, AbstractAction)

@given(instance=ClassicalExpression::BinaryIntegerExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression::binaryintegerexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression::BinaryIntegerExpression)

@given(instance=FSMModel::IntegerAssignement_strategy)
@settings(max_examples=50)
def test_fsmmodel::integerassignement_instantiation(instance):
    assert isinstance(instance, FSMModel::IntegerAssignement)

@given(instance=ClockExpressionAndRelation::BindableEntity_strategy)
@settings(max_examples=50)
def test_clockexpressionandrelation::bindableentity_instantiation(instance):
    assert isinstance(instance, ClockExpressionAndRelation::BindableEntity)

@given(instance=AbstractTrigger_strategy)
@settings(max_examples=50)
def test_abstracttrigger_instantiation(instance):
    assert isinstance(instance, AbstractTrigger)

@given(instance=ClassicalExpression::ClassicalExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression::classicalexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression::ClassicalExpression)

@given(instance=ClockExpressionAndRelation::ConcreteEntity_strategy)
@settings(max_examples=50)
def test_clockexpressionandrelation::concreteentity_instantiation(instance):
    assert isinstance(instance, ClockExpressionAndRelation::ConcreteEntity)

@given(instance=FSMModel::Trigger_strategy)
@settings(max_examples=50)
def test_fsmmodel::trigger_instantiation(instance):
    assert isinstance(instance, FSMModel::Trigger)

@given(instance=ClassicalExpression::BooleanExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression::booleanexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression::BooleanExpression)

@given(instance=AbstractGuard_strategy)
@settings(max_examples=50)
def test_abstractguard_instantiation(instance):
    assert isinstance(instance, AbstractGuard)

@given(instance=FSMModel::Guard_strategy)
@settings(max_examples=50)
def test_fsmmodel::guard_instantiation(instance):
    assert isinstance(instance, FSMModel::Guard)

@given(instance=FSMModel::AbstractTrigger_strategy)
@settings(max_examples=50)
def test_fsmmodel::abstracttrigger_instantiation(instance):
    assert isinstance(instance, FSMModel::AbstractTrigger)

@given(instance=FSMModel::AbstractGuard_strategy)
@settings(max_examples=50)
def test_fsmmodel::abstractguard_instantiation(instance):
    assert isinstance(instance, FSMModel::AbstractGuard)

@given(instance=FSMModel::DeclarationBlock_strategy)
@settings(max_examples=50)
def test_fsmmodel::declarationblock_instantiation(instance):
    assert isinstance(instance, FSMModel::DeclarationBlock)

@given(instance=FSMModel::AbstractAction_strategy)
@settings(max_examples=50)
def test_fsmmodel::abstractaction_instantiation(instance):
    assert isinstance(instance, FSMModel::AbstractAction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FSMModel::StateMachineDefinition_strategy)
@settings(max_examples=50)
def test_fsmmodel::statemachinedefinition_instantiation(instance):
    assert isinstance(instance, FSMModel::StateMachineDefinition)

@given(instance=FSMModel::Transition_strategy)
@settings(max_examples=50)
def test_fsmmodel::transition_instantiation(instance):
    assert isinstance(instance, FSMModel::Transition)

@given(instance=FSMModel::State_strategy)
@settings(max_examples=50)
def test_fsmmodel::state_instantiation(instance):
    assert isinstance(instance, FSMModel::State)
