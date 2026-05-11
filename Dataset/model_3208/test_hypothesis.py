import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Loop,
    hlp::ConditionalLoop,
    hlp::VariableDeclarationScope,
    BinaryExpression,
    hlp::ArithmeticExpression,
    UnaryExpression,
    hlp::UnaryMinusExpression,
    Expression,
    hlp::BinaryExpression,
    hlp::UnaryExpression,
    hlp::AtomicExpression,
    ArithmeticExpression,
    hlp::MultiplyExpression,
    hlp::DivideExpression,
    hlp::SubtractExpression,
    hlp::AddExpression,
    AtomicExpression,
    hlp::LiteralValue,
    hlp::Statement,
    hlp::VariableReference,
    Statement,
    hlp::SynchronizedStatement,
    hlp::Loop,
    hlp::Assignment,
    hlp::Condition,
    hlp::IfStatement,
    hlp::Block,
    hlp::ParenthesisExpression,
    hlp::Expression,
    hlp::VariableDeclaration,
    hlp::ScheduleInstruction,
    Nameable,
    hlp::Variable,
    VariableDeclarationScope,
    hlp::Task,
    hlp::HighLevelProgram,
    hlp::ExpressionStatement,
    hlp::Nameable,
    hlp::ForLoop,
    ConditionalLoop,
    hlp::WhileLoop,
    ComparisonOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_loop_is_not_abstract():
    assert not inspect.isabstract(Loop)


def test_loop_constructor_exists():
    assert callable(Loop.__init__)


def test_loop_constructor_args():
    sig = inspect.signature(Loop.__init__)
    params = list(sig.parameters.keys())



def test_hlp::conditionalloop_is_not_abstract():
    assert not inspect.isabstract(hlp::ConditionalLoop)


def test_hlp::conditionalloop_constructor_exists():
    assert callable(hlp::ConditionalLoop.__init__)


def test_hlp::conditionalloop_constructor_args():
    sig = inspect.signature(hlp::ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_hlp::variabledeclarationscope_is_not_abstract():
    assert not inspect.isabstract(hlp::VariableDeclarationScope)


def test_hlp::variabledeclarationscope_constructor_exists():
    assert callable(hlp::VariableDeclarationScope.__init__)


def test_hlp::variabledeclarationscope_constructor_args():
    sig = inspect.signature(hlp::VariableDeclarationScope.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::ArithmeticExpression)


def test_hlp::arithmeticexpression_constructor_exists():
    assert callable(hlp::ArithmeticExpression.__init__)


def test_hlp::arithmeticexpression_constructor_args():
    sig = inspect.signature(hlp::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::unaryminusexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::UnaryMinusExpression)


def test_hlp::unaryminusexpression_constructor_exists():
    assert callable(hlp::UnaryMinusExpression.__init__)


def test_hlp::unaryminusexpression_constructor_args():
    sig = inspect.signature(hlp::UnaryMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::BinaryExpression)


def test_hlp::binaryexpression_constructor_exists():
    assert callable(hlp::BinaryExpression.__init__)


def test_hlp::binaryexpression_constructor_args():
    sig = inspect.signature(hlp::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::UnaryExpression)


def test_hlp::unaryexpression_constructor_exists():
    assert callable(hlp::UnaryExpression.__init__)


def test_hlp::unaryexpression_constructor_args():
    sig = inspect.signature(hlp::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::atomicexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::AtomicExpression)


def test_hlp::atomicexpression_constructor_exists():
    assert callable(hlp::AtomicExpression.__init__)


def test_hlp::atomicexpression_constructor_args():
    sig = inspect.signature(hlp::AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::multiplyexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::MultiplyExpression)


def test_hlp::multiplyexpression_constructor_exists():
    assert callable(hlp::MultiplyExpression.__init__)


def test_hlp::multiplyexpression_constructor_args():
    sig = inspect.signature(hlp::MultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::divideexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::DivideExpression)


def test_hlp::divideexpression_constructor_exists():
    assert callable(hlp::DivideExpression.__init__)


def test_hlp::divideexpression_constructor_args():
    sig = inspect.signature(hlp::DivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::subtractexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::SubtractExpression)


def test_hlp::subtractexpression_constructor_exists():
    assert callable(hlp::SubtractExpression.__init__)


def test_hlp::subtractexpression_constructor_args():
    sig = inspect.signature(hlp::SubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::addexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::AddExpression)


def test_hlp::addexpression_constructor_exists():
    assert callable(hlp::AddExpression.__init__)


def test_hlp::addexpression_constructor_args():
    sig = inspect.signature(hlp::AddExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicexpression_is_not_abstract():
    assert not inspect.isabstract(AtomicExpression)


def test_atomicexpression_constructor_exists():
    assert callable(AtomicExpression.__init__)


def test_atomicexpression_constructor_args():
    sig = inspect.signature(AtomicExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::literalvalue_is_not_abstract():
    assert not inspect.isabstract(hlp::LiteralValue)


def test_hlp::literalvalue_constructor_exists():
    assert callable(hlp::LiteralValue.__init__)


def test_hlp::literalvalue_constructor_args():
    sig = inspect.signature(hlp::LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "rawValue" in params, "Missing parameter 'rawValue'"

def test_hlp::literalvalue_has_rawValue():
    assert hasattr(hlp::LiteralValue, "rawValue")
    descriptor = None
    for klass in hlp::LiteralValue.__mro__:
        if "rawValue" in klass.__dict__:
            descriptor = klass.__dict__["rawValue"]
            break
    assert isinstance(descriptor, property)



def test_hlp::statement_is_not_abstract():
    assert not inspect.isabstract(hlp::Statement)


def test_hlp::statement_constructor_exists():
    assert callable(hlp::Statement.__init__)


def test_hlp::statement_constructor_args():
    sig = inspect.signature(hlp::Statement.__init__)
    params = list(sig.parameters.keys())



def test_hlp::variablereference_is_not_abstract():
    assert not inspect.isabstract(hlp::VariableReference)


def test_hlp::variablereference_constructor_exists():
    assert callable(hlp::VariableReference.__init__)


def test_hlp::variablereference_constructor_args():
    sig = inspect.signature(hlp::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hlp::synchronizedstatement_is_not_abstract():
    assert not inspect.isabstract(hlp::SynchronizedStatement)


def test_hlp::synchronizedstatement_constructor_exists():
    assert callable(hlp::SynchronizedStatement.__init__)


def test_hlp::synchronizedstatement_constructor_args():
    sig = inspect.signature(hlp::SynchronizedStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp::loop_is_not_abstract():
    assert not inspect.isabstract(hlp::Loop)


def test_hlp::loop_constructor_exists():
    assert callable(hlp::Loop.__init__)


def test_hlp::loop_constructor_args():
    sig = inspect.signature(hlp::Loop.__init__)
    params = list(sig.parameters.keys())



def test_hlp::assignment_is_not_abstract():
    assert not inspect.isabstract(hlp::Assignment)


def test_hlp::assignment_constructor_exists():
    assert callable(hlp::Assignment.__init__)


def test_hlp::assignment_constructor_args():
    sig = inspect.signature(hlp::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_hlp::condition_is_not_abstract():
    assert not inspect.isabstract(hlp::Condition)


def test_hlp::condition_constructor_exists():
    assert callable(hlp::Condition.__init__)


def test_hlp::condition_constructor_args():
    sig = inspect.signature(hlp::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_hlp::condition_has_operator():
    assert hasattr(hlp::Condition, "operator")
    descriptor = None
    for klass in hlp::Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_hlp::ifstatement_is_not_abstract():
    assert not inspect.isabstract(hlp::IfStatement)


def test_hlp::ifstatement_constructor_exists():
    assert callable(hlp::IfStatement.__init__)


def test_hlp::ifstatement_constructor_args():
    sig = inspect.signature(hlp::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp::block_is_not_abstract():
    assert not inspect.isabstract(hlp::Block)


def test_hlp::block_constructor_exists():
    assert callable(hlp::Block.__init__)


def test_hlp::block_constructor_args():
    sig = inspect.signature(hlp::Block.__init__)
    params = list(sig.parameters.keys())



def test_hlp::parenthesisexpression_is_not_abstract():
    assert not inspect.isabstract(hlp::ParenthesisExpression)


def test_hlp::parenthesisexpression_constructor_exists():
    assert callable(hlp::ParenthesisExpression.__init__)


def test_hlp::parenthesisexpression_constructor_args():
    sig = inspect.signature(hlp::ParenthesisExpression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::expression_is_not_abstract():
    assert not inspect.isabstract(hlp::Expression)


def test_hlp::expression_constructor_exists():
    assert callable(hlp::Expression.__init__)


def test_hlp::expression_constructor_args():
    sig = inspect.signature(hlp::Expression.__init__)
    params = list(sig.parameters.keys())



def test_hlp::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(hlp::VariableDeclaration)


def test_hlp::variabledeclaration_constructor_exists():
    assert callable(hlp::VariableDeclaration.__init__)


def test_hlp::variabledeclaration_constructor_args():
    sig = inspect.signature(hlp::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hlp::scheduleinstruction_is_not_abstract():
    assert not inspect.isabstract(hlp::ScheduleInstruction)


def test_hlp::scheduleinstruction_constructor_exists():
    assert callable(hlp::ScheduleInstruction.__init__)


def test_hlp::scheduleinstruction_constructor_args():
    sig = inspect.signature(hlp::ScheduleInstruction.__init__)
    params = list(sig.parameters.keys())



def test_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_hlp::variable_is_not_abstract():
    assert not inspect.isabstract(hlp::Variable)


def test_hlp::variable_constructor_exists():
    assert callable(hlp::Variable.__init__)


def test_hlp::variable_constructor_args():
    sig = inspect.signature(hlp::Variable.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclarationscope_is_not_abstract():
    assert not inspect.isabstract(VariableDeclarationScope)


def test_variabledeclarationscope_constructor_exists():
    assert callable(VariableDeclarationScope.__init__)


def test_variabledeclarationscope_constructor_args():
    sig = inspect.signature(VariableDeclarationScope.__init__)
    params = list(sig.parameters.keys())



def test_hlp::task_is_not_abstract():
    assert not inspect.isabstract(hlp::Task)


def test_hlp::task_constructor_exists():
    assert callable(hlp::Task.__init__)


def test_hlp::task_constructor_args():
    sig = inspect.signature(hlp::Task.__init__)
    params = list(sig.parameters.keys())



def test_hlp::highlevelprogram_is_not_abstract():
    assert not inspect.isabstract(hlp::HighLevelProgram)


def test_hlp::highlevelprogram_constructor_exists():
    assert callable(hlp::HighLevelProgram.__init__)


def test_hlp::highlevelprogram_constructor_args():
    sig = inspect.signature(hlp::HighLevelProgram.__init__)
    params = list(sig.parameters.keys())



def test_hlp::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(hlp::ExpressionStatement)


def test_hlp::expressionstatement_constructor_exists():
    assert callable(hlp::ExpressionStatement.__init__)


def test_hlp::expressionstatement_constructor_args():
    sig = inspect.signature(hlp::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_hlp::nameable_is_not_abstract():
    assert not inspect.isabstract(hlp::Nameable)


def test_hlp::nameable_constructor_exists():
    assert callable(hlp::Nameable.__init__)


def test_hlp::nameable_constructor_args():
    sig = inspect.signature(hlp::Nameable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hlp::nameable_has_name():
    assert hasattr(hlp::Nameable, "name")
    descriptor = None
    for klass in hlp::Nameable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hlp::forloop_is_not_abstract():
    assert not inspect.isabstract(hlp::ForLoop)


def test_hlp::forloop_constructor_exists():
    assert callable(hlp::ForLoop.__init__)


def test_hlp::forloop_constructor_args():
    sig = inspect.signature(hlp::ForLoop.__init__)
    params = list(sig.parameters.keys())
    assert "incrementing" in params, "Missing parameter 'incrementing'"

def test_hlp::forloop_has_incrementing():
    assert hasattr(hlp::ForLoop, "incrementing")
    descriptor = None
    for klass in hlp::ForLoop.__mro__:
        if "incrementing" in klass.__dict__:
            descriptor = klass.__dict__["incrementing"]
            break
    assert isinstance(descriptor, property)



def test_conditionalloop_is_not_abstract():
    assert not inspect.isabstract(ConditionalLoop)


def test_conditionalloop_constructor_exists():
    assert callable(ConditionalLoop.__init__)


def test_conditionalloop_constructor_args():
    sig = inspect.signature(ConditionalLoop.__init__)
    params = list(sig.parameters.keys())



def test_hlp::whileloop_is_not_abstract():
    assert not inspect.isabstract(hlp::WhileLoop)


def test_hlp::whileloop_constructor_exists():
    assert callable(hlp::WhileLoop.__init__)


def test_hlp::whileloop_constructor_args():
    sig = inspect.signature(hlp::WhileLoop.__init__)
    params = list(sig.parameters.keys())

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "GREATER_THAN",
        "EQUAL",
        "LESS_THAN_OR_EQUAL",
        "LESS_THAN",
        "UNEQUAL",
        "GREATER_THAN_OR_EQUAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"


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
Loop_strategy = st.builds(
    Loop,
)
hlp::ConditionalLoop_strategy = st.builds(
    hlp::ConditionalLoop,
)
hlp::VariableDeclarationScope_strategy = st.builds(
    hlp::VariableDeclarationScope,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
hlp::ArithmeticExpression_strategy = st.builds(
    hlp::ArithmeticExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
hlp::UnaryMinusExpression_strategy = st.builds(
    hlp::UnaryMinusExpression,
)
Expression_strategy = st.builds(
    Expression,
)
hlp::BinaryExpression_strategy = st.builds(
    hlp::BinaryExpression,
)
hlp::UnaryExpression_strategy = st.builds(
    hlp::UnaryExpression,
)
hlp::AtomicExpression_strategy = st.builds(
    hlp::AtomicExpression,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
hlp::MultiplyExpression_strategy = st.builds(
    hlp::MultiplyExpression,
)
hlp::DivideExpression_strategy = st.builds(
    hlp::DivideExpression,
)
hlp::SubtractExpression_strategy = st.builds(
    hlp::SubtractExpression,
)
hlp::AddExpression_strategy = st.builds(
    hlp::AddExpression,
)
AtomicExpression_strategy = st.builds(
    AtomicExpression,
)
hlp::LiteralValue_strategy = st.builds(
    hlp::LiteralValue,
    rawValue=
        safe_text
)
hlp::Statement_strategy = st.builds(
    hlp::Statement,
)
hlp::VariableReference_strategy = st.builds(
    hlp::VariableReference,
)
Statement_strategy = st.builds(
    Statement,
)
hlp::SynchronizedStatement_strategy = st.builds(
    hlp::SynchronizedStatement,
)
hlp::Loop_strategy = st.builds(
    hlp::Loop,
)
hlp::Assignment_strategy = st.builds(
    hlp::Assignment,
)
hlp::Condition_strategy = st.builds(
    hlp::Condition,
    operator=
        safe_text
)
hlp::IfStatement_strategy = st.builds(
    hlp::IfStatement,
)
hlp::Block_strategy = st.builds(
    hlp::Block,
)
hlp::ParenthesisExpression_strategy = st.builds(
    hlp::ParenthesisExpression,
)
hlp::Expression_strategy = st.builds(
    hlp::Expression,
)
hlp::VariableDeclaration_strategy = st.builds(
    hlp::VariableDeclaration,
)
hlp::ScheduleInstruction_strategy = st.builds(
    hlp::ScheduleInstruction,
)
Nameable_strategy = st.builds(
    Nameable,
)
hlp::Variable_strategy = st.builds(
    hlp::Variable,
)
VariableDeclarationScope_strategy = st.builds(
    VariableDeclarationScope,
)
hlp::Task_strategy = st.builds(
    hlp::Task,
)
hlp::HighLevelProgram_strategy = st.builds(
    hlp::HighLevelProgram,
)
hlp::ExpressionStatement_strategy = st.builds(
    hlp::ExpressionStatement,
)
hlp::Nameable_strategy = st.builds(
    hlp::Nameable,
    name=
        safe_text
)
hlp::ForLoop_strategy = st.builds(
    hlp::ForLoop,
    incrementing=
        st.booleans()
)
ConditionalLoop_strategy = st.builds(
    ConditionalLoop,
)
hlp::WhileLoop_strategy = st.builds(
    hlp::WhileLoop,
)

@given(instance=Loop_strategy)
@settings(max_examples=50)
def test_loop_instantiation(instance):
    assert isinstance(instance, Loop)

@given(instance=hlp::ConditionalLoop_strategy)
@settings(max_examples=50)
def test_hlp::conditionalloop_instantiation(instance):
    assert isinstance(instance, hlp::ConditionalLoop)

@given(instance=hlp::VariableDeclarationScope_strategy)
@settings(max_examples=50)
def test_hlp::variabledeclarationscope_instantiation(instance):
    assert isinstance(instance, hlp::VariableDeclarationScope)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=hlp::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_hlp::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, hlp::ArithmeticExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=hlp::UnaryMinusExpression_strategy)
@settings(max_examples=50)
def test_hlp::unaryminusexpression_instantiation(instance):
    assert isinstance(instance, hlp::UnaryMinusExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=hlp::BinaryExpression_strategy)
@settings(max_examples=50)
def test_hlp::binaryexpression_instantiation(instance):
    assert isinstance(instance, hlp::BinaryExpression)

@given(instance=hlp::UnaryExpression_strategy)
@settings(max_examples=50)
def test_hlp::unaryexpression_instantiation(instance):
    assert isinstance(instance, hlp::UnaryExpression)

@given(instance=hlp::AtomicExpression_strategy)
@settings(max_examples=50)
def test_hlp::atomicexpression_instantiation(instance):
    assert isinstance(instance, hlp::AtomicExpression)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=hlp::MultiplyExpression_strategy)
@settings(max_examples=50)
def test_hlp::multiplyexpression_instantiation(instance):
    assert isinstance(instance, hlp::MultiplyExpression)

@given(instance=hlp::DivideExpression_strategy)
@settings(max_examples=50)
def test_hlp::divideexpression_instantiation(instance):
    assert isinstance(instance, hlp::DivideExpression)

@given(instance=hlp::SubtractExpression_strategy)
@settings(max_examples=50)
def test_hlp::subtractexpression_instantiation(instance):
    assert isinstance(instance, hlp::SubtractExpression)

@given(instance=hlp::AddExpression_strategy)
@settings(max_examples=50)
def test_hlp::addexpression_instantiation(instance):
    assert isinstance(instance, hlp::AddExpression)

@given(instance=AtomicExpression_strategy)
@settings(max_examples=50)
def test_atomicexpression_instantiation(instance):
    assert isinstance(instance, AtomicExpression)

@given(instance=hlp::LiteralValue_strategy)
@settings(max_examples=50)
def test_hlp::literalvalue_instantiation(instance):
    assert isinstance(instance, hlp::LiteralValue)

@given(instance=hlp::LiteralValue_strategy)
def test_hlp::literalvalue_rawValue_type(instance):
    assert isinstance(instance.rawValue, str)


@given(instance=hlp::LiteralValue_strategy)
def test_hlp::literalvalue_rawValue_setter(instance):
    original = instance.rawValue
    instance.rawValue = original
    assert instance.rawValue == original

@given(instance=hlp::Statement_strategy)
@settings(max_examples=50)
def test_hlp::statement_instantiation(instance):
    assert isinstance(instance, hlp::Statement)

@given(instance=hlp::VariableReference_strategy)
@settings(max_examples=50)
def test_hlp::variablereference_instantiation(instance):
    assert isinstance(instance, hlp::VariableReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=hlp::SynchronizedStatement_strategy)
@settings(max_examples=50)
def test_hlp::synchronizedstatement_instantiation(instance):
    assert isinstance(instance, hlp::SynchronizedStatement)

@given(instance=hlp::Loop_strategy)
@settings(max_examples=50)
def test_hlp::loop_instantiation(instance):
    assert isinstance(instance, hlp::Loop)

@given(instance=hlp::Assignment_strategy)
@settings(max_examples=50)
def test_hlp::assignment_instantiation(instance):
    assert isinstance(instance, hlp::Assignment)

@given(instance=hlp::Condition_strategy)
@settings(max_examples=50)
def test_hlp::condition_instantiation(instance):
    assert isinstance(instance, hlp::Condition)

@given(instance=hlp::Condition_strategy)
def test_hlp::condition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=hlp::Condition_strategy)
def test_hlp::condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=hlp::IfStatement_strategy)
@settings(max_examples=50)
def test_hlp::ifstatement_instantiation(instance):
    assert isinstance(instance, hlp::IfStatement)

@given(instance=hlp::Block_strategy)
@settings(max_examples=50)
def test_hlp::block_instantiation(instance):
    assert isinstance(instance, hlp::Block)

@given(instance=hlp::ParenthesisExpression_strategy)
@settings(max_examples=50)
def test_hlp::parenthesisexpression_instantiation(instance):
    assert isinstance(instance, hlp::ParenthesisExpression)

@given(instance=hlp::Expression_strategy)
@settings(max_examples=50)
def test_hlp::expression_instantiation(instance):
    assert isinstance(instance, hlp::Expression)

@given(instance=hlp::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_hlp::variabledeclaration_instantiation(instance):
    assert isinstance(instance, hlp::VariableDeclaration)

@given(instance=hlp::ScheduleInstruction_strategy)
@settings(max_examples=50)
def test_hlp::scheduleinstruction_instantiation(instance):
    assert isinstance(instance, hlp::ScheduleInstruction)

@given(instance=Nameable_strategy)
@settings(max_examples=50)
def test_nameable_instantiation(instance):
    assert isinstance(instance, Nameable)

@given(instance=hlp::Variable_strategy)
@settings(max_examples=50)
def test_hlp::variable_instantiation(instance):
    assert isinstance(instance, hlp::Variable)

@given(instance=VariableDeclarationScope_strategy)
@settings(max_examples=50)
def test_variabledeclarationscope_instantiation(instance):
    assert isinstance(instance, VariableDeclarationScope)

@given(instance=hlp::Task_strategy)
@settings(max_examples=50)
def test_hlp::task_instantiation(instance):
    assert isinstance(instance, hlp::Task)

@given(instance=hlp::HighLevelProgram_strategy)
@settings(max_examples=50)
def test_hlp::highlevelprogram_instantiation(instance):
    assert isinstance(instance, hlp::HighLevelProgram)

@given(instance=hlp::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_hlp::expressionstatement_instantiation(instance):
    assert isinstance(instance, hlp::ExpressionStatement)

@given(instance=hlp::Nameable_strategy)
@settings(max_examples=50)
def test_hlp::nameable_instantiation(instance):
    assert isinstance(instance, hlp::Nameable)

@given(instance=hlp::Nameable_strategy)
def test_hlp::nameable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hlp::Nameable_strategy)
def test_hlp::nameable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hlp::ForLoop_strategy)
@settings(max_examples=50)
def test_hlp::forloop_instantiation(instance):
    assert isinstance(instance, hlp::ForLoop)

@given(instance=hlp::ForLoop_strategy)
def test_hlp::forloop_incrementing_type(instance):
    assert isinstance(instance.incrementing, bool)


@given(instance=hlp::ForLoop_strategy)
def test_hlp::forloop_incrementing_setter(instance):
    original = instance.incrementing
    instance.incrementing = original
    assert instance.incrementing == original

@given(instance=ConditionalLoop_strategy)
@settings(max_examples=50)
def test_conditionalloop_instantiation(instance):
    assert isinstance(instance, ConditionalLoop)

@given(instance=hlp::WhileLoop_strategy)
@settings(max_examples=50)
def test_hlp::whileloop_instantiation(instance):
    assert isinstance(instance, hlp::WhileLoop)
