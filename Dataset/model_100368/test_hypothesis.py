import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractAction,
    ClassicalExpression_BinaryIntegerExpression,
    FSMModel_IntegerAssignement,
    ClockExpressionAndRelation_BindableEntity,
    AbstractTrigger,
    ClassicalExpression_ClassicalExpression,
    ClockExpressionAndRelation_ConcreteEntity,
    FSMModel_Trigger,
    ClassicalExpression_BooleanExpression,
    AbstractGuard,
    FSMModel_Guard,
    FSMModel_AbstractTrigger,
    FSMModel_AbstractGuard,
    FSMModel_DeclarationBlock,
    FSMModel_AbstractAction,
    NamedElement,
    FSMModel_Transition,
    FSMModel_StateMachineDefinition,
    FSMModel_State,
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



def test_classicalexpression_binaryintegerexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression_BinaryIntegerExpression)


def test_classicalexpression_binaryintegerexpression_constructor_exists():
    assert callable(ClassicalExpression_BinaryIntegerExpression.__init__)


def test_classicalexpression_binaryintegerexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression_BinaryIntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_integerassignement_is_not_abstract():
    assert not inspect.isabstract(FSMModel_IntegerAssignement)


def test_fsmmodel_integerassignement_constructor_exists():
    assert callable(FSMModel_IntegerAssignement.__init__)


def test_fsmmodel_integerassignement_constructor_args():
    sig = inspect.signature(FSMModel_IntegerAssignement.__init__)
    params = list(sig.parameters.keys())



def test_clockexpressionandrelation_bindableentity_is_not_abstract():
    assert not inspect.isabstract(ClockExpressionAndRelation_BindableEntity)


def test_clockexpressionandrelation_bindableentity_constructor_exists():
    assert callable(ClockExpressionAndRelation_BindableEntity.__init__)


def test_clockexpressionandrelation_bindableentity_constructor_args():
    sig = inspect.signature(ClockExpressionAndRelation_BindableEntity.__init__)
    params = list(sig.parameters.keys())



def test_abstracttrigger_is_not_abstract():
    assert not inspect.isabstract(AbstractTrigger)


def test_abstracttrigger_constructor_exists():
    assert callable(AbstractTrigger.__init__)


def test_abstracttrigger_constructor_args():
    sig = inspect.signature(AbstractTrigger.__init__)
    params = list(sig.parameters.keys())



def test_classicalexpression_classicalexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression_ClassicalExpression)


def test_classicalexpression_classicalexpression_constructor_exists():
    assert callable(ClassicalExpression_ClassicalExpression.__init__)


def test_classicalexpression_classicalexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression_ClassicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_clockexpressionandrelation_concreteentity_is_not_abstract():
    assert not inspect.isabstract(ClockExpressionAndRelation_ConcreteEntity)


def test_clockexpressionandrelation_concreteentity_constructor_exists():
    assert callable(ClockExpressionAndRelation_ConcreteEntity.__init__)


def test_clockexpressionandrelation_concreteentity_constructor_args():
    sig = inspect.signature(ClockExpressionAndRelation_ConcreteEntity.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_trigger_is_not_abstract():
    assert not inspect.isabstract(FSMModel_Trigger)


def test_fsmmodel_trigger_constructor_exists():
    assert callable(FSMModel_Trigger.__init__)


def test_fsmmodel_trigger_constructor_args():
    sig = inspect.signature(FSMModel_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_classicalexpression_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ClassicalExpression_BooleanExpression)


def test_classicalexpression_booleanexpression_constructor_exists():
    assert callable(ClassicalExpression_BooleanExpression.__init__)


def test_classicalexpression_booleanexpression_constructor_args():
    sig = inspect.signature(ClassicalExpression_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_abstractguard_is_not_abstract():
    assert not inspect.isabstract(AbstractGuard)


def test_abstractguard_constructor_exists():
    assert callable(AbstractGuard.__init__)


def test_abstractguard_constructor_args():
    sig = inspect.signature(AbstractGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_guard_is_not_abstract():
    assert not inspect.isabstract(FSMModel_Guard)


def test_fsmmodel_guard_constructor_exists():
    assert callable(FSMModel_Guard.__init__)


def test_fsmmodel_guard_constructor_args():
    sig = inspect.signature(FSMModel_Guard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_abstracttrigger_is_not_abstract():
    assert not inspect.isabstract(FSMModel_AbstractTrigger)


def test_fsmmodel_abstracttrigger_constructor_exists():
    assert callable(FSMModel_AbstractTrigger.__init__)


def test_fsmmodel_abstracttrigger_constructor_args():
    sig = inspect.signature(FSMModel_AbstractTrigger.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_abstractguard_is_not_abstract():
    assert not inspect.isabstract(FSMModel_AbstractGuard)


def test_fsmmodel_abstractguard_constructor_exists():
    assert callable(FSMModel_AbstractGuard.__init__)


def test_fsmmodel_abstractguard_constructor_args():
    sig = inspect.signature(FSMModel_AbstractGuard.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_declarationblock_is_not_abstract():
    assert not inspect.isabstract(FSMModel_DeclarationBlock)


def test_fsmmodel_declarationblock_constructor_exists():
    assert callable(FSMModel_DeclarationBlock.__init__)


def test_fsmmodel_declarationblock_constructor_args():
    sig = inspect.signature(FSMModel_DeclarationBlock.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_abstractaction_is_not_abstract():
    assert not inspect.isabstract(FSMModel_AbstractAction)


def test_fsmmodel_abstractaction_constructor_exists():
    assert callable(FSMModel_AbstractAction.__init__)


def test_fsmmodel_abstractaction_constructor_args():
    sig = inspect.signature(FSMModel_AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_transition_is_not_abstract():
    assert not inspect.isabstract(FSMModel_Transition)


def test_fsmmodel_transition_constructor_exists():
    assert callable(FSMModel_Transition.__init__)


def test_fsmmodel_transition_constructor_args():
    sig = inspect.signature(FSMModel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_statemachinedefinition_is_not_abstract():
    assert not inspect.isabstract(FSMModel_StateMachineDefinition)


def test_fsmmodel_statemachinedefinition_constructor_exists():
    assert callable(FSMModel_StateMachineDefinition.__init__)


def test_fsmmodel_statemachinedefinition_constructor_args():
    sig = inspect.signature(FSMModel_StateMachineDefinition.__init__)
    params = list(sig.parameters.keys())



def test_fsmmodel_state_is_not_abstract():
    assert not inspect.isabstract(FSMModel_State)


def test_fsmmodel_state_constructor_exists():
    assert callable(FSMModel_State.__init__)


def test_fsmmodel_state_constructor_args():
    sig = inspect.signature(FSMModel_State.__init__)
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
ClassicalExpression_BinaryIntegerExpression_strategy = st.builds(
    ClassicalExpression_BinaryIntegerExpression,
)
FSMModel_IntegerAssignement_strategy = st.builds(
    FSMModel_IntegerAssignement,
)
ClockExpressionAndRelation_BindableEntity_strategy = st.builds(
    ClockExpressionAndRelation_BindableEntity,
)
AbstractTrigger_strategy = st.builds(
    AbstractTrigger,
)
ClassicalExpression_ClassicalExpression_strategy = st.builds(
    ClassicalExpression_ClassicalExpression,
)
ClockExpressionAndRelation_ConcreteEntity_strategy = st.builds(
    ClockExpressionAndRelation_ConcreteEntity,
)
FSMModel_Trigger_strategy = st.builds(
    FSMModel_Trigger,
)
ClassicalExpression_BooleanExpression_strategy = st.builds(
    ClassicalExpression_BooleanExpression,
)
AbstractGuard_strategy = st.builds(
    AbstractGuard,
)
FSMModel_Guard_strategy = st.builds(
    FSMModel_Guard,
)
FSMModel_AbstractTrigger_strategy = st.builds(
    FSMModel_AbstractTrigger,
)
FSMModel_AbstractGuard_strategy = st.builds(
    FSMModel_AbstractGuard,
)
FSMModel_DeclarationBlock_strategy = st.builds(
    FSMModel_DeclarationBlock,
)
FSMModel_AbstractAction_strategy = st.builds(
    FSMModel_AbstractAction,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
FSMModel_Transition_strategy = st.builds(
    FSMModel_Transition,
)
FSMModel_StateMachineDefinition_strategy = st.builds(
    FSMModel_StateMachineDefinition,
)
FSMModel_State_strategy = st.builds(
    FSMModel_State,
)

@given(instance=AbstractAction_strategy)
@settings(max_examples=50)
def test_abstractaction_instantiation(instance):
    assert isinstance(instance, AbstractAction)

@given(instance=ClassicalExpression_BinaryIntegerExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression_binaryintegerexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression_BinaryIntegerExpression)

@given(instance=FSMModel_IntegerAssignement_strategy)
@settings(max_examples=50)
def test_fsmmodel_integerassignement_instantiation(instance):
    assert isinstance(instance, FSMModel_IntegerAssignement)

@given(instance=ClockExpressionAndRelation_BindableEntity_strategy)
@settings(max_examples=50)
def test_clockexpressionandrelation_bindableentity_instantiation(instance):
    assert isinstance(instance, ClockExpressionAndRelation_BindableEntity)

@given(instance=AbstractTrigger_strategy)
@settings(max_examples=50)
def test_abstracttrigger_instantiation(instance):
    assert isinstance(instance, AbstractTrigger)

@given(instance=ClassicalExpression_ClassicalExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression_classicalexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression_ClassicalExpression)

@given(instance=ClockExpressionAndRelation_ConcreteEntity_strategy)
@settings(max_examples=50)
def test_clockexpressionandrelation_concreteentity_instantiation(instance):
    assert isinstance(instance, ClockExpressionAndRelation_ConcreteEntity)

@given(instance=FSMModel_Trigger_strategy)
@settings(max_examples=50)
def test_fsmmodel_trigger_instantiation(instance):
    assert isinstance(instance, FSMModel_Trigger)

@given(instance=ClassicalExpression_BooleanExpression_strategy)
@settings(max_examples=50)
def test_classicalexpression_booleanexpression_instantiation(instance):
    assert isinstance(instance, ClassicalExpression_BooleanExpression)

@given(instance=AbstractGuard_strategy)
@settings(max_examples=50)
def test_abstractguard_instantiation(instance):
    assert isinstance(instance, AbstractGuard)

@given(instance=FSMModel_Guard_strategy)
@settings(max_examples=50)
def test_fsmmodel_guard_instantiation(instance):
    assert isinstance(instance, FSMModel_Guard)

@given(instance=FSMModel_AbstractTrigger_strategy)
@settings(max_examples=50)
def test_fsmmodel_abstracttrigger_instantiation(instance):
    assert isinstance(instance, FSMModel_AbstractTrigger)

@given(instance=FSMModel_AbstractGuard_strategy)
@settings(max_examples=50)
def test_fsmmodel_abstractguard_instantiation(instance):
    assert isinstance(instance, FSMModel_AbstractGuard)

@given(instance=FSMModel_DeclarationBlock_strategy)
@settings(max_examples=50)
def test_fsmmodel_declarationblock_instantiation(instance):
    assert isinstance(instance, FSMModel_DeclarationBlock)

@given(instance=FSMModel_AbstractAction_strategy)
@settings(max_examples=50)
def test_fsmmodel_abstractaction_instantiation(instance):
    assert isinstance(instance, FSMModel_AbstractAction)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=FSMModel_Transition_strategy)
@settings(max_examples=50)
def test_fsmmodel_transition_instantiation(instance):
    assert isinstance(instance, FSMModel_Transition)

@given(instance=FSMModel_StateMachineDefinition_strategy)
@settings(max_examples=50)
def test_fsmmodel_statemachinedefinition_instantiation(instance):
    assert isinstance(instance, FSMModel_StateMachineDefinition)

@given(instance=FSMModel_State_strategy)
@settings(max_examples=50)
def test_fsmmodel_state_instantiation(instance):
    assert isinstance(instance, FSMModel_State)
