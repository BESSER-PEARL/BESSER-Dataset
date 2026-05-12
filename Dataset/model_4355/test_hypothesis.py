import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_ParameterDeclaration,
    model_ConstantDeclaration,
    model_VariableDeclaration,
    model_ReferenceExpression,
    model_Expression,
    model_Branch,
    Statement,
    model_ForStatement,
    model_SwitchStatement,
    model_ChoiceStatement,
    model_ReturnStatement,
    model_IfStatement,
    model_ConstantDeclarationStatement,
    model_VariableDeclarationStatement,
    model_ExpressionStatement,
    model_AssignmentStatement,
    model_BreakStatement,
    model_EmptyStatement,
    Action,
    model_Statement,
    model_Action,
    model_Block,
    FunctionDeclaration,
    model_ProcedureDeclaration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ParameterDeclaration)


def test_model_parameterdeclaration_constructor_exists():
    assert callable(model_ParameterDeclaration.__init__)


def test_model_parameterdeclaration_constructor_args():
    sig = inspect.signature(model_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ConstantDeclaration)


def test_model_constantdeclaration_constructor_exists():
    assert callable(model_ConstantDeclaration.__init__)


def test_model_constantdeclaration_constructor_args():
    sig = inspect.signature(model_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(model_VariableDeclaration)


def test_model_variabledeclaration_constructor_exists():
    assert callable(model_VariableDeclaration.__init__)


def test_model_variabledeclaration_constructor_args():
    sig = inspect.signature(model_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_referenceexpression_is_not_abstract():
    assert not inspect.isabstract(model_ReferenceExpression)


def test_model_referenceexpression_constructor_exists():
    assert callable(model_ReferenceExpression.__init__)


def test_model_referenceexpression_constructor_args():
    sig = inspect.signature(model_ReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_model_expression_is_not_abstract():
    assert not inspect.isabstract(model_Expression)


def test_model_expression_constructor_exists():
    assert callable(model_Expression.__init__)


def test_model_expression_constructor_args():
    sig = inspect.signature(model_Expression.__init__)
    params = list(sig.parameters.keys())



def test_model_branch_is_not_abstract():
    assert not inspect.isabstract(model_Branch)


def test_model_branch_constructor_exists():
    assert callable(model_Branch.__init__)


def test_model_branch_constructor_args():
    sig = inspect.signature(model_Branch.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_model_forstatement_is_not_abstract():
    assert not inspect.isabstract(model_ForStatement)


def test_model_forstatement_constructor_exists():
    assert callable(model_ForStatement.__init__)


def test_model_forstatement_constructor_args():
    sig = inspect.signature(model_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_switchstatement_is_not_abstract():
    assert not inspect.isabstract(model_SwitchStatement)


def test_model_switchstatement_constructor_exists():
    assert callable(model_SwitchStatement.__init__)


def test_model_switchstatement_constructor_args():
    sig = inspect.signature(model_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_choicestatement_is_not_abstract():
    assert not inspect.isabstract(model_ChoiceStatement)


def test_model_choicestatement_constructor_exists():
    assert callable(model_ChoiceStatement.__init__)


def test_model_choicestatement_constructor_args():
    sig = inspect.signature(model_ChoiceStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_returnstatement_is_not_abstract():
    assert not inspect.isabstract(model_ReturnStatement)


def test_model_returnstatement_constructor_exists():
    assert callable(model_ReturnStatement.__init__)


def test_model_returnstatement_constructor_args():
    sig = inspect.signature(model_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_ifstatement_is_not_abstract():
    assert not inspect.isabstract(model_IfStatement)


def test_model_ifstatement_constructor_exists():
    assert callable(model_IfStatement.__init__)


def test_model_ifstatement_constructor_args():
    sig = inspect.signature(model_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_constantdeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(model_ConstantDeclarationStatement)


def test_model_constantdeclarationstatement_constructor_exists():
    assert callable(model_ConstantDeclarationStatement.__init__)


def test_model_constantdeclarationstatement_constructor_args():
    sig = inspect.signature(model_ConstantDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_variabledeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(model_VariableDeclarationStatement)


def test_model_variabledeclarationstatement_constructor_exists():
    assert callable(model_VariableDeclarationStatement.__init__)


def test_model_variabledeclarationstatement_constructor_args():
    sig = inspect.signature(model_VariableDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_expressionstatement_is_not_abstract():
    assert not inspect.isabstract(model_ExpressionStatement)


def test_model_expressionstatement_constructor_exists():
    assert callable(model_ExpressionStatement.__init__)


def test_model_expressionstatement_constructor_args():
    sig = inspect.signature(model_ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(model_AssignmentStatement)


def test_model_assignmentstatement_constructor_exists():
    assert callable(model_AssignmentStatement.__init__)


def test_model_assignmentstatement_constructor_args():
    sig = inspect.signature(model_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_breakstatement_is_not_abstract():
    assert not inspect.isabstract(model_BreakStatement)


def test_model_breakstatement_constructor_exists():
    assert callable(model_BreakStatement.__init__)


def test_model_breakstatement_constructor_args():
    sig = inspect.signature(model_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_model_emptystatement_is_not_abstract():
    assert not inspect.isabstract(model_EmptyStatement)


def test_model_emptystatement_constructor_exists():
    assert callable(model_EmptyStatement.__init__)


def test_model_emptystatement_constructor_args():
    sig = inspect.signature(model_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_model_statement_is_not_abstract():
    assert not inspect.isabstract(model_Statement)


def test_model_statement_constructor_exists():
    assert callable(model_Statement.__init__)


def test_model_statement_constructor_args():
    sig = inspect.signature(model_Statement.__init__)
    params = list(sig.parameters.keys())



def test_model_action_is_not_abstract():
    assert not inspect.isabstract(model_Action)


def test_model_action_constructor_exists():
    assert callable(model_Action.__init__)


def test_model_action_constructor_args():
    sig = inspect.signature(model_Action.__init__)
    params = list(sig.parameters.keys())



def test_model_block_is_not_abstract():
    assert not inspect.isabstract(model_Block)


def test_model_block_constructor_exists():
    assert callable(model_Block.__init__)


def test_model_block_constructor_args():
    sig = inspect.signature(model_Block.__init__)
    params = list(sig.parameters.keys())



def test_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(FunctionDeclaration)


def test_functiondeclaration_constructor_exists():
    assert callable(FunctionDeclaration.__init__)


def test_functiondeclaration_constructor_args():
    sig = inspect.signature(FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_model_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(model_ProcedureDeclaration)


def test_model_proceduredeclaration_constructor_exists():
    assert callable(model_ProcedureDeclaration.__init__)


def test_model_proceduredeclaration_constructor_args():
    sig = inspect.signature(model_ProcedureDeclaration.__init__)
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
model_ParameterDeclaration_strategy = st.builds(
    model_ParameterDeclaration,
)
model_ConstantDeclaration_strategy = st.builds(
    model_ConstantDeclaration,
)
model_VariableDeclaration_strategy = st.builds(
    model_VariableDeclaration,
)
model_ReferenceExpression_strategy = st.builds(
    model_ReferenceExpression,
)
model_Expression_strategy = st.builds(
    model_Expression,
)
model_Branch_strategy = st.builds(
    model_Branch,
)
Statement_strategy = st.builds(
    Statement,
)
model_ForStatement_strategy = st.builds(
    model_ForStatement,
)
model_SwitchStatement_strategy = st.builds(
    model_SwitchStatement,
)
model_ChoiceStatement_strategy = st.builds(
    model_ChoiceStatement,
)
model_ReturnStatement_strategy = st.builds(
    model_ReturnStatement,
)
model_IfStatement_strategy = st.builds(
    model_IfStatement,
)
model_ConstantDeclarationStatement_strategy = st.builds(
    model_ConstantDeclarationStatement,
)
model_VariableDeclarationStatement_strategy = st.builds(
    model_VariableDeclarationStatement,
)
model_ExpressionStatement_strategy = st.builds(
    model_ExpressionStatement,
)
model_AssignmentStatement_strategy = st.builds(
    model_AssignmentStatement,
)
model_BreakStatement_strategy = st.builds(
    model_BreakStatement,
)
model_EmptyStatement_strategy = st.builds(
    model_EmptyStatement,
)
Action_strategy = st.builds(
    Action,
)
model_Statement_strategy = st.builds(
    model_Statement,
)
model_Action_strategy = st.builds(
    model_Action,
)
model_Block_strategy = st.builds(
    model_Block,
)
FunctionDeclaration_strategy = st.builds(
    FunctionDeclaration,
)
model_ProcedureDeclaration_strategy = st.builds(
    model_ProcedureDeclaration,
)

@given(instance=model_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_model_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, model_ParameterDeclaration)

@given(instance=model_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_model_constantdeclaration_instantiation(instance):
    assert isinstance(instance, model_ConstantDeclaration)

@given(instance=model_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_model_variabledeclaration_instantiation(instance):
    assert isinstance(instance, model_VariableDeclaration)

@given(instance=model_ReferenceExpression_strategy)
@settings(max_examples=50)
def test_model_referenceexpression_instantiation(instance):
    assert isinstance(instance, model_ReferenceExpression)

@given(instance=model_Expression_strategy)
@settings(max_examples=50)
def test_model_expression_instantiation(instance):
    assert isinstance(instance, model_Expression)

@given(instance=model_Branch_strategy)
@settings(max_examples=50)
def test_model_branch_instantiation(instance):
    assert isinstance(instance, model_Branch)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=model_ForStatement_strategy)
@settings(max_examples=50)
def test_model_forstatement_instantiation(instance):
    assert isinstance(instance, model_ForStatement)

@given(instance=model_SwitchStatement_strategy)
@settings(max_examples=50)
def test_model_switchstatement_instantiation(instance):
    assert isinstance(instance, model_SwitchStatement)

@given(instance=model_ChoiceStatement_strategy)
@settings(max_examples=50)
def test_model_choicestatement_instantiation(instance):
    assert isinstance(instance, model_ChoiceStatement)

@given(instance=model_ReturnStatement_strategy)
@settings(max_examples=50)
def test_model_returnstatement_instantiation(instance):
    assert isinstance(instance, model_ReturnStatement)

@given(instance=model_IfStatement_strategy)
@settings(max_examples=50)
def test_model_ifstatement_instantiation(instance):
    assert isinstance(instance, model_IfStatement)

@given(instance=model_ConstantDeclarationStatement_strategy)
@settings(max_examples=50)
def test_model_constantdeclarationstatement_instantiation(instance):
    assert isinstance(instance, model_ConstantDeclarationStatement)

@given(instance=model_VariableDeclarationStatement_strategy)
@settings(max_examples=50)
def test_model_variabledeclarationstatement_instantiation(instance):
    assert isinstance(instance, model_VariableDeclarationStatement)

@given(instance=model_ExpressionStatement_strategy)
@settings(max_examples=50)
def test_model_expressionstatement_instantiation(instance):
    assert isinstance(instance, model_ExpressionStatement)

@given(instance=model_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_model_assignmentstatement_instantiation(instance):
    assert isinstance(instance, model_AssignmentStatement)

@given(instance=model_BreakStatement_strategy)
@settings(max_examples=50)
def test_model_breakstatement_instantiation(instance):
    assert isinstance(instance, model_BreakStatement)

@given(instance=model_EmptyStatement_strategy)
@settings(max_examples=50)
def test_model_emptystatement_instantiation(instance):
    assert isinstance(instance, model_EmptyStatement)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=model_Statement_strategy)
@settings(max_examples=50)
def test_model_statement_instantiation(instance):
    assert isinstance(instance, model_Statement)

@given(instance=model_Action_strategy)
@settings(max_examples=50)
def test_model_action_instantiation(instance):
    assert isinstance(instance, model_Action)

@given(instance=model_Block_strategy)
@settings(max_examples=50)
def test_model_block_instantiation(instance):
    assert isinstance(instance, model_Block)

@given(instance=FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_functiondeclaration_instantiation(instance):
    assert isinstance(instance, FunctionDeclaration)

@given(instance=model_ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_model_proceduredeclaration_instantiation(instance):
    assert isinstance(instance, model_ProcedureDeclaration)
