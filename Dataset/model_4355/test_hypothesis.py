import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::ParameterDeclaration,
    model::ConstantDeclaration,
    model::VariableDeclaration,
    model::ReferenceExpression,
    model::Expression,
    model::Branch,
    Statement,
    model::SwitchStatement,
    model::VariableDeclarationStatement,
    model::ExpressionStatement,
    model::ChoiceStatement,
    model::IfStatement,
    model::BreakStatement,
    model::ReturnStatement,
    model::AssignmentStatement,
    model::ForStatement,
    model::ConstantDeclarationStatement,
    model::EmptyStatement,
    Action,
    model::Statement,
    model::Action,
    model::Block,
    FunctionDeclaration,
    model::ProcedureDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ParameterDeclaration)


def test_model::parameterdeclaration_constructor_exists():
    assert callable(model::ParameterDeclaration.__init__)


def test_model::parameterdeclaration_constructor_args():
    sig = inspect.signature(model::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ConstantDeclaration)


def test_model::constantdeclaration_constructor_exists():
    assert callable(model::ConstantDeclaration.__init__)


def test_model::constantdeclaration_constructor_args():
    sig = inspect.signature(model::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model::VariableDeclaration)


def test_model::variabledeclaration_constructor_exists():
    assert callable(model::VariableDeclaration.__init__)


def test_model::variabledeclaration_constructor_args():
    sig = inspect.signature(model::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::referenceexpression_is_not_abstract():
    assert not inspect.isabstract(model::ReferenceExpression)


def test_model::referenceexpression_constructor_exists():
    assert callable(model::ReferenceExpression.__init__)


def test_model::referenceexpression_constructor_args():
    sig = inspect.signature(model::ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model::expression_is_not_abstract():
    assert not inspect.isabstract(model::Expression)


def test_model::expression_constructor_exists():
    assert callable(model::Expression.__init__)


def test_model::expression_constructor_args():
    sig = inspect.signature(model::Expression.__init__)
    params = list(sig.parameters.keys())



def test_model::branch_is_not_abstract():
    assert not inspect.isabstract(model::Branch)


def test_model::branch_constructor_exists():
    assert callable(model::Branch.__init__)


def test_model::branch_constructor_args():
    sig = inspect.signature(model::Branch.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_model::switchstatement_is_not_abstract():
    assert not inspect.isabstract(model::SwitchStatement)


def test_model::switchstatement_constructor_exists():
    assert callable(model::SwitchStatement.__init__)


def test_model::switchstatement_constructor_args():
    sig = inspect.signature(model::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(model::VariableDeclarationStatement)


def test_model::variabledeclarationstatement_constructor_exists():
    assert callable(model::VariableDeclarationStatement.__init__)


def test_model::variabledeclarationstatement_constructor_args():
    sig = inspect.signature(model::VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(model::ExpressionStatement)


def test_model::expressionstatement_constructor_exists():
    assert callable(model::ExpressionStatement.__init__)


def test_model::expressionstatement_constructor_args():
    sig = inspect.signature(model::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::choicestatement_is_not_abstract():
    assert not inspect.isabstract(model::ChoiceStatement)


def test_model::choicestatement_constructor_exists():
    assert callable(model::ChoiceStatement.__init__)


def test_model::choicestatement_constructor_args():
    sig = inspect.signature(model::ChoiceStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::ifstatement_is_not_abstract():
    assert not inspect.isabstract(model::IfStatement)


def test_model::ifstatement_constructor_exists():
    assert callable(model::IfStatement.__init__)


def test_model::ifstatement_constructor_args():
    sig = inspect.signature(model::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::breakstatement_is_not_abstract():
    assert not inspect.isabstract(model::BreakStatement)


def test_model::breakstatement_constructor_exists():
    assert callable(model::BreakStatement.__init__)


def test_model::breakstatement_constructor_args():
    sig = inspect.signature(model::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::returnstatement_is_not_abstract():
    assert not inspect.isabstract(model::ReturnStatement)


def test_model::returnstatement_constructor_exists():
    assert callable(model::ReturnStatement.__init__)


def test_model::returnstatement_constructor_args():
    sig = inspect.signature(model::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(model::AssignmentStatement)


def test_model::assignmentstatement_constructor_exists():
    assert callable(model::AssignmentStatement.__init__)


def test_model::assignmentstatement_constructor_args():
    sig = inspect.signature(model::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::forstatement_is_not_abstract():
    assert not inspect.isabstract(model::ForStatement)


def test_model::forstatement_constructor_exists():
    assert callable(model::ForStatement.__init__)


def test_model::forstatement_constructor_args():
    sig = inspect.signature(model::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::constantdeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(model::ConstantDeclarationStatement)


def test_model::constantdeclarationstatement_constructor_exists():
    assert callable(model::ConstantDeclarationStatement.__init__)


def test_model::constantdeclarationstatement_constructor_args():
    sig = inspect.signature(model::ConstantDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_model::emptystatement_is_not_abstract():
    assert not inspect.isabstract(model::EmptyStatement)


def test_model::emptystatement_constructor_exists():
    assert callable(model::EmptyStatement.__init__)


def test_model::emptystatement_constructor_args():
    sig = inspect.signature(model::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_model::statement_is_not_abstract():
    assert not inspect.isabstract(model::Statement)


def test_model::statement_constructor_exists():
    assert callable(model::Statement.__init__)


def test_model::statement_constructor_args():
    sig = inspect.signature(model::Statement.__init__)
    params = list(sig.parameters.keys())



def test_model::action_is_not_abstract():
    assert not inspect.isabstract(model::Action)


def test_model::action_constructor_exists():
    assert callable(model::Action.__init__)


def test_model::action_constructor_args():
    sig = inspect.signature(model::Action.__init__)
    params = list(sig.parameters.keys())



def test_model::block_is_not_abstract():
    assert not inspect.isabstract(model::Block)


def test_model::block_constructor_exists():
    assert callable(model::Block.__init__)


def test_model::block_constructor_args():
    sig = inspect.signature(model::Block.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model::proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(model::ProcedureDeclaration)


def test_model::proceduredeclaration_constructor_exists():
    assert callable(model::ProcedureDeclaration.__init__)


def test_model::proceduredeclaration_constructor_args():
    sig = inspect.signature(model::ProcedureDeclaration.__init__)
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
model::ParameterDeclaration_strategy = st.builds(
    model::ParameterDeclaration,
)
model::ConstantDeclaration_strategy = st.builds(
    model::ConstantDeclaration,
)
model::VariableDeclaration_strategy = st.builds(
    model::VariableDeclaration,
)
model::ReferenceExpression_strategy = st.builds(
    model::ReferenceExpression,
)
model::Expression_strategy = st.builds(
    model::Expression,
)
model::Branch_strategy = st.builds(
    model::Branch,
)
Statement_strategy = st.builds(
    Statement,
)
model::SwitchStatement_strategy = st.builds(
    model::SwitchStatement,
)
model::VariableDeclarationStatement_strategy = st.builds(
    model::VariableDeclarationStatement,
)
model::ExpressionStatement_strategy = st.builds(
    model::ExpressionStatement,
)
model::ChoiceStatement_strategy = st.builds(
    model::ChoiceStatement,
)
model::IfStatement_strategy = st.builds(
    model::IfStatement,
)
model::BreakStatement_strategy = st.builds(
    model::BreakStatement,
)
model::ReturnStatement_strategy = st.builds(
    model::ReturnStatement,
)
model::AssignmentStatement_strategy = st.builds(
    model::AssignmentStatement,
)
model::ForStatement_strategy = st.builds(
    model::ForStatement,
)
model::ConstantDeclarationStatement_strategy = st.builds(
    model::ConstantDeclarationStatement,
)
model::EmptyStatement_strategy = st.builds(
    model::EmptyStatement,
)
Action_strategy = st.builds(
    Action,
)
model::Statement_strategy = st.builds(
    model::Statement,
)
model::Action_strategy = st.builds(
    model::Action,
)
model::Block_strategy = st.builds(
    model::Block,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
model::ProcedureDeclaration_strategy = st.builds(
    model::ProcedureDeclaration,
)

@given(instance=model::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_model::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, model::ParameterDeclaration)

@given(instance=model::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_model::constantdeclaration_instantiation(instance):
    assert isinstance(instance, model::ConstantDeclaration)

@given(instance=model::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_model::variabledeclaration_instantiation(instance):
    assert isinstance(instance, model::VariableDeclaration)

@given(instance=model::ReferenceExpression_strategy)
@settings(max_examples=50)
def test_model::referenceexpression_instantiation(instance):
    assert isinstance(instance, model::ReferenceExpression)

@given(instance=model::Expression_strategy)
@settings(max_examples=50)
def test_model::expression_instantiation(instance):
    assert isinstance(instance, model::Expression)

@given(instance=model::Branch_strategy)
@settings(max_examples=50)
def test_model::branch_instantiation(instance):
    assert isinstance(instance, model::Branch)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=model::SwitchStatement_strategy)
@settings(max_examples=50)
def test_model::switchstatement_instantiation(instance):
    assert isinstance(instance, model::SwitchStatement)

@given(instance=model::VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_model::variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, model::VariableDeclarationStatement)

@given(instance=model::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_model::expressionstatement_instantiation(instance):
    assert isinstance(instance, model::ExpressionStatement)

@given(instance=model::ChoiceStatement_strategy)
@settings(max_examples=50)
def test_model::choicestatement_instantiation(instance):
    assert isinstance(instance, model::ChoiceStatement)

@given(instance=model::IfStatement_strategy)
@settings(max_examples=50)
def test_model::ifstatement_instantiation(instance):
    assert isinstance(instance, model::IfStatement)

@given(instance=model::BreakStatement_strategy)
@settings(max_examples=50)
def test_model::breakstatement_instantiation(instance):
    assert isinstance(instance, model::BreakStatement)

@given(instance=model::ReturnStatement_strategy)
@settings(max_examples=50)
def test_model::returnstatement_instantiation(instance):
    assert isinstance(instance, model::ReturnStatement)

@given(instance=model::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_model::assignmentstatement_instantiation(instance):
    assert isinstance(instance, model::AssignmentStatement)

@given(instance=model::ForStatement_strategy)
@settings(max_examples=50)
def test_model::forstatement_instantiation(instance):
    assert isinstance(instance, model::ForStatement)

@given(instance=model::ConstantDeclarationStatement_strategy)
@settings(max_examples=50)
def test_model::constantdeclarationstatement_instantiation(instance):
    assert isinstance(instance, model::ConstantDeclarationStatement)

@given(instance=model::EmptyStatement_strategy)
@settings(max_examples=50)
def test_model::emptystatement_instantiation(instance):
    assert isinstance(instance, model::EmptyStatement)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model::Statement_strategy)
@settings(max_examples=50)
def test_model::statement_instantiation(instance):
    assert isinstance(instance, model::Statement)

@given(instance=model::Action_strategy)
@settings(max_examples=50)
def test_model::action_instantiation(instance):
    assert isinstance(instance, model::Action)

@given(instance=model::Block_strategy)
@settings(max_examples=50)
def test_model::block_instantiation(instance):
    assert isinstance(instance, model::Block)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=model::ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_model::proceduredeclaration_instantiation(instance):
    assert isinstance(instance, model::ProcedureDeclaration)
