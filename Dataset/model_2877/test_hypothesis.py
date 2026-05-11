import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    eol::statements::ModelDeclarationParameter,
    eol::statements::StringExpression,
    AnnotationStatement,
    eol::statements::ExecutableAnnotationStatement,
    eol::statements::SimpleAnnotationStatement,
    eol::statements::NameExpression,
    AssignmentStatement,
    eol::statements::SpecialAssignmentStatement,
    eol::statements::VariableDeclarationExpression,
    SwitchCaseStatement,
    eol::statements::ExpressionOrStatementBlock,
    eol::statements::SwitchCaseDefaultStatement,
    eol::statements::SwitchCaseExpressionStatement,
    eol::statements::Expression,
    Statement,
    eol::statements::AbortStatement,
    eol::statements::ThrowStatement,
    eol::statements::SwitchStatement,
    eol::statements::DeleteStatement,
    eol::statements::ContinueStatement,
    eol::statements::BreakAllStatement,
    eol::statements::AssignmentStatement,
    eol::statements::ReturnStatement,
    eol::statements::AnnotationStatement,
    eol::statements::SwitchCaseStatement,
    eol::statements::IfStatement,
    eol::statements::BreakStatement,
    eol::statements::WhileStatement,
    eol::statements::ModelDeclarationStatement,
    eol::statements::ExpressionStatement,
    eol::statements::Statement,
    eol::statements::FormalParameterExpression,
    eol::statements::ForStatement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ModelDeclarationParameter)


def test_eol::statements::modeldeclarationparameter_constructor_exists():
    assert callable(eol::statements::ModelDeclarationParameter.__init__)


def test_eol::statements::modeldeclarationparameter_constructor_args():
    sig = inspect.signature(eol::statements::ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::stringexpression_is_not_abstract():
    assert not inspect.isabstract(eol::statements::StringExpression)


def test_eol::statements::stringexpression_constructor_exists():
    assert callable(eol::statements::StringExpression.__init__)


def test_eol::statements::stringexpression_constructor_args():
    sig = inspect.signature(eol::statements::StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotationstatement_is_not_abstract():
    assert not inspect.isabstract(AnnotationStatement)


def test_annotationstatement_constructor_exists():
    assert callable(AnnotationStatement.__init__)


def test_annotationstatement_constructor_args():
    sig = inspect.signature(AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::executableannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ExecutableAnnotationStatement)


def test_eol::statements::executableannotationstatement_constructor_exists():
    assert callable(eol::statements::ExecutableAnnotationStatement.__init__)


def test_eol::statements::executableannotationstatement_constructor_args():
    sig = inspect.signature(eol::statements::ExecutableAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::simpleannotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SimpleAnnotationStatement)


def test_eol::statements::simpleannotationstatement_constructor_exists():
    assert callable(eol::statements::SimpleAnnotationStatement.__init__)


def test_eol::statements::simpleannotationstatement_constructor_args():
    sig = inspect.signature(eol::statements::SimpleAnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::nameexpression_is_not_abstract():
    assert not inspect.isabstract(eol::statements::NameExpression)


def test_eol::statements::nameexpression_constructor_exists():
    assert callable(eol::statements::NameExpression.__init__)


def test_eol::statements::nameexpression_constructor_args():
    sig = inspect.signature(eol::statements::NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SpecialAssignmentStatement)


def test_eol::statements::specialassignmentstatement_constructor_exists():
    assert callable(eol::statements::SpecialAssignmentStatement.__init__)


def test_eol::statements::specialassignmentstatement_constructor_args():
    sig = inspect.signature(eol::statements::SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(eol::statements::VariableDeclarationExpression)


def test_eol::statements::variabledeclarationexpression_constructor_exists():
    assert callable(eol::statements::VariableDeclarationExpression.__init__)


def test_eol::statements::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(eol::statements::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::expressionorstatementblock_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ExpressionOrStatementBlock)


def test_eol::statements::expressionorstatementblock_constructor_exists():
    assert callable(eol::statements::ExpressionOrStatementBlock.__init__)


def test_eol::statements::expressionorstatementblock_constructor_args():
    sig = inspect.signature(eol::statements::ExpressionOrStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SwitchCaseDefaultStatement)


def test_eol::statements::switchcasedefaultstatement_constructor_exists():
    assert callable(eol::statements::SwitchCaseDefaultStatement.__init__)


def test_eol::statements::switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(eol::statements::SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SwitchCaseExpressionStatement)


def test_eol::statements::switchcaseexpressionstatement_constructor_exists():
    assert callable(eol::statements::SwitchCaseExpressionStatement.__init__)


def test_eol::statements::switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(eol::statements::SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::expression_is_not_abstract():
    assert not inspect.isabstract(eol::statements::Expression)


def test_eol::statements::expression_constructor_exists():
    assert callable(eol::statements::Expression.__init__)


def test_eol::statements::expression_constructor_args():
    sig = inspect.signature(eol::statements::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::abortstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::AbortStatement)


def test_eol::statements::abortstatement_constructor_exists():
    assert callable(eol::statements::AbortStatement.__init__)


def test_eol::statements::abortstatement_constructor_args():
    sig = inspect.signature(eol::statements::AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::throwstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ThrowStatement)


def test_eol::statements::throwstatement_constructor_exists():
    assert callable(eol::statements::ThrowStatement.__init__)


def test_eol::statements::throwstatement_constructor_args():
    sig = inspect.signature(eol::statements::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::switchstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SwitchStatement)


def test_eol::statements::switchstatement_constructor_exists():
    assert callable(eol::statements::SwitchStatement.__init__)


def test_eol::statements::switchstatement_constructor_args():
    sig = inspect.signature(eol::statements::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::deletestatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::DeleteStatement)


def test_eol::statements::deletestatement_constructor_exists():
    assert callable(eol::statements::DeleteStatement.__init__)


def test_eol::statements::deletestatement_constructor_args():
    sig = inspect.signature(eol::statements::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::continuestatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ContinueStatement)


def test_eol::statements::continuestatement_constructor_exists():
    assert callable(eol::statements::ContinueStatement.__init__)


def test_eol::statements::continuestatement_constructor_args():
    sig = inspect.signature(eol::statements::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::breakallstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::BreakAllStatement)


def test_eol::statements::breakallstatement_constructor_exists():
    assert callable(eol::statements::BreakAllStatement.__init__)


def test_eol::statements::breakallstatement_constructor_args():
    sig = inspect.signature(eol::statements::BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::AssignmentStatement)


def test_eol::statements::assignmentstatement_constructor_exists():
    assert callable(eol::statements::AssignmentStatement.__init__)


def test_eol::statements::assignmentstatement_constructor_args():
    sig = inspect.signature(eol::statements::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::returnstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ReturnStatement)


def test_eol::statements::returnstatement_constructor_exists():
    assert callable(eol::statements::ReturnStatement.__init__)


def test_eol::statements::returnstatement_constructor_args():
    sig = inspect.signature(eol::statements::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::annotationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::AnnotationStatement)


def test_eol::statements::annotationstatement_constructor_exists():
    assert callable(eol::statements::AnnotationStatement.__init__)


def test_eol::statements::annotationstatement_constructor_args():
    sig = inspect.signature(eol::statements::AnnotationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::SwitchCaseStatement)


def test_eol::statements::switchcasestatement_constructor_exists():
    assert callable(eol::statements::SwitchCaseStatement.__init__)


def test_eol::statements::switchcasestatement_constructor_args():
    sig = inspect.signature(eol::statements::SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::ifstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::IfStatement)


def test_eol::statements::ifstatement_constructor_exists():
    assert callable(eol::statements::IfStatement.__init__)


def test_eol::statements::ifstatement_constructor_args():
    sig = inspect.signature(eol::statements::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::breakstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::BreakStatement)


def test_eol::statements::breakstatement_constructor_exists():
    assert callable(eol::statements::BreakStatement.__init__)


def test_eol::statements::breakstatement_constructor_args():
    sig = inspect.signature(eol::statements::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::whilestatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::WhileStatement)


def test_eol::statements::whilestatement_constructor_exists():
    assert callable(eol::statements::WhileStatement.__init__)


def test_eol::statements::whilestatement_constructor_args():
    sig = inspect.signature(eol::statements::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ModelDeclarationStatement)


def test_eol::statements::modeldeclarationstatement_constructor_exists():
    assert callable(eol::statements::ModelDeclarationStatement.__init__)


def test_eol::statements::modeldeclarationstatement_constructor_args():
    sig = inspect.signature(eol::statements::ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ExpressionStatement)


def test_eol::statements::expressionstatement_constructor_exists():
    assert callable(eol::statements::ExpressionStatement.__init__)


def test_eol::statements::expressionstatement_constructor_args():
    sig = inspect.signature(eol::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::statement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::Statement)


def test_eol::statements::statement_constructor_exists():
    assert callable(eol::statements::Statement.__init__)


def test_eol::statements::statement_constructor_args():
    sig = inspect.signature(eol::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(eol::statements::FormalParameterExpression)


def test_eol::statements::formalparameterexpression_constructor_exists():
    assert callable(eol::statements::FormalParameterExpression.__init__)


def test_eol::statements::formalparameterexpression_constructor_args():
    sig = inspect.signature(eol::statements::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_eol::statements::forstatement_is_not_abstract():
    assert not inspect.isabstract(eol::statements::ForStatement)


def test_eol::statements::forstatement_constructor_exists():
    assert callable(eol::statements::ForStatement.__init__)


def test_eol::statements::forstatement_constructor_args():
    sig = inspect.signature(eol::statements::ForStatement.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
eol::statements::ModelDeclarationParameter_strategy = st.builds(
    eol::statements::ModelDeclarationParameter,
)
eol::statements::StringExpression_strategy = st.builds(
    eol::statements::StringExpression,
)
AnnotationStatement_strategy = st.builds(
    AnnotationStatement,
)
eol::statements::ExecutableAnnotationStatement_strategy = st.builds(
    eol::statements::ExecutableAnnotationStatement,
)
eol::statements::SimpleAnnotationStatement_strategy = st.builds(
    eol::statements::SimpleAnnotationStatement,
)
eol::statements::NameExpression_strategy = st.builds(
    eol::statements::NameExpression,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
eol::statements::SpecialAssignmentStatement_strategy = st.builds(
    eol::statements::SpecialAssignmentStatement,
)
eol::statements::VariableDeclarationExpression_strategy = st.builds(
    eol::statements::VariableDeclarationExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
eol::statements::ExpressionOrStatementBlock_strategy = st.builds(
    eol::statements::ExpressionOrStatementBlock,
)
eol::statements::SwitchCaseDefaultStatement_strategy = st.builds(
    eol::statements::SwitchCaseDefaultStatement,
)
eol::statements::SwitchCaseExpressionStatement_strategy = st.builds(
    eol::statements::SwitchCaseExpressionStatement,
)
eol::statements::Expression_strategy = st.builds(
    eol::statements::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
eol::statements::AbortStatement_strategy = st.builds(
    eol::statements::AbortStatement,
)
eol::statements::ThrowStatement_strategy = st.builds(
    eol::statements::ThrowStatement,
)
eol::statements::SwitchStatement_strategy = st.builds(
    eol::statements::SwitchStatement,
)
eol::statements::DeleteStatement_strategy = st.builds(
    eol::statements::DeleteStatement,
)
eol::statements::ContinueStatement_strategy = st.builds(
    eol::statements::ContinueStatement,
)
eol::statements::BreakAllStatement_strategy = st.builds(
    eol::statements::BreakAllStatement,
)
eol::statements::AssignmentStatement_strategy = st.builds(
    eol::statements::AssignmentStatement,
)
eol::statements::ReturnStatement_strategy = st.builds(
    eol::statements::ReturnStatement,
)
eol::statements::AnnotationStatement_strategy = st.builds(
    eol::statements::AnnotationStatement,
)
eol::statements::SwitchCaseStatement_strategy = st.builds(
    eol::statements::SwitchCaseStatement,
)
eol::statements::IfStatement_strategy = st.builds(
    eol::statements::IfStatement,
)
eol::statements::BreakStatement_strategy = st.builds(
    eol::statements::BreakStatement,
)
eol::statements::WhileStatement_strategy = st.builds(
    eol::statements::WhileStatement,
)
eol::statements::ModelDeclarationStatement_strategy = st.builds(
    eol::statements::ModelDeclarationStatement,
)
eol::statements::ExpressionStatement_strategy = st.builds(
    eol::statements::ExpressionStatement,
)
eol::statements::Statement_strategy = st.builds(
    eol::statements::Statement,
)
eol::statements::FormalParameterExpression_strategy = st.builds(
    eol::statements::FormalParameterExpression,
)
eol::statements::ForStatement_strategy = st.builds(
    eol::statements::ForStatement,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=eol::statements::ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_eol::statements::modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, eol::statements::ModelDeclarationParameter)

@given(instance=eol::statements::StringExpression_strategy)
@settings(max_examples=50)
def test_eol::statements::stringexpression_instantiation(instance):
    assert isinstance(instance, eol::statements::StringExpression)

@given(instance=AnnotationStatement_strategy)
@settings(max_examples=50)
def test_annotationstatement_instantiation(instance):
    assert isinstance(instance, AnnotationStatement)

@given(instance=eol::statements::ExecutableAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::executableannotationstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ExecutableAnnotationStatement)

@given(instance=eol::statements::SimpleAnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::simpleannotationstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SimpleAnnotationStatement)

@given(instance=eol::statements::NameExpression_strategy)
@settings(max_examples=50)
def test_eol::statements::nameexpression_instantiation(instance):
    assert isinstance(instance, eol::statements::NameExpression)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=eol::statements::SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SpecialAssignmentStatement)

@given(instance=eol::statements::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_eol::statements::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, eol::statements::VariableDeclarationExpression)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=eol::statements::ExpressionOrStatementBlock_strategy)
@settings(max_examples=50)
def test_eol::statements::expressionorstatementblock_instantiation(instance):
    assert isinstance(instance, eol::statements::ExpressionOrStatementBlock)

@given(instance=eol::statements::SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SwitchCaseDefaultStatement)

@given(instance=eol::statements::SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SwitchCaseExpressionStatement)

@given(instance=eol::statements::Expression_strategy)
@settings(max_examples=50)
def test_eol::statements::expression_instantiation(instance):
    assert isinstance(instance, eol::statements::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=eol::statements::AbortStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::abortstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::AbortStatement)

@given(instance=eol::statements::ThrowStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::throwstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ThrowStatement)

@given(instance=eol::statements::SwitchStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::switchstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SwitchStatement)

@given(instance=eol::statements::DeleteStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::deletestatement_instantiation(instance):
    assert isinstance(instance, eol::statements::DeleteStatement)

@given(instance=eol::statements::ContinueStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::continuestatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ContinueStatement)

@given(instance=eol::statements::BreakAllStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::breakallstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::BreakAllStatement)

@given(instance=eol::statements::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::assignmentstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::AssignmentStatement)

@given(instance=eol::statements::ReturnStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::returnstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ReturnStatement)

@given(instance=eol::statements::AnnotationStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::annotationstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::AnnotationStatement)

@given(instance=eol::statements::SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::switchcasestatement_instantiation(instance):
    assert isinstance(instance, eol::statements::SwitchCaseStatement)

@given(instance=eol::statements::IfStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::ifstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::IfStatement)

@given(instance=eol::statements::BreakStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::breakstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::BreakStatement)

@given(instance=eol::statements::WhileStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::whilestatement_instantiation(instance):
    assert isinstance(instance, eol::statements::WhileStatement)

@given(instance=eol::statements::ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ModelDeclarationStatement)

@given(instance=eol::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ExpressionStatement)

@given(instance=eol::statements::Statement_strategy)
@settings(max_examples=50)
def test_eol::statements::statement_instantiation(instance):
    assert isinstance(instance, eol::statements::Statement)

@given(instance=eol::statements::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_eol::statements::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, eol::statements::FormalParameterExpression)

@given(instance=eol::statements::ForStatement_strategy)
@settings(max_examples=50)
def test_eol::statements::forstatement_instantiation(instance):
    assert isinstance(instance, eol::statements::ForStatement)
